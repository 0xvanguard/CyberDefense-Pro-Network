---
title: "10 — Introducción a Linux para Ciberseguridad"
---

# 10 — Introducción a Linux para Ciberseguridad

> 🎯 **Objetivo:** dominar Linux desde la perspectiva de seguridad — no solo administrarlo, sino entender cómo se protege, cómo se ataca y cómo se monitorea. Linux es el OS de la ciberseguridad: lo usan los defensores Y los atacantes.

## 1. Por qué Linux es el OS de la ciberseguridad

| Razón | Explicación |
|-------|-------------|
| **Transparencia** | Código abierto = puedes ver exactamente qué hace cada herramienta |
| **Control total** | Sin interfaz gráfica = menos superficie de ataque |
| **Servidores** | 90%+ de servidores web corren Linux |
| **Seguridad nativa** | SELinux, AppArmor, capabilities, namespaces |
| **Herramientas** | Kali, Parrot, BlackArch vienen preconfigurados |
| **Costo** | Gratuito, sin licencias |

### Distribuciones para seguridad

| Distro | Uso principal | Ventaja |
|--------|--------------|---------|
| **Kali Linux** | Pentesting / Red Team | 600+ herramientas preinstaladas |
| **Parrot OS** | Pentesting + privacidad | Más ligero que Kali |
| **Ubuntu/Debian** | Servidores defensivos | Estabilidad, enorme comunidad |
| **Alpine Linux** | Contenedores Docker | ~5MB, mínimo ataque |
| **CentOS/RHEL** | Entornos empresariales | Enterprise-grade, SELinux |
| **Arch Linux** | Personalizado | Rolling release, todo manual |

## 2. Seguridad del sistema de archivos

### 2.1 Permisos avanzados

```bash
# Permisos básicos (rwx)
ls -la archivo
# -rwxr-xr-x  1 root root 4096 Jan 21 10:00 archivo
#  ^^^^       ^^^^ ^^^^
#  permisos   dueño grupo

# Octales: r=4, w=2, x=1
chmod 755 archivo    # rwxr-xr-x
chmod 644 archivo    # rw-r--r--
chmod 600 secreto    # rw------- (solo dueño)

# Setuid (ejecuta como dueño, no como usuario)
chmod u+s /usr/bin/passwd    # passwd necesita ser root
ls -la /usr/bin/passwd
# -rwsr-xr-x ... /usr/bin/passwd
#     ^^^ setuid activo

# Setgid (hereda grupo del directorio padre)
chmod g+s /proyecto/
# Archivos nuevos heredan el grupo "proyecto"

# Sticky bit (solo el dueño puede borrar en /tmp)
chmod +t /tmp/
# drwxrwxrwt ... /tmp/
#            ^^^ sticky bit
```

### 2.2 ACL — Control de acceso detallado

```bash
# Ver ACL de un archivo
getfacl archivo.txt

# Dar permiso específico a un usuario
setfacl -m u:juan:rwx archivo.txt

# Dar permiso a un grupo completo
setfacl -m g:auditores:r archivo.log

# Herencia de ACL en directorios
setfacl -d -m g:equipo:rwx /proyecto/
# Los archivos nuevos heredan automáticamente la ACL
```

### 2.3 Attributes (atributos especiales)

```bash
# Hacer archivo inmutable (ni root puede borrarlo)
sudo chattr +i archivo_critico.txt
lsattr archivo_critico.txt
# ----i------------- archivo_critico.txt

# Para modificarlo, primero quitas la inmutabilidad
sudo chattr -i archivo_critico.txt

# Atributo de append-only (solo agregar, no modificar)
sudo chattr +a /var/log/auditoria.log
# Útil: evita que un atacante borre logs
```

### 2.4 Búsqueda de SUID/SGID

```bash
# Archivos con SUID (peligroso si están en el path equivocado)
find / -perm -4000 -type f 2>/dev/null

# Archivos con SGID
find / -perm -2000 -type f 2>/dev/null

# Archivos modificados recientemente
find / -mtime -1 -type f 2>/dev/null

# Archivos sin dueño
find / -nouser -o -nogroup 2>/dev/null

# Archivos con permisos excesivos
find / -perm -777 -type f 2>/dev/null
```

## 3. Seguridad de red en Linux

### 3.1 Firewall con iptables

```bash
# Ver reglas actuales
sudo iptables -L -n -v

# Política por defecto: denegar todo
sudo iptables -P INPUT DROP
sudo iptables -P FORWARD DROP
sudo iptables -P OUTPUT ACCEPT

# Permitir tráfico establecido y relacionado
sudo iptables -A INPUT -m state --state ESTABLISHED,RELATED -j ACCEPT

# Permitir loopback
sudo iptables -A INPUT -i lo -j ACCEPT

# Permitir SSH (solo tu IP)
sudo iptables -A INPUT -p tcp --dport 22 -s 192.168.1.100 -j ACCEPT

# Permitir HTTP/HTTPS
sudo iptables -A INPUT -p tcp --dport 80 -j ACCEPT
sudo iptables -A INPUT -p tcp --dport 443 -j ACCEPT

# Bloquear un IP específico
sudo iptables -A INPUT -s 10.10.10.100 -j DROP

# Logging de paquetes bloqueados
sudo iptables -A INPUT -j LOG --log-prefix "BLOCKED: " --log-level 4

# Guardar reglas
sudo iptables-save > /etc/iptables/rules.v4
```

### 3.2 nftables (reemplazo moderno de iptables)

```bash
# Ver reglas
sudo nft list ruleset

# Tabla básica de firewall
sudo nft add table inet filter
sudo nft add chain inet filter input { type filter hook input priority 0 \; policy drop \; }
sudo nft add rule inet filter input ct state established,related accept
sudo nft add rule inet filter input iif lo accept
sudo nft add rule inet filter input tcp dport 22 accept
sudo nft add rule inet filter input tcp dport {80, 443} accept
```

### 3.3 firewalld (CentOS/RHEL/Fedora)

```bash
# Ver zonas
sudo firewall-cmd --get-active-zones

# Abrir un puerto
sudo firewall-cmd --add-port=8080/tcp --permanent
sudo firewall-cmd --reload

# Servicios predefinidos
sudo firewall-cmd --add-service=http --permanent
sudo firewall-cmd --add-service=https --permanent

# Bloquear un servicio
sudo firewall-cmd --remove-service=telnet --permanent
```

### 3.4 Monitoreo de red

```bash
# Conexiones activas
ss -tulnp          #Puertos abiertos con proceso
netstat -tulnp     #Equivalente clásico

# Tráfico en tiempo real
iftop              # Conexiones por ancho de banda
nethogs            # Tráfico por proceso
bmon               # Monitor de interfaces

# Captura de paquetes
sudo tcpdump -i eth0 -w captura.pcap
sudo tcpdump -i eth0 port 443
sudo tcpdump -i eth0 host 10.0.0.1

# Análisis con Wireshark (GUI)
wireshark captura.pcap
```

## 4. Seguridad de procesos

### 4.1 Linux Capabilities

```bash
# Ver capabilities de un binario
getcap /usr/bin/passwd
# /usr/bin/passwd cap_setuid+ep

# Listar todos los binarios con capabilities
getcap -r / 2>/dev/null

# Asignar capability específica
sudo setcap cap_net_raw+ep /usr/bin/tcpdump
# tcpdump ahora puede capturar paquetes sin ser root

# Eliminar capability
sudo setcap -r /usr/bin/tcpdump

# Ver capabilities de un proceso en ejecución
cat /proc/$(pgrep nginx)/status | grep Cap
```

### 4.2 Namespaces y namespaces de seguridad

```bash
# Ver namespaces de un proceso
ls -la /proc/1/ns/

# Crear namespace aislado
sudo unshare --mount --uts --ipc --net --pid --fork /bin/bash

# Verificar aislamiento
ip addr    # Red aislada
mount      # Montajes aislados
ps aux     # Procesos aislados
```

### 4.3 cgroups (control de recursos)

```bash
# Ver cgroups
cat /proc/self/cgroup

# Limitar memoria de un proceso
sudo cgcreate -g memory:limite_512m
echo 524288000 | sudo tee /sys/fs/cgroup/memory/limite_512m/memory.limit_in_bytes
sudo cgexec -g memory:limite_512m ./mi_app

# Limitar CPU
sudo cgcreate -g cpu:limite_cpu
echo 50000 | sudo tee /sys/fs/cgroup/cpu/limite_cpu/cpu.cfs_quota_us
```

## 5. SELinux y AppArmor

### 5.1 SELinux (Security-Enhanced Linux)

```bash
# Ver estado
getenforce          # Enforcing, Permissive, Disabled
sestatus             # Estado detallado

# Cambiar modo temporalmente
sudo setenforce 0    # Permissive (logs pero no bloquea)
sudo setenforce 1    # Enforcing (bloquea)

# Ver contexto de seguridad
ls -Z /var/www/html/
# -rw-r--r--. root root unconfined_u:object_r:httpd_sys_content_t:s0 index.html

# Cambiar contexto
sudo chcon -t httpd_sys_content_t /var/www/nuevo/

# Restaurar contextos
sudo restorecon -Rv /var/www/

# Boololeans (configuraciones predefinidas)
getsebool -a | grep httpd
sudo setsebool -P httpd_can_network_connect on

# Ver logs de AVC (access vector cache)
sudo ausearch -m avc -ts recent
sudo audit2why < /var/log/audit/audit.log
```

### 5.2 AppArmor (Ubuntu/Debian)

```bash
# Ver estado
sudo aa-status

# Modos por perfil
# enforce: bloquea violaciones
# complain: solo loggea violaciones

# Cambiar modo de un perfil
sudo aa-complain /usr/sbin/nginx
sudo aa-enforce /usr/sbin/nginx

# Crear perfil para una app
sudo aa-genprof /usr/bin/mi_app
# Interactivo: ejecuta la app, usa sus funcionalidades,
# y AppArmor crea el perfil automáticamente

# Verificar perfil
sudo aa-logprof    # Revisa logs y sugiere cambios
```

## 6. Auditoría y logging avanzado

### 6.1 auditd — Auditoría del sistema

```bash
# Estado del servicio
sudo systemctl status auditd

# Verificar reglas de auditoría
sudo auditctl -l

# Auditar acceso a un archivo
sudo auditctl -w /etc/passwd -p wa -k passwd_changes
# -w: watch (monitorear)
# -p: permisos (r=read, w=write, x=execute, a=attribute)
# -k: clave para buscar en logs

# Auditar comandos ejecutados
sudo auditctl -a always,exit -F arch=b64 -S execve -k comandos

# Auditar conexiones de red
sudo auditctl -a always,exit -F arch=b64 -S connect -k conexiones

# Buscar en logs de auditoría
sudo ausearch -k passwd_changes --interpret
sudo ausearch -k comandos -ts today
sudo aureport --summary
sudo aureport --login --summary
```

### 6.2 journalctl — Logs del sistema

```bash
# Logs recientes
journalctl -xe

# Logs de un servicio específico
journalctl -u nginx -f          # seguir en vivo
journalctl -u nginx --since today
journalctl -u sshd --since "1 hour ago"

# Logs de seguridad
journalctl -u auditd
journalctl -k                   # solo kernel

# Errores críticos
journalctl -p err -b             # desde último boot
journalctl -p crit               # solo críticos

# Exportar logs
journalctl --since "2024-01-01" --until "2024-01-31" > /tmp/enero.log
```

### 6.3 Monitoreo de integridad

```bash
# AIDE — Advanced Intrusion Detection Environment
# Instalar
sudo apt install aide

# Inicializar base de datos
sudo aideinit

# Verificar cambios
sudo aide --check

# Actualizar base después de cambios legítimos
sudo aide --update
sudo cp /var/lib/aide/aide.db.new /var/lib/aide/aide.db

# Tripwire (alternativa)
sudo apt install tripwire
sudo tripwire --init
sudo tripwire --check
```

## 7. SSH seguro

### 7.1 Configuración hardened

```bash
# /etc/ssh/sshd_config
PermitRootLogin no                 # No login root directo
PasswordAuthentication no          # Solo claves públicas
PubkeyAuthentication yes
MaxAuthTries 3                     # Máximo 3 intentos
ClientAliveInterval 300            # Timeout 5 min
ClientAliveCountMax 2
AllowUsers admin juan              # Solo usuarios específicos
Protocol 2
X11Forwarding no                   # Sin X11
PermitEmptyPasswords no
LoginGraceTime 30
Banner /etc/issue.net              # Aviso legal
```

### 7.2 Fail2Ban — Protección contra fuerza bruta

```bash
# Instalar
sudo apt install fail2ban

# Configurar para SSH
sudo cp /etc/fail2ban/jail.conf /etc/fail2ban/jail.local
sudo nano /etc/fail2ban/jail.local
```

```ini
[sshd]
enabled = true
port = ssh
filter = sshd
logpath = /var/log/auth.log
maxretry = 3
bantime = 3600
findtime = 600
```

```bash
# Ver estado
sudo fail2ban-client status sshd

# Desbanear IP
sudo fail2ban-client set sshd unbanip 192.168.1.50

# Ver IPs baneadas
sudo fail2ban-client banned
```

## 8. Seguridad de contenedores Linux

```bash
# Docker的安全配置
# No correr como root
docker run --user 1000:1000 mi_app

# Solo lectura de filesystem
docker run --read-only mi_app

# Sin privilege escalation
docker run --security-opt=no-new-privileges mi_app

# Limitar recursos
docker run --memory=256m --cpus=1.0 mi_app

# Ver namespaces de un contenedor
ls -la /proc/$(docker inspect -f '{{.State.Pid}}' contenedor)/ns/
```

## 9. Hardening del sistema

### 9.1 CIS Benchmark (CHECKLIST)

```bash
# === REDUCIR SUPERFICIE DE ATAQUE ===

# Deshabilitar servicios innecesarios
sudo systemctl disable cups        # Impresora (si no usas)
sudo systemctl disable avahi-daemon
sudo systemctl disable bluetooth

# Deshabilitar IPv6 si no se usa
echo "net.ipv6.conf.all.disable_ipv6 = 1" | sudo tee -a /etc/sysctl.conf
sudo sysctl -p

# Configurar kernel sysctl
cat << EOF | sudo tee /etc/sysctl.d/99-security.conf
# Proteger against SYN flood
net.ipv4.tcp_syncookies = 1
net.ipv4.tcp_max_syn_backlog = 2048
net.ipv4.tcp_synack_retries = 2

# Proteger contra IP spoofing
net.ipv4.conf.all.rp_filter = 1
net.ipv4.conf.default.rp_filter = 1

# No aceptar redirecciones ICMP
net.ipv4.conf.all.accept_redirects = 0
net.ipv6.conf.all.accept_redirects = 0

# No enviar redirecciones ICMP
net.ipv4.conf.all.send_redirects = 0

# Habilitar ASLR
kernel.randomize_va_space = 2

# Proteger against ptrace
kernel.yama.ptrace_scope = 1

# Restringir dmesg
kernel.dmesg_restrict = 1

# Proteger symlink y hardlink
fs.protected_hardlinks = 1
fs.protected_symlinks = 1
EOF
sudo sysctl --system
```

### 9.2 Auto-auditoría con Lynis

```bash
# Instalar
sudo apt install lynis

# Ejecutar auditoría completa
sudo lynis audit system

# Resultado:Hardening index
# Target: 67-75 = good, 76+ = excellent
# Revisa las sugerencias y aplica los cambios
```

## 10. Ejercicios prácticos

### Ejercicio 1: Análisis de seguridad del sistema

```bash
# 1. Encuentra todos los archivos con SUID
sudo find / -perm -4000 -type f 2>/dev/null | tee /tmp/suid_files.txt

# 2. Identifica permisos excesivos
sudo find / -perm -777 -type f 2>/dev/null | head -20

# 3. Revisa archivos sin dueño
sudo find / -nouser -o -nogroup 2>/dev/null

# 4. Verifica servicios corriendo como root
ps aux | grep " root "

# 5. Revisa puertos abiertos
ss -tulnp

# Documenta tus hallazgos y evalúa el riesgo de cada uno
```

### Ejercicio 2: Configurar firewall desde cero

```bash
# 1. Política por defecto: denegar todo
sudo iptables -P INPUT DROP
sudo iptables -P FORWARD DROP

# 2. Permitir solo lo necesario
sudo iptables -A INPUT -m state --state ESTABLISHED,RELATED -j ACCEPT
sudo iptables -A INPUT -i lo -j ACCEPT
sudo iptables -A INPUT -p tcp --dport 22 -j ACCEPT
sudo iptables -A INPUT -p tcp --dport 80 -j ACCEPT
sudo iptables -A INPUT -p tcp --dport 443 -j ACCEPT

# 3. Logging
sudo iptables -A INPUT -j LOG --log-prefix "BLOCKED: "

# 4. Verificar que funciona
sudo iptables -L -n -v

# 5. Guardar reglas para persistir tras reboot
sudo iptables-save | sudo tee /etc/iptables/rules.v4
```

### Ejercicio 3: Configurar auditd para monitoreo

```bash
# 1. Monitorear cambios en archivos de configuración
sudo auditctl -w /etc/passwd -p wa -k user_changes
sudo auditctl -w /etc/shadow -p wa -k shadow_changes
sudo auditctl -w /etc/sudoers -p wa -k sudo_changes

# 2. Monitorear ejecución de comandos
sudo auditctl -a always,exit -F arch=b64 -S execve -k comandos

# 3. Monitorear conexiones de red
sudo auditctl -a always,exit -F arch=b64 -S connect -k conexiones

# 4. Verificar que las reglas están activas
sudo auditctl -l

# 5. Generar actividad y revisar logs
sudo ausearch -k user_changes --interpret
sudo aureport --summary
```

### Ejercicio 4: Harden SSH

```bash
# 1. Generar clave Ed25519
ssh-keygen -t ed25519 -C "admin@cyberdefense"

# 2. Copiar al servidor
ssh-copy-id -i ~/.ssh/id_ed25519.pub usuario@servidor

# 3. Configurar sshd_config
sudo nano /etc/ssh/sshd_config
# Apply: PermitRootLogin no, PasswordAuthentication no

# 4. Instalar Fail2Ban
sudo apt install fail2ban
sudo systemctl enable fail2ban

# 5. Verificar
sudo fail2ban-client status sshd
```

### Ejercicio 5: CTF práctico — Escapar de restrictión

```bash
# 1. Explora tu entorno
whoami
id
ls -la /home/
cat /etc/passwd

# 2. Busca oportunidades
find / -perm -4000 2>/devatos
find / -writable -type d 2>/dev/null
find / -name "*.conf" -writable 2>/dev/null

# 3. Priva escalar (en tu VM/lab)
sudo -l
cat /etc/crontab
ls -la /etc/cron*

# 4. Documenta el camino completo desde user hasta root
```

## 📌 Recursos adicionales

| Recurso | Descripción |
|---------|-------------|
| [OverTheWire: Bandit](https://overthewire.org/wargames/bandit/) | Aprender Linux jugando |
| [Linux Survival](https://linuxsurvival.com/) | Tutorial interactivo |
| [CIS Benchmarks](https://www.cisecurity.org/cis-benchmarks/) | Hardening guides |
| [Lynis](https://cisofy.com/lynis/) | Security auditing tool |
| [LinPEAS](https://github.com/carlospolop/PEASS-ng) | Privilege escalation |

## ✏️ Tarea final

1. **Instala Kali o Parrot en una VM** (VirtualBox/VMware)
2. **Ejecuta Lynis** y alcanza un hardening index de 70+
3. **Configura iptables** con política por defecto DENY
4. **Configura auditd** para monitorear `/etc/passwd` y conexiones SSH
5. **Ejercicio CTF:** completa [Bandit](https://overthewire.org/wargames/bandit/) niveles 0-10

> ⏭️ **Siguiente:** [`09-como-seguir-este-repo.md`](./09-como-seguir-este-repo.md) — cómo continuar tu aprendizaje en el campus.
