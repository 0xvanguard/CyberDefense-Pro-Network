<div align="center">

# 🗺️ ROADMAP — cyber-arsenal

**Plan de estudio personalizado · John Sebastian Camargo (@0xvanguard)**

*De Técnico en Sistemas a Red Team / DevSecOps Engineer*

[![Fase actual](https://img.shields.io/badge/fase%20actual-1%20%C2%B7%20Base%20activa-yellow)](#fase-1--base-activa-ahora-mismo)
[![Horizonte](https://img.shields.io/badge/horizonte-12%20meses-blue)](#timeline-global)
[![Objetivo final](https://img.shields.io/badge/objetivo-OSCP-red)](#fase-4--devsecops--ia-6-12-meses)

</div>

---

## 🎯 Visión

Convertir este repositorio en mi **portafolio técnico verificable** mientras evoluciono de:

```
Técnico en Sistemas (hoy)
        │
        ▼
Junior Pentester / SOC Analyst (6 meses)
        │
        ▼
Red Team Operator + DevSecOps (12-18 meses)
        │
        ▼
Especialista en Agentic Security (18-24 meses)
```

---

## 📊 Timeline global

```
Mes:    0───1───2───3───4───5───6───7───8───9───10──11──12
        │   │   │   │   │   │   │   │   │   │   │   │   │
Fase 1  ████░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░  ← Base activa
Fase 2  ░░░░██████████░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░  ← Ofensiva (eJPT)
Fase 3  ░░░░░░░░░░░░██████████████░░░░░░░░░░░░░░░░░░░░░░░░  ← Defensiva (Sec+)
Fase 4  ░░░░░░░░░░░░░░░░░░░░░░░░░░██████████████████████░░  ← DevSecOps + IA (OSCP)
```

---

## ✅ Estado actual (snapshot)

| Capacidad | Nivel | Evidencia |
|---|---|---|
| Python | 🟢 Operativo | Scripts propios · automatización |
| Docker | 🟢 Operativo | Compose · contenedores aislados |
| Nmap | 🟡 Intermedio | Scans básicos y NSE selectivo |
| Wazuh | 🟡 Intermedio | Instalación y reglas básicas |
| MITRE ATT&CK | 🟡 Intermedio | Lectura de tácticas / técnicas |
| OSINT | 🟡 Intermedio | Herramientas dispersas, falta sistema |
| Web Pentest | 🔴 Inicial | Conceptos OWASP, sin Burp profundo |
| AD / Red Team | 🔴 Inicial | Pendiente Impacket / BloodHound |
| Reportería | 🔴 Inicial | Pendiente metodología PTES |

---

# Fase 1 — Base activa *(ahora mismo)*

> **Duración estimada:** ya en curso · cierre objetivo en 4 semanas
> **Objetivo:** consolidar fundamentos y dejar el repositorio operativo.

### Logros completados

- [x] Python como lenguaje principal de automatización
- [x] Docker + Docker Compose para entornos aislados
- [x] Nmap básico (host discovery, port scan, service detection)
- [x] Wazuh básico (instalación, agentes, dashboard)
- [x] Técnico en Sistemas finalizado
- [x] Repositorio `cyber-arsenal` creado
- [x] **Arquitectura del knowledge base inicializada** ← *este PR*

### Pendiente Fase 1

- [ ] Certificación **Hacking Social** finalizada *(en curso)*
- [ ] Completar 5 laboratorios de OSINT documentados en `01-CIBERSEGURIDAD/01-reconocimiento-osint/laboratorios/`
- [ ] Documentar el proyecto **Attack-Surface.Validation** dentro del repo
- [ ] Configurar `pre-commit` con TruffleHog + GitLeaks (anti-leak de secretos en commits)
- [ ] Cheatsheet personal de Nmap en `05-RECURSOS/cheatsheets/nmap.md`

### Entregables medibles

| Métrica | Meta |
|---|---|
| Carpetas pobladas con contenido real | ≥ 8 |
| READMEs de subdominios completados | ≥ 5 |
| Labs OSINT documentados | 5 |

---

# Fase 2 — Especialización ofensiva *(1–3 meses)*

> **Duración estimada:** 60–90 días
> **Objetivo:** alcanzar nivel **Junior Pentester** verificable con eJPT.

### Roadmap táctico

- [ ] **TryHackMe path: Jr Penetration Tester** completado al 100%
  - [ ] Network Security
  - [ ] Web Hacking Fundamentals
  - [ ] Burp Suite Basics
  - [ ] Metasploit
- [ ] **Burp Suite** dominado
  - [ ] Proxy + Repeater + Intruder + Decoder
  - [ ] Extensiones: Logger++, Autorize, Param Miner
- [ ] **SQLMap** avanzado
  - [ ] Inyecciones manuales antes de automatizar
  - [ ] Tampers · WAF bypass · DBMS específicos
- [ ] **Metasploit** funcional
  - [ ] msfvenom para payloads
  - [ ] Post-exploitation modules
- [ ] **Active Directory básico**
  - [ ] Impacket (psexec, secretsdump, GetUserSPNs)
  - [ ] BloodHound + SharpHound
- [ ] Primer **CTF documentado** en `04-LABORATORIOS/ctf-writeups/`
- [ ] **5 máquinas HTB/THM** rooteadas y documentadas
- [ ] 🎓 **Certificación: eJPT** (eLearnSecurity Junior Penetration Tester)

### Stack a dominar

```
Burp Suite · SQLMap · FFUF · Gobuster · Nuclei · Metasploit · Impacket · BloodHound
```

### Entregables medibles

| Métrica | Meta |
|---|---|
| Writeups de máquinas | 5 |
| Cheatsheets ofensivos creados | 5 |
| Certificación eJPT | ✅ |

---

# Fase 3 — Defensiva y SOC *(3–6 meses)*

> **Duración estimada:** 90 días posteriores a Fase 2
> **Objetivo:** ser empleable como **SOC Analyst Tier 1/2**.

### Roadmap táctico

- [ ] **Wazuh SIEM avanzado**
  - [ ] Reglas custom (decoders + rules) en YAML/XML
  - [ ] Integración con Suricata / Sysmon
  - [ ] Active Response (bloqueos automáticos)
  - [ ] Dashboards Kibana customizados
- [ ] **MITRE ATT&CK aplicado**
  - [ ] Mapear técnicas a logs reales
  - [ ] Detection-as-Code en `02-SEGURIDAD-INFORMACION/02-blue-team-defensa/`
- [ ] **MITRE D3FEND**
  - [ ] Mapear cada detección a una contramedida
- [ ] **Threat Hunting**
  - [ ] Hipótesis estructuradas (PEAK / TaHiTI)
  - [ ] 3 hunts documentados end-to-end
- [ ] **Incident Response**
  - [ ] 2 playbooks NIST 800-61 (phishing + compromiso de credenciales)
  - [ ] Timeline forense con Velociraptor o KAPE
- [ ] **YARA + Sigma**
  - [ ] 5 reglas YARA propias
  - [ ] 5 reglas Sigma traducidas a Wazuh
- [ ] 🎓 **Certificación: CompTIA Security+** *(o CEH como alternativa)*

### Stack a dominar

```
Wazuh · Suricata · Sigma · YARA · Velociraptor · KAPE · Volatility · MITRE ATT&CK Navigator
```

### Entregables medibles

| Métrica | Meta |
|---|---|
| Playbooks NIST 800-61 | 2 |
| Reglas Sigma + YARA | 10 |
| Threat hunts documentados | 3 |
| Certificación Security+ | ✅ |

---

# Fase 4 — DevSecOps + IA *(6–12 meses)*

> **Duración estimada:** 180 días posteriores a Fase 3
> **Objetivo:** posicionarme como **DevSecOps + Agentic Security Engineer**.

### Roadmap táctico

- [ ] **Pipeline CI/CD seguro propio**
  - [ ] GitHub Actions con TruffleHog + GitLeaks (secret scanning)
  - [ ] Trivy + Grype (vulns en imágenes Docker)
  - [ ] Semgrep / Bandit (SAST Python)
  - [ ] OWASP ZAP (DAST automatizado)
- [ ] **Docker Hardening**
  - [ ] Imágenes distroless / Chainguard
  - [ ] Usuario no-root + read-only filesystem
  - [ ] Cosign para firmar imágenes
- [ ] **Agentes IA — recon automatizado**
  - [ ] Pipeline Python + Anthropic Claude
  - [ ] Estructurar salida de Nmap/Subfinder/Nuclei → LLM → reporte ejecutivo
  - [ ] Confidence scoring + escalado humano si <85%
  - [ ] Notificaciones Telegram/Discord
- [ ] **LLM Security**
  - [ ] OWASP LLM Top 10 estudiado
  - [ ] 3 demos de prompt injection documentadas
  - [ ] AI red teaming: jailbreaks éticos contra modelos propios
- [ ] **OSCP Prep**
  - [ ] HTB Pro Labs (Dante u Offshore)
  - [ ] PG Practice (al menos 30 máquinas)
  - [ ] Buffer overflow manual end-to-end
- [ ] 🎓 **Certificación: OSCP** (objetivo premium)

### Stack a dominar

```
GitHub Actions · TruffleHog · GitLeaks · Trivy · Semgrep · Bandit · ZAP · Cosign
Anthropic API · Ollama · LangGraph (referencia) · Pydantic · structlog
```

### Entregables medibles

| Métrica | Meta |
|---|---|
| Pipeline CI/CD seguro funcional | ✅ |
| Agente IA de recon operativo | ✅ |
| Demos de LLM security | 3 |
| Máquinas OSCP-style rooteadas | ≥ 30 |
| Certificación OSCP | 🎯 objetivo |

---

## 📈 KPIs personales

Métricas que reviso cada **lunes**:

| KPI | Frecuencia | Meta semanal |
|---|---|---|
| Commits al repo | semanal | ≥ 5 |
| Máquinas/CTFs resueltos | semanal | ≥ 1 |
| Cheatsheets nuevos | mensual | ≥ 2 |
| Horas de estudio activo | semanal | ≥ 10h |
| Reglas defensivas creadas | mensual | ≥ 3 |

---

## 🧠 Filosofía de aprendizaje

1. **Documentar antes de avanzar** — si no lo escribiste, no lo aprendiste.
2. **Ofensiva ↔ Defensiva siempre juntas** — cada técnica ATT&CK estudia su contramedida D3FEND.
3. **Automatizar cuando lo entiendes manualmente** — primero entender, después scriptear.
4. **Certificación = consecuencia, no objetivo** — el objetivo es el conocimiento; la certificación es el recibo.
5. **Lab > tutorial** — si no lo rompiste y lo arreglaste, no lo entiendes.

---

## 🎓 Mapa de certificaciones

```
                  Hacking Social (en curso)
                          │
                          ▼
                       eJPT (Fase 2)
                       /       \
                      ▼         ▼
                 Security+    CEH      ← elegir uno (Fase 3)
                      \       /
                       ▼     ▼
                       OSCP (Fase 4)  🎯
                          │
                          ▼
              CRTO / OSEP / OSWE     (futuro)
```

---

## 🔄 Revisiones

| Fecha | Cambio | Versión |
|---|---|---|
| 2026-05-28 | Versión inicial del roadmap | v1.0 |

> Este roadmap se revisa al final de cada fase. Cualquier cambio se documenta aquí con un nuevo registro.

---

<div align="center">

**[⬅ Volver al README](./README.md)**

*"Plans are nothing; planning is everything." — Eisenhower*

</div>
