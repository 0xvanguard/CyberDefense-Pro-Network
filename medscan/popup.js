/**
 * MedScan Popup Script
 * Handles UI interactions and data display
 */

document.addEventListener('DOMContentLoaded', () => {
  loadStats();
  loadHistory();
  setupEventListeners();
});

// ========== LOAD STATS ==========
function loadStats() {
  chrome.runtime.sendMessage({ type: 'GET_STATS' }, (response) => {
    if (chrome.runtime.lastError || !response) return;
    
    const { stats } = response;
    document.getElementById('totalScanned').textContent = stats.claimsFound || 0;
    document.getElementById('falseFound').textContent = stats.falseFound || 0;
    document.getElementById('misleadingFound').textContent = stats.misleadingFound || 0;
  });
}

// ========== LOAD HISTORY ==========
function loadHistory() {
  chrome.runtime.sendMessage({ type: 'GET_HISTORY' }, (response) => {
    if (chrome.runtime.lastError || !response) return;
    
    const { history } = response;
    const list = document.getElementById('historyList');
    
    if (!history || history.length === 0) {
      list.innerHTML = `
        <div class="empty-state">
          <span class="empty-icon">📭</span>
          <p>No claims scanned yet</p>
        </div>
      `;
      return;
    }
    
    list.innerHTML = history.slice(0, 10).map(item => {
      const icon = item.falseCount > 0 ? '❌' : 
                   item.verifiedCount > 0 ? '⚠️' : '🔍';
      const time = formatTime(item.timestamp);
      
      return `
        <div class="history-item" data-id="${item.id}">
          <span class="history-icon">${icon}</span>
          <div class="history-info">
            <div class="history-snippet">${escapeHtml(item.snippet)}</div>
            <div class="history-meta">${item.verifiedCount + item.potentialCount} claims · ${time}</div>
          </div>
        </div>
      `;
    }).join('');
  });
}

// ========== EVENT LISTENERS ==========
function setupEventListeners() {
  // Scan button
  const scanBtn = document.getElementById('scanBtn');
  scanBtn.addEventListener('click', () => {
    scanBtn.classList.add('scanning');
    scanBtn.innerHTML = '<span class="scan-icon">⏳</span> Scanning...';
    
    // Get current tab
    chrome.tabs.query({ active: true, currentWindow: true }, (tabs) => {
      if (tabs[0]) {
        chrome.tabs.sendMessage(tabs[0].id, { type: 'TOGGLE_SCAN' }, (response) => {
          // Trigger scan
          chrome.tabs.sendMessage(tabs[0].id, { type: 'SCAN_PAGE' }, () => {
            setTimeout(() => {
              scanBtn.classList.remove('scanning');
              scanBtn.innerHTML = '<span class="scan-icon">⚡</span> Scan Current Page';
              loadStats();
              loadHistory();
            }, 2000);
          });
        });
      }
    });
  });
  
  // Clear history
  document.getElementById('clearHistory').addEventListener('click', () => {
    chrome.runtime.sendMessage({ type: 'RESET_STATS' }, () => {
      chrome.storage.local.set({ history: [] }, () => {
        loadStats();
        loadHistory();
      });
    });
  });
  
  // Auto-scan toggle
  document.getElementById('autoScan').addEventListener('change', (e) => {
    chrome.storage.local.get('settings', (result) => {
      const settings = result.settings || {};
      settings.autoScan = e.target.checked;
      chrome.storage.local.set({ settings });
    });
  });
  
  // Show badges toggle
  document.getElementById('showBadges').addEventListener('change', (e) => {
    chrome.storage.local.get('settings', (result) => {
      const settings = result.settings || {};
      settings.showBadges = e.target.checked;
      chrome.storage.local.set({ settings });
    });
  });
  
  // Load saved settings
  chrome.storage.local.get('settings', (result) => {
    if (result.settings) {
      document.getElementById('autoScan').checked = result.settings.autoScan !== false;
      document.getElementById('showBadges').checked = result.settings.showBadges !== false;
    }
  });
}

// ========== HELPERS ==========
function formatTime(isoString) {
  const date = new Date(isoString);
  const now = new Date();
  const diff = now - date;
  
  if (diff < 60000) return 'Just now';
  if (diff < 3600000) return `${Math.floor(diff / 60000)}m ago`;
  if (diff < 86400000) return `${Math.floor(diff / 3600000)}h ago`;
  return date.toLocaleDateString();
}

function escapeHtml(text) {
  const div = document.createElement('div');
  div.textContent = text;
  return div.innerHTML;
}
