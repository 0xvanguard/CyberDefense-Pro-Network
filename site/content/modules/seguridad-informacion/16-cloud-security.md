---
title: "16 — Cloud Security"
description: "16 — Cloud Security"
---

# 16 — Cloud Security

> 🎯 **Objetivo:** dominar la seguridad en la nube: cómo proteger, atacar y defender infraestructuras cloud en AWS, Azure y GCP.

## 1. Fundamentos de Cloud Security

### 1.1 ¿Qué es Cloud Security?

Cloud Security es el conjunto de políticas, tecnologías y controles que protegen datos, aplicaciones e infraestructuras en la nube.

```
┌─────────────────────────────────────────────────────────┐
│               MODELOS DE SERVICIO CLOUD                 │
├─────────────────────────────────────────────────────────┤
│                                                         │
│   SaaS (Software as a Service)                         │
│   ├── Gmail, Office 365, Salesforce                    │
│   ├── El proveedor gestiona TODO                       │
│   └── Tú solo usas la aplicación                       │
│                                                         │
│   PaaS (Platform as a Service)                         │
│   ├── Heroku, Google App Engine                        │
│   ├── El proveedor gestiona SO + Runtime               │
│   └── Tú despliegas tu código                          │
│                                                         │
│   IaaS (Infrastructure as a Service)                   │
│   ├── AWS EC2, Azure VMs, GCP Compute                  │
│   ├── El proveedor gestiona Hardware                   │
│   └── Tú gestionas SO, apps, datos                     │
│                                                         │
│   CaaS (Container as a Service)                        │
│   ├── AWS ECS, Azure AKS, GCP GKE                     │
│   ├── Orquestación de contenedores                     │
│   └── Tú gestionas contenedores y apps                 │
│                                                         │
└─────────────────────────────────────────────────────────┘
```

### 1.2 Proveedores Principales

| Proveedor | Servicios Principales | Certificación |
|-----------|----------------------|---------------|
| **AWS** | EC2, S3, IAM, Lambda, RDS | AWS Security Specialty |
| **Azure** | VMs, AD, Sentinel, Functions | AZ-500 |
| **GCP** | Compute, IAM, Chronicle, Functions | Professional Cloud Security |

### 1.3 Modelo de Responsabilidad Compartida

```
┌─────────────────────────────────────────────────────────┐
│           RESPONSABILIDAD COMPARTIDA                    │
├─────────────────────────────────────────────────────────┤
│                                                         │
│   PROVEEDOR CLOUD              CLIENTE                  │
│   (AWS/Azure/GCP)             (Tú)                     │
│   ─────────────────           ─────────────            │
│   ✓ Physical security         ✓ Datos                  │
│   ✓ Network infra             ✓ Identity & Access      │
│   ✓ Hypervisor                ✓ Application security   │
│   ✓ Hardware                  ✓ OS patching            │
│   ✓ Power/Cooling             ✓ Network config         │
│                                ✓ Encryption            │
│                                ✓ Firewall rules        │
│                                                         │
│   IaaS: Más responsabilidad para el cliente            │
│   SaaS: Más responsabilidad para el proveedor          │
│                                                         │
└─────────────────────────────────────────────────────────┘
```

## 2. Seguridad en AWS

### 2.1 IAM (Identity & Access Management)

```bash
# === GESTIÓN DE USUARIOS ===
# Crear usuario
aws iam create-user --user-name pentester

# Crear acceso programático
aws iam create-access-key --user-name pentester

# === POLÍTICAS ===
# Política de solo lectura
aws iam create-policy \
  --policy-name ReadOnlyAccess \
  --policy-document '{
    "Version": "2012-10-17",
    "Statement": [{
      "Effect": "Allow",
      "Action": ["s3:GetObject", "s3:ListBucket"],
      "Resource": "*"
    }]
  }'

# Asignar política a usuario
aws iam attach-user-policy \
  --user-name pentester \
  --policy-arn arn:aws:iam::policy/ReadOnlyAccess

# === ROLES ===
# Crear rol para EC2
aws iam create-role \
  --role-name EC2-S3-Access \
  --assume-role-policy-document '{
    "Version": "2012-10-17",
    "Statement": [{
      "Effect": "Allow",
      "Principal": {"Service": "ec2.amazonaws.com"},
      "Action": "sts:AssumeRole"
    }]
  }'

# === AUDITORÍA ===
# Ver políticas de un usuario
aws iam list-attached-user-policies --user-name pentester

# Ver quién tiene acceso root
aws iam get-account-authorization-details
```

### 2.2 S3 Security

```bash
# === CONFIGURAR BUCKET SEGURA ===
# Crear bucket con bloqueo de acceso público
aws s3api create-bucket \
  --bucket my-secure-bucket \
  --region us-east-1

# Habilitar bloqueo de acceso público
aws s3api put-public-access-block \
  --bucket my-secure-bucket \
  --public-access-block-configuration \
    BlockPublicAcls=true,\
    IgnorePublicAcls=true,\
    BlockPublicPolicy=true,\
    RestrictPublicBuckets=true

# === CORS Y ENCRYPTION ===
# Habilitar cifrado en reposo
aws s3api put-bucket-encryption \
  --bucket my-secure-bucket \
  --server-side-encryption-configuration '{
    "Rules": [{
      "ApplyServerSideEncryptionByDefault": {
        "SSEAlgorithm": "aws:kms"
      }
    }]
  }'

# === POLÍTICAS DE BUCKET ===
# Política para acceso solo desde VPN
aws s3api put-bucket-policy \
  --bucket my-secure-bucket \
  --policy '{
    "Version": "2012-10-17",
    "Statement": [{
      "Sid": "AllowVPNOnly",
      "Effect": "Deny",
      "Principal": "*",
      "Action": "s3:*",
      "Resource": "arn:aws:s3:::my-secure-bucket/*",
      "Condition": {
        "NotIpAddress": {
          "aws:SourceIp": "10.0.0.0/8"
        }
      }
    }]
  }'
```

### 2.3 EC2 Security

```bash
# === SECURITY GROUPS ===
# Crear security group
aws ec2 create-security-group \
  --group-name web-sg \
  --description "Web Server Security Group"

# Reglas de entrada
aws ec2 authorize-security-group-ingress \
  --group-id sg-12345678 \
  --protocol tcp \
  --port 443 \
  --cidr 0.0.0.0/0

# Bloquear SSH desde Internet
aws ec2 authorize-security-group-ingress \
  --group-id sg-12345678 \
  --protocol tcp \
  --port 22 \
  --cidr 10.0.0.0/8

# === KEY PAIRS ===
# Generar clave
aws ec2 create-key-pair --key-name my-key

# === INSTANCIAS ===
# Lanzar instancia con IAM role
aws ec2 run-instances \
  --image-id ami-12345678 \
  --instance-type t2.micro \
  --key-name my-key \
  --security-group-ids sg-12345678 \
  --iam-instance-profile Name=EC2-S3-Access

# === MONITORIZACIÓN ===
# Habilitar CloudTrail
aws cloudtrail create-trail \
  --name my-trail \
  --s3-bucket-name my-log-bucket

aws cloudtrail start-logging --name my-trail
```

### 2.4 Lambda Security

```bash
# === CREAR FUNCIÓN SEGURA ===
# Política mínima necesaria
aws lambda create-function \
  --function-name my-function \
  --runtime python3.9 \
  --role arn:aws:iam::role/lambda-role \
  --handler lambda_function.lambda_handler \
  --zip-file fileb://function.zip

# === VARIABLES DE ENTORNO ENCRIPTADAS ===
aws lambda update-function-configuration \
  --function-name my-function \
  --kms-key-arn arn:aws:kms:us-east-1:123456789:key/my-key

# === VPC CONFIGURATION ===
# Ejecutar en VPC privada
aws lambda update-function-configuration \
  --function-name my-function \
  --vpc-config SubnetIds=subnet-12345678,SecurityGroupIds=sg-12345678
```

## 3. Seguridad en Azure

### 3.1 Azure AD

```bash
# === GESTIÓN DE IDENTIDADES ===
# Instalar Azure CLI
curl -sL https://aka.ms/InstallAzureCLI | bash

# Login
az login

# Crear usuario
az ad user create \
  --display-name "Pentester" \
  --user-principal-name pentester@domain.com \
  --password "SecureP@ss123!"

# === ROLES ===
# Asignar rol
az role assignment create \
  --assignee pentester@domain.com \
  --role "Reader" \
  --scope /subscriptions/subscription-id

# === CONDICIONES DE ACCESO ===
# Configurar Conditional Access
az rest --method POST \
  --uri "https://graph.microsoft.com/v1.0/identity/conditionalAccess/policies" \
  --body '{
    "displayName": "Require MFA for Admins",
    "state": "enabled",
    "conditions": {
      "users": {
        "includeRoles": ["62e90394-49bc-4c43-8d32-123456789012"]
      },
      "applications": {
        "includeApplications": ["All"]
      }
    },
    "grantControls": {
      "operator": "OR",
      "builtInControls": ["mfa"]
    }
  }'
```

### 3.2 Azure Security Center

```bash
# === HABILITAR SECURITY CENTER ===
# Habilitar Azure Defender
az security pricing create \
  --name "VirtualMachines" \
  --tier "Standard"

# === POLÍTICAS DE SEGURIDAD ===
# Asignar initiative de seguridad
az policy assignment create \
  --name "SecurityBaseline" \
  --policy-set-definition "SecurityBaseline" \
  --scope "/subscriptions/subscription-id"

# === ALERTAS ===
# Ver alertas
az security alert list \
  --query "[].{Name:name, Severity:severity, Time:detectedTime}"
```

### 3.3 Azure Sentinel (SIEM)

```bash
# === CONFIGURAR SENTINEL ===
# Crear workspace
az monitor log-analytics workspace create \
  --resource-group myRG \
  --workspace-name myWorkspace

# Habilitar Sentinel
az security workspace-setting create \
  --target-workspace "/subscriptions/.../workspaces/myWorkspace"

# === CONECTORES ===
# Conectar Azure AD
az monitor data-collection rule create \
  --name "AADConnector" \
  --location eastus

# === ALERTAS ===
# Crear regla de alerta
az rest --method PUT \
  --uri "https://management.azure.com/.../alertRules/myRule" \
  --body '{
    "kind": "Scheduled",
    "properties": {
      "displayName": "Suspicious Login",
      "severity": "High",
      "query": "SigninLogs | where ResultType != 0"
    }
  }'
```

## 4. Seguridad en GCP

### 4.1 IAM y Organisation Policy

```bash
# === GESTIÓN DE IDENTIDADES ===
# Login
gcloud auth login

# Crear servicio
gcloud iam service-accounts create pentester \
  --display-name "Pentester Service Account"

# Crear clave
gcloud iam service-accounts keys create key.json \
  --iam-account pentester@project.iam.gserviceaccount.com

# === ROLES ===
# Asignar rol
gcloud projects add-iam-policy-binding my-project \
  --member="user:pentester@domain.com" \
  --role="roles/viewer"

# === ORGANISATION POLICY ===
# Restringir acceso público
gcloud resource-manager org-policies enforce \
  constraints/compute.vmExternalIpAccess \
  --organization 123456789 \
  --valueDisallowAll
```

### 4.2 Cloud Security Command Center

```bash
# === HABILITAR SCC ===
gcloud services enable securitycenter.googleapis.com

# Ver activos
gcloud scc assets list organizations/123456789 \
  --filter="securityCenterProperties.resourceType=\"google.compute.instance\""

# Ver findings
gcloud scc findings list organizations/123456789 \
  --filter="state=\"ACTIVE\""
```

### 4.3 VPC Security

```bash
# === FIREWALL RULES ===
# Crear regla
gcloud compute firewall-rules create allow-ssh \
  --network=default \
  --allow=tcp:22 \
  --source-ranges=10.0.0.0/8 \
  --target-tags=ssh-allowed

# === VPC SERVICE CONTROLS ===
# Crear perimeter
gcloud access-context-manager perimeters create myPerimeter \
  --title="My Perimeter" \
  --resources=projects/123456789 \
  --restricted-services=storage.googleapis.com
```

## 5. Herramientas Cloud Security

### 5.1 Herramientas de Auditoría

| Herramienta | Proveedor | Uso |
|-------------|-----------|-----|
| **ScoutSuite** | Multi-cloud | Auditoría de configuración |
| **Prowler** | AWS | Auditoría AWS CIS Benchmark |
| **CloudSploit** | Multi-cloud | Escaneo de seguridad |
| **Pacu** | AWS | Framework de pentesting AWS |
| **MicroBurst** | Azure | Auditoría Azure |
| **Flynn** | GCP | Auditoría GCP |

### 5.2 ScoutSuite

```bash
# Instalar
pip install scoutsuite

# Ejecutar auditoría AWS
scout aws --access-keys ACCESS_KEY --secret-key SECRET_KEY

# Ejecutar auditoría Azure
scout azure --user-account --username user@domain.com --password pass

# Ejecutar auditoría GCP
scout gcp --user-account --user-account-keyfile key.json

# Ver resultados
# Abre el reporte HTML generado
```

### 5.3 Prowler

```bash
# Instalar
git clone https://github.com/prowler-cloud/prowler.git
cd prowler
pip install -r requirements.txt

# Ejecutar todas las checks
./prowler -B my-bucket

# Ejecutar checks específicos
./prowler -c check11 check12 check13

# Generar reporte
./prowler -M json,csv,html
```

### 5.4 Pacu (AWS Exploitation)

```bash
# Instalar
git clone https://github.com/RhinoSecurityLabs/pacu.git
cd pacu
pip install -r requirements.txt

# Ejecutar
python3 pacu.py

# Módulos útiles
Pacu> run iam__enum_users_roles_policies_groups
Pacu> run iam__privesc_scan
Pacu> run s3__bucket_finder
Pacu> run lambda__backdoor_new_roles
```

## 6. Ataques Cloud Comunes

### 6.1 AWS Attacks

```bash
# === SSRF → METADATA SERVICE ===
# Acceder a credenciales de instancia
curl http://169.254.169.254/latest/meta-data/iam/security-credentials/

# === S3 BUCKET ENUMERATION ===
# Buscar buckets públicos
aws s3 ls s3://target-bucket --recursive

# === LAMBDA EXTRACTION ===
# Descargar código de Lambda
aws lambda get-function --function-name my-function

# === PRIVILEGE ESCALATION ===
# Crear usuario con permisos admin
aws iam create-user --user-name backdoor
aws iam create-access-key --user-name backdoor
aws iam attach-user-policy --user-name backdoor --policy-arn arn:aws:iam::policy/AdministratorAccess
```

### 6.2 Azure Attacks

```bash
# === AZURE AD RECON ===
# Enumerar usuarios
az ad user list --query "[].{DisplayName:displayName,UserPrincipalName:userPrincipalName}"

# Enumerar grupos
az ad group list --query "[].{DisplayName:displayName}"

# === MANAGED IDENTITY ABUSE ===
# Obtener token de managed identity
curl -H "Metadata: true" "http://169.254.169.254/metadata/identity/oauth2/token?api-version=2018-02-01&resource=https://management.azure.com/"

# === KEY VAULT ACCESS ===
# Listar secrets
az keyvault secret list --vault-name myVault
```

## 7. Defensa Cloud

### 7.1 Controles Preventivos

```yaml
# AWS Security Best Practices
security_controls:
  iam:
    - "Habilitar MFA para todos los usuarios"
    - "Usar roles en vez de access keys"
    - "Implementar least privilege"
    - "Rotar credenciales regularmente"
  
  networking:
    - "Usar VPC privadas"
    - "Configurar security groups restrictivos"
    - "Habilitar VPC Flow Logs"
    - "Implementar NACLs"
  
  data:
    - "Cifrado en reposo (S3, RDS)"
    - "Cifrado en tránsito (TLS)"
    - "Habilitar versioning en S3"
    - "Implementar bucket policies"
  
  monitoring:
    - "Habilitar CloudTrail"
    - "Configurar CloudWatch alarms"
    - "Usar GuardDuty"
    - "Implementar Security Hub"
```

### 7.2 GuardDuty (AWS)

```bash
# Habilitar GuardDuty
aws guardduty create-detector --enable

# Ver findings
aws guardduty list-findings --detector-id detector-id

# Crear custom threat list
aws guardduty create-threat-intel-set \
  --detector-id detector-id \
  --name "Custom Threats" \
  --format TXT \
  --location "s3://my-bucket/threats.txt"
```

### 7.3 Security Hub (AWS)

```bash
# Habilitar Security Hub
aws securityhub enable-security-hub

# Ver standard findings
aws securityhub get-findings \
  --filters '{"GeneratorId": [{"Value": "arn:aws:securityhub:::ruleset/cis-aws-foundations-benchmark", "Comparison": "PREFIX"}]}'

# Exportar a S3
aws securityhub create-action-target \
  --name "ExportFindings" \
  --description "Export findings to S3"
```

## 8. Ejercicios Prácticos

### Ejercicio 1: Auditoría AWS con ScoutSuite

```bash
# 1. Instalar ScoutSuite
pip install scoutsuite

# 2. Ejecutar auditoría
scout aws --access-keys $AWS_ACCESS_KEY --secret-key $AWS_SECRET_KEY

# 3. Analizar reporte
# Abrir output/aws/.../report.html

# 4. Identificar hallazgos críticos
# - S3 buckets públicos
# - Security groups abiertos
# - IAM users sin MFA
# - CloudTrail deshabilitado

# 5. Documentar hallazgos
cat > aws_audit_report.md << 'EOF'
# AWS Security Audit Report

## Hallazgos Críticos
1. S3 bucket público: my-bucket
2. Security group con SSH abierto a 0.0.0.0/0
3. 3 usuarios sin MFA habilitado

## Hallazgos Medios
1. CloudTrail no habilitado en todas las regiones
2. GuardDuty deshabilitado
3. VPC Flow Logs no habilitados

## Recomendaciones
1. Habilitar bloqueo de acceso público en S3
2. Restringir SSH a IPs internas
3. Habilitar MFA para todos los usuarios
EOF
```

### Ejercicio 2: Explotación con Pacu

```bash
# 1. Iniciar Pacu
python3 pacu.py

# 2. Configurar credenciales
Pacu> set_keys aws_access_key_id aws_secret_access_key

# 3. Enumerar usuarios IAM
Pacu> run iam__enum_users_roles_policies_groups

# 4. Buscar escalamiento de privilegios
Pacu> run iam__privesc_scan

# 5. Buscar S3 buckets
Pacu> run s3__bucket_finder --wordlist /usr/share/wordlists/s3 buckets.txt

# 6. Documentar hallazgos
```

### Ejercicio 3: Configurar Azure Security

```bash
# 1. Habilitar Azure Defender
az security pricing create --name "VirtualMachines" --tier "Standard"

# 2. Configurar Sentinel
az monitor log-analytics workspace create --resource-group myRG --workspace-name myWorkspace

# 3. Crear regla de alerta
az rest --method PUT --uri "..." --body '...'

# 4. Probar con escaneo
nmap -sV target.cloudapp.azure.com

# 5. Verificar alerta generada
az security alert list --query "[].{Name:name,Severity:severity}"
```

### Ejercicio 4: Reporte Cloud Security

```markdown
# Cloud Security Report - [Proveedor]

## Resumen Ejecutivo
- Proveedor: [AWS/Azure/GCP]
- Servicios auditados: [X]
- Hallazgos críticos: [X]
- Hallazgos medios: [X]

## Hallazgos por Categoría

### Identity & Access Management
| Hallazgo | Severidad | Estado |
|----------|-----------|--------|
| Usuarios sin MFA | Alto | [X] |
| Roles con permisos excesivos | Medio | [X] |
| Access keys antiguas | Bajo | [X] |

### Networking
| Hallazgo | Severidad | Estado |
|----------|-----------|--------|
| Security groups abiertos | Alto | [X] |
| VPC Flow Logs deshabilitados | Medio | [X] |

### Data Protection
| Hallazgo | Severidad | Estado |
|----------|-----------|--------|
| S3 buckets públicos | Crítico | [X] |
| Cifrado no habilitado | Alto | [X] |

### Monitoring
| Hallazgo | Severidad | Estado |
|----------|-----------|--------|
| CloudTrail deshabilitado | Alto | [X] |
| GuardDuty deshabilitado | Medio | [X] |

## Recomendaciones
1. [Recomendación 1]
2. [Recomendación 2]
3. [Recomendación 3]

## Roadmap de Seguridad
- **Corto plazo (1 semana):** [Acciones inmediatas]
- **Medio plazo (1 mes):** [Mejoras de configuración]
- **Largo plazo (3 meses):** [Arquitectura de seguridad]
```

## 9. Referencias

| Recurso | Descripción |
|---------|-------------|
| [AWS Security Best Practices](https://docs.aws.amazon.com/wellarchitected/latest/security-pillar/welcome.html) | Guía oficial AWS |
| [Azure Security Documentation](https://docs.microsoft.com/en-us/azure/security/) | Documentación Azure |
| [GCP Security Best Practices](https://cloud.google.com/security/best-practices) | Guía oficial GCP |
| [ScoutSuite](https://github.com/nccgroup/ScoutSuite) | Auditoría multi-cloud |
| [Prowler](https://github.com/prowler-cloud/prowler) | Auditoría AWS |
| [Pacu](https://github.com/RhinoSecurityLabs/pacu) | Pentesting AWS |

## 📌 Checkpoint final

Antes de avanzar, verifica que puedas:

- [ ] Explicar el modelo de responsabilidad compartida
- [ ] Configurar IAM con least privilege
- [ ] Auditar infraestructura cloud con ScoutSuite
- [ ] Ejecutar ataques cloud básicos en laboratorio
- [ ] Implementar controles de seguridad cloud
- [ ] Generar reporte de seguridad cloud

> ⏭️ **Siguiente:** [`17-ai-security.md`](./17-ai-security.md) — Seguridad de Inteligencia Artificial.
