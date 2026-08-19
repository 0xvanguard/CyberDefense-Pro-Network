<div align="center">

# 🎯 AI Red Teamer

**Emerging 2024-2026 · Adversarial AI / LLM Red Teaming**

*"Cualquiera puede romper un input field. Pocos saben jailbreakear un agente con tool-use."*

![Tier](https://img.shields.io/badge/tier%20salarial-S-purple) ![Demanda](https://img.shields.io/badge/demanda-explosiva-brightgreen) ![Entry](https://img.shields.io/badge/entry%20level-medio--alto-yellow)

</div>

---

## 📋 Descripción

Rol **ofensivo especializado** en sistemas de IA: LLMs, agentes con tool-use, RAG systems, modelos clásicos de ML. Audita su seguridad y robustez ante adversarios. Cubre:

- **Prompt injection** (direct + indirect)
- **Jailbreaking** modelos alineados
- **Model extraction / stealing**
- **Training data extraction** (membership inference, model inversion)
- **Adversarial examples** en visión / audio / texto
- **Excessive agency** en agentes (LLM08 OWASP)
- **Supply chain attacks** en el ML pipeline

Diferencia con **`ia-security`** *(01)*:
- **`ia-security` (defensiva)** = construye los guardrails
- **`ai-red-teamer` (esta)** = los rompe para validarlos

Es el **rol más sexy de 2025-2026**. Empresas top contratando: Anthropic, OpenAI, Google DeepMind, Microsoft AI Red Team, Meta, NVIDIA, Lakera, Mindgard, HiddenLayer.

---

## 👤 Roles típicos

- **AI Red Teamer / AI Security Researcher** — investigación + auditoría
- **LLM Red Team Engineer** — testing programático con frameworks
- **Adversarial ML Researcher** — academia + industria
- **Trust & Safety Red Team** — content policy bypass + jailbreaks
- **Agentic Security Researcher** *(emergente)* — agentes con tool-use

---

## 🛠️ Stack y herramientas

| Categoría | Herramientas |
|---|---|
| **LLM red teaming frameworks** | **Garak** (NVIDIA) · **PyRIT** (Microsoft) · **promptfoo** · Mindgard · Lakera Red |
| **Adversarial ML** | ART (IBM) · CleverHans · Foolbox · TextAttack · OpenAttack |
| **Agent attack** | LangChain attack patterns · Anthropic Computer Use red team scripts |
| **Jailbreak research** | DAN prompts · masterkey · GCG (gradient-based) · AutoDAN · PAIR |
| **Model extraction** | Membership inference · model stealing PoCs · canary tokens |
| **Datasets** | AdvBench · HarmBench · JailbreakBench · MITRE ATLAS test cases |
| **Frameworks de eval** | OpenAI evals · LMSYS · HumanEval · TruthfulQA · BIG-bench |
| **Ofensiva tradicional** | Burp Suite · custom Python · Browser DevTools (para LLM apps) |
| **Frameworks defensivos refs** | OWASP LLM Top 10 · MITRE ATLAS · NIST AI 600-1 (GenAI) |

---

## 🎓 Certificaciones / formación

| Nivel | Certificación / curso | Vendor | Costo (USD) | Notas |
|---|---|---|---|---|
| Entry | OWASP LLM Top 10 study | OWASP | $0 | **Imprescindible** |
| Entry | MITRE ATLAS matrix study | MITRE | $0 | **Imprescindible** |
| Entry | DeepLearning.AI Generative AI Eng | DeepLearning.AI | ~$50 | Buena base |
| Mid | Lakera Red Team / Gandalf challenges | Lakera | $0-200 | Práctico |
| Mid | NVIDIA Generative AI / Garak | NVIDIA | ~$135 | Garak hands-on |
| Mid | CSA AI Security Professional | CSA | ~$400 | 2024 cert nueva |
| Senior | Pre-OSCP/OSWE *(complementario)* | OffSec | varía | Para sólida base ofensiva clásica |
| Senior | Publicaciones / contribuciones | — | $0 | Reputación >> cert |

---

## 🗺️ Roadmap (12 meses)

### Fase 1 — Fundamentos (0-3 meses)
- [ ] OWASP LLM Top 10 + MITRE ATLAS leídos a profundidad
- [ ] Gandalf (Lakera) niveles 1-7 superados manualmente
- [ ] 3 prompt injections funcionales documentadas
- [ ] Python + LLM APIs (Anthropic, OpenAI, Ollama) funcionando

### Fase 2 — Frameworks (3-7 meses)
- [ ] **Garak** ejecutado contra Llama, Mistral, Claude, GPT
- [ ] **PyRIT** con red team orchestrator + scoring
- [ ] **promptfoo** test suite para 10 jailbreak categories
- [ ] Replicar 3 ataques académicos publicados (PAIR, GCG, AutoDAN)

### Fase 3 — Investigación / aporte (7-12 meses)
- [ ] Auditoría completa de un sistema agentic open source
- [ ] 1 hallazgo reportado (responsible disclosure) a un LLM vendor
- [ ] Contribución a Garak / PyRIT / promptfoo
- [ ] Charla técnica (BSides, DEF CON AI Village, AISA)

---

## 💰 Salarios en Colombia (USD/mes)

| Nivel | Local 🇨🇴 | Remoto 🌎 | Notas |
|---|---|---|---|
| Junior (0-2 años) | $1,500 - $3,000 | $3,000 - $5,500 | Combo IA+sec escaso, premium |
| Mid (2-5 años) | $3,500 - $6,500 | $6,000 - $12,000 | Garak/PyRIT proficiency = palanca |
| Senior (5+ años) | $7,000 - $14,000 | $13,000 - $25,000+ | Anthropic/OpenAI red team tier |

> **Tip:** este es **el nicho de mayor crecimiento %** del 2025-2026. Reputación pública (papers, GitHub, charlas) **vale más que el CV**.

---

## 🔗 Conexión con otras ramas

- **`ia-security`** *(01)* → tu primo gemelo defensivo
- **`ml-security-engineer`** *(03)* → solapamiento técnico fuerte
- **`pentester-red-team`** *(01)* → base ofensiva clásica útil
- **`penetration-tester-specialized`** *(01)* → mismo perfil de specialist
- **`prompt-engineer-security`** *(03)* → subdisciplina aplicada
- **`agentic-security-developer`** *(03)* → red team de agentes

---

## 📂 Estructura

```
ai-red-teamer/
├── herramientas/    # Garak configs, PyRIT scripts, promptfoo suites
├── recursos/        # OWASP LLM Top 10, ATLAS, papers (GCG, PAIR, AutoDAN)
├── laboratorios/    # Modelos abiertos + jailbreak benchmarks
└── casos-uso/       # Reportes responsable disclosure, write-ups éticos
```

---

<div align="center">

**[⬅ Volver a AI Agents & Tools](../README.md)**

</div>
