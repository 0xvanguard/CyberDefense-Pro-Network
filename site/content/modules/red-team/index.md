---
title: Área 1 — Ciberseguridad Ofensiva y Base Purple
description: Área 1 — Ciberseguridad Ofensiva y Base Purple
---

> 🚀 **¿Eres principiante?** Antes de este módulo, revisa la **[base común del repo](../fundamentos/)** (1 carpeta atrás). Ahí están los conceptos que necesitas para que esto te haga sentido.
>
> Elige tu ruta de aprendizaje: 🛡️ [Defensor](../fundamentos/rutas/ruta-defensor.md) · ⚔️ [Atacante](../fundamentos/rutas/ruta-atacante.md) · 🤖 [AI Security](../fundamentos/rutas/ruta-ai-security.md)

# 🔴 Área 1 — Ciberseguridad Ofensiva y Base Purple

> **Misión de el área:** Formarte en los fundamentos técnicos de la ciberseguridad ofensiva (hacking ético) y darte la base práctica que luego alimenta rutas Purple Team, Blue Team y DevSecOps.

Aquí se aprende **a pensar como atacante para defender mejor**. Es la columna vertebral técnica de la plataforma.

---

## 🎯 Objetivos formativos

Al completar los módulos clave de esta área deberías ser capaz de:

- Entender y aplicar el **ciclo completo de un pentest**: reconocimiento, enumeración, explotación, post-explotación y reporte.
- Usar herramientas ofensivas estándar (Nmap, Gobuster, Burp, etc.) con criterio, no solo como "listas de comandos".
- Analizar vulnerabilidades y priorizarlas según impacto real.
- Documentar tus hallazgos de forma profesional (informes claros, reproducibles y útiles para equipos técnicos y de negocio).
- Conectar la visión ofensiva con la defensa (base para Purple Team).

---

## 🧱 Áreas clave de el Área 1

Los módulos de esta área se organizan alrededor de estas áreas:

- **Reconocimiento y OSINT técnico**
  - Identificación de objetivos, rangos, dominios, tecnologías visibles.
  - Uso de herramientas de escaneo y recolección de información.

- **Análisis de vulnerabilidades**
  - Interpretar resultados de escáneres.
  - Entender CWE, CVE, CVSS a nivel práctico.

- **Explotación Web y de Servicios**
  - Ataques a aplicaciones web (inyecciones, auth, sesiones, etc.).
  - Explotación de servicios típicos (FTP, SSH, SMB, etc.) en entornos de laboratorio.

- **Post-explotación y movimiento lateral**
  - Enumeración interna tras lograr acceso.
  - Escalada de privilegios en sistemas Windows/Linux.

- **Forense básico y registro de evidencias**
  - Captura y preservación de evidencias en labs.
  - Uso básico de herramientas forenses para entender qué pasó.

- **Purple Team Base**
  - Traducir técnicas ofensivas a detecciones y controles defensivos.
  - Mapear ataques a marcos como MITRE ATT&CK.

---

## 🗺️ Mapa de subdominios

| # | Subdominio | Fase Kill Chain | Tácticas MITRE |
|---|---|---|---|
| 01 | [Reconocimiento OSINT](./01-reconocimiento-osint/) | Reconnaissance | TA0043 |
| 02 | [Pentesting / Red Team](./02-pentesting-red-team/) | Múltiples | TA0001-TA0011 |
| 03 | [Análisis de Vulnerabilidades](./03-analisis-vulnerabilidades/) | Weaponization | TA0042 |
| 04 | [Explotación Web](./04-explotacion-web/) | Exploitation | TA0001 |
| 05 | [Post-Explotación](./05-post-explotacion/) | Actions on Objectives | TA0003-TA0008 |
| 06 | [Forense Digital](./06-forense-digital/) | Análisis | — |
| 07 | [Ingeniería Social](./07-ingenieria-social/) | Initial Access | TA0001 |
| 08 | [Criptografía](./08-criptografia/) | Transversal | — |

---

## 🗂 Estructura tipo de cada módulo

```text
NN-nombre/
├── herramientas/      ← Una carpeta por herramienta + README con uso
├── tecnicas/          ← Procedimientos paso a paso
├── laboratorios/      ← Labs reproducibles (Docker / Vagrant / HTB/THM)
└── README.md          ← Índice del módulo
```

Cada módulo usará `TEMPLATE-MODULO.md` como base: objetivos, teoría mínima, práctica guiada, evidencia y entregables de portafolio.

---

## 👤 Perfiles que se forman en esta área

Esta área sirve de base para varios roles:

- **Hacker ético / Pentester junior**
  - Foco en reconocer, explotar y documentar vulnerabilidades en entornos controlados.

- **Analista de seguridad / Blue Team junior**
  - Usa la visión ofensiva para entender mejor qué detectar y cómo responder.

- **Purple Teamer**
  - Conecta ataques con detecciones y mejoras de controles.

- **Futuro DevSecOps / ML-Security Engineer**
  - Necesita entender qué vulnerabilidades existen en la práctica antes de automatizar o asegurar pipelines.

Más adelante se podrán definir roles específicos (por ejemplo, "Red Team Operator", "Purple Team Engineer") igual que se hizo con `prompt-engineer-security` en Área 3.

---

## 🔗 Relación con otras áreaes

- **Área 2 – Seguridad de la Información y Defensa (`02-SEGURIDAD-INFORMACION/`)**
  - Toma las técnicas ofensivas vistas aquí y las aterriza en monitoreo, respuesta a incidentes, gestión de riesgos y cumplimiento.

- **Área 3 – IA, Agentes y Automatización (`03-IA-AGENTES-HERRAMIENTAS/`)**
  - Usa lo aprendido aquí como base para crear agentes de OSINT/pentest y automatizaciones con IA.

- **Área 4 – Laboratorios (`04-LABORATORIOS/`)**
  - Muchos labs de CTF, HTB, THM y labs propios estarán alineados con estos módulos.

---

## 📌 Ruta sugerida dentro de el Área 1

Un camino recomendado para avanzar en esta área:

1. **`01-reconocimiento-osint/`**
   - Fundamentos de reconocimiento y OSINT técnico sin IA.
   - Uso de Nmap, whois, DNS, escaneos básicos.

2. **`02-pentesting-red-team/`**
   - Ciclo completo de pentest sobre máquinas de laboratorio.

3. **`03-analisis-vulnerabilidades/`**
   - Interpretar resultados de escáneres, priorizar findings y entender CWE/CVE.

4. **`04-explotacion-web/` y `05-post-explotacion/`**
   - Hacking web + movimiento lateral y escalada de privilegios.

5. **`06-forense-digital/` y `07-ingenieria-social/`**
   - Entender el impacto de ataques y la capa humana.

6. **`08-criptografia/`**
   - Base de cifrado, hashing, PKI y errores comunes en su implementación.

---

## 📂 Entregables típicos de esta área

En los módulos de esta área es común que generes:

- Informes de recon y pentest en Markdown/PDF.
- Writeups de máquinas CTF (paso a paso, reproducibles).
- Scripts simples (bash/Python) para automatizar pequeños pasos.
- Notas y cheatsheets de comandos y técnicas.

Todos estos se conectarán luego con `PORTAFOLIO.md` para que construyas una historia coherente de tu progreso ofensivo.

---

<div align="center">

**[⬅ Volver al README principal](../README.md)** · **[🔵 Ir a Defensiva →](../02-SEGURIDAD-INFORMACION/)**

</div>
