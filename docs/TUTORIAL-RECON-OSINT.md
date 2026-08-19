# 🎓 Tutorial: Reconocimiento OSINT Paso a Paso

## 📋 Información del Tutorial

| Campo | Valor |
|-------|-------|
| **Nivel** | Principiante |
| **Duración** | 45-60 minutos |
| **Objetivo** | Realizar reconocimiento OSINT completo de un dominio |
| **Herramientas** | recon_automatizado.py, TheHarvester |
| **Prerrequisitos** | Python 3.8+, conexión a internet |

---

## 🎯 Objetivos de Aprendizaje

Al completar este tutorial serás capaz de:

1. ✅ Entender qué es el reconocimiento OSINT
2. ✅ Usar recon_automatizado.py para enumerar subdominios
3. ✅ Crear wordlists personalizadas
4. ✅ Analizar y documentar resultados
5. ✅ Identificar superficie de ataque

---

## 📚 Teoría: ¿Qué es el Reconocimiento OSINT?

### Definición

**OSINT (Open Source Intelligence)** es la recopilación de información de fuentes públicas. En ciberseguridad, se refiere a recopilar información sobre un objetivo sin interactuar directamente con sus sistemas.

### Fases del Reconocimiento

```
┌─────────────────────────────────────────────────────────────┐
│                    RECONOCIMIENTO OSINT                     │
├─────────────────────────────────────────────────────────────┤
│  1. Definición del alcance (Scope)                          │
│  2. Recopilación de información básica                      │
│  3. Enumeración de subdominios                              │
│  4. Identificación de servicios                            │
│  5. Análisis de superficie de ataque                        │
│  6. Documentación de hallazgos                              │
└─────────────────────────────────────────────────────────────┘
```

### Fuentes de Información

| Fuente | Tipo | Ejemplo |
|--------|------|---------|
| **DNS** | Técnica | Resolución de dominios |
| **WHOIS** | Técnica | Información de registro |
| **Search Engines** | Humana | Google, Bing |
| **Redes Sociales** | Humana | LinkedIn, Twitter |
| **GitHub** | Técnica | Repositorios públicos |
| **Shodan** | Técnica | Dispositivos IoT |
| **Censys** | Técnica | Certificados SSL |

---

## 🛠️ Preparación del Entorno

### Paso 1: Clonar el Repositorio

```bash
# Clonar repositorio
git clone https://github.com/0xvanguard/CyberDefense-Pro-Network.git
cd CyberDefense-Pro-Network/01-CIBERSEGURIDAD/01-reconocimiento-osint/herramientas/

# Verificar archivos
ls -la
# Deberías ver:
# - recon_automatizado.py
# - theharvester.md
# - README.md
```

### Paso 2: Verificar Python

```bash
# Verificar versión de Python
python3 --version
# Debe mostrar Python 3.8 o superior

# Dar permisos de ejecución
chmod +x recon_automatizado.py
```

### Paso 3: Crear Directorio de Trabajo

```bash
# Crear directorio para este tutorial
mkdir -p ~/labs/tutorial-recon
cd ~/labs/tutorial-recon

# Crear wordlist básica
cat > wordlist_basica.txt << 'EOF'
# Subdominios comunes
www
mail
ftp
api
admin
test
dev
staging
portal
webmail
blog
shop
store
app
mobile
EOF

# Verificar wordlist
cat wordlist_basica.txt
```

---

## 🚀 Ejercicio Práctico

### Escenario

Eres un consultor de seguridad contratado para realizar un reconocimiento inicial de **ejemplo.com** (dominio ficticio para práctica). El cliente te dio autorización por escrito.

### Paso 1: Reconocimiento Inicial

```bash
# Ejecutar reconocimiento básico
python3 recon_automatizado.py -d ejemplo.com
```

**Salida esperada:**
```
  ____  _____ _____ _   _     ____  _   _ _____ ____
 |  _ \| ____| ____| \ | |   / ___|| | | | ____|  _ \
 | |_) |  _| |  _| |  \| |   \___ \| |_| |  _| | |_) |
 |  _ <| |___| |___| |\  |    ___) |  _  | |___|  _ <
 |_| \_\_____|_____|_| \_|   |____/|_| |_|_____|_| \_\
            Reconocimiento OSINT automatizado

[*] Inicio: 2026-08-19T10:30:00.000000
[*] Objetivo: ejemplo.com
============================================================
[+] ejemplo.com -> 93.184.216.34
```

**Análisis:**
- ✅ Dominio resuelve correctamente
- ✅ Se obtuvo dirección IP principal
- 📝 Anotar IP: `93.184.216.34`

### Paso 2: Enumeración de Subdominios

```bash
# Ejecutar con wordlist
python3 recon_automatizado.py -d ejemplo.com -w wordlist_basica.txt
```

**Salida esperada:**
```
[*] Enumerando subdominios con wordlist_basica.txt ...
[+] 5 subdominios resueltos
    mail.ejemplo.com                           -> 93.184.216.35
    www.ejemplo.com                            -> 93.184.216.34
    api.ejemplo.com                            -> 93.184.216.36
    ftp.ejemplo.com                            -> 93.184.216.37
    dev.ejemplo.com                            -> 93.184.216.38
[*] Consultando títulos HTTP/HTTPS ...
    www.ejemplo.com                            | Bienvenido a Ejemplo
    mail.ejemplo.com                           | Webmail - Ejemplo
    api.ejemplo.com                            | API Documentation
```

**Análisis:**
- ✅ 5 subdominios encontrados
- 🔍 Subdominios interesantes:
  - `api.ejemplo.com` - Posible API expuesta
  - `dev.ejemplo.com` - Posible entorno de desarrollo
  - `ftp.ejemplo.com` - Servicio FTP (verificar)
- 📝 Anotar IPs y títulos

### Paso 3: Guardar Resultados

```bash
# Guardar informe completo
python3 recon_automatizado.py -d ejemplo.com -w wordlist_basica.txt -o recon_ejemplo.json

# Verificar que se creó
ls -la recon_ejemplo.json

# Ver resultado formateado
cat recon_ejemplo.json | python3 -m json.tool
```

### Paso 4: Análisis de Resultados

```bash
# Extraer subdominios encontrados
cat recon_ejemplo.json | python3 -c "
import sys, json
data = json.load(sys.stdin)
print('=== Subdominios Encontrados ===')
for sub, ips in data.get('subdominios', {}).items():
    print(f'{sub} -> {", ".join(ips)}')
print()
print('=== Títulos de Páginas ===')
for url, title in data.get('titles', {}).items():
    print(f'{url} -> {title}')
"
```

### Paso 5: Crear Informe

Crear archivo `informe-recon.md`:

```markdown
# Informe de Reconocimiento OSINT

## Información General
- **Dominio:** ejemplo.com
- **Fecha:** 2026-08-19
- **Analista:** [Tu nombre]
- **Autorización:** Sí (documento #XXX)

## Resumen Ejecutivo
Se realizó reconocimiento OSINT del dominio ejemplo.com, encontrando 5 subdominios activos y 3 servicios HTTP/HTTPS.

## Hallazgos

### Subdominios Encontrados

| Subdominio | IP | Servicio | Estado |
|------------|-----|----------|--------|
| www.ejemplo.com | 93.184.216.34 | HTTP/HTTPS | ✅ Activo |
| mail.ejemplo.com | 93.184.216.35 | HTTP/HTTPS | ✅ Activo |
| api.ejemplo.com | 93.184.216.36 | HTTP/HTTPS | ✅ Activo |
| ftp.ejemplo.com | 93.184.216.37 | FTP | ⚠️ Verificar |
| dev.ejemplo.com | 93.184.216.38 | HTTP/HTTPS | ⚠️ Entorno dev |

### Análisis de Riesgos

1. **api.ejemplo.com** - API expuesta públicamente
   - Riesgo: Posible acceso no autorizado
   - Acción: Verificar autenticación y autorización

2. **dev.ejemplo.com** - Entorno de desarrollo
   - Riesgo: Posible información sensible
   - Acción: Restringir acceso

3. **ftp.ejemplo.com** - Servicio FTP
   - Riesgo: Transferencia no cifrada
   - Acción: Verificar si es necesario, considerar SFTP

## Recomendaciones

1. Restringir acceso a dev.ejemplo.com
2. Auditar API en api.ejemplo.com
3. Migrar FTP a SFTP o SSH
4. Implementar monitoring en todos los servicios

## Próximos Pasos

1. Escaneo de puertos en IPs encontradas
2. Análisis de servicios HTTP/HTTPS
3. Pruebas de seguridad en endpoints
4. Verificación de vulnerabilidades

## Evidencia
- Archivo JSON: `recon_ejemplo.json`
- Capturas de pantalla: [Si aplica]

---
*Informe generado el 2026-08-19*
```

---

## 📊 Análisis de Superficie de Ataque

### ¿Qué es la Superficie de Ataque?

Es el conjunto de todos los puntos donde un atacante puede intentar entrar a un sistema.

### Mapeo de Superficie

```
ejemplo.com
├── www.ejemplo.com (93.184.216.34)
│   ├── HTTP/HTTPS
│   ├── Posibles vulnerabilidades: XSS, SQLi, CSRF
│   └── Acción: Análisis web
│
├── mail.ejemplo.com (93.184.216.35)
│   ├── HTTP/HTTPS (Webmail)
│   ├── Posibles vulnerabilidades: Phishing, credenciales
│   └── Acción: Verificar autenticación
│
├── api.ejemplo.com (93.184.216.36)
│   ├── HTTP/HTTPS (API)
│   ├── Posibles vulnerabilidades: IDOR, BOLA, rate limiting
│   └── Acción: Auditoría de API
│
├── ftp.ejemplo.com (93.184.216.37)
│   ├── FTP
│   ├── Posibles vulnerabilidades: Credenciales débiles, anonymous
│   └── Acción: Verificar configuración
│
└── dev.ejemplo.com (93.184.216.38)
    ├── HTTP/HTTPS
    ├── Posibles vulnerabilidades: Código expuesto, debug activo
    └── Acción: Restringir acceso
```

---

## ✅ Verificación del Aprendizaje

### Preguntas de Comprensión

1. **¿Qué es OSINT?**
   - Respuesta esperada: Recopilación de información de fuentes públicas

2. **¿Por qué es importante el reconocimiento?**
   - Respuesta esperada: Para entender la superficie de ataque antes de probar vulnerabilidades

3. **¿Qué información puedes obtener con recon_automatizado.py?**
   - Respuesta esperada: Subdominios, IPs, títulos de páginas

4. **¿Por qué debes crear una wordlist personalizada?**
   - Respuesta esperada: Para encontrar subdominios específicos del objetivo

### Ejercicio Final

**Objetivo:** Realizar reconocimiento completo de un dominio de práctica.

**Instrucciones:**

1. Elegir un dominio de práctica (ej: tryhackme.com, hackthebox.com)
2. Crear wordlist personalizada
3. Ejecutar recon_automatizado.py
4. Analizar resultados
5. Crear informe completo
6. Identificar 3 áreas de interés para pruebas futuras

**Entregable:** Informe en Markdown con análisis y recomendaciones

---

## 📚 Recursos Adicionales

### Lecturas Recomendadas
- [MITRE ATT&CK - Reconnaissance](https://attack.mitre.org/techniques/T1596/)
- [OWASP Testing Guide - Information Gathering](https://owasp.org/www-project-web-security-testing-guide/)
- [PTES - Intelligence Gathering](http://www.pentest-standard.org/index.php/Intelligence_Gathering)

### Práctica Adicional
- [TryHackMe - OSINT](https://tryhackme.com/room/ohsint)
- [HackTheBox - OSINT Challenges](https://www.hackthebox.com/)
- [PicoCTF - OSINT](https://picoctf.org/)

---

## 🎯 Siguientes Pasos

Después de completar este tutorial:

1. **Practicar** con más dominios
2. **Aprender** TheHarvester
3. **Combinar** herramientas para mejores resultados
4. **Avanzar** al siguiente módulo: Escaneo y Enumeración

---

*Tutorial creado para CyberDefense Pro Network • 2026*
