# 🛡️ OpenVAS / GVM — Visión de gestión de vulnerabilidades

> `OpenVAS` dentro de `GVM` sirve muy bien para ver vulnerabilidades por activo, severidad, tendencia y remediación sugerida.

---

## Cuándo usarlo

Usa GVM cuando necesites:
- inventario por activos,
- severidad por host,
- reportes para equipos defensivos,
- validación periódica tras remediación.

---

## Enfoque del módulo

En este módulo no buscamos dominar toda la administración de GVM, sino entender cómo interpretar su salida:

| Campo | Qué debes mirar |
|---|---|
| CVSS | Base score técnico |
| Threat / Severity | Cómo lo clasifica el escáner |
| QoD | Calidad de detección |
| Host | Qué activo específico está afectado |
| Solution | Qué recomienda corregir |

---

## Preguntas clave al analizar un finding

- ¿El hallazgo es verificable?
- ¿Está expuesto a internet o solo a red interna?
- ¿El sistema es crítico?
- ¿Afecta C, I o A?
- ¿Qué equipo debe actuar primero?

---

## Traducción por equipos

| Si ves esto en GVM | Acción inmediata |
|---|---|
| CVSS alto + activo expuesto | Blue prioriza; Red valida; Purple re-testea |
| Puerto legacy innecesario | Blue cierra o segmenta |
| Banner de versión vulnerable | Red busca exploitabilidad controlada |
| Múltiples hallazgos repetidos | Purple propone corrección sistémica |

---

**[← Nuclei](./nuclei.md)** · **[→ searchsploit](./searchsploit.md)**
