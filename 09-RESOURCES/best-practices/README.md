# ✅ Mejores Prácticas de Ciberseguridad

## 📋 Descripción

Colección de mejores prácticas y estándares de la industria para implementar seguridad de forma efectiva.

---

## 📁 Categorías

### 🔴 Red Team (Ofensiva)

| Práctica | Descripción | Prioridad |
|----------|-------------|-----------|
| [Metodología de Pentest](red-team/metodologia-pentest.md) | Proceso estándar de auditoría | 🔴 Alta |
| [Alcance y Autorización](red-team/alcance-autorizacion.md) | Definir límites del test | 🔴 Alta |
| [Documentación de Hallazgos](red-team/documentacion-hallazgos.md) | Cómo reportar vulnerabilidades | 🔴 Alta |
| [ Herramientas Autorizadas](red-team/herramientas-autorizadas.md) | Lista de herramientas permitidas | 🟡 Media |

### 🔵 Blue Team (Defensiva)

| Práctica | Descripción | Prioridad |
|----------|-------------|-----------|
| [Hardening de Sistemas](blue-team/hardening-sistemas.md) | Endurecimiento de SO | 🔴 Alta |
| [Configuración de Firewall](blue-team/configuracion-firewall.md) | Reglas efectivas | 🔴 Alta |
| [Monitoreo y Alertas](blue-team/monitoreo-alertas.md) | SIEM y detección | 🔴 Alta |
| [Respuesta a Incidentes](blue-team/respuesta-incidentes.md) | Proceso de IR | 🔴 Alta |

### ☁️ Cloud Security

| Práctica | Descripción | Prioridad |
|----------|-------------|-----------|
| [AWS Security](cloud/aws-security.md) | Mejores prácticas AWS | 🔴 Alta |
| [Azure Security](cloud/azure-security.md) | Mejores prácticas Azure | 🔴 Alta |
| [Container Security](cloud/container-security.md) | Docker y Kubernetes | 🔴 Alta |
| [IAM y Accesos](cloud/iam-accesos.md) | Gestión de identidades | 🔴 Alta |

### 🐳 DevSecOps

| Práctica | Descripción | Prioridad |
|----------|-------------|-----------|
| [Secure Coding](devsecops/secure-coding.md) | Código seguro | 🔴 Alta |
| [SAST/DAST](devsecops/sast-dast.md) | Testing de seguridad | 🔴 Alta |
| [Secret Scanning](devsecops/secret-scanning.md) | Detección de secretos | 🔴 Alta |
| [CI/CD Security](devsecops/cicd-security.md) | Pipelines seguros | 🟡 Media |

---

## 🔴 Red Team: Metodología de Pentest

### Fases del Pentest

```
┌─────────────────────────────────────────────────────────────┐
│                 METODOLOGÍA DE PENTEST                      │
├─────────────────────────────────────────────────────────────┤
│                                                              │
│  1. Pre-engagement     │ Acuerdo, alcance, reglas            │
│  2. Reconocimiento     │ OSINT, fingerprinting               │
│  3. Enumeración        │ Puertos, servicios, versiones       │
│  4. Explotación        │ Vulnerabilidades, exploits          │
│  5. Post-Explotación   │ Persistencia, escalada              │
│  6. Reporte            │ Documentación, recomendaciones      │
│                                                              │
└─────────────────────────────────────────────────────────────┘
```

### Checklist Pre-Engagement

```markdown
## Pre-Engagement Checklist

### Legal
- [ ] Contrato firmado
- [ ] Alcance definido
- [ ] Reglas de engagement acordadas
- [ ] Contacto de emergencia definido
- [ ] Seguro de responsabilidad civil

### Técnico
- [ ] Acceso a sistemas autorizados
- [ ] Credenciales de prueba
- [ ] VPN configurada
- [ ] Herramientas autorizadas
- [ ] Entorno de pruebas aislado

### Comunicación
- [ ] Puntos de contacto
- [ ] Frecuencia de updates
- [ ] Proceso de escalamiento
- [ ] Horarios de contacto
- [ ] Canales seguros
```

---

## 🔵 Blue Team: Hardening de Sistemas

### Linux Hardening

```bash
# 1. Actualizar sistema
sudo apt update && sudo apt upgrade -y

# 2. Configurar firewall
sudo ufw default deny incoming
sudo ufw default allow outgoing
sudo ufw allow ssh
sudo ufw enable

# 3. SSH Hardening
sudo nano /etc/ssh/sshd_config
# Cambiar:
# PermitRootLogin no
# PasswordAuthentication no
# Port 2222

# 4. Instalar Fail2Ban
sudo apt install fail2ban
sudo systemctl enable fail2ban

# 5. Auditoría de usuarios
sudo cat /etc/passwd | grep -v nologin
```

### Windows Hardening

```powershell
# 1. Actualizar Windows
Install-Module PSWindowsUpdate
Get-WindowsUpdate -AcceptAll -Install

# 2. Habilitar Firewall
Set-NetFirewallProfile -Profile Domain,Public,Private -Enabled True

# 3. Configurar políticas de contraseña
net accounts /minpwlen:12 /maxpwage:90

# 4. Habilitar logging
auditpol /set /subcategory:"Logon" /success:enable /failure:enable

# 5. Deshabilitar servicios innecesarios
Stop-Service -Name "Telnet" -Force
Set-Service -Name "Telnet" -StartupType Disabled
```

---

## ☁️ Cloud Security: AWS

### Checklist AWS Security

```markdown
## AWS Security Checklist

### IAM
- [ ] MFA habilitado para todos los usuarios
- [ ] Root account protegido y sin uso diario
- [ ] Políticas least privilege
- [ ] Access keys rotadas cada 90 días
- [ ] Roles IAM para servicios EC2/ECS

### S3
- [ ] Block Public Access habilitado
- [ ] Cifrado SSE-S3 o SSE-KMS
- [ ] Versionado habilitado
- [ ] Access Logging activado
- [ ] Lifecycle policies

### EC2
- [ ] Security Groups restrictivos
- [ ] SSH solo por key pairs
- [ ] Cifrado EBS habilitado
- [ ] IMDSv2 habilitado
- [ ] Actualizaciones aplicadas

### RDS
- [ ] Cifrado en reposo
- [ ] Acceso restringido a VPC
- [ ] Backups automatizados
- [ ] Multi-AZ para producción
- [ ] Audit logging

### Networking
- [ ] VPC con subnets privadas
- [ ] NAT Gateway configurado
- [ ] Flow Logs habilitados
- [ ] Security Groups revisados
- [ ] NACLs configuradas
```

---

## 🐳 DevSecOps

### Pipeline de Seguridad

```yaml
# .github/workflows/security.yml
name: Security Pipeline

on: [push, pull_request]

jobs:
  security:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v3
      
      - name: Run SAST
        uses: github/codeql-action/analyze@v2
        
      - name: Run Secret Scanning
        uses: trufflesecurity/trufflehog@main
        
      - name: Run Dependency Check
        uses: dependency-check/Dependency-Check_Action@main
        
      - name: Run Container Scanning
        uses: aquasecurity/trivy-action@master
```

### Secure Coding Practices

```python
# ✅ Buen código - Validación de entrada
def process_user_input(user_input: str) -> str:
    """Procesa entrada del usuario de forma segura."""
    # Validar longitud
    if len(user_input) > 1000:
        raise ValueError("Input demasiado largo")
    
    # Sanitizar
    import html
    sanitized = html.escape(user_input)
    
    # Validar formato
    import re
    if not re.match(r'^[a-zA-Z0-9_\-]+$', sanitized):
        raise ValueError("Formato inválido")
    
    return sanitized

# ❌ Mal código - Sin validación
def process_user_input_bad(user_input: str) -> str:
    """NUNCA hacer esto."""
    return user_input  # Vulnerable a XSS, SQLi, etc.
```

---

## 📊 Frameworks de Seguridad

### NIST Cybersecurity Framework

```
┌─────────────────────────────────────────────────────────────┐
│              NIST CYBERSECURITY FRAMEWORK                   │
├─────────────────────────────────────────────────────────────┤
│                                                              │
│  IDENTIFY      │ Identificar activos y riesgos              │
│  PROTECT       │ Implementar controles                       │
│  DETECT        │ Monitorear y detectar incidentes           │
│  RESPONDER     │ Responder a incidentes                      │
│  RECOVER       │ Recuperarse de incidentes                   │
│                                                              │
└─────────────────────────────────────────────────────────────┘
```

### MITRE ATT&CK

| Táctica | Descripción | Herramientas |
|---------|-------------|--------------|
| Reconocimiento | Recopilar información | theHarvester, Recon-ng |
| Acceso Inicial | Obtener entrada | Phishing, Exploits |
| Ejecución | Ejecutar código | PowerShell, Macros |
| Persistencia | Mantener acceso | Scheduled Tasks, Registry |
| Escalada | Obtener privilegios | exploits, misconfig |
| Evasión | Evadir defensas | Obfuscation, Anti-forensics |
| Acceso a Credenciales | Robar credenciales | Mimikatz, LaZagne |
| Movimiento Lateral | Moverse en la red | PsExec, WMI |
| Recolección | Recopilar datos | Keyloggers, Screenshots |
| Exfiltration | Sacar datos | DNS, HTTP, Cloud |
| Impacto | Causar daño | Ransomware, Wiper |

---

## 📋 Plantillas de Documentación

### Template de Auditoría

```markdown
# Informe de Auditoría de Seguridad

## Información General
- **Fecha:** YYYY-MM-DD
- **Auditor:** [Nombre]
- **Objetivo:** [Sistema/Red]
- **Alcance:** [Definido en contrato]

## Resumen Ejecutivo
[Resumen para ejecutivos]

## Metodología
[Herramientas y técnicas utilizadas]

## Hallazgos

### Críticos
1. [Hallazgo 1]

### Altos
1. [Hallazgo 2]

### Medios
1. [Hallazgo 3]

### Bajos
1. [Hallazgo 4]

## Recomendaciones
1. [Recomendación 1]
2. [Recomendación 2]

## Conclusiones
[Conclusiones generales]

## Anexos
[Evidencia, logs, capturas]
```

---

## 📚 Recursos

### Estándares

| Estándar | Descripción |
|----------|-------------|
| ISO 27001 | Gestión de seguridad de la información |
| NIST CSF | Framework de ciberseguridad |
| CIS Controls | Controles de seguridad prioritarios |
| OWASP Top 10 | Vulnerabilidades web principales |

### Herramientas de Auditoría

| Herramienta | Uso |
|-------------|-----|
| Nessus | Escaneo de vulnerabilidades |
| OpenVAS | Vulnerability scanner |
| Lynis | Auditoría Linux |
| Microsoft Baseline Security Analyzer | Auditoría Windows |

---

## 🔄 Actualizaciones

| Fecha | Contenido |
|-------|-----------|
| 2026-08-19 | Mejores prácticas iniciales |

---

*Mejores prácticas para profesionales de ciberseguridad • CyberDefense Pro Network*
