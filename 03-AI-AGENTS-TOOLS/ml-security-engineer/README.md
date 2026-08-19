<div align="center">

# 🧠 ML Security Engineer

**Emerging 2024-2026 · ML Pipeline & Model Security**

*"Modelos son código. Datos son input no confiable. MLOps debería ser DevSecOps."*

![Tier](https://img.shields.io/badge/tier%20salarial-S-purple) ![Demanda](https://img.shields.io/badge/demanda-creciente-green) ![Entry](https://img.shields.io/badge/entry%20level-medio--alto-yellow)

</div>

---

## 📋 Descripción

Rol **defensivo-técnico** que **protege el ML pipeline end-to-end**: training data, training infrastructure, model artifacts, deployment, inference APIs. Cubre amenazas que las stack de seguridad clásicas no ven:

- **Data poisoning** (training time)
- **Model file backdoors** (pickle/GGUF malicioso → RCE)
- **Model serialization attacks** (Pickle, joblib)
- **Model artifact integrity** (firmas, SBOM ML)
- **Inference-time abuse** (DoS por prompt larga, costo runaway)
- **Supply chain ML** (modelos de Hugging Face, datasets sin verificar)

Diferencia con `ai-red-teamer`:
- **AI Red Teamer (ofensiva)** → ataca modelos para encontrar fallas
- **ML Security Engineer (defensiva)** → protege el ciclo MLOps + modelos en producción

---

## 👤 Roles típicos

- **ML Security Engineer** — generalista MLOps + sec
- **MLOps Security Engineer** — embedido en plataforma ML
- **Model Risk Engineer** — banca, healthcare (regulatorio)
- **AI Platform Security** *(big tech)* — Bedrock/Vertex/OpenAI infra
- **Adversarial ML Defender** — robustez vs adversarial inputs

---

## 🛠️ Stack y herramientas

| Categoría | Herramientas |
|---|---|
| **Model scanning** | **ProtectAI ModelScan** · HiddenLayer Model Scanner · Trivy ML · Picklescan (HF) |
| **Adversarial defenses** | ART defenses (IBM) · adversarial training · randomized smoothing |
| **Model signing / SBOM** | Sigstore + Cosign for models · ML SBOM specs (CycloneDX-ML) · OpenSSF |
| **MLOps platforms** | MLflow · Kubeflow · Weights & Biases · DVC (versioning) |
| **Inference servers** | Triton (NVIDIA) · TorchServe · TGI (HF) · vLLM · Ollama |
| **Cloud ML** | AWS SageMaker (security features) · Azure ML · GCP Vertex AI · Databricks |
| **Robustness / eval** | Counterfit (Microsoft) · ART · Foolbox · CleverHans |
| **Privacy** | Opacus · TensorFlow Privacy · OpenDP (overlap con privacy-engineer) |
| **Languages** | Python · Go · Rust (perf-critical) |
| **Frameworks** | NIST AI RMF · MITRE ATLAS · OWASP ML Top 10 · ISO/IEC 42001 |

---

## 🎓 Certificaciones / formación

| Nivel | Certificación / curso | Vendor | Costo (USD) | Notas |
|---|---|---|---|---|
| Entry | AWS AI Practitioner (AIF-C01) | AWS | ~$100 | Base AI cloud |
| Entry | Coursera Machine Learning (Andrew Ng) | DeepLearning.AI | ~$50 | Imprescindible |
| Entry | OWASP ML Security Top 10 | OWASP | $0 | Lectura obligatoria |
| Mid | NIST AI RMF self-study | NIST | $0 | Government framework |
| Mid | DeepLearning.AI MLOps Specialization | Coursera | ~$50/mes | MLOps base |
| Mid | CSA AI Security Professional | CSA | ~$400 | 2024 cert |
| Mid | ISO/IEC 42001 Lead Implementer | PECB | ~$1,200 | AI Management System |
| Senior | Maestría ML + security | varios | $$$ | Para investigación |

---

## 🗺️ Roadmap (12 meses)

### Fase 1 — Fundamentos (0-3 meses)
- [ ] Andrew Ng's ML Specialization completa
- [ ] OWASP ML Top 10 + MITRE ATLAS estudiados
- [ ] Python: PyTorch / TensorFlow básico
- [ ] AWS AIF aprobado

### Fase 2 — Aplicación defensiva (3-7 meses)
- [ ] ModelScan + Picklescan contra modelos de Hugging Face
- [ ] Adversarial training con ART en modelo CV simple
- [ ] MLflow + DVC con políticas de signing
- [ ] CSA AI Security empezado

### Fase 3 — Profesional (7-12 meses)
- [ ] Pipeline MLOps seguro: ingest → train → eval → sign → deploy → monitor
- [ ] Caso real: hardening de un servicio LLM (rate limit, input cap, output filtering)
- [ ] Contribución a ProtectAI / HiddenLayer / OWASP ML
- [ ] ISO 42001 LI o CSA AI

---

## 💰 Salarios en Colombia (USD/mes)

| Nivel | Local 🇨🇴 | Remoto 🌎 | Notas |
|---|---|---|---|
| Junior (0-2 años) | $1,200 - $2,500 | $2,500 - $4,500 | ML eng + security background |
| Mid (2-5 años) | $3,000 - $6,000 | $5,500 - $11,000 | MLOps + sec hands-on |
| Senior (5+ años) | $6,500 - $13,000 | $11,000 - $22,000 | Big tech + AI platforms top |

> **Tip:** Hugging Face, Anthropic, OpenAI, Cohere, Mistral, NVIDIA tienen equipos remotos abiertos a LATAM. Skill scarcity = premium.

---

## 🔗 Conexión con otras ramas

- **`ai-red-teamer`** *(03)* → tu primo ofensivo (purple team)
- **`ia-security`** *(01)* → defensiva broader, tú eres el specialty MLOps
- **`seguridad-cadena-suministro`** *(01)* → ML supply chain (modelos, datasets)
- **`privacy-engineer`** *(02)* → DP en training pipelines
- **`security-engineer`** *(01)* → MLOps es subset moderno de DevSecOps
- **`ai-governance-officer`** *(03)* → tú implementas, ellos gobiernan

---

## 📂 Estructura

```
ml-security-engineer/
├── herramientas/    # ModelScan configs, ART notebooks, MLflow policies
├── recursos/        # OWASP ML Top 10, ATLAS, NIST AI RMF, papers
├── laboratorios/    # Pipelines MLOps seguros, adversarial training labs
└── casos-uso/       # Hardenings reales, model audits, post-mortems ML
```

---

<div align="center">

**[⬅ Volver a AI Agents & Tools](../README.md)**

</div>
