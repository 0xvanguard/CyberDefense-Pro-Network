---
title: "Seguridad en la nube: AWS, Azure y GCP desde cero"
description: "Errores comunes en cloud, configuración segura y mejores prácticas para AWS, Azure y GCP"
author: Equipo CDPN
date: 2026-09-14
tags: [cloud, aws, azure, gcp, devsecops]
readingTime: 6 min
---

<script setup>
import { useData } from 'vitepress'
const { frontmatter } = useData()
</script>

<style>
.article-meta { display:flex; gap:0.8rem; flex-wrap:wrap; margin:0.8rem 0 1.5rem; font-size:0.85rem; color:var(--vp-c-text-3); }
.article-meta span { background:var(--vp-c-default-soft); padding:2px 10px; border-radius:6px; }
.article-meta .accent { background:var(--vp-c-brand-soft); color:var(--vp-c-brand-1); }
</style>

# Seguridad en la nube: AWS, Azure y GCP desde cero

<div class="article-meta">
  <span class="accent">📝 Equipo CDPN</span>
  <span>📅 14 Septiembre 2026</span>
  <span>📖 6 min de lectura</span>
  <span>🏷️ Cloud</span>
  <span>🏷️ AWS</span>
</div>

## ¿Por qué Cloud Security?

El **95% de las cargas de trabajo** nuevas se despliegan en la nube. Los errores de configuración en cloud son la **causa #1 de breaches** en la actualidad.

### Estadísticas que importan

| Dato | Cifra |
|------|-------|
| Breaches por mala config en cloud | **15% del total** |
| Datos expuestos en S3 buckets | **33 billones de registros** (2024) |
| Coste promedio de breach en cloud | **$5.1 millones** |
| Empresas con acceso root en cloud | **40%** |

## Los 3 proveedores principales

| Proveedor | Servicio principal | Certificación | Cuota mercado |
|-----------|-------------------|---------------|---------------|
| **AWS** | EC2, S3, Lambda | AWS Security Specialty | 31% |
| **Azure** | VMs, Blob Storage | AZ-500 | 25% |
| **GCP** | Compute Engine, GCS | Professional Cloud Security | 11% |

## Top 10 errores de seguridad en cloud

### 1. 🪣 S3 Buckets públicos

```bash
# MAL ❌ — Cualquiera puede acceder
aws s3api put-bucket-policy --bucket mi-bucket --policy '{
  "Statement": [{"Effect": "Allow", "Principal": "*", "Action": "s3:GetObject", "Resource": "arn:aws:s3:::mi-bucket/*"}]
}'

# BIEN ✅ — Solo usuarios autenticados
aws s3api put-bucket-policy --bucket mi-bucket --policy '{
  "Statement": [{"Effect": "Deny", "Principal": "*", "Action": "s3:*", "Resource": "arn:aws:s3:::mi-bucket/*", "Condition": {"Bool": {"aws:SecureTransport": "false"}}}]
}'
```

### 2. 🔑 Access Keys expuestas

```bash
# MAL ❌ — Hardcoded en código
AWS_ACCESS_KEY=AKIAIOSFODNN7EXAMPLE
AWS_SECRET_KEY=wJalrXUtnFEMI/K7MDENG/bPxRfiCYEXAMPLEKEY

# BIEN ✅ — Variables de entorno o IAM roles
export AWS_PROFILE=production
# O mejor: usar IAM roles en EC2/ECS
```

### 3. 👤 IAM overly permissive

```json
// MAL ❌ — Admin total para todos
{
  "Effect": "Allow",
  "Action": "*",
  "Resource": "*"
}

// BIEN ✅ — Least privilege
{
  "Effect": "Allow",
  "Action": ["s3:GetObject", "s3:PutObject"],
  "Resource": "arn:aws:s3:::mi-bucket/*"
}
```

### 4. 🌐 Security Groups abiertos

```bash
# MAL ❌ — SSH abierto al mundo
aws ec2 authorize-security-group-ingress \
  --group-id sg-12345 \
  --protocol tcp --port 22 --cidr 0.0.0.0/0

# BIEN ✅ — Solo tu IP
aws ec2 authorize-security-group-ingress \
  --group-id sg-12345 \
  --protocol tcp --port 22 --cidr 203.0.113.50/32
```

### 5. 🔒 Sin cifrado en reposo

```bash
# AWS S3 — Habilitar cifrado
aws s3api put-bucket-encryption --bucket mi-bucket --server-side-encryption-configuration '{
  "Rules": [{"ApplyServerSideEncryptionByDefault": {"SSEAlgorithm": "aws:kms"}}]
}'

# Azure Blob Storage
az storage account update --name mystorageaccount --encryption-services blob --resource-group myRG
```

### 6. 📝 Sin logging habilitado

```bash
# AWS CloudTrail — Registrar todas las llamadas API
aws cloudtrail create-trail --name security-trail --s3-bucket-name logs-bucket
aws cloudtrail start-logging --name security-trail

# Azure Activity Log
az monitor activity-log alert create --name "AllErrors" --resource-group myRG
```

### 7. 🚫 Sin MFA en cuentas root

```bash
# Verificar MFA
aws iam get-account-summary | grep "AccountMFAEnabled"
# Si dice 0, MFA no está habilitado

# Habilitar MFA
aws iam enable-mfa-device --user-name root --serial-number arn:aws:iam::123456789:mfa/root --auth-code-1 123456 --auth-code-2 789012
```

### 8. 🐳 Imágenes Docker sin escanear

```bash
# Escanear imagen antes de desplegar
docker scout cves my-app:latest

# AWS ECR scanning
aws ecr start-image-scan --repository-name my-app --image-id imageTag=latest
```

### 9. 🔑 Secrets en código

```yaml
# MAL ❌ — Secrets en docker-compose
environment:
  - DB_PASSWORD=supersecret123

# BIEN ✅ — Usar secrets manager
# AWS Secrets Manager
aws secretsmanager get-secret-value --secret-id prod/db/password

# Docker secrets
secrets:
  db_password:
    file: ./secrets/db_password.txt
```

### 10. 📊 Sin monitoreo

```bash
# AWS GuardDuty — Detección de amenazas
aws guardduty create-detector --enable

# AWS Config — Compliance checking
aws configservice put-configuration-recorder --configuration-recorder name= recorder-role-arn=arn:aws:iam::123:role/config-role

# Azure Defender
az security pricing create --name VirtualMachines --tier Standard
```

## Checklist de seguridad cloud

```
☐ Cuentas root con MFA habilitado
☐ IAM roles con least privilege
☐ Storage buckets NO públicos
☐ Cifrado en reposo y tránsito habilitado
☐ Logging (CloudTrail/Azure Monitor) activo
☐ Security Groups restringidos
☐ Secrets en Key Vault/Secrets Manager
☐ Imágenes Docker escaneadas
☐ Backup automático habilitado
☐ Monitoreo y alertas configurados
```

## Certificaciones recomendadas

| Certificación | Proveedor | Nivel | Valor |
|--------------|-----------|-------|-------|
| **AWS Security Specialty** | Amazon | Avanzado | ⭐⭐⭐⭐⭐ |
| **AZ-500** | Microsoft | Intermedio | ⭐⭐⭐⭐ |
| **Google Cloud Security** | Google | Intermedio | ⭐⭐⭐⭐ |
| **CCSK** | CSA | Fundamentos | ⭐⭐⭐ |
| **CCSP** | (ISC)² | Avanzado | ⭐⭐⭐⭐⭐ |

## Conclusión

Cloud security no es opcional — es **crítica**. Un S3 bucket público puede exponer millones de registros en minutos. La buena noticia: los errores más comunes son fáciles de prevenir con configuración correcta y herramientas de monitoreo.

---

*Artículo publicado en el Blog CDPN — Semana 16*
