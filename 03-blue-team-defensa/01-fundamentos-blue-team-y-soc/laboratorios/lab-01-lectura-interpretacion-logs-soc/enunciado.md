# Lab 01 — Lectura e interpretación básica de eventos SOC

> **Área:** 03-blue-team-defensa  
> **Módulo:** 01-fundamentos-blue-team-y-soc  
> **Tipo de lab:** Teórico–práctico con logs estáticos (texto/JSON), sin necesidad de montar herramientas.

---

## 1. Narrativa del lab

Imagina que eres analista Junior en el **SOC de una fintech** (como NovaPay Labs).  
Tu equipo te entrega varios archivos de logs estáticos que representan eventos de un periodo corto de tiempo.

Tu misión en este lab no es usar SIEMs ni herramientas complejas, sino **aprender a leer y entender los eventos**, identificando:

- Qué tipo de fuente los genera (sistema, red, aplicación, seguridad).  
- Qué campos importantes aparecen (IP, usuario, acción, resultado).  
- Cuáles parecen eventos rutinarios y cuáles podrían indicar algo sospechoso.

Este es el primer contacto con la "materia prima" de un SOC: los logs.

---

## 2. Material del lab (logs simulados)

Para este lab se usarán uno o varios archivos de ejemplo (en texto plano o JSON), por ejemplo:

- `logs_firewall.txt`  
- `logs_aplicacion_web.json`  
- `logs_autenticacion.txt`  

Cada archivo contendrá eventos **simulados** inspirados en un entorno fintech, incluyendo:

- Tráfico permitido y bloqueado en el firewall.  
- Peticiones HTTP a un portal web (incluyendo algunas a rutas "raras").  
- Intentos de autenticación exitosos y fallidos.  

> Nota: en esta primera versión del lab, basta con que el estudiante reciba estos archivos como parte del material del curso (no es necesario generarlos dinámicamente).

---

## 3. Objetivos del lab

Al finalizar este lab deberías ser capaz de:

1. Diferenciar al menos **tres tipos de fuentes de logs** (por ejemplo, firewall, aplicación web, autenticación).  
2. Identificar campos clave en eventos de logs (IP origen/destino, usuario, acción, resultado, timestamp).  
3. Reconocer patrones que podrían indicar comportamientos sospechosos básicos (por ejemplo, muchos intentos de login fallidos, accesos repetidos a la misma ruta).  
4. Explicar con tus palabras cómo estos eventos podrían verse en un SOC real y qué haría un analista con ellos.

---

## 4. Tareas de análisis

### Tarea 1 — Clasificar la fuente de los logs

Para cada archivo:

1. Abre el archivo y revisa varios eventos.  
2. Responde:  
   - ¿De qué tipo de sistema crees que vienen estos logs?  
   - ¿Los clasificarías como logs de **sistema**, **red**, **aplicación** o **seguridad**?  
3. Justifica brevemente tu respuesta (por ejemplo, "veo campos como src_ip/dst_ip y action=ALLOW/BLOCK, así que parece un firewall").

### Tarea 2 — Identificar campos clave

Elige entre 5 y 10 eventos de cada archivo y, para cada evento:

1. Señala:  
   - Timestamp (fecha y hora).  
   - IP origen y destino (si aplica).  
   - Usuario (si aplica).  
   - Acción o evento (por ejemplo, LOGIN_SUCCESS, LOGIN_FAILURE, HTTP 200/404/500, ALLOW/BLOCK).  
2. Explica por qué cada uno de esos campos es importante para un analista SOC.

### Tarea 3 — Detectar patrones interesantes

Mirando los logs como conjunto (no solo evento por evento):

1. ¿Ves **múltiples intentos de login fallidos** desde la misma IP o para el mismo usuario?  
2. ¿Observas accesos repetidos a una ruta web poco común (por ejemplo, `/admin`, `/test`, `/backup`)?  
3. ¿Notas tráfico bloqueado recurrente hacia un mismo destino interno?  

Para cada patrón que encuentres:

- Describe el patrón (qué ves y dónde).  
- Indica por qué podría ser interesante o sospechoso.  
- Explica si crees que justificaría una alerta o al menos una revisión más detallada.

### Tarea 4 — Conectar con la ruta ofensiva

Piensa en lo que has visto en la ruta ofensiva (recon, escaneos, intentos de acceso a portales):

1. Elige **un ejemplo ofensivo** (por ejemplo, un escaneo de puertos o muchos intentos de login con credenciales falsas).  
2. Explica cómo crees que se vería esa actividad en los logs de firewall, autenticación o aplicación web.  
3. Relaciona al menos un evento de los archivos proporcionados con ese tipo de actividad.

---

## 5. Preguntas guía

Incluye en tu informe respuestas claras (pueden ser en formato lista o párrafos breves) a estas preguntas:

1. ¿Qué diferencia ves entre un log de firewall y un log de aplicación web?  
2. ¿Qué campos consideras mínimos para poder investigar un evento de login fallido?  
3. ¿Cuándo muchos intentos de login fallidos deberían empezar a preocuparte como analista SOC?  
4. ¿Por qué es útil que los logs tengan timestamps claros y en una zona horaria consistente?  
5. Elige un evento que te parezca especialmente sospechoso y explica qué pasos tomarías a continuación (aunque sea a nivel conceptual, sin herramientas).

---

## 6. Entregables del lab

Para considerar el lab como completado, deberás entregar (o dejar listos en tu `portafolio/`):

1. **Informe breve de análisis de logs** (por ejemplo, `informe-lab01-logs-soc.md`) con:  
   - Clasificación de las fuentes de logs (por archivo).  
   - Ejemplos de eventos con campos clave identificados.  
   - Patrones interesantes encontrados y su posible significado.  
   - Conexión con al menos un ejemplo ofensivo (cómo se vería en los logs).  
2. **Respuestas a las preguntas guía** del apartado 5 (pueden ir dentro del mismo informe, en una sección final).  

> Este informe será el primer artefacto de tu portafolio Blue Team, aunque sea básico.

---

## 7. Pistas y recomendaciones

- No intentes "adivinar" cosas que no se ven en los logs: concéntrate en lo que sí tienes (campos, patrones).  
- Si un evento no te queda claro, describe qué entiendes y qué información te faltaría para estar seguro.  
- Usa la experiencia de la ruta ofensiva como contexto: pregúntate siempre "si yo fuera atacante y hiciera X, ¿cómo se vería aquí?".  
- No te preocupes todavía por queries complejas o reglas SIEM: este lab es para aprender a **mirar y pensar**.

---

**[⬅ Volver al README del módulo 01](../README.md)**
