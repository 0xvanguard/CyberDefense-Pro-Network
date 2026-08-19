<div align="center">

# 🚒 Incident Responder

**NIST NICE · Cyber Defense Incident Responder**

*"Cuando todo arde, alguien tiene que mantener la cabeza fría — eres tú."*

![Tier](https://img.shields.io/badge/tier%20salarial-A%2FB-orange) ![Demanda](https://img.shields.io/badge/demanda-creciente-green) ![Entry](https://img.shields.io/badge/entry%20level-medio--alto-yellow)

</div>

---

## 📋 Descripción

Rol que **lidera la respuesta** cuando se confirma un incidente de seguridad. Sigue el ciclo NIST 800-61 (Preparation → Detection → Containment → Eradication → Recovery → Lessons Learned) bajo presión, coordinando equipos técnicos, legales, comunicaciones y dirección.

Es **alta presión, alto pago**. Las firmas que dominan: Mandiant, CrowdStrike Services, Kroll, Unit 42 (Palo Alto), Sygnia, Coveware (ransomware-focused). En empresa, el IR es senior dentro del SOC o reporta directo al CISO.

---

## 👤 Roles típicos

- **Incident Responder / IR Analyst** — tier 3 SOC con foco IR
- **DFIR Consultant** — firmas externas (Mandiant, CrowdStrike Services)
- **IR Lead / Manager** — coordinación end-to-end
- **Ransomware Negotiator** *(senior, escaso)* — firmas como Coveware
- **Crisis Manager** *(seniority)* — top, hablado con C-suite

---

## 🛠️ Stack y herramientas

| Categoría | Herramientas |
|---|---|
| **Triage rápido** | Velociraptor · KAPE · CyLR · Magnet RESPONSE · GRR |
| **Memory** | Volatility 3 · Rekall · MemProcFS |
| **Disk forensics** | Autopsy · TSK · plaso · Eric Zimmerman tools · X-Ways |
| **Network** | Wireshark · Zeek · Suricata · Arkime · ngrep |
| **EDR / threat hunt** | CrowdStrike RTR · Defender Live Response · SentinelOne RemoteOps |
| **Sandbox** | Any.Run · Hybrid Analysis · CAPE · Cuckoo · Joe Sandbox |
| **Threat Intel** | MISP · OpenCTI · VirusTotal Enterprise · Mandiant Advantage |
| **Communication** | Signal · ProtonMail · isolated comms · pre-defined runbooks |
| **Case mgmt** | TheHive · Resilient · Splunk SOAR cases · Jira incident |
| **Frameworks** | NIST 800-61 · SANS PICERL · MITRE ATT&CK · Diamond Model |

---

## 🎓 Certificaciones recomendadas

| Nivel | Certificación | Vendor | Costo (USD) | Notas |
|---|---|---|---|---|
| Entry | Microsoft SC-200 | Microsoft | ~$165 | Sentinel + IR básica |
| Entry | Blue Team Level 1 (BTL1) | SecurityBlue | ~$500 | Práctica real |
| Mid | GIAC GCIH | SANS | ~$2,500+ | Estándar IR |
| Mid | GIAC GCFA | SANS | ~$2,500+ | Forensics + IR |
| Mid | EC-Council ECIH | EC-Council | ~$700 | Más accesible que SANS |
| Senior | GIAC GCFR (cloud) | SANS | ~$2,500+ | Cloud incident |
| Senior | GIAC GREM | SANS | ~$2,500+ | Reverse de muestras |

---

## 🗺️ Roadmap (12 meses)

### Fase 1 — Fundamentos (0-3 meses)
- [ ] NIST 800-61 leído y sintetizado
- [ ] Lab: ransomware simulado con KAPE + Velociraptor recovery
- [ ] Plantillas IR: runbooks para top-5 incidentes (phishing, ransom, BEC, lateral, exfil)
- [ ] BTL1 o SC-200 aprobado

### Fase 2 — Especialización (3-6 meses)
- [ ] Tabletop exercise documentado (escenario completo)
- [ ] Análisis end-to-end de un caso público (Lapsus$, MOVEit, etc.)
- [ ] Memory forensics con Volatility en 3 imágenes distintas
- [ ] ECIH o GCIH empezado

### Fase 3 — Profesional (6-12 meses)
- [ ] Cloud IR: caso simulado en AWS con CloudTrail + GuardDuty + Detective
- [ ] Reporte ejecutivo + técnico de un incidente real (anonimizado)
- [ ] GCIH o GCFA aprobado
- [ ] Comunicación con stakeholders no-técnicos (charla / drill)

---

## 💰 Salarios en Colombia (USD/mes)

| Nivel | Local 🇨🇴 | Remoto 🌎 | Notas |
|---|---|---|---|
| Junior (0-2 años) | $800 - $1,500 | $1,500 - $2,800 | Llegada vía Tier 2 SOC |
| Mid (2-5 años) | $2,000 - $4,000 | $3,500 - $6,500 | GCIH es palanca importante |
| Senior (5+ años) | $5,000 - $9,500 | $8,000 - $14,000 | DFIR consulting (Mandiant-tier) top |

> **Tip:** firmas como Mandiant, CrowdStrike Services, Kroll y Stroz Friedberg pagan **30-50% más** que enterprise para IR senior remoto.

---

## 🔗 Conexión con otras ramas

- **`forense-digital`** → fusión natural (DFIR)
- **`analista-soc`** → escalas hacia ti en Tier 3
- **`threat-hunter`** → tras el IR, hunting busca persistencia residual
- **`malware-analyst`** → samples encontrados durante IR
- **`seguridad-endpoint`** → tu fuente principal de evidencia
- **`grc-compliance`** → notificaciones regulatorias (GDPR, NIS2, Ley 1581)

---

## 📂 Estructura

```
incident-responder/
├── herramientas/    # KAPE configs, Velociraptor artifacts, runbooks
├── recursos/        # NIST 800-61, SANS PICERL, ATT&CK matrix
├── laboratorios/    # Casos simulados (ransomware, BEC, exfil)
└── casos-uso/       # Post-mortems, lessons learned, timelines
```

---

<div align="center">

**[⬅ Volver a Ciberseguridad](../README.md)**

</div>
