# 📅 Sesión 2026-08-21 — Expansión de Módulos y Correcciones

## 🎯 Objetivos de la sesión
1. Corregir sidebar que daba 404 al hacer clic en módulos
2. Expandir contenido de blue-team y purple-team
3. Mejorar módulos de fundamentos con ejercicios prácticos
4. Corregir workflow Validate Content

---

## ✅ Logros completados

### 1. Corrección del Sidebar (404 fix)

**Problema raíz:**
- VitePost generaba links con extensión `.html` en el sidebar
- El postbuild convertía archivos a directorios (`file.html` → `file/index.html`)
- Los links `.html` quedaban rotos después de la conversión
- GitHub Actions sobreescribía `content/.vitepress/` con `site/.vitepress/` (config viejo)

**Soluciones aplicadas:**
- Habilitado `cleanUrls: true` en VitePress config
- Agregado `fixSidebarLinks` al postbuild para limpiar links `.html` residuales
- Sincronizado `site/.vitepress/config.mjs` con `site/content/.vitepress/config.mjs`

**Commits:**
- `747ff41` — fix(sidebar): corrige links .html rotos y agrega módulos faltantes
- `8238e4f` — fix(sidebar): agrega 5 módulos faltantes a sidebar AI Agents
- `d89fd5c` — fix(config): sincroniza config.mjs con version vieja en site/.vitepress

---

### 2. Expansión de Blue Team (5 módulos nuevos)

| # | Módulo | Tema | Líneas |
|---|--------|------|--------|
| 02 | Análisis de Incidentes | NIST SP 800-61, Volatility, YARA | ~200 |
| 03 | Threat Hunting | MITRE ATT&CK, Sigma, Velociraptor | ~185 |
| 04 | SIEM y Monitoreo | Wazuh, ELK, Splunk | ~184 |
| 05 | Hardening y Seguridad | CIS Benchmark, Lynis, UFW | ~181 |
| 06 | Forense de Endpoint | Volatility, EDR, Autopsy | ~150 |

---

### 3. Expansión de Purple Team (4 módulos nuevos)

| # | Módulo | Tema | Líneas |
|---|--------|------|--------|
| 04 | Tabletop Exercises | Simulacros de incidentes | ~160 |
| 05 | Breach & Attack Simulation | Atomic Red Team, CALDERA | ~160 |
| 06 | Automated Compliance | OpenSCAP, InSpec, Prowler | ~203 |
| 07 | Threat Intelligence Purple Team | CTI + Purple Team | ~171 |

---

### 4. Mejora de Fundamentos (4 módulos mejorados)

| Módulo | Antes | Después | Ejercicios nuevos |
|--------|-------|---------|-------------------|
| 01 - Qué es ciberseguridad | 115 líneas | 166 (+44%) | Mapa de amenazas, CTF, superficie de ataque |
| 03 - Internet y redes | 165 líneas | 267 (+62%) | Análisis red local, DNS, captura tráfico |
| 05 - Criptografía | 159 líneas | 302 (+90%) | Hashes, cifrado, firmas, SSH, romper hashes |
| 06 - Vulnerabilidades | 204 líneas | 339 (+66%) | Nmap, DVWA, SQLi, OpenVAS, reportes |

---

### 5. Corrección del Workflow Validate Content

**Problemas encontrados:**
- VitePress genera `<meta charset="utf-8">` (minúsculas) pero validator buscaba `<meta charset="UTF-8"`
- Validator verificaba archivos VitePress generados (campus/, labs/) que usan SPA routing
- Links internos de archivos `.html` viejos causaban falsos positivos

**Soluciones:**
- Case-insensitive grep para meta charset
- Solo validar archivos HTML manuales en `docs/*.html`
- Skip de archivos generados por VitePress
- Exclusión de patrones `$`, `javascript:`, `/`

**Commit:** `0986d67` — fix(ci): corrige Validate Content workflow

---

## 📊 Métricas de la sesión

| Métrica | Valor |
|---------|-------|
| **Duración** | ~180 minutos |
| **Commits** | 6 |
| **Archivos creados** | 9 módulos nuevos |
| **Archivos mejorados** | 4 módulos fundamentos |
| **Líneas de código** | ~3,200+ |
| **Módulos totales campus** | 37 (9 fundamentos + 6 red + 6 blue + 7 purple + 5 AI + 4 seg.info) |
| **Workflows CI/CD** | 2/2 pasando ✅ |

---

## 🗂️ Estado del Proyecto

### Campus Virtual - Módulos

| Categoría | Módulos | Estado |
|-----------|---------|--------|
| 🚀 Fundamentos | 9 + 3 rutas | ✅ Completado |
| 🔴 Red Team | 8 | ✅ Completado |
| 🔵 Blue Team | 6 | ✅ Completado |
| 🟣 Purple Team | 7 | ✅ Completado |
| 🤖 AI Agents | 5 | ✅ Completado |
| 🛡️ Seguridad Info | 1 | ⏳ Pendiente expansión |
| **Total** | **37 módulos** | |

### Blog

| Métrica | Valor |
|---------|-------|
| Artículos publicados | 16 |
| URLs verificadas | 16/16 ✅ |

### CI/CD

| Workflow | Estado |
|----------|--------|
| Deploy to GitHub Pages | ✅ success |
| Validate Content | ✅ success |

---

## 📝 Commits de la sesión

| # | Hash | Descripción |
|---|------|-------------|
| 1 | `747ff41` | fix(sidebar): corrige links .html rotos y agrega módulos faltantes |
| 2 | `8238e4f` | fix(sidebar): agrega 5 módulos faltantes a sidebar AI Agents |
| 3 | `d89fd5c` | fix(config): sincroniza config.mjs con version vieja en site/.vitepress |
| 4 | `2af3777` | feat(modules): agrega 9 módulos nuevos a blue-team y purple-team |
| 5 | `0986d67` | fix(ci): corrige workflow Validate Content |
| 6 | `43b4412` | feat(fundamentals): agrega ejercicios prácticos a 4 módulos |

---

## 🔴 Pendientes para próxima sesión

1. **Expandir Seguridad de la Información** — solo tiene 1 módulo (index)
2. **Crear labs Docker interactivos** — para fundamentos y módulos avanzados
3. **Agregar módulo 10 de fundamentos** — Introducción a Linux para ciberseguridad
4. **Fase 4 — Monetización** — Tier Premium, donaciones, sponsors
5. **Activar Discord** — 39 canales configurados
6. **Mejorar SEO** — meta tags, sitemap, Open Graph

---

## 🛠️ Archivos modificados

### Configuración
- `site/content/.vitepress/config.mjs` — sidebar actualizado
- `site/.vitepress/config.mjs` — sincronizado
- `site/postbuild.cjs` — fixSidebarLinks agregado
- `.github/workflows/validate.yml` — correcciones de validación

### Contenido nuevo (9 módulos)
- `site/content/modules/blue-team/02-analisis-incidentes.md`
- `site/content/modules/blue-team/03-threat-hunting.md`
- `site/content/modules/blue-team/04-siem-monitoreo.md`
- `site/content/modules/blue-team/05-hardening.md`
- `site/content/modules/blue-team/06-forense-endpoint.md`
- `site/content/modules/purple-team/04-tabletop-exercises.md`
- `site/content/modules/purple-team/05-breach-attack-simulation.md`
- `site/content/modules/purple-team/06-automated-compliance.md`
- `site/content/modules/purple-team/07-threat-intelligence.md`

### Contenido mejorado (4 módulos)
- `site/content/modules/fundamentos/01-que-es-ciberseguridad.md`
- `site/content/modules/fundamentos/03-internet-y-redes.md`
- `site/content/modules/fundamentos/05-criptografia-basica.md`
- `site/content/modules/fundamentos/06-vulnerabilidades.md`

---

*Última actualización: 2026-08-21*
