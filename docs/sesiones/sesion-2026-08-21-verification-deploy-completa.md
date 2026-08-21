# Sesión 8 — Verificación de Deploy y Corrección de Errores
**Fecha:** 2026-08-21  
**Duración:** ~60 minutos  
**Objetivo:** Verificar deploy en GitHub Pages y corregir errores de URLs

---

## 📋 Resumen de la Sesión

### Problemas detectados y corregidos

#### 1. Links duplicados `/campus/campus/` en landing page
- **Problema:** Los links en `site/content/index.md` tenían prefijo `/campus/` que VitePress duplicaba al agregar `base: '/CyberDefense-Pro-Network/campus/'`
- **Resultado:** URLs como `/campus/campus/modules/fundamentos/` → 404
- **Solución:** Cambiar links de `/campus/modules/...` a `/modules/...`
- **Commit:** `e43b339`

#### 2. GitHub Pages no soporta clean URLs
- **Problema:** VitePress genera `recon-01.html` pero los links apuntan a `/recon-01/` (sin `.html`)
- **Resultado:** Todas las URLs de módulos, labs y roles daban 404
- **Solución:** Script `postbuild.cjs` que convierte archivos planos a directorios con `index.html`
- **Commits:** `7cacbec`, `90f96e4`

#### 3. Postbuild saltaba subdirectorios existentes
- **Problema:** El postbuild original no recursaba en directorios que ya tenían `index.html`
- **Resultado:** Archivos internos de módulos (ej: `01-reconocimiento-osint.html`) no se convertían
- **Solución:** Eliminar condición de skip, siempre recursar
- **Commit:** `90f96e4`

#### 4. Labs faltantes en sync
- **Problema:** `fundamentos/net-01`, `expert/incident-01`, `intermedio/persist-01`, `social-01`, `lateral-01` no estaban en `SYNC_MAP`
- **Resultado:** Esos labs no aparecían en el campus
- **Solución:** Agregar 6 entradas al SYNC_MAP + crear `labs/index.md` como catálogo
- **Commit:** `d07e98a`

#### 5. Índices de roles faltantes
- **Problema:** No existían `roles/red-team/index.html`, etc.
- **Solución:** Crear 5 páginas index.md para cada categoría de roles
- **Commit:** `90f96e4`

---

## 🔧 Archivos modificados

| Archivo | Cambio |
|---------|--------|
| `site/content/index.md` | Links corregidos (sin prefijo /campus/) |
| `site/sync.cjs` | +6 entradas para labs faltantes |
| `site/postbuild.cjs` | Bug fix: recursar todos los subdirectorios |
| `site/content/labs/index.md` | Catálogo completo de 20 labs |
| `site/content/roles/red-team/index.md` | Índice roles Red Team |
| `site/content/roles/blue-team/index.md` | Índice roles Blue Team |
| `site/content/roles/engineering/index.md` | Índice roles Engineering |
| `site/content/roles/grc/index.md` | Índice roles GRC |
| `site/content/roles/ai-security/index.md` | Índice roles AI Security |
| `.github/workflows/deploy.yml` | +paso postbuild después de vitepress build |
| `site/package.json` | Scripts corregidos |

---

## ✅ Verificación Final — 19/19 URLs

```
✅ 200  /                                          (Landing)
✅ 200  /campus/                                   (Campus Virtual)
✅ 200  /campus/modules/red-team/                  (Red Team index)
✅ 200  /campus/modules/red-team/01-reconocimiento-osint/  (Módulo)
✅ 200  /campus/modules/blue-team/                 (Blue Team index)
✅ 200  /campus/modules/ai-agents/                 (AI Agents index)
✅ 200  /campus/modules/fundamentos/               (Fundamentos index)
✅ 200  /campus/labs/                              (Catálogo labs)
✅ 200  /campus/labs/intermedio/recon-01/          (Lab intermedio)
✅ 200  /campus/labs/avanzado/ad-01/               (Lab avanzado)
✅ 200  /campus/labs/expert/incident-01/           (Lab expert)
✅ 200  /campus/labs/fundamentos/net-01/           (Lab fundamento)
✅ 200  /campus/blog/                              (Blog index)
✅ 200  /campus/leaderboard/                       (Leaderboard)
✅ 200  /admin.html                                (Admin editor)
✅ 200  /campus/roles/red-team/                    (Roles Red Team)
✅ 200  /campus/roles/grc/ciso/                    (Rol específico)
✅ 200  /campus/roles/ai-security/                 (Roles AI Security)
✅ 200  /campus/blog/01-porque-ciberseguridad/     (Artículo blog)
```

---

## 📊 Commits de la Sesión

| Commit | Descripción |
|--------|-------------|
| `e43b339` | fix: links duplicados /campus/campus/ en landing page |
| `d07e98a` | fix: labs faltantes (fundamentos, expert) + catálogo |
| `7cacbec` | fix: postbuild para clean URLs en GitHub Pages |
| `90f96e4` | fix: postbuild procesa subdirectorios + índices de roles |

---

## 🏗️ Arquitectura del Build Pipeline

```
README.md (repo)
    ↓ sync.cjs pull
site/content/*.md (Markdown sincronizado)
    ↓ VitePress build
docs/campus/*.html (HTML generado)
    ↓ postbuild.cjs
docs/campus/*/index.html (Clean URLs para GitHub Pages)
    ↓ git push
GitHub Actions → Deploy a GitHub Pages
    ↓
🌐 https://0xvanguard.github.io/CyberDefense-Pro-Network/
```

---

## 🎯 Estado del Proyecto al Cierre

| Fase | Estado |
|------|--------|
| **Fase 1** | ✅ Videos, Discord (39 canales), Gamificación |
| **Fase 2** | ✅ 20 labs interactivos, 119 ejercicios, 7,550 XP |
| **Fase 2.5** | ✅ Sistema sync web ↔ GitHub, postbuild clean URLs |
| **Fase 3** | ✅ Blog (8 artículos SEO), Leaderboard global |
| **Fase 4** | ⏳ Pendiente (Premium, Donaciones, Sponsors) |
| **Fase 5** | ⏳ Pendiente (API, Mobile, Certificaciones) |

### Métricas acumuladas (8 sesiones):
- **23 commits** esta sesión
- **96 páginas HTML** generadas en campus
- **78 archivos** sincronizados (modules + labs + roles)
- **40 roles** profesionales migrados
- **20 labs** interactivos
- **8 artículos** blog
- **19/19 URLs** verificadas ✅
