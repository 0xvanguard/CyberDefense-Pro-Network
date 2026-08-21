---
title: "Área: Purple Team / Colaboración Red–Blue"
description: "Área: Purple Team / Colaboración Red–Blue"
---

> 🚀 **¿Eres principiante?** Antes de este módulo, revisa la **[base común del repo](../00-FUNDAMENTOS/)** (1 carpeta atrás). Purple team une red+blue: necesitas base de ambos lados primero.
>
> Empieza por 🛡️ [Ruta Defensor](../00-FUNDAMENTOS/rutas/ruta-defensor.md) o ⚔️ [Ruta Atacante](../00-FUNDAMENTOS/rutas/ruta-atacante.md) y vuelve aquí cuando domines una de las dos.

# Área: Purple Team / Colaboración Red–Blue

> **Rol de el área:** Unir el trabajo de **Red Team (ofensiva)** y **Blue Team (defensiva)** para diseñar, ejecutar y medir ejercicios donde ataque y defensa colaboran para mejorar las detecciones y la seguridad real del entorno.

---

## 1. Propósito de el Área Purple Team

Mientras que Red Team se centra en simular adversarios y Blue Team en detectar y responder, **Purple Team** busca que ambos trabajen juntos de forma estructurada.

En esta área el estudiante aprenderá a:

- Traducir técnicas ofensivas concretas en **hipótesis de detección**.  
- Diseñar y ejecutar **ejercicios colaborativos** donde se dispara una técnica y se observa cómo responde el entorno.  
- Medir si las detecciones son suficientes, mejorarlas y documentar el resultado.  

El objetivo final es que el estudiante entienda el ciclo completo: **ataque → detección → respuesta → mejora continua**, usando el mismo escenario (por ejemplo, la fintech NovaPay Labs) desde ambas perspectivas.

---

## 2. Objetivos de aprendizaje

Al completar los primeros módulos de Purple Team, el estudiante debería ser capaz de:

1. Explicar qué es Purple Team y en qué se diferencia de ejercicios puramente Red o Blue.  
2. Tomar una técnica ofensiva simple (por ejemplo, intentos de login fallidos masivos contra el portal de merchants) y diseñar un **caso de detección** asociado.  
3. Ejecutar un ejercicio de Purple Team básico: disparar una actividad ofensiva controlada y observar cómo aparece en los logs/herramientas de monitoreo.  
4. Evaluar la efectividad de las detecciones existentes (¿hay alerta?, ¿se ve el patrón?, ¿falta contexto?) y proponer mejoras.  
5. Documentar el ejercicio en términos de tácticas/técnicas (por ejemplo, usando MITRE ATT&CK como mapa mental).  

---

## 2.5 Módulos del área

| Módulo | Contenido | Estado |
|---|---|---|
| [`01-purple-endpoint-procesos-telemetria/`](./01-purple-endpoint-procesos-telemetria/) | Telemetría de host: procesos, comandos y detección en endpoint | ✅ Base |
| [`02-detection-engineering/`](./02-detection-engineering/) | Ciclo de vida de detecciones, tipos, **métricas (precision/recall/MTTD/MTTR)** y cobertura ATT&CK | ✅ Completo |
| [`03-adversary-emulation/`](./03-adversary-emulation/) | **Atomic Red Team + CALDERA** para validar detecciones con emulación | ✅ Completo |
| [`laboratorios/`](./laboratorios/) | Pack Purple Web NovaPay (login storm, rutas raras) | ✅ Base |

---

## 3. Pack Purple Web NovaPay v1 (ruta sugerida)

Como primer conjunto de ejercicios integrados, esta área ofrece el **Pack Purple Web NovaPay v1**, una ruta sugerida que conecta los módulos ofensivos y defensivos ya construidos en torno al portal de merchants de NovaPay Labs.

### 3.1 Lab 01 — Purple Web: Login storm controlado

- **Ruta:** `04-purple-team-colaboracion/laboratorios/lab-01-purple-web-login-storm/`  
- **Idea central:** Simular un pequeño "login storm" controlado (varios intentos de login fallidos) contra el portal de merchants y ver cómo se reflejan en los logs de autenticación/aplicación web o en la herramienta SOC. [cite:183]
- **Conexión con Red y Blue:**  
  - Red: se apoya en el conocimiento del login del portal adquirido en el módulo de Pentesting/Red Team. [cite:172]  
  - Blue: reutiliza los conceptos de logs de autenticación y su visualización trabajados en los labs SOC de el área Blue Team. [cite:181]
- **Enfoque Purple:** El estudiante diseña y ejecuta el patrón ofensivo, lo busca en la telemetría y propone al menos una idea de alerta/umbral para un SOC, documentando todo en una ficha SOC y en versiones para gerente y analista.

### 3.2 Lab 02 — Purple Web: Exploración de rutas "raras"

- **Ruta:** `04-purple-team-colaboracion/laboratorios/lab-02-purple-web-rutas-raras/`  
- **Idea central:** Realizar una exploración controlada de rutas poco comunes o no enlazadas (por ejemplo, `/admin`, `/backup`, `/test`) en el portal, y analizar cómo ese reconocimiento se ve en los logs de servidor/aplicación. [cite:184]
- **Conexión con Red y Blue:**  
  - Red: se basa en las técnicas de reconocimiento y enumeración de rutas vistas en los labs de Pentest web. [cite:172]  
  - Blue: utiliza la lectura de logs de servidor y códigos HTTP introducida en los ejercicios Blue Team (lectura de eventos y visualización en herramientas SOC). [cite:181]
- **Enfoque Purple:** El estudiante identifica patrones de exploración (múltiples 404, accesos repetidos a `/admin`, etc.), evalúa su visibilidad y propone ideas de alerta o casos de hunting para detectar este tipo de actividad.

> **Recomendación de uso:** esta ruta Purple Web es ideal para estudiantes que ya hayan completado la parte básica de Recon/Pentest Web en Red Team y los primeros labs de lectura/visualización de logs en Blue Team. Permite ver, en un escenario web realista, cómo los ataques que se practican en Red generan señales que Blue puede usar, y cómo Purple puede cerrar el ciclo con mejoras concretas de detección.

---

## 4. Primera pieza Purple Team con NovaPay Labs

Para arrancar, se usará el escenario ya conocido de **NovaPay Labs**:

- Portal de merchants (ruta ofensiva: Recon + Pentest web).  
- Logs de firewall, autenticación y aplicación web (ruta Blue Team: Lab 01 + Lab 02 SOC).  

La primera pieza Purple Team consistirá en un **laboratorio integrado** donde el estudiante:

- Ejecuta una actividad ofensiva sencilla (por ejemplo, intentos de login fallidos controlados contra el portal).  
- Observa cómo esos intentos aparecen en la plataforma de monitoreo (ELK/Wazuh).  
- Evalúa si la visibilidad actual sería suficiente para detectar una fuerza bruta básica.  
- Propone ajustes o ideas de detección.

*(Contenido ampliado en los enunciados específicos de cada lab del pack.)*

---

## 5. Comunicación Efectiva en Purple Team

El Purple Team conecta directamente ataque, detección y mejora continua, y eso requiere una comunicación clara hacia varios perfiles.

En los ejercicios de esta área, el estudiante practicará:

- **Explicaciones para gerencia:** resúmenes en 2–3 frases sobre qué ejercicio se hizo, qué se descubrió y cómo mejora la seguridad de la organización.  
- **Explicaciones para equipos técnicos:** descripción de las técnicas ofensivas usadas, cómo se ven en la telemetría, qué regla o alerta se validó y qué ajustes se proponen.

Así, cada ejercicio Purple no solo mejora la cobertura técnica de detecciones, sino también la capacidad del estudiante de **contar la historia completa del ataque y la defensa** a audiencias distintas.

---

## 6. Próximos pasos para el área Purple Team

A partir del Pack Purple Web NovaPay v1, se podrán ir añadiendo:

- Un módulo Purple centrado en endpoint (procesos, comandos, PowerShell, creación de usuarios, etc.) con ejercicios similares a los de web pero sobre telemetría de host.  
- Labs adicionales que usen otras técnicas ofensivas simples (por ejemplo, actividad en endpoints, movimiento lateral limitado) y sus reflejos en la telemetría.  
- Una futura integración con módulos de IA/MLSecOps donde parte de la lógica de detección y mejora se automatice.

Esta área se irá actualizando para reflejar nuevas rutas Purple a medida que se enriquezcan las áreaes Red y Blue.
