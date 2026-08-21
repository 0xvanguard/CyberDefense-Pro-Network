---
title: "04 — Sistema operativo y línea de comandos"
---

# 04 — Sistema operativo y línea de comandos

> 🎯 **Objetivo:** moverte con soltura en Linux y Windows desde la terminal, entender usuarios/permisos y leer logs básicos. La terminal es tu herramienta diaria — es como el bisturí del cirujano: sin ella, no sigues.

## 1. ¿Por qué la terminal?

- Casi todo en servidores funciona **sin interfaz gráfica**.
- Los atacantes operan en shell (no hay GUI donde esconderse).
- Automatizas con scripts lo que en GUI sería eterno.
- Cuando algo se rompe, la terminal es tu única esperanza.

## 2. Linux básico

### 2.1 Distribuciones que verás en seguridad

| Distro | Para qué |
|---|---|
| **Kali Linux** | Pentest. Viene con todas las herramientas preinstaladas. |
| **Parrot OS** | Similar a Kali, más ligero. |
| **Ubuntu / Debian** | Servidores comunes. Aprender a defender aquí es clave. |
| **Alpine** | Imágenes Docker minimalistas. |
| **BlackArch** | Arch-based, catálogo enorme de herramientas de pentest. |

### 2.2 Los 15 comandos que aprender primero

```bash
# Navegación
pwd                     # dónde estoy
ls -la                  # qué hay aquí (incluye ocultos)
cd /var/log             # cambiar de directorio
tree -L 2               # árbol de directorios

# Archivos
cat archivo             # ver contenido
less archivo            # ver con scroll
head -n 20 archivo      # primeras 20 líneas
tail -f archivo         # últimas líneas en vivo (logs!)
grep "error" archivo    # buscar patrón
find / -name "*.conf"   # buscar archivos

# Permisos / ownership
chmod 755 script.sh     # permisos octales
chown user:group file   # cambiar dueño
sudo comando            # ejecutar como root

# Sistema
ps aux                  # procesos en ejecución
top / htop              # procesos en vivo
df -h                   # espacio en disco
free -h                 # memoria
systemctl status nginx  # estado de un servicio
```

### 2.3 El sistema de archivos

```
/
├── /home/usuario          ← tus archivos personales
├── /etc                   ← configuración del sistema
├── /var/log               ← logs (oro para defender)
├── /var/www               ← webs típicas
├── /tmp                   ← temporales (sospechoso si persistencia)
├── /opt                   ← apps opcionales
├── /usr/bin               ← binarios instalados
└── /root                  ← home del root
```

> 💡 **Para un atacante:** `/tmp`, `/var/tmp` y ocultos en `~/.ssh/` son zonas favoritas para persistencia.

### 2.4 Usuarios y permisos

```bash
# Quién soy
whoami
id

# Ver permisos (rwx = read/write/execute)
ls -la archivo
# -rwxr-xr-x  1 user group 1234 archivo
#  ^^^ permiso dueño
#     ^^^ permiso grupo
#        ^^^ permiso otros

# Octal: r=4, w=2, x=1
# 755 = rwx para dueño, rx para grupo y otros
chmod 755 archivo
```

### 2.5 Paquetería

```bash
# Debian / Ubuntu
sudo apt update && sudo apt install nmap

# Arch
sudo pacman -S nmap

# RHEL / Fedora / CentOS
sudo dnf install nmap
```

### 2.6 SSH, la navaja del admin

```bash
# Conectar
ssh usuario@servidor

# Generar clave
ssh-keygen -t ed25519

# Copiar clave pública al servidor
ssh-copy-id usuario@servidor

# Túnel (proxy)
ssh -D 1080 usuario@servidor         # SOCKS proxy
ssh -L 8080:localhost:80 usuario@s   # local forward
```

> 📂 Configuración típica en `/etc/ssh/sshd_config`. Por seguridad: deshabilita login root por contraseña, usa solo claves.

## 3. Windows básico

### 3.1 PowerShell — el reemplazo moderno de CMD

```powershell
# Navegación
Get-ChildItem           # alias: ls, dir
Set-Location C:\Users   # alias: cd
Get-Location            # alias: pwd

# Procesos
Get-Process             # alias: ps
Stop-Process -Name notepad

# Servicios
Get-Service
Restart-Service Spooler

# Red
Get-NetIPAddress
Test-NetConnection google.com -Port 443

# Logs (Event Viewer desde CLI)
Get-EventLog -LogName System -Newest 20
Get-WinEvent -FilterHashtable @{LogName='Security'; ID=4624} -MaxEvents 10
```

### 3.2 CMD clásico (sigue vivo)

```cmd
dir
cd
type archivo.txt        # equivalente a cat
findstr "error" log.txt
ipconfig
netstat -an
tasklist
```

### 3.3 Usuarios y permisos en Windows

- **SID** — identifier de cada usuario/grupo
- **ACL** — Access Control List (reglas)
- **UAC** — User Account Control (prompt de elevación)

```cmd
:: Ver usuarios locales
net user
net localgroup administrators

:: Ver recursos compartidos
net share

:: Permisos de un archivo
icacls C:\Users\admin
```

## 4. Logs: lo que de verdad importa

### Linux

| Archivo | Qué tiene |
|---|---|
| `/var/log/syslog` | Eventos generales del sistema |
| `/var/log/auth.log` | Logins, sudo, SSH |
| `/var/log/kern.log` | Eventos del kernel |
| `/var/log/nginx/` | Logs del servidor web |
| `~/.bash_history` | Historial de comandos (!) |

### Windows (Event Viewer)

| Event ID | Qué pasó |
|---|---|
| 4624 | Logon exitoso |
| 4625 | Logon fallido |
| 4648 | Logon con credenciales explícitas |
| 4688 | Nuevo proceso creado |
| 4720 | Usuario creado |
| 1102 | Log de auditoría borrado (🚩) |

> 💡 **Atacante**: para no dejar rastro, borra logs y edita `~/.bash_history`. **Defensor**: así detectas esos intentos.

## 5. Procesos sospechosos — qué mirar

- Procesos que corren desde `/tmp`, `\Temp`, `AppData`
- Procesos con nombres que imitan a los del sistema (`svch0st.exe` en lugar de `svchost.exe`)
- Procesos sin padre o con padre `explorer.exe` con argumentos raros
- Conexiones salientes a IPs públicas desde procesos que no deberían

```bash
# Linux: ver árbol de procesos
ps auxf

# Linux: procesos con conexiones de red
sudo ss -tulnp

# Windows: procesos y dueño
Get-Process | Where {$_.Path -like "*Temp*"}
```

## 📌 Dónde practicar

| Recurso | Dónde |
|---|---|
| Labs Linux/Windows | [`04-LABORATORIOS/docker-labs/`](../04-LABORATORIOS/docker-labs/) |
| Cheatsheets Linux | [`05-RECURSOS/cheatsheets/`](../05-RECURSOS/cheatsheets/) |
| Blue team forensics | [`01-CIBERSEGURIDAD/forense-digital/`](../01-CIBERSEGURIDAD/forense-digital/) |

## ✏️ Ejercicios

1. **Terminal nula:** abre una terminal y ve cuánto vives sin ratón durante una hora.
2. **Logs en vivo:** `tail -f /var/log/syslog` (Linux) o `Get-EventLog -LogName System -Newest 0 -Wait` y mira qué pasa al enchufar un USB.
3. **Permisos:** crea un archivo `secreto.txt`, dale permisos `600`, comprueba que solo tú puedes leerlo.
4. **SSH:** genera una clave y conéctate a una máquina virtual o a tu propio servidor remoto.

> ⏭️ **Siguiente:** [`05-criptografia-basica.md`](./05-criptografia-basica.md) — lo esencial que necesitas entender sobre cifrado.
