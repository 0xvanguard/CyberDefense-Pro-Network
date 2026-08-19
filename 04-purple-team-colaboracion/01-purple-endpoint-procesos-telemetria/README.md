# Módulo 01 — Purple Endpoint: procesos, comandos y telemetría de host

> **Área:** 04-purple-team-colaboracion  
> **Enfoque:** Ejercicios Purple Team centrados en la actividad de endpoints (hosts de empleados/servidores) y su reflejo en la telemetría.

---

## 1. Misión del módulo

Mientras que el **Pack Purple Web NovaPay v1** se enfoca en el portal de merchants y sus logs web, este módulo lleva la colaboración Red–Blue al **endpoint**.

La misión es que el estudiante aprenda a:

- Entender qué ocurre en un host cuando se ejecutan comandos típicos de post-explotación ligera (cmd, PowerShell, etc.).  
- Leer la telemetría de procesos en formato simplificado (pseudo‑JSON o tabla) y reconstruir historias de lo que pasó.  
- Conectar acciones ofensivas en el endpoint con señales concretas en la telemetría y proponer ideas de detección.

Este módulo es la base para rutas Purple más avanzadas en **EDR, ATT&CK y detección basada en comportamiento**.

---

## 2. Objetivos de aprendizaje

Al completar este módulo, el estudiante debería ser capaz de:

1. Interpretar eventos de creación de procesos en endpoints (campos `Image`, `ParentImage`, `CommandLine`, `User`, `TimeCreated`).  
2. Diferenciar patrones normales de uso de consola/PowerShell de patrones sospechosos (por ejemplo, PowerShell oculto con comandos codificados).  
3. Reconstruir mini-historias de ataque en endpoint a partir de 3–5 eventos encadenados.  
4. Formular hipótesis de detección para estos patrones (ideas de reglas, umbrales o casos de hunting).  
5. Documentar los casos en fichas de evento SOC y resúmenes ejecutivos orientados tanto a gerencia como a analistas SOC.

---

## 3. Áreas clave del módulo

### 3.1 Telemetría de procesos en endpoint

- Concepto de telemetría de host: eventos de proceso, línea de comandos, usuario, padre/hijo.  
- Diferencia entre ver solo "qué proceso" se ejecutó y entender **quién lo lanzó y con qué parámetros**.

### 3.2 Patrones ofensivos básicos en host

- Reconocimiento simple: comandos como `whoami`, `ipconfig`, `tasklist`, `Get-Process`.  
- Uso legítimo de PowerShell vs uso malicioso (parámetros raros, ejecución oculta, comandos codificados).  
- Casos simples de persistencia/abuso (creación de usuario de prueba en entorno controlado).

### 3.3 Lectura y correlación de eventos

- Cómo leer eventos en formatos simplificados (pseudo‑JSON, tabla de texto).  
- Ordenar eventos por tiempo y usuario para reconstruir una mini‑historia de lo que pasó en el host.

### 3.4 Pensamiento Purple en endpoint

- Conexión entre acciones Red en host y lo que ve Blue (telemetría, EDR/SIEM).  
- Diseñar ideas de detección a partir de historias: qué campos usar, qué condiciones disparar, qué falsos positivos esperar.

---

## 4. Relación con Purple Web, Red y Blue

- **Con Purple Web:**  
  Purple Web muestra cómo los ataques al portal generan señales en logs web; Purple Endpoint extiende el concepto al host, donde los atacantes ejecutan comandos y scripts.  
  Juntos, permiten ver el ciclo completo: desde la superficie externa hasta lo que pasa "dentro" de las máquinas.

- **Con Red Team (endpoint):**  
  Este módulo aprovechará acciones ofensivas sencillas en host (comandos controlados en entornos de lab) para generar eventos.  
  Más adelante, se podrá conectar explícitamente con módulos ofensivos de post-explotación o labs de movimiento lateral.

- **Con Blue Team (telemetría de host/SOC):**  
  Usa la base creada en Blue Team sobre lectura de eventos y visualización de logs, aplicándola a eventos de procesos en endpoint.  
  Refuerza la idea de fichas SOC, análisis de campos clave y construcción de hipótesis de detección.

---

## 5. Idea del primer lab — Purple Endpoint 0X: procesos y PowerShell sospechoso

El primer lab de este módulo se centrará en un escenario sencillo pero muy representativo:

- **Parte Red:** el estudiante ejecuta una serie de comandos controlados en el endpoint:
  - Comandos "normales" de enumeración (`whoami`, `ipconfig`, `tasklist`).  
  - Un ejemplo de uso legítimo de PowerShell (`Get-Process`).  
  - Uno o más ejemplos de PowerShell sospechoso (parámetros como `-WindowStyle Hidden` y `-EncodedCommand`) en un entorno de lab seguro.

- **Parte Blue:** el estudiante analiza los eventos de procesos correspondientes, en formato simplificado (pseudo‑JSON y tabla):  
  - Identifica `Image`, `ParentImage`, `CommandLine`, `User`, `TimeCreated`.  
  - Clasifica eventos como normales, anómalos o sospechosos.  
  - Reconstruye una mini‑historia del caso.

- **Parte Purple:** el estudiante:
  - Elige uno de los patrones sospechosos (por ejemplo, PowerShell oculto con comando codificado).  
  - Completa una ficha de evento SOC para ese caso.  
  - Propone una idea de alerta o regla de detección basada en los parámetros y el contexto (padre/hijo).  
  - Redacta dos versiones de la explicación: una para gerente, otra para analista SOC.

Este lab servirá como "hello world" de Purple Endpoint: un ejemplo claro de cómo un comportamiento ofensivo mínimo en el host deja una huella que Blue puede ver y Purple puede transformar en detección.

---

## 6. Integración progresiva con Red y Blue específicos

A medida que el módulo avance, se podrán añadir:

- Labs donde las acciones Red en endpoint estén conectadas a 
  - resultados de un lab ofensivo previo (por ejemplo, tras comprometer credenciales en el portal), o  
  - simulaciones de movimiento lateral básico.  
- Ejercicios donde la telemetría de host se vea tanto en formato simplificado como dentro de una herramienta SOC (Wazuh/ELK), reutilizando el aprendizaje del módulo Blue Team sobre visualización de eventos.

De esta forma, Purple Endpoint se convertirá en el puente natural entre:

- Lo que los estudiantes aprenden sobre ataques en entornos Red, y  
- Lo que descubren sobre detección, hunting y respuesta en el área Blue Team.

---

**[⬅ Volver al README de el área Purple Team](../README.md)**
