/**
 * MedScan Background Service Worker
 * Handles classification, storage, and messaging
 */

// Import knowledge base
importScripts('data/knowledge-base.js');

// ========== STATE ==========
let scanStats = {
  totalScanned: 0,
  claimsFound: 0,
  falseFound: 0,
  misleadingFound: 0,
  lastScan: null
};

// Load stats from storage
chrome.storage.local.get('scanStats', (result) => {
  if (result.scanStats) scanStats = result.scanStats;
});

// ========== MESSAGE HANDLER ==========
chrome.runtime.onMessage.addListener((request, sender, sendResponse) => {
  if (request.type === 'SCAN_TEXT') {
    const results = classifyText(request.text);
    sendResponse({ results });
    return true;
  }
  
  if (request.type === 'GET_STATS') {
    sendResponse({ stats: scanStats });
    return true;
  }
  
  if (request.type === 'RESET_STATS') {
    scanStats = { totalScanned: 0, claimsFound: 0, falseFound: 0, misleadingFound: 0, lastScan: null };
    chrome.storage.local.set({ scanStats });
    sendResponse({ stats: scanStats });
    return true;
  }

  if (request.type === 'GET_HISTORY') {
    chrome.storage.local.get('history', (result) => {
      sendResponse({ history: result.history || [] });
    });
    return true;
  }
});

// ========== CLASSIFICATION ENGINE ==========
function classifyText(text) {
  const results = [];
  const kb = window.MedScanKB.knowledgeBase;
  const patterns = window.MedScanKB.medicalPatterns;
  
  // Step 1: Check against knowledge base
  for (const entry of kb) {
    for (const pattern of entry.patterns) {
      const match = text.match(pattern);
      if (match) {
        results.push({
          id: entry.id,
          matchedText: match[0],
          verdict: entry.verdict,
          confidence: entry.confidence,
          explanation: entry.explanation,
          sources: entry.sources,
          category: entry.category,
          severity: entry.severity
        });
        break; // One match per knowledge entry
      }
    }
  }
  
  // Step 2: Detect potential medical claims (pattern-based)
  const potentialClaims = [];
  for (const pattern of patterns) {
    const matches = text.matchAll(pattern);
    for (const match of matches) {
      // Check if this match overlaps with a known KB match
      const overlaps = results.some(r => {
        const rIdx = text.indexOf(r.matchedText);
        const mIdx = match.index;
        return Math.abs(rIdx - mIdx) < 50;
      });
      
      if (!overlaps) {
        potentialClaims.push({
          matchedText: match[0],
          index: match.index,
          suggestion: 'This looks like a medical claim. Verify with trusted sources.'
        });
      }
    }
  }
  
  // Update stats
  if (results.length > 0 || potentialClaims.length > 0) {
    scanStats.claimsFound += results.length + potentialClaims.length;
    scanStats.falseFound += results.filter(r => r.verdict === 'false').length;
    scanStats.misleadingFound += results.filter(r => r.verdict === 'misleading').length;
    scanStats.lastScan = new Date().toISOString();
    chrome.storage.local.set({ scanStats });
    
    // Save to history
    saveToHistory(text, results, potentialClaims);
  }
  
  return {
    verified: results,
    potential: potentialClaims,
    scanTime: new Date().toISOString()
  };
}

// ========== HISTORY ==========
function saveToHistory(text, verified, potential) {
  chrome.storage.local.get('history', (result) => {
    const history = result.history || [];
    
    // Extract the most relevant snippet
    const snippet = text.length > 200 ? text.substring(0, 200) + '...' : text;
    
    const entry = {
      id: Date.now(),
      snippet,
      verifiedCount: verified.length,
      potentialCount: potential.length,
      falseCount: verified.filter(v => v.verdict === 'false').length,
      timestamp: new Date().toISOString()
    };
    
    history.unshift(entry);
    
    // Keep last 100 entries
    if (history.length > 100) history.pop();
    
    chrome.storage.local.set({ history });
  });
}

// ========== CONTEXT MENU ==========
chrome.runtime.onInstalled.addListener(() => {
  chrome.contextMenus.create({
    id: 'medscan-scan',
    title: '🔍 MedScan: Analyze this text',
    contexts: ['selection']
  });
});

chrome.contextMenus.onClicked.addListener((info, tab) => {
  if (info.menuItemId === 'medscan-scan' && info.selectionText) {
    const results = classifyText(info.selectionText);
    
    // Send results to content script for display
    chrome.tabs.sendMessage(tab.id, {
      type: 'SHOW_VERDICT',
      results: {
        verified: results.verified,
        potential: results.potential,
        originalText: info.selectionText
      }
    });
  }
});

// ========== ALARM: Daily reminder ==========
chrome.alarms.create('medscan-daily', { periodInMinutes: 1440 });
chrome.alarms.onAlarm.addListener((alarm) => {
  if (alarm.name === 'medscan-daily') {
    chrome.storage.local.get('scanStats', (result) => {
      const stats = result.scanStats || {};
      if (stats.claimsFound > 0) {
        console.log(`[MedScan] Daily: ${stats.claimsFound} claims scanned, ${stats.falseFound} false found`);
      }
    });
  }
});
