/**
 * MedScan Content Script
 * Scans web pages for medical misinformation
 */

(function() {
  'use strict';
  
  // ========== CONFIG ==========
  const CONFIG = {
    enabled: true,
    autoScan: true,
    minTextLength: 30,
    scanDelay: 1500, // ms after page load
    overlayDuration: 8000 // ms to show overlay
  };
  
  // ========== STATE ==========
  let isScanning = false;
  let overlays = [];
  
  // ========== INIT ==========
  function init() {
    // Load settings
    chrome.storage.local.get('settings', (result) => {
      if (result.settings) {
        Object.assign(CONFIG, result.settings);
      }
      
      if (CONFIG.autoScan) {
        setTimeout(scanPage, CONFIG.scanDelay);
      }
    });
    
    // Listen for messages from background
    chrome.runtime.onMessage.addListener((request, sender, sendResponse) => {
      if (request.type === 'SHOW_VERDICT') {
        showVerdictOverlay(request.results);
        sendResponse({ received: true });
      }
      if (request.type === 'TOGGLE_SCAN') {
        CONFIG.enabled = !CONFIG.enabled;
        chrome.storage.local.set({ settings: CONFIG });
        sendResponse({ enabled: CONFIG.enabled });
      }
      return true;
    });
    
    // Scan on significant DOM changes
    const observer = new MutationObserver((mutations) => {
      if (CONFIG.enabled && !isScanning) {
        const hasNewText = mutations.some(m => 
          m.addedNodes.length > 0 && 
          Array.from(m.addedNodes).some(n => n.textContent && n.textContent.length > CONFIG.minTextLength)
        );
        if (hasNewText) {
          setTimeout(scanPage, 2000);
        }
      }
    });
    
    observer.observe(document.body, { childList: true, subtree: true });
  }
  
  // ========== SCANNER ==========
  function scanPage() {
    if (isScanning || !CONFIG.enabled) return;
    isScanning = true;
    
    // Extract text content from page
    const textBlocks = extractTextBlocks();
    
    if (textBlocks.length === 0) {
      isScanning = false;
      return;
    }
    
    // Scan each block
    let foundClaims = 0;
    
    for (const block of textBlocks) {
      if (block.text.length < CONFIG.minTextLength) continue;
      
      chrome.runtime.sendMessage(
        { type: 'SCAN_TEXT', text: block.text },
        (response) => {
          if (chrome.runtime.lastError) return;
          if (!response || !response.results) return;
          
          const { verified, potential } = response.results;
          
          if (verified.length > 0) {
            foundClaims += verified.length;
            highlightBlock(block.element, verified);
          }
          
          if (potential.length > 0 && verified.length === 0) {
            // Only show potential claims if no verified matches
            foundClaims += potential.length;
          }
        }
      );
    }
    
    // Reset scanning state
    setTimeout(() => { isScanning = false; }, 3000);
  }
  
  // ========== TEXT EXTRACTION ==========
  function extractTextBlocks() {
    const blocks = [];
    const selectors = [
      'p', 'article', 'section', 'div', 'li', 'h1', 'h2', 'h3', 'h4',
      'blockquote', 'span', 'td', 'th', 'figcaption', 'aside'
    ];
    
    const elements = document.querySelectorAll(selectors.join(', '));
    
    for (const el of elements) {
      // Skip hidden elements
      if (el.offsetParent === null && el.tagName !== 'BODY') continue;
      if (el.closest('.medscan-overlay')) continue; // Skip our own overlays
      
      const text = el.textContent.trim();
      if (text.length >= CONFIG.minTextLength && text.length < 5000) {
        blocks.push({ element: el, text });
      }
    }
    
    // Deduplicate (parent often contains child text)
    const unique = [];
    const seen = new Set();
    
    for (const block of blocks) {
      const hash = block.text.substring(0, 100);
      if (!seen.has(hash)) {
        seen.add(hash);
        unique.push(block);
      }
    }
    
    return unique.slice(0, 50); // Limit to prevent performance issues
  }
  
  // ========== HIGHLIGHTING ==========
  function highlightBlock(element, claims) {
    const severity = claims.some(c => c.severity === 'critical') ? 'critical' :
                     claims.some(c => c.severity === 'high') ? 'high' : 'medium';
    
    // Add border indicator
    element.style.borderLeft = `4px solid ${
      severity === 'critical' ? '#ef4444' :
      severity === 'high' ? '#f59e0b' : '#3b82f6'
    }`;
    element.style.paddingLeft = '12px';
    element.style.transition = 'all 0.3s ease';
    element.style.position = 'relative';
    
    // Add badge
    const badge = document.createElement('div');
    badge.className = 'medscan-badge';
    badge.innerHTML = `
      <span class="medscan-badge-icon">⚠️</span>
      <span class="medscan-badge-text">MedScan: ${claims.length} claim${claims.length > 1 ? 's' : ''}</span>
    `;
    badge.style.cssText = `
      position: absolute;
      top: -12px;
      right: 8px;
      background: ${severity === 'critical' ? '#ef4444' : severity === 'high' ? '#f59e0b' : '#3b82f6'};
      color: white;
      padding: 2px 8px;
      border-radius: 12px;
      font-size: 11px;
      font-family: -apple-system, BlinkMacSystemFont, sans-serif;
      cursor: pointer;
      z-index: 10000;
      box-shadow: 0 2px 8px rgba(0,0,0,0.2);
    `;
    
    badge.addEventListener('click', (e) => {
      e.stopPropagation();
      showVerdictOverlay({
        verified: claims,
        potential: [],
        originalText: element.textContent.substring(0, 200)
      });
    });
    
    element.style.position = 'relative';
    element.appendChild(badge);
    
    // Click to show details
    element.addEventListener('click', (e) => {
      if (e.target.closest('.medscan-badge')) return;
      showVerdictOverlay({
        verified: claims,
        potential: [],
        originalText: element.textContent.substring(0, 200)
      });
    }, { once: true });
  }
  
  // ========== VERDICT OVERLAY ==========
  function showVerdictOverlay(results) {
    // Remove existing overlays
    overlays.forEach(el => el.remove());
    overlays = [];
    
    const overlay = document.createElement('div');
    overlay.className = 'medscan-overlay';
    overlay.innerHTML = buildOverlayHTML(results);
    
    document.body.appendChild(overlay);
    overlays.push(overlay);
    
    // Animate in
    requestAnimationFrame(() => overlay.classList.add('medscan-visible'));
    
    // Close handlers
    overlay.querySelector('.medscan-close').addEventListener('click', () => {
      overlay.classList.remove('medscan-visible');
      setTimeout(() => overlay.remove(), 300);
    });
    
    // Auto-close
    setTimeout(() => {
      if (overlay.parentNode) {
        overlay.classList.remove('medscan-visible');
        setTimeout(() => overlay.remove(), 300);
      }
    }, CONFIG.overlayDuration);
  }
  
  function buildOverlayHTML(results) {
    const { verified, potential } = results;
    
    let html = `
      <div class="medscan-header">
        <div class="medscan-logo">🔍 MedScan</div>
        <button class="medscan-close">✕</button>
      </div>
      <div class="medscan-body">
    `;
    
    if (verified.length > 0) {
      for (const claim of verified) {
        const verdictColor = claim.verdict === 'false' ? '#ef4444' :
                            claim.verdict === 'misleading' ? '#f59e0b' : '#3b82f6';
        const verdictIcon = claim.verdict === 'false' ? '❌' :
                           claim.verdict === 'misleading' ? '⚠️' : 'ℹ️';
        const verdictLabel = claim.verdict === 'false' ? 'FALSE' :
                            claim.verdict === 'misleading' ? 'MISLEADING' : 'UNVERIFIED';
        
        html += `
          <div class="medscan-claim" style="border-left-color: ${verdictColor}">
            <div class="medscan-claim-header">
              <span class="medscan-verdict" style="background: ${verdictColor}">${verdictIcon} ${verdictLabel}</span>
              <span class="medscan-confidence">${Math.round(claim.confidence * 100)}% confidence</span>
            </div>
            <div class="medscan-matched">"${claim.matchedText}"</div>
            <div class="medscan-explanation">${claim.explanation}</div>
            <div class="medscan-sources">
              <strong>Sources:</strong>
              ${claim.sources.map(s => `<a href="${s.url}" target="_blank" class="medscan-source">${s.name}</a>`).join('')}
            </div>
            <div class="medscan-category">Category: ${claim.category} | Severity: ${claim.severity}</div>
          </div>
        `;
      }
    }
    
    if (potential.length > 0 && verified.length === 0) {
      html += `
        <div class="medscan-potential">
          <div class="medscan-potential-header">⚠️ Potential Medical Claims Detected</div>
          <div class="medscan-potential-text">
            We found patterns that look like medical claims. Always verify with trusted sources like WHO, CDC, or your doctor.
          </div>
          <div class="medscan-potential-claims">
            ${potential.map(p => `<div class="medscan-potential-claim">"${p.matchedText}"</div>`).join('')}
          </div>
        </div>
      `;
    }
    
    html += `
      </div>
      <div class="medscan-footer">
        <span>MedScan v1.0 — Always consult healthcare professionals</span>
        <a href="https://medscan.community" target="_blank" class="medscan-link">Learn more</a>
      </div>
    `;
    
    return html;
  }
  
  // ========== START ==========
  if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', init);
  } else {
    init();
  }
})();
