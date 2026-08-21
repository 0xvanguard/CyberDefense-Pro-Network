---
title: "Módulo 01 — Fundamentos Blue Team y SOC"
---

# Módulo 01 — Fundamentos Blue Team y SOC

> **Área:** 03-blue-team-defensa  
> **Rol principal al que aporta:** SOC Analyst (Nivel 1–2), base para Incident Responder y Threat Hunter.

---

## 1. Misión del módulo

Este módulo introduce al estudiante en el mundo del **Blue Team** desde el punto de vista más operativo: el **Centro de Operaciones de Seguridad (SOC)**.

La misión es que el estudiante entienda qué hace realmente un SOC en la vida real, qué tipo de datos ve a diario (logs, alertas, eventos) y cómo se encaja eso dentro de la defensa de una organización.

Al terminar el módulo, el estudiante debe tener un mapa mental claro de:

- Qué es un Blue Team, qué es un SOC y en qué se diferencia de Red/Purple Team.  
- Qué tipo de telemetría y herramientas se usan para **monitorizar y detectar** actividad sospechosa.  
- Cómo se ve, a alto nivel, el **flujo de trabajo de un analista de SOC**.  

Este módulo es la base conceptual y práctica sobre la que se construirán los siguientes: Incident Response, Threat Hunting e Ingeniería de detecciones.

---

## 2. Objetivos de aprendizaje

Al completar este módulo, el estudiante debería ser capaz de:

1. Explicar con sus propias palabras qué es un SOC, qué es un Blue Team y qué rol juegan dentro de la seguridad de una organización.  
2. Identificar los tipos de logs y eventos más comunes que llegan a un SOC (sistema, red, aplicaciones, seguridad).  
3. Describir los componentes básicos de una arquitectura de monitoreo (fuentes de logs → recolección → normalización → almacenamiento → análisis/alertas).  
4. Reconocer el flujo típico de trabajo de un analista de SOC (recepción de alertas, triage, escalado).  
5. Relacionar de forma básica actividades ofensivas (escaneos, intentos de login, uso de herramientas) con eventos/logs que un SOC podría ver.  

Más adelante, otros módulos profundizarán en la parte técnica (queries, reglas, playbooks, hunting), pero este módulo busca cimentar el **lenguaje común y el contexto**.

---

## 3. Áreas clave del módulo

Este módulo se divide en áreas temáticas breves, pensadas para dar una base sólida sin abrumar.

### 3.1 Qué es el Blue Team

- Definición de Blue Team y su relación con Red Team y Purple Team.  
- Diferencia entre defensa reactiva (SOC tradicional) y defensa más proactiva (Threat Hunting, ingeniería de detecciones).  
- Ejemplos de situaciones reales en las que interviene un Blue Team.

### 3.2 Introducción al SOC

- Qué es un **Security Operations Center (SOC)**.  
- Roles típicos dentro de un SOC: analista Tier 1, Tier 2, Tier 3, líder de turno.  
- Flujo básico de una alerta: generación → recepción → revisión → clasificación → escalado/cierre.  

### 3.3 Telemetría y fuentes de información

- Tipos de logs:  
  - Sistema (Windows/Linux).  
  - Red (firewalls, routers, proxies).  
  - Aplicaciones (servidores web, aplicaciones internas, APIs).  
  - Seguridad (EDR, antivirus, WAF, autenticación).  
- Conceptos de normalización y correlación básica.

### 3.4 Herramientas de monitoreo y SIEM (visión general)

- Visión general de SIEM (Security Information and Event Management).  
- Ejemplos de herramientas: Wazuh/OSSEC, ELK/Graylog, SIEM comerciales (sin entrar en detalle).  
- Qué ve un analista: dashboards, listados de eventos, reglas/queries.

### 3.5 Conexión con la ruta ofensiva

- Cómo los escaneos, ataques web o movimientos vistos en el área de Pentesting/Red Team se traducen en eventos que el SOC debería ver.  
- Ejemplos conceptuales:  
  - Escaneo de puertos → logs de firewall.  
  - Intentos de login fallidos → logs de autenticación.  
  - Acceso a rutas sensibles de una aplicación → logs de servidor web/WAF.  

---

## 4. Estructura del módulo

La idea es mantener una estructura coherente con el resto de la plataforma:

1. **README del módulo (este archivo):**  contexto, misión, objetivos y áreas clave.  
2. **Teoría mínima guiada:**  
   - Conceptos básicos de Blue Team y SOC.  
   - Ejemplos de logs y alertas.  
3. **Laboratorio 01 (por definir):**  
   - Lectura e interpretación de eventos básicos en un entorno guiado.  
   - Relación entre una actividad ofensiva simple y los eventos que genera.  
4. **Portafolio:**  
   - Un entregable breve que el estudiante pueda guardar (por ejemplo, una ficha de "Evento SOC" o un mini informe explicando qué vio en el lab).

---

## 5. Entregables del módulo

Los entregables son sencillos pero orientados a que el estudiante empiece a construir **material de portafolio** desde el primer módulo de Blue Team.

### 5.1 Entregable teórico

- Un breve documento (puede ser un archivo Markdown en `portafolio/`) donde el estudiante responda, en formato claro:
  - ¿Qué es un SOC y qué hace un Blue Team?  
  - ¿Qué tipos de logs ve un SOC a diario?  
  - ¿Qué diferencia hay entre recibir una alerta y hacer threat hunting?  

### 5.2 Entregable práctico (ligado al Lab 01)

Cuando se defina el **Lab 01 del módulo**, el entregable práctico esperado será algo como:

- Un pequeño resumen de 1–2 páginas donde el estudiante:
  - Describa el escenario del lab (por ejemplo, "SOC de una fintech recibiendo eventos").  
  - Enumere algunos eventos/logs relevantes que haya observado (sin necesidad de un nivel técnico profundo todavía).  
  - Explique cómo esos eventos podrían relacionarse con una actividad ofensiva simple.

> Más adelante, en módulos siguientes, estos entregables crecerán hasta convertirse en **informes de incidente completos**, timelines de ataque y reglas de detección documentadas.

---

## 6. Relación con otros módulos y áreaes

- **Área Pentesting / Red Team:**  
  Este módulo se apoya en lo que ya se ha visto a nivel ofensivo (por ejemplo, Recon y Pentest web), para mostrar el "eco" de esas acciones en la telemetría que vería un SOC.

- **Módulos futuros de Blue Team:**  
  - Incident Response: tomará los conceptos de telemetría y SOC y los llevará a escenarios donde hay que contener y gestionar incidentes.  
  - Threat Hunting: usará este mismo lenguaje de logs y eventos, pero de forma proactiva, buscando patrones anómalos.

- **Área Purple Team (más adelante):**  
  La comprensión básica de SOC y Blue Team será clave para diseñar ejercicios donde Red y Blue colaboran.

---

## 7. Próximos pasos

Para completar este módulo a nivel de contenido y práctica, los siguientes pasos serán:

1. Crear un **Lab 01 — Introducción a eventos y alertas SOC** donde el estudiante revise un conjunto de eventos simples y los relacione con acciones (benignas o maliciosas).  
2. Diseñar una plantilla de **ficha de evento SOC** o mini informe de laboratorio para `portafolio/`, que el estudiante pueda completar tras el lab.  
3. Conectar este módulo con uno de los escenarios ofensivos existentes (por ejemplo, actividad mínima contra NovaPay Labs) para que el estudiante vea el puente Red→Blue.

Este módulo se seguirá ajustando a medida que se creen los labs y plantillas de informes, manteniendo siempre el enfoque profesional y práctico de la plataforma.
