# Sesión 8.5 — Blog Profesionalización + 16 Artículos
**Fecha:** 2026-08-21  
**Duración:** ~120 minutos  
**Objetivo:** Corregir 404 del blog, profesionalizar diseño, crear 16 artículos

---

## 📋 Resumen Ejecutivo

### Problema inicial
Los artículos del blog daban **404 Not Found** al hacer clic desde el índice.

### Causa raíz
1. Links absolutos hardcodeados (`/CyberDefense-Pro-Network/blog/01-...`) en vez de paths relativos VitePress
2. VitePress generaba links con `.html` que el postbuild convertía a directorios, creando mismatch
3. No existía `cleanUrls` habilitado en VitePress

### Soluciones implementadas
1. ✅ Habilitar `cleanUrls: true` en VitePress config
2. ✅ Rediseñar blog index con cards Vue interactivas
3. ✅ Agregar sidebar con navegación entre artículos
4. ✅ Agregar frontmatter profesional (autor, fecha, tags, reading time)
5. ✅ Corregir links rotos y caracteres unicode
6. ✅ Crear 16 artículos de blog sobre ciberseguridad

---

## 🔧 Archivos modificados

### Configuración
| Archivo | Cambio |
|---------|--------|
| `site/content/.vitepress/config.mjs` | +`cleanUrls: true`, +sidebar blog (16 artículos) |

### Blog Index
| Archivo | Cambio |
|---------|--------|
| `site/content/blog/index.md` | Cards Vue con 16 artículos, layout profesional |

### Artículos 1-8 (existentes, mejorados)
| Archivo | Cambio |
|---------|--------|
| `site/content/blog/01-porque-ciberseguridad.md` | +Frontmatter, fix footer link |
| `site/content/blog/02-tcp-ip-simplificado.md` | +Frontmatter |
| `site/content/blog/03-nmap-guia-definitiva.md` | +Frontmatter |
| `site/content/blog/04-sql-injection.md` | +Frontmatter |
| `site/content/blog/05-mi-primer-ctf.md` | +Frontmatter, fix unicode |
| `site/content/blog/06-primer-empleo.md` | +Frontmatter |
| `site/content/blog/07-laboratorio-casero.md` | +Frontmatter |
| `site/content/blog/08-comunidades.md` | +Frontmatter, fix link |

### Artículos 9-16 (nuevos)
| Archivo | Tema | Tags | Lectura |
|---------|------|------|---------|
| `site/content/blog/09-reverse-engineering.md` | Ghidra, radare2, binarios | reverse-engineering, ghidra | 6 min |
| `site/content/blog/10-phishing-ingenieria-social.md` | 5 tipos de phishing | phishing, ingenieria-social | 5 min |
| `site/content/blog/11-docker-ciberseguridad.md` | 3 labs prácticos | docker, labs, containers | 5 min |
| `site/content/blog/12-owasp-top10.md` | OWASP 2021 completo | owasp, web-security | 7 min |
| `site/content/blog/13-hashing-cracking.md` | John, Hashcat, bcrypt | hashing, cracking | 5 min |
| `site/content/blog/14-wifi-hacking.md` | Aircrack-ng, Evil Twin | wifi, aircrack | 5 min |
| `site/content/blog/15-bug-bounty.md` | HackerOne, metodología | bugbounty, rewards | 5 min |
| `site/content/blog/16-cloud-security.md` | AWS, Azure, GCP | cloud, aws | 6 min |

### Documentación
| Archivo | Contenido |
|---------|-----------|
| `docs/sesiones/sesion-2026-08-21-blog-profesionalizacion.md` | Sesión parcial (artículos 9-12) |
| `docs/sesiones/sesion-2026-08-21-completa-blog-16-articulos.md` | Esta sesión completa |

---

## 📊 Commits de la Sesión

| Commit | Hash | Descripción |
|--------|------|-------------|
| 1 | `ae16ae8` | feat(blog): profesionaliza blog con clean URLs, sidebar y metadata |
| 2 | `b2bc9ec` | feat(blog): agrega 4 artículos nuevos (semanas 9-12) |
| 3 | `abb85db` | feat(blog): agrega 4 artículos nuevos (semanas 13-16) |

---

## ✅ Verificación de URLs — 16/16

### Deploy #1 (ae16ae8) — Blog profesionalizado
```
✅ 200  /campus/blog/
✅ 200  /campus/blog/01-porque-ciberseguridad/
✅ 200  /campus/blog/02-tcp-ip-simplificado/
✅ 200  /campus/blog/03-nmap-guia-definitiva/
✅ 200  /campus/blog/04-sql-injection/
✅ 200  /campus/blog/05-mi-primer-ctf/
✅ 200  /campus/blog/06-primer-empleo/
✅ 200  /campus/blog/07-laboratorio-casero/
✅ 200  /campus/blog/08-comunidades/
```

### Deploy #2 (b2bc9ec) — Artículos 9-12
```
✅ 200  /campus/blog/09-reverse-engineering/
✅ 200  /campus/blog/10-phishing-ingenieria-social/
✅ 200  /campus/blog/11-docker-ciberseguridad/
✅ 200  /campus/blog/12-owasp-top10/
```

### Deploy #3 (abb85db) — Artículos 13-16
```
✅ 200  /campus/blog/13-hashing-cracking/
✅ 200  /campus/blog/14-wifi-hacking/
✅ 200  /campus/blog/15-bug-bounty/
✅ 200  /campus/blog/16-cloud-security/
```

---

## 🏗️ Arquitectura Técnica del Blog

```
site/content/blog/*.md
    ↓ VitePress build (cleanUrls: true)
docs/campus/blog/*.html
    ↓ postbuild.cjs
docs/campus/blog/*/index.html
    ↓ git push → GitHub Actions
🌐 https://0xvanguard.github.io/CyberDefense-Pro-Network/campus/blog/
```

### Componentes del blog:
1. **Blog index** — Vue component con `v-for` cards interactivas
2. **Sidebar** — Navegación entre 16 artículos
3. **Article metadata** — Autor, fecha, tags, reading time
4. **Previous/Next** — Navegación al pie de cada artículo
5. **Clean URLs** — Sin `.html` en los links

---

## 📊 Métricas del Blog

| Métrica | Valor |
|---------|-------|
| Total artículos | 16 |
| Tiempo de contenido | ~85 minutos de lectura |
| URLs verificadas | 16/16 ✅ |
| Deploy exitoso | 3/3 ✅ |
| Artículos por semana | 4-6 min cada uno |
| Temas cubiertos | Carrera, Redes, Herramientas, Web, CTF, Labs, Comunidad, RE, Social Eng., Docker, OWASP, Crypto, WiFi, Bug Bounty, Cloud |

---

## 📝 Contenido del Blog — Resumen

| # | Artículo | Tema Principal | Nivel |
|---|----------|---------------|-------|
| 01 | ¿Por qué ciberseguridad? | Estadísticas y salarios | Principiante |
| 02 | TCP/IP explicado | Fundamentos de redes | Principiante |
| 03 | Nmap guía definitiva | 20 comandos esenciales | Principiante |
| 04 | SQL Injection | OWASP #1 explicado | Intermedio |
| 05 | Mi primer CTF | Experiencia y recursos | Principiante |
| 06 | Primer empleo | Carrera y certificaciones | Intermedio |
| 07 | Lab casero | Hardware y Docker | Principiante |
| 08 | Mejores comunidades | 10 comunidades | Principiante |
| 09 | Reverse Engineering | Ghidra y binarios | Intermedio |
| 10 | Phishing | 5 tipos + defensa | Intermedio |
| 11 | Docker para ciberseguridad | 3 labs prácticos | Intermedio |
| 12 | OWASP Top 10 | 10 vulnerabilidades | Intermedio |
| 13 | Hashing y Cracking | John, Hashcat | Intermedio |
| 14 | Wi-Fi Hacking | Aircrack-ng, Evil Twin | Intermedio |
| 15 | Bug Bounty | HackerOne, metodología | Intermedio |
| 16 | Cloud Security | AWS, Azure, GCP | Intermedio |

---

## 🔗 URLs del Proyecto

| Recurso | URL |
|---------|-----|
| **Blog** | https://0xvanguard.github.io/CyberDefense-Pro-Network/campus/blog/ |
| **Campus** | https://0xvanguard.github.io/CyberDefense-Pro-Network/campus/ |
| **Landing** | https://0xvanguard.github.io/CyberDefense-Pro-Network/ |
| **GitHub** | https://github.com/0xvanguard/CyberDefense-Pro-Network |

---

## ⚠️ Issues Conocidos

1. **Validate Content workflow** — Falla en "Validate HTML metadata". No afecta el deploy. Causa: el validador espera metadata HTML específica que VitePress no genera.

---

## 📈 Estado del Proyecto Actualizado

| Fase | Estado |
|------|--------|
| **Fase 1** — Videos, Discord, Gamificación | ✅ Completada |
| **Fase 2** — 20 Labs interactivos | ✅ Completada |
| **Fase 2.5** — Sync web ↔ GitHub + Postbuild | ✅ Completada |
| **Fase 3** — Blog (16 artículos) + Leaderboard | ✅ Completada |
| **Fase 3.5** — Blog profesionalizado | ✅ Completada |
| **Fase 4** — Monetización | ⏳ Pendiente |
| **Fase 5** — API, Mobile, Certificaciones | ⏳ Pendiente |

### Métricas acumuladas (9 sesiones):
- **26+ commits** totales
- **96+ páginas HTML** en campus
- **16 artículos** blog
- **20 labs** interactivos
- **40 roles** profesionales
- **16/16 URLs** blog verificadas ✅
- **86 archivos** convertidos a clean URLs
