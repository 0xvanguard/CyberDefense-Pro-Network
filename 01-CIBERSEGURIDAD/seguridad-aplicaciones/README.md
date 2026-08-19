<div align="center">

# 🧱 Seguridad de Aplicaciones (AppSec)

**CISSP Domain · Software Development Security**

*"Si tu CI/CD no falla por una vulnerabilidad, tu CI/CD no es seguro."*

![Tier](https://img.shields.io/badge/tier%20salarial-A-orange) ![Demanda](https://img.shields.io/badge/demanda-muy%20alta-brightgreen) ![Entry](https://img.shields.io/badge/entry%20level-medio-yellow)

</div>

---

## 📋 Descripción

Disciplina que **integra seguridad en el SDLC**: desde el threat modeling en diseño hasta el SAST/DAST en CI/CD, pasando por code review, dependencias y runtime protection. Es la rama con mayor crecimiento 2024-2026 por la presión de **supply chain attacks** (SolarWinds, Log4Shell, XZ backdoor).

Cruce natural con DevSecOps. El AppSec Engineer maduro no solo encuentra bugs — diseña **guardrails** que previenen que regresen, automatiza políticas y reduce fricción para los devs.

---

## 👤 Roles típicos

- **AppSec Engineer** — herramientas, code review, threat modeling, secure coding training
- **DevSecOps Engineer** — pipelines de seguridad shift-left
- **Application Security Architect** — políticas, frameworks de desarrollo seguro
- **Product Security Engineer** *(big tech)* — alineado a un producto específico
- **Bug Bounty Hunter especializado** *(freelance)* — overlap con esta rama

---

## 🛠️ Stack y herramientas

| Categoría | Herramientas |
|---|---|
| **SAST** | Semgrep · SonarQube · Checkmarx · Fortify · CodeQL · Bandit (Python) |
| **DAST** | OWASP ZAP · Burp Suite Pro · Nuclei · Acunetix |
| **SCA / deps** | Snyk · Dependabot · Trivy · Grype · OWASP Dependency-Check · Renovate |
| **Secret scanning** | TruffleHog · GitLeaks · detect-secrets · GitHub Advanced Security |
| **IAST / RASP** | Contrast Security · Datadog ASM · HDIV |
| **Threat Modeling** | Microsoft Threat Modeling Tool · OWASP Threat Dragon · pytm |
| **Container & K8s** | Trivy · Kubescape · Falco · OPA Gatekeeper · Kyverno |
| **Pruebas manuales** | Burp Suite · Caido · Postman + custom scripts |

---

## 🎓 Certificaciones recomendadas

| Nivel | Certificación | Vendor | Costo (USD) | Notas |
|---|---|---|---|---|
| Entry | OWASP TOP 10 (gratis) | OWASP | $0 | Lectura obligatoria |
| Entry | PortSwigger Web Security Academy | PortSwigger | $0 | Práctica gratuita imprescindible |
| Mid | eWPT / eWPTXv2 | INE Security | ~$400-600 | Web pentest aplicado |
| Mid | Burp Suite Certified Practitioner | PortSwigger | ~$100 | Examen práctico |
| Mid | GIAC GWEB | SANS | ~$2,500+ | Defensiva web |
| Senior | OSWE | OffSec | ~$1,649 | Top tier en code review ofensivo |
| Senior | CSSLP | (ISC)² | ~$700 | Más estratégico que técnico |

---

## 🗺️ Roadmap (12 meses)

### Fase 1 — Fundamentos (0-3 meses)
- [ ] OWASP Top 10 (Web · API · LLM) leído y entendido
- [ ] PortSwigger Academy: completar Apprentice (gratis)
- [ ] Semgrep + Bandit en repos propios
- [ ] Threat modeling de una app conocida con STRIDE

### Fase 2 — Especialización (3-6 meses)
- [ ] Burp Suite Pro: Repeater, Intruder, Logger++, Autorize
- [ ] Pipeline GitHub Actions con: Semgrep + TruffleHog + Trivy + ZAP baseline
- [ ] Code review ofensivo de un proyecto open source (reportar issues)
- [ ] eWPT o BSCP aprobado

### Fase 3 — Profesional (6-12 meses)
- [ ] OSWE prep: white-box exploitation
- [ ] Diseñar y publicar un guardrail (ejemplo: detector custom de Semgrep)
- [ ] Threat model real para un cliente / proyecto interno
- [ ] Charla técnica o blog sobre un hallazgo

---

## 💰 Salarios en Colombia (USD/mes)

| Nivel | Local 🇨🇴 | Remoto 🌎 | Notas |
|---|---|---|---|
| Junior (0-2 años) | $800 - $1,500 | $1,500 - $2,800 | Devs con interés en seguridad |
| Mid (2-5 años) | $2,000 - $4,000 | $3,500 - $6,500 | Startups + scaleups pagan bien |
| Senior (5+ años) | $5,000 - $9,000 | $8,000 - $14,000 | Big tech remoto rompe techos |

> **Tip:** demuestra con repos públicos (CTFs, write-ups, SAST rules custom) — pesa más que la cert.

---

## 🔗 Conexión con otras ramas

- **`pentester-red-team`** → AppSec es el lado defensivo del web pentest
- **`vulnerability-manager`** → tu output (CVEs, hallazgos) entra a su pipeline
- **`bug-bounty-hunting`** → mismo skillset técnico, modelo distinto
- **`02-SEGURIDAD-INFORMACION/04-devsecops`** → CI/CD security es tu hábitat
- **`seguridad-cadena-suministro`** → SBOM, SCA, firma de artefactos

---

## 📂 Estructura

```
seguridad-aplicaciones/
├── herramientas/    # Configs de Semgrep, ZAP baseline, Trivy
├── recursos/        # OWASP cheatsheets, threat model templates
├── laboratorios/    # Apps vulnerables (Juice Shop, DVWA, WebGoat)
└── casos-uso/       # CVEs reales reproducidos + writeups
```

---

<div align="center">

**[⬅ Volver a Ciberseguridad](../README.md)**

</div>
