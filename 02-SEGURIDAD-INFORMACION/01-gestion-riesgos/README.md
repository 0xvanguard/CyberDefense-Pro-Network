# 📊 Módulo 01 — Gestión de Riesgos de Ciberseguridad

> **Objetivo principal:** Aprender a identificar, evaluar y tratar riesgos de seguridad de la información utilizando marcos cuantitativos y cualitativos (ISO 31000, NIST RMF, FAIR).

[![Nivel](https://img.shields.io/badge/Nivel-Intermedio%20→%20Avanzado-orange?style=flat-square)]()
[![Enfoque](https://img.shields.io/badge/Enfoque-GRC%20%7C%20Risk%20Management-red?style=flat-square)]()
[![Frameworks](https://img.shields.io/badge/Frameworks-ISO%2031000%20%7C%20NIST%20RMF%20%7C%20FAIR-blue?style=flat-square)]()

---

## 📋 Resumen del módulo

| Atributo | Detalle |
|---|---|
| 🏷️ **Nivel** | Intermedio → Avanzado |
| ⏱️ **Duración estimada** | 4–5 semanas |
| 🎯 **Resultado esperado** | Realizar evaluaciones de riesgo cuantitativas y cualitativas, crear planes de tratamiento y reportes ejecutivos |
| 🧪 **Práctica verificable** | Risk assessment completo, heat map, risk register, treatment plan |
| 🗂️ **Portafolio** | Documento de evaluación de riesgos listo para revisión |
| 🔗 **Requiere** | Fundamentos de seguridad de la información |
| 🔗 **Conduce a** | Compliance, Auditoría, CISO |

---

## 🎯 Qué aprenderás

- [ ] Aplicar el proceso ISO 31000 de gestión de riesgos
- [ ] Utilizar el NIST Risk Management Framework (RMF)
- [ ] Realizar análisis cuantitativo de riesgos con FAIR
- [ ] Crear risk registers y heat maps
- [ ] Definir planes de tratamiento de riesgos
- [ ] Comunicar riesgos a la alta dirección

---

## 📚 Contenido del módulo

### FASE 1 — Fundamentos de Gestión de Riesgos (Semana 1)

#### 1.1 ¿Qué es un Riesgo?
```
Riesgo = Probabilidad × Impacto
```

Un riesgo de seguridad es la combinación de:
- **Amenaza:** Evento que podría causar daño
- **Vulnerabilidad:** Debilidad que puede ser explotada
- **Activo:** Lo que tiene valor para la organización
- **Impacto:** Consecuencia materializada la amenaza

#### 1.2 Proceso ISO 31000
```
┌─────────────────────────────────────────┐
│  1. Alcance, contexto y criterios       │
│  2. Análisis de riesgos                 │
│     2.1 Identificación de riesgos       │
│     2.2 Análisis de consecuencias       │
│     2.3 Análisis de likelihood          │
│  3. Evaluación de riesgos               │
│  4. Tratamiento de riesgos              │
│  5. Monitoreo y revisión                │
│  6. Comunicación y consulta             │
└─────────────────────────────────────────┘
```

---

### FASE 2 — Análisis Cualitativo (Semana 2)

#### 2.1 Matriz de Probabilidad vs Impacto

|  | Impacto Bajo | Impacto Medio | Impacto Alto | Impacto Crítico |
|--|-------------|---------------|--------------|-----------------|
| **Prob. Alta** | Medio | Alto | Crítico | Crítico |
| **Prob. Media** | Bajo | Medio | Alto | Crítico |
| **Prob. Baja** | Bajo | Bajo | Medio | Alto |
| **Prob. Muy Baja** | Bajo | Bajo | Bajo | Medio |

#### 2.2 Escalas de Calificación

**Probabilidad:**
| Nivel | Descripción | Frecuencia |
|-------|-------------|------------|
| 5 - Casi seguro | Ocurrirá probablemente | > 1 vez/año |
| 4 - Probable | Podría ocurrir | 1 vez/año |
| 3 - Posible | Podría ocurrir | 1 vez/2-5 años |
| 2 - Improbable | No se espera | 1 vez/5-10 años |
| 1 - Raro | Extremadamente improbable | < 1 vez/10 años |

**Impacto:**
| Nivel | Financiero | Reputacional | Operacional | Legal |
|-------|-----------|--------------|-------------|-------|
| 5 - Crítico | > $1M | Cobertura nacional | Negocio detenido | Multas graves |
| 4 - Mayor | $100K-$1M | Cobertura regional | Servicio degradado | Investigación |
| 3 - Moderado | $10K-$100K | Cobertura local | Retrasos menores | Amonestación |
| 2 - Menor | $1K-$10K | Impacto interno | Inconveniencias | Ninguna |
| 1 - Insignificante | < $1K | Ninguno | Sin impacto | Ninguna |

---

### FASE 3 — Análisis Cuantitativo con FAIR (Semana 3)

#### 3.1 FAIR Model
FAIR (Factor Analysis of Information Risk) convierte el riesgo en términos financieros:

```
Riesgo = Pérdida de Evento (LEF) × Magnitud de Pérdida (LM)
LEF = Probabilidad de Exploit (PLE) × Probabilidad de Amenaza (PLT)
```

#### 3.2 Métricas FAIR

| Métrica | Fórmula | Descripción |
|---------|---------|-------------|
| **SLE** (Single Loss Expectancy) | AV × EF | Pérdida esperada por evento |
| **ARO** (Annualized Rate of Occurrence) | Frecuencia anual estimada | Veces que ocurrirá al año |
| **ALE** (Annualized Loss Expectancy) | SLE × ARO | Pérdida anual esperada |
| **ROSI** (Return on Security Investment) | (ALE_before - ALE_after - Cost) / Cost | Retorno de la inversión en seguridad |

#### 3.3 Ejemplo Práctico
```
Activo: Base de datos de clientes
Valor (AV): $500,000
Exposición (EF): 40%
SLE = $500,000 × 0.40 = $200,000
Frecuencia (ARO): 0.2 (1 cada 5 años)
ALE = $200,000 × 0.2 = $40,000/año

Control propuesto: WAF + DLP
Costo del control: $15,000/año
Reducción del ALE: 80%
ALE_after = $40,000 × 0.20 = $8,000

ROSI = ($40,000 - $8,000 - $15,000) / $15,000 = 113%
```

---

### FASE 4 — Tratamiento y Reporte (Semana 4)

#### 4.1 Estrategias de Tratamiento

| Estrategia | Descripción | Cuándo usar |
|------------|-------------|-------------|
| **Mitigar** | Implementar controles para reducir riesgo | Riesgo alto, control costo-efectivo |
| **Transferir** | Seguros, tercerización | Riesgo con impacto financiero alto |
| **Evitar** | Eliminar la actividad que genera riesgo | Riesgo crítico sin mitigación posible |
| **Aceptar** | Asumir el riesgo conscientemente | Riesgo bajo o costo de mitigación > impacto |

#### 4.2 Risk Register Template

| ID | Riesgo | Activo | Probabilidad | Impacto | Nivel | Tratamiento | Responsable | Estado |
|----|--------|--------|--------------|---------|-------|-------------|-------------|--------|
| R01 | Ransomware | Servidores | Alta | Crítico | Crítico | Mitigar | CISO | En progreso |
| R02 | Phishing | Empleados | Alta | Alto | Alto | Mitigar | SOC | Planificado |
| R03 | Data leak | BD clientes | Media | Crítico | Crítico | Mitigar+Transferir | DPO | En progreso |

---

## 🧪 Laboratorios

| Lab | Descripción | Nivel |
|-----|-------------|-------|
| `lab-01` | Risk assessment cualitativo de PYME | Básico |
| `lab-02` | Análisis FAIR de activo crítico | Intermedio |
| `lab-03` | Crear risk register completo | Intermedio |
| `lab-04` | Reporte ejecutivo para la dirección | Avanzado |

---

## 🔗 Referencias

- [ISO 31000:2018](https://www.iso.org/standard/65090.html)
- [NIST SP 800-30 Rev. 1](https://csrc.nist.gov/publications/detail/sp/800-30/rev-1/final)
- [FAIR Institute](https://www.fairinstitute.org/)
- [NIST RMF](https://csrc.nist.gov/projects/risk-management)

---

*Última actualización: Agosto 2026*
