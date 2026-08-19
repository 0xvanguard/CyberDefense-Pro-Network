<div align="center">

# 🛡️ Seguridad Defensiva (Blue Team)

**Emerging 2024-2026 · Modern Blue Team Operations**

*"El blue team de 2026 escribe código, no llena hojas de Excel."*

![Tier](https://img.shields.io/badge/tier%20salarial-B%2FA-orange) ![Demanda](https://img.shields.io/badge/demanda-muy%20alta-brightgreen) ![Entry](https://img.shields.io/badge/entry%20level-amigable-success)

</div>

---

## 📋 Descripción

Rama **paraguas** del blue team moderno — agrega y modela las prácticas defensivas que evolucionan rápido: **Detection-as-Code**, **Detection Engineering**, **Purple Team** continuo, **Adversary Emulation** programática y SOC moderno *engineering-first*.

Diferencia con ramas relacionadas:
- **`analista-soc`** = operación reactiva en consola
- **`threat-hunter`** = búsqueda proactiva en datos
- **`seguridad-defensiva-blue-team`** *(esta)* = **ingeniería + estrategia** de la defensa como producto

Es donde convergen: SOC + Threat Hunting + Detection Engineering + Purple Team.

---

## 👤 Roles típicos

- **Blue Team Lead** — coordinación SOC + hunting + DE
- **Detection Engineer** — reglas como código (Sigma, KQL, SPL)
- **Purple Team Engineer** — emulación + medición de detección
- **SOC Engineer / SOC Architect** — diseño y mejora del SOC
- **Defense-as-Code Engineer** — IaC + GitOps para detecciones
- **Cyber Defense Manager** — métricas, ATT&CK coverage, playbooks

---

## 🛠️ Stack y herramientas

| Categoría | Herramientas |
|---|---|
| **Detection-as-Code** | Sigma · Splunk Content Pack · Sentinel + GitHub · Detection.gg |
| **SIEM** | Splunk · Sentinel · Elastic SIEM · Wazuh · Chronicle · Sumo |
| **EDR / XDR** | CrowdStrike · SentinelOne · Defender for Endpoint · Cortex XDR |
| **SOAR** | Tines · Shuffle · Splunk SOAR · Cortex XSOAR · n8n |
| **Adversary emulation** | Atomic Red Team · CALDERA · Stratus Red Team · APTSimulator |
| **Coverage tools** | MITRE ATT&CK Navigator · DeTT&CT · Vectr · AttackIQ · SCYTHE |
| **Hunting** | Velociraptor · osquery · Sysmon · Zeek · ETW |
| **Frameworks** | MITRE ATT&CK · D3FEND · NIST CSF · SOC-CMM |
| **Orchestration** | GitHub Actions (CI for detections) · Terraform · Ansible |

---

## 🎓 Certificaciones recomendadas

| Nivel | Certificación | Vendor | Costo (USD) | Notas |
|---|---|---|---|---|
| Entry | Microsoft SC-200 | Microsoft | ~$165 | Sentinel + Defender |
| Entry | Blue Team Level 1 (BTL1) | SecurityBlue | ~$500 | Práctica real |
| Mid | Blue Team Level 2 (BTL2) | SecurityBlue | ~$700 | Avanzado |
| Mid | GIAC GCDA / GCIA | SANS | ~$2,500+ | Estándar industria |
| Mid | Splunk Certified Power User → Architect | Splunk | $0-200 | Si tu stack es Splunk |
| Senior | GIAC GCIH + GCFA | SANS | ~$5,000 | DFIR ready |
| Senior | CISSP | (ISC)² | ~$750 | Para mando |

---

## 🗺️ Roadmap (12 meses)

### Fase 1 — Fundamentos (0-3 meses)
- [ ] MITRE ATT&CK Enterprise: top 50 técnicas con sub-techniques
- [ ] D3FEND mapping a tus detecciones actuales
- [ ] Wazuh + Sysmon + Zeek operando en lab
- [ ] BTL1 o SC-200 aprobado

### Fase 2 — Detection Engineering (3-6 meses)
- [ ] 15 reglas Sigma propias contra ATT&CK Top 20
- [ ] Pipeline GitHub Actions: Sigma → SPL/KQL/Wazuh + tests
- [ ] DeTT&CT layer: cobertura ATT&CK actual + gaps
- [ ] BTL2 empezado

### Fase 3 — Profesional (6-12 meses)
- [ ] Purple team exercise documentado: red ataca → blue detecta → mejora
- [ ] CALDERA o Atomic Red Team automatizado vs lab
- [ ] SOC maturity assessment con SOC-CMM
- [ ] GCDA o BTL2 aprobado

---

## 💰 Salarios en Colombia (USD/mes)

| Nivel | Local 🇨🇴 | Remoto 🌎 | Notas |
|---|---|---|---|
| Junior (0-2 años) | $800 - $1,500 | $1,500 - $2,800 | Detection eng entry-level |
| Mid (2-5 años) | $2,000 - $4,000 | $3,800 - $7,000 | Sigma rules en GitHub = palanca |
| Senior (5+ años) | $5,000 - $9,500 | $8,500 - $14,000 | Blue team lead remoto top |

> **Tip:** publicar reglas Sigma propias + writeups de purple team en GitHub es **el portafolio decisivo** del blue team moderno.

---

## 🔗 Conexión con otras ramas

- **`analista-soc`** → operación que tú diseñas
- **`threat-hunter`** → input para nuevas detecciones
- **`incident-responder`** → tus detecciones disparan su trabajo
- **`pentester-red-team`** → contraparte; juntos hacen purple
- **`security-engineer`** → detection-as-code + automation
- **`02-SEGURIDAD-INFORMACION/02-blue-team-defensa`** → área de conocimiento detrás

---

## 📂 Estructura

```
seguridad-defensiva-blue-team/
├── herramientas/    # Sigma rules, KQL queries, SOAR playbooks
├── recursos/        # ATT&CK layers, D3FEND mapping, SOC-CMM
├── laboratorios/    # Wazuh + Sysmon + Atomic + CALDERA full stack
└── casos-uso/       # Purple team writeups, post-mortems, métricas
```

---

<div align="center">

**[⬅ Volver a Ciberseguridad](../README.md)**

</div>
