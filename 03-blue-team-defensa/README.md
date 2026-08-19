# Área: Blue Team / Defensa

> **Rol de el área:** Formar profesionales capaces de **detectar, investigar y responder** a ataques en entornos reales, conectando directamente con lo que hacen los equipos SOC, incident response y threat hunting en la industria.

---

## 1. Propósito de el Área Blue Team

Esta área complementa la ruta ofensiva (Recon, Pentesting, Red Team) con el "otro lado": **defensa, monitoreo, detección y respuesta**.

La idea es que los estudiantes no solo aprendan a encontrar y explotar vulnerabilidades, sino también a:

- Entender cómo se **monitoriza** una infraestructura.  
- Diseñar y operar **detecciones** frente a técnicas reales (por ejemplo, usando MITRE ATT&CK como mapa mental).  
- Investigar **incidentes** y trazar la historia de un ataque.  
- Documentar y comunicar hallazgos de forma profesional (informes, timelines, recomendaciones).

El objetivo final es crear perfiles que puedan trabajar en equipos SOC, responder incidentes y hacer threat hunting de forma sólida, con mentalidad profesional y no solo "de laboratorio".

---

## 2. Objetivos de aprendizaje

Al completar el área Blue Team, el estudiante debería ser capaz de:

1. Explicar el **rol del Blue Team** y cómo se relaciona con Red Team y Purple Team dentro de una organización.  
2. Entender los conceptos básicos de **detección, monitoreo y respuesta a incidentes** (SOC, SIEM, EDR, logs, alertas, playbooks).  
3. Usar herramientas clave de análisis y monitoreo (por ejemplo, Wazuh/OSSEC, ELK/Graylog, Wireshark/tcpdump, Sysmon) en entornos de laboratorio.  
4. Mapear actividades ofensivas (como las vistas en la ruta de Pentesting/Red Team) a **técnicas MITRE ATT&CK** y pensar en cómo detectarlas.  
5. Participar en el ciclo completo de un incidente básico: **detección → análisis → contención → erradicación → recuperación → lecciones aprendidas**.  
6. Crear **informes y timelines** de incidentes con calidad profesional, listos para portafolio.  

---

## 3. Áreas clave dentro de el área

El área Blue Team se organizará en áreas temáticas que luego se traducirán en módulos y laboratorios.

### 3.1 Fundamentos de defensa y monitoreo

- Conceptos base: Blue Team, SOC, NOC, CSIRT, CERT.  
- Tipos de telemetría: logs de sistema, logs de red, logs de aplicaciones, eventos de seguridad.  
- Visión general de SIEM, EDR, NDR y su rol en la detección.  

### 3.2 SOC Analyst / Monitoring

- Operaciones de un SOC: turnos, niveles (Tier 1/2/3), tipos de alertas.  
- Detección inicial: correlación de eventos, priorización de alertas, falsos positivos.  
- Uso básico de herramientas tipo SIEM (consultas, dashboards, reglas sencillas).  

### 3.3 Incident Response

- Fases del manejo de incidentes (NIST/ISO): preparación, identificación, contención, erradicación, recuperación, lecciones aprendidas.  
- Evidencia y cadena de custodia (a nivel básico de laboratorio).  
- Documentación de incidentes: timelines, impacto, acciones ejecutadas, recomendaciones.  

### 3.4 Threat Hunting

- Diferencia entre **detección reactiva** y **búsqueda proactiva**.  
- Hipótesis de hunting basadas en ATT&CK y en conocimiento del entorno.  
- Uso de logs, queries y visualizaciones para buscar actividad anómala.  

### 3.5 Ingeniería de detecciones / MITRE ATT&CK

- Introducción a MITRE ATT&CK como catálogo de tácticas/técnicas.  
- Cómo traducir una técnica ofensiva (por ejemplo, ejecución remota, movimiento lateral, cred dumping) en **casos de detección**.  
- Validación de detecciones en laboratorio: simular actividad maliciosa y verificar si se genera alerta/evento.

---

## 4. Rutas y roles dentro de el área

El área Blue Team ofrecerá rutas que se conectan con roles concretos de la industria.

### 4.1 Ruta: SOC Analyst (Nivel 1–2)

**Objetivo:** Preparar al estudiante para trabajar en un SOC como analista de primer/segundo nivel.

Enfoque del camino:

- Comprender el flujo de alertas en un SOC.  
- Aprender a revisar y clasificar alertas (triage).  
- Trabajar con dashboards y queries sencillas en herramientas de monitoreo.  
- Documentar incidentes simples y escalarlos con buena comunicación.

Posibles módulos/labs (a futuro):

- Introducción a SOC y SIEM.  
- Laboratorio de revisión de alertas en entorno simulado (fintech atacada).  
- Ejercicios de clasificación de eventos (benigno vs sospechoso vs malicioso).  

### 4.2 Ruta: Incident Responder

**Objetivo:** Desarrollar habilidades para coordinar y ejecutar la respuesta técnica a incidentes.

Enfoque del camino:

- Profundizar en las fases de respuesta a incidentes.  
- Practicar contención y erradicación en laboratorios controlados (por ejemplo, aislar hosts, revocar credenciales, revisar persistencia).  
- Generar informes de incidente con enfoque técnico y ejecutivo.

Posibles módulos/labs (a futuro):

- Laboratorio de incidente simulado (ransomware / compromiso de cuenta / movimiento lateral).  
- Análisis de artefactos básicos (logs, procesos, conexiones).  
- Construcción de un informe de incidente listo para portafolio.

### 4.3 Ruta: Threat Hunter

**Objetivo:** Enseñar a buscar amenazas de forma proactiva usando hipótesis y datos del entorno.

Enfoque del camino:

- Formular hipótesis de hunting basadas en ATT&CK y en la realidad del entorno (por ejemplo, una fintech como NovaPay Labs).  
- Diseñar consultas en herramientas de logs/telemetría.  
- Identificar patrones anómalos y relacionarlos con técnicas ofensivas.

Posibles módulos/labs (a futuro):

- Hunting de ejecución sospechosa en endpoints.  
- Hunting de actividad anómala en autenticaciones y cuentas.  
- Creación de casos de hunting reutilizables ("playbooks" simples).

### 4.4 Ruta: Detección e Ingeniería de reglas

**Objetivo:** Conectar directamente con la experiencia de construir y ajustar detecciones.

Enfoque del camino:

- Usar técnicas ofensivas vistas en el área de Red Team para diseñar detecciones concretas.  
- Crear y ajustar reglas en herramientas como Wazuh, SIEM o plataformas similares.  
- Validar detecciones con pruebas de ataque controladas (Purple Team mindset).

Posibles módulos/labs (a futuro):

- Laboratorio de creación de reglas de detección para actividad sospechosa en logs de sistema.  
- Mapeo de laboratorio ofensivo (por ejemplo, ataque a NovaPay Labs) a detecciones específicas.  

---

## 5. Conexión con otras áreaes

El área Blue Team no vive aislada: está pensada para que los estudiantes vean **los mismos escenarios desde ángulos diferentes**.

- **Con Pentesting / Red Team:**  
  Los mismos ataques que se practican en los labs ofensivos (por ejemplo, contra la fintech NovaPay Labs) se reutilizarán como casos de estudio para detección y respuesta en Blue Team.

- **Con Purple Team:**  
  Esta área sienta las bases para, en el futuro, diseñar ejercicios donde Red y Blue colaboran, validando detecciones frente a técnicas ofensivas específicas.

- **Con AI / MLSecOps (más adelante):**  
  La telemetría, detecciones y playbooks que se construyan aquí pueden alimentar módulos avanzados donde se use IA para detección, priorización o automatización.

---

## 6. Tipo de labs y entregables

Al igual que en la ruta ofensiva, los laboratorios de el área Blue Team seguirán un enfoque profesional y progresivo:

- Labs con **narrativa inmersiva** (por ejemplo, incidentes y ataques contra una fintech como NovaPay Labs).  
- Uso de herramientas reales de la industria (Wazuh, SIEM open source, capturas de tráfico, etc.) en entornos controlados.  
- Entregables orientados a portafolio:  
  - Informes de incidente.  
  - Timelines de eventos.  
  - Reglas de detección (o pseudocódigo de reglas).  
  - Casos de hunting documentados.

La progresión empezará por fundamentos claros y labs guiados, y con el tiempo dará más libertad al estudiante para investigar, plantear hipótesis y tomar decisiones de análisis por su cuenta.

---

## 7. Próximos pasos

Los siguientes pasos para esta área podrían ser:

1. Crear el **README del primer módulo Blue Team** (por ejemplo, `01-fundamentos-blue-team-y-soc/`) con objetivos claros y un primer lab muy guiado sobre lectura e interpretación de logs y alertas básicas.  
2. Diseñar un primer **lab de SOC básico** reutilizando eventos/ataques simples desde la ruta ofensiva de NovaPay Labs.  
3. Definir una plantilla de **informe de incidente** en `portafolio/`, similar a las plantillas de recon y pentest, pero orientada a Blue Team.

A medida que se construyan los módulos, esta área se irá actualizando para reflejar las rutas y labs disponibles.
