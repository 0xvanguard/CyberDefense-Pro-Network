# 🛠️ Herramientas y Recursos Recomendados

## 📋 Guía Curada para Principiantes y Profesionales

Colección de las mejores herramientas y recursos, organizadas por nivel de dificultad y caso de uso.

---

## 🟢 Herramientas para Principiantes

### 🖥️ Sistemas Operativos

| Herramienta | Uso | Dificultad | Link |
|-------------|-----|------------|------|
| **Ubuntu** | Linux para principiantes | 🟢 Fácil | https://ubuntu.com |
| **Kali Linux** | Pentesting | 🟡 Intermedio | https://kali.org |
| **Parrot OS** | Seguridad y privacidad | 🟡 Intermedio | https://parrotsec.org |

**Recomendación:** Empieza con **Ubuntu** para aprender Linux, luego migra a **Kali** cuando tengas experiencia.

---

### 🔍 Reconocimiento

| Herramienta | Uso | Dificultad | Gratis |
|-------------|-----|------------|--------|
| **Nmap** | Escaneo de redes | 🟢 Fácil | ✅ |
| **theHarvester** | Recopilación de emails | 🟢 Fácil | ✅ |
| **Shodan** | Búsqueda de dispositivos | 🟢 Fácil | ✅ |
| **Censys** | Búsqueda de certificados | 🟢 Fácil | ✅ |

```bash
# Instalar Nmap
sudo apt install nmap

# Uso básico
nmap -sV scanme.nmap.org
```

---

### 🕷️ Testing Web

| Herramienta | Uso | Dificultad | Gratis |
|-------------|-----|------------|--------|
| **Burp Suite Community** | Proxy de testing | 🟡 Intermedio | ✅ |
| **OWASP ZAP** | Scanner de vulnerabilidades | 🟡 Intermedio | ✅ |
| **Nikto** | Scanner web | 🟢 Fácil | ✅ |
| **Dirb** | Fuzzing de directorios | 🟢 Fácil | ✅ |

```bash
# Instalar OWASP ZAP
sudo apt install zaproxy

# Instalar Nikto
sudo apt install nikto
```

---

### 📡 Análisis de Red

| Herramienta | Uso | Dificultad | Gratis |
|-------------|-----|------------|--------|
| **Wireshark** | Análisis de tráfico | 🟡 Intermedio | ✅ |
| **TCPDump** | Captura de paquetes | 🟡 Intermedio | ✅ |
| **Netcat** | Swiss army knife de red | 🟢 Fácil | ✅ |

```bash
# Instalar Wireshark
sudo apt install wireshark

# Capturar tráfico
sudo tcpdump -i eth0 -w capture.pcap
```

---

## 🟡 Herramientas para Intermedios

### 💥 Explotación

| Herramienta | Uso | Dificultad | Gratis |
|-------------|-----|------------|--------|
| **Metasploit** | Framework de exploits | 🔴 Avanzado | ✅ |
| **SQLMap** | SQL Injection | 🟡 Intermedio | ✅ |
| **Hydra** | Fuerza bruta | 🟡 Intermedio | ✅ |
| **John the Ripper** | Cracking de hashes | 🟡 Intermedio | ✅ |

```bash
# Instalar Metasploit
curl https://raw.githubusercontent.com/rapid7/metasploit-omnibus/master/config/templates/metasploit-framework-wrappers/msfupdate.erb > msfinstall
chmod 755 msfinstall
./msfinstall

# SQLMap
sqlmap -u "http://target.com/?id=1" --dbs
```

---

### 🦠 Análisis de Malware

| Herramienta | Uso | Dificultad | Gratis |
|-------------|-----|------------|--------|
| **YARA** | Reglas de detección | 🟡 Intermedio | ✅ |
| **VirusTotal** | Análisis online | 🟢 Fácil | ✅ |
| **Any.Run** | Sandbox interactivo | 🟡 Intermedio | ✅ |
| **PE-bear** | Análisis de PE | 🟡 Intermedio | ✅ |

```bash
# Instalar YARA
sudo apt install yara

# Escanear archivo
yara -r reglas/ malware样本.exe
```

---

### 🔍 Forense Digital

| Herramienta | Uso | Dificultad | Gratis |
|-------------|-----|------------|--------|
| **Autopsy** | Forense de disco | 🟡 Intermedio | ✅ |
| **Volatility** | Forense de memoria | 🔴 Avanzado | ✅ |
| **FTK Imager** | Adquisición de evidencia | 🟡 Intermedio | ✅ |

---

## 🔴 Herramientas para Avanzados

### ☁️ Cloud Security

| Herramienta | Uso | Plataforma | Gratis |
|-------------|-----|------------|--------|
| **Prowler** | Auditoría AWS | AWS | ✅ |
| **ScoutSuite** | Auditoría multi-cloud | Multi | ✅ |
| **Checkov** | IaC Security | Multi | ✅ |
| **Trivy** | Scanner de contenedores | Docker/K8s | ✅ |
| **kube-bench** | Auditoría Kubernetes | K8s | ✅ |

```bash
# Instalar Prowler
pip install prowler

# Ejecutar auditoría AWS
prowler aws
```

---

### 🛡️ SIEM y Monitoreo

| Herramienta | Uso | Dificultad | Gratis |
|-------------|-----|------------|--------|
| **Wazuh** | SIEM completo | 🟡 Intermedio | ✅ |
| **ELK Stack** | Análisis de logs | 🔴 Avanzado | ✅ |
| **OSSEC** | HIDS | 🟡 Intermedio | ✅ |
| **Snort** | IDS/IPS | 🔴 Avanzado | ✅ |

```bash
# Instalar Wazuh
curl -sO https://packages.wazuh.com/4.7/wazuh-install.sh && sudo bash ./wazuh-install.sh -a
```

---

### 🔧 Automatización

| Herramienta | Uso | Dificultad | Gratis |
|-------------|-----|------------|--------|
| **Python** | Scripting | 🟡 Intermedio | ✅ |
| **Bash** | Automatización Linux | 🟢 Fácil | ✅ |
| **PowerShell** | Automatización Windows | 🟡 Intermedio | ✅ |
| **Ansible** | Configuración | 🔴 Avanzado | ✅ |
| **Docker** | Contenedores | 🟡 Intermedio | ✅ |

---

## 📚 Plataformas de Aprendizaje

### 🎮 Practica Interactiva

| Plataforma | Tipo | Precio | Ideal para |
|------------|------|--------|------------|
| **TryHackMe** | Rooms guiados | Gratis/Premium | 🟢 Principiantes |
| **HackTheBox** | Máquinas retos | Gratis/Premium | 🟡 Intermedios |
| **PicoCTF** | CTF educativo | Gratis | 🟢 Principiantes |
| **OverTheWire** | Wargames | Gratis | 🟡 Intermedios |
| **VulnHub** | VMs descargables | Gratis | 🟡 Intermedios |
| **PortSwigger Academy** | Web security | Gratis | 🟡 Intermedios |

**Recomendación para principiantes:** Empieza con **TryHackMe** → ruta "Pre-Security"

---

### 📖 Cursos Online

| Curso | Plataforma | Precio | Certificado |
|-------|------------|--------|-------------|
| Introduction to Cybersecurity | Cisco NetAcad | Gratis | ✅ |
| IBM Cybersecurity Analyst | Coursera | Gratis (audit) | ✅ |
| Complete Cyber Security Course | Udemy | ~$15 | ✅ |
| Google Cybersecurity | Coursera | ~$39/mes | ✅ |

---

### 📚 Documentación Oficial

| Recurso | Descripción |
|---------|-------------|
| [MITRE ATT&CK](https://attack.mitre.org/) | Base de conocimiento de amenazas |
| [OWASP Top 10](https://owasp.org/www-project-top-ten/) | Vulnerabilidades web principales |
| [NIST CSF](https://www.nist.gov/cyberframework) | Framework de ciberseguridad |
| [PTES](http://www.pentest-standard.org/) | Estándar de pentesting |

---

## 🏆 Certificaciones por Nivel

### 🟢 Nivel Básico

| Certificación | Organización | Costo | Validez |
|---------------|--------------|-------|---------|
| CompTIA Security+ | CompTIA | ~$400 | 3 años |
| eLearnSecurity eJPT | INE | ~$200 | 3 años |
| Google Cybersecurity | Google | ~$39/mes | - |

### 🟡 Nivel Intermedio

| Certificación | Organización | Costo | Validez |
|---------------|--------------|-------|---------|
| CompTIA CySA+ | CompTIA | ~$400 | 3 años |
| CEH | EC-Council | ~$1,200 | 3 años |
| AWS Security Specialty | Amazon | ~$300 | 2 años |

### 🔴 Nivel Avanzado

| Certificación | Organización | Costo | Validez |
|---------------|--------------|-------|---------|
| OSCP | OffSec | ~$1,600 | Sin expirar |
| CISSP | (ISC)² | ~$700 | 3 años |
| GXPN | GIAC | ~$900 | 4 años |

---

## 📱 Apps Móviles Útiles

| App | Plataforma | Uso |
|-----|------------|-----|
| **Termux** | Android | Terminal Linux en móvil |
| **NetHunter** | Android | Kali Linux en Android |
| **SSH Client** | iOS/Android | Acceso remoto SSH |
| **Authy** | iOS/Android | 2FA authenticator |
| **KeePass** | iOS/Android | Gestor de contraseñas |

---

## 🎯 Ruta de Aprendizaje Recomendada

### Para Principiantes (0-3 meses)

```
Mes 1: Fundamentos
├── Ubuntu/Debian en VirtualBox
├── 20 comandos de Linux
├── Modelo OSI y TCP/IP
└── TryHackMe: Pre-Security Path

Mes 2: Reconocimiento
├── Nmap básico e intermedio
├── theHarvester
├── OSINT fundamentals
└── TryHackMe: Intro to Cyber Security

Mes 3: Primeros Pasos
├── OWASP Top 10
├── SQL Injection básico
├── XSS básico
└── PicoCTF: Primeros retos
```

### Para Intermedios (3-12 meses)

```
Mes 4-6: Especialización
├── Elegir camino (Red/Blue/Cloud)
├── Herramientas especializadas
├── Labs avanzados
└── HackTheBox: Máquinas fáciles

Mes 7-9: Práctica
├── CTFs regulares
├── Bug bounty (con autorización)
├── Proyectos personales
└── Contribución a open source

Mes 10-12: Certificación
├── Preparar certificación
├── Estudiar guías oficiales
├── Prácticas de examen
└── Obtener primera cert
```

---

## 📊 Comparativa de Herramientas

### Nmap vs Masscan vs Zmap

| Característica | Nmap | Masscan | Zmap |
|----------------|------|---------|------|
| Velocidad | 🟡 Media | 🟢 Rápida | 🟢 Rápida |
| Precisión | 🟢 Alta | 🟡 Media | 🟡 Media |
| Uso de CPU | 🟡 Normal | 🔴 Alta | 🟡 Normal |
| Uso de RAM | 🟢 Baja | 🟡 Normal | 🟢 Baja |
| Ideal para | Escaneo completo | Redes grandes | Búsqueda rápida |

### Burp Suite vs OWASP ZAP

| Característica | Burp Suite | OWASP ZAP |
|----------------|------------|-----------|
| Precio | Freemium | Gratis |
| Facilidad | 🟡 Intermedio | 🟡 Intermedio |
| Comunidad | Grande | Grande |
| Plugins | Muchos | Algunos |
| Ideal para | Profesionales | Principiantes |

---

## 📋 Checklist de Instalación

### Entorno de Practica

```bash
# 1. VirtualBox instalado ✓
# 2. Ubuntu/Debian VM creada ✓
# 3. Kali Linux VM creada ✓
# 4. Herramientas básicas:
sudo apt update
sudo apt install -y \
    nmap \
    wireshark \
    nikto \
    sqlmap \
    burpsuite \
    metasploit-framework \
    python3-pip \
    git \
    curl \
    wget

# 5. Directorio de trabajo
mkdir -p ~/labs/{recon,exploit,forensics,malware}
```

---

## 🔄 Actualizaciones

| Fecha | Herramientas Agregadas |
|-------|------------------------|
| 2026-08-19 | Guía inicial completa |

---

*Herramientas curadas para la comunidad de ciberseguridad • CyberDefense Pro Network*
