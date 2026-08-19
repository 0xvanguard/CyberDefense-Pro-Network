# 📡 IoT Security / Seguridad de Internet de las Cosas

## 📋 Descripción

Módulo dedicado a la seguridad de dispositivos IoT: cámaras, routers, dispositivos médicos, smart home y más.

**Nivel:** Intermedio-Avanzado

**Duración estimada:** 4-6 semanas

**Prerrequisitos:**
- Conocimientos básicos de redes
- Linux básico
- Python básico (opcional)

---

## ⚠️ ADVERTENCIA ÉTICA

> **🚨 IMPORTANTE:** Este módulo es estrictamente educativo.
>
> - ✅ Analizar dispositivos propios o autorizados
> - ✅ Usar entornos de laboratorio
> - ✅ Investigación con autorización
> - ❌ **NUNCA** acceder a dispositivos ajenos sin permiso
> - ❌ **NUNCA** causar daño a dispositivos

---

## 🎯 Objetivos de Aprendizaje

Al completar este módulo serás capaz de:

- ✅ Entender la arquitectura de dispositivos IoT
- ✅ Identificar vulnerabilidades comunes en IoT
- ✅ Realizar análisis de firmware
- ✅ Auditorizar redes IoT
- ✅ Implementar controles de seguridad IoT
- ✅ Responder a incidentes en dispositivos IoT

---

## 🗂️ Contenido del Módulo

### 📚 Teoría

| Archivo | Tema |
|---------|------|
| [01-fundamentos-iot.md](teoria/01-fundamentos-iot.md) | Conceptos y arquitectura IoT |
| [02-amenazas-iot.md](teoria/02-amenazas-iot.md) | Amenazas y vectores de ataque |
| [03-firmware-analysis.md](teoria/03-firmware-analysis.md) | Análisis de firmware |
| [04-network-iot.md](teoria/04-network-iot.md) | Seguridad de redes IoT |
| [05-cloud-iot.md](teoria/05-cloud-iot.md) | Seguridad en la nube IoT |
| [06-ics-scada.md](teoria/06-ics-scada.md) | Sistemas de control industrial |

### 🔧 Herramientas

| Herramienta | Propósito | Categoría |
|-------------|-----------|-----------|
| [Binwalk](herramientas/binwalk.md) | Análisis de firmware | Firmware |
| [Firmware-Mod-Kit](herramientas/fmk.md) | Modificación de firmware | Firmware |
| [RouterSploit](herramientas/routersploit.md) | Exploits para routers | Explotación |
| [Shodan](herramientas/shodan.md) | Búsqueda de dispositivos IoT | Reconocimiento |
| [Wireshark](herramientas/wireshark.md) | Análisis de tráfico | Red |
| [Mosquitto](herramientas/mosquitto.md) | MQTT broker para testing | Red |

### 🧪 Laboratorios

| Laboratorio | Nivel | Dispositivo |
|-------------|-------|-------------|
| [lab-01-firmware-analysis](laboratorios/lab-01-firmware-analysis/) | Intermedio | Router TP-Link |
| [lab-02-camera-hacking](laboratorios/lab-02-camera-hacking/) | Avanzado | IP Camera |
| [lab-03-smart-home](laboratorios/lab-03-smart-home/) | Intermedio | Smart Home Hub |
| [lab-04-ics-scada](laboratorios/lab-04-ics-scada/) | Avanzado | PLC Siemens |

---

## 🚀 Inicio Rápido

### Herramientas Necesarias

```bash
# Binwalk (análisis de firmware)
sudo apt install binwalk

# RouterSploit
git clone https://github.com/threat9/routersploit
cd routersploit
pip install -r requirements.txt

# Shodan CLI
pip install shodan

# MQTT client
pip install paho-mqtt
```

### Primer Ejercicio

```bash
# 1. Clona el repositorio
git clone https://github.com/0xvanguard/CyberDefense-Pro-Network.git
cd CyberDefense-Pro-Network/01-CIBERSEGURIDAD/11-iot-security/

# 2. Analiza un firmware de ejemplo
binwalk firmware.bin

# 3. Busca dispositivos IoT en Shodan
shodan search "webcam has_screenshot:true"
```

---

## 📊 Arquitectura IoT Típica

```
┌─────────────────────────────────────────────────────────────┐
│                    ARQUITECTURA IoT                         │
├─────────────────────────────────────────────────────────────┤
│                                                              │
│  ┌─────────────┐    ┌─────────────┐    ┌─────────────┐     │
│  │  Dispositivo │    │  Gateway    │    │  Cloud      │     │
│  │  (Sensor)    │───▶│  (Router)   │───▶│  (Servidor) │     │
│  └─────────────┘    └─────────────┘    └─────────────┘     │
│         │                  │                  │              │
│         ▼                  ▼                  ▼              │
│  ┌─────────────┐    ┌─────────────┐    ┌─────────────┐     │
│  │  Firmware    │    │  Red        │    │  API        │     │
│  │  Análisis    │    │  Análisis   │    │  Análisis   │     │
│  └─────────────┘    └─────────────┘    └─────────────┘     │
│                                                              │
└─────────────────────────────────────────────────────────────┘
```

---

## 🔍 Vulnerabilidades Comunes en IoT

### 1. Credenciales por Defecto

```bash
# Lista de credenciales comunes
admin:admin
admin:password
root:root
admin:(vacío)
root:admin
```

### 2. Firmware sin Actualizar

```bash
# Verificar versión de firmware
curl http://dispositivo/firmware_version
# Buscar CVEs para esa versión
```

### 3. Servicios Expuertos

```bash
# Escaneo de puertos
nmap -sV -p- dispositivo_ip

# Servicios comunes en IoT
# 23 (Telnet), 80 (HTTP), 443 (HTTPS)
# 554 (RTSP), 1883 (MQTT), 8883 (MQTT-S)
```

### 4. Firmware con Credenciales Hardcodeadas

```bash
# Extraer firmware
binwalk -e firmware.bin

# Buscar credenciales
grep -r "password" squashfs-root/
grep -r "admin" squashfs-root/
grep -r "secret" squashfs-root/
```

### 5. Comunicaciones sin Cifrar

```bash
# Capturar tráfico MQTT
mosquitto_sub -h broker_ip -t "#"

# Analizar tráfico con Wireshark
# Filtro: mqtt
```

---

## 🏭 IoT en Industria (ICS/SCADA)

### Protocolos Comunes

| Protocolo | Puerto | Uso |
|-----------|--------|-----|
| Modbus | 502 | Automatización industrial |
| DNP3 | 20000 | Redes eléctricas |
| OPC UA | 4840 | Comunicación industrial |
| BACnet | 47808 | Edificios inteligentes |

### Herramientas ICS/SCADA

```bash
# Modbus scanning
nmap --script modbus-discover -p 502 target_ip

# DNP3 enumeration
nmap --script dnp3-info -p 20000 target_ip
```

---

## 📡 Protocolos IoT

### MQTT (Message Queuing Telemetry Transport)

```bash
# Conectar a broker MQTT
mosquitto_sub -h broker_ip -t "home/sensor/#"

# Publicar mensaje
mosquitto_pub -h broker_ip -t "home/light" -m "on"
```

### CoAP (Constrained Application Protocol)

```bash
# Request CoAP
coap-client -m get coap://dispositivo/sensores
```

### Zigbee/Z-Wave

```
# Análisis con SDR (Software Defined Radio)
# Requiere hardware especializado
```

---

## 🛡️ Controles de Seguridad IoT

### Checklist de Seguridad

```markdown
## IoT Security Checklist

### Dispositivo
- [ ] Credenciales por defecto cambiadas
- [ ] Firmware actualizado
- [ ] Servicios innecesarios deshabilitados
- [ ] Cifrado habilitado (TLS/SSL)
- [ ] Secure boot implementado

### Red
- [ ] VLAN separada para IoT
- [ ] Firewall configurado
- [ ] Tráfico monitoreado
- [ ] Acceso a internet restringido
- [ ] VPN para acceso remoto

### Cloud/API
- [ ] Autenticación robusta
- [ ] Rate limiting implementado
- [ ] API keys rotadas regularmente
- [ ] Logs habilitados
- [ ] Datos cifrados en reposo

### Físico
- [ ] Puerto UART/JTAG deshabilitado
- [ ] Modo de fábrica protegido
- [ ] Etiquetas de seguridad
```

---

## 📊 Dispositivos IoT Comunes

### Smart Home

| Dispositivo | Vulnerabilidades | Riesgo |
|-------------|------------------|--------|
| Cámaras IP | Credenciales débiles, RTSP abierto | Alto |
| Smart Locks | Bluetooth sniffing, API flaws | Crítico |
| Termostatos | Firmware outdated, cloud issues | Medio |
| Asistentes voice | Eavesdropping, skills maliciosos | Medio |

### Industrial

| Dispositivo | Vulnerabilidades | Riesgo |
|-------------|------------------|--------|
| PLCs | Sin autenticación, protocolos claros | Crítico |
| RTUs | Modbus sin cifrar | Crítico |
| HMIs | Web interfaces expuestas | Alto |
| SCADA | Redes no segmentadas | Crítico |

### Healthcare

| Dispositivo | Vulnerabilidades | Riesgo |
|-------------|------------------|--------|
| Infusion pumps | Firmware bugs, red compartida | Crítico |
| Monitores cardiacos | Wireless sniffing | Crítico |
| DICOM systems | Sin cifrado | Alto |

---

## 📚 Recursos

### Fuentes de Investigación

| Fuente | Tipo | Link |
|--------|------|------|
| OWASP IoT | Proyecto | https://owasp.org/www-project-internet-of-things/ |
| IoT Security Foundation | Organización | https://iotsecurityfoundation.org/ |
| ICS-CERT | Advisories | https://www.cisa.gov/ics-cert |
| Shodan | Búsqueda | https://shodan.io |

### Certificaciones

| Certificación | Enfoque |
|---------------|---------|
| GIAC ICS | Industrial Control Systems |
| GICSP | Global ICS Cyber Security |
| Certified IoT Security | IoT Security |

### Cursos

| Curso | Plataforma |
|-------|------------|
| IoT Security | SANS |
| ICS Security | SANS |
| IoT Hacking | Offensive Security |

---

## 📝 Templates

- [TEMPLATE-iot-audit.md](portafolio/TEMPLATE-iot-audit.md)
- [TEMPLATE-firmware-report.md](portafolio/TEMPLATE-firmware-report.md)

---

## 🔄 Actualizaciones

| Fecha | Cambio |
|-------|--------|
| 2026-08-19 | Módulo creado |

---

*Parte de [CyberDefense Pro Network](../../../../README.md)*
