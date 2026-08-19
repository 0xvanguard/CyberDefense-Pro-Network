<div align="center">

# 🔬 Forense Digital

**NIST NICE · Cyber Defense Forensics Analyst**

*"En forense, los bytes no mienten — solo hay que saber preguntarles."*

![Tier](https://img.shields.io/badge/tier%20salarial-B-blue) ![Demanda](https://img.shields.io/badge/demanda-estable-green) ![Entry](https://img.shields.io/badge/entry%20level-medio-yellow)

</div>

---

## 📋 Descripción

Disciplina que **reconstruye lo que pasó** en sistemas, redes y memoria tras un incidente. Cubre disk forensics, memory forensics, network forensics, mobile forensics y cloud forensics. Es **legal-friendly**: cadena de custodia, integridad de evidencia y peritaje técnico.

Dos vertientes:
- **DFIR** (Digital Forensics + Incident Response) — combo más demandado en empresa
- **eDiscovery / litigation forensics** — soporte legal, fraude, peritajes

---

## 👤 Roles típicos

- **DFIR Analyst** — fusión forense + IR
- **Computer Forensic Examiner** — peritaje legal
- **Mobile Forensics Specialist** — extracción y análisis de móviles
- **Memory Forensics Analyst** *(senior)* — Volatility specialist
- **Cloud Forensics** *(emergente)* — AWS/Azure incident reconstruction

---

## 🛠️ Stack y herramientas

| Categoría | Herramientas |
|---|---|
| **Disk forensics** | Autopsy · The Sleuth Kit · FTK · X-Ways · EnCase *(comerciales)* |
| **Memory** | Volatility 3 · Rekall · MemProcFS · Volatility Workbench |
| **Triage rápido** | KAPE · Velociraptor offline collector · CyLR · Magnet AXIOM |
| **Timeline** | log2timeline (plaso) · Timeline Explorer · Eric Zimmerman tools |
| **Network forensics** | Wireshark · NetworkMiner · tshark · Arkime · Brim |
| **Mobile** | Cellebrite UFED · Magnet AXIOM Mobile · iLEAPP/aLEAPP · MOBILedit |
| **Cloud** | AWS CloudTrail Analyzer · Azure logs analyzer · GCP Audit Logs |
| **Hashing & integridad** | sha256sum · md5deep · ssdeep · TLSH |
| **Análisis de archivos** | ExifTool · oletools · pdfinfo · pdf-parser · binwalk |

---

## 🎓 Certificaciones recomendadas

| Nivel | Certificación | Vendor | Costo (USD) | Notas |
|---|---|---|---|---|
| Entry | CompTIA Security+ | CompTIA | ~$400 | Base general |
| Entry | CHFI v10 | EC-Council | ~$1,200 | Conocida pero criticada |
| Mid | GIAC GCFE / GCFA | SANS | ~$2,500+ ea | Estándar de industria |
| Mid | GIAC GREM (malware) | SANS | ~$2,500+ | Si te interesa malware |
| Mid | Cellebrite CCO/CCPA | Cellebrite | ~$2,000 | Si vas por móvil/legal |
| Senior | GIAC GCFR (cloud forensics) | SANS | ~$2,500+ | Nicho creciente |
| Senior | EnCE / EnCEP | OpenText | ~$1,000 | Legal-heavy |

---

## 🗺️ Roadmap (12 meses)

### Fase 1 — Fundamentos (0-3 meses)
- [ ] Conceptos: cadena de custodia, integridad, hashing forense
- [ ] Lab: Autopsy + imagen E01 de prueba (CFReDS Project samples)
- [ ] Volatility 3 + memdump de Windows lab
- [ ] Security+ aprobado

### Fase 2 — Especialización (3-6 meses)
- [ ] KAPE + Velociraptor para triage de un caso simulado
- [ ] Timeline forense con plaso
- [ ] 3 retos de DFIR (Cyberdefenders, BlueTeamLabs Online)
- [ ] GCFE empezado

### Fase 3 — Profesional (6-12 meses)
- [ ] Análisis end-to-end de un caso ransomware (post-mortem público)
- [ ] Cloud forensics: análisis de CloudTrail tras compromiso simulado
- [ ] Reporte forense con cadena de custodia formal
- [ ] GCFE o CHFI aprobado

---

## 💰 Salarios en Colombia (USD/mes)

| Nivel | Local 🇨🇴 | Remoto 🌎 | Notas |
|---|---|---|---|
| Junior (0-2 años) | $700 - $1,300 | $1,300 - $2,500 | DFIR jr en MSSPs/MDR |
| Mid (2-5 años) | $1,800 - $3,500 | $3,000 - $5,500 | Pericial legal sube tarifa |
| Senior (5+ años) | $4,000 - $7,500 | $6,500 - $11,000 | DFIR + cloud + memory = premium |

> **Tip:** complementar con peritaje legal ante fiscalía / cortes en Colombia abre tarifas por hora muy distintas a salario.

---

## 🔗 Conexión con otras ramas

- **`incident-responder`** → DFIR es la fusión natural
- **`malware-analyst`** → samples encontrados durante forense
- **`threat-hunter`** → memoria + disco son insumo de hunts
- **`analista-soc`** → escalas hacia ti cuando un caso se calienta
- **`seguridad-endpoint`** → fuente principal de evidencia
- **`grc-compliance`** → cadena de custodia + privacidad de evidencia

---

## 📂 Estructura

```
forense-digital/
├── herramientas/    # KAPE configs, Volatility plugins, plaso filters
├── recursos/        # NIST 800-86, RFC 3227, plantillas cadena de custodia
├── laboratorios/    # CFReDS samples, BlueTeamLabs writeups
└── casos-uso/       # Casos completos (anonimizados) end-to-end
```

---

<div align="center">

**[⬅ Volver a Ciberseguridad](../README.md)**

</div>
