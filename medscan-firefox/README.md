# 🔍 MedScan — Medical Misinformation Detector

**Chrome Extension that detects medical misinformation in real-time and shows evidence-based verdicts from trusted sources.**

> 🌍 Protecting health, one scan at a time.

![MedScan Logo](icons/icon128.png)

## 🚀 Quick Install (Development)

### Step 1: Clone or Download

```bash
git clone https://github.com/medscan/community.git
# or just download the ZIP
```

### Step 2: Load in Chrome

1. Open Chrome and go to `chrome://extensions/`
2. Enable **Developer Mode** (toggle in top right)
3. Click **"Load unpacked"**
4. Select the `medscan-extension` folder
5. Done! 🎉

### Step 3: Test It

1. Visit any health article
2. MedScan will automatically scan for medical claims
3. Look for the ⚠️ badges on suspicious content
4. Click a badge to see the full verdict

## 🎯 Features

### 🛡️ Automatic Scanning
- Detects medical claims as you browse
- Highlights suspicious content with color-coded badges
- Red = False | Yellow = Misleading | Blue = Unverified

### 📊 Knowledge Base
Verified claims from trusted sources:
- **WHO** (World Health Organization)
- **CDC** (Centers for Disease Control)
- **NIH** (National Institutes of Health)
- **PubMed** peer-reviewed studies
- **FDA** (Food and Drug Administration)

### 🔍 Manual Scan
- Click the MedScan icon → "Scan Current Page"
- Right-click selected text → "MedScan: Analyze this text"
- Real-time verdict with sources

### 📈 Stats Dashboard
- Claims scanned count
- False claims found
- Misleading content detected
- Scan history with timestamps

### ⚙️ Settings
- Toggle auto-scan on/off
- Toggle badge visibility
- Clear scan history

## 🧪 What It Detects

### Categories

| Category | Examples |
|----------|----------|
| **Vaccines** | "Vaccines cause autism", "Microchips in vaccines" |
| **Cancer** | "Baking soda cures cancer", "Chemo is worse" |
| **COVID-19** | "Ivermectin cures COVID", "COVID is just the flu" |
| **Dangerous Remedies** | "MMS cures disease", "Colloidal silver cures" |
| **Mental Health** | "Depression is weakness", "Don't take antidepressants" |
| **Nutrition** | "Gluten causes autism", "Detox cleanses" |
| **Antibiotics** | "Antibiotics for the flu", "Antibiotics for prevention" |
| **Emergency** | "Don't call an ambulance", "Treat heart attack at home" |

### Verdicts

| Verdict | Meaning |
|---------|---------|
| ❌ **FALSE** | Scientifically disproven, consensus against |
| ⚠️ **MISLEADING** | Contains truth but distorted or exaggerated |
| ℹ️ **UNVERIFIED** | Not enough evidence to confirm or deny |

## 📁 Project Structure

```
medscan-extension/
├── manifest.json          # Chrome Extension manifest v3
├── popup.html             # Extension popup UI
├── popup.js               # Popup logic
├── icons/
│   ├── icon16.png         # 16x16 icon
│   ├── icon48.png         # 48x48 icon
│   └── icon128.png        # 128x128 icon
├── scripts/
│   ├── background.js      # Service worker
│   └── content.js         # Content script
├── styles/
│   ├── popup.css          # Popup styles
│   └── overlay.css        # Content overlay styles
├── data/
│   └── knowledge-base.js  # Medical claims database
└── README.md
```

## 🛠️ Development

### Add New Claims

Edit `data/knowledge-base.js`:

```javascript
{
  id: "NEW-001",
  patterns: [
    /your\s+regex\s+pattern/i
  ],
  verdict: "false",          // "false" | "misleading" | "unverified"
  confidence: 0.95,
  explanation: "Your explanation here.",
  sources: [
    { name: "Source Name", url: "https://source.url" }
  ],
  category: "category-name",
  severity: "high"           // "critical" | "high" | "medium" | "low"
}
```

### Testing

1. Load extension in Chrome (Developer Mode)
2. Visit health articles with known misinformation
3. Check console for scan logs
4. Verify overlay appears correctly

## 🌍 Contributing

We welcome contributions! Here's how:

1. **Add claims**: Submit PRs with new verified claims
2. **Translate**: Help translate to other languages
3. **Improve detection**: Enhance pattern matching
4. **Design**: Improve UI/UX
5. **Research**: Find new sources to include

### Claim Submission Format

```markdown
## Claim: [What the misinformation says]

**Verdict**: FALSE / MISLEADING / UNVERIFIED
**Category**: vaccines / cancer / covid / etc.
**Sources**:
- [Source 1](url)
- [Source 2](url)
**Explanation**: Why this is misinformation
```

## 📊 Impact

Every scan prevents misinformation from spreading. Help us protect:

- 🏥 Patients making health decisions
- 👨‍👩‍👧‍👦 Families researching treatments
- 🌐 Spanish-speaking communities (most affected)
- 📱 Mobile users in developing countries

## 🔒 Privacy

- **No data leaves your browser**
- All scans happen locally
- No tracking, no analytics, no telemetry
- History stored only in Chrome storage

## 📜 License

MIT License — Free forever, for everyone.

## 🙏 Acknowledgments

- WHO, CDC, NIH for trusted medical information
- The open source community
- Everyone fighting medical misinformation

---

**Made with ❤️ to protect health worldwide.**
