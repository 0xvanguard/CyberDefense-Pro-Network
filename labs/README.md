# 🧪 CDPN Labs — Laboratorios Prácticos

> *Aprende haciendo. Cada lab es un entorno Docker reproducible que puedes levantar en segundos.*

[![Docker](https://img.shields.io/badge/Docker-Ready-blue?style=flat-square&logo=docker)]()
[![Labs](https://img.shields.io/badge/Labs-22-brightgreen?style=flat-square)]()
[![Levels](https://img.shields.io/badge/Levels-4-orange?style=flat-square)]()

---

## 🚀 Quick Start

```bash
# Clone el repo
git clone https://github.com/0xvanguard/CyberDefense-Pro-Network.git
cd CyberDefense-Pro-Network

# Listar todos los labs disponibles
./labs/setup.sh --list

# Levantar un lab específico
./labs/setup.sh intermedio/pentest-01

# Verificar que todos los compose files son válidos
./labs/setup.sh --validate

# Parar un lab
./labs/setup.sh intermedio/pentest-01 --stop
```

---

## 📋 Catálogo Completo de Labs

### 🟢 Fundamentos

| Lab | Nombre | Servicios | Descripción | Nivel |
|-----|--------|-----------|-------------|-------|
| `net-01` | Redes Básicas | 5 | TCP/IP, DNS, HTTP, subnets | Principiante |

### 🟡 Intermedio

| Lab | Nombre | Servicios | Descripción | Nivel |
|-----|--------|-----------|-------------|-------|
| `recon-01` | Reconocimiento | 5 | Nmap, subfinder, httpx, nuclei | Intermedio |
| `vulnscan-01` | Vulnerability Scan | 4 | OpenVAS, Nuclei, Nikto | Intermedio |
| `web-01` | Web Hacking | 4 | DVWA, SQLi, XSS, IDOR | Intermedio |
| `webapp-01` | Web App Pentest | 4 | Juice Shop, API testing | Intermedio |
| `pentest-01` | Pentest Completo | 3 | PTES completo, Metasploit | Intermedio |
| `crypto-01` | Criptografía | 1 | Hash, RSA, AES, cracking | Intermedio |
| `disk-forensics-01` | Forense de Disco | 1 | Disk imaging, Autopsy | Intermedio |
| `lateral-01` | Lateral Movement | 4 | Pass-the-hash, SMB, WinRM | Intermedio |
| `privesc-01` | Privilege Escalation | 1 | SUID, kernel exploits, sudo | Intermedio |
| `persist-01` | Persistence | 1 | Cron, services, registry | Intermedio |
| `social-01` | Ingeniería Social | 3 | Phishing, pretexting | Intermedio |

### 🔴 Avanzado

| Lab | Nombre | Servicios | Descripción | Nivel |
|-----|--------|-----------|-------------|-------|
| `ad-01` | Active Directory | 6 | AD hacking, Kerberoasting | Avanzado |
| `cloud-01` | Cloud Security | 2 | AWS/Azure misconfig | Avanzado |
| `forensics-01` | Forense Avanzado | 2 | Memory, malware, timeline | Avanzado |
| `malware-01` | Análisis Malware | 4 | Static, dynamic, sandbox | Avanzado |
| `net-forensics-01` | Forense de Red | 4 | PCAP, Suricata, Zeek | Avanzado |
| `reverse-eng-01` | Reverse Engineering | 1 | Binary analysis, Ghidra | Avanzado |
| `redteam-c2-01` | Red Team C2 | 7 | Sliver, evasion, OPSEC | Avanzado |
| `purple-emulation-01` | Purple Team | 5 | Atomic Red Team, Wazuh | Avanzado |

### 💀 Expert

| Lab | Nombre | Servicios | Descripción | Nivel |
|-----|--------|-----------|-------------|-------|
| `incident-01` | Incident Response | 7 | Full IR pipeline | Expert |
| `malware-01` | Malware Dev | 3 | Create & analyze malware | Expert |

---

## 🛠️ Requisitos

- **Docker** >= 24.0
- **Docker Compose** >= 2.0
- **RAM** >= 4GB (algunos labs requieren 8GB)
- **Disco** >= 10GB libres

### Instalar Docker

```bash
# Ubuntu/Debian
curl -fsSL https://get.docker.com | sh
sudo usermod -aG docker $USER

# macOS
brew install --cask docker

# Windows
# Descargar Docker Desktop desde docker.com
```

---

## 📖 Cómo usar cada lab

### 1. Elegir un lab
```bash
./labs/setup.sh --list
```

### 2. Leer el README del lab
```bash
cat labs/intermedio/pentest-01/README.md
```

### 3. Levantar el lab
```bash
./labs/setup.sh intermedio/pentest-01
```

### 4. Seguir las instrucciones del README
Cada lab tiene:
- **Objetivos de aprendizaje** claros
- **Diagrama de red** con IPs
- **Paso a paso** detallado
- **Métricas de éxito** para saber cuándo completaste

### 5. Parar el lab
```bash
./labs/setup.sh intermedio/pentest-01 --stop
```

---

## 🎯 Ruta de Aprendizaje Recomendada

```
FUNDAMENTOS                    INTERMEDIO
    │                              │
    ▼                              ▼
 net-01 ────────→ recon-01 ──────→ vulnscan-01
 (Redes)         (Recon)          (Vulnerabilities)
                                      │
                    ┌─────────────────┤
                    ▼                 ▼
               web-01            pentest-01
              (Web)             (Full Pentest)
                    │                 │
                    ▼                 ▼
               crypto-01         privesc-01
              (Crypto)           (Priv Esc)
                                     │
                    ┌────────────────┤
                    ▼                ▼
              lateral-01        persist-01
             (Lateral)         (Persistence)
                                     │
                                     ▼
                              AVANZADO/EXPERT
                                     │
                    ┌────────────────┤
                    ▼                ▼
              redteam-c2-01    purple-emulation-01
               (Red Team)      (Purple Team)
                    │                │
                    ▼                ▼
              malware-01        incident-01
             (Malware)         (Incident Response)
```

---

## 🔧 Troubleshooting

### Docker no arranca
```bash
sudo systemctl start docker
# o reiniciar Docker Desktop
```

### Puerto en uso
```bash
# Ver qué está usando el puerto
lsof -i :8080
# Cambiar el puerto en docker-compose.yml
```

### Lab no funciona
```bash
# Ver logs
cd labs/intermedio/pentest-01
docker compose logs

# Reconstruir desde cero
docker compose down -v
docker compose up -d --build
```

### Limpiar todos los labs
```bash
docker system prune -f
docker volume prune -f
```

---

## 📊 Estadísticas

| Métrica | Valor |
|---------|-------|
| Total de labs | 22 |
| Con Docker | 22 (100%) |
| Fundamentos | 1 |
| Intermedio | 11 |
| Avanzado | 8 |
| Expert | 2 |
| Servicios totales | ~70 |

---

*Última actualización: Agosto 2026*
*CyberDefense-Pro-Network — Aprende haciendo. Demuestra con evidencia.*
