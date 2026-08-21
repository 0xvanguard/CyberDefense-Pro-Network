---
title: "⚔️ Lab adversary-01: Adversary Emulation"
description: "⚔️ Lab adversary-01: Adversary Emulation"
---

# ⚔️ Lab adversary-01: Adversary Emulation

> Emula adversaries reales usando MITRE ATT&CK y mide la efectividad de tus defensas.

## 🎯 Objetivos de Aprendizaje

Al completar este lab podrás:

- [ ] Emular adversaries usando Atomic Red Team
- [ ] Ejecutar técnicas del framework MITRE ATT&CK
- [ ] Medir la efectividad de controles de seguridad
- [ ] Identificar gaps en detección
- [ ] Documentar resultados para mejora continua

## ⏱️ Información del Lab

| Campo | Valor |
|-------|-------|
| **Dificultad** | 🟡 Intermedio |
| **Tiempo estimado** | 90 minutos |
| **XP en juego** | 450 puntos |
| **Herramientas** | Atomic Red Team, MITRE ATT&CK Navigator |
| **Flags** | 8 |

## 🚀 Inicio Rápido

```bash
# Levantar el entorno
cd labs/purple-team/adversary-01/
docker compose up -d

# Verificar servicios
docker compose ps
```

## 📋 Ejercicios

### Ejercicio 1: Configurar Entorno (60 XP)

Prepara el entorno de emulación:

```bash
# 1. Instalar Atomic Red Team en Windows
# PowerShell
IEX (New-Object Net.WebClient).DownloadString('https://raw.githubusercontent.com/redcanaryco/invoke-atomicredteam/master/Install-AtomicRedTeam.ps1')
Install-AtomicRedTeam -getAtomics

# 2. Verificar instalación
ls C:\AtomicRedTeam\atomics

# 3. Listar técnicas disponibles
Get-ChildItem C:\AtomicRedTeam\atomics -Directory | Select-Object Name
```

**Flag:** `[___]`

---

### Ejercicio 2: Emular Initial Access (60 XP)

Emula técnicas de acceso inicial:

```bash
# T1566 - Phishing (simulado)
# Crear archivo de prueba
echo "Simulated phishing payload" > /tmp/phishing_test.txt

# T1190 - Exploit Public-Facing Application
# Intentar explotar servicio web
nmap -sV 10.0.2.20

# Documentar resultados
cat > initial_access.md << 'EOF'
# Initial Access Emulation

## T1566 - Phishing
- Ejecutado: Sí/No
- Detectado: Sí/No
- MTTD: [X] min

## T1190 - Exploit Public-Facing
- Ejecutado: Sí/No
- Detectado: Sí/No
- MTTD: [X] min
EOF
```

**Flag:** `[___]`

---

### Ejercicio 3: Emular Execution (60 XP)

Emula técnicas de ejecución:

```bash
# T1059 - Command and Scripting Interpreter
# PowerShell
powershell -enc [Base64]

# T1053 - Scheduled Task
schtasks /create /tn "TestTask" /tr "cmd.exe /c echo test" /sc once /st 00:00

# T1047 - Windows Management Instrumentation
wmic process list brief

# Documentar resultados
```

**Flag:** `[___]`

---

### Ejercicio 4: Emular Persistence (60 XP)

Emula técnicas de persistencia:

```bash
# T1547 - Boot or Logon Autostart Execution
reg add "HKLM\Software\Microsoft\Windows\CurrentVersion\Run" /v "Test" /d "C:\test.exe"

# T1053 - Scheduled Task
schtasks /create /tn "PersistTask" /tr "C:\backdoor.exe" /sc daily

# T1543 - Create or Modify System Process
# Crear servicio
sc create "TestService" binPath= "C:\test.exe" start= auto

# Documentar resultados
```

**Flag:** `[___]`

---

### Ejercicio 5: Emular Privilege Escalation (60 XP)

Emula técnicas de escalada:

```bash
# T1548 - Abuse Elevation Control Mechanism
# UAC Bypass (simulado)

# T1068 - Exploitation for Privilege Escalation
# Buscar vulnerabilidades de kernel

# T1134 - Access Token Manipulation
# Token impersonation

# Documentar resultados
```

**Flag:** `[___]`

---

### Ejercicio 6: Emular Defense Evasion (60 XP)

Emula técnicas de evasión:

```bash
# T1027 - Obfuscated Files or Information
# Ofuscar payload

# T1140 - Deobfuscate/Decode Files
# Decodificar archivos

# T1036 - Masquerading
# Renombrar procesos

# Documentar resultados
```

**Flag:** `[___]`

---

### Ejercicio 7: Emular Credential Access (60 XP)

Emula técnicas de credenciales:

```bash
# T1003 - OS Credential Dumping
# Mimikatz (simulado)

# T1558 - Steal or Forge Kerberos Tickets
# Kerberoasting

# T1110 - Brute Force
hydra -l admin -P /usr/share/wordlists/rockyou.txt ssh://10.0.2.20

# Documentar resultados
```

**Flag:** `[___]`

---

### Ejercicio 8: Análisis y Reporte (60 XP)

Analiza y documenta resultados:

```yaml
# adversary_emulation_report.yml
metadata:
  project: "Adversary Emulation Lab"
  date: "2024-01-15"

techniques_executed:
  - id: "T1566"
    name: "Phishing"
    detected: true
    mttd: 5
    
  - id: "T1059"
    name: "PowerShell"
    detected: true
    mttd: 8
    
  - id: "T1547"
    name: "Autostart Execution"
    detected: false
    mttd: null
    
  - id: "T1003"
    name: "Credential Dumping"
    detected: true
    mttd: 12

metrics:
  total_techniques: 4
  detected: 3
  coverage: 75%
  avg_mttd: 8.3

gaps:
  - technique: "T1547"
    reason: "Registry monitoring not configured"
    priority: "High"

recommendations:
  - "Enable registry auditing"
  - "Configure Sysmon for persistence detection"
```

**Flag:** `[___]`

## 🏁 Validación

```bash
./scripts/validate.sh
```

## 📝 Criterios de Éxito

| Ejercicio | Criterio | Puntos | Estado |
|-----------|----------|--------|--------|
| 1 | Entorno configurado | 60 | ⬜ |
| 2 | Initial Access emulado | 60 | ⬜ |
| 3 | Execution emulado | 60 | ⬜ |
| 4 | Persistence emulado | 60 | ⬜ |
| 5 | Privilege Escalation emulado | 60 | ⬜ |
| 6 | Defense Evasion emulado | 60 | ⬜ |
| 7 | Credential Access emulado | 60 | ⬜ |
| 8 | Reporte generado | 60 | ⬜ |
| **Total** | | **450** | ⬜ |

---

*Lab creado para CyberDefense Labs — Nivel Intermedio*
