# Plan v1.2.0 — AI Security + Labs Expansion

**Fecha de planificación:** 23 Agosto 2026
**Última actualización:** 23 Agosto 2026 (post módulo 06)
**Objetivo:** Expandir la sección de AI Security y mejorar la experiencia de labs.

---

## 🎯 Resumen Ejecutivo

| Área | Features | Completados | Pendientes |
|------|----------|-------------|------------|
| AI Security | 3 módulos nuevos | 2 | 1 |
| Labs | 2 labs nuevos + 1 interactivo | 1 | 2 |
| Infraestructura | Auth + i18n + navbar | 0 | 3 |
| Documentación | Módulos faltantes + roles | 2 | 1 |

### Progreso General: **6/12 (50%)**

---

## 🔴 Prioridad Alta — AI Security

### 1. Módulo `06-mlsecops-pipeline-seguro.md` ✅
- Pipeline completo MLSecOps documentado
- Puntos de control: datos → modelo → despliegue → operación
- Integración con GovLLM-Sentinel
- **Esfuerzo:** 2-3 horas
- **Dependencias:** Ninguna
- **Estado:** ✅ Completado (436 líneas, commit `71fad56`)
- **Archivos:** `site/content/modules/ai-agents/06-mlsecops-pipeline-seguro.md`

### 2. Módulo `04-owasp-llm-top10-2025.md` ✅
- OWASP LLM Top 10 detallado con ejemplos
- Mitigaciones para cada vulnerabilidad
- Casos de estudio reales
- **Esfuerzo:** 2-3 horas
- **Dependencias:** Ninguna
- **Estado:** ✅ Completado (427 líneas, commit `8fab933`)
- **Archivos:** `site/content/modules/ai-agents/04-owasp-llm-top10-2025.md`

### 3. Dashboard de Evaluación de Modelos
- Página interactiva para comparar modelos
- Métricas: ASR, refusal rate, latency
- Integración con GovLLM-Sentinel
- **Esfuerzo:** 3-4 horas
- **Dependencias:** Módulos 05 y 06
- **Estado:** ⏳ Pendiente

---

## 🔴 Prioridad Alta — Labs

### 4. Lab `prompt-injection-01.html`
- Lab dedicado a prompt injection
- Ejercicios con diferentes tipos de injection
- Validación de defensas
- **Esfuerzo:** 2-3 horas
- **Dependencias:** Módulo 05
- **Estado:** ⏳ Pendiente

### 5. Lab `red-teaming-01.html`
- Introducción a AI Red Teaming
- Uso de herramientas: Garak, PyRIT
- Documentación de hallazgos
- **Esfuerzo:** 3-4 horas
- **Dependencias:** Módulo 06
- **Estado:** ⏳ Pendiente

### 6. Gamificación de Labs AI
- Sistema de XP para labs de AI Security
- Badges: "Jailbreak Expert", "Guardrail Master", "AI Red Teamer"
- Leaderboard integrado
- **Esfuerzo:** 2-3 horas
- **Dependencias:** Labs 4 y 5
- **Estado:** ⏳ Pendiente

---

## 🟡 Prioridad Media — Infraestructura

### 7. Fix AUTH_STORED
- Actualizar hash de autenticación en admin.html
- Eliminar generate-hash.html (seguridad)
- **Esfuerzo:** 30 minutos
- **Dependencias:** Ninguna
- **Nota:** CRÍTICO pendiente desde 22 Ago
- **Estado:** ⏳ Pendiente

### 8. Navbar AI Security
- Agregar sección "AI Security" al dropdown de módulos
- Links a dashboard, labs y módulos
- **Esfuerzo:** 30 minutos
- **Dependencias:** Ninguna
- **Estado:** ⏳ Pendiente

### 9. i18n — Contenido AI Security
- Traducir dashboard y labs a inglés
- Actualizar i18n-lang.js con nuevas claves
- **Esfuerzo:** 2-3 horas
- **Dependencias:** Features 1-6 completados
- **Estado:** ⏳ Pendiente

---

## 🟢 Prioridad Normal — Documentación

### 10. Roles AI Security actualizados
- Actualizar `ai-red-teamer.md` con labs nuevos
- Actualizar `prompt-engineer-security.md` con módulos
- Actualizar `ml-security-engineer.md` con GovLLM-Sentinel
- **Esfuerzo:** 1-2 horas
- **Dependencias:** Features 1-3
- **Estado:** ⏳ Pendiente

### 11. README actualizado
- Agregar sección "AI Security Labs"
- Actualizar estadísticas (labs, módulos)
- Agregar link a CHANGELOG
- **Esfuerzo:** 30 minutos
- **Dependencias:** Features 1-6
- **Estado:** ⏳ Pendiente

### 12. Portfolio AI Security
- Crear `PORTAFOLIO-AI-SECURITY.md`
- Documentar proyectos: GovLLM-Sentinel, labs, dashboard
- Incluir métricas de evaluación
- **Esfuerzo:** 1 hora
- **Dependencias:** Features 1-6
- **Estado:** ⏳ Pendiente

---

## 📅 Cronograma Propuesto

```
Semana 1 (24-30 Ago):
├── ✅ Módulo 04-owasp-llm-top10-2025.md
├── Fix AUTH_STORED (CRÍTICO)
├── Módulo 06-mlsecops-pipeline-seguro.md
└── Navbar AI Security

Semana 2 (31 Ago - 6 Sep):
├── Lab prompt-injection-01.html
├── Lab red-teaming-01.html
└── Dashboard de Evaluación

Semana 3 (7-13 Sep):
├── Gamificación de Labs
├── Roles AI Security actualizados
├── README actualizado
└── Portfolio AI Security

Semana 4 (14-20 Sep):
├── i18n contenido AI Security
├── Testing completo
└── Release v1.2.0
```

### Completado en v1.1.0 + v1.1.1 (23 Ago)
- ✅ Dashboard educativo jailbreaking
- ✅ Lab jailbreak-01 (400 XP)
- ✅ Módulo 05-prompt-injection-y-jailbreaks.md
- ✅ Módulo 04-owasp-llm-top10-2025.md
- ✅ Módulo 06-mlsecops-pipeline-seguro.md
- ✅ Catálogo labs actualizado

---

## 📊 Métricas de Éxito

| Métrica | v1.1.0 | v1.2.0 (meta) | Actual |
|---------|--------|----------------|--------|
| Módulos AI Security | 3 | 6 | 5 ✅ |
| Labs AI Security | 2 | 5 | 2 |
| Líneas de contenido | ~2,268 | ~4,500 | ~3,500 |
| Roles documentados | 7 | 10 | 7 |
| Idiomas soportados | 1 | 2 (es + en) | 1 |

---

## 🔗 Dependencias con GovLLM-Sentinel

| Feature | Requiere GovLLM-Sentinel |
|---------|--------------------------|
| Dashboard de Evaluación | Sí — datos de benchmark |
| Lab red-teaming-01 | Sí — configuración de modelos |
| Módulo 06 | No — referencia documental |
| Gamificación | No — sistema interno |

---

## ⚠️ Riesgos

| Riesgo | Impacto | Mitigación |
|--------|---------|------------|
| GovLLM-Sentinel no tiene datos reales | Medio | Usar datos sintéticos para demo |
| i18n consume mucho tiempo | Bajo | Priorizar inglés, otros idiomas en v1.3 |
| AUTH_STORED pendiente太久 | Alto | Fix inmediato en Semana 1 |

---

## 📝 Historial de Cambios

| Fecha | Cambio |
|-------|--------|
| 2026-08-23 | Plan creado con 12 features |
| 2026-08-23 | Módulo 04-owasp-llm-top10-2025.md completado |
| 2026-08-23 | v1.1.0 lanzado con dashboard, lab y módulo 05 |
| 2026-08-23 | Módulo 06-mlsecops-pipeline-seguro.md completado |

---

*Plan creado por Buffy — 23 Agosto 2026*
*Última actualización: 23 Agosto 2026*
