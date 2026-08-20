# ☁️ Seguridad Cloud (AWS / Azure / GCP) — Guía profesional

> **Nivel:** Intermedio → Avanzado
>
> Objetivo: entender los controles de seguridad de los 3 grandes proveedores y **aplicarlos** (IAM, storage, red, logging, detección). La nube no es "el datacenter de otro": tiene su propio modelo de seguridad.

---

## Índice

1. [El modelo de responsabilidad compartida](#1-el-modelo-de-responsabilidad-compartida)
2. [IAM: least privilege en los 3 providers](#2-iam-least-privilege-en-los-3-providers)
3. [Storage: buckets/blobs públicos](#3-storage-bucketsblobs-públicos)
4. [Red: security groups / NSG / firewall](#4-red-security-groups--nsg--firewall)
5. [Logging y detección](#5-logging-y-detección)
6. [CSPM y IaC scanning](#6-cspm-y-iac-scanning)
7. [Referencias](#7-referencias)

---

## 1. El modelo de responsabilidad compartida

| Capa | Cloud provider | **Tú (cliente)** |
|---|---|---|
| Físico, red del datacenter | ✅ | — |
| Hipervisor, storage, servicios | ✅ | — |
| **Configuración, IAM, datos** | — | ✅ |
| **Apps, código, secretos** | — | ✅ |

> **La mayoría de brechas cloud NO son del proveedor:** son buckets S3 públicos, IAM sobre-permisivo y secretos filtrados. **Tu responsabilidad es la configuración.**

---

## 2. IAM: least privilege en los 3 providers

### 2.1 AWS (IAM policies)

```json
// Política de least privilege: solo leer un bucket concreto
{
  "Version": "2012-10-17",
  "Statement": [
    {
      "Effect": "Allow",
      "Action": ["s3:GetObject"],
      "Resource": "arn:aws:s3:::mi-bucket/*"
    }
  ]
}
```

Buenas prácticas AWS:
- Usa **roles** (no llaves de larga vida) → OIDC desde CI.
- **MFA** obligatorio para cuentas humanas.
- **Organizations + SCP** (Service Control Policies) para guardrails globales.
- Audita con **IAM Access Analyzer**.

### 2.2 Azure (RBAC + roles)

```bash
# Asignar rol de "Reader" a un usuario solo sobre un resource group
az role assignment create \
  --assignee user@corp.com \
  --role "Reader" \
  --scope /subscriptions/<sub>/resourceGroups/mi-rg
```

- Usa **Managed Identities** (no connection strings).
- **PIM** (Privileged Identity Management) para acceso temporal/just-in-time.

### 2.3 GCP (IAM bindings)

```bash
# Otorgar rol mínimo sobre un proyecto
gcloud projects add-iam-policy-binding mi-proyecto \
  --member="user:user@corp.com" \
  --role="roles/storage.objectViewer"
```

- Principio: **roles predefinidos** antes que `roles/editor`/`roles/owner`.
- **Workload Identity** para cargas (no service account keys).

---

## 3. Storage: buckets/blobs públicos

El fallo #1 de la nube: **almacenamiento expuesto al público**.

### 3.1 AWS S3

```bash
# ¿El bucket es público?
aws s3api get-bucket-acl --bucket mi-bucket

# Bloquear acceso público a nivel de cuenta
aws s3control put-public-access-block \
  --account-id 123456789012 \
  --public-access-block-configuration BlockPublicAcls=true,IgnorePublicAcls=true,BlockPublicPolicy=true,RestrictPublicBuckets=true
```

### 3.2 Azure Blob

```bash
# Ver si el storage permite acceso público anónimo
az storage account show --name mistorage --query allowBlobPublicAccess

# Deshabilitarlo
az storage account update --name mistorage --allow-blob-public-access false
```

### 3.3 GCP GCS

```bash
# Ver IAM público (allUsers/allAuthenticatedUsers)
gsutil iam get gs://mi-bucket

# Quitar acceso público
gsutil iam ch -d allUsers gs://mi-bucket
```

---

## 4. Red: security groups / NSG / firewall

| Provider | Control | Nota |
|---|---|---|
| AWS | **Security Groups** (por instancia) + NACLs | SGs son stateful, allow por defecto |
| Azure | **NSG** (Network Security Groups) | Asociadas a subnets/NICs |
| GCP | **VPC Firewall Rules** | Default allow dentro de VPC |

### Ejemplo AWS (bloquear todo, permitir solo 443)

```bash
aws ec2 authorize-security-group-ingress \
  --group-id sg-12345 \
  --protocol tcp --port 443 --cidr 0.0.0.0/0
```

> **Regla:** nunca `0.0.0.0/0` para SSH/RDP/DB. Restringe a IPs/VPN conocidas.

---

## 5. Logging y detección

### 5.1 Logs de auditoría (imprescindibles)

| Provider | Log principal | Qué registra |
|---|---|---|
| AWS | **CloudTrail** | Toda llamada a la API |
| Azure | **Activity Log** | Operaciones de gestión |
| GCP | **Cloud Audit Logs** | Admin + Data Access |

### 5.2 Detección de amenazas nativa

| Provider | Servicio | Detecta |
|---|---|---|
| AWS | **GuardDuty** | C2, crypto mining, IAM anómalo, port scans |
| Azure | **Defender for Cloud** | Alertas de seguridad, postura |
| GCP | **Security Command Center** | Findings, misconfigs, threats |

```bash
# AWS: habilitar GuardDuty
aws guardduty create-detector --enable

# GCP: ver findings del SCC
gcloud scc findings list --organization=<org-id>
```

### 5.3 Centralizar y correlacionar

- AWS: **Security Hub** (agrega GuardDuty + Inspector + findings).
- Azure: **Sentinel** (SIEM nativo).
- GCP: **Chronicle** (SIEM).

---

## 6. CSPM y IaC scanning

### 6.1 CSPM (postura de seguridad)

| Provider nativo | Third-party |
|---|---|
| AWS Config / Security Hub | Wiz, Prisma Cloud, Lacework, Orca |

El CSPM escanea continuamente misconfiguraciones (bucket público, MFA ausente, IAM sobre-permisivo) y las prioriza.

### 6.2 Escanear IaC antes de desplegar (shift-left)

```bash
# Checkov (multi-cloud)
checkov -d ./terraform

# tfsec (Terraform)
tfsec ./terraform

# Trivy también escanea IaC
trivy config ./terraform
```

Ejemplo de hallazgo:

```hcl
# ❌ Checkov detecta: bucket público
resource "aws_s3_bucket" "b" {
  bucket = "mi-bucket"
  acl    = "public-read"   # ← bloqueado por Checkov
}
```

---

## 7. Referencias

- [AWS Well-Architected — Security Pillar](https://aws.amazon.com/architecture/well-architected/)
- [Microsoft Cloud Security Benchmark](https://learn.microsoft.com/en-us/security/benchmark/azure/)
- [GCP Security Best Practices](https://cloud.google.com/security/best-practices)
- [CIS Benchmarks (AWS/Azure/GCP)](https://www.cisecurity.org/cis-benchmarks)
- [Checkov](https://www.checkov.io/) · [tfsec](https://github.com/aquasecurity/tfsec)

---

**[⬅ Volver al README de Seguridad en la Nube](../README.md)** · **[→ DevSecOps](../../../02-SEGURIDAD-INFORMACION/04-devsecops/)**
