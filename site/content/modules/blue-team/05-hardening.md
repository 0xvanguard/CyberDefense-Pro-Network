---
title: "Módulo 05 — Hardening y Seguridad de Sistemas"
---

# 🔒 Módulo 05 — Hardening y Seguridad de Sistemas

> **Objetivo Principal:** Aprender a endurecer sistemas operativos, redes y aplicaciones para reducir la superficie de ataque.

[![Nivel](https://img.shields.io/badge/Nivel-Intermedio-orange?style=flat-square)]()
[![Duración](https://img.shields.io/badge/Duración-1.5%20meses-blue?style=flat-square)]()

---

## 📋 Resumen del módulo

| Atributo | Detalle |
|----------|---------|
| **Pre-requisitos** | Módulo 01 completado |
| **Herramientas** | CIS Benchmark, Lynis, OpenSCAP |
| **Entregable** | Reporte de hardening + implementación |
| **Nivel** | Intermedio |

---

## 1. 🧠 Teoría: ¿Qué es Hardening?

Hardening es el proceso de **reducir la superficie de ataque** de un sistema eliminando servicios innecesarios, aplicando parches y configurando controles de seguridad.

### Superficie de Ataque

```
┌─────────────────────────────────────────────────────┐
│              SUPERFICIE DE ATAQUE                     │
├─────────────┬──────────────┬────────────┬───────────┤
│  Servicios  │  Puertos     │  Usuarios  │  Software │
│  abiertos   │  expuestos   │  con perm. │  desactual│
├──────────────┼──────────────┼────────────┼───────────┤
│  Configurac. │  Red         │  Datos     │  Acceso   │
│  por defecto │  interna     │  sensibles │  remoto   │
└──────────────┴──────────────┴────────────┴───────────┘
```

### Principios de Hardening

| Principio | Descripción |
|-----------|-------------|
| **Principio de mínimo privilegio** | Solo los permisos necesarios |
| **Defense in depth** | Múltiples capas de seguridad |
| **Seguridad por defecto** | Todo bloqueado por defecto |
| **Fail-safe** | Si falla, se deniega acceso |
| **Separación de deberes** | Un persona no tiene todos los permisos |

---

## 2. 🛠️ Herramientas

### CIS Benchmark

```bash
# Descargar CIS Benchmark para Ubuntu
wget https://www.cisecurity.org/cis-benchmarks

# Aplicar configuraciones recomendadas
# Ejemplo: Configurar SSH según CIS
sudo apt install openssh-server

# /etc/ssh/sshd_config
PermitRootLogin no
PasswordAuthentication no
Protocol 2
MaxAuthTries 3
ClientAliveInterval 300
ClientAliveCountMax 2
```

### Lynis - Auditoría de Seguridad

```bash
# Instalar Lynis
sudo apt install lynis

# Ejecutar auditoría completa
sudo lynis audit system

# Ver reporte
cat /var/log/lynis.log
```

---

## 3. 🔬 Práctica Guiada: Hardening de Linux

### Paso 1: Deshabilitar servicios innecesarios

```bash
# Listar servicios activos
systemctl list-units --type=service --state=running

# Deshabilitar servicios innecesarios
sudo systemctl disable --now cups
sudo systemctl disable --now avahi-daemon
sudo systemctl disable --now bluetooth
```

### Paso 2: Configurar firewall

```bash
# Configurar UFW
sudo ufw default deny incoming
sudo ufw default allow outgoing
sudo ufw allow 22/tcp    # SSH
sudo ufw allow 443/tcp   # HTTPS
sudo ufw enable

# Verificar reglas
sudo ufw status verbose
```

### Paso 3: Configurar auditoría con auditd

```bash
# Instalar auditd
sudo apt install auditd

# Configurar reglas de auditoría
sudo auditctl -w /etc/passwd -p wa -k passwd_changes
sudo auditctl -w /etc/shadow -p wa -k shadow_changes
sudo auditctl -w /var/log/auth.log -p wa -k auth_log

# Ver eventos
sudo ausearch -k passwd_changes
```

---

## 4. 📊 Checklist de Hardening

### Linux Server

- [ ] SSH hardening (no root, key-based auth)
- [ ] Firewall configurado (UFW/iptables)
- [ ] Servicios innecesarios deshabilitados
- [ ] Parches de seguridad actualizados
- [ ] Auditoría habilitada (auditd)
- [ ] Fail2ban instalado y configurado
- [ ] Permisos de archivos restringidos
- [ ] Logging centralizado configurado

### Windows Server

- [ ] Actualizaciones de Windows aplicadas
- [ ] Windows Defender habilitado
- [ ] Firewall de Windows activo
- [ ] Cuentas admin renombradas
- [ ] Políticas de contraseña fuertes
- [ ] UAC habilitado
- [ ] BitLocker activado
- [ ] Auditing habilitado

---

## 5. 🎯 Mini-Entregable

**Tarea:** Realizar hardening de un sistema Linux que incluya:

1. **Auditoría inicial** con Lynis
2. **Implementación** de controles CIS
3. **Verificación** post-hardening
4. **Reporte** con hallazgos y mejoras

---

## 6. 🔗 Recursos Adicionales

- [CIS Benchmarks](https://www.cisecurity.org/cis-benchmarks/)
- [Lynis Documentation](https://cisofy.com/documentation/lynis/)
- [OpenSCAP](https://www.open-scap.org/)

---

> **Siguiente paso:** Continúa con el [Módulo 06 — Forense de Endpoint](../blue-team/06-forense-endpoint) para aprender análisis de endpoints.
