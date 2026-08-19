<div align="center">

# 🕵️ Threat Intelligence (CTI)

**Emerging 2024-2026 · Cyber Threat Intelligence**

*"No basta saber qué pasó. CTI te dice quién te atacará la próxima semana."*

![Tier](https://img.shields.io/badge/tier%20salarial-B%2FA-orange) ![Demanda](https://img.shields.io/badge/demanda-creciente-green) ![Entry](https://img.shields.io/badge/entry%20level-medio-yellow)

</div>

---

## 📋 Descripción

Disciplina que **convierte datos en decisiones**. Recolecta indicadores (IOCs), TTPs, infraestructura adversaria, dark web chatter, y los traduce en información accionable para SOC, IR, hunt y leadership.

Tres niveles clásicos:
- **Estratégica** — para C-suite (¿quién nos ataca y por qué?)
- **Operativa** — para directores (¿cómo atacan? campañas)
- **Táctica/técnica** — para SOC/hunt (¿IOCs? ¿reglas?)

CTI es **el mejor puente** entre seguridad y áreas no técnicas. Buenos CTI analysts terminan asesorando juntas directivas — el lado "Bond villain dossier" de la ciber.

---

## 👤 Roles típicos

- **Threat Intelligence Analyst** — operación CTI diaria
- **Cyber Threat Researcher** — investigación profunda de actores/campañas
- **Dark Web Analyst** — monitoreo foros, mercados, leaks
- **Brand Protection Analyst** — phishing kits, dominios falsos, fraude
- **Geopolitical Cyber Analyst** *(senior)* — APT atribución, naciones-estado
- **CTI Engineer** — automatización de pipelines OSINT/CTI

---

## 🛠️ Stack y herramientas

| Categoría | Herramientas |
|---|---|
| **Plataformas TIP** | MISP · OpenCTI · Anomali · ThreatConnect · ThreatQ · EclecticIQ |
| **Threat feeds** | AlienVault OTX · Abuse.ch (URLhaus, ThreatFox, MalwareBazaar) · Recorded Future · Mandiant Advantage · Intel 471 |
| **Frameworks de análisis** | Diamond Model · Cyber Kill Chain · MITRE ATT&CK · F3EAD |
| **Standards / sharing** | STIX 2.1 · TAXII 2.x · MISP format · OpenIOC |
| **OSINT** | Maltego · Shodan · Censys · ZoomEye · GreyNoise · DomainTools · RiskIQ (Defender EASM) |
| **Dark web** | Flashpoint · Searchlight Cyber · DarkOwl · Tor browser + opsec |
| **Reporting** | Markdown + Pandoc · Confluence · Notion · custom HTML/PDF |
| **Análisis de muestras** | VirusTotal · Hybrid Analysis · Triage · Any.Run |

---

## 🎓 Certificaciones recomendadas

| Nivel | Certificación | Vendor | Costo (USD) | Notas |
|---|---|---|---|---|
| Entry | OSINT Combine fundamentals | OSINT Combine | $0-100 | Gratis / accesible |
| Entry | SANS SEC487 (OSINT) | SANS | ~$5,000+ | Premium pero gold |
| Mid | GIAC GCTI | SANS | ~$2,500+ | Estándar industria CTI |
| Mid | EC-Council CTIA | EC-Council | ~$1,200 | Más accesible |
| Mid | Mandiant Threat Intel Academy | Mandiant | $0-corporate | Top calidad si tienes acceso |
| Mid | CREST Practitioner Threat Intelligence Analyst (CPTIA) | CREST | ~$700 | Reconocida en EU/UK |
| Senior | CREST Registered TI Analyst (CRTIA) | CREST | ~$1,500 | Top tier |

---

## 🗺️ Roadmap (12 meses)

### Fase 1 — Fundamentos (0-3 meses)
- [ ] Diamond Model + Cyber Kill Chain + MITRE ATT&CK leídos
- [ ] MISP desplegado + 5 feeds OSINT integrados
- [ ] STIX/TAXII estructura entendida
- [ ] OSINT Combine fundamentals o equivalente

### Fase 2 — Análisis aplicado (3-6 meses)
- [ ] Perfil completo de un grupo APT (e.g. APT29, Lazarus, FIN7)
- [ ] Reporte CTI ejecutivo (1 página) + técnico (5+ páginas) sobre el grupo
- [ ] OpenCTI o MISP poblado con relaciones reales
- [ ] CTIA o GCTI empezado

### Fase 3 — Profesional (6-12 meses)
- [ ] Pipeline OSINT automatizado (Python + APIs + MISP push)
- [ ] Charla técnica: análisis de campaña reciente
- [ ] Subscripción a 1 feed premium (Recorded Future trial / Mandiant)
- [ ] GCTI o CRTIA aprobado

---

## 💰 Salarios en Colombia (USD/mes)

| Nivel | Local 🇨🇴 | Remoto 🌎 | Notas |
|---|---|---|---|
| Junior (0-2 años) | $800 - $1,500 | $1,500 - $2,800 | CTI analyst en MSSP/MDR |
| Mid (2-5 años) | $2,000 - $4,000 | $3,500 - $6,500 | GCTI duplica el rango |
| Senior (5+ años) | $4,500 - $8,500 | $7,500 - $13,000 | Lead CTI en banca / vendors |

> **Tip:** combinar inglés + ruso/mandarín/persa **multiplica** el rango (geo-cyber). Pocos lo hacen en LATAM.

---

## 🔗 Conexión con otras ramas

- **`threat-hunter`** → tu output (IOCs, TTPs) guía sus hunts
- **`incident-responder`** → contexto adversario durante IR
- **`malware-analyst`** → atribución basada en code reuse
- **`analista-soc`** → te alimenta, tú lo enriqueces
- **`02-SEGURIDAD-INFORMACION/07-threat-intelligence`** → área de conocimiento
- **`brand-protection`** → si te especializas en fraude/phishing

---

## 📂 Estructura

```
threat-intelligence/
├── herramientas/    # MISP configs, OpenCTI scripts, OSINT pipelines
├── recursos/        # APT reports, ATT&CK groups, frameworks
├── laboratorios/    # MISP local + feeds + correlation
└── casos-uso/       # Análisis de campañas reales (perfilados anonimizados)
```

---

<div align="center">

**[⬅ Volver a Ciberseguridad](../README.md)**

</div>
