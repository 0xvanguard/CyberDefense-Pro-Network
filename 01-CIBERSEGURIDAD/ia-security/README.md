<div align="center">

# 🤖 IA Security

**Emerging 2024-2026 · AI/ML Security**

*"El próximo CVE crítico no será en Apache — será en el LLM de tu ChatBot."*

![Tier](https://img.shields.io/badge/tier%20salarial-S-purple) ![Demanda](https://img.shields.io/badge/demanda-explosiva-brightgreen) ![Entry](https://img.shields.io/badge/entry%20level-medio--alto-yellow)

</div>

---

## 📋 Descripción

Rama **emergente y explosiva**: protege sistemas de IA/ML (LLMs, modelos clásicos, agentes) y usa IA para mejorar la propia ciberseguridad (detección, automatización). Cubre OWASP LLM Top 10, MITRE ATLAS, NIST AI RMF y los nuevos vectores: prompt injection, model extraction, training data poisoning, jailbreaks, agentic excessive agency.

Diferencia con `ai-red-teamer` *(03)*:
- **`ia-security` (esta)**: rol **defensivo** end-to-end — proteger sistemas de IA en producción
- **`ai-red-teamer` (03)**: rol **ofensivo** — atacar y auditar modelos/agentes

Es el nicho con **mayor crecimiento porcentual** de la industria 2024-2026.

---

## 👤 Roles típicos

- **AI Security Engineer** — protección de pipelines ML y deployments LLM
- **ML Security Researcher** — academia + industria, vulnerabilidades en modelos
- **Agentic Security Engineer** *(emergente)* — para sistemas con tool-use
- **GenAI Trust & Safety** — moderación + alignment + jailbreak resistance
- **AI Privacy Engineer** — DP, PETs, federated learning

---

## 🛠️ Stack y herramientas

| Categoría | Herramientas |
|---|---|
| **LLM red teaming** | Garak (NVIDIA) · PyRIT (Microsoft) · promptfoo · Mindgard · Lakera |
| **Adversarial ML** | ART (IBM) · CleverHans · Foolbox · TextAttack |
| **Agent security** | LangSmith eval · Llama Guard · NeMo Guardrails · Lakera Guard |
| **Prompt eval** | promptfoo · LangSmith · Helicone · Phoenix (Arize) |
| **Model scanning** | ProtectAI ModelScan · Hugging Face Picklescan · Trivy ML |
| **MLOps security** | MLflow · DVC · Wandb (con security policies) |
| **PETs** | OpenDP · Opacus (DP) · TenSEAL (FHE) · PySyft (FL) |
| **LLM Frameworks** | LangChain (con cuidado) · LlamaIndex · Haystack · DSPy |
| **Frameworks defensivos** | OWASP LLM Top 10 · MITRE ATLAS · NIST AI RMF · ISO/IEC 42001 |

---

## 🎓 Certificaciones recomendadas

| Nivel | Certificación | Vendor | Costo (USD) | Notas |
|---|---|---|---|---|
| Entry | AWS AI Practitioner (AIF-C01) | AWS | ~$100 | Base AI cloud |
| Entry | Microsoft AI-900 | Microsoft | ~$100 | Conceptos |
| Entry | Coursera ML Security & Privacy | Coursera | ~$50 | Buenas bases |
| Mid | OWASP LLM Top 10 study (no cert) | OWASP | $0 | **Imprescindible leerlo** |
| Mid | NVIDIA Generative AI Pro | NVIDIA | ~$135 | Buena para arrancar |
| Mid | Lakera Red Team Course | Lakera | $0-200 | Red team práctico |
| Mid | CSA AI Security Professional | CSA | ~$400 | 2024 cert nueva |
| Senior | ISC2 ISSAP / SABSA + AI focus | (ISC)² | varia | No hay cert dedicada senior aún |

---

## 🗺️ Roadmap (12 meses)

### Fase 1 — Fundamentos (0-3 meses)
- [ ] OWASP LLM Top 10 leído + 3 demos por ítem
- [ ] MITRE ATLAS matrix entendida
- [ ] NIST AI RMF (AI 100-1) leído
- [ ] AWS AIF o Azure AI-900 aprobado

### Fase 2 — Práctica ofensiva-defensiva (3-6 meses)
- [ ] Garak ejecutado contra modelo abierto (Llama, Mistral)
- [ ] PyRIT + promptfoo para test suite de prompts
- [ ] Llama Guard / NeMo Guardrails desplegado en lab
- [ ] 3 jailbreaks reproducidos + writeup defensivo

### Fase 3 — Profesional (6-12 meses)
- [ ] Auditoría de seguridad de un sistema LLM real (open source)
- [ ] Implementar defensas: input sanitization + output filtering + prompt firewalling
- [ ] Charla / blog técnico sobre AI security
- [ ] CSA AI Security Professional empezado

---

## 💰 Salarios en Colombia (USD/mes)

| Nivel | Local 🇨🇴 | Remoto 🌎 | Notas |
|---|---|---|---|
| Junior (0-2 años) | $1,000 - $2,000 | $2,000 - $4,000 | Solo si vienes de ML o seguridad |
| Mid (2-5 años) | $2,500 - $5,000 | $4,500 - $9,000 | Combo ML + sec = scarcity premium |
| Senior (5+ años) | $6,000 - $12,000 | $11,000 - $22,000 | Top mundial — escasez extrema |

> **Tip:** este nicho **dobla salarios** vs roles equivalentes de seguridad clásica. La barrera no es técnica, es **combinar ML + security** — pocos lo hacen.

---

## 🔗 Conexión con otras ramas

- **`ai-red-teamer`** *(03)* → tu primo gemelo ofensivo
- **`ml-security-engineer`** *(03)* → overlap fuerte; algunos lo tratan como sinónimo
- **`prompt-engineer-security`** *(03)* → subdisciplina aplicada
- **`seguridad-aplicaciones`** → si LLMs van en apps web
- **`seguridad-nube`** → AWS Bedrock, Azure OpenAI, GCP Vertex security
- **`cryptographer`** → privacy-preserving ML (FHE, MPC, DP)

---

## 📂 Estructura

```
ia-security/
├── herramientas/    # Garak configs, PyRIT scripts, guardrails
├── recursos/        # OWASP LLM Top 10, ATLAS, NIST AI RMF, papers
├── laboratorios/    # LLM lab + jailbreaks + defensas en compose
└── casos-uso/       # Auditorías de sistemas IA reales (anonimizadas)
```

---

<div align="center">

**[⬅ Volver a Ciberseguridad](../README.md)**

</div>
