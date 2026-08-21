---
title: "Módulo 01 — Gestión de Riesgos"
---

# 📊 Módulo 01 — Gestión de Riesgos

> **Objetivo:** Identificar, evaluar y tratar riesgos de seguridad de manera sistemática usando frameworks reconocidos.

[![Nivel](https://img.shields.io/badge/Nivel-Intermedio-orange?style=flat-square)]()
[![Duración](https://img.shields.io/badge/Duración-2%20meses-blue?style=flat-square)]()

---

## 📋 Resumen del módulo

| Atributo | Detalle |
|----------|---------|
| **Pre-requisitos** | Fundamentos completados |
| **Frameworks** | ISO 27001, NIST CSF, OCTAVE |
| **Entregable** | Matriz de riesgos + Plan de tratamiento |
| **Nivel** | Intermedio |

---

## 1. 🧠 Teoría: ¿Qué es la gestión de riesgos?

La gestión de riesgos es el proceso de **identificar, evaluar y priorizar** amenazas y vulnerabilidades, y luego asignar recursos para minimizar su impacto.

### Ciclo de vida del riesgo

```
┌─────────────────────────────────────────────────────┐
│           CICLO DE GESTIÓN DE RIESGOS                 │
├─────────────┬──────────────┬────────────┬───────────┤
│  1. Contexto │ 2. Identificar│ 3. Analizar │ 4. Evaluar│
│  y alcance   │ riesgos      │ riesgos     │ riesgos   │
├──────────────┼──────────────┼─────────────┼───────────┤
│ 5. Tratar    │ 6. Monitorear │ 7. Comunicar│ 8. Revisar│
│ riesgos      │ y revisar     │ resultados  │ y mejorar │
└──────────────┴──────────────┴─────────────┴───────────┘
```

---

## 2. 📐 Frameworks de gestión de riesgos

### ISO 27001:2022

| Componente | Descripción |
|------------|-------------|
| **SoA** | Declaración de Aplicabilidad — qué controles aplica |
| **Clausa 6.1.2** | Análisis y tratamiento de riesgos |
| **Anexo A** | 93 controles de seguridad |
| **Ciclo PDCA** | Plan-Do-Check-Act continuo |

### NIST CSF 2.0

| Función | Descripción |
|---------|-------------|
| **Govern** | Gobernanza y estrategia |
| **Identificar** | Entender el contexto y activos |
| **Proteger** | Implementar controles |
| **Detectar** | Identificar eventos de seguridad |
| **Responder** | Tomar acción ante incidentes |
| **Recuperar** | Restaurar operaciones |

### OCTAVE Allegro

Enfoque cualitativo para organizaciones sin equipo de seguridad dedicado:
1. Establecer amenazas de información
2. Identificar activos de información
3. Desarrollar zona de protección
4. Identificar amenazas a activos
5. Identificar vulnerabilidades
6. Estrategia de protección

---

## 3. 🔍 Identificación de activos

### Tipos de activos

| Tipo | Ejemplos | Valor |
|------|----------|-------|
| **Datos** | Clientes, financieros, propiedad intelectual | Crítico |
| **Software** | Aplicaciones, base de datos, código fuente | Alto |
| **Hardware** | Servidores, estaciones, dispositivos móviles | Medio |
| **Personas** | Empleados, contratistas, usuarios | Alto |
| **Servicios** | Email, VPN, cloud, internet | Alto |

### Inventario de activos

```markdown
## Inventario de Activos - Empresa X

| ID | Activo | Tipo | Ubicación | Responsable | Valor |
|----|--------|------|-----------|-------------|-------|
| A001 | Server BD principal | Hardware | Datacenter | Ops | Crítico |
| A002 | Base de datos clientes | Datos | Server BD | Dev | Crítico |
| A003 | App web principal | Software | Cloud | Dev | Alto |
| A004 | Email corporativo | Servicio | Cloud | IT | Alto |
| A005 | GitHub repos | Software | Cloud | Dev | Alto |
```

---

## 4. 📊 Evaluación de riesgos

### Matriz de probabilidad vs impacto

```
Impacto ↑
        │
   5    │  5  10  15  20  25
        │
   4    │  4   8  12  16  20
        │
   3    │  3   6   9  12  15
        │
   2    │  2   4   6   8  10
        │
   1    │  1   2   3   4   5
        │
        └────────────────────→ Probabilidad
           1    2   3   4   5
```

### Escala de calificación

| Probabilidad | Descripción |
|--------------|-------------|
| 1 - Raro | Ocurre una vez cada 5+ años |
| 2 - Improbable | Puede ocurrir una vez al año |
| 3 - Posible | Puede ocurrir una vez al trimestre |
| 4 - Probable | Probable que ocurra mensualmente |
| 5 - Casi seguro | Ocurrirá semanalmente o más |

| Impacto | Descripción |
|---------|-------------|
| 1 - Insignificante | Sin efecto en el negocio |
| 2 - Menor | Dolor de cabeza, resolución rápida |
| 3 - Moderado | Interrupción parcial del negocio |
| 4 - Mayor | Interrupción significativa |
| 5 - Catastrófico | Amenaza la supervivencia del negocio |

---

## 5. 🛡️ Tratamiento de riesgos

### Estrategias de tratamiento

| Estrategia | Descripción | Cuándo usar |
|------------|-------------|-------------|
| **Mitigar** | Implementar controles para reducir | Riesgo aceptable con controles |
| **Transferir** | Seguros, outsourcing | Riesgo costoso de mitigar |
| **Evitar** | Eliminar la actividad | Riesgo inaceptable |
| **Aceptar** | Asumir el riesgo | Bajo costo de mitigación |

### Ejemplo de plan de tratamiento

```markdown
## Plan de Tratamiento - Riesgo R003

**Riesgo:** Exfiltración de datos de clientes
**Probabilidad:** 3 (Posible)
**Impacto:** 5 (Catastrófico)
**Puntuación:** 15 (Alto)

### Estrategia: Mitigar

| Acción | Responsable | Fecha | Costo |
|--------|-------------|-------|-------|
| Implementar DLP | Seguridad | 2024-03 | $5,000 |
| Encriptar datos en reposo | Dev | 2024-02 | $2,000 |
| Capacitar usuarios | RRHH | 2024-01 | $1,000 |

### Riesgo residual
- Después de mitigar: Probabilidad 2 × Impacto 3 = 6 (Medio)
```

---

## 6. 🔧 Herramientas

| Herramienta | Uso | Costo |
|-------------|-----|-------|
| **RiskWatch** | Gestión de riesgos automatizada | Comercial |
| **OpenFAIR** | Análisis cuantitativo de riesgo | Gratis |
| **RiskyBusiness** | Evaluación de riesgos | Gratis |
| **ISO 27001 Toolkit** | Plantillas y checklists | Gratis |

---

## 7. ✏️ Ejercicios prácticos

### Ejercicio 1: Identificar activos (20 min)

1. Lista los 10 activos más importantes de tu organización (o una ficticia)
2. Clasifícalos por tipo y valor
3. Identifica qué amenazas podrían afectar cada uno

### Ejercicio 2: Matriz de riesgos (30 min)

1. Crea una matriz de probabilidad × impacto para 5 riesgos
2. Califica cada riesgo
3. Clasifica: Crítico (>15), Alto (10-15), Medio (5-9), Bajo (<5)

### Ejercicio 3: Plan de tratamiento (30 min)

1. Selecciona el riesgo más alto de tu matriz
2. Diseña un plan de tratamiento con 3 acciones concretas
3. Asigna responsables y fechas
4. Calcula el riesgo residual

---

> **Siguiente:** [Módulo 02 — Blue Team / Defensa](./02-blue-team-defensa)
