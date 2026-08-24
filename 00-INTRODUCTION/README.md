> 🚀 **¿Eres principiante?** Esta carpeta es una intro específica. La **base completa para principiantes** del repo vive ahora en **[00-FUNDAMENTOS/](../fundamentos/)** — empieza ahí.
>
> Rutas desde la base: 🛡️ [Defensor](../fundamentos/rutas/ruta-defensor.md) · ⚔️ [Atacante](../fundamentos/rutas/ruta-atacante.md) · 🤖 [AI Security](../fundamentos/rutas/ruta-ai-security.md)

# 🎓 Introducción a la Ciberseguridad

## 👋 Bienvenido

Si estás empezando desde cero, este es tu punto de partida. Aquí aprenderás los fundamentos de la ciberseguridad de forma clara y práctica.

---

## 📋 Tabla de Contenidos

- [¿Qué es la Ciberseguridad?](#qué-es-la-ciberseguridad)
- [¿Por Qué es Importante?](#por-qué-es-importante)
- [Ramas de la Ciberseguridad](#ramas-de-la-ciberseguridad)
- [Conceptos Básicos](#conceptos-básicos)
- [Cómo Empezar](#cómo-empezar)
- [Recursos para Principiantes](#recursos-para-principiantes)
- [Tu Primera Semana](#tu-primera-semana)

---

## 🛡️ ¿Qué es la Ciberseguridad?

La **ciberseguridad** es la práctica de proteger sistemas, redes y programas de ataques digitales. Estos ataques suelen tener como objetivo acceder, cambiar o destruir información sensible.

### En palabras simples:

```
┌─────────────────────────────────────────────────────────────┐
│                    CIBERSEGURIDAD                           │
├─────────────────────────────────────────────────────────────┤
│                                                              │
│  Proteger:                                                   │
│  ├── 📱 Tus dispositivos (computadora, celular)             │
│  ├── 🌐 Tus datos (fotos, contraseñas, información)        │
│  ├── 💻 Tus cuentas (email, redes sociales, banco)         │
│  └── 🏢 Las empresas (servidores, bases de datos)          │
│                                                              │
│  Contra:                                                     │
│  ├── 🦠 Virus y malware                                     │
│  ├── 🎣 Phishing (correos falsos)                           │
│  ├── 🔓 Hackers (personas maliciosas)                       │
│  └── 💥 Ataques cibernéticos                                │
│                                                              │
└─────────────────────────────────────────────────────────────┘
```

---

## 🎯 ¿Por Qué es Importante?

### Datos que debes conocer:

| Dato | Impacto |
|------|---------|
| 🌍 **3.5 mil millones** | Correos electrónicos maliciosos enviados diariamente |
| 💰 **$10.5 billones** | Costo anual de la ciberdelincuencia para 2025 |
| 👨‍💼 **3.5 millones** | Empleos de ciberseguridad vacantes mundialmente |
| ⏱️ **Cada 39 segundos** | Ocurre un ataque cibernético |

### Ejemplos reales:

1. **Colonial Pipeline (2021)** - Ransomware que paralizó el suministro de combustible en EE.UU.
2. **SolarWinds (2020)** - Ataque que comprometió agencias gubernamentales
3. **Log4Shell (2021)** - Vulnerabilidad que afectó millones de aplicaciones

---

## 🔀 Ramas de la Ciberseguridad

### 1. 🔴 Seguridad Ofensiva (Red Team)

**¿Qué es?** Atacar sistemas para encontrar vulnerabilidades (con autorización).

```
Red Team = "El Bueno que se hace pasar por el Malo"
```

**Actividades:**
- Pentesting (pruebas de penetración)
- Explotación de vulnerabilidades
- Ingeniería social
- Bug bounty (cazar bugs por dinero)

**Herramientas:** Nmap, Burp Suite, Metasploit

**Ideal para:** Personas curiosas que les gusta resolver problemas

---

### 2. 🔵 Seguridad Defensiva (Blue Team)

**¿Qué es?** Proteger sistemas y detectar ataques.

```
Blue Team = "El Guardián que protege el castillo"
```

**Actividades:**
- Monitoreo de seguridad (SOC)
- Análisis de logs
- Respuesta a incidentes
- Configuración de firewalls

**Herramientas:** Wazuh, ELK Stack, Wireshark

**Ideal para:** Personas metódicas y detallistas

---

### 3. 🟣 Purple Team (Colaboración)

**¿Qué es?** Combinación de Red y Blue Team.

```
Purple Team = "El Equipo completo que ataca y defiende"
```

**Actividades:**
- Simulaciones de ataques
- Mejora continua
- Capacitación entre equipos

---

### 4. ☁️ Seguridad Cloud

**¿Qué es?** Proteger servicios en la nube (AWS, Azure, GCP).

```
Cloud Security = "Proteger tu información en el cielo digital"
```

**Actividades:**
- Auditorías cloud
- Seguridad de contenedores
- DevSecOps

---

### 5. 🦠 Análisis de Malware

**¿Qué es?** Estudiar virus y software malicioso.

```
Malware Analysis = "Ser el doctor que estudia la enfermedad"
```

**Actividades:**
- Análisis estático (sin ejecutar)
- Análisis dinámico (ejecutando en sandbox)
- Creación de reglas de detección

---

### 6. 🔍 Forense Digital

**¿Qué es?** Investigar crímenes digitales.

```
Digital Forensics = "El detective de la era digital"
```

**Actividades:**
- Recuperación de evidencia
- Análisis de discos duros
- Investigación de incidentes

---

## 📚 Conceptos Básicos

### 🔐 Autenticación vs Autorización

| Concepto | Definición | Ejemplo |
|----------|------------|---------|
| **Autenticación** | ¿Quién eres? | Login con usuario/contraseña |
| **Autorización** | ¿Qué puedes hacer? | Permisos de administrador |

### 🔑 Tipos de Autenticación

```
┌─────────────────────────────────────────────────────────────┐
│                 FACTORES DE AUTENTICACIÓN                   │
├─────────────────────────────────────────────────────────────┤
│                                                              │
│  1. Algo que SABES    → Contraseña, PIN                     │
│  2. Algo que TIENES   → Teléfono, tarjeta                   │
│  3. Algo que ERES     → Huella digital, rostro              │
│                                                              │
│  MFA = Usar 2 o más factores                                │
│                                                              │
└─────────────────────────────────────────────────────────────┘
```

### 🛡️ CIA Triad (Triada CIA)

El modelo fundamental de seguridad:

```
         CONFIDENCIALIDAD
              /\
             /  \
            /    \
           /  CIA  \
          /________\
         /          \
        /            \
INTEGRIDAD -------- DISPONIBILIDAD
```

| Pilar | Pregunta | Ejemplo |
|-------|----------|---------|
| **Confidencialidad** | ¿Quién puede ver la info? | Cifrado de datos |
| **Integridad** | ¿La info es correcta? | Firmas digitales |
| **Disponibilidad** | ¿Se puede acceder? | Backups, redundancia |

### 🌐 Protocolos de Seguridad

| Protocolo | Uso | Puerto |
|-----------|-----|--------|
| **HTTPS** | Web segura | 443 |
| **SSH** | Acceso remoto | 22 |
| **SSL/TLS** | Cifrado de datos | - |
| **VPN** | Red privada virtual | - |

---

## 🚀 Cómo Empezar

### Paso 1: Aprende lo Básico

```
Semana 1-2: Fundamentos
├── Instalar Linux (VirtualBox)
├── Aprender comandos básicos
├── Entender redes (TCP/IP)
└── Conceptos de seguridad
```

### Paso 2: Elige tu Camino

```
¿Qué te interesa más?
│
├── 🔴 Atacar sistemas → Red Team
├── 🔵 Defender sistemas → Blue Team
├── ☁️ Cloud y DevOps → Cloud Security
├── 🦠 Analizar malware → Malware Analysis
└── 🔍 Investigar crímenes → Forense Digital
```

### Paso 3: Practica

```
Plataformas gratuitas para practicar:
├── 🎮 TryHackMe (https://tryhackme.com)
├── 🎮 HackTheBox (https://hackthebox.com)
├── 🎮 PicoCTF (https://picoctf.org)
├── 🎮 OverTheWire (https://overthewire.org)
└── 🎮 VulnHub (https://vulnhub.com)
```

### Paso 4: Obtén Certificaciones

```
Certificaciones para principiantes:
├── 🥉 CompTIA Security+ (Básico)
├── 🥈 eLearnSecurity eJPT (Práctico)
├── 🥇 CompTIA CySA+ (Intermedio)
└── 🏆 OSCP (Avanzado)
```

---

## 📚 Recursos para Principiantes

### 🎥 Videos

| Recurso | Descripción | Link |
|---------|-------------|------|
| NetworkChuck | Tutoriales de redes y seguridad | YouTube |
| John Hammond | CTFs y Ciberseguridad | YouTube |
| David Bombal | Redes y Automatización | YouTube |
| The Cyber Mentor | Hacking Ético | YouTube |

### 📖 Cursos Gratuitos

| Curso | Plataforma | Duración |
|-------|------------|----------|
| Introduction to Cybersecurity | Cisco Networking Academy | 20 horas |
| IBM Cybersecurity Analyst | Coursera | 8 semanas |
| Cybersecurity for Beginners | Udemy | 4 horas |
| Pre-Security | TryHackMe | 35 horas |

### 📚 Libros para Principiantes

| Libro | Autor | Nivel |
|-------|-------|-------|
| "Cybersecurity for Beginners" | Raef Meeuwisse | 🟢 Básico |
| "The Web Application Hacker's Handbook" | Dafydd Stuttard | 🟡 Intermedio |
| "Hacking: The Art of Exploitation" | Jon Erickson | 🔴 Avanzado |

### 🛠️ Herramientas para Empezar

| Herramienta | Uso | Dificultad |
|-------------|-----|------------|
| **VirtualBox** | Crear máquinas virtuales | 🟢 Fácil |
| **Kali Linux** | Distribución de pentesting | 🟡 Intermedio |
| **Nmap** | Escaneo de redes | 🟡 Intermedio |
| **Wireshark** | Análisis de tráfico | 🟡 Intermedio |
| **Burp Suite** | Testing web | 🟡 Intermedio |

---

## 📅 Tu Primera Semana

### Día 1-2: Preparar Entorno

```bash
# 1. Descargar VirtualBox
# https://www.virtualbox.org/

# 2. Descargar Ubuntu Desktop
# https://ubuntu.com/download/desktop

# 3. Crear máquina virtual
# - 4GB RAM
# - 50GB disco
# - 2 cores CPU

# 4. Instalar Ubuntu en la VM
```

### Día 3-4: Aprender Linux

```bash
# Comandos esenciales
pwd                 # Ver directorio actual
ls                  # Listar archivos
cd                  # Cambiar directorio
mkdir               # Crear carpeta
touch               # Crear archivo
nano                # Editar archivo
sudo                # Ejecutar como administrador
apt update          # Actualizar repositorios
apt install         # Instalar software
```

### Día 5: Entender Redes

```
Conceptos clave:
├── IP Address (dirección de tu computadora en la red)
├── DNS (traduce nombres a IPs)
├── HTTP/HTTPS (protocolos web)
├── TCP/UDP (protocolos de transporte)
└── Ports (puertos de comunicación)
```

### Día 6: Primer Escaneo

```bash
# Instalar Nmap
sudo apt install nmap

# Escanear tu propia máquina
nmap localhost

# Escanear una web (con autorización)
nmap scanme.nmap.org
```

### Día 7: Explorar Plataformas

```
1. Crear cuenta en TryHackMe
2. Completar "Introduction to Cyber Security"
3. Explorar la ruta "Pre-Security"
4. Unirte a la comunidad de Discord
```

---

## 🎯 Objetivos del Mes 1

```
□ Completar entorno de práctica (Linux VM)
□ Aprender 20 comandos de Linux
□ Entender modelo OSI y TCP/IP
□ Escanear tu primera red con Nmap
□ Completar 5 rooms en TryHackMe
□ Crear tu primer script en Python
□ Unirte a comunidad de ciberseguridad
```

---

## 🤝 ¿Necesitas Ayuda?

### Comunidades para Principiantes

| Comunidad | Tipo | Link |
|-----------|------|------|
| TryHackMe Discord | Chat | https://discord.gg/tryhackme |
| HackTheBox Discord | Chat | https://discord.gg/hackthebox |
| r/cybersecurity | Reddit | https://reddit.com/r/cybersecurity |
| r/netsec | Reddit | https://reddit.com/r/netsec |

### Preguntas Frecuentes

**¿Necesito saber programar?**
> Sí, pero puedes empezar con lo básico. Python es el más recomendado.

**¿Necesito una computadora potente?**
> No, con 8GB de RAM y 50GB de espacio es suficiente para empezar.

**¿Cuánto tiempo toma aprender?**
> Los fundamentos en 1-2 meses. Ser profesional: 1-2 años.

**¿Es legal aprender hacking?**
> Sí, mientras practiques en entornos autorizados (labs, tu propia VM).

---

## 📊 Resumen

```
┌─────────────────────────────────────────────────────────────┐
│              TU CAMINO EN CIBERSEGURIDAD                    │
├─────────────────────────────────────────────────────────────┤
│                                                              │
│  🟢 Principiante (0-3 meses)                                │
│     └── Fundamentos, Linux, Redes                           │
│                                                              │
│  🟡 Intermedio (3-12 meses)                                 │
│     └── Especialización, Labs, Certificaciones              │
│                                                              │
│  🔴 Avanzado (1-2 años)                                     │
│     └── Experiencia real, Bug Bounty, Empleo                │
│                                                              │
│  💎 Experto (2+ años)                                       │
│     └── Investigación, Publicaciones, Mentoría              │
│                                                              │
└─────────────────────────────────────────────────────────────┘
```

---

## 🚀 Siguiente Paso

Una vez que completes esta introducción:

1. **Ve a la [Ruta de Fundamentos](../01-CIBERSEGURIDAD/README.md)**
2. **Comienza con Reconocimiento OSINT**
3. **Practica en TryHackMe**

---

*"El viaje de mil millas comienza con un solo paso."* 🛡️

**¡Bienvenido a la comunidad de ciberdefensa!**
