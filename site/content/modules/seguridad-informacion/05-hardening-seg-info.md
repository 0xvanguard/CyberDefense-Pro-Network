---
title: "Módulo 05 — Hardening"
---

# 🔒 Módulo 05 — Hardening

> **Objetivo:** Reducir la superficie de ataque en sistemas operativos, redes y aplicaciones.

[![Nivel](https://img.shields.io/badge/Nivel-Intermedio-orange?style=flat-square)]()
[![Duración](https://img.shields.io/badge/Duración-1.5%20meses-blue?style=flat-square)]()

---

## 📋 Resumen del módulo

| Atributo | Detalle |
|----------|---------|
| **Pre-requisitos** | Fundamentos completados |
| **Estándares** | CIS Benchmark, STIG |
| **Herramientas** | Lynis, OpenSCAP, Ansible |
| **Nivel** | Intermedio |

---

## 1. 🧠 Teoría: Principios de Hardening

| Principio | Descripción |
|-----------|-------------|
| **Mínimo privilegio** | Solo permisos necesarios |
| **Defense in depth** | Múltiples capas |
| **Seguridad por defecto** | Todo bloqueado |
| **Fail-safe** | Si falla, denegar |
| **Separación de deberes** | Un persona ≠ todos los permisos |

---

## 2. 🛠️ Hardening Linux

### CIS Benchmark checklist

```bash
# 1. Deshabilitar servicios innecesarios
sudo systemctl disable --now cups avahi-daemon bluetooth

# 2. Configurar SSH
sudo sed -i 's/#PermitRootLogin yes/PermitRootLogin no/' /etc/ssh/sshd_config
sudo sed -i 's/#PasswordAuthentication yes/PasswordAuthentication no/' /etc/ssh/sshd_config
sudo systemctl restart sshd

# 3. Configurar firewall
sudo ufw default deny incoming
sudo ufw default allow outgoing
sudo ufw allow 22/tcp
sudo ufw enable

# 4. Instalar y ejecutar Lynis
sudo apt install lynis
sudo lynis audit system
```

### Auditoría con OpenSCAP

```bash
# Evaluar contra CIS Benchmark
sudo oscap xccdf eval \
  --profile cis \
  --results results.xml \
  --report report.html \
  /usr/share/xml/scap/ssg/content/ssg-ubuntu2204-ds.xml
```

---

## 3. 🛠️ Hardening Windows

### PowerShell

```powershell
# 1. Habilitar Windows Defender
Set-MpPreference -DisableRealtimeMonitoring $false

# 2. Habilitar firewall
Set-NetFirewallProfile -Profile Domain,Public,Private -Enabled True

# 3. Configurar políticas de contraseña
net accounts /minpwlen:12 /maxpwage:90

# 4. Auditar cambios
auditpol /set /category:"Account Management" /success:enable /failure:enable
```

### CIS Benchmark Windows

```powershell
# Descargar herramientas
https://learn.cisecurity.org/benchmarks
```

---

## 4. ✏️ Ejercicios prácticos

### Ejercicio 1: Auditar Linux (30 min)

1. Instala Lynis en tu máquina o VM
2. Ejecuta auditoría completa
3. Revisa los hallazgos
4. Implementa las 3 recomendaciones más críticas

### Ejercicio 2: Crear playbook de hardening (30 min)

1. Elige un SO (Linux o Windows)
2. Crea un playbook Ansible con 10 controles CIS
3. Prueba en una VM

### Ejercicio 3: Medir mejora (20 min)

1. Ejecuta Lynis antes del hardening
2. Anota el score
3. Aplica los controles
4. Ejecuta de nuevo y compara

---

> **Siguiente:** [Módulo 06 — Compliance y Normativas](./06-compliance-normativas)
