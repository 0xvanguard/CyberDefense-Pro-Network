<div align="center">

# 💬 Prompt Engineer (Security focus)

**Emerging 2024-2026 · Defensive Prompting & Guardrails**

*"Un buen prompt es un firewall invisible. Un mal prompt es un SQL injection con esteroides."*

![Tier](https://img.shields.io/badge/tier%20salarial-B%2FA-orange) ![Demanda](https://img.shields.io/badge/demanda-creciente-green) ![Entry](https://img.shields.io/badge/entry%20level-amigable-success)

</div>

---

## 📋 Descripción

Subdisciplina **práctica y aplicada** del AI Security: diseñar **prompts defensivos**, **system instructions resistentes a jailbreak**, **guardrails** y **output filtering**. Es el lugar donde converge **lingüística + ingeniería + seguridad**.

Diferencia con `ai-red-teamer` y `ml-security-engineer`:
- **AI Red Teamer** *(ofensivo)* — rompe prompts/modelos
- **ML Security Engineer** *(defensa MLOps)* — protege el pipeline
- **Prompt Engineer (Security)** *(esta)* — **diseña el contrato lingüístico** entre user + model + tools

Es el rol con **menor barrera técnica** dentro de `03-` — perfil ideal para perfiles de UX writers, product managers o devs con interés en NLP. La buena noticia: **escasez global de prompt-eng-sec maduros**.

---

## 👤 Roles típicos

- **Security Prompt Engineer** — diseño de system prompts hardened
- **Trust & Safety Prompt Engineer** — content moderation prompts + classifiers
- **Guardrails Engineer** — input validation + output filtering systems
- **GenAI Product Engineer (Security focus)** — features con foco safety
- **LLM Application Engineer (Sec)** — apps con LLM con threat model

---

## 🛠️ Stack y herramientas

| Categoría | Herramientas |
|---|---|
| **LLM platforms** | Anthropic Claude · OpenAI GPT · Google Gemini · Mistral · Llama · Ollama (offline) |
| **Frameworks de prompting** | LangChain · LlamaIndex · DSPy · Guidance · Outlines |
| **Guardrails** | NeMo Guardrails (NVIDIA) · Llama Guard (Meta) · Lakera Guard · Guardrails AI · Rebuff |
| **Eval / testing** | promptfoo · LangSmith · Phoenix (Arize) · Helicone · Galileo |
| **Output structured** | Pydantic + LLM JSON mode · Instructor · Outlines · TypeChat |
| **Red team frameworks (refs)** | Garak · PyRIT (para validar tus defensas) |
| **Prompt patterns** | Few-shot · Chain-of-thought · ReAct · Plan-and-execute · self-critique |
| **Frameworks defensivos** | OWASP LLM Top 10 (LLM01, LLM02, LLM06, LLM08) · Anthropic constitutional AI |
| **Templates** | Jinja2 · LangChain prompt templates · Anthropic prompt library |

---

## 🎓 Certificaciones / formación

| Nivel | Recurso | Vendor | Costo (USD) | Notas |
|---|---|---|---|---|
| Entry | OWASP LLM Top 10 study | OWASP | $0 | Imprescindible |
| Entry | Anthropic Prompt Engineering Course | Anthropic | $0 | Gratis, gold standard |
| Entry | DeepLearning.AI ChatGPT Prompt Eng | DeepLearning.AI | $0 | Andrew Ng + Isa Fulford |
| Entry | OpenAI Cookbook | OpenAI | $0 | Patrones prácticos |
| Mid | Lakera Gandalf challenges | Lakera | $0 | Práctico |
| Mid | LangChain certification | LangChain | ~$200 | Si tu stack es LC |
| Mid | NVIDIA Generative AI | NVIDIA | ~$135 | NeMo Guardrails hands-on |
| Mid | CSA AI Security Professional | CSA | ~$400 | 2024 cert |
| Senior | Reputación pública (papers, GitHub) | — | $0 | Vale más que cert |

---

## 🗺️ Roadmap (12 meses)

### Fase 1 — Fundamentos (0-3 meses)
- [ ] Anthropic + OpenAI prompt courses completados
- [ ] OWASP LLM Top 10 (LLM01, 02, 06, 08) profundo
- [ ] 10 prompts hardened con defenses documentadas
- [ ] Gandalf niveles 1-5 superados

### Fase 2 — Aplicación defensiva (3-6 meses)
- [ ] NeMo Guardrails desplegado en lab
- [ ] Llama Guard + Rebuff como capas de defensa
- [ ] promptfoo test suite con 20+ jailbreak attempts conocidos
- [ ] Sistema completo: input filter → LLM → output filter → audit log

### Fase 3 — Profesional (6-12 meses)
- [ ] Auditoría completa de un sistema con LLM en producción
- [ ] Constitutional AI principles aplicados a un agent propio
- [ ] Charla / blog sobre defensive prompting patterns
- [ ] Contribución a Guardrails AI / NeMo Guardrails / Rebuff

---

## 💰 Salarios en Colombia (USD/mes)

| Nivel | Local 🇨🇴 | Remoto 🌎 | Notas |
|---|---|---|---|
| Junior (0-2 años) | $900 - $1,800 | $1,800 - $3,500 | Prompt eng + sec interest |
| Mid (2-5 años) | $2,200 - $4,500 | $4,000 - $8,000 | Guardrails hands-on = palanca |
| Senior (5+ años) | $5,500 - $10,000 | $9,000 - $16,000 | Trust & Safety en GenAI vendors |

> **Tip:** rol con **mejor ratio entry-vs-pago** dentro de `03-`. Si vienes de UX writing / linguistics / product, **es tu mejor entrada a AI security**.

---

## 🔗 Conexión con otras ramas

- **`ai-red-teamer`** *(03)* → red team que valida tus defensas
- **`ia-security`** *(01)* → engineering broader, tú eres el specialty prompts
- **`agentic-security-developer`** *(03)* → prompts son base de agents seguros
- **`ml-security-engineer`** *(03)* → solapamiento en GenAI product
- **`seguridad-aplicaciones`** *(01)* → si LLMs van en apps web

---

## 📂 Estructura

```
prompt-engineer-security/
├── herramientas/    # NeMo Guardrails configs, Llama Guard, promptfoo suites
├── recursos/        # Anthropic prompt library, OWASP LLM, papers
├── laboratorios/    # Hardened prompts vs jailbreaks documented
└── casos-uso/       # Production prompts (anonimizados), defensive patterns
```

---

<div align="center">

**[⬅ Volver a AI Agents & Tools](../README.md)**

</div>
