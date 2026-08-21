# 📋 Follow-ups Pendientes — Actualizado 21 de Agosto, 2026 (Sesión 6)

> **Última sesión:** Sesión 6 — Sincronización Web ↔ GitHub
> **Estado:** Fase 2 al 40% + Sistema de sync completo

---

## ✅ Completado en Sesión 6

- [x] Auditoría Web vs GitHub
- [x] VitePress configurado y funcionando
- [x] 33 READMEs sincronizados
- [x] 36 páginas HTML generadas
- [x] Editor web (admin.html) funcional
- [x] Deploy automático via GitHub Actions
- [x] URLs verificadas en GitHub Pages

---

## 🎯 Prioridad Inmediata: Completar Fase 2 + Expandir Campus

### 1. Migrar Roles Profesionales al Campus

**30+ READMEs de roles** que solo existen en GitHub:

| Categoría | Roles | Prioridad |
|-----------|-------|-----------|
| **Red Team** | Pentester, Threat Hunter, Bug Bounty, Malware Analyst | ⭐⭐⭐⭐ |
| **Blue Team** | SOC Analyst, Incident Responder, Threat Intelligence | ⭐⭐⭐⭐ |
| **AI Security** | Prompt Engineer, AI Red Teamer, ML Security Engineer | ⭐⭐⭐ |
| **GRC** | CISO, DPO, Risk Manager, Auditor, Privacy Engineer | ⭐⭐⭐ |
| **DevSecOps** | Security Engineer, DevSecOps, Cloud Security | ⭐⭐⭐ |

**Acción:** Agregar al SYNC_MAP en `site/sync.cjs` y ejecutar `node sync.cjs pull`

### 2. Completar Labs Interactivos Restantes

**12 labs sin versión interactiva:**

| # | Lab | Dificultad | XP | Prioridad |
|---|-----|------------|-----|-----------|
| 1 | net-01 | Fundamentos | 200 | ⭐⭐⭐⭐ |
| 2 | persist-01 | Intermedio | 300 | ⭐⭐⭐⭐ |
| 3 | social-01 | Intermedio | 200 | ⭐⭐⭐ |
| 4 | lateral-01 | Intermedio | 350 | ⭐⭐⭐ |
| 5 | ad-01 | Avanzado | 500 | ⭐⭐⭐⭐ |
| 6 | malware-01 | Avanzado | 450 | ⭐⭐⭐⭐ |
| 7 | cloud-01 | Avanzado | 400 | ⭐⭐⭐ |
| 8 | forensics-01 | Avanzado | 400 | ⭐⭐⭐ |
| 9 | reverse-eng-01 | Avanzado | 450 | ⭐⭐⭐ |
| 10 | net-forensics-01 | Avanzado | 350 | ⭐⭐⭐ |
| 11 | incident-01 | Expert | 600 | ⭐⭐ |
| 12 | malware-expert-01 | Expert | 700 | ⭐⭐ |

### 3. Integrar Labs Interactivos en Campus

Los labs interactivos (`lab-runner.js`) existen en `labs/` pero no están integrados en el campus VitePress.

**Acción:** Crear componentes Vue o iframe embed para mostrar labs interactivos dentro del campus.

---

## 🎯 Fase 3: Lanzamiento (Post-Fase 2)

| Tarea | Prioridad | Tiempo Est. |
|-------|-----------|-------------|
| Activar Discord (bots, roles, canales) | ⭐⭐⭐⭐⭐ | 2 semanas |
| Blog semanal (8 artículos SEO) | ⭐⭐⭐⭐ | 4 semanas |
| Leaderboard global | ⭐⭐⭐ | 2 semanas |
| Eventos de lanzamiento | ⭐⭐⭐⭐⭐ | 1 semana |

---

## 🎯 Fase 4: Monetización

| Tarea | Prioridad | Tiempo Est. |
|-------|-----------|-------------|
| Tier Premium (cursos exclusivos) | ⭐⭐⭐ | 1 mes |
| Donaciones (GitHub Sponsors, Ko-fi) | ⭐⭐⭐ | 1 semana |
| Sponsors (herramientas de seguridad) | ⭐⭐ | 2 meses |

---

## 🎯 Fase 5: Escalamiento

| Tarea | Prioridad | Tiempo Est. |
|-------|-----------|-------------|
| API pública (labs, rankings) | ⭐⭐ | 2 meses |
| Mobile app (React Native) | ⭐ | 3 meses |
| Certificaciones propias | ⭐ | 6 meses |

---

## 📊 Estado de Archivos Clave

```
site/
├── .vitepress/config.mjs    ✅ Configuración VitePress
├── content/
│   ├── index.md             ✅ Landing page
│   ├── modules/             ✅ 33 archivos MD
│   ├── labs/                ✅ 14 archivos MD
│   └── public/admin.html    ✅ Editor web
├── sync.cjs                 ✅ Script de sincronización
└── package.json             ✅ Dependencias

docs/
├── admin.html               ✅ Editor web (deploy)
├── campus/                  ✅ 36 páginas HTML
├── modules/                 ✅ Módulos legacy
├── labs/                    ✅ Labs legacy
├── sesiones/                ✅ Documentación
└── assets/                  ✅ Recursos estáticos

labs/
├── intermedio/              ✅ 8 labs con index.html
├── avanzado/                ⏳ READMEs sin index.html
├── fundamentos/             ⏳ READMEs sin index.html
└── expert/                  ⏳ READMEs sin index.html
```

---

## 🔗 URLs de Prueba

| Página | URL |
|--------|-----|
| Landing | `https://0xvanguard.github.io/CyberDefense-Pro-Network/` |
| Campus | `https://0xvanguard.github.io/CyberDefense-Pro-Network/campus/` |
| Admin | `https://0xvanguard.github.io/CyberDefense-Pro-Network/admin.html` |
| GitHub | `https://github.com/0xvanguard/CyberDefense-Pro-Network` |

---

*Documento generado por Buffy — 21 de Agosto, 2026*
