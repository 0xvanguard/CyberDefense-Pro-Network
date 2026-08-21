---
title: "Módulo 04 — Tabletop Exercises y Simulacros"
---

# 🎭 Módulo 04 — Tabletop Exercises y Simulacros

> **Objetivo Principal:** Diseñar y ejecutar ejercicios de simulación (tabletop) para evaluar la preparación del equipo de seguridad ante incidentes.

[![Nivel](https://img.shields.io/badge/Nivel-Intermedio-orange?style=flat-square)]()
[![Duración](https://img.shields.io/badge/Duración-1%20mes-blue?style=flat-square)]()

---

## 📋 Resumen del módulo

| Atributo | Detalle |
|----------|---------|
| **Pre-requisitos** | Módulos 01-03 completados |
| **Herramientas** | Frameworks MITRE, Plantillas de escenarios |
| **Entregable** | Ejercicio de tabletop ejecutado + reporte |
| **Nivel** | Intermedio |

---

## 1. 🧠 Teoría: ¿Qué es un Tabletop Exercise?

Un tabletop exercise es una **discusión guiada** donde el equipo de seguridad simula responder a un escenario de incidente sin ejecutar acciones técnicas reales.

### Beneficios

| Beneficio | Descripción |
|-----------|-------------|
| **Identificar gaps** | Descubrir procesos faltantes |
| **Mejorar comunicación** | Coordinar entre equipos |
| **Entrenar decisiones** | Practicar bajo presión |
| **Cumplimiento** | Requisitos de frameworks (NIST, ISO) |

---

## 2. 📋 Escenarios de Tabletop

### Escenario 1: Ransomware en Producción

```
ESCENARIO: Ransomware en Servidor de Base de Datos

Día: Lunes 9:00 AM
Situación:
- El equipo de ops recibe alerta de que el servidor de BD principal
  está cifrado y muestra nota de ransomware
- El atacante pide 50 BTC por la clave de descifrado
- El backup más reciente es de hace 3 días
- 3 aplicaciones dependen de esta base de datos

PREGUNTAS:
1. ¿Quién activa el plan de respuesta?
2. ¿Se paga el rescate? ¿Por qué sí o por qué no?
3. ¿Cómo se comunica con los clientes afectados?
4. ¿Cuál es el plan de recuperación?
```

### Escenario 2: Compromiso de Credenciales de Admin

```
ESCENARIO: Credenciales de Admin en Dark Web

Día: Viernes 4:30 PM
Situación:
- Un dark web monitoring detecta credenciales de admin del dominio
- Las credenciales parecen válidas (obtenidas de un breach reciente)
- El admin afectado niega haber sido comprometido
- Es viernes y el equipo está reducido

PREGUNTAS:
1. ¿Cuáles son las primeras 3 acciones?
2. ¿Se fuerza cambio de contraseña inmediato?
3. ¿Se revisan logs de las últimas 24 horas?
4. ¿Se escala al CISO o se maneja internamente?
```

---

## 3. 🔬 Práctica Guiada: Diseñar un Tabletop

### Paso 1: Definir objetivos

```markdown
## Objetivos del Ejercicio
- Evaluar tiempos de respuesta del equipo
- Identificar gaps en procesos de comunicación
- Probar herramientas de detección existentes
- Documentar lecciones aprendidas
```

### Paso 2: Crear escenario

```markdown
## Escenario: Data Breach por Third Party

**Contexto:**
- Proveedor de cloud storage reporta breach
- Sus clientes incluyen nuestra organización
- Datos potencialmente comprometidos: emails, hashes de contraseñas
- El breach fue descubierto hace 48 horas

**Preguntas:**
1. ¿Tenemos visibility sobre qué datos tenía el proveedor?
2. ¿Cómo notificamos a los usuarios afectados?
3. ¿Cumplimos con GDPR/CCPA para notificación?
4. ¿Qué controles adicionales implementamos?
```

### Paso 3: Ejecutar el ejercicio

```
Duración típica: 2-3 horas

09:00 - Introducción y reglas (15 min)
09:15 - Presentación del escenario (15 min)
09:30 - Discusión por fase del incidente (90 min)
11:00 - Preguntas abiertas (30 min)
11:30 - Wrap-up y próximos pasos (15 min)
```

---

## 4. 📊 Evaluación del Ejercicio

### Métricas a medir

| Métrica | Descripción |
|---------|-------------|
| **Tiempo de escalamiento** | ¿Cuánto tomó escalar? |
| **Claridad de roles** | ¿Quién hacía qué? |
| **Comunicación** | ¿Se mantuvo informado al equipo? |
| **Decisiones** | ¿Se tomaron decisiones acertadas? |
| **Documentación** | ¿Se documentaron acciones? |

---

## 5. 🎯 Mini-Entregable

**Tarea:** Diseñar y ejecutar un tabletop exercise que incluya:

1. **Escenario** detallado con contexto realista
2. **Preguntas** para guiar la discusión
3. **Facilitación** del ejercicio (30-60 min)
4. **Reporte** con hallazgos y recomendaciones

---

## 6. 🔗 Recursos Adicionales

- [NIST SP 800-84 - Guide to Test, Training, and Exercise Programs](https://csrc.nist.gov/publications/detail/sp/800-84/final)
- [CISA Tabletop Exercise Packages](https://www.cisa.gov/resources-tools/services/cisa-tabletop-exercise-packages)
- [MITRE ATT&CK - Adversary Emulation](https://attack.mitre.org/resources/adversary-emulation/)

---

> **Siguiente paso:** Continúa con el [Módulo 05 — Breach & Attack Simulation](../purple-team/05-breach-attack-simulation) para aprender a automatizar pruebas de seguridad.
