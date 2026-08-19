# Plantilla — Ficha de Evento SOC / Mini Informe de Laboratorio

> **Uso:** copia esta plantilla dentro de `portafolio/` y renómbrala (por ejemplo, `ficha-evento-soc-lab01.md`). Complétala para cada conjunto de eventos o para el evento más representativo de un lab.

---

## 1. Datos generales

- **Módulo:** `01-fundamentos-blue-team-y-soc`  
- **Lab:** `Lab 01 — Lectura e interpretación básica de eventos SOC` (u otro, si aplica)  
- **Estudiante:** `Tu nombre o alias`  
- **Fecha:** `AAAA-MM-DD`  
- **Fuente de logs principal analizada:**  
  - `Ejemplo: logs_firewall.txt / logs_aplicacion_web.json / logs_autenticacion.txt`

---

## 2. Clasificación del evento / conjunto de eventos

### 2.1 Tipo de fuente

- **Tipo de log principal:**  
  - `[ ] Sistema`  
  - `[ ] Red / Firewall / Proxy`  
  - `[ ] Aplicación / Servidor web`  
  - `[ ] Autenticación / Directorio / IAM`  
  - `[ ] Seguridad (EDR / AV / WAF / otros)`  
- **Justificación breve:**  
  `Ejemplo: Veo campos src_ip, dst_ip y action=ALLOW/BLOCK → parece firewall.`

### 2.2 Tipo de evento

- **Categoría del evento (a alto nivel):**  
  - `[ ] Acceso permitido normal`  
  - `[ ] Acceso bloqueado`  
  - `[ ] Intentos de autenticación`  
  - `[ ] Error de aplicación`  
  - `[ ] Comportamiento anómalo / sospechoso`  
  - `[ ] Otro (especificar): __________`  
- **Motivo de la clasificación:**  
  `Ejemplo: Son varios LOGIN_FAILURE seguidos para el mismo usuario → lo marco como posible comportamiento sospechoso.`

---

## 3. Descripción del evento

### 3.1 Evento específico (o patrón) elegido

- **Evento puntual o patrón de eventos:**  
  `Describe qué evento o grupo de eventos estás analizando. Puede ser una línea concreta de log o un patrón (por ejemplo, "10 intentos de login fallidos desde la IP X en 2 minutos").`  

- **Ejemplo de registro (resumido):**  
  `Copia el evento de forma resumida/anónima, sin datos sensibles reales, solo lo necesario para entenderlo (timestamp, IP, usuario, acción, resultado).`

### 3.2 Contexto conocido

- **¿En qué contexto aparece este evento?**  
  - `¿Forma parte de un periodo normal de operación o coincide con una actividad ofensiva simulada en el lab?`  
  - `¿Hay otros eventos cercanos en el tiempo que parezcan relacionados?`

---

## 4. Análisis del evento

### 4.1 Campos clave identificados

Enumera los campos que consideras más importantes para analizar este evento:

- **Timestamp:**  
  `Ejemplo: 2026-06-09T18:00:15Z`  
- **IP origen:**  
  `Ejemplo: 192.0.2.10`  
- **IP destino / host:**  
  `Ejemplo: 10.20.30.20:443`  
- **Usuario (si aplica):**  
  `Ejemplo: merchant_user01`  
- **Acción / evento:**  
  `Ejemplo: LOGIN_FAILURE / HTTP 404 / BLOCK`  
- **Resultado / código:**  
  `Ejemplo: HTTP 401, HTTP 200, action=BLOCK`  
- **Otros campos relevantes:**  
  `Ejemplo: user-agent, ruta solicitada, regla de firewall, etc.`

### 4.2 Interpretación

Responde brevemente:

1. **¿Qué crees que está pasando en este evento o patrón?**  
   `Describe con tus palabras la situación que representan estos logs.`  
2. **¿Te parece un comportamiento normal, anómalo o claramente malicioso? ¿Por qué?**  
   `Justifica tu respuesta en función de cantidad, frecuencia, origen, destino, etc.`  
3. **¿Qué impacto potencial podría tener si fuera parte de un ataque real?**  
   `Ejemplo: riesgo de fuerza bruta de credenciales, reconocimiento de rutas sensibles, etc.`

### 4.3 Relación con actividades ofensivas

- **¿A qué tipo de actividad ofensiva lo relacionarías?**  
  - `[ ] Reconocimiento (scans, discovery)`  
  - `[ ] Intentos de acceso / fuerza bruta`  
  - `[ ] Explotación de aplicación web`  
  - `[ ] Movimiento lateral / persistencia`  
  - `[ ] Otro (especificar): __________`  
- **Conexión con lo visto en la ruta ofensiva:**  
  `Ejemplo: Esto se parece a los intentos de login con credenciales falsas que hicimos contra el portal de merchants en el Lab 02 de Pentest Web.`

---

## 5. Recomendaciones

En esta sección, propone acciones que un Blue Team podría tomar, incluso si todavía no se han visto todas las técnicas de respuesta.

### 5.1 Acciones inmediatas sugeridas

- `[ ] Registrar y monitorear el patrón`  
- `[ ] Generar una alerta de baja / media / alta prioridad`  
- `[ ] Bloquear o poner en lista de observación la IP origen`  
- `[ ] Revisar otros logs relacionados (autenticación, aplicación, sistema)`  
- `[ ] Escalar al equipo de Incident Response`  
- `[ ] Otro (especificar): __________`  

Explica brevemente el porqué de tus recomendaciones:

> `Ejemplo: Si el número de intentos de login fallidos supera un umbral en poco tiempo, recomendaría generar alerta de prioridad media y revisar si hay otros indicadores de fuerza bruta.`

### 5.2 Mejora de visibilidad / detección

- **¿Qué podrías mejorar en los logs o en la configuración para detectar mejor este tipo de evento en el futuro?**  
  `Ejemplo: añadir más campos al log, configurar umbrales de alertas, correlacionar con otras fuentes.`  

---

## 6. Reflexiones personales

Esta sección es para consolidar tu aprendizaje.

1. **¿Qué aprendiste al analizar este evento o conjunto de eventos?**  
2. **¿Qué te resultó más difícil: entender el formato, identificar los campos clave o interpretar el significado del evento?**  
3. **Si volvieras a analizar un caso similar, qué harías diferente desde el inicio?**  
4. **¿Qué relación ves entre este análisis y lo que hiciste antes en los labs ofensivos (recon, pentest web, etc.)?**  

Puedes responder en párrafos cortos o en forma de lista, lo importante es que quede claro qué te llevas del ejercicio.

---

## 7. Notas adicionales (opcional)

Utiliza este espacio para cualquier detalle extra:

- Comandos que usaste para filtrar/leer logs (aunque sea solo `grep`, `less`, `jq`, etc.).  
- Dudas que te surgieron y que quieras revisar más adelante.  
- Ideas para futuras detecciones o labs relacionados con este tipo de evento.
