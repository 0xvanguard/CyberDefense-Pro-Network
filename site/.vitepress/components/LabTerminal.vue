<template>
  <div class="lab-terminal-container">
    <!-- Header -->
    <div class="lab-header">
      <div class="lab-title">
        <span class="lab-icon">{{ icon }}</span>
        <h3>{{ title }}</h3>
      </div>
      <div class="lab-stats">
        <span class="stat">{{ currentStep + 1 }}/{{ steps.length }}</span>
        <span class="stat xp">{{ totalXP }} XP</span>
      </div>
    </div>

    <!-- Progress Bar -->
    <div class="progress-bar">
      <div class="progress-fill" :style="{ width: progressPercent + '%' }"></div>
    </div>

    <!-- Step Info -->
    <div class="step-info" v-if="currentStep < steps.length">
      <div class="step-badge">Paso {{ currentStep + 1 }}</div>
      <h4>{{ steps[currentStep].title }}</h4>
      <p>{{ steps[currentStep].description }}</p>
    </div>

    <!-- Terminal -->
    <div class="terminal" ref="terminalRef">
      <div class="terminal-header">
        <div class="terminal-dots">
          <span class="dot red"></span>
          <span class="dot yellow"></span>
          <span class="dot green"></span>
        </div>
        <span class="terminal-title">terminal@lab ~ $</span>
      </div>
      <div class="terminal-body" ref="terminalBody">
        <div class="welcome-msg">
          <span class="prompt-char">🌐</span> <span class="text-cyan">CyberDefense Pro Network — Lab Interactivo</span><br>
          <span class="text-dim">Escribe <span class="text-yellow">hint</span> si necesitas ayuda | <span class="text-yellow">clear</span> para limpiar | <span class="text-yellow">next</span> para avanzar</span>
        </div>
        
        <!-- Command history -->
        <div v-for="(entry, i) in history" :key="i" class="history-entry">
          <div class="command-line">
            <span class="prompt">⚡ {{ username }}@lab:~$</span>
            <span class="command">{{ entry.command }}</span>
          </div>
          <div class="output" v-html="entry.output"></div>
        </div>

        <!-- Current input -->
        <div class="input-line" v-if="!completed">
          <span class="prompt">⚡ {{ username }}@lab:~$</span>
          <input
            ref="inputRef"
            v-model="userInput"
            @keydown.enter="processCommand"
            @keydown.up="historyUp"
            @keydown.down="historyDown"
            class="terminal-input"
            :placeholder="currentStep < steps.length ? steps[currentStep].placeholder : ''"
            autocomplete="off"
            spellcheck="false"
          />
        </div>

        <!-- Completed message -->
        <div v-if="completed" class="completed-msg">
          <span class="text-green">✅ ¡Lab completado!</span> +{{ totalXP }} XP ganados<br>
          <span class="text-dim">Puedes seguir experimentando en la terminal.</span>
        </div>
      </div>
    </div>

    <!-- IOC / Findings Panel -->
    <div class="findings-panel" v-if="findings.length > 0">
      <h4>🔍 Hallazgos</h4>
      <div class="finding" v-for="(f, i) in findings" :key="i">
        <span class="finding-type" :class="'type-' + f.type">{{ f.type.toUpperCase() }}</span>
        <span class="finding-text">{{ f.text }}</span>
      </div>
    </div>

    <!-- Hints Panel -->
    <div class="hints-panel" v-if="showHint && currentStep < steps.length">
      <span class="hint-icon">💡</span>
      <span>{{ steps[currentStep].hint }}</span>
    </div>
  </div>
</template>

<script setup>
import { ref, computed, onMounted, nextTick, watch } from 'vue'

const props = defineProps({
  title: { type: String, default: 'Lab Interactivo' },
  icon: { type: String, default: '🧪' },
  username: { type: String, default: 'hacker' },
  steps: {
    type: Array,
    default: () => []
  },
  stepsJson: {
    type: String,
    default: ''
  }
})

// Parse stepsJson if steps is empty
const parsedSteps = computed(() => {
  if (props.steps && props.steps.length > 0) return props.steps
  if (props.stepsJson) {
    try {
      return JSON.parse(props.stepsJson)
    } catch(e) {
      console.error('Failed to parse stepsJson:', e)
      return []
    }
  }
  return []
})

const terminalRef = ref(null)
const terminalBody = ref(null)
const inputRef = ref(null)
const userInput = ref('')
const history = ref([])
const commandHistory = ref([])
const historyIndex = ref(-1)
const currentStep = ref(0)
const completed = ref(false)
const findings = ref([])
const showHint = ref(false)

const totalXP = computed(() => {
  let xp = 0
  for (let i = 0; i < currentStep.value; i++) {
    xp += props.steps[i]?.xp || 0
  }
  return xp
})

const progressPercent = computed(() => {
  return Math.round((currentStep.value / props.steps.length) * 100)
})

function processCommand() {
  const cmd = userInput.value.trim()
  if (!cmd) return
  
  showHint.value = false
  commandHistory.value.push(cmd)
  historyIndex.value = commandHistory.value.length
  
  const step = props.steps[currentStep.value]
  let output = ''
  let found = false
  
  if (cmd === 'hint') {
    showHint.value = true
    output = '<span class="text-yellow">💡 Hint: ' + (step?.hint || 'No hay hint disponible') + '</span>'
  } else if (cmd === 'clear') {
    history.value = []
    userInput.value = ''
    return
  } else if (cmd === 'next') {
    if (step) {
      output = '<span class="text-green">✅ Paso ' + (currentStep.value + 1) + ' completado (+' + step.xp + ' XP)</span>'
      if (step.finding) {
        findings.value.push(step.finding)
      }
      currentStep.value++
      if (currentStep.value >= props.steps.length) {
        completed.value = true
      }
    }
  } else if (cmd === 'help') {
    output = '<span class="text-cyan">Comandos disponibles:</span>\n' +
             '<span class="text-dim">  hint     — Mostrar hint del paso actual</span>\n' +
             '<span class="text-dim">  clear    — Limpiar terminal</span>\n' +
             '<span class="text-dim">  next     — Avanzar al siguiente paso</span>\n' +
             '<span class="text-dim">  help     — Mostrar esta ayuda</span>\n' +
             '<span class="text-dim">  findings — Ver hallazgos</span>'
  } else if (cmd === 'findings') {
    if (findings.value.length === 0) {
      output = '<span class="text-dim">Aún no hay hallazgos. Completa los pasos para descubrirlos.</span>'
    } else {
      output = '<span class="text-cyan">🔍 Hallazgos:</span>\n' +
               findings.value.map(f => '<span class="text-yellow">[' + f.type.toUpperCase() + ']</span> ' + f.text).join('\n')
    }
  } else if (step && step.commands) {
    // Check if command matches any valid command for this step
    const validCmds = Array.isArray(step.commands) ? step.commands : [step.commands]
    for (const vc of validCmds) {
      if (typeof vc === 'string' && cmd.startsWith(vc)) {
        found = true
        break
      }
      if (vc.regex && new RegExp(vc.regex).test(cmd)) {
        found = true
        break
      }
    }
    
    if (found) {
      output = step.output || '<span class="text-green">✅ Comando ejecutado correctamente</span>'
      if (step.finding && !findings.value.find(f => f.text === step.finding.text)) {
        findings.value.push(step.finding)
      }
      currentStep.value++
      if (currentStep.value >= props.steps.length) {
        completed.value = true
      }
    } else {
      // Simulate command output for common commands
      output = simulateCommand(cmd)
    }
  } else {
    output = simulateCommand(cmd)
  }
  
  history.value.push({ command: cmd, output })
  userInput.value = ''
  
  nextTick(() => {
    if (terminalBody.value) {
      terminalBody.value.scrollTop = terminalBody.value.scrollHeight
    }
  })
}

function simulateCommand(cmd) {
  const lower = cmd.toLowerCase()
  
  if (lower.startsWith('nmap')) {
    return `<span class="text-dim">Starting Nmap scan...</span>\n` +
           `<span class="text-green">Nmap scan report for 10.10.10.10</span>\n` +
           `<span class="text-cyan">PORT     STATE SERVICE VERSION</span>\n` +
           `<span class="text-yellow">22/tcp   open  ssh     OpenSSH 8.4</span>\n` +
           `<span class="text-yellow">80/tcp   open  http    Apache/2.4.51</span>\n` +
           `<span class="text-yellow">443/tcp  open  https   Apache/2.4.51</span>\n` +
           `<span class="text-yellow">3306/tcp open  mysql   MySQL 8.0.28</span>\n` +
           `<span class="text-dim">Nmap done: 1 IP address (1 host up) scanned in 2.34s</span>`
  }
  
  if (lower.startsWith('whois')) {
    return `<span class="text-cyan">Domain Name: example.com</span>\n` +
           `<span class="text-dim">Registrar: GoDaddy.com, LLC</span>\n` +
           `<span class="text-dim">Updated Date: 2024-01-15</span>\n` +
           `<span class="text-dim">Creation Date: 2010-03-22</span>\n` +
           `<span class="text-dim">Expiry Date: 2025-03-22</span>\n` +
           `<span class="text-yellow">Name Server: ns1.example.com</span>\n` +
           `<span class="text-yellow">Name Server: ns2.example.com</span>`
  }
  
  if (lower.startsWith('dig') || lower.startsWith('nslookup')) {
    return `<span class="text-cyan">;; ANSWER SECTION:</span>\n` +
           `<span class="text-green">example.com.  300  IN  A  93.184.216.34</span>\n` +
           `<span class="text-green">example.com.  300  IN  MX  mail.example.com (priority 10)</span>\n` +
           `<span class="text-green">example.com.  300  IN  TXT "v=spf1 include:_spf.example.com ~all"</span>\n` +
           `<span class="text-green">example.com.  300  IN  NS  ns1.example.com</span>`
  }
  
  if (lower.startsWith('curl')) {
    return `<span class="text-dim">  % Total    % Received  —  Time   Time</span>\n` +
           `<span class="text-dim">100  1256  100  1256    0     0  5233      0 --:--:-- --:--:-- --:--:--  5233</span>\n` +
           `<span class="text-green">HTTP/1.1 200 OK</span>\n` +
           `<span class="text-dim">Content-Type: text/html; charset=UTF-8</span>\n` +
           `<span class="text-dim">Server: Apache/2.4.51 (Ubuntu)</span>\n` +
           `<span class="text-dim">X-Powered-By: PHP/8.0.13</span>`
  }
  
  if (lower.startsWith('sqlmap')) {
    return `<span class="text-yellow">[!] Legal disclaimer: Usage of sqlmap...</span>\n` +
           `<span class="text-green">[+] GET parameter 'id' is vulnerable.</span>\n` +
           `<span class="text-green">[+] Type: boolean-based blind</span>\n` +
           `<span class="text-green">[+] Title: AND boolean-based blind</span>\n` +
           `<span class="text-yellow">[+] Payload: id=1 AND 1=1</span>\n` +
           `<span class="text-green">[+] Database: MySQL 8.0.28</span>\n` +
           `<span class="text-dim">[*] Finished</span>`
  }
  
  if (lower.startsWith('gobuster')) {
    return `<span class="text-dim">=====================================================</span>\n` +
           `<span class="text-dim">Gobuster v3.6</span>\n` +
           `<span class="text-dim">=====================================================</span>\n` +
           `<span class="text-green">/admin                (Status: 301) [Size: 312]</span>\n` +
           `<span class="text-green">/login                (Status: 200) [Size: 1547]</span>\n` +
           `<span class="text-yellow">/robots.txt           (Status: 200) [Size: 134]</span>\n` +
           `<span class="text-green">/api                  (Status: 403) [Size: 277]</span>\n` +
           `<span class="text-yellow">/.git/HEAD            (Status: 200) [Size: 23]</span>\n` +
           `<span class="text-dim">=====================================================</span>`
  }
  
  if (lower.startsWith('ls') || lower.startsWith('dir')) {
    return `<span class="text-cyan">total 48</span>\n` +
           `<span class="text-green">drwxr-xr-x  hacker hacker 4096 Jan 15 10:30 .</span>\n` +
           `<span class="text-dim">drwxr-xr-x  root   root   4096 Jan 10 08:00 ..</span>\n` +
           `<span class="text-yellow">-rwx------  hacker hacker  220 Jan 15 10:30 notes.txt</span>\n` +
           `<span class="text-yellow">-rw-r--r--  hacker hacker 1024 Jan 15 10:30 scan_results.xml</span>\n` +
           `<span class="text-green">drwxr-xr-x  hacker hacker 4096 Jan 15 10:30 scripts/</span>`
  }
  
  if (lower.startsWith('cat')) {
    return `<span class="text-dim"># Scan results from 2024-01-15</span>\n` +
           `<span class="text-green">Target: 10.10.10.0/24</span>\n` +
           `<span class="text-green">Open ports: 22, 80, 443, 3306</span>\n` +
           `<span class="text-yellow">Services: SSH, HTTP, HTTPS, MySQL</span>\n` +
           `<span class="text-dim"># TODO: Test for vulnerabilities on port 80</span>`
  }
  
  if (lower.startsWith('hashcat') || lower.startsWith('john')) {
    return `<span class="text-yellow">[?] Crack mode: dictionary</span>\n` +
           `<span class="text-green">[+] hash.txt: admin:$2b$12$LJ3m4...</span>\n` +
           `<span class="text-green">[+] Session completed</span>\n` +
           `<span class="text-cyan">admin:password123</span>\n` +
           `<span class="text-dim">All 1 hashes cracked</span>`
  }

  if (lower.startsWith('wireshark') || lower.startsWith('tshark')) {
    return `<span class="text-dim">Capturing on 'eth0'</span>\n` +
           `<span class="text-green">1  0.000000  10.10.10.100 → 10.10.10.10  TCP  SYN</span>\n` +
           `<span class="text-green">2  0.001234  10.10.10.10  → 10.10.10.100 TCP  SYN-ACK</span>\n` +
           `<span class="text-green">3  0.001567  10.10.10.100 → 10.10.10.10  TCP  ACK</span>\n` +
           `<span class="text-yellow">4  0.002100  10.10.10.100 → 10.10.10.10  HTTP GET /</span>\n` +
           `<span class="text-green">5  0.054321  10.10.10.10  → 10.10.10.100 HTTP 200 OK</span>`
  }
  
  if (lower.startsWith('enum4linux') || lower.startsWith('smbclient')) {
    return `<span class="text-dim">enum4linux v4.9.2</span>\n` +
           `<span class="text-green">[+] Found Windows group: Domain Admins</span>\n` +
           `<span class="text-yellow">[+] Users: admin, guest, backup, svc_sql</span>\n` +
           `<span class="text-green">[+] Shares: IPC$, NETLOGON, SYSVOL, DATA</span>\n` +
           `<span class="text-yellow">[!] NULL session possible on IPC$</span>`
  }
  
  return `<span class="text-dim">$ ${cmd}</span>\n<span class="text-dim">Command executed.</span>`
}

function historyUp() {
  if (commandHistory.value.length === 0) return
  historyIndex.value = Math.max(0, historyIndex.value - 1)
  userInput.value = commandHistory.value[historyIndex.value] || ''
}

function historyDown() {
  if (historyIndex.value >= commandHistory.value.length - 1) {
    historyIndex.value = commandHistory.value.length
    userInput.value = ''
    return
  }
  historyIndex.value++
  userInput.value = commandHistory.value[historyIndex.value] || ''
}

onMounted(() => {
  nextTick(() => {
    if (inputRef.value) inputRef.value.focus()
  })
})
</script>

<style scoped>
.lab-terminal-container {
  margin: 1.5rem 0;
  border-radius: 12px;
  overflow: hidden;
  background: #0d1117;
  border: 1px solid #30363d;
  font-family: 'JetBrains Mono', 'Fira Code', monospace;
}

.lab-header {
  display: flex;
  justify-content: space-between;
  align-items: center;
  padding: 12px 16px;
  background: linear-gradient(135deg, #161b22, #0d1117);
  border-bottom: 1px solid #30363d;
}

.lab-title {
  display: flex;
  align-items: center;
  gap: 8px;
}

.lab-title h3 {
  margin: 0;
  font-size: 0.95rem;
  color: #e6edf3;
}

.lab-icon {
  font-size: 1.2rem;
}

.lab-stats {
  display: flex;
  gap: 12px;
}

.stat {
  font-size: 0.8rem;
  color: #8b949e;
  background: #21262d;
  padding: 2px 8px;
  border-radius: 4px;
}

.stat.xp {
  color: #f0883e;
  font-weight: 600;
}

.progress-bar {
  height: 3px;
  background: #21262d;
}

.progress-fill {
  height: 100%;
  background: linear-gradient(90deg, #238636, #3fb950);
  transition: width 0.3s ease;
}

.step-info {
  padding: 12px 16px;
  background: #161b22;
  border-bottom: 1px solid #30363d;
}

.step-badge {
  display: inline-block;
  background: #1f6feb;
  color: white;
  font-size: 0.7rem;
  padding: 2px 8px;
  border-radius: 4px;
  margin-bottom: 6px;
  font-weight: 600;
}

.step-info h4 {
  margin: 0 0 4px;
  color: #e6edf3;
  font-size: 0.9rem;
}

.step-info p {
  margin: 0;
  color: #8b949e;
  font-size: 0.8rem;
}

.terminal {
  border-radius: 0;
  overflow: hidden;
}

.terminal-header {
  display: flex;
  align-items: center;
  padding: 8px 12px;
  background: #161b22;
  border-bottom: 1px solid #30363d;
  gap: 8px;
}

.terminal-dots {
  display: flex;
  gap: 6px;
}

.dot {
  width: 10px;
  height: 10px;
  border-radius: 50%;
}

.dot.red { background: #ff5f57; }
.dot.yellow { background: #febc2e; }
.dot.green { background: #28c840; }

.terminal-title {
  color: #8b949e;
  font-size: 0.75rem;
}

.terminal-body {
  padding: 12px 16px;
  min-height: 200px;
  max-height: 500px;
  overflow-y: auto;
  background: #0d1117;
  font-size: 0.82rem;
  line-height: 1.5;
}

.terminal-body::-webkit-scrollbar {
  width: 6px;
}

.terminal-body::-webkit-scrollbar-track {
  background: #0d1117;
}

.terminal-body::-webkit-scrollbar-thumb {
  background: #30363d;
  border-radius: 3px;
}

.welcome-msg {
  margin-bottom: 12px;
  padding-bottom: 8px;
  border-bottom: 1px solid #21262d;
}

.history-entry {
  margin-bottom: 8px;
}

.command-line {
  display: flex;
  gap: 8px;
}

.prompt {
  color: #3fb950;
  white-space: nowrap;
}

.command {
  color: #e6edf3;
}

.output {
  margin-left: 0;
  padding: 4px 0;
  white-space: pre-wrap;
  color: #c9d1d9;
}

.input-line {
  display: flex;
  gap: 8px;
  align-items: center;
}

.terminal-input {
  flex: 1;
  background: transparent;
  border: none;
  color: #e6edf3;
  font-family: inherit;
  font-size: inherit;
  outline: none;
  caret-color: #3fb950;
}

.terminal-input::placeholder {
  color: #484f58;
}

.completed-msg {
  margin-top: 12px;
  padding: 12px;
  background: #0d2818;
  border: 1px solid #238636;
  border-radius: 6px;
}

.findings-panel {
  padding: 12px 16px;
  background: #161b22;
  border-top: 1px solid #30363d;
}

.findings-panel h4 {
  margin: 0 0 8px;
  color: #e6edf3;
  font-size: 0.85rem;
}

.finding {
  display: flex;
  align-items: center;
  gap: 8px;
  padding: 4px 0;
  font-size: 0.8rem;
}

.finding-type {
  font-size: 0.65rem;
  padding: 1px 6px;
  border-radius: 3px;
  font-weight: 600;
  white-space: nowrap;
}

.type-ip { background: #1f6feb33; color: #58a6ff; }
.type-port { background: #f0883e33; color: #f0883e; }
.type-vuln { background: #f8514933; color: #f85149; }
.type-cred { background: #a371f733; color: #a371f7; }
.type-info { background: #3fb95033; color: #3fb950; }
.type-hash { background: #f0883e33; color: #f0883e; }

.finding-text {
  color: #c9d1d9;
}

.hints-panel {
  padding: 10px 16px;
  background: #1c1917;
  border-top: 1px solid #30363d;
  color: #fbbf24;
  font-size: 0.82rem;
}

.hint-icon {
  margin-right: 6px;
}

/* Text utility classes */
.text-green { color: #3fb950; }
.text-red { color: #f85149; }
.text-yellow { color: #f0883e; }
.text-cyan { color: #58a6ff; }
.text-dim { color: #8b949e; }
</style>
