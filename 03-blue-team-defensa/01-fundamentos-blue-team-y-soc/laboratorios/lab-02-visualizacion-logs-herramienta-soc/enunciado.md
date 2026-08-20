# Lab 02 — Visualización de eventos SOC en una herramienta (ELK/Wazuh)

> **Área:** 03-blue-team-defensa  
> **Módulo:** 01-fundamentos-blue-team-y-soc  
> **Tipo de lab:** Práctico guiado usando una herramienta sencilla (por ejemplo, ELK o Wazuh) para visualizar logs.

---

## 1. Narrativa del lab

Sigues siendo analista Junior en el SOC de una fintech (similar a NovaPay Labs).  
En el **Lab 01** trabajaste con archivos de logs estáticos y aprendiste a leer eventos "a mano".

En este **Lab 02**, tu equipo te da acceso a una **plataforma de monitoreo** ya preparada (por ejemplo, un entorno de práctica con ELK o Wazuh) donde se han cargado eventos similares a los que viste en el lab anterior.

Tu misión ahora es:

- Ver cómo esos mismos eventos se muestran en una herramienta real.  
- Aprender a usar paneles, filtros y búsquedas básicas.  
- Identificar patrones interesantes desde la vista de la herramienta y documentarlos.

No tendrás que instalar ni configurar la plataforma desde cero; el foco está en **aprender a mirar, buscar y pensar** dentro de la herramienta.

---

## 2. Alcance del lab

### 2.1 Incluido en el alcance

- Uso de una instancia de práctica de **ELK (Elasticsearch + Kibana)** o **Wazuh** (según indique el entorno del curso).  
- Visualización de eventos ya cargados (firewall, aplicación web, autenticación).  
- Uso de funciones básicas:  
  - Selección de índice o fuente de datos.  
  - Búsqueda simple por campos (IP, usuario, acción).  
  - Filtros por tiempo.  
  - Visualización de tablas/listas de eventos.  

### 2.2 Fuera de alcance

- Instalación desde cero del stack ELK/Wazuh.  
- Creación de reglas avanzadas o dashboards complejos.  
- Tareas de administración de la plataforma (gestión de nodos, índices, etc.).

> Este lab se centra en que entiendas cómo usar la herramienta como **analista**, no como administrador.

---

## 3. Objetivos del lab

Al finalizar este lab deberías ser capaz de:

1. Acceder a una herramienta de monitoreo (ELK/Wazuh) y orientarte en su interfaz principal.  
2. Localizar los eventos de un tipo de log (por ejemplo, firewall o autenticación) usando filtros básicos.  
3. Buscar eventos específicos por IP, usuario, ruta o tipo de acción.  
4. Identificar patrones simples (por ejemplo, múltiples login fallidos desde una misma IP) utilizando la herramienta.  
5. Documentar tus hallazgos en una **ficha de evento SOC** o mini informe, conectando lo visto en Lab 01 con esta experiencia.

---

## 4. Material del lab

El material e instrucciones concretas dependerán del entorno del curso, pero en general tendrás:

- Una **URL** de acceso a la plataforma (por ejemplo, interfaz web de Kibana o Wazuh).  
- Un **usuario y contraseña** genéricos para el entorno de práctica.  
- Uno o varios **índices/espacios de datos** ya preparados con:  
  - Eventos de firewall (tráfico permitido/bloqueado).  
  - Eventos de aplicación web (peticiones HTTP a un portal).  
  - Eventos de autenticación (login success/failure).  
- Una guía breve de referencia con capturas o indicaciones de dónde encontrar:  
  - El buscador principal.  
  - Los filtros de tiempo.  
  - La vista de lista de eventos.

---

## 5. Tareas del lab (enfoque guiado)

### Tarea 1 — Orientación en la herramienta

1. Accede a la herramienta con las credenciales proporcionadas.  
2. Identifica:  
   - Dónde se realiza la selección de índice o fuente de datos.  
   - Dónde se establece el rango de tiempo (por ejemplo, última hora, último día).  
   - Dónde se muestran los eventos en forma de lista.  
3. Toma nota (o captura de pantalla, si está permitido) de la vista principal que usarás para trabajar.

### Tarea 2 — Buscar eventos de firewall

1. Selecciona el índice/fuente de datos correspondiente a **logs de firewall**.  
2. Aplica un rango de tiempo que incluya los eventos del ejercicio (según indicaciones del lab).  
3. Filtra o busca por alguno de estos criterios (según lo disponible):  
   - IP origen concreta.  
   - Acción = ALLOW/BLOCK.  
   - Puerto o servicio (por ejemplo, 443, 80).  
4. Anota al menos **un patrón interesante** que veas (por ejemplo, varios bloques desde la misma IP hacia un destino interno).

### Tarea 3 — Buscar eventos de autenticación

1. Cambia al índice/fuente de datos de **logs de autenticación**.  
2. Realiza búsquedas o filtros por:  
   - Usuario concreto (si conoces alguno del Lab 01).  
   - Resultado = LOGIN_FAILURE o similar.  
3. Intenta responder:  
   - ¿Hay usuarios con muchos login fallidos en poco tiempo?  
   - ¿Hay IPs que parecen probar varios usuarios distintos?  
4. Anota un ejemplo concreto de patrón sospechoso.

### Tarea 4 — Buscar eventos de aplicación web

1. Cambia al índice/fuente de datos de **logs de aplicación web**.  
2. Filtra/busca por:  
   - Rutas específicas (por ejemplo, `/login`, `/admin`, `/test`).  
   - Códigos HTTP (404, 500, etc.).  
3. Identifica si hay:  
   - Muchos accesos a una ruta poco común.  
   - Errores repetidos (por ejemplo, muchos 404 a rutas que parecen inventadas).  
4. Elige un patrón y relaciónalo con una posible actividad de reconocimiento o prueba de rutas.

### Tarea 5 — Conectar con el Lab 01 y documentar

1. Elige un patrón interesante (por ejemplo, login fallidos masivos o accesos repetidos a `/admin`).  
2. Vuelve a la **plantilla de ficha de evento SOC** (`TEMPLATE-ficha-evento-soc.md`) en `03-blue-team-defensa/portafolio/`.  
3. Complétala para este patrón, incluyendo clasificación, descripción, análisis, recomendaciones y reflexiones personales.  
4. Guarda tu ficha en `portafolio/` con un nombre como `ficha-evento-soc-lab02-<algo-descriptivo>.md`.

---

## 6. Preguntas guía

Responde en tu informe o ficha (pueden ser respuestas breves):

1. ¿Qué diferencia notaste entre analizar los logs a mano (Lab 01) y verlos en la herramienta?  
2. ¿Qué te resultó más fácil con la herramienta (por ejemplo, filtrar, buscar por IP, ver rangos de tiempo)?  
3. ¿Qué te sigue pareciendo complicado o confuso al usar ELK/Wazuh en este nivel?  
4. Si tuvieras que explicarle a otra persona qué hace un analista SOC al ver estos paneles, ¿cómo lo resumirías en 3–4 frases?  

---

## 7. Entregables del lab

Para considerar el lab como completado, deberás entregar (o dejar listos en tu `portafolio/`):

1. Al menos **una ficha de evento SOC** completada a partir de un patrón encontrado en la herramienta (usando la plantilla oficial).  
2. Un breve resumen (puede ser una sección dentro de la ficha o un archivo aparte) con las respuestas a las preguntas guía del apartado 6.  

Opcionalmente, si las normas del curso lo permiten, puedes conservar capturas de pantalla donde se vea la búsqueda o filtro que usaste, siempre cuidando no exponer información sensible real.

---

## 8. Pistas y recomendaciones

- Empieza simple: primero asegúrate de ver **cualquier evento**, luego ve afinando la búsqueda.  
- No intentes dominar toda la herramienta en un solo lab: céntrate en saber **buscar y filtrar**.  
- Si algo no funciona (no ves eventos, filtros vacíos), revisa el rango de tiempo: es un error muy común dejar un rango sin datos.  
- Piensa siempre como analista: "¿qué me está diciendo este patrón?", más allá de solo ver números.  

---

**[⬅ Volver al README del módulo 01](../../README.md)**
