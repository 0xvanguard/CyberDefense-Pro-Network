<div align="center">

# ☁️ Seguridad en la Nube

**CISSP Domain · Cloud Security**

*"En la nube, una mala policy de IAM cuesta más que un 0-day."*

![Tier](https://img.shields.io/badge/tier%20salarial-A-orange) ![Demanda](https://img.shields.io/badge/demanda-explosiva-brightgreen) ![Entry](https://img.shields.io/badge/entry%20level-medio-yellow)

</div>

---

## 📋 Descripción

Rama centrada en proteger workloads y datos en **AWS, Azure y GCP** (más Oracle Cloud y Alibaba en menor medida). Cubre CSPM (Cloud Security Posture Management), CWPP (Cloud Workload Protection), CIEM (Cloud Infrastructure Entitlement Management), IAM avanzado, secret management, container/k8s security y SaaS security (SSPM).

**Es el rol con mayor crecimiento de la última década** — y probablemente la próxima. La presión viene de migraciones masivas, multi-cloud forzado y la complejidad explosiva de IAM en AWS (~10K acciones).

---

## 👤 Roles típicos

- **Cloud Security Engineer** — implementación de controles, policy as code
- **Cloud Security Architect** — diseño multi-cuenta, landing zones, ZT
- **DevSecOps / Platform Security** — embedido con SRE/Platform
- **CSPM Analyst** — operación diaria de Wiz/Prisma/Lacework
- **Kubernetes Security Engineer** *(emergente)* — clusters, mesh, supply chain

---

## 🛠️ Stack y herramientas

| Categoría | Herramientas |
|---|---|
| **CSPM** | Wiz · Prisma Cloud · Lacework · Orca · CrowdStrike Falcon Cloud · Defender for Cloud |
| **CWPP / runtime** | Aqua · Sysdig Secure · Falco · Tetragon · Datadog Cloud Security |
| **CIEM** | SailPoint · Sonrai · CloudKnox (Microsoft) · Wiz CIEM |
| **IaC scanning** | Checkov · tfsec · Terrascan · KICS · Snyk IaC · Trivy |
| **Containers** | Trivy · Grype · Snyk Container · Anchore · Clair · Cosign + Sigstore |
| **K8s** | Kubescape · Kube-bench · OPA Gatekeeper · Kyverno · Falco · Pixie |
| **Native AWS/Azure/GCP** | AWS Security Hub · GuardDuty · Inspector · Azure Defender · GCP SCC |
| **Secrets** | AWS Secrets Mgr · Azure Key Vault · GCP Secret Mgr · HashiCorp Vault |

---

## 🎓 Certificaciones recomendadas

| Nivel | Certificación | Vendor | Costo (USD) | Notas |
|---|---|---|---|---|
| Entry | AWS Cloud Practitioner | AWS | ~$100 | Base obligatoria si no sabes AWS |
| Entry | Microsoft SC-900 | Microsoft | ~$100 | Excelente entry-level |
| Mid | AWS Security Specialty (SCS-C02) | AWS | ~$300 | El estándar de la industria |
| Mid | Azure AZ-500 | Microsoft | ~$165 | Estrella en mercado MS |
| Mid | GCP Pro Cloud Security Engineer | Google | ~$200 | Nicho premium |
| Mid | CKS (Kubernetes Security) | CNCF | ~$395 | Top tier para k8s |
| Senior | CCSP | (ISC)² | ~$600 | Estratégico cross-cloud |
| Senior | HashiCorp Vault Pro | HashiCorp | ~$300 | Secret mgmt avanzado |

---

## 🗺️ Roadmap (12 meses)

### Fase 1 — Fundamentos (0-3 meses)
- [ ] AWS Cloud Practitioner aprobado
- [ ] Cuenta AWS con MFA + organizations + SCPs básicas
- [ ] Lab: Terraform + S3 + IAM con least privilege
- [ ] Checkov o tfsec en pipeline propio

### Fase 2 — Especialización (3-6 meses)
- [ ] AWS Security Specialty o AZ-500 aprobado
- [ ] Implementar landing zone (Control Tower o Bicep blueprint)
- [ ] CSPM gratis o trial: Wiz / Prisma evaluation
- [ ] EKS con Falco + Kubescape + Kyverno

### Fase 3 — Profesional (6-12 meses)
- [ ] Multi-account AWS Organizations con guardrails
- [ ] Threat detection: GuardDuty + Detective + Security Hub correlation
- [ ] CKS aprobado
- [ ] Caso real: hardening cloud para una pyme + reporte CSPM

---

## 💰 Salarios en Colombia (USD/mes)

| Nivel | Local 🇨🇴 | Remoto 🌎 | Notas |
|---|---|---|---|
| Junior (0-2 años) | $800 - $1,500 | $1,500 - $3,000 | Cloud + DevOps reduce barrera |
| Mid (2-5 años) | $2,000 - $4,000 | $4,000 - $7,500 | AWS Specialty es palanca |
| Senior (5+ años) | $5,000 - $9,000 | $9,000 - $16,000 | Architect + multi-cloud = top LATAM |

> **Tip:** este es el nicho con **mayor brecha salarial** en LATAM remoto vs local — apunta a remoto desde el día 1.

---

## 🔗 Conexión con otras ramas

- **`arquitecto-seguridad`** → diseño de landing zones, ZT en cloud
- **`ai-security`** → Bedrock/Vertex/Azure OpenAI security overlap creciente
- **`02-SEGURIDAD-INFORMACION/04-devsecops`** → IaC + pipelines son el día a día
- **`seguridad-cadena-suministro`** → containers, SBOM, firma de imágenes
- **`vulnerability-manager`** → priorización de findings cloud

---

## 📂 Estructura

```
seguridad-nube/
├── herramientas/    # Configs Wiz, Prisma, Checkov, Falco
├── recursos/        # Well-Architected Framework, CIS Benchmarks
├── laboratorios/    # Terraform de cuentas inseguras + remediación
└── casos-uso/       # IAM privilege escalation, S3 público, EKS RBAC
```

---

<div align="center">

**[⬅ Volver a Ciberseguridad](../README.md)**

</div>
