<div align="center">

# 🔄 Business Continuity Manager

**Continuity & Resilience · ISO 22301 · DR**

*"No te pagan por que nunca pase. Te pagan por que cuando pase, no se note."*

![Tier](https://img.shields.io/badge/tier%20salarial-C%2FB-blue) ![Demanda](https://img.shields.io/badge/demanda-estable-green) ![Entry](https://img.shields.io/badge/entry%20level-amigable-success)

</div>

---

## 📋 Descripción

Rol que **diseña, mantiene y prueba** la capacidad de la organización de **seguir operando** ante interrupciones: desastres naturales, ciberataques (ransomware), fallas de proveedores, pandemias, crisis políticas. Cubre Business Continuity Management (BCM) y Disaster Recovery (DR).

Conceptos centrales:
- **BIA** — Business Impact Analysis (qué procesos son críticos)
- **RTO** — Recovery Time Objective (cuánto tardo en recuperar)
- **RPO** — Recovery Point Objective (cuánto data puedo perder)
- **MTPD** — Maximum Tolerable Period of Disruption
- **BCP / DRP** — Business Continuity Plan / Disaster Recovery Plan
- **Tabletop / Functional / Full-scale** exercises

Demanda subiendo por **DORA** (UE, banca), **NIS2** (UE), **CIRCIA** (US) — regulaciones que exigen continuidad probada.

---

## 👤 Roles típicos

- **Business Continuity Coordinator** — operación BAU
- **BCMS Manager** — programa completo ISO 22301
- **Disaster Recovery Engineer** — más técnico, foco IT
- **Resilience Manager** *(senior)* — combina BCM + cyber + ops risk
- **Cyber Resilience Officer** *(emergente, sectores regulados)*

---

## 🛠️ Stack y herramientas

| Categoría | Herramientas |
|---|---|
| **Standards** | **ISO 22301:2019** (BCMS) · ISO 22313 (guidance) · ISO 22317 (BIA) · ISO/TS 22330-22332 |
| **BCM platforms** | Fusion Risk Mgmt · Veoci · Castellan · Riskonnect · Origami Risk · BC in the Cloud |
| **DR / replication** | Veeam · Zerto · AWS DRS · Azure Site Recovery · Druva · Rubrik |
| **Crisis communication** | Everbridge · OnSolve · AlertMedia · BlackBerry AtHoc |
| **Tabletop / drills** | Tabletop simulation kits · custom decks · Loom asíncronos |
| **Backup verification** | scripts custom · Veeam Surebackup · Rubrik Live Mount |
| **Documentation** | Confluence · Notion · plantillas BCP/DRP |
| **Cloud DR** | Multi-region (AWS/Azure/GCP) · Pilot light / Warm standby / Multi-site active |

---

## 🎓 Certificaciones recomendadas

| Nivel | Certificación | Vendor | Costo (USD) | Notas |
|---|---|---|---|---|
| Entry | ISO 22301 Foundation | PECB | ~$300 | Base |
| Mid | **ISO 22301 Lead Implementer** | PECB | ~$1,200 | El cert estrella |
| Mid | ISO 22301 Lead Auditor | PECB | ~$1,200 | Complemento |
| Mid | CBCP (DRI International) | DRI | ~$800 | Estrella global |
| Mid | MBCP (Master DRI) | DRI | ~$1,200 | Senior tier |
| Mid | CDCP (Data Center Pro) | EPI | ~$1,400 | Si vas DR técnico |
| Senior | FBCI (Fellow BCI) | Business Continuity Institute | varía | UK-strong |

---

## 🗺️ Roadmap (12 meses)

### Fase 1 — Fundamentos (0-3 meses)
- [ ] ISO 22301:2019 leído + ISO 22313 (guía implementación)
- [ ] Diferencia BCP vs DRP vs Crisis Mgmt entendida
- [ ] BIA template + 5 procesos críticos modelados
- [ ] ISO 22301 Foundation aprobado

### Fase 2 — Implementación (3-6 meses)
- [ ] BCMS completo para empresa ficticia (BIA + BCP + DRP + comms)
- [ ] Tabletop documentado: escenario ransomware end-to-end
- [ ] RTO/RPO matrix por sistema crítico
- [ ] **ISO 22301 Lead Implementer aprobado** o CBCP

### Fase 3 — Profesional (6-12 meses)
- [ ] DR técnico: failover real entre regiones cloud
- [ ] Crisis communication plan operativo
- [ ] Functional exercise (no solo tabletop)
- [ ] CBCP o ISO 22301 Lead Auditor

---

## 💰 Salarios en Colombia (USD/mes)

| Nivel | Local 🇨🇴 | Remoto 🌎 | Notas |
|---|---|---|---|
| Junior (0-2 años) | $600 - $1,200 | $1,200 - $2,200 | BCM coordinator |
| Mid (2-5 años) | $1,500 - $3,000 | $2,800 - $5,000 | LI ISO 22301 + CBCP |
| Senior (5+ años) | $3,500 - $6,500 | $5,500 - $10,000 | Resilience Director banca |

> **Tip:** sectores con mayor demanda en CO: **banca, energía, salud, telco**. Combinar BCM + cyber resilience te posiciona en regulaciones modernas (DORA, NIS2).

---

## 🔗 Conexión con otras ramas

- **`grc-compliance`** *(01)* → BCM es control top en ISO 27001 (A.5.29-30)
- **`risk-manager`** *(02)* → BIA usa risk assessments
- **`incident-responder`** *(01)* → ransomware es escenario top de BCP
- **`ciso`** *(02)* → reporte funcional
- **`seguridad-nube`** *(01)* → multi-region DR es técnica crítica

---

## 📂 Estructura

```
business-continuity-manager/
├── herramientas/    # Plantillas BIA, BCP, DRP, crisis comms
├── recursos/        # ISO 22301/22313/22317, NIST 800-34
├── laboratorios/    # Tabletops, multi-region failover labs
└── casos-uso/       # Ejercicios reales documentados, lessons learned
```

---

<div align="center">

**[⬅ Volver a Seguridad de la Información](../README.md)**

</div>
