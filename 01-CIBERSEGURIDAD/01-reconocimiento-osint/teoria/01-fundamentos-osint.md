# Fundamentos de OSINT y Reconocimiento Técnico

> **Objetivo de este documento:** darte el marco mínimo de conceptos y fases para que entiendas **qué estás haciendo** cuando ejecutas reconocimiento OSINT técnico en un pentest.

Este texto no busca ser un libro; es una guía compacta que podrás revisar rápido antes de cada lab.

---

## 1. ¿Qué es OSINT?

**OSINT (Open Source Intelligence)** es la obtención y análisis de información a partir de **fuentes públicas o accesibles sin intrusión**.

En ciberseguridad, las fuentes OSINT pueden incluir:

- Motores de búsqueda (Google, Bing, DuckDuckGo).
- Registros de dominios (WHOIS), DNS públicos, certificados (CRT).
- Repositorios públicos (GitHub, GitLab).
- Redes sociales y perfiles profesionales.
- Documentos expuestos (PDF, DOCX, hojas de cálculo).

OSINT no implica todavía explotar vulnerabilidades: se trata de **entender el contexto y la exposición** del objetivo.

---

## 2. Reconocimiento técnico aplicado a pentesting

Dentro de un pentest, el enfoque se vuelve más concreto: pasas de información general a **superficie técnica de ataque**.

Cuando hablamos de **reconocimiento técnico**, nos interesan principalmente:

- Dominios y subdominios relacionados con la organización.
- Direcciones IP y rangos de red asociados.
- Puertos abiertos y servicios escuchando.
- Tecnologías visibles (servidores web, frameworks, CMS, versiones).

El reconocimiento técnico se puede dividir en dos grandes tipos:

- **Reconocimiento pasivo:**
  - Intentas aprender del objetivo sin enviarle tráfico directo (o lo mínimo posible).
  - Ejemplos: consultar WHOIS, revisar DNS públicos, usar buscadores, revisar certificados en CRT.

- **Reconocimiento activo controlado:**
  - Envías tráfico directamente al objetivo dentro del **scope autorizado**.
  - Ejemplos: escanear un rango de IP con Nmap, enumerar puertos/servicios de un host.

En este módulo combinaremos ambos enfoques, siempre dentro de los límites éticos y legales definidos.

---

## 3. Importancia del scope

Antes de escribir un solo comando, en un entorno profesional siempre se define el **scope**:

- Qué dominios están incluidos (por ejemplo: `empresa-ficticia.local`, `intranet.local`).
- Qué rangos de IP puedes tocar (por ejemplo: `10.10.10.0/24`).
- Qué partes están explícitamente fuera de alcance.

Trabajar **fuera del scope** es un error grave en un pentest real.

En nuestros labs, el scope estará claramente definido en el enunciado; tu tarea será respetarlo y documentarlo en tu informe de recon.

---

## 4. Fases típicas de reconocimiento

A nivel práctico, puedes pensar el reconocimiento en **cinco fases**. No siempre son lineales, pero ayudan a ordenar el trabajo.

### 4.1 Definir scope y contexto

- Anotar dominios, subdominios conocidos, rangos de IP de laboratorio.
- Entender, aunque sea de forma simple, **qué negocio simula el lab** (app web, intranet, servicio expuesto, etc.).

### 4.2 Reconocimiento pasivo

Ejemplos de tareas:

- Consultar WHOIS para ver información de registro de dominio.
- Revisar registros DNS públicos (A, AAAA, MX, NS, TXT).
- Ver si hay subdominios obvios (dev, test, staging) mencionados en certificados o registros.

En esta fase, todavía puedes aprender mucho sin escanear nada.

### 4.3 Descubrimiento de hosts

Aquí empiezas a responder:

- ¿Qué IPs dentro del rango están activas?
- ¿Qué responde a ping? (cuando tiene sentido)
- ¿Qué hosts responden a ciertos tipos de paquetes?

Herramientas típicas: Nmap en modo host discovery.

### 4.4 Enumeración de puertos y servicios

Una vez que sabes qué hosts están vivos, pasas a:

- Identificar puertos abiertos (por ejemplo, 22, 80, 443, 445, etc.).
- Obtener información básica del servicio: banners, versiones aparentes.

Con esto puedes empezar a formar hipótesis:

- "Este host parece un servidor web antiguo".
- "Este otro expone SMB y puede tener recursos interesantes".

### 4.5 Organización de hallazgos

Todo lo anterior pierde valor si no lo organizas bien. Lo recomendable es:

- Mantener una tabla por host: IP, puertos, servicios, notas.
- Marcar posibles vectores a revisar más adelante (por ejemplo, `HTTP en 8080 con panel de login`).
- Guardar comandos útiles en un archivo de notas.

Este orden hará que el lab de mapeo de superficie sea más fácil de seguir y repetir.

---

## 5. Ejemplo simple de flujo de trabajo

Imagina que el lab te da este scope:

- Dominio: `empresa-ficticia.local` (simulado en el lab).
- Rango de red: `10.10.10.0/24`.

Un posible flujo sería:

1. Anotar el scope en tu informe (`informe-recon-inicial.md`).
2. Hacer una consulta WHOIS y algunas consultas DNS básicas.
3. Ejecutar un host discovery sobre `10.10.10.0/24` para ver qué IPs responden.
4. Para cada IP viva, hacer un escaneo de puertos limitado (por ejemplo, puertos más comunes).
5. Crear una tabla con los hosts, puertos y servicios encontrados.
6. Escribir un pequeño resumen de qué infraestructura parece existir en ese lab.

Este tipo de flujo será la base del **Lab 01 — Mapeo de superficie básico**.

---

## 6. Cómo usar este archivo en el módulo

Antes de cada actividad o lab de recon, puedes:

- Revisar rápidamente las definiciones de OSINT y recon técnico.
- Recordar las cinco fases y en cuál estás trabajando.
- Actualizar tus notas personales con ejemplos concretos.

La idea es que este documento sea tu "hoja de referencia" para no perder la visión general mientras estás ejecutando comandos.
