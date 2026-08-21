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

| Lab | Tema | Módulo | Duración | XP | Certificación |
|-----|------|--------|----------|-----|---------------|
| [recon-01](intermedio/recon-01/) | Reconocimiento y OSINT | 01 - Reconocimiento | 45 min | 250 | eJPT |
| [pentest-01](intermedio/pentest-01/) | Pentesting — Ciclo PTES | 02 - Pentesting | 90 min | 400 | eJPT/OSCP |
| [vulnscan-01](intermedio/vulnscan-01/) | Análisis de Vulnerabilidades | 03 - Análisis Vulns | 60 min | 300 | CEH |
| [webapp-01](intermedio/webapp-01/) | Explotación Web (OWASP) | 04 - Explotación Web | 90 min | 400 | CEH |
| [privesc-01](intermedio/privesc-01/) | Linux Privilege Escalation | 05 - Post-Explotación | 60 min | 300 | eJPT |
| [privesc-02](intermedio/privesc-02/) | Windows Privilege Escalation | 05 - Post-Explotación | 60 min | 300 | eJPT |
| [web-01](intermedio/web-01/) | Web Application Security (OWASP) | 04 - Explotación Web | 90 min | 400 | CEH |
| [crypto-01](intermedio/crypto-01/) | Cryptography Challenges | 08 - Criptografía | 90 min | 400 | CEH |

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
git clone https://github.com/0xvanguard/CyberDefense-Pro-Network.git
cd CyberDefense-Pro-Network

# Ejecutar un lab específico
cd labs/intermedio/recon-01
docker compose up -d

# Obtener shell del atacante
docker compose exec kali bash

# Verificar solución
./scripts/validate.sh

# Parar el entorno
docker compose down
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

## 🗺️ Ruta de Aprendizaje Recomendada

```
Fundamentos                    Red Team (Módulos 01-08)
─────────────                  ─────────────────────────
net-01 (Redes)      ──────▶   recon-01 (Reconocimiento)
linux-01 (Linux)    ──────▶   pentest-01 (Pentesting)
script-01 (Python)  ──────▶   vulnscan-01 (Análisis Vulns)
                               webapp-01 (Explotación Web)
                               privesc-01 (Post-Explotación)
                               crypto-01 (Criptografía)
                                    │
                                    ▼
                               Nivel Avanzado
                               ad-01, forensics-01, cloud-01
                                    │
                                    ▼
                               Nivel Expert
                               apt-01, incident-01, malware-01
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
├── Dockerfile*            # Configuración de contenedores
├── scripts/
│   └── validate.sh        # Script de validación
├── solutions/
│   └── solution.md        # Solución completa
└── data/                  # Datos iniciales (si aplica)
```

## 🔧 Herramientas Requeridas

```bash
# Solo necesitas Docker
docker --version
docker compose version
```

### Dependencias por Nivel

| Nivel | Herramientas |
|-------|--------------|
| Fundamentos | Docker, curl, netcat |
| Intermedio | + nmap, hydra, sqlmap, nuclei |
| Avanzado | + impacket, mimikatz, bloodhound |
| Expert | + metasploit, burp suite, vol3 |

## 📚 Recursos Adicionales

- [OWASP Top 10](https://owasp.org/www-project-top-ten/)
- [MITRE ATT&CK](https://attack.mitre.org/)
- [GTFOBins](https://gtfobins.github.io/)
- [HackTheBox](https://www.hackthebox.com/)
- [TryHackMe](https://tryhackme.com/)

---

**¿Listo para empezar?** Selecciona un lab y comienza tu journey en ciberseguridad.

*Última actualización: Agosto 2024*
