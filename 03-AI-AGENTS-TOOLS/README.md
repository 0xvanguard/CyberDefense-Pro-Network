<div align="center">

# 🤖 03 — AI AGENTS & TOOLS

**Automatización con LLMs · Agentes IA · LLM Security**

*"El próximo pentester no escribe payloads — orquesta agentes que los escriben."*

</div>

---

## 🎯 Propósito

Esta sección documenta el cruce entre **Inteligencia Artificial** y **ciberseguridad** en sus tres dimensiones:

1. **IA aplicada a ofensiva** — agentes que automatizan recon, pentest, generación de reportes.
2. **IA aplicada a defensiva** — clasificación de alertas, triage automatizado, detección de anomalías.
3. **Seguridad de la propia IA** — atacar y defender LLMs (prompt injection, jailbreaks, AI red teaming).

> 🧠 **Filosofía:** *Agency over Automation*. Los agentes deben **razonar** sobre los hallazgos, no solo redirigir output crudo. Cada decisión lleva un **confidence score** y se escala a humano si baja del 85%.

---

## 🗺️ Mapa de subdominios

| # | Subdominio | Foco |
|---|---|---|
| 01 | [Agentes OSINT](./01-agentes-osint/) | Pipelines de recolección + análisis automatizado |
| 02 | [Agentes Pentest](./02-agentes-pentest/) | Recon automático · generadores de reportes |
| 03 | [LLM Security](./03-llm-security/) | Atacar y defender modelos (OWASP LLM Top 10) |
| 04 | [Herramientas Trending](./04-herramientas-trending/) | Tooling emergente que vale la pena explorar |
| 05 | [Automatización Python](./05-automatizacion-python/) | Scripts y bots utilitarios |

---

## 🕸️ 01 — Agentes OSINT

> **Objetivo:** orquestar herramientas OSINT con un LLM que estructura, deduplica y prioriza hallazgos.

**Patrón de pipeline:**
```
[Input: dominio/email/usuario]
        │
        ▼
[Recolección paralela] ── theHarvester · Subfinder · SpiderFoot · Photon
        │
        ▼
[Normalización] ── Pydantic models · deduplicación
        │
        ▼
[LLM análisis] ── Claude/Ollama · structured output (JSON schema)
        │
        ▼
[Reporte] ── Markdown + HTML + notificación Telegram
```

**Subcarpetas:**
- `pipelines/` — DAGs reutilizables
- `automatizacion/` — scripts CLI

📁 [`./01-agentes-osint/`](./01-agentes-osint/)

---

## ⚔️ 02 — Agentes Pentest

> **Objetivo:** agentes que coordinan herramientas ofensivas con razonamiento contextual.

**Subcarpetas:**

| Subcarpeta | Foco |
|---|---|
| `recon-automatizado/` | Nmap → Nuclei → wafw00f → razonamiento LLM → priorización |
| `report-generators/` | Plantillas Jinja2 + WeasyPrint para PDF · output Markdown |

**Reglas obligatorias para agentes ofensivos:**
1. ✅ Validación de scope (whitelist de targets) **antes** de cualquier ejecución
2. ✅ Confidence scoring en cada paso (0–100)
3. ✅ Timeout + retry con exponential backoff en cada herramienta
4. ✅ Logs estructurados (JSON, structlog)
5. ✅ **Halt graceful** ante cualquier excepción + notificación al operador

📁 [`./02-agentes-pentest/`](./02-agentes-pentest/)

---

## 🛡️ 03 — LLM Security

> **Objetivo:** atacar y defender modelos de lenguaje grandes.

**Marcos de referencia:**
- **OWASP Top 10 for LLM Applications**
- **NIST AI RMF (AI 100-1)**
- **MITRE ATLAS** — Adversarial Threat Landscape for AI Systems

**OWASP LLM Top 10 cubierto:**

| ID | Vulnerabilidad |
|---|---|
| LLM01 | Prompt Injection |
| LLM02 | Insecure Output Handling |
| LLM03 | Training Data Poisoning |
| LLM04 | Model Denial of Service |
| LLM05 | Supply Chain Vulnerabilities |
| LLM06 | Sensitive Information Disclosure |
| LLM07 | Insecure Plugin Design |
| LLM08 | Excessive Agency |
| LLM09 | Overreliance |
| LLM10 | Model Theft |

**Subcarpetas:**
- `prompt-injection/` — direct + indirect injection · jailbreaks documentados
- `ai-red-teaming/` — metodología para auditar LLMs (PyRIT, Garak)

**Herramientas:**
- `Garak` (NVIDIA) — LLM vulnerability scanner
- `PyRIT` (Microsoft) — Python Risk Identification Tool
- `promptfoo` — testing de prompts

📁 [`./03-llm-security/`](./03-llm-security/)

---

## 🚀 04 — Herramientas Trending

> **Objetivo:** explorar tooling emergente del ecosistema agentic.

**Subcarpetas:**

| Subcarpeta | Concepto |
|---|---|
| `agents-cli/` | CLIs basados en agentes (e.g. Google's agents-cli, Aider, Claude Code) |
| `freellmapi/` | APIs de LLMs gratuitas/self-hosted (Ollama, Groq, OpenRouter) |
| `background-computer-use/` | Anthropic Computer Use, browser agents en background |
| `otros/` | Kit-bag general de herramientas emergentes |

**Criterio de inclusión:**
1. Open source o con tier gratuito sólido
2. Aplicable a casos de seguridad
3. Activamente mantenido (commits en últimos 3 meses)

📁 [`./04-herramientas-trending/`](./04-herramientas-trending/)

---

## 🐍 05 — Automatización Python

> **Objetivo:** utilities reutilizables que conectan todo el ecosistema.

**Subcarpetas:**

| Subcarpeta | Contenido |
|---|---|
| `scripts/` | Scripts CLI específicos (parsers, normalizadores, exporters) |
| `bots/` | Bots de Telegram/Discord para notificaciones de eventos de seguridad |

**Stack estándar:**
- Python 3.12+ (async-first)
- `Pydantic v2` — validación + structured output
- `httpx` — HTTP async
- `structlog` — logging JSON
- `python-dotenv` — secrets en `.env`
- `Typer` — CLIs declarativas
- `pytest` — testing

**Principios obligatorios:**
- ✅ Type hints en **todo**
- ✅ Docstrings en **toda función pública**
- ✅ Manejo de errores explícito (no `except: pass`)
- ✅ Secrets jamás hardcodeados (siempre `.env` + `.env.example`)
- ✅ Tests para lógica de negocio (no para wrappers triviales)

📁 [`./05-automatizacion-python/`](./05-automatizacion-python/)

---

## 💼 Ramas laborales — Carrera profesional (7 paths)

> Los **roles laborales** que el cruce IA × Ciberseguridad está creando. Algunos son frontera 2025-2026 con escasez global de talento.

| Rama | Tier salarial | Mid-USD/mes | Highlight |
|---|---|---|---|
| [`ai-red-teamer/`](./ai-red-teamer/) | **S** | $3,500-6,500 | Anthropic / OpenAI tier · reputación pública > CV |
| [`ml-security-engineer/`](./ml-security-engineer/) | **S** | $3,000-6,000 | MLOps + sec en HF / Anthropic / Cohere remoto |
| [`ai-governance-officer/`](./ai-governance-officer/) | A/S | $3,000-6,000 | Puede pagar más que CISO en sectores regulados |
| [`prompt-engineer-security/`](./prompt-engineer-security/) | B/A | $2,200-4,500 | Mejor ratio entry-vs-pago de `03-` |
| [`agentic-security-developer/`](./agentic-security-developer/) | **S** | $3,500-7,000 | El rol más nuevo y mejor pagado · cero saturación |
| [`ai-incident-responder/`](./ai-incident-responder/) | A | $2,800-5,500 | First-mover advantage 2025-2026 |
| [`ai-supply-chain-security/`](./ai-supply-chain-security/) | A | $2,500-4,800 | Ideal cruce desde DevSecOps clásico |

> Ver cada README para breakdown completo por nivel (Junior / Mid / Senior · Local / Remoto).

---

## 🧱 Patrón arquitectónico de referencia

Inspirado en arquitecturas agenticas modernas (AISAC, ReAct, Plan-and-Execute):

```
┌─────────────────────────────────────────────────────────────┐
│                      ORCHESTRATOR                           │
│  (Plan · Reason · Decide · Confidence Score · Escalate)     │
└─────────────────────────────────────────────────────────────┘
            │                    │                    │
            ▼                    ▼                    ▼
    ┌───────────────┐    ┌───────────────┐    ┌───────────────┐
    │  Recon Agent  │    │ Vuln Analyst  │    │ Report Agent  │
    │   (theHarv,   │    │    (Nuclei,   │    │  (Jinja2 +    │
    │   Subfinder)  │    │   Nmap NSE)   │    │  WeasyPrint)  │
    └───────────────┘    └───────────────┘    └───────────────┘
            │                    │                    │
            └────────────┬───────┴───────────┬────────┘
                         ▼                   ▼
                  ┌─────────────┐    ┌─────────────┐
                  │  Storage    │    │ Notifier    │
                  │ (SQLite/PG) │    │ (TG/Disc)   │
                  └─────────────┘    └─────────────┘
```

---

## ⚖️ Aviso ético específico para IA

- 🚫 **No usar LLMs para generar malware funcional** ni para automatizar ataques contra terceros sin autorización.
- 🔍 **Auditar siempre** el output de un LLM antes de ejecutarlo (especialmente comandos shell).
- 🔐 **Sanitizar inputs** antes de enviarlos al modelo (evitar prompt injection desde fuentes externas).
- 🧾 **Registrar prompts y responses** para trazabilidad forense.

---

<div align="center">

**[⬅ Volver al README principal](../README.md)** · **[🧪 Ir a Laboratorios →](../04-LABORATORIOS/)**

</div>
