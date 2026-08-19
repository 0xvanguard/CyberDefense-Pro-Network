# Lab 02 — Purple Web: Exploración de rutas "raras" en el portal de merchants

> **Área:** 04-purple-team-colaboracion  
> **Escenario:** NovaPay Labs — Portal de merchants  
> **Tipo de lab:** Ejercicio Purple Team básico (reconocimiento de rutas web + detección en logs/SOC).

---

## 1. Narrativa del lab

Además de atacar credenciales, muchos atacantes comienzan explorando **rutas y páginas menos obvias** de una aplicación web: paneles de administración, rutas de prueba, páginas antiguas, etc.

La fintech **NovaPay Labs** quiere saber si su entorno es capaz de **ver y entender** este tipo de reconocimiento sobre el portal de merchants.

Como equipo **Purple Team**:

- Con el gorro **Red**, realizarás una exploración controlada de rutas "curiosas" (como `/admin`, `/backup`, `/test`) contra el portal.  
- Con el gorro **Blue**, revisarás los logs de servidor/aplicación web para identificar el patrón que generan estos accesos.  
- Con el gorro **Purple**, evaluarás qué tan fácil sería detectar este comportamiento y qué tipo de alerta o caso de hunting podrías diseñar.

---

## 2. Alcance del lab

### 2.1 Incluido en el alcance

- Portal de merchants de NovaPay Labs en el entorno de laboratorio.  
- Acceso controlado a un conjunto limitado de rutas poco comunes o no enlazadas desde la página principal.  
- Revisión de logs de servidor/aplicación web (archivos o herramienta SOC usada en Blue Team).  

### 2.2 Fuera de alcance

- Scans agresivos con miles de rutas o herramientas en modo masivo.  
- Ataques de denegación de servicio (DoS).  
- Explotación de vulnerabilidades más allá de la exploración de rutas (inyecciones, etc.).

> Este lab se centra en **ver y entender el reconocimiento de rutas**, no en explotar lo que se encuentre.

---

## 3. Objetivos del lab

Al finalizar este lab deberías ser capaz de:

1. Ejecutar una exploración controlada de rutas "raras" contra el portal de merchants.  
2. Localizar en los logs los accesos a esas rutas y analizar sus códigos de respuesta (404, 403, 200, etc.).  
3. Identificar patrones de reconocimiento (múltiples 404 a rutas distintas, accesos repetidos a `/admin`, etc.).  
4. Formular al menos **una idea de alerta o caso de hunting** para detectar este tipo de actividad.  
5. Documentar el caso en una ficha de evento SOC y generar explicaciones adaptadas a gerente y analista SOC.

---

## 4. Parte Red — Exploración de rutas "raras"

### 4.1 Preparación

1. Asegúrate de conocer la URL principal del portal de merchants (por ejemplo, `https://.../` y la ruta de login).  
2. Elabora una pequeña lista de rutas "curiosas" a probar, por ejemplo:
   - `/admin`  
   - `/backup`  
   - `/test`  
   - `/old`  
   - `/dev`  
   - `/phpinfo` (si tiene sentido en el lab)  

> Usa un número razonable de rutas (por ejemplo, 10–20) para no saturar el servicio.

### 4.2 Ejecución

3. Realiza peticiones hacia esas rutas, de forma manual (navegador) o con una herramienta ligera (curl, burp, una lista pequeña en ffuf/gobuster en modo suave).  
4. Anota en tus notas:  
   - Lista de rutas que probaste.  
   - IP desde la que hiciste las peticiones.  
   - Hora aproximada de inicio y fin de la exploración.

---

## 5. Parte Blue — Análisis de logs de servidor/aplicación

Dependiendo del entorno, tendrás acceso a:

- Archivos de logs de servidor/aplicación web, o  
- Una herramienta SOC (Kibana/Wazuh) con esos logs ya cargados.

### 5.1 Localizar accesos a rutas "raras"

1. Filtra o busca en los logs por:  
   - Rutas concretas (`/admin`, `/backup`, `/test`, etc.).  
   - IP origen usada en la exploración.  
2. Observa los campos clave en los eventos:  
   - Timestamp.  
   - Ruta/URL solicitada.  
   - Código HTTP de respuesta (200, 404, 403, 500, etc.).  
   - IP origen y, si aplica, usuario autenticado.

### 5.2 Identificar patrones de reconocimiento

3. Responde en tus notas:
   - ¿Cuántas rutas distintas probaste que devolvieran 404?  
   - ¿Hubo alguna ruta que devolviera 200/403 y pareciera más sensible (por ejemplo, `/admin`)?  
   - ¿Se ven estas peticiones agrupadas en un período corto desde la misma IP?

4. Describe el patrón de reconocimiento que generaste, por ejemplo:  
   - "12 peticiones a rutas no enlazadas (`/admin`, `/backup`, `/old`, `/test`) en 2 minutos desde la IP 10.0.0.60, la mayoría con respuesta 404".

---

## 6. Parte Purple — Evaluación de detección y casos de hunting

### 6.1 Evaluación

1. Pregúntate:  
   - ¿Un analista SOC podría ver fácilmente este patrón revisando los logs?  
   - ¿Existe ya alguna alerta que dispare ante muchos 404 o accesos a `/admin`?  
2. Si no tienes esa información, asume que no hay reglas específicas y piensa qué visibilidad te gustaría tener.

### 6.2 Propuestas de alerta/hunting

3. Formula al menos **una idea de alerta o caso de hunting**, por ejemplo:
   - "Buscar IPs que hagan más de 15 peticiones con código 404 a rutas distintas en 5 minutos".  
   - "Alertar si se accede a `/admin` desde IPs externas que no lo habían hecho en los últimos 30 días".  
4. Opcionalmente, piensa cómo reducir falsos positivos (por ejemplo, excluir IPs internas de pruebas o ciertos escáneres autorizados).

---

## 7. Entregables del lab

Para completar el lab, deberás preparar:

1. **Ficha de evento SOC** centrada en el patrón de rutas "raras":  
   - Clasificación del tipo de evento (aplicación web, comportamiento de reconocimiento).  
   - Descripción del patrón de exploración de rutas.  
   - Análisis de impacto potencial (preparación para descubrir paneles ocultos o rutas sensibles).  
   - Recomendaciones de detección y respuesta (alertas, casos de hunting, revisión de rutas accesibles).

2. **Explicaciones duales (recomendadas):**  
   - Versión para gerente: 3–4 frases explicando que se observaron intentos de "probar puertas y ventanas" del portal y por qué eso es relevante para el negocio.  
   - Versión para analista SOC: resumen técnico del patrón (404/403/200, rutas probadas, IP de origen) y descripción de la idea de alerta/hunting.

Puedes guardar ambos elementos en un archivo Markdown en tu `portafolio/`, por ejemplo:  
`portafolio/lab02-purple-web-rutas-raras.md`.

---

## 8. Preguntas guía

Incluye respuestas breves a estas preguntas en tu informe o ficha:

1. ¿Por qué es importante detectar reconocimiento de rutas incluso si todavía no se ha explotado nada?  
2. ¿Qué campos de los logs de servidor consideras clave para este tipo de análisis (ruta, código HTTP, IP, timestamp, etc.)?  
3. ¿Qué posibles falsos positivos podría generar una alerta basada en muchos 404?  
4. ¿Cómo combinarías esta información con otros eventos (por ejemplo, login fallidos) para tener una visión más completa del comportamiento de una IP?

---

## 9. Pistas y recomendaciones

- Recuerda que un atacante paciente puede mezclar peticiones "normales" con rutas raras; por eso los patrones sutiles también importan.  
- No te obsesiones con encontrar una ruta crítica: el objetivo del lab es aprender a ver y pensar sobre el **patrón de exploración**, no encontrar el "panel secreto".  
- Puedes inspirarte en los patrones de acceso que ves en labs ofensivos (por ejemplo, en pentest web) para imaginar qué buscarías como Blue/Purple.  
- Piensa siempre cómo explicarías este comportamiento a alguien no técnico: "están probando qué puertas hay en el edificio" suele ser una buena metáfora.

---

**[⬅ Volver al README de el área Purple Team](../../README.md)**
