# Lab 01 — Mapeo de superficie básico (NovaPay Labs)

> **Tipo de lab:** Reconocimiento OSINT técnico clásico (sin IA)  
> **Rol simulado:** Consultor externo de ciberseguridad realizando la fase de recon de un pentest

---

## 1. Narrativa: NovaPay Labs

**NovaPay Labs** es una startup fintech que está preparando el lanzamiento de una plataforma de pagos para pequeños comercios.

- Su producto principal es un **portal web para merchants** donde pueden gestionar pagos, clientes y reportes.  
- Además, tiene un **sitio público de marketing** con información comercial.  
- La empresa sospecha que podría haber **servicios internos expuestos** por errores de configuración en su infraestructura de pruebas.

Antes de ir a producción, NovaPay contrata a tu equipo para realizar una **evaluación externa limitada solo a reconocimiento técnico**, con el objetivo de entender qué está exponiendo a Internet (o al rango de pruebas) sin darse cuenta.

Tú eres la persona encargada de ejecutar esta fase de recon y entregar un **informe de reconocimiento inicial**.

---

## 2. Scope del lab

En este lab trabajas **exclusivamente** sobre un entorno de laboratorio controlado.

### 2.1 Alcance autorizado

- **Dominio simulado:**  
  - `novapay-labs.local`  

- **Rango de red del laboratorio:**  
  - `10.20.30.0/24`  

- **Tipo de actividades permitidas:**  
  - Reconocimiento pasivo sobre el dominio simulado (WHOIS/DNS según esté configurado en el lab).  
  - Descubrimiento de hosts dentro de `10.20.30.0/24`.  
  - Enumeración de puertos y servicios de los hosts que encuentres **dentro del rango autorizado**.  

### 2.2 Fuera de alcance

- Cualquier IP fuera de `10.20.30.0/24`.  
- Cualquier dominio real en Internet que no sea parte del lab.  
- Fuerza bruta de credenciales, fuzzing agresivo o ataques de denegación de servicio.  
- Ejecución de exploits o explotación de vulnerabilidades (eso se verá en módulos posteriores).

> **Recordatorio:** romper el scope en un entorno real es motivo para terminar el contrato y, en casos graves, problemas legales. Practica la disciplina desde el lab.

---

## 3. Objetivo del lab

El objetivo principal es **mapear la superficie de ataque de NovaPay Labs** dentro del rango autorizado y **documentarla** en un informe de recon profesional.

Concretamente, al terminar el lab deberías haber:

1. Identificado qué hosts dentro de `10.20.30.0/24` están vivos.  
2. Enumerado puertos y servicios principales de esos hosts.  
3. Clasificado qué hosts parecen:  
   - Sitio público de marketing.  
   - Portal de merchants / panel administrativo.  
   - Servicios internos o de backend.  
4. Generado un informe `informe-recon-novapay-labs.md` basado en la plantilla `TEMPLATE-informe-recon.md`.  

No se trata de explotar nada, solo de **ver y entender** qué hay expuesto.

---

## 4. Retos del lab (HTB-style)

Además de cumplir el objetivo general, intenta resolver estos retos:

1. **Reto 1 — Cartografía completa:**  
   - Identifica todos los hosts vivos dentro de `10.20.30.0/24` (según la configuración del lab).  
   - Inclúyelos en tu tabla de hosts y servicios.

2. **Reto 2 — ¿Dónde vive el negocio?**  
   - Determina qué host parece ser el **frontend público** (sitio de marketing) de NovaPay Labs.  
   - Determina qué host parece ser el **portal para merchants** (panel con login).  
   - Justifica tu respuesta en la sección de observaciones de tu informe.

3. **Reto 3 — Algo huele raro:**  
   - Encuentra al menos un puerto/servicio que, en tu opinión, **no encaja** con el perfil de una fintech (por ejemplo, un servicio innecesario o un puerto poco habitual).  
   - Explícalo brevemente en las hipótesis de futuros vectores.

4. **Reto 4 — Resumen ejecutivo convincente:**  
   - Escribe un resumen ejecutivo de 3–6 líneas que cualquier gerente entienda, sin tecnicismos innecesarios, explicando qué exposición encontraste y qué recomendarías como siguiente paso.

---

## 5. Guía de trabajo sugerida (no es una receta rígida)

Usa las fases de reconocimiento del módulo como referencia. [No tienes que seguirlas al pie de la letra, pero te ayudarán a tener orden.]

### Paso 1 — Preparar el informe

1. Copia la plantilla de informe:  
   `portafolio/TEMPLATE-informe-recon.md` → `portafolio/informe-recon-novapay-labs.md`.  
2. Rellena desde ya la sección de **Datos generales** y el **Scope** con la información del lab.

### Paso 2 — Reconocimiento pasivo (si aplica en tu entorno)

3. Intenta obtener información básica del dominio simulado `novapay-labs.local` usando herramientas como `whois` y `dig` (según cómo esté configurado el lab).  
4. Anota cualquier dato útil en tu informe (registros DNS, posibles subdominios, etc.).

### Paso 3 — Descubrimiento de hosts

5. Usa Nmap (u otra herramienta equivalente) para descubrir hosts activos en `10.20.30.0/24`.  
6. Añade los hosts identificados a tu tabla en la sección de Hallazgos.

### Paso 4 — Enumeración de puertos y servicios

7. Para cada host que encontraste, ejecuta un escaneo de puertos razonable (por ejemplo, puertos comunes o top 1000).  
8. Identifica qué servicios parecen correr en esos puertos (HTTP, HTTPS, SSH, etc.).  
9. Completa la tabla de hosts/servicios con estos datos.

### Paso 5 — Clasificación y observaciones

10. Intenta clasificar cada host según su función probable: marketing, portal merchants, servicio interno, etc.  
11. Anota tus observaciones y primeras hipótesis en la sección correspondiente del informe.

### Paso 6 — Resumen ejecutivo

12. Escribe el resumen ejecutivo pensando en alguien que no va a mirar la tabla técnica, pero necesita saber **qué tan expuesto** está NovaPay Labs y qué hacer después.

---

## 6. Entregables

Para considerar el lab como completado, deberás tener:

1. Archivo `portafolio/informe-recon-novapay-labs.md` completado, basado en la plantilla.  
2. Tabla de hosts/servicios bien estructurada.  
3. Observaciones e hipótesis coherentes con lo que encontraste.  
4. Resumen ejecutivo claro y entendible.

Opcionalmente, puedes guardar también:

- Un archivo de notas con comandos utilizados.  
- Capturas de pantalla (si el lab y el entorno lo permiten) para tu propio portafolio.

---

## 7. Pistas opcionales (solo si te atascas)

- Si tu escaneo no encuentra ningún host, revisa:  
  - ¿Estás usando el rango correcto (`10.20.30.0/24`)?  
  - ¿El escaneo está en modo host discovery (`-sn`) o solo puertos?  

- Si ves muchos puertos, empieza por los más comunes (22, 80, 443, 8080, 8443) antes de intentar un escaneo completo.

- Si no sabes qué hace un servicio, fíjate primero en el puerto y luego, si el entorno lo permite, intenta acceder de forma normal (por ejemplo, visitar un HTTP/HTTPS en el navegador) **sin hacer fuzzing ni fuerza bruta**.

---

**[⬅ Volver al README del módulo](../../README.md)**
