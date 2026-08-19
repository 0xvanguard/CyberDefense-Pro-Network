# Reporte de Análisis de Vulnerabilidades

> **⚠️ Plantilla educativa y profesional.**  
> Anonimiza todos los datos sensibles antes de publicar.

---

## 1. Portada

| Campo | Valor |
|---|---|
| Analista | Tu nombre / alias |
| Fecha | YYYY-MM-DD |
| Alcance | [IPs / URLs / activos] |
| Tipo de assessment | Interno / Externo / Web |
| Metodología | CIA Triad + VM Lifecycle + validación Red/Blue/Purple |
| Clasificación | Interno / Portafolio |

---

## 2. Resumen ejecutivo

Resume en 120–180 palabras:
- postura general,
- cantidad de hallazgos,
- los 2 o 3 más relevantes,
- riesgo principal,
- acción recomendada inmediata.

---

## 3. Inventario revisado

| Activo | Tipo | Exposición | Dueño técnico |
|---|---|---|---|
| app1 | Web | Pública | [equipo] |

---

## 4. Matriz de hallazgos

| ID | Activo | Hallazgo | Sev | C | I | A | Validado | Prioridad |
|---|---|---|---|---|---|---|---|---|
| V-01 | app1 | Directory listing | Medio | M | B | B | Sí | Alta |

---

## 5. Hallazgos detallados

### V-01 — [Nombre del hallazgo]

| Campo | Valor |
|---|---|
| Activo | [activo] |
| Severidad | [Low/Medium/High/Critical] |
| CVSS | [score] |
| CIA | C:[B/M/A] · I:[B/M/A] · A:[B/M/A] |
| Estado | Confirmado / Potencial / Falso positivo |

#### Descripción
[Qué es y por qué importa]

#### Evidencia
```bash
# comandos, headers, outputs, capturas, etc.
```

#### Lectura por equipos
- **Red Team:** [cómo lo explotaría o validaría]
- **Blue Team:** [qué debe corregir o monitorear]
- **Purple Team:** [cómo re-testear y medir mejora]

#### Remediación
- Acción inmediata:
- Acción de fondo:
- Validación posterior:

---

## 6. Plan de remediación

| Prioridad | Hallazgo | Acción | SLA |
|---|---|---|---|
| 1 | V-01 | Deshabilitar listing y revisar permisos | 72h |

---

## 7. Conclusiones

Incluye:
- patrón principal observado,
- punto más débil del entorno,
- mejora más importante,
- cómo debería continuar el siguiente assessment.

---

## 8. Anexos

```bash
# Pegar comandos completos usados
```
