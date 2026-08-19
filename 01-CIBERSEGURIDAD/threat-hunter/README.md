<div align="center">

# 🎯 Threat Hunter

**NIST NICE · Cyber Defense Analyst (Advanced)**

*"Asume la brecha. Búscala. Documenta lo que el SIEM no vio."*

![Tier](https://img.shields.io/badge/tier%20salarial-A-orange) ![Demanda](https://img.shields.io/badge/demanda-alta-green) ![Entry](https://img.shields.io/badge/entry%20level-medio--alto-yellow)

</div>

---

## 📋 Descripción

Rol **proactivo** de defensa: parte de la hipótesis de que **el adversario ya está dentro** y no genera alertas. Su trabajo es buscar evidencias de TTPs avanzados (lateralización sigilosa, persistencia atípica, exfiltración baja-y-lenta) usando datos masivos del SIEM, EDR, NetFlow y logs cloud.

Diferencia con SOC analyst: SOC reacciona a alertas, hunter **genera la próxima alerta** que el SOC verá. Es un evolutivo natural desde Tier 2/3 SOC + curiosidad ofensiva.

---

## 👤 Roles típicos

- **Threat Hunter** — full-time hunting con metodología estructurada
- **Detection Engineer** — overlap fuerte; convierte hunts en reglas
- **Cyber Defense Forensics Analyst** *(NIST NICE)* — hybrid hunt+forensics
- **Purple Team Member** — colaboración red+blue
- **Senior SOC Analyst** *(Tier 3)* — hunting como parte del rol

---

## 🛠️ Stack y herramientas

| Categoría | Herramientas |
|---|---|
| **SIEM (queries)** | Splunk SPL · Microsoft Sentinel KQL · Elastic Lucene · Sigma · Chronicle YARA-L |
| **EDR / OS telemetry** | osquery · Velociraptor · Sysmon · ETW · auditd · Falco · Wazuh |
| **Network** | Zeek · Suricata · NetFlow · Arkime (Moloch) · RITA |
| **Threat Intel** | MISP · OpenCTI · ATT&CK Navigator · CrowdStrike Falcon Intel |
| **Frameworks** | MITRE ATT&CK · MITRE D3FEND · Diamond Model · Cyber Kill Chain |
| **Hunting methodologies** | PEAK · TaHiTI · MaGMA · ABLE Framework |
| **Adversary emulation** | Atomic Red Team · CALDERA · APTSimulator |
| **Forensic** | KAPE · plaso · Volatility · Velociraptor offline collector |
| **Notebook / análisis** | Jupyter · Pandas · Splunk · Elastic Notebooks |

---

## 🎓 Certificaciones recomendadas

| Nivel | Certificación | Vendor | Costo (USD) | Notas |
|---|---|---|---|---|
| Entry | Microsoft SC-200 | Microsoft | ~$165 | Sentinel + KQL |
| Entry | LetsDefend Threat Hunting | LetsDefend | ~$50/mes | Práctica gratis-low cost |
| Mid | GIAC GCTI | SANS | ~$2,500+ | Threat intelligence applied |
| Mid | GIAC GCFA | SANS | ~$2,500+ | Forensics + hunting |
| Mid | eCTHP | INE | ~$400 | Buen costo-beneficio |
| Senior | GIAC GCIH + GREM | SANS | ~$5,000+ | Top tier |
| Senior | CRTO | Zero-Point Sec | ~$365 | Pero como hunter, conoce TTPs reales |

---

## 🗺️ Roadmap (12 meses)

### Fase 1 — Fundamentos (0-3 meses)
- [ ] MITRE ATT&CK Enterprise: leer top 30 técnicas con sub-techniques
- [ ] Sysmon configurado con [SwiftOnSecurity config](https://github.com/SwiftOnSecurity/sysmon-config)
- [ ] KQL básico en Sentinel (queries para T1059, T1078, T1547)
- [ ] Construir 5 hunts simples documentados con PEAK

### Fase 2 — Especialización (3-6 meses)
- [ ] Atomic Red Team ejecutado contra lab + verificar telemetría
- [ ] CALDERA red ops contra lab → caza con Wazuh + Sysmon
- [ ] Reglas Sigma propias derivadas de tus hunts
- [ ] eCTHP o SC-200 aprobado

### Fase 3 — Profesional (6-12 meses)
- [ ] 10 hunts end-to-end con methodology PEAK
- [ ] Notebook Jupyter con análisis de un IOC chain
- [ ] Charla interna o blog sobre un hallazgo
- [ ] GCTI o GCFA empezado

---

## 💰 Salarios en Colombia (USD/mes)

| Nivel | Local 🇨🇴 | Remoto 🌎 | Notas |
|---|---|---|---|
| Junior (0-2 años) | $900 - $1,700 | $1,800 - $3,200 | Casi siempre llega vía Tier 2 SOC |
| Mid (2-5 años) | $2,200 - $4,500 | $4,000 - $7,500 | Detection Engineer overlap = boost |
| Senior (5+ años) | $5,500 - $10,000 | $8,500 - $14,000 | Hunters con threat intel = premium |

> **Tip:** publicar reglas Sigma propias en GitHub es **el mejor portafolio** para este rol.

---

## 🔗 Conexión con otras ramas

- **`analista-soc`** → tu evolución natural desde Tier 2/3
- **`threat-intelligence`** → hermano gemelo; los IOCs/TTPs guían los hunts
- **`incident-responder`** → handoff cuando confirmas un compromiso
- **`malware-analyst`** → para entender qué buscas
- **`pentester-red-team`** → purple team; entender TTPs ofensivos te hace mejor hunter
- **`forense-digital`** → para evidencia profunda

---

## 📂 Estructura

```
threat-hunter/
├── herramientas/    # KQL queries, SPL searches, osquery packs, Sigma rules
├── recursos/        # ATT&CK layers, PEAK templates, hunting playbooks
├── laboratorios/    # CALDERA + Atomic Red Team + Wazuh setup
└── casos-uso/       # Hunts documentados (hipótesis → datos → resultado)
```

---

<div align="center">

**[⬅ Volver a Ciberseguridad](../README.md)**

</div>
