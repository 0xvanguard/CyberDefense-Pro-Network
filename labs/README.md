# 🧪 CyberDefense Labs — Entornos Interactivos Profesionales

> Labs prácticos con validación automática, progresión de dificultad y feedback en tiempo real.

## 🎯 Objetivo

Proporcionar un entorno de aprendizaje práctico y medible para ciberseguridad, desde fundamentos hasta escenarios avanzados de realidad simulada.

## 📋 Catálogo de Labs

### 🟢 Nivel Fundamentos (Principiante)

| Lab | Tema | Duración | XP | Certificación |
|-----|------|----------|-----|---------------|
| [net-01](fundamentos/net-01/) | TCP/IP & OSI Model | 30 min | 100 | Comptia Network+ |
| [linux-01](fundamentos/linux-01/) | Linux Basics & CLI | 45 min | 150 | Comptia Linux+ |
| [win-01](fundamentos/win-01/) | Windows Administration | 45 min | 150 | Comptia A+ |
| [script-01](fundamentos/script-01/) | Python for Security | 60 min | 200 | - |

### 🟡 Nivel Intermedio

| Lab | Tema | Duración | XP | Certificación |
|-----|------|----------|-----|---------------|
| [privesc-01](intermedio/privesc-01/) | Linux Privilege Escalation | 60 min | 300 | eJPT |
| [privesc-02](intermedio/privesc-02/) | Windows Privilege Escalation | 60 min | 300 | eJPT |
| [web-01](intermedio/web-01/) | Web Application Security (OWASP) | 90 min | 400 | CEH |
| [crypto-01](intermedio/crypto-01/) | Cryptography Challenges | 90 min | 400 | CEH |
| [recon-01](intermedio/recon-01/) | Reconnaissance & OSINT | 45 min | 250 | eJPT |

### 🔴 Nivel Avanzado

| Lab | Tema | Duración | XP | Certificación |
|-----|------|----------|-----|---------------|
| [ad-01](avanzado/ad-01/) | Active Directory Attacks | 120 min | 500 | OSCP |
| [forensics-01](avanzado/forensics-01/) | Digital Forensics | 120 min | 500 | GCFE |
| [cloud-01](avanzado/cloud-01/) | Cloud Security (AWS/Azure) | 120 min | 500 | CCSP |
| [persist-01](avanzado/persist-01/) | Persistence Techniques | 90 min | 400 | OSCP |
| [lateral-01](avanzado/lateral-01/) | Lateral Movement | 90 min | 400 | OSCP |

### 🏆 Nivel Expert (Simulación Real)

| Lab | Tema | Duración | XP | Certificación |
|-----|------|----------|-----|---------------|
| [apt-01](expert/apt-01/) | APT Simulation | 180 min | 1000 | OSCP/OSCE |
| [incident-01](expert/incident-01/) | Incident Response | 180 min | 1000 | GCIH |
| [malware-01](expert/malware-01/) | Malware Analysis | 120 min | 750 | GREM |
| [redteam-01](expert/redteam-01/) | Red Team Exercise | 240 min | 1500 | OSCE |

## 🚀 Inicio Rápido

```bash
# Clonar el repositorio
git clone https://github.com/your-org/cyberdefense-labs.git
cd cyberdefense-labs

# Verificar requisitos
./scripts/check-requirements.sh

# Ejecutar un lab específico
./scripts/run-lab.sh fundamentos/net-01

# Verificar solución
./scripts/validate-lab.sh fundamentos/net-01
```

## 📊 Sistema de Progresión

```
┌─────────────────────────────────────────────────────────────┐
│                    SISTEMA DE XP & LOGROS                   │
├─────────────────────────────────────────────────────────────┤
│  🟢 Fundamentos:    0 - 1,000 XP  →  Security Novice       │
│  🟡 Intermedio: 1,000 - 3,000 XP  →  Security Analyst      │
│  🔴 Avanzado:   3,000 - 7,000 XP  →  Security Engineer     │
│  🏆 Expert:     7,000+ XP         →  Security Expert       │
└─────────────────────────────────────────────────────────────┘
```

## 🏅 Logros Desbloqueables

| Logro | Requisito | XP Bonus |
|-------|-----------|----------|
| 🔰 Primer Lab | Completar tu primer lab | +50 XP |
| 🎯 Precisión Perfecta | 100% en validación | +100 XP |
| ⚡ Velocidad Récord | Completar bajo tiempo límite | +150 XP |
| 🧠 Sin Ayuda | Completar sin hints | +200 XP |
| 🔓 Escalador | 5 labs de privesc completados | +300 XP |
| 🛡️ Defensor | 5 labs defensivos completados | +300 XP |
| 🏆 Maestro | Todos los labs expert completados | +2000 XP |

## 🛠️ Estructura de un Lab

```
lab-name/
├── README.md              # Instrucciones y objetivos
├── docker-compose.yml     # Entorno Docker
├── Dockerfile             # Configuración del contenedor
├── challenge.yml          # Metadatos del challenge
├── validation/
│   ├── check.sh           # Script de validación
│   └── expected.txt       # Resultados esperados
├── hints/
│   ├── hint-01.md         # Pista nivel 1
│   ├── hint-02.md         # Pista nivel 2
│   └── hint-03.md         # Pista nivel 3 (spoiler)
├── solutions/
│   └── solution.md        # Solución completa
└── assets/
    ├── topology.svg       # Diagrama de red
    └── flags.txt          # Flags a encontrar
```

## 📈 Métricas de Aprendizaje

Cada lab trackea:
- **Tiempo de resolución**
- **Número de intentos**
- **Hints utilizados**
- **Comandos ejecutados**
- **Errores encontrados**

## 🔧 Herramientas Requeridas

```bash
# Verificar todas las herramientas
./scripts/check-requirements.sh

# Instalar dependencias
./scripts/install-deps.sh
```

### Dependencias por Nivel

| Nivel | Herramientas |
|-------|--------------|
| Fundamentos | Docker, curl, netcat |
| Intermedio | + nmap, hydra, gobuster, sqlmap |
| Avanzado | + impacket, mimikatz, bloodhound, evil-winrm |
| Expert | + metasploit, burp suite, wireshark, vol3 |

## 📚 Recursos Adicionales

- [Documentación de Labs](./docs/)
- [Guía de Contribución](./CONTRIBUTING.md)
- [Changelog](./CHANGELOG.md)
- [Discord Community](https://discord.gg/cyberdefense)

---

**¿Listo para empezar?** Selecciona un lab de nivel Fundamentos y comienza tu journey en ciberseguridad.

*Última actualización: Agosto 2024*
