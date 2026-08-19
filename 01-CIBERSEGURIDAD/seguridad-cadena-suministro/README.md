<div align="center">

# 📦 Seguridad de la Cadena de Suministro

**Emerging 2024-2026 · Software Supply Chain Security**

*"SolarWinds · Log4Shell · XZ backdoor · 3CX. La próxima va a tu CI/CD."*

![Tier](https://img.shields.io/badge/tier%20salarial-A-orange) ![Demanda](https://img.shields.io/badge/demanda-explosiva-brightgreen) ![Entry](https://img.shields.io/badge/entry%20level-medio-yellow)

</div>

---

## 📋 Descripción

Rama emergente que **protege todo lo que va de los developers a producción**: dependencias open source (npm, PyPI, Maven), imágenes Docker, artefactos firmados, build systems (CI/CD), y proveedores de software (vendor risk). Aceleración masiva tras incidentes como SolarWinds (2020), Log4Shell (2021), 3CX (2023), XZ backdoor (2024) y ataques continuos a npm/PyPI typosquatting.

Frameworks centrales: **SLSA** (Supply chain Levels for Software Artifacts), **SBOM** (CycloneDX, SPDX), **in-toto**, **Sigstore** (Cosign + Rekor + Fulcio), y normativas como **EO 14028** (US), **CRA** (UE Cyber Resilience Act, 2024).

---

## 👤 Roles típicos

- **Supply Chain Security Engineer** — SBOM, signing, SCA en pipelines
- **DevSecOps Engineer (SC focus)** — pipeline gates + provenance
- **Vendor Risk Analyst** — third-party assessment, due diligence
- **Open Source Security Researcher** — auditar deps populares (OpenSSF Alpha-Omega)
- **Software Bill of Materials (SBOM) Lead** *(emergente)* — gobierno y privado

---

## 🛠️ Stack y herramientas

| Categoría | Herramientas |
|---|---|
| **SBOM gen / consume** | Syft (Anchore) · CycloneDX CLI · Trivy SBOM · Microsoft SBOM tool · sbom-tool |
| **SCA / dep scanning** | Snyk · Dependabot · Renovate · OWASP Dep-Check · Trivy · Grype |
| **Signing / provenance** | Cosign + Sigstore · in-toto · SLSA + slsa-verifier · GitHub Attestations |
| **Build systems** | GitHub Actions · GitLab CI · Tekton · Buildkite · Bazel + rules_oci |
| **Image registries** | ECR / GAR / ACR (con scanning) · Harbor + Notary |
| **Secret detection** | TruffleHog · GitLeaks · detect-secrets · GitHub Secret Scanning |
| **License compliance** | FOSSA · Snyk License · ScanCode · Black Duck |
| **OSS posture** | OpenSSF Scorecard · deps.dev · Sonatype OSS Index · Socket.dev |
| **Vendor risk** | Whistic · BitSight · SecurityScorecard · UpGuard |

---

## 🎓 Certificaciones recomendadas

| Nivel | Certificación | Vendor | Costo (USD) | Notas |
|---|---|---|---|---|
| Entry | OpenSSF Best Practices badge | OpenSSF | $0 | Aplica a tus repos |
| Entry | GitHub Advanced Security | GitHub | corporate | Si tu org la usa |
| Mid | CKS (K8s Security) | CNCF | ~$395 | Container/cluster supply chain |
| Mid | Snyk certs (free) | Snyk | $0 | Producto-específico |
| Mid | Linux Foundation OpenSSF Certs | LF/OpenSSF | ~$200-500 | Crece este 2025 |
| Senior | CCSP | (ISC)² | ~$600 | Cloud + supply chain mapping |
| Senior | CISSP-ISSEP | (ISC)² | ~$700 | Security engineering |

---

## 🗺️ Roadmap (12 meses)

### Fase 1 — Fundamentos (0-3 meses)
- [ ] Lectura: SLSA framework + EO 14028 + EU CRA highlights
- [ ] Generar SBOM (Syft) para 3 imágenes Docker
- [ ] OpenSSF Scorecard contra 5 repos open source
- [ ] Pipeline GitHub Actions con: TruffleHog + Trivy + Dependabot

### Fase 2 — Aplicación (3-6 meses)
- [ ] Cosign + Sigstore para firmar imágenes
- [ ] in-toto attestations en build (provenance)
- [ ] Integrar SBOM en VM (Defectdojo / Dependency-Track)
- [ ] CKS o Snyk certs

### Fase 3 — Profesional (6-12 meses)
- [ ] SLSA Level 3 alcanzado en un proyecto propio
- [ ] Vendor risk program para pyme (template completo)
- [ ] Auditoría a una dep popular open source (PR de hardening)
- [ ] Charla técnica o blog sobre supply chain security

---

## 💰 Salarios en Colombia (USD/mes)

| Nivel | Local 🇨🇴 | Remoto 🌎 | Notas |
|---|---|---|---|
| Junior (0-2 años) | $900 - $1,700 | $1,800 - $3,200 | DevSecOps con SC focus |
| Mid (2-5 años) | $2,200 - $4,300 | $4,000 - $7,500 | SBOM + Sigstore = palanca |
| Senior (5+ años) | $5,500 - $10,000 | $9,000 - $16,000 | Lead supply chain en big tech |

> **Tip:** este es el nicho **con más demanda regulatoria** (EU CRA, EO 14028). Empresas que venden a US Federal o EU **deben tener** SBOM. Posicionarte aquí en 2025-2026 es timing perfecto.

---

## 🔗 Conexión con otras ramas

- **`seguridad-aplicaciones`** → AppSec con foco supply chain
- **`02-SEGURIDAD-INFORMACION/04-devsecops`** → tu hábitat de pipelines
- **`seguridad-nube`** → containers + IaC + provenance
- **`vulnerability-manager`** → SBOM ↔ CVE matching
- **`grc-compliance`** → CRA, EO 14028, SOC 2 supply chain controls
- **`cryptographer`** → firmas digitales + Sigstore certificates

---

## 📂 Estructura

```
seguridad-cadena-suministro/
├── herramientas/    # Cosign configs, Syft setups, Scorecard configs
├── recursos/        # SLSA, SBOM specs (CycloneDX/SPDX), regulación
├── laboratorios/    # Pipeline ejemplo SLSA Level 3
└── casos-uso/       # Análisis: SolarWinds, Log4Shell, XZ, 3CX
```

---

<div align="center">

**[⬅ Volver a Ciberseguridad](../README.md)**

</div>
