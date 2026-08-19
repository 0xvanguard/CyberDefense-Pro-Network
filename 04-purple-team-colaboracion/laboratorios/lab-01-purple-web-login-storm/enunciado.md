# Lab 01 — Purple Web: Login storm controlado en el portal de merchants

> **Área:** 04-purple-team-colaboracion  
> **Escenario:** NovaPay Labs — Portal de merchants  
> **Tipo de lab:** Ejercicio Purple Team básico (ataque de login controlado + detección en logs/SOC).

---

## 1. Narrativa del lab

La fintech **NovaPay Labs** quiere validar si su entorno es capaz de detectar un patrón muy típico de ataque: **múltiples intentos de login fallidos** contra el portal de merchants.

Como equipo **Purple Team**, te pondrás dos gorros:

- Con el gorro **Red**, simularás un pequeño "login storm" controlado contra el portal de merchants (sin llegar a fuerza bruta agresiva ni DoS).  
- Con el gorro **Blue**, buscarás cómo se reflejan esos intentos en los logs de autenticación/aplicación web y evaluarás si sería fácil o difícil detectarlos en un SOC.  

Tu objetivo es ver el ciclo completo: **lo que hace el atacante, cómo lo ve el sistema y qué alerta podrías diseñar**.

---

## 2. Alcance del lab

### 2.1 Incluido en el alcance

- Portal de merchants de NovaPay Labs en el entorno de laboratorio.  
- Generación controlada de intentos de login fallidos usando una cuenta de prueba o credenciales claramente falsas.  
- Revisión de logs de autenticación/aplicación web (en archivos o en la herramienta SOC que se esté usando en Blue Team: ELK/Wazuh u otra).  

### 2.2 Fuera de alcance

- Fuerza bruta masiva (uso de diccionarios grandes o miles de intentos).  
- Ataques de denegación de servicio (DoS).  
- Explotación de vulnerabilidades distintas al login (inyecciones, etc.).

> Este lab se centra en **patrones de login fallido** y su visibilidad, no en agotar el servicio ni en explotar otras funciones.

---

## 3. Objetivos del lab

Al finalizar este lab deberías ser capaz de:

1. Ejecutar un conjunto de intentos de login fallidos de forma controlada contra el portal de merchants.  
2. Localizar esos eventos en los logs de autenticación/aplicación web y confirmar que la telemetría captura usuario, IP y resultado.  
3. Identificar un patrón simple de login storm (N fallos en X minutos desde la misma IP/usuario).  
4. Formular al menos **una idea de alerta o regla** para detectar este patrón en un SOC.  
5. Documentar el caso en una ficha de evento SOC y resumirlo en lenguaje técnico y en lenguaje para gerencia.

---

## 4. Parte Red — Simulación de login storm controlado

### 4.1 Preparación

1. Identifica la URL de login del portal de merchants (por ejemplo, `/login` o similar).  
2. Asegúrate de que estás usando:  
   - Una cuenta de prueba provista por el lab, **o**  
   - Credenciales claramente falsas (usuario/contraseña inventados) que no correspondan a usuarios reales.  

### 4.2 Ejecución

3. Realiza un número limitado de intentos de login fallidos, por ejemplo entre **10 y 20 intentos**, en un periodo de unos pocos minutos.  
4. Puedes hacerlos manualmente (introduciendo credenciales erróneas varias veces) o con un script/ferramienta ligera, siempre respetando los límites de este lab.  
5. Anota en tus notas:  
   - IP desde la que haces los intentos (tu máquina de laboratorio).  
   - Usuario(s) utilizado(s) en los intentos.  
   - Ventana de tiempo aproximada (inicio y fin de la prueba).

> La idea es generar un patrón claro pero **no agresivo**, que se vea en los logs sin dañar el entorno.

---

## 5. Parte Blue — Búsqueda y análisis en los logs

Dependiendo del entorno, tendrás acceso a:

- Archivos de logs de autenticación/aplicación web, o  
- Una herramienta SOC (por ejemplo, Kibana/Wazuh) donde esos eventos ya están cargados.

### 5.1 Localizar los eventos de login

1. Filtra o busca en los logs usando alguno de estos criterios:  
   - Usuario utilizado en los intentos.  
   - IP origen desde donde ejecutaste el login storm.  
   - Resultado `LOGIN_FAILURE` (o equivalente).  
2. Confirma que puedes ver:  
   - Timestamp de cada intento.  
   - Usuario (o identificador similar).  
   - IP origen.  
   - Resultado (fallido).

### 5.2 Identificar el patrón de login storm

3. Observa el conjunto de eventos y responde:  
   - ¿Cuántos intentos fallidos se ven en el intervalo de tiempo que generaste?  
   - ¿Son todos del mismo usuario, de la misma IP o variados?  
4. Describe el patrón en tus notas, por ejemplo:  
   - "15 intentos de login fallidos para el usuario `merchant_test` en 3 minutos desde la IP 10.0.0.50".

---

## 6. Parte Purple — Evaluación de detección y propuesta de alerta

### 6.1 Evaluación

1. Pregúntate:  
   - ¿Un analista SOC vería fácilmente este patrón hoy, con los logs disponibles?  
   - ¿Existe alguna alerta ya configurada para muchos login fallidos?  
2. Si no tienes esa información, asume que **no hay alerta específica** y piensa qué te gustaría que existiera.

### 6.2 Propuesta de alerta

3. Formula al menos **una idea de alerta** o regla en lenguaje natural, por ejemplo:  
   - "Generar alerta de prioridad media si un mismo usuario tiene más de 10 intentos de login fallidos en 5 minutos".  
   - "Generar alerta si una misma IP produce más de 20 login fallidos contra cualquier usuario en 10 minutos".  
4. Opcionalmente, añade condiciones adicionales si quieres afinar (por ejemplo, que la alerta solo aplique a ciertos roles/sistemas críticos).

---

## 7. Entregables del lab

Para completar el lab, deberás preparar:

1. **Ficha de evento SOC** centrada en el login storm (usa `TEMPLATE-ficha-evento-soc.md` de Blue Team/Purple adaptada al caso):  
   - Clasificación del tipo de evento (autenticación, comportamiento sospechoso).  
   - Descripción del patrón (qué se hizo como Red, qué se vio como Blue).  
   - Análisis de impacto potencial (riesgo de fuerza bruta de credenciales).  
   - Recomendaciones de detección y respuesta (alerta propuesta, revisión de otros eventos, etc.).  

2. **Explicación dual (recomendada):**  
   - Versión para gerente de NovaPay (3–4 frases): lenguaje simple, impacto en negocio, acción propuesta.  
   - Versión para analista SOC: resumen técnico del patrón, campos clave en los logs y descripción de la alerta propuesta.

Puedes colocar ambos elementos en un archivo Markdown en tu `portafolio/`, por ejemplo:  
`portafolio/lab01-purple-web-login-storm.md`.

---

## 8. Preguntas guía

Incluye respuestas breves a estas preguntas en tu informe o ficha:

1. ¿Qué diferencia hay entre un par de login fallidos aislados y el patrón que generaste en este lab?  
2. ¿Qué campos de los logs consideras mínimos para poder detectar un login storm (usuario, IP, tiempo, resultado, etc.)?  
3. ¿Qué podría pasar si este patrón no se detecta nunca en un entorno real?  
4. ¿Qué posibles falsos positivos crees que podrían aparecer con la alerta que propusiste?

---

## 9. Pistas y recomendaciones

- Si no ves tus eventos en los logs, revisa primero el **rango de tiempo** y los filtros aplicados (es un error común).  
- Si el lab usa archivos de logs en lugar de SIEM, puedes apoyarte en herramientas simples (`grep`, filtros por texto) para buscar por usuario o IP.  
- No busques una "alerta perfecta" en el primer intento: es mejor una idea sencilla pero clara que nada.  
- Como Purple Team, recuerda que tu misión es usar lo que aprendiste en Red para mejorar lo que se ve y se detecta en Blue.

---

**[⬅ Volver al README de el área Purple Team](../../README.md)**
