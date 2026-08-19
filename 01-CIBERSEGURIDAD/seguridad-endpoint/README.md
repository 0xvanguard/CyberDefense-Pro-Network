<div align="center">

# 💻 Seguridad de Endpoint

**CISSP Domain · Endpoint Security**

*"El usuario hace clic. Tu EDR decide si la empresa sobrevive."*

![Tier](https://img.shields.io/badge/tier%20salarial-B-blue) ![Demanda](https://img.shields.io/badge/demanda-alta-green) ![Entry](https://img.shields.io/badge/entry%20level-amigable-success)

</div>

---

## 📋 Descripción

Disciplina enfocada en proteger el **último kilómetro**: PCs, laptops, servidores, móviles, IoT corporativo. Cubre EDR/XDR, MDM, hardening de SO, application allow-listing, control de dispositivos USB y respuesta a incidentes en endpoint.

Históricamente "antivirus" — hoy es la rama con **mejores señales de telemetría** para threat hunting (Sysmon, EDR events, ETW). Es entry-level amigable: muchos pasan de soporte L2 → SOC Tier 1 → Endpoint Engineer en 2-3 años.

---

## 👤 Roles típicos

- **Endpoint Security Engineer** — diseño + operación de EDR/XDR
- **EDR Analyst (SOC)** — investigación de alertas en CrowdStrike/SentinelOne
- **MDM / UEM Administrator** — Intune, Jamf, Workspace ONE
- **Hardening Specialist** — CIS Benchmarks, STIGs, GPO/MDM policies
- **Detection Engineer (endpoint)** — reglas Sigma, custom IOAs

---

## 🛠️ Stack y herramientas

| Categoría | Herramientas |
|---|---|
| **EDR / XDR** | CrowdStrike Falcon · SentinelOne · Microsoft Defender for Endpoint · Cortex XDR · Carbon Black · Sophos |
| **Open source** | Wazuh · OSSEC · Velociraptor · osquery · Sysmon · Auditd · Falco |
| **MDM / UEM** | Microsoft Intune · Jamf Pro · VMware Workspace ONE · Kandji · MobileIron |
| **AppLocker / WDAC** | Microsoft AppLocker · WDAC · MacOS XProtect · ThreatLocker |
| **Hardening** | CIS-CAT · STIG Viewer · Lynis · Microsoft Security Compliance Toolkit |
| **Forensic triage** | KAPE · Velociraptor · Cyber Triage · Magnet AXIOM |
| **Anti-malware/anti-ransomware** | Microsoft Defender · Bitdefender · ESET · Malwarebytes |

---

## 🎓 Certificaciones recomendadas

| Nivel | Certificación | Vendor | Costo (USD) | Notas |
|---|---|---|---|---|
| Entry | CompTIA Security+ | CompTIA | ~$400 | Base |
| Entry | Microsoft SC-200 | Microsoft | ~$165 | Defender + Sentinel |
| Mid | CrowdStrike CCFA / CCFR | CrowdStrike | ~$200-300 | Estándar EDR |
| Mid | Jamf 200 (cert macOS) | Jamf | ~$200 | Si vas por macOS enterprise |
| Mid | GIAC GCED / GCFE | SANS | ~$2,500+ | Defensiva profunda |
| Senior | CISSP | (ISC)² | ~$750 | Para mando |

---

## 🗺️ Roadmap (12 meses)

### Fase 1 — Fundamentos (0-3 meses)
- [ ] Sysmon + ETW + Auditd activados en lab Windows/Linux
- [ ] Wazuh agent en 3 endpoints (Windows + Linux + macOS)
- [ ] CIS Benchmarks aplicados a un Windows 11 + Ubuntu 22.04
- [ ] SC-200 o Security+ aprobado

### Fase 2 — Especialización (3-6 meses)
- [ ] CrowdStrike Falcon trial: investigación de detecciones
- [ ] osquery + Velociraptor para hunt en endpoints
- [ ] 5 reglas Sigma propias contra técnicas MITRE T1059, T1547, T1078
- [ ] CCFA aprobado

### Fase 3 — Profesional (6-12 meses)
- [ ] MDM real: Intune con compliance policies + autopilot
- [ ] WDAC custom policy con Microsoft Code Integrity
- [ ] Investigación de un incidente real con KAPE + Velociraptor
- [ ] CCFR o GCFE en preparación

---

## 💰 Salarios en Colombia (USD/mes)

| Nivel | Local 🇨🇴 | Remoto 🌎 | Notas |
|---|---|---|---|
| Junior (0-2 años) | $700 - $1,300 | $1,300 - $2,500 | EDR analyst entry-level |
| Mid (2-5 años) | $1,700 - $3,200 | $3,000 - $5,500 | CrowdStrike senior es premium |
| Senior (5+ años) | $4,000 - $7,500 | $6,500 - $11,000 | Detection Engineer remoto top |

> **Tip:** combinar EDR + reglas Sigma propias + GitHub público con detecciones es **mejor que un CV genérico**.

---

## 🔗 Conexión con otras ramas

- **`incident-responder`** → endpoint es la fuente #1 de evidencia
- **`threat-hunter`** → osquery + Sysmon + EDR son tu cocina
- **`malware-analyst`** → samples llegan desde endpoints
- **`analista-soc`** → 60-70% de alertas vienen de endpoint
- **`forense-digital`** → triage rápido es el primer paso

---

## 📂 Estructura

```
seguridad-endpoint/
├── herramientas/    # Configs Sysmon, Wazuh agent, AppLocker XML
├── recursos/        # CIS Benchmarks, STIGs, MITRE D3FEND mapping
├── laboratorios/    # Endpoint comprometido + recovery
└── casos-uso/       # LOLBins detection, ransomware containment
```

---

<div align="center">

**[⬅ Volver a Ciberseguridad](../README.md)**

</div>
