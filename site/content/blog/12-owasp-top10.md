---
title: "OWASP Top 10: las 10 vulnerabilidades web más peligrosas"
description: "Explicación práctica de cada vulnerabilidad del OWASP Top 10 con ejemplos y prevención"
author: Equipo CDPN
date: 2026-08-17
tags: [owasp, web-security, vulnerabilidades, appsec]
readingTime: 7 min
---

<script setup>
import { useData } from 'vitepress'
const { frontmatter } = useData()
</script>

<style>
.article-meta { display:flex; gap:0.8rem; flex-wrap:wrap; margin:0.8rem 0 1.5rem; font-size:0.85rem; color:var(--vp-c-text-3); }
.article-meta span { background:var(--vp-c-default-soft); padding:2px 10px; border-radius:6px; }
.article-meta .accent { background:var(--vp-c-brand-soft); color:var(--vp-c-brand-1); }
.owasp-item { border:1px solid var(--vp-c-divider); border-radius:10px; padding:1.2rem; margin:1rem 0; background:var(--vp-c-bg-soft); }
.owasp-item h3 { margin-top:0; }
</style>

# OWASP Top 10: las 10 vulnerabilidades web más peligrosas

<div class="article-meta">
  <span class="accent">📝 Equipo CDPN</span>
  <span>📅 17 Agosto 2026</span>
  <span>📖 7 min de lectura</span>
  <span>🏷️ OWASP</span>
  <span>🏷️ Web Security</span>
</div>

## ¿Qué es OWASP?

**OWASP** (Open Worldwide Application Security Project) es una organización open source dedicada a mejorar la seguridad del software. Su **Top 10** es la lista de las vulnerabilidades web más comunes y peligrosas, actualizada cada 3 años.

## El OWASP Top 10 (2021)

<div class="owasp-item">

### 🔴 A01: Broken Access Control (antes #5)

**¿Qué es?** Un usuario puede acceder a recursos o acciones que no debería.

```bash
# Ejemplo: IDOR (Insecure Direct Object Reference)
# Usuario 123 accede a:
GET /api/users/123/orders   → ✅ Sus propios pedidos
GET /api/users/456/orders   → ❌ Accede a los de otro usuario

# Por qué pasa: No se valida el ownership en el backend
```

**Prevención:**
- Validar permisos en el backend (nunca solo en el frontend)
- Usar UUIDs en vez de IDs incrementales
- Implementar RBAC (Role-Based Access Control)

</div>

<div class="owasp-item">

### 🔴 A02: Cryptographic Failures (antes #3)

**¿Qué es?** Datos sensibles se almacenan o transmiten sin cifrar adecuadamente.

```python
# MAL ❌
password = "admin123"  # Sin hash
db.save(password)

# BIEN ✅
import bcrypt
hashed = bcrypt.hashpw(password.encode(), bcrypt.gensalt())
db.save(hashed)
```

**Prevención:**
- Cifrar datos en reposo (AES-256) y en tránsito (TLS 1.3)
- Nunca almacenar passwords en texto plano
- Usar algoritmos actualizados (bcrypt, Argon2)

</div>

<div class="owasp-item">

### 🔴 A03: Injection (antes #1)

**¿Qué es?** Inyectar código malicioso en campos de entrada (SQL, NoSQL, OS, LDAP).

```sql
-- SQL Injection
-- Input: ' OR '1'='1' --
SELECT * FROM users WHERE name='' OR '1'='1' --';

-- Prevención: Prepared Statements
-- Python
cursor.execute("SELECT * FROM users WHERE name=%s", (user_input,))
```

**Prevención:**
- Prepared statements / parameterized queries
- Input validation (allowlists)
- WAF (Web Application Firewall)

</div>

<div class="owasp-item">

### 🟡 A04: Insecure Design (nuevo)

**¿Qué es?** Fallos en el diseño/architectura de la aplicación, no en la implementación.

```bash
# Ejemplo: Login sin rate limiting
# Un atacante puede hacer brute force sin restricciones

# Prevención: Threat Modeling en diseño
# 1. Identificar assets críticos
# 2. Enumerar amenazas por componente
# 3. Diseñar controles antes de codear
```

</div>

<div class="owasp-item">

### 🟡 A05: Security Misconfiguration (antes #6)

**¿Qué es?** Configuraciones por defecto, incompletas o inseguras.

```bash
# Ejemplos comunes:
# - Puertos abiertos innecesarios
# - Mensajes de error con stack traces
# - Cuentas default (admin/admin)
# - Headers HTTP faltantes (CSP, HSTS)
```

**Prevención:**
- Automatizar configuración con scripts reproducibles
- Revisar headers de seguridad (securityheaders.com)
- Deshabilitar debug en producción

</div>

<div class="owasp-item">

### 🟡 A06: Vulnerable and Outdated Components (antes #9)

**¿Qué es?** Usar libraries, frameworks o componentes con vulnerabilidades conocidas.

```bash
# Detectar dependencias vulnerables
npm audit              # Node.js
pip-audit              # Python
docker scout cves .    # Docker images

# Ejemplo: Usar Log4j 2.14 (vulnerable a Log4Shell)
# Fix: Actualizar a 2.17+
```

</div>

<div class="owasp-item">

### 🟡 A07: Identification and Authentication Failures (antes #2)

**¿Qué es?** Debilidades en la autenticación (login, sesiones, tokens).

```bash
# Problemas comunes:
# - Brute force sin rate limiting
# - Sesiones no expiran
# - Tokens predecibles
# - MFA no implementado
```

**Prevención:**
- Implementar MFA (Multi-Factor Authentication)
- Rate limiting en endpoints de autenticación
- Usar frameworks de auth probados (OAuth2, OIDC)

</div>

<div class="owasp-item">

### 🟡 A08: Software and Data Integrity Failures (antes #8)

**¿Qué es?** No verificar la integridad de software actualizaciones o datos.

```bash
# Ejemplo: Supply chain attack
# Un paquete npm es comprometido con código malicioso
# Si no verificas hashes, instalas malware

# Prevención:
npm install --package-lock-only
# Verificar checksums de downloads
# Usar SLSA framework para supply chain
```

</div>

<div class="owasp-item">

### 🟢 A09: Security Logging and Monitoring Failures (antes #10)

**¿Qué es?** No registrar eventos de seguridad ni monitorear anomalías.

```bash
# Qué loggear:
# - Intentos de login fallidos
# - Accesos a recursos sensibles
# - Errores de aplicación
# - Cambios en configuración

# Herramientas:
# - ELK Stack (Elasticsearch + Logstash + Kibana)
# - Wazuh (SIEM open source)
# - OSSEC (HIDS)
```

</div>

<div class="owasp-item">

### 🟢 A10: Server-Side Request Forgery - SSRF (antes #10)

**¿Qué es?** El servidor hace peticiones a recursos internos en nombre del atacante.

```python
# Ejemplo vulnerable
url = request.args.get('url')
response = requests.get(url)  # El servidor accede a cualquier URL

# Atacante envía: ?url=http://169.254.169.254/latest/meta-data/
# Accede a los metadata de AWS (credenciales)

# Prevención: Allowlist de URLs permitidas
ALLOWED_HOSTS = ['api.miservidor.com']
```

</div>

## Resumen rápido

| # | Vulnerabilidad | Frecuencia | Impacto |
|---|---------------|------------|---------|
| A01 | Broken Access Control | 🔴 Alta | 🔴 Alto |
| A02 | Cryptographic Failures | 🟡 Media | 🔴 Alto |
| A03 | Injection | 🟡 Media | 🔴 Alto |
| A04 | Insecure Design | 🟡 Media | 🟡 Medio |
| A05 | Security Misconfiguration | 🔴 Alta | 🟡 Medio |
| A06 | Vulnerable Components | 🔴 Alta | 🟡 Medio |
| A07 | Auth Failures | 🟡 Media | 🔴 Alto |
| A08 | Integrity Failures | 🟢 Baja | 🔴 Alto |
| A09 | Logging Failures | 🟡 Media | 🟡 Medio |
| A10 | SSRF | 🟢 Baja | 🔴 Alto |

## Recursos

- **owasp.org/www-project-top-ten** — Top 10 oficial
- **OWASP Juice Shop** — App vulnerable para practicar
- **PortSwigger Web Security Academy** — Labs gratuitos
- **HackTheBox Starting Point** — Machines guiadas

## Conclusión

El OWASP Top 10 no es solo una lista de考試 — es un **mapa de carreteras** para entender dónde están los peligros en cualquier aplicación web. Si dominas estas 10 categorías, entiendes el 90% de las vulnerabilidades web.

---

*Artículo publicado en el Blog CDPN — Semana 12*
