<div align="center">

# 📦 AI Supply Chain Security

**Emerging 2024-2026 · ML Models, Datasets & Frameworks Provenance**

*"Hugging Face es el npm de la IA. Y `npm install` no fue famoso por seguro."*

![Tier](https://img.shields.io/badge/tier%20salarial-A-orange) ![Demanda](https://img.shields.io/badge/demanda-creciente-green) ![Entry](https://img.shields.io/badge/entry%20level-medio-yellow)

</div>

---

## 📋 Descripción

Rama **emergente y crítica** que aplica los principios de **Software Supply Chain Security** al ecosistema de IA/ML. Cubre:

- **Model file integrity** — detección de pickle/PyTorch/GGUF backdoors
- **Dataset provenance** — origen, contaminación, sesgos heredados
- **ML framework supply chain** — PyTorch, TensorFlow, transformers (HF)
- **Model registry security** — Hugging Face, Ollama, custom registries
- **MCP server supply chain** *(super-emergente 2025)* — third-party MCP servers
- **AI plugin/extensions** — agente plugins, ChatGPT GPTs, custom integrations
- **Foundation model vendor risk** — Anthropic, OpenAI, Google, Mistral due diligence

Hubo varios incidentes 2024-2025 que validaron la rama: modelos de HF con código malicioso (~100+ flagged en 2024), datasets envenenados (LAION variants), framework CVEs (PyTorch nightly compromise 2022).

---

## 👤 Roles típicos

- **AI Supply Chain Security Engineer** — operación técnica del programa
- **ML Vendor Risk Analyst** — assessments de proveedores AI
- **Model Registry Security Lead** *(big tech)* — Hugging Face, custom regs
- **AI Plugin Auditor** *(emergente)* — review de plugins + GPTs + MCPs
- **AI Provenance Engineer** — cadena de custodia model + dataset

---

## 🛠️ Stack y herramientas

| Categoría | Herramientas |
|---|---|
| **Model scanning** | **ProtectAI ModelScan** · HiddenLayer Model Scanner · Picklescan (HF) · Trivy ML |
| **Provenance / signing** | Sigstore + Cosign · in-toto attestations · Hugging Face Model Cards · ML SBOM (CycloneDX-ML emerging) |
| **SCA para ML** | Snyk · Trivy · Grype · Renovate (con foco ML deps) · pip-audit · safety |
| **Vendor due diligence** | Whistic · OneTrust Vendor · BitSight · Securiti AI · Credo AI Lens |
| **Dataset auditing** | Datasheets for Datasets · Hugging Face Dataset Cards · custom checksums + diff tools |
| **Framework hardening** | torch.load with weights_only=True · safetensors (preferred over .pt) · Onnx (con audit) |
| **MCP security** | MCP server registry checks · audit de tools expuestas · capability scoping |
| **Plugin auditing** | OWASP ChatGPT Plugin Top 10 · OAuth scope review · API allowlists |
| **Frameworks** | SLSA + ML adaptation · NIST AI RMF (Map 4) · OWASP LLM05 (Supply Chain) |

---

## 🎓 Certificaciones / formación

| Nivel | Recurso | Vendor | Costo (USD) | Notas |
|---|---|---|---|---|
| Entry | OWASP LLM05 study | OWASP | $0 | Imprescindible |
| Entry | NIST AI RMF (Map 4) | NIST | $0 | Provenance focus |
| Entry | OpenSSF Best Practices | OpenSSF | $0 | Aplicado a repos ML |
| Mid | CKS (Kubernetes Security) | CNCF | ~$395 | Container/cluster supply chain |
| Mid | Linux Foundation OpenSSF certs | LF/OpenSSF | ~$200-500 | Crece 2025 |
| Mid | CSA AI Security Professional | CSA | ~$400 | 2024 cert |
| Senior | ISO/IEC 42001 LI | PECB | ~$1,200 | AI Management System |

---

## 🗺️ Roadmap (12 meses)

### Fase 1 — Fundamentos (0-3 meses)
- [ ] OWASP LLM05 + NIST AI RMF Map 4 leídos
- [ ] ModelScan + Picklescan ejecutados sobre 10 modelos HF aleatorios
- [ ] Diferencia .pt (pickle) vs .safetensors entendida + aplicada
- [ ] OpenSSF Scorecard contra 5 ML repos (transformers, diffusers, etc.)

### Fase 2 — Aplicación (3-7 meses)
- [ ] Pipeline ML CI con: model scanning + provenance + signing
- [ ] Cosign para firmar modelos + Rekor transparencia
- [ ] AI vendor risk template con 30+ controles (foundation model providers)
- [ ] CSA AI Security empezado

### Fase 3 — Profesional (7-12 meses)
- [ ] Programa supply chain AI completo para empresa modelo
- [ ] Auditoría de un MCP server o ChatGPT GPT popular (responsible disclosure)
- [ ] Blog / charla técnica sobre AI supply chain attacks
- [ ] ISO 42001 LI o CKS aprobada

---

## 💰 Salarios en Colombia (USD/mes)

| Nivel | Local 🇨🇴 | Remoto 🌎 | Notas |
|---|---|---|---|
| Junior (0-2 años) | $1,000 - $1,800 | $1,800 - $3,500 | DevSecOps + ML focus |
| Mid (2-5 años) | $2,500 - $4,800 | $4,500 - $9,000 | ModelScan + Sigstore = palanca |
| Senior (5+ años) | $5,500 - $11,000 | $9,500 - $18,000 | Lead supply chain en AI vendors |

> **Tip:** este es **el cruce ideal** si vienes de DevSecOps clásico y quieres entrar a AI security. Tu skillset de SBOM/Sigstore/Trivy se traduce directo — solo agrega el contexto ML.

---

## 🔗 Conexión con otras ramas

- **`seguridad-cadena-suministro`** *(01)* → tu hermano mayor (sin AI)
- **`ml-security-engineer`** *(03)* → operación pipeline broader
- **`ai-governance-officer`** *(03)* → policy que tú implementas técnicamente
- **`02-SEGURIDAD-INFORMACION/04-devsecops`** → CI/CD para ML
- **`vulnerability-manager`** *(01)* → CVEs en frameworks ML
- **`agentic-security-developer`** *(03)* → MCP servers son supply chain de agents

---

## 📂 Estructura

```
ai-supply-chain-security/
├── herramientas/    # ModelScan configs, Cosign for models, vendor templates
├── recursos/        # NIST AI RMF Map 4, OWASP LLM05, SLSA + ML
├── laboratorios/    # Pipeline ML SLSA Level 3, MCP server hardening
└── casos-uso/       # Análisis: HF malicious models, PyTorch CVEs, dataset audits
```

---

<div align="center">

**[⬅ Volver a AI Agents & Tools](../README.md)**

</div>
