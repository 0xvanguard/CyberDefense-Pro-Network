<div align="center">

# 🚨 Analista SOC

**NIST NICE · Cyber Defense Analyst**

*"El SOC es la sala de cuidados intensivos de la seguridad — y tú eres el primer médico."*

![Tier](https://img.shields.io/badge/tier%20salarial-B-blue) ![Demanda](https://img.shields.io/badge/demanda-muy%20alta-brightgreen) ![Entry](https://img.shields.io/badge/entry%20level-MUY%20amigable-success)

</div>

---

## 📋 Descripción

Rol de **primera línea defensiva** en operaciones de seguridad. Recibe alertas del SIEM/EDR, hace **triage**, escala incidentes y documenta. Es el rol con **más vacantes y menor barrera de entrada** en ciberseguridad — el típico "salto" desde soporte L2/L3 o sysadmin.

Estructura típica en escalones (Tier 1/2/3):
- **Tier 1**: triage, clasificación, escalamiento (turnos 24/7)
- **Tier 2**: investigación profunda, contención, threat hunting básico
- **Tier 3**: caza avanzada, malware analysis, mejora de detecciones

---

## 👤 Roles típicos

- **SOC Analyst Tier 1 / 2 / 3** — escalafón clásico
- **MDR Analyst** — para clientes en modelo managed (Arctic Wolf, Esentire)
- **Cyber Defense Analyst** *(NIST NICE oficial)* — gobierno y enterprise
- **MSSP Analyst** — multi-cliente en MSSPs (NTT, Optiv, IBM)

---

## 🛠️ Stack y herramientas

| Categoría | Herramientas |
|---|---|
| **SIEM** | Splunk · Microsoft Sentinel · QRadar · Elastic SIEM · Wazuh · Sumo Logic · Chronicle |
| **EDR / XDR** | CrowdStrike · SentinelOne · MS Defender for Endpoint · Cortex XDR · Carbon Black |
| **SOAR** | Splunk SOAR (Phantom) · Tines · Cortex XSOAR · Microsoft Sentinel Playbooks · Shuffle |
| **Threat Intel** | MISP · OpenCTI · ThreatConnect · AlienVault OTX · Recorded Future · Mandiant Advantage |
| **Sandbox / análisis** | Any.Run · Hybrid Analysis · Joe Sandbox · VirusTotal · Cuckoo · CAPE |
| **Network / packet** | Wireshark · Zeek · Suricata · Arkime · NetworkMiner |
| **Ticket / case mgmt** | TheHive · Jira Security · ServiceNow IRM · Resilient |
| **Reglas / detection** | Sigma · YARA · KQL (Sentinel) · SPL (Splunk) · AQL (QRadar) |

---

## 🎓 Certificaciones recomendadas

| Nivel | Certificación | Vendor | Costo (USD) | Notas |
|---|---|---|---|---|
| Entry | CompTIA Security+ | CompTIA | ~$400 | Base obligatoria |
| Entry | Microsoft SC-200 | Microsoft | ~$165 | Sentinel + Defender — excelente para arrancar |
| Entry | Blue Team Level 1 (BTL1) | SecurityBlue | ~$500 | Práctica real, MUY recomendado |
| Mid | CompTIA CySA+ | CompTIA | ~$400 | Análisis de comportamiento |
| Mid | GIAC GCIA / GCED | SANS | ~$2,500+ | Premium |
| Mid | Splunk Core Certified User → Power User | Splunk | $0-130 | Si tu SOC usa Splunk |
| Senior | GIAC GCIH (Incident Handler) | SANS | ~$2,500+ | Salto a IR/T3 |
| Senior | Blue Team Level 2 (BTL2) | SecurityBlue | ~$700 | Práctico avanzado |

---

## 🗺️ Roadmap (12 meses)

### Fase 1 — Fundamentos (0-3 meses)
- [ ] Wazuh montado + 3 agentes generando alertas
- [ ] OWASP Top 10 + MITRE ATT&CK Enterprise leídos
- [ ] LetsDefend.io: completar SOC Analyst path
- [ ] Security+ aprobado

### Fase 2 — Especialización (3-6 meses)
- [ ] BTL1 aprobado (laboratorio práctico real)
- [ ] 10 reglas Sigma propias contra ATT&CK Top 10 (T1059, T1078, T1547...)
- [ ] Investigación documentada de 5 alertas (formato 5W+H)
- [ ] SC-200 o CySA+ aprobado

### Fase 3 — Profesional (6-12 meses)
- [ ] Playbook SOAR funcional (Shuffle / Tines free) para phishing
- [ ] Threat hunt documentado con hipótesis (PEAK methodology)
- [ ] Migración mental Tier 1 → Tier 2: investigaciones profundas
- [ ] GCIH o BTL2 empezado

---

## 💰 Salarios en Colombia (USD/mes)

| Nivel | Local 🇨🇴 | Remoto 🌎 | Notas |
|---|---|---|---|
| Tier 1 (0-1 años) | $600 - $1,100 | $1,100 - $2,000 | Turnos 24/7, MSSPs absorben mucho |
| Tier 2 (1-3 años) | $1,400 - $2,500 | $2,500 - $4,500 | BTL1 + Sigma propios = boost |
| Tier 3 (3-6 años) | $3,000 - $5,500 | $5,000 - $8,500 | Detection Engineer especializado top |

> **Tip:** Tier 1 es la **mejor puerta de entrada a ciberseguridad** desde sysadmin/helpdesk. La rotación es alta — usa eso a tu favor.

---

## 🔗 Conexión con otras ramas

- **`incident-responder`** → escalas hacia ahí en Tier 3
- **`threat-hunter`** → evolución natural desde Tier 2/3
- **`seguridad-endpoint`** → 60% de tus alertas vienen de EDR
- **`threat-intelligence`** → te alimenta con IOCs y TTPs
- **`forense-digital`** → handoff cuando un caso requiere evidencia forense

---

## 📂 Estructura

```
analista-soc/
├── herramientas/    # Configs Wazuh, Splunk searches, Sentinel KQL
├── recursos/        # ATT&CK navigator layers, playbooks, templates
├── laboratorios/    # LetsDefend writeups, Wazuh + Sysmon
└── casos-uso/       # Phishing IR, lateral movement detection, etc.
```

---

<div align="center">

**[⬅ Volver a Ciberseguridad](../README.md)**

</div>
