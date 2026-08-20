# 01 — ¿Qué es la ciberseguridad?

## Definición corta

La **ciberseguridad** es la práctica de proteger sistemas, redes, programas, dispositivos y datos de ataques, daños o accesos no autorizados. Es una disciplina técnica **y** organizativa: la tecnología sola no basta, también importan las personas y los procesos.

## ¿Por qué importa?

Cualquier cosa conectada a internet — desde un smartwatch hasta una planta industrial — es un objetivo potencial. Los atacantes buscan:

- 💰 Dinero (ransomware, robo de tarjetas, fraude)
- 🕵️ Espionaje (estatal o corporativo)
- 🎭 Venganza o activismo (hacktivismo)
- 🎮 Diversión o fama (script kiddies, CTF)
- 🧠 Reto intelectual (los hay éticos y los hay no)

**En el otro lado**, los profesionales de defensa ganan sueldos competitivos, hay mucha demanda global y el trabajo tiene impacto directo en la vida real (un hospital que cae por ransomware es un paciente que no recibe su tratamiento).

## Los grandes equipos (los 3 "teams")

| Equipo | Mentalidad | Una frase que los define |
|---|---|---|
| 🔴 **Red Team** (ofensivo) | "Piensa como el atacante" | "Si rompo esto, ¿qué tan grave es?" |
| 🔵 **Blue Team** (defensivo) | "Piensa como el defensor" | "¿Cómo detecto esto a tiempo?" |
| 🟣 **Purple Team** (colaboración) | "Ambos juntos, mejor" | "¿Cómo aprendemos los unos de los otros?" |

> 💡 Hay un cuarto equipo creciente: ⚪ **AI Security / ML Security** — protege modelos de IA, mitiga prompt injection, evalúa riesgos de los nuevos LLMs.

## Roles profesionales comunes

Cada equipo tiene roles especializados. Aquí un mapa rápido (este repo tiene una carpeta dedicada a cada uno en `01-CIBERSEGURIDAD/`):

### 🔴 Ofensivos (Red Team)
- **Pentester** — busca vulnerabilidades en sistemas autorizados
- **Red Teamer** — simula adversarios reales en ejercicios prolongados
- **Bug Bounty Hunter** — trabaja por recompensas públicas
- **Exploit Developer** — escribe código que aprovecha vulnerabilidades

### 🔵 Defensivos (Blue Team)
- **Analista SOC** — vigila alertas 24/7 en un centro de operaciones
- **Threat Hunter** — busca atacantes que ya están dentro
- **Incident Responder** — actúa cuando algo se rompe
- **Threat Intelligence Analyst** — estudia quién atacaría y cómo
- **Malware Analyst** — desarma software malicioso para entenderlo

### 🟣 GRC (Gobernanza, Riesgo, Cumplimiento)
- **CISO** — el máximo responsable de seguridad en una organización
- **Risk Manager** — cuantifica y prioriza riesgos
- **Auditor de seguridad** — verifica que se cumplen normas (ISO 27001, NIST, PCI-DSS)
- **Data Protection Officer (DPO)** — vela por la privacidad (GDPR, leyes locales)
- **GRC Analyst** — une los tres anteriores

### 🤖 Seguridad de IA
- **AI Red Teamer** — ataca modelos con prompt injection, jailbreaks, etc.
- **ML Security Engineer** — protege pipelines de entrenamiento
- **AI Governance Officer** — define políticas de uso de IA

### Otros roles útiles
- **Arquitecto de seguridad** — diseña cómo se construye un sistema seguro
- **Forense digital** — investiga después de un incidente
- **DevSecOps** — integra seguridad en el ciclo de desarrollo
- **Cryptographer / Criptoanalista** — diseña o rompe criptografía

## Las 6 "categorías" de ataque más conocidas (la CIA Triad ampliada)

Para empezar a hablar el idioma, hay una mnemotecnia clásica:

- **C**onfidencialidad — solo quien debe ve la información
- **I**ntegridad — la información no se alteró sin permiso
- **A**uthentication / Availability — quién eres / que el sistema funcione cuando toca

Pero en la práctica los atacantes hacen cosas como:

1. 🦠 **Malware** — virus, gusanos, troyanos, ransomware
2. 🎣 **Phishing** — ingeniería social por email/mensaje
3. 🔑 **Robo de credenciales** — bases de datos filtradas, keyloggers
4. 💣 **Explotación de vulnerabilidades** — bugs en software sin parchear
5. 🌊 **DDoS** — tumbar un servicio saturándolo
6. 🕵️ **Insider threat** — el atacante está dentro de la organización

## ¿Qué necesitas para entrar?

- **Curiosidad** (no se enseña, se tiene o se desarrolla)
- **Ganas de leer documentación** (el 80% del trabajo es leer)
- **Paciencia para practicar en labs** (teoría sin práctica es inútil)
- **Ética firme** — esto es lo que separa al profesional del criminal

No necesitas:
- Un título específico (hay caminos autodidactas)
- Ser un genio de las matemáticas (es útil pero no esencial)
- Haber nacido sabiendo (nadie nació sabiendo)

## 📌 Dónde profundizar en este repo

| Tema | Carpeta |
|---|---|
| Red Team general | [`02-pentesting-red-team/`](../02-pentesting-red-team/), [`01-CIBERSEGURIDAD/02-pentesting-red-team/`](../01-CIBERSEGURIDAD/02-pentesting-red-team/) |
| Blue Team general | [`03-blue-team-defensa/`](../03-blue-team-defensa/), [`02-SEGURIDAD-INFORMACION/02-blue-team-defensa/`](../02-SEGURIDAD-INFORMACION/02-blue-team-defensa/) |
| Seguridad de IA | [`03-IA-AGENTES-HERRAMIENTAS/`](../03-IA-AGENTES-HERRAMIENTAS/) |
| Roles profesionales | [`01-CIBERSEGURIDAD/`](../01-CIBERSEGURIDAD/) (37 subcarpetas) |
| Labs para practicar | [`04-LABORATORIOS/`](../04-LABORATORIOS/) |
| Certificaciones recomendadas | [`05-RECURSOS/certificaciones/`](../05-RECURSOS/certificaciones/) |

## ✏️ Ejercicio para ti

1. Escoge **uno** de los equipos (Red / Blue / Purple / AI).
2. Escribe en tu libreta: ¿qué hace una persona en ese equipo un lunes cualquiera?
3. Busca en [`01-CIBERSEGURIDAD/`](../01-CIBERSEGURIDAD/) una subcarpeta que se llame como un rol de ese equipo.
4. Léela y compara con lo que tú escribiste.

> ⏭️ **Siguiente:** [`02-glosario.md`](./02-glosario.md) — los términos que verás en todos los archivos de este repo.
