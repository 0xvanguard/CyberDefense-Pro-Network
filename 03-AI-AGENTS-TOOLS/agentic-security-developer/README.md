<div align="center">

# 🤖 Agentic Security Developer

**Emerging 2024-2026 · Secure Agent Engineering**

*"Un agente con tool-use es shell-as-a-service. Sin sandbox, es shell-as-a-disaster."*

![Tier](https://img.shields.io/badge/tier%20salarial-S-purple) ![Demanda](https://img.shields.io/badge/demanda-explosiva-brightgreen) ![Entry](https://img.shields.io/badge/entry%20level-medio--alto-yellow)

</div>

---

## 📋 Descripción

Rol **frontera 2025-2026** que combina **engineering de agentes IA con tool-use** + **principios de seguridad robustos**. Cubre el riesgo más nuevo y peor entendido de la industria: **excessive agency** (LLM08 OWASP) — agentes que pueden ejecutar herramientas, leer/escribir filesystems, hacer requests HTTP, navegar browsers, ejecutar código.

Stack típico de un agente moderno:
```
[User intent]
    ↓
[Planner LLM] → genera plan
    ↓
[Tool selector] → escoge herramientas
    ↓
[Tool executor] ← ⚠️ ZONA DE PELIGRO
    ↓ (shell, browser, API, RAG)
[Memory / state]
    ↓
[Response]
```

Cada flecha es un vector. Este rol **piensa en cada flecha como threat model**.

---

## 👤 Roles típicos

- **Agentic Engineer (Security focus)** — desarrollo seguro de agentes
- **AI Platform Security Engineer** — infraestructura para múltiples agentes
- **Computer Use Security** *(emergente)* — Anthropic Computer Use, browser agents
- **Tool-use Sandbox Engineer** — ejecución aislada de tool calls
- **MCP / A2A Security Engineer** *(super-emergente)* — Model Context Protocol security

---

## 🛠️ Stack y herramientas

| Categoría | Herramientas |
|---|---|
| **Agent frameworks** | LangGraph (LangChain) · CrewAI · AutoGen (Microsoft) · OpenAI Agents SDK · Anthropic SDK · Pydantic AI |
| **Sandboxing tools** | E2B · Daytona · Modal · Firecracker microVMs · Docker rootless · gVisor · containerd |
| **MCP / A2A** | Anthropic MCP · Google A2A · custom JSON-RPC |
| **Browser agents** | Playwright + sandbox · BrowserUse · Stagehand · Anthropic Computer Use |
| **Code execution** | E2B Code Interpreter · Daytona · Pyodide (browser) · isolated containers |
| **Memory / state** | Redis (con encryption) · Postgres (RLS) · vector DBs (Pinecone/Weaviate) |
| **Guardrails** | NeMo Guardrails · Llama Guard · custom validators |
| **Audit / observability** | LangSmith · Helicone · Langfuse · structlog + OpenTelemetry |
| **Security patterns** | Capability-based security · least privilege per tool · per-call scope tokens |
| **Frameworks** | OWASP LLM (LLM07 Insecure Plugins, LLM08 Excessive Agency) · MITRE ATLAS |

---

## 🎓 Certificaciones / formación

| Nivel | Recurso | Vendor | Costo (USD) | Notas |
|---|---|---|---|---|
| Entry | Anthropic Tool Use docs + cookbook | Anthropic | $0 | Imprescindible |
| Entry | OpenAI Function Calling guide | OpenAI | $0 | Imprescindible |
| Entry | OWASP LLM07 + LLM08 study | OWASP | $0 | Foco para esta rama |
| Mid | LangChain Academy (Agents) | LangChain | ~$200 | LangGraph hands-on |
| Mid | DeepLearning.AI Multi-Agent Systems | DeepLearning.AI | ~$50 | Andrew Ng + AutoGen |
| Mid | NVIDIA Multi-Agent Generative AI | NVIDIA | ~$135 | Práctico |
| Senior | Publicaciones / research | — | $0 | Reputación >> cert |

---

## 🗺️ Roadmap (12 meses)

### Fase 1 — Fundamentos (0-3 meses)
- [ ] Tool use con Anthropic + OpenAI funcional (5 tools custom)
- [ ] OWASP LLM07 + LLM08 estudiados con casos
- [ ] Threat model de un agente simple (file system + web)
- [ ] LangGraph básico

### Fase 2 — Sandbox & guardrails (3-7 meses)
- [ ] Tool execution en E2B / Daytona / Docker rootless
- [ ] Capability-based scoping por tool
- [ ] Output validation con Pydantic + JSON Schema strict
- [ ] Audit log estructurado de cada tool call

### Fase 3 — Agente production-ready (7-12 meses)
- [ ] Agente completo con: scope enforcement + sandboxing + guardrails + audit
- [ ] Threat model + attack tree publicado
- [ ] MCP server propio con autenticación + rate limiting
- [ ] Charla técnica o blog sobre agentic security

---

## 💰 Salarios en Colombia (USD/mes)

| Nivel | Local 🇨🇴 | Remoto 🌎 | Notas |
|---|---|---|---|
| Junior (0-2 años) | $1,500 - $3,000 | $3,000 - $5,500 | Combo agentic + sec escaso |
| Mid (2-5 años) | $3,500 - $7,000 | $6,500 - $13,000 | LangGraph + sandbox = palanca |
| Senior (5+ años) | $7,500 - $14,000 | $13,000 - $25,000+ | Anthropic / OpenAI / Mistral tier |

> **Tip 2025-2026:** este es **el rol más nuevo y mejor pagado de la lista**. Pre-OSCP base ofensiva + Python avanzado + agent framework mastery = combo único en LATAM. Cero saturación.

---

## 🔗 Conexión con otras ramas

- **`ai-red-teamer`** *(03)* → testing de tus agentes
- **`ia-security`** *(01)* → tu output entra a su programa defensivo
- **`prompt-engineer-security`** *(03)* → prompts defensivos para agents
- **`ml-security-engineer`** *(03)* → infra MLOps que ejecuta agents
- **`security-engineer`** *(01)* → seguridad backend tradicional aplicada a agents
- **`seguridad-cadena-suministro`** *(01)* → MCP servers + tool definitions supply chain

---

## 📂 Estructura

```
agentic-security-developer/
├── herramientas/    # E2B configs, MCP servers, sandbox patterns
├── recursos/        # OWASP LLM07/08, MITRE ATLAS, MCP spec
├── laboratorios/    # Agentes con threat model + sandbox implementado
└── casos-uso/       # Agentes production-ready (anonimizados), audits
```

---

<div align="center">

**[⬅ Volver a AI Agents & Tools](../README.md)**

</div>
