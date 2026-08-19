# 📋 Tabla Completa de Módulos

> Todos los módulos de la plataforma en una sola vista. Ordenados por área y nivel.

---

## Cómo leer esta tabla

| Campo | Significado |
|---|---|
| **Nivel** | 🟢 Básico · 🟡 Intermedio · 🔴 Avanzado |
| **Duración** | Estimación a 1–2 horas/día |
| **Proyecto** | Entregable publicable al finalizar |
| **Carpeta** | Enlace a la carpeta del módulo |

---

## 🔴 Área 1 — Ciberseguridad Ofensiva

| # | Módulo | Nivel | Duración | Proyecto de portafolio | Carpeta |
|---|---|---|---|---|---|
| 1.01 | Reconocimiento OSINT | 🟢 Básico | 1 semana | Script OSINT propio con theHarvester/Photon | [01-reconocimiento-osint](./01-CIBERSEGURIDAD/01-reconocimiento-osint/) |
| 1.02 | Pentesting y Red Team | 🟡 Intermedio | 3 semanas | Reporte de pentest sobre lab propio | [02-pentesting-red-team](./01-CIBERSEGURIDAD/02-pentesting-red-team/) |
| 1.03 | Análisis de Vulnerabilidades | 🟢 Básico | 1 semana | Script de escaneo Nmap/Nuclei automatizado | [03-analisis-vulnerabilidades](./01-CIBERSEGURIDAD/03-analisis-vulnerabilidades/) |
| 1.04 | Explotación Web (OWASP) | 🟡 Intermedio | 2 semanas | Writeup de lab DVWA o WebGoat | [04-explotacion-web](./01-CIBERSEGURIDAD/04-explotacion-web/) |
| 1.05 | Post-Explotación | 🔴 Avanzado | 2 semanas | Writeup HTB/THM con metodología documentada | [05-post-explotacion](./01-CIBERSEGURIDAD/05-post-explotacion/) |
| 1.06 | Forense Digital | 🟡 Intermedio | 1–2 semanas | Análisis e informe forense de imagen de disco | [06-forense-digital](./01-CIBERSEGURIDAD/06-forense-digital/) |
| 1.07 | Ingeniería Social | 🟢 Básico | 1 semana | Campaña de phishing simulado con GoPhish | [07-ingenieria-social](./01-CIBERSEGURIDAD/07-ingenieria-social/) |
| 1.08 | Criptografía aplicada | 🟢 Básico | 1 semana | Script Python de análisis y cracking de hashes | [08-criptografia](./01-CIBERSEGURIDAD/08-criptografia/) |

---

## 🔵 Área 2 — Seguridad Defensiva y GRC

| # | Módulo | Nivel | Duración | Proyecto de portafolio | Carpeta |
|---|---|---|---|---|---|
| 2.01 | Gestión de Riesgos | 🟢 Básico | 1–2 semanas | Matriz de riesgo de organización ficticia | [01-gestion-riesgos](./02-SEGURIDAD-INFORMACION/01-gestion-riesgos/) |
| 2.02 | Blue Team y Defensa | 🟡 Intermedio | 3 semanas | Reglas SIGMA/YARA y entorno Wazuh en Docker | [02-blue-team-defensa](./02-SEGURIDAD-INFORMACION/02-blue-team-defensa/) |
| 2.03 | SOC Operations | 🟡 Intermedio | 2 semanas | Playbook de respuesta a incidente (ransomware/phishing) | [03-soc-operations](./02-SEGURIDAD-INFORMACION/03-soc-operations/) |
| 2.04 | DevSecOps | 🔴 Avanzado | 3–4 semanas | Pipeline CI/CD con secret scanning + SAST + DAST | [04-devsecops](./02-SEGURIDAD-INFORMACION/04-devsecops/) |
| 2.05 | Hardening | 🟢 Básico | 1 semana | Script de hardening Linux (CIS Benchmarks) publicado | [05-hardening](./02-SEGURIDAD-INFORMACION/05-hardening/) |
| 2.06 | Compliance y Normativas | 🟡 Intermedio | 1–2 semanas | Checklist de cumplimiento GDPR / Ley 1581 CO | [06-compliance-normativas](./02-SEGURIDAD-INFORMACION/06-compliance-normativas/) |
| 2.07 | Threat Intelligence | 🔴 Avanzado | 2–3 semanas | Análisis de campaña APT con ATT&CK Navigator | [07-threat-intelligence](./02-SEGURIDAD-INFORMACION/07-threat-intelligence/) |

---

## 🤖 Área 3 — IA Aplicada a Seguridad

| # | Módulo | Nivel | Duración | Proyecto de portafolio | Carpeta |
|---|---|---|---|---|---|
| 3.01 | Agentes OSINT | 🟡 Intermedio | 2 semanas | Pipeline OSINT automatizado con múltiples fuentes | [01-agentes-osint](./03-AI-AGENTS-TOOLS/01-agentes-osint/) |
| 3.02 | Agentes Pentest | 🔴 Avanzado | 2–3 semanas | Agente que orquesta recon + análisis + reporte | [02-agentes-pentest](./03-AI-AGENTS-TOOLS/02-agentes-pentest/) |
| 3.03 | LLM Security | 🟡 Intermedio | 1–2 semanas | Reporte de auditoría de sistema basado en LLM | [03-llm-security](./03-AI-AGENTS-TOOLS/03-llm-security/) |
| 3.04 | Herramientas Trending | 🟢 Básico | 1 semana | Comparativa de herramientas IA para seguridad | [04-herramientas-trending](./03-AI-AGENTS-TOOLS/04-herramientas-trending/) |
| 3.05 | Automatización Python | 🟢 Básico | 1–2 semanas | Bot de alertas de seguridad en Telegram/Discord | [05-automatizacion-python](./03-AI-AGENTS-TOOLS/05-automatizacion-python/) |

---

## 🧪 Laboratorios

| # | Lab | Tipo | Nivel | Prerrequisitos |
|---|---|---|---|---|
| L.01 | Máquinas HTB / THM | Plataforma externa | 🟡–🔴 | Módulos 1.01–1.04 |
| L.02 | CTF Writeups | Resolución + documentación | 🟢–🔴 | Cualquier módulo |
| L.03 | Labs propios Docker | Entorno vulnerable local | 🟢–🟡 | Docker instalado |
| L.04 | Docker Compose Labs | Reproducible completo | 🟢–🔴 | Docker + módulo relacionado |

---

## 📚 Recursos de referencia

| Recurso | Nivel | Uso |
|---|---|---|
| Cheatsheets | Todos | Referencia rápida durante operaciones |
| Rutas de certificación | Todos | Planificación de carrera y exámenes |
| Notas de libros técnicos | Intermedio+ | Profundización teórica |
| Cursos recomendados | Todos | Complemento a los módulos |

---

## 📊 Estadísticas del currículum

| Área | Módulos | Proyectos de portafolio | Niveles |
|---|---|---|---|
| Ofensiva (Área 1) | 8 | 8 | Básico a Avanzado |
| Defensiva / GRC (Área 2) | 7 | 7 | Básico a Avanzado |
| IA Aplicada (Área 3) | 5 | 5 | Básico a Avanzado |
| Laboratorios | 4 tipos | Ilimitados | Todos |
| **Total** | **24 módulos** | **20+ proyectos** | **Todos los niveles** |

---

*[← Volver al README](./README.md) · [🗺️ Ver Rutas](./RUTAS.md) · [🗂️ Construir mi portafolio](./PORTAFOLIO.md)*
