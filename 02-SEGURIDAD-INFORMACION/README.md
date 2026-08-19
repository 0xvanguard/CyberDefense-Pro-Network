<div align="center">

# 🔵 02 — SEGURIDAD DE LA INFORMACIÓN

**Defensiva · SOC · Blue Team · DevSecOps · GRC**

*"La detección sin respuesta es solo telemetría cara."*

</div>

---

## 🎯 Propósito

Esta sección agrupa todo el conocimiento defensivo, de operaciones de seguridad (SOC), DevSecOps, hardening, cumplimiento normativo y threat intelligence. Cada subdominio se mapea explícitamente a los marcos **NIST CSF 2.0**, **ISO 27001:2022** y **MITRE D3FEND**.

---

## 🗺️ Mapa de subdominios

| # | Subdominio | NIST CSF Function | ISO 27001 Anexo A |
|---|---|---|---|
| 01 | [Gestión de Riesgos](./01-gestion-riesgos/) | Govern · Identify | A.5 |
| 02 | [Blue Team / Defensa](./02-blue-team-defensa/) | Detect · Respond | A.8.16 |
| 03 | [SOC Operations](./03-soc-operations/) | Detect · Respond | A.5.24-29 |
| 04 | [DevSecOps](./04-devsecops/) | Protect | A.8.25-34 |
| 05 | [Hardening](./05-hardening/) | Protect | A.8.9-19 |
| 06 | [Compliance / Normativas](./06-compliance-normativas/) | Govern | A.5.31-36 |
| 07 | [Threat Intelligence](./07-threat-intelligence/) | Identify · Detect | A.5.7 |

---

## 📋 01 — Gestión de Riesgos

> **Objetivo:** identificar, evaluar y tratar riesgos de seguridad de manera sistemática.

**Frameworks:**
- **ISO/IEC 27001:2022** — SGSI (Sistema de Gestión de Seguridad de la Información)
- **ISO/IEC 27005:2022** — gestión de riesgos específica
- **NIST RMF (SP 800-37)** — Risk Management Framework
- **NIST SP 800-30** — guía de evaluación de riesgos
- **OCTAVE Allegro** — alternativa cualitativa

**Entregables esperados:**
- Matrices de riesgo (probabilidad × impacto)
- Plantillas de declaración de aplicabilidad (SoA)
- Plan de tratamiento de riesgos (RTP)

📁 [`./01-gestion-riesgos/`](./01-gestion-riesgos/)

---

## 🛡️ 02 — Blue Team / Defensa

> **Objetivo:** detectar, contener y erradicar amenazas en tiempo real.

**Stack defensivo:**
- 🔵 **Wazuh** — SIEM + XDR open source *(stack principal)*
- 🦁 **Suricata** — IDS/IPS de red
- 🦌 **Sigma** — formato vendor-agnostic de reglas de detección
- 🐍 **YARA** — pattern matching para malware
- 📡 **Sysmon** — telemetría avanzada en Windows

**Subcarpetas:**
- `siem-wazuh/` — instalación, decoders, reglas custom, integraciones
- `threat-hunting/` — hipótesis estructuradas (PEAK, TaHiTI, MaGMA)
- `herramientas/` — Wazuh · Suricata · YARA · Velociraptor
- `mitre-d3fend/` — contramedidas defensivas mapeadas a ATT&CK

**Detection Engineering:**
- Detection-as-Code en Git (reglas versionadas)
- CI/CD para validar reglas con datasets sintéticos (Atomic Red Team, Mordor)

📁 [`./02-blue-team-defensa/`](./02-blue-team-defensa/)

---

## 🚨 03 — SOC Operations

> **Objetivo:** operar un Security Operations Center con procesos repetibles.

**Estructura típica de un SOC:**
- **Tier 1** — triage de alertas, escalado
- **Tier 2** — investigación profunda, contención
- **Tier 3** — threat hunting, forense, malware analysis
- **SOC Manager** — métricas, mejora continua

**Carpetas:**
| Carpeta | Contenido |
|---|---|
| `playbooks/` | Procedimientos paso a paso (basados en NIST 800-61) |
| `incident-response/` | Casos reales documentados (anonimizados) |
| `alertas-y-dashboards/` | Queries Wazuh / KQL / SPL · paneles Kibana |

**Métricas SOC clave:**
- MTTD (Mean Time To Detect)
- MTTR (Mean Time To Respond)
- Tasa de falsos positivos
- Cobertura MITRE ATT&CK (porcentaje de técnicas detectadas)

📁 [`./03-soc-operations/`](./03-soc-operations/)

---

## ⚙️ 04 — DevSecOps

> **Objetivo:** integrar seguridad en cada fase del SDLC sin frenar la entrega.

**Subcarpetas:**

| Subcarpeta | Stack |
|---|---|
| `ci-cd-security/` | GitHub Actions · GitLab CI · pipeline gates |
| `secret-scanning/` | **TruffleHog** · **GitLeaks** · `detect-secrets` · `gitleaks-pre-commit` |
| `docker-security/` | Trivy · Grype · Dockle · Hadolint · Cosign · distroless |
| `sast-dast/` | Semgrep · Bandit · CodeQL (SAST) · OWASP ZAP · Nuclei (DAST) |

**Principios aplicados:**
- **Shift-left** — seguridad desde el commit, no desde producción
- **Policy-as-Code** — OPA / Kyverno para Kubernetes
- **Supply chain security** — SBOM (CycloneDX) · firma con Cosign · SLSA
- **Least privilege** — non-root containers · read-only FS · capabilities mínimas

**Pipeline de referencia:**
```
commit → secret-scan → SAST → build → SBOM → image-scan → sign → DAST → deploy
```

📁 [`./04-devsecops/`](./04-devsecops/)

---

## 🔒 05 — Hardening

> **Objetivo:** reducir superficie de ataque en sistemas operativos y red.

**Subcarpetas:**

| Subcarpeta | Estándares de referencia |
|---|---|
| `linux/` | CIS Benchmarks · STIG · `Lynis` · `OpenSCAP` |
| `windows/` | CIS Benchmarks · LAPS · BitLocker · AppLocker · Credential Guard |
| `redes/` | Segmentación · firewalls · 802.1X · DNS-sec · port security |

**Herramientas de auditoría:**
- `Lynis` (Linux) · `Microsoft Security Compliance Toolkit` · `CIS-CAT`

📁 [`./05-hardening/`](./05-hardening/)

---

## 📜 06 — Compliance y Normativas

> **Objetivo:** mapear controles técnicos a requisitos legales y regulatorios.

**Subcarpetas:**

| Subcarpeta | Marco |
|---|---|
| `gdpr/` | Reglamento (UE) 2016/679 — Protección de datos UE |
| `iso-27001/` | ISO/IEC 27001:2022 + Anexo A (93 controles) |
| `colombia-ley-1581/` | Ley 1581 de 2012 + Decreto 1377/2013 — Habeas Data 🇨🇴 |

**Otros marcos referenciados:**
- **NIST CSF 2.0** · **CIS Controls v8** · **PCI-DSS v4.0** · **HIPAA** · **SOC 2**

📁 [`./06-compliance-normativas/`](./06-compliance-normativas/)

---

## 🕵️ 07 — Threat Intelligence

> **Objetivo:** anticipar ataques con inteligencia operativa, táctica y estratégica.

**Subcarpetas:**

| Subcarpeta | Contenido |
|---|---|
| `mitre-attack/` | Matrices: Enterprise · Mobile · ICS · navigator layers propios |
| `feeds/` | Listas de IPs/dominios maliciosos · OSINT feeds (AbuseIPDB, AlienVault OTX) |
| `iocs/` | IOCs versionados (STIX/TAXII · MISP) |

**Niveles de TI:**
- **Estratégica** — ¿quién y por qué? (informes APT)
- **Operativa** — ¿cómo atacan? (TTPs)
- **Táctica** — ¿qué herramientas usan?
- **Técnica** — ¿qué IOCs específicos?

**Plataformas relevantes:**
- **MISP** — Malware Information Sharing Platform
- **OpenCTI** — plataforma open source de CTI
- **TheHive + Cortex** — case management + observable analysis

📁 [`./07-threat-intelligence/`](./07-threat-intelligence/)

---

## 💼 Ramas laborales — Carrera profesional (7 paths)

> Roles de **C-suite, GRC y privacy** que evolucionan desde las áreas de conocimiento de arriba. Cada README tiene descripción, stack, certificaciones, roadmap, salarios Colombia y conexiones.

| Rama | Tier salarial | Mid-USD/mes | Highlight |
|---|---|---|---|
| [`ciso/`](./ciso/) | **S** | $7,500-14,000 | Top jerárquico defensivo · vCISO como variante |
| [`iso-27001-lead-implementer/`](./iso-27001-lead-implementer/) | C/B | $1,500-3,000 | Mayor demanda LATAM 2025-2026 (SaaS pre-sales US/EU) |
| [`data-protection-officer/`](./data-protection-officer/) | A | $2,000-4,000 | CIPP + inglés legal = combo de oro |
| [`auditor-seguridad/`](./auditor-seguridad/) | C/B | $1,500-3,000 | CISA = mejor ROI · Big 4 → industry +50-80% |
| [`risk-manager/`](./risk-manager/) | B/A | $1,800-3,500 | CRISC + Open FAIR + Python = top 5% |
| [`business-continuity-manager/`](./business-continuity-manager/) | C/B | $1,500-3,000 | DORA + NIS2 + CIRCIA empuja demanda |
| [`privacy-engineer/`](./privacy-engineer/) | A | $2,500-5,000 | Combina dev + privacy + cripto · CIPT clave |

> Ver cada README para breakdown completo por nivel (Junior / Mid / Senior · Local / Remoto).

---

## 🔄 Relación con la sección ofensiva

> Cada técnica ofensiva en `01-CIBERSEGURIDAD/` debería tener su contramedida defensiva mapeada aquí.

```
ATT&CK Technique  →  D3FEND Countermeasure  →  Wazuh/Sigma Detection Rule
   (TA0001)              (D3-***)                  (sigma/wazuh-rule.yml)
```

Esto cierra el bucle **Red ↔ Blue** y es la filosofía de **Purple Team**.

---

<div align="center">

**[⬅ Volver al README principal](../README.md)** · **[🤖 Ir a AI Agents →](../03-AI-AGENTS-TOOLS/)**

</div>
