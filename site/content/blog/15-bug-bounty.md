---
title: "Bug Bounty: gana dinero encontrando vulnerabilidades"
description: "Cómo empezar en bug bounty, plataformas, metodología y tips para encontrar tu primer bounty"
author: Equipo CDPN
date: 2026-09-07
tags: [bugbounty, hackerone, bugcrowd, rewards, career]
readingTime: 5 min
---

<script setup>
import { useData } from 'vitepress'
const { frontmatter } = useData()
</script>

<style>
.article-meta { display:flex; gap:0.8rem; flex-wrap:wrap; margin:0.8rem 0 1.5rem; font-size:0.85rem; color:var(--vp-c-text-3); }
.article-meta span { background:var(--vp-c-default-soft); padding:2px 10px; border-radius:6px; }
.article-meta .accent { background:var(--vp-c-brand-soft); color:var(--vp-c-brand-1); }
</style>

# Bug Bounty: gana dinero encontrando vulnerabilidades

<div class="article-meta">
  <span class="accent">📝 Equipo CDPN</span>
  <span>📅 7 Septiembre 2026</span>
  <span>📖 5 min de lectura</span>
  <span>🏷️ Bug Bounty</span>
  <span>🏷️ HackerOne</span>
</div>

## ¿Qué es Bug Bounty?

**Bug Bounty** es un programa donde empresas pagan a investigadores de seguridad por encontrar y reportar vulnerabilidades en sus sistemas. Es la forma más ética y lucrativa de practicar hacking.

### Pagos reales

| Vulnerabilidad | Pago promedio | Récord |
|---------------|---------------|--------|
| **Critical (RCE)** | $5,000 - $50,000 | $250,000+ |
| **High (Auth Bypass)** | $2,000 - $10,000 | $100,000+ |
| **Medium (XSS)** | $500 - $2,000 | $10,000+ |
| **Low (Info Disclosure)** | $100 - $500 | $2,000+ |

> 💡 **Dato:** El top bug bounty hunter del mundo ganó **$4.1 millones** en 2024.

## Plataformas principales

| Plataforma | Empresas | Pago mínimo | Link |
|------------|----------|-------------|------|
| **HackerOne** | 2,000+ | $150 | hackerone.com |
| **Bugcrowd** | 500+ | $100 | bugcrowd.com |
| **Intigriti** | 1,500+ | €50 | intigriti.com |
| **YesWeHack** | 1,000+ | €100 | yeswehack.com |
| **Open Bug Bounty** | 5,000+ | Sin mínimo | openbugbounty.org |

## Metodología de un bug bounty hunter

### Fase 1: Reconocimiento

```bash
# Enumerar subdominios
subfinder -d target.com -o subdomains.txt
amass enum -d target.com >> subdomains.txt

# Encontrar endpoints
katana -u https://target.com -d 3 -jc -o urls.txt

# Buscar archivos sensibles
dirsearch -u https://target.com -w /usr/share/wordlists/dirb/common.txt
```

### Fase 2: Análisis

```
🔍 Buscar vulnerabilidades comunes:
├── SQL Injection (sqlmap)
├── XSS (Reflected, Stored, DOM)
├── IDOR (Insecure Direct Object Reference)
├── SSRF (Server-Side Request Forgery)
├── Authentication Bypass
├── Race Conditions
├── Business Logic Flaws
└── API vulnerabilities (BOLA, mass assignment)
```

### Fase 3: Explotación controlada

```bash
# Probar XSS
"><script>alert(1)</script>
"><img src=x onerror=alert(1)>
javascript:alert(1)

# Probar SSRF
?url=http://169.254.169.254/latest/meta-data/
?url=http://localhost:8080/admin

# Probar IDOR
GET /api/users/123/profile   → tu perfil
GET /api/users/456/profile   → ¿ves el de otro?
```

### Fase 4: Reporte

```markdown
# Reporte de ejemplo

## Título: IDOR en API de perfil de usuario

## Resumen
Un usuario autenticado puede acceder al perfil de cualquier 
otro usuario cambiando el ID en la URL.

## Severidad: HIGH

## Pasos para reproducir
1. Login como user1 (user1@test.com / test123)
2. Navegar a GET /api/users/123/profile
3. Cambiar 123 por 456 (ID de user2)
4. Se muestran los datos de user2 (email, teléfono, dirección)

## Impacto
Exposición de datos personales de todos los usuarios (PII leak).

## Impacto económico
Potencial violación de GDPR con multas de hasta €20M.
```

## Tips para encontrar tu primer bounty

### 1. Empieza por programas pequeños

```
❌ NO empieces por Google, Apple, Microsoft
✅ Empieza por startups y empresas medianas
→ Menos competencia, más fácil encontrar bugs
```

### 2. Focus en los "Low Hanging Fruit"

```
🔎 XSS en campos de búsqueda
🔎 IDOR en endpoints de API
🔎 Information Disclosure en headers
🔎 Missing rate limiting en login
🔎 CORS misconfiguration
🔎 Exposed .git / .env files
```

### 3. Herramientas esenciales

| Herramienta | Uso |
|-------------|-----|
| **Burp Suite** | Proxy y testing de APIs |
| **Nuclei** | Scanner de vulnerabilidades |
| **httpx** | Descubrir servicios |
| **ffuf** | Fuzzing de directorios |
| **sqlmap** | SQL injection automatizado |
| **XSStrike** | XSS detection |

### 4. Lee writeups de otros

```bash
# CTF writeups y bug bounty writeups son oro puro
# Recursos:
# - github.com/arkadiyt/bounty-targets-data
# - medium.com/tag/bug-bounty
# - bugs.huntr.com
```

## Errores comunes de principiantes

1. **No leer el scope** — Solo testea los dominios permitidos
2. **Reportar duplicados** — Busca antes si ya fue reportado
3. **No explicar el impacto** — El bounty depende del impacto, no solo de la漏洞
4. **Automatizar de más** — Los bugs de lógica de negocio se encuentran manualmente
5. **No tener paciencia** — El primer bounty puede tardar meses

## Progresión típica

```
Mes 1-3:   Aprender herramientas, resolver CTFs
Mes 3-6:   Empezar en bug bounty, primeros reports
Mes 6-12:  Encontrar primer bounty ($100-$500)
Año 1-2:   Bounty regular ($500-$2000/bounty)
Año 2+:    Top hunter ($5000+/bounty)
```

## Conclusión

Bug bounty es una carrera donde **tu habilidad = tu salario**. No necesitas título, solo habilidad, paciencia y ética. El primer bounty es el más difícil — después, se vuelve adictivo.

---

*Artículo publicado en el Blog CDPN — Semana 15*
