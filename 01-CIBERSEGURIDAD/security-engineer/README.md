<div align="center">

# 🔧 Security Engineer

**NIST NICE · Information Systems Security Engineer**

*"El que construye los controles que el resto del equipo solo dibuja."*

![Tier](https://img.shields.io/badge/tier%20salarial-A-orange) ![Demanda](https://img.shields.io/badge/demanda-muy%20alta-brightgreen) ![Entry](https://img.shields.io/badge/entry%20level-medio-yellow)

</div>

---

## 📋 Descripción

Rol **operativo-técnico** que **implementa** los controles que el architect diseña. Cubre desde despliegue de SIEM/EDR hasta integraciones SOAR, hardening de infraestructura, automatización de respuestas y desarrollo de tooling interno. Es el rol más **versátil** y mejor pagado consistentemente.

A diferencia del SOC analyst (reactivo) o del architect (estratégico), el Security Engineer **escribe código y configuraciones que se ejecutan en producción**. Es el rol más cercano a SRE / DevOps con sombrero de seguridad.

---

## 👤 Roles típicos

- **Security Engineer** — generalista, full-stack defensivo
- **Detection Engineer** — reglas Sigma/SPL/KQL, ML detection
- **Cloud Security Engineer** — IaC + policy as code + CSPM operación
- **SOAR Engineer** — playbooks, integraciones, automatización
- **Platform Security Engineer** *(big tech)* — embedido con SRE/Platform

---

## 🛠️ Stack y herramientas

| Categoría | Herramientas |
|---|---|
| **SIEM / detection** | Splunk · Sentinel · Elastic · Wazuh · Sigma · YARA |
| **EDR / XDR** | CrowdStrike · SentinelOne · Defender · Carbon Black · osquery |
| **SOAR / automation** | Tines · Shuffle · Splunk SOAR · Cortex XSOAR · Sentinel Playbooks · n8n |
| **IaC** | Terraform · Pulumi · Bicep · CloudFormation · Ansible · Salt |
| **Policy as code** | OPA · Sentinel (HashiCorp) · Cedar · Kyverno · Conftest · Checkov |
| **Languages** | Python · Go · PowerShell · Bash · TypeScript |
| **CI/CD** | GitHub Actions · GitLab CI · Jenkins · ArgoCD |
| **Containers** | Docker · K8s · Helm · Trivy · Falco · Kubescape |
| **Secrets / vault** | HashiCorp Vault · AWS Secrets Manager · Doppler · 1Password Secrets |
| **Monitoring** | Grafana · Prometheus · Datadog · Loki · Elastic |

---

## 🎓 Certificaciones recomendadas

| Nivel | Certificación | Vendor | Costo (USD) | Notas |
|---|---|---|---|---|
| Entry | CompTIA Security+ | CompTIA | ~$400 | Base |
| Entry | AWS Cloud Practitioner | AWS | ~$100 | Si vas cloud |
| Mid | AWS Security Specialty | AWS | ~$300 | Estándar |
| Mid | Microsoft SC-200 / SC-300 | Microsoft | ~$165 ea | Defender / Identity |
| Mid | HashiCorp Vault Pro | HashiCorp | ~$300 | Secret mgmt |
| Mid | CKS (Kubernetes Security) | CNCF | ~$395 | K8s |
| Senior | CISSP | (ISC)² | ~$750 | Para mando |
| Senior | OSCP *(opcional, perfil hybrid)* | OffSec | ~$1,649 | Si haces purple |

---

## 🗺️ Roadmap (12 meses)

### Fase 1 — Fundamentos (0-3 meses)
- [ ] Python intermedio (Pydantic, async, typing strict)
- [ ] Terraform en AWS / Azure (IaC con módulos)
- [ ] Pipeline GitHub Actions con secret scan + Trivy + ZAP baseline
- [ ] Security+ aprobado

### Fase 2 — Especialización (3-6 meses)
- [ ] Wazuh / Sentinel custom rules (10 propias)
- [ ] SOAR playbook real: phishing IR end-to-end (Tines / Shuffle)
- [ ] OPA con políticas para K8s + Terraform (Conftest)
- [ ] AWS Sec Specialty o SC-200

### Fase 3 — Profesional (6-12 meses)
- [ ] Tooling propio: CLI o bot que automatiza una tarea recurrente
- [ ] CKS o Vault Pro aprobado
- [ ] Contribución open source a una herramienta de seguridad
- [ ] Charla / blog técnico

---

## 💰 Salarios en Colombia (USD/mes)

| Nivel | Local 🇨🇴 | Remoto 🌎 | Notas |
|---|---|---|---|
| Junior (0-2 años) | $900 - $1,700 | $1,800 - $3,200 | Entrada típica desde DevOps |
| Mid (2-5 años) | $2,200 - $4,300 | $4,000 - $7,500 | AWS Sec Spec es palanca |
| Senior (5+ años) | $5,500 - $10,000 | $9,000 - $16,000 | Detection Engineer remoto top |

> **Tip:** este rol tiene **el mejor balance demanda + salario + entry** de toda ciberseguridad. GitHub público con Terraform + Sigma rules es decisivo.

---

## 🔗 Conexión con otras ramas

- **`arquitecto-seguridad`** → tu paso siguiente (en 5-7 años)
- **`seguridad-nube`** → mucho overlap; muchos engineers son cloud-focused
- **`02-SEGURIDAD-INFORMACION/04-devsecops`** → tu día a día CI/CD
- **`incident-responder`** → automatización SOAR
- **`threat-hunter`** → detection engineering overlap

---

## 📂 Estructura

```
security-engineer/
├── herramientas/    # Terraform modules, OPA policies, SOAR playbooks
├── recursos/        # AWS Well-Architected, OWASP, NIST 800-53
├── laboratorios/    # Lab completo: SIEM + EDR + SOAR en compose
└── casos-uso/       # Automatizaciones reales, post-mortems técnicos
```

---

<div align="center">

**[⬅ Volver a Ciberseguridad](../README.md)**

</div>
