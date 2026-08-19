<div align="center">

# 🚨 AI Incident Responder

**Emerging 2024-2026 · IR for AI Systems**

*"Tu agente leakeó la KB privada. Tu LLM hizo refunds. Tu RAG entregó datos de otro cliente. ¿Y ahora qué?"*

![Tier](https://img.shields.io/badge/tier%20salarial-A-orange) ![Demanda](https://img.shields.io/badge/demanda-creciente-green) ![Entry](https://img.shields.io/badge/entry%20level-medio--alto-yellow)

</div>

---

## 📋 Descripción

Rol **híbrido y emergente** que adapta el ciclo NIST 800-61 a **incidentes específicos de sistemas IA**:

- **LLM03** — Training data poisoning (descubierto post-deployment)
- **LLM06** — Sensitive Information Disclosure (RAG leaks, prompt injection extrayendo datos)
- **LLM07** — Insecure Plugin / Tool execution (acción no autorizada)
- **LLM08** — Excessive Agency (agente ejecutó algo destructivo)
- **LLM10** — Model theft / Model file backdoor
- **GenAI hallucinations causando daño** (médico, legal, financiero)
- **Bias / discrimination incidents** (regulatorios)

Difiere del IR clásico:
- **No hay disco que imagear** — el "incidente" puede ser una conversación
- **Reproducir es difícil** — temperature, sampling, model versions
- **Stakeholders nuevos** — Legal, Trust & Safety, comms, AI ethics board
- **Notificaciones regulatorias nuevas** — EU AI Act art. 73 (serious incidents)

---

## 👤 Roles típicos

- **AI Incident Responder** — IR especializado en sistemas IA
- **Trust & Safety Incident Lead** *(GenAI vendors)* — content/policy violations
- **AI Crisis Manager** *(senior)* — comms ejecutiva durante incidentes
- **GenAI Product IR** — embebido en equipo de producto
- **AI Forensics Specialist** *(emergente)* — reconstrucción de prompt/tool chains

---

## 🛠️ Stack y herramientas

| Categoría | Herramientas |
|---|---|
| **Observability LLM** | LangSmith · Langfuse · Helicone · Phoenix (Arize) · Galileo · Honeycomb |
| **Audit logs** | Custom structlog · OpenTelemetry · S3 logs con object lock · CloudWatch |
| **Replay / forensics** | LangSmith traces · prompt + response + tools captured · model version pinning |
| **Sandbox de análisis** | Modelos abiertos (Llama, Mistral) en lab para reproducir |
| **Threat Intel AI** | OWASP LLM Top 10 · MITRE ATLAS · AI Vulnerability Database (AVID) · Robust Intelligence DB |
| **Notification / case mgmt** | TheHive · ServiceNow IRM · Jira · custom GenAI runbooks |
| **Comms** | Signal · ProtonMail · pre-defined comms templates · regulatory notification templates |
| **Frameworks** | NIST 800-61 (adaptado) · NIST AI RMF · EU AI Act Art. 73 · OWASP LLM IR playbooks |

---

## 🎓 Certificaciones / formación

| Nivel | Certificación | Vendor | Costo (USD) | Notas |
|---|---|---|---|---|
| Pre-req | GIAC GCIH o BTL1 | SANS / SecBlue | ~$500-2,500 | IR tradicional base |
| Entry | OWASP LLM Top 10 + ATLAS | OWASP / MITRE | $0 | Imprescindible |
| Entry | Anthropic / OpenAI safety guides | vendors | $0 | Patrones de incidentes |
| Mid | NIST AI RMF self-study | NIST | $0 | Adapta IR al ciclo AI |
| Mid | AIGP (AI Governance Pro) | IAPP | ~$550 | Regulatorio |
| Mid | CSA AI Security Professional | CSA | ~$400 | 2024 cert |
| Senior | GIAC GCFR (cloud forensics) | SANS | ~$2,500+ | Cloud + AI overlap |

---

## 🗺️ Roadmap (12 meses)

### Fase 1 — Fundamentos (0-3 meses)
- [ ] NIST 800-61 dominado
- [ ] OWASP LLM Top 10 + MITRE ATLAS estudiados con foco IR
- [ ] LangSmith / Langfuse desplegado en lab con app LLM
- [ ] Runbooks AI IR: 5 escenarios típicos (leak RAG, jailbreak en prod, hallucination dañina, agente ejecutó X, bias detectado)

### Fase 2 — Práctica aplicada (3-7 meses)
- [ ] Tabletop AI: leak de PII vía prompt injection (end-to-end)
- [ ] Replay de un incidente con prompt + tool trace + model version
- [ ] Plantillas de notificación regulatoria (EU AI Act + Ley 1581 + sectorial)
- [ ] AIGP empezado o CSA AI Security

### Fase 3 — Profesional (7-12 meses)
- [ ] AI IR plan completo para una empresa con sistemas GenAI
- [ ] Coordinación con Trust & Safety + Legal + Privacy en simulacro
- [ ] Caso real (público): post-mortem de un incidente notable (ej. Air Canada chatbot, Samsung leak vía ChatGPT)
- [ ] Charla técnica o blog

---

## 💰 Salarios en Colombia (USD/mes)

| Nivel | Local 🇨🇴 | Remoto 🌎 | Notas |
|---|---|---|---|
| Junior (0-2 años) | $1,200 - $2,200 | $2,200 - $4,000 | IR tradicional + AI awareness |
| Mid (2-5 años) | $2,800 - $5,500 | $4,500 - $9,000 | Hands-on AI IR runbooks |
| Senior (5+ años) | $6,500 - $12,000 | $10,000 - $20,000 | GenAI vendor T&S + IR top |

> **Tip:** el primer ola de "AI incident response" maduros aparece en 2025-2026. Posicionarte ahora con runbooks publicados + casos públicos analizados = **first-mover advantage**.

---

## 🔗 Conexión con otras ramas

- **`incident-responder`** *(01)* → tu base IR clásica
- **`ai-red-teamer`** *(03)* → para reproducir el ataque post-incidente
- **`ia-security`** *(01)* → defensiva que tú coordinas en crisis
- **`ai-governance-officer`** *(03)* → regulatory + reporting al Board
- **`forense-digital`** *(01)* → adaptación de cadena de custodia a AI
- **`threat-intelligence`** *(01)* → AI threat intel emergente (AVID, ATLAS)

---

## 📂 Estructura

```
ai-incident-responder/
├── herramientas/    # LangSmith dashboards, runbooks AI IR, plantillas notif
├── recursos/        # NIST 800-61 + AI adaptación, ATLAS, EU AI Act art.73
├── laboratorios/    # Tabletops AI completos (leak, jailbreak, hallucination)
└── casos-uso/       # Post-mortems públicos analizados, lessons learned
```

---

<div align="center">

**[⬅ Volver a AI Agents & Tools](../README.md)**

</div>
