# 🚀 Rutas de Aprendizaje

> Esta plataforma no es un curso lineal: es un **sistema de rutas** para que llegues de donde estás a un perfil profesional empleable. Cada ruta combina teoría mínima, laboratorio reproducible y entregable de portafolio.

---

## Cómo leer las rutas

| Símbolo | Significado |
|---|---|
| 📖 Teoría | Lecturas y conceptos (carpeta `teoria/` o `teoria` del módulo) |
| 🧪 Lab | Práctica guiada o entorno reproducible (carpeta `laboratorios/`) |
| 🛠️ Herramienta | Herramientas que deberás dominar en ese tramo |
| 🎯 Entregable | Resultado publicable para tu portafolio |
| ✅ Checkpoint | Prueba de autoevaluación antes de avanzar |

**Duración:** estimaciones a **1–2 horas diarias**. Ajusta según tu ritmo.

---

## 🟢 Ruta 1 — Fundamentos (sin experiencia previa)

**Duración estimada:** 4–6 semanas
**Objetivo:** entender qué es la ciberseguridad, dominar tu entorno de trabajo y construir los hábitos del profesional (documentar, laborear, automatizar).

### Semana 1–2: Base técnica
- 📖 [¿Qué es la ciberseguridad?](01-CIBERSEGURIDAD/README.md) — dominios, roles y ética
- 📖 Introducción a Linux: terminal, permisos, red básica
- 📖 Introducción a redes: modelo OSI/TCP-IP, direccionamiento, protocolos
- 🧪 Instalar tu laboratorio: VirtualBox/VMware + Kali o Parrot + máquina vulnerable local
- 🛠️ Terminal, `nmap` (básico), navegador con herramientas de desarrollo

### Semana 3–4: Primeras habilidades ofensivas y defensivas
- 📖 [Módulo 01 — Reconocimiento OSINT](01-CIBERSEGURIDAD/01-reconocimiento-osint/README.md)
- 🧪 [Lab 01 — Mapeo de superficie (NovaPay Labs)](01-CIBERSEGURIDAD/01-reconocimiento-osint/laboratorios/lab-01-mapeo-superficie-basico/enunciado.md)
- 📖 Introducción a la defensa: logs, monitoreo y "pensar como adversario"
- 🛠️ `whois`, `theHarvester`, `nslookup/dig`, `nmap`

### Semana 5–6: Cierre y portafolio
- 🧪 Resolver 1–2 CTFs principiantes (TryHackMe / Hack The Box)
- 🎯 **Entregable:** [informe de reconocimiento OSINT](01-CIBERSEGURIDAD/01-reconocimiento-osint/portafolio/TEMPLATE-reporte-osint.md) sobre tu propio lab + primer writeup de CTF
- ✅ **Checkpoint:** explicas en un párrafo qué es un pentest, qué es un SOC y en qué se diferencia atacar de defender

**Certificaciones sugeridas:** CompTIA Security+ (a futuro) · eJPT (después de la Ruta 2)

---

## 🔴 Ruta 2 — Red Team / Seguridad Ofensiva

**Duración estimada:** 3–4 meses
**Prerrequisitos:** Ruta 1 o conocimientos equivalentes de Linux y redes.
**Objetivo:** ejecutar el ciclo completo de un pentest siguiendo PTES, de forma legal y profesional.

### Fase A (Semana 1–3): Reconocimiento y análisis
- 📖 [Metodología PTES](01-CIBERSEGURIDAD/02-pentesting-red-team/teoria/01-metodologia-ptes.md)
- 📖 [Pentest vs Red Team](01-CIBERSEGURIDAD/02-pentesting-red-team/teoria/01-metodologia-pentest-vs-red-team.md)
- 📖 [Módulo 01 — Reconocimiento OSINT](01-CIBERSEGURIDAD/01-reconocimiento-osint/README.md) (profundización)
- 📖 [Módulo 03 — Análisis de Vulnerabilidades](01-CIBERSEGURIDAD/03-analisis-vulnerabilidades/README.md)
- 🧪 Escaneo y enumeración sobre tu lab local
- 🛠️ `nmap` (+NSE), `nuclei`, `gobuster/ffuf`, `theHarvester`

### Fase B (Semana 4–7): Explotación
- 📖 [Módulo 04 — Explotación Web (OWASP Top 10)](01-CIBERSEGURIDAD/04-explotacion-web/README.md)
- 📖 [Módulo 07 — Ingeniería Social](01-CIBERSEGURIDAD/07-ingenieria-social/README.md) (fase de acceso)
- 🧪 [Lab 02 — Pentest Web Portal Merchants](02-pentesting-red-team/laboratorios/lab-02-pentest-web-portal-merchants/enunciado.md)
- 🧪 DVWA / WebGoat / PortSwigger Academy (labs gratuitos)
- 🛠️ Burp Suite, `sqlmap`, `ffuf`, `curl`

### Fase C (Semana 8–12): Post-explotación, informes y cierre
- 📖 [Módulo 05 — Post-Explotación](01-CIBERSEGURIDAD/05-post-explotacion/README.md): escalada de privilegios, persistencia, movimiento lateral
- 📖 [Módulo 06 — Forense Digital](01-CIBERSEGURIDAD/06-forense-digital/README.md) (complemento)
- 🧪 Máquinas HTB/THM de nivel fácil–medio
- 🎯 **Entregable:** [informe de pentest completo](01-CIBERSEGURIDAD/02-pentesting-red-team/portafolio/TEMPLATE-reporte-pentest.md) (7 fases PTES, CVSS, remediación) sobre tu lab
- ✅ **Checkpoint:** completas el lab 02 de punta a punta sin guía

**Certificaciones sugeridas:** eJPT → (a futuro) OSCP

---

## 🔵 Ruta 3 — Blue Team / Defensa

**Duración estimada:** 3–4 meses
**Prerrequisitos:** Ruta 1 o conocimientos de sistemas y logs.
**Objetivo:** defender, monitorear y responder como lo haría un analista SOC.

### Fase A (Semana 1–3): Fundamentos defensivos
- 📖 [Módulo 02 — Blue Team y Defensa](02-SEGURIDAD-INFORMACION/02-blue-team-defensa/README.md)
- 📖 [Módulo 03 — SOC Operations](02-SEGURIDAD-INFORMACION/03-soc-operations/README.md)
- 📖 MITRE ATT&CK y MITRE D3FEND como lenguajes comunes
- 🧪 [Lab 01 — Lectura e interpretación de logs SOC](03-blue-team-defensa/01-fundamentos-blue-team-y-soc/laboratorios/lab-01-lectura-interpretacion-logs-soc/enunciado.md)
- 🧪 [Lab 02 — Visualización de logs con herramienta SOC](03-blue-team-defensa/01-fundamentos-blue-team-y-soc/laboratorios/lab-02-visualizacion-logs-herramienta-soc/enunciado.md)

### Fase B (Semana 4–8): SIEM, monitoreo y detección
- 📖 Wazuh: instalación, agentes, reglas y dashboards (en `02-blue-team-defensa/siem-wazuh/`)
- 📖 Reglas SIGMA y YARA
- 🧪 Levantar tu SOC simulado en Docker (Wazuh + agentes de prueba)
- 🛠️ Wazuh, Elastic/OpenSearch, `jq`, Splunk Free (opcional)

### Fase C (Semana 9–12): Respuesta a incidentes y purple
- 📖 [Módulo 03 — Incident Response / Playbooks](02-SEGURIDAD-INFORMACION/03-soc-operations/incident-response/)
- 🧪 [Lab 01 — Purple: Web Login Storm](04-purple-team-colaboracion/laboratorios/lab-01-purple-web-login-storm/enunciado.md)
- 🧪 [Lab 02 — Purple: Rutas Raras](04-purple-team-colaboracion/laboratorios/lab-02-purple-web-rutas-raras/enunciado.md)
- 🎯 **Entregable:** [playbook de respuesta a incidentes](03-blue-team-defensa/portafolio/TEMPLATE-ficha-evento-soc.md) + análisis de un evento simulado con Wazuh
- ✅ **Checkpoint:** detectas un ataque simulado, lo trias y documentas la cadena de eventos

**Certificaciones sugeridas:** CompTIA Security+ → Blue Team Level 1 (BTL1) → (a futuro) GCFA

---

## ⚙️ Ruta 4 — DevSecOps

**Duración estimada:** 2–3 meses
**Prerrequisitos:** saber programar (cualquier lenguaje; Python recomendado) y nociones de CI/CD.
**Objetivo:** integrar seguridad en el ciclo de vida del software.

### Semana 1–2: Fundamentos
- 📖 [Módulo 04 — DevSecOps](02-SEGURIDAD-INFORMACION/04-devsecops/README.md)
- 📖 Docker Security: imágenes, escaneo, hardening de contenedores
- 🧪 Dockerizar una app vulnerable y analizarla
- 🛠️ Docker, `docker scan` / Trivy, GitHub Actions

### Semana 3–5: SAST, DAST y secretos
- 📖 SAST vs DAST: cuándo y cómo usarlos
- 📖 Secret Scanning: por qué los secretos en código son un incidente
- 🧪 Pipeline CI/CD con: escaneo de secretos (gitleaks), SAST (Semgrep/CodeQL) y DAST (ZAP) en un repositorio de prueba
- 🛠️ Gitleaks, Semgrep, OWASP ZAP, GitHub Actions

### Semana 6–8: Cierre
- 🎯 **Entregable:** pipeline DevSecOps completo y documentado (diagrama + repo)
- ✅ **Checkpoint:** demuestras que un secret commit es bloqueado por tu pipeline

**Certificaciones sugeridas:** (ISC)² CCSP (a futuro) · cursos de cloud security en AWS/Azure

---

## 🤖 Ruta 5 — IA Aplicada a Seguridad

**Duración estimada:** 2–3 meses
**Prerrequisitos:** Python básico y haber completado al menos la Ruta 1.
**Objetivo:** usar IA como copiloto y asegurar sistemas basados en IA (MLSecOps).

### Semana 1–2: IA como copiloto
- 📖 [Cómo usar IA como Copiloto](docs/USANDO-IA.md)
- 📖 [Módulo 05 — Automatización Python](03-IA-AGENTES-HERRAMIENTAS/05-automatizacion-python/README.md)
- 🧪 Automatizar una tarea de seguridad (recon, parsing de logs, alertas)
- 🛠️ Python, APIs de LLM (Claude/GPT), scripts

### Semana 3–5: Agentes y pipelines
- 📖 [Módulo 01 — Agentes OSINT](03-IA-AGENTES-HERRAMIENTAS/01-agentes-osint/README.md)
- 📖 [Módulo 02 — Agentes Pentest](03-IA-AGENTES-HERRAMIENTAS/02-agentes-pentest/README.md)
- 🧪 Construir un pipeline OSINT automatizado con múltiples fuentes
- 🛠️ Python, `requests`, integraciones de APIs, reportes automáticos

### Semana 6–8: MLSecOps y Seguridad de LLM
- 📖 [Módulo — MLSecOps y Seguridad de LLM](03-IA-AGENTES-HERRAMIENTAS/03-mlsecops-llm-security/README.md)
- 🧪 Pruebas de seguridad a LLM: prompt injection, jailbreaking básico, exfiltración (entorno controlado)
- 🎯 **Entregable:** post educativo + repo de pruebas LLM + guía de pipeline seguro
- ✅ **Checkpoint:** documentas 3 vectores de ataque a un LLM y sus mitigaciones

**Certificaciones sugeridas:** (a futuro) cursos de AI Security (OWASP Top 10 for LLM, NVIDIA/IBM)

---

## 🧭 Resumen de rutas

| Ruta | Perfil de entrada | Duración | Primer entregable | Salida laboral típica |
|---|---|---|---|---|
| 🟢 Fundamentos | Ninguno | 4–6 semanas | Informe OSINT + writeup CTF | Base para cualquier rol |
| 🔴 Red Team | Linux + redes | 3–4 meses | Informe de pentest | Pentester Jr / Red Team Jr |
| 🔵 Blue Team | Sistemas + logs | 3–4 meses | Playbook IR + análisis SOC | Analista SOC N1 |
| ⚙️ DevSecOps | Programación | 2–3 meses | Pipeline DevSecOps | DevSecOps Jr |
| 🤖 IA Aplicada | Python básico | 2–3 meses | Suite de pruebas LLM | Security AI / MLSecOps Jr |

---

*[← Volver al README](./README.md) · [📋 Ver Módulos](./MODULOS.md) · [🗂️ Construir mi portafolio](./PORTAFOLIO.md)*
