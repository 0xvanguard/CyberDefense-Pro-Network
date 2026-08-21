# 🧠 Volatilidad y Análisis de Memoria RAM

> *"La memoria RAM es la puerta de entrada a lo que realmente está pasando en un sistema. Todo está ahí: credenciales, conexiones, procesos ocultos."*

---

## 📋 Tabla de contenido

1. [¿Qué es la memoria volátil?](#1-qué-es-la-memoria-volátil)
2. [Qué se puede encontrar en RAM](#2-qué-se-puede-encontrar-en-ram)
3. [Adquisición de memoria](#3-adquisición-de-memoria)
4. [Formatos de volcado de memoria](#4-formatos-de-volcado-de-memoria)
5. [Volatility 3: guía completa](#5-volatility-3-guía-completa)
6. [IOC en memoria](#6-ioc-en-memoria)
7. [Caso práctico: análisis completo](#7-caso-práctico-análisis-completo)
8. [Defensa y detección](#8-defensa-y-detección)
9. [Referencias](#9-referencias)

---

## 1. ¿Qué es la memoria volátil?

### Definición

La **memoria volátil** (RAM) es almacenamiento temporal que **pierde su contenido al apagar el sistema**. A diferencia del disco duro, los datos en RAM se pierden inmediatamente cuando se corta la energía.

```
┌─────────────────────────────────────────────────────┐
│                    MEMORIA RAM                       │
├─────────────────────────────────────────────────────┤
│  Procesos en ejecución (incluso los ocultos)        │
│  Conexiones de red activas                          │
│  Claves de cifrado (BitLocker, LUKS)               │
│  Contraseñas en texto plano                         │
│  DLLs inyectadas / código malicioso                │
│  Comandos ejecutados recientemente                 │
│  Archivos abiertos por procesos                     │
│  Variables de entorno                               │
│  Handles y descriptores de archivos                 │
│  Cache DNS                                          │
└─────────────────────────────────────────────────────┘
```

### ¿Por qué es tan importante?

| Dato en RAM | No está en el disco |
|---|---|
| Claves de cifrado activas | Las claves se generan al descifrar |
| Conexiones de red activas | Las conexiones se cierran al apagar |
| Procesos en memoria | Los procesos se eliminan al apagar |
| DLLs inyectadas | La inyección es temporal |
| Comandos de PowerShell | Los comandos no se guardan en logs por defecto |
| Credenciales de sesión | Las sesiones se cierran al apagar |

### Volatilidad: orden de importancia

```
MÁS VOLÁTIL                                    MENOS VOLÁTIL
    │                                               │
    ▼                                               ▼
┌─────────┐  ┌─────────┐  ┌─────────┐  ┌─────────┐  ┌─────────┐
│  CPU /  │  │  RAM /  │  │  Red /  │  │  Disco  │  │  Logs   │
│ Caché   │  │ Estado  │  │ARP/DNS  │  │  duro   │  │remotos  │
└─────────┘  └─────────┘  └─────────┘  └─────────┘  └─────────┘
  Nanoseg    Segundos     Minutos      Horas        Días/meses
```

---

## 2. Qué se puede encontrar en RAM

### Procesos ocultos

```
┌─────────────────────────────────────────────────┐
│  Árbol de procesos legítimo:                     │
│                                                  │
│  System (PID 4)                                  │
│  ├── csrss.exe (PID 340)                        │
│  ├── wininit.exe (PID 476)                      │
│  ├── winlogon.exe (PID 528)                     │
│  └── explorer.exe (PID 3456)                    │
│       └── cmd.exe (PID 4012)                    │
│           └── powershell.exe (PID 5567) ← SOSPECHOSO │
│                                                  │
│  Procesos sin padre legítimo:                    │
│  svchost.exe (PID 888) ← SIN padre svchost      │
│  lsass.exe (PID 999) ← cadena inusual            │
└─────────────────────────────────────────────────┘
```

### Conexiones de red

```bash
# Lo que ves en memoria:
# PID 5567: powershell.exe → 185.234.72.15:443 (ESTABLISHED)
# PID 4012: cmd.exe → 10.10.10.5:8080 (ESTABLISHED)
# PID 888: svchost.exe → 192.168.1.1:53 (ESTABLISHED)

# Indicadores:
# - Conexión desde powershell.exe → sospechoso
# - Puerto 443 a IP externa no habitual → posible C2
# - Puerto 8080 interno → pivoting
```

### Credenciales en texto plano

```
# Lo que Volatility puede extraer:
Username: administrator
Hash NTLM: aad3b435b51404eeaad3b435b51404ee:e0fb1fb8f4...
Password (plaintext): P@ssw0rd123!

# Credenciales de navegador:
https://mail.company.com → admin@company.com / MyP@ssword!
https://aws.amazon.com → AKIA... / secretkey123
```

### Código inyectado

```bash
# Lo que malfind detecta:
# PID 3456 (explorer.exe) tiene memoria ejecutable en:
# 0x000002a4c8d00000 - RWX (Read-Write-Execute)
# Contenido: shellcode de 400 bytes
# Patrón: 0x48, 0x89, 0xe5, 0x48, 0x83... (x64 shellcode)

# PID 5567 (powershell.exe) tiene DLL inyectada:
# memory.dll (no en disco)
# Tamaño: 120KB
# Funciones exportadas: RunShell, DownloadExec
```

---

## 3. Adquisición de memoria

### Herramientas de adquisición

#### Linux: avml (recomendado)

```bash
# Descargar avml
wget https://github.com/microsoft/avml/releases/latest/download/avml
chmod +x avml

# Capturar RAM
sudo ./avml memory.lime

# Verificar tamaño (debe ser ≈ RAM instalada)
ls -lh memory.lime
# -rw-r--r-- 1 user user 16G memory.lime  (para 16GB de RAM)
```

#### Windows: winpmem

```bash
# Descargar winpmem
# https://github.com/Velocidex/winpmem/releases

# Ejecutar como Administrador
winpmem_4.0.exe memory.raw

# Verificar
dir memory.raw
```

#### Windows: DumpIt

```
1. Descargar DumpIt desde Comae Technologies
2. Ejecutar como Administrador
3. DumpIt crea memory.raw automáticamente
4. Verificar tamaño del archivo
```

### Precauciones críticas

| Precaución | Razón |
|---|---|
| **Ejecutar desde USB booteable** | No modificar la memoria del sistema |
| **No instalar software** | La instalación altera la memoria |
| **Ejecutar lo más rápido posible** | La RAM se modifica constantemente |
| **No conectar a red** | Las conexiones generan tráfico nuevo |
| **Documentar el proceso** | Cadena de custodia incluye hora exacta |

### Decisión: ¿Apagar o no?

| Escenario | Recomendación | Razón |
|---|---|---|
| **Servidor encendido** | NO apagar — capturar RAM primero | Se pierde evidencia volátil |
| **Laptop con bitlocker** | NO apagar — bypass requiere RAM | Claves en memoria |
| **Estación de trabajo** | Capturar RAM → apagar → disco | Equilibrio |
| **Dispositivo apagado** | NO encender — adquirir disco directamente | Encender altera evidencia |

---

## 4. Formatos de volcado de memoria

| Formato | Herramienta | Plataforma | Uso |
|---|---|---|---|
| **LiME** | avml, LiME | Linux | Estándar para Linux |
| **RAW** | winpmem, DumpIt | Windows | Formato sin procesar |
| **VMEM** | VMware, VirtualBox | Virtual | Volcado de VM |
| **AFF4** | avml | Multi | Formato abierto forense |
| **Hibernation file** | — | Windows | `hiberfil.sys` |
| **Pagefile** | — | Windows | `pagefile.sys` |
| **Swap** | — | Linux | `/swapfile` o `/dev/sda2` |

### Archivos especiales de Windows

```bash
# Estos archivos contienen datos de memoria
C:\hiberfil.sys     → Volcado de hibernación (puede contener RAM)
C:\pagefile.sys     → Archivo de paginación (datos de memoria)
C:\Swapfile.sys     → Swap de UWP apps
```

---

## 5. Volatility 3: guía completa

### Instalación

```bash
# Opción 1: pip
pip install volatility3

# Opción 2: desde source
git clone https://github.com/volatilityfoundation/volatility3.git
cd volatility3
pip install -r requirements.txt

# Verificar instalación
vol -h
```

### Comandos esenciales

#### Información del sistema

```bash
# Identificar el volcado (perfil, OS, arquitectura)
vol -f memory.raw windows.info

# Output:
# Volatility 3 Framework 2.5.0
# Variable              Value
# Kernel Base           0xf80002a4c8000000
# DTB                   0x1ad000
# Symbols               file:///.../windows...
# Is64Bit               True
# IsPAE                 False
# Primary Layer         Intel32e
# Memory Layer          FileLayer
# KdVersionBlock        0xf80002a4c8d4e2b8
# Major/Minor           15.19041
# Machine Type          34404
# KeNumberProcessors    8
# SystemTime            2026-08-20 14:30:00.000000
# NtBuildLab            19041.1.amd64fre.vb_release.191206-1406
# NtProductType         NtProductWinNt
# NtSystemRoot          C:\Windows
```

#### Procesos

```bash
# Lista de procesos
vol -f memory.raw windows.pslist

# Árbol de procesos (detecta procesos hijos sospechosos)
vol -f memory.raw windows.pstree

# Líneas de comando de cada proceso (ORO PURO)
vol -f memory.raw windows.cmdline

# DLLs cargadas por un proceso
vol -f memory.raw windows.dlllist --pid 1234

# Handles abiertos por un proceso
vol -f memory.raw windows.handles --pid 1234

# Archivos abiertos en memoria
vol -f memory.raw windows.filescan
```

#### Red

```bash
# Conexiones de red activas
vol -f memory.raw windows.netscan

# Output:
# Offset        Proto  LocalAddr       LocalPort  ForeignAddr      ForeignPort  State         PID  Owner          Created
# 0xe1234567    TCPv4  10.10.10.100    49732      185.234.72.15    443          ESTABLISHED   5567 powershell.exe 2026-08-20 14:25:00
# 0xe1234568    TCPv4  10.10.10.100    49733      192.168.1.1      53           ESTABLISHED   888  svchost.exe    2026-08-20 14:20:00

# Socket listening
vol -f memory.raw windows.netscan | grep LISTENING
```

#### Código malicioso

```bash
# Detectar código inyectado en procesos
vol -f memory.raw windows.malfind

# Output:
# PID   Process         Start VPN       End VPN         Tag  Hexdump                  Disasm
# 3456  explorer.exe    0x2a4c8d00000   0x2a4c8d10000  VadS 48 89 e5 48 83...      push rbp; mov rbp, rsp...

# Filtrar por proceso específico
vol -f memory.raw windows.malfind --pid 3456

# Volcado de memoria sospechosa
vol -f memory.raw windows.malfind --pid 3456 --dump
# Genera archivo PID.3456.0x2a4c8d00000.dmp
```

#### Credenciales

```bash
# Dump de hashes NTLM
vol -f memory.raw windows.hashdump

# Dump de credenciales LSA
vol -f memory.raw windows.lsadump

# Caché de credenciales
vol -f memory.raw windows.cachedump
```

#### Servicios y drivers

```bash
# Servicios en ejecución
vol -f memory.raw windows.svcscan

# Drivers cargados
vol -f memory.raw windows.driverscan

# Módulos (DLLs del kernel)
vol -f memory.raw windows.modules
```

#### Registro

```bash
# Hives de registro en memoria
vol -f memory.raw windows.registry.hivelist

# Listar keys de una hive
vol -f memory.raw windows.registry.printkey --key "Software\Microsoft\Windows\CurrentVersion\Run"

# Buscar valores específicos
vol -f memory.raw windows.registry.printkey --key "Software\Microsoft\Windows\CurrentVersion\Run" -v
```

### Resumen de plugins útiles

| Plugin | Qué extrae | Prioridad |
|---|---|---|
| `windows.info` | Información del sistema | ⭐⭐⭐⭐⭐ |
| `windows.pslist` | Lista de procesos | ⭐⭐⭐⭐⭐ |
| `windows.pstree` | Árbol de procesos | ⭐⭐⭐⭐⭐ |
| `windows.cmdline` | Comandos ejecutados | ⭐⭐⭐⭐⭐ |
| `windows.netscan` | Conexiones de red | ⭐⭐⭐⭐⭐ |
| `windows.malfind` | Código inyectado | ⭐⭐⭐⭐⭐ |
| `windows.hashdump` | Credenciales NTLM | ⭐⭐⭐⭐ |
| `windows.dlllist` | DLLs cargadas | ⭐⭐⭐⭐ |
| `windows.filescan` | Archivos abiertos | ⭐⭐⭐⭐ |
| `windows.handles` | Handles de procesos | ⭐⭐⭐ |
| `windows.svcscan` | Servicios | ⭐⭐⭐ |
| `windows.registry.hivelist` | Hives de registro | ⭐⭐⭐ |

---

## 6. IOC en memoria

### Indicadores de compromiso (IOC) que se buscan en RAM

| IOC | Qué buscar | Plugin |
|---|---|---|
| **Proceso sin padre legítimo** | `svchost.exe` sin `services.exe` como padre | `pstree` |
| **cmd.exe / powershell.exe con base64** | Argumentos ofuscados | `cmdline` |
| **Conexión a IP externa no habitual** | IPs que no son del SIEM/infra | `netscan` |
| **DLL inyectada en proceso legítimo** | Memoria RWX en procesos de sistema | `malfind` |
| **mimikatz en memoria** | Strings o código de mimikatz | `malfind`, `cmdline` |
| **lsass.exe accediendo a credenciales** | Acceso inusual a SAM/LSA | `hashdump`, `lsadump` |
| **Archivo .exe temporal** | Ejecutables en carpetas temporales | `filescan` |
| **Proceso con nombre sospechoso** | Nombres genéricos o aleatorios | `pslist` |

### Ejemplo: detectar mimikatz en memoria

```bash
# 1. Buscar procesos sospechosos
vol -f memory.raw windows.pstree | grep -i "mimikatz\|sekurlsa\|kerberos"
# Output: no encontrado (mimikatz puede no estar como proceso)

# 2. Buscar en comandos
vol -f memory.raw windows.cmdline | grep -i "mimikatz\|sekurlsa"
# Output: PID 5678: powershell.exe -enc <base64>

# 3. Buscar código inyectado
vol -f memory.raw windows.malfind
# Output: PID 999 (lsass.exe) tiene memoria RWX sospechosa

# 4. Verificar conexión de red
vol -f memory.raw windows.netscan | grep "5678\|999"
# Output: PID 5678 → 185.234.72.15:443 ESTABLISHED

# 5. Extraer evidencia
vol -f memory.raw windows.malfind --pid 999 --dump
```

### Ejemplo: detectar reverse shell

```bash
# 1. Buscar procesos con conexiones inusuales
vol -f memory.raw windows.netscan | grep ESTABLISHED

# 2. Identificar qué proceso tiene la conexión
vol -f memory.raw windows.pslist | grep "PID del proceso"

# 3. Ver comandos del proceso
vol -f memory.raw windows.cmdline --pid <PID>
# Output: cmd.exe /c powershell -nop -w hidden -c "IEX..."

# 4. Verificar código inyectado
vol -f memory.raw windows.malfind --pid <PID>

# 5. Extraer evidencia
vol -f memory.raw windows.malfind --pid <PID> --dump
```

---

## 7. Caso práctico: análisis completo

### Escenario

```
Sistema: Windows 10, 16GB RAM
Volcado: memory.raw (16GB)
Sospecha: workstation comprometida, reverse shell activo
```

### Paso a paso

```bash
# PASO 1: Información del sistema
vol -f memory.raw windows.info
# → Windows 10 19041, 64-bit, 8 cores

# PASO 2: Lista de procesos
vol -f memory.raw windows.pslist > pslist.txt
# Buscar procesos anómalos:
# - powershell.exe con PID inusual
# - cmd.exe sin padre legítimo
# - .exe en carpetas temporales

# PASO 3: Árbol de procesos (CRÍTICO)
vol -f memory.raw windows.pstree > pstree.txt
# Buscar:
# - procesos huérfanos (sin padre)
# - procesos con nombre similar a legítimos pero distinto
# - cadenas de procesos inusuales

# PASO 4: Comandos ejecutados
vol -f memory.raw windows.cmdline > cmdline.txt
# Buscar:
# - powershell con -enc (base64)
# - cmd.exe ejecutando scripts descargados
# - comandos con URLs o IPs

# PASO 5: Conexiones de red
vol -f memory.raw windows.netscan > netscan.txt
# Buscar:
# - Conexiones ESTABLISHED a IPs externas
# - Conexiones desde procesos inusuales
# - Puertos inusuales (443 con procesos normales, 8080 sospechoso)

# PASO 6: Código inyectado
vol -f memory.raw windows.malfind > malfind.txt
# Buscar:
# - Memoria RWX en procesos de sistema
# - Shellcode en explorer.exe, svchost.exe
# - DLLs no encontradas en disco

# PASO 7: DLLs cargadas
vol -f memory.raw windows.dlllist --pid <PID sospechoso> > dlllist.txt
# Buscar:
# - DLLs en carpetas temporales
# - DLLs no firmadas
# - DLLs con nombres genéricos

# PASO 8: Credenciales
vol -f memory.raw windows.hashdump > hashdump.txt
vol -f memory.raw windows.lsadump > lsadump.txt
# Buscar:
# - Credenciales de administrador
# - Caché de credenciales
# - Kerberos tickets

# PASO 9: Artefactos de ejecución
vol -f memory.raw windows.filescan > filescan.txt
# Buscar:
# - .exe en C:\Users\*\AppData\Local\Temp\
# - Scripts en C:\Users\*\Downloads\
# - Archivos con extensiones .ps1, .bat, .vbs
```

### Análisis de resultados

```
HALLAZGOS:
1. powershell.exe (PID 5567) ejecutando con -enc (base64)
2. Conexión ESTABLISHED desde PID 5567 a 185.234.72.15:443
3. Código RWX inyectado en PID 5567
4. DLL memory.dll (120KB) cargada en memoria (no en disco)
5. NTLM hashes extraídos (administrator, guest)

CONCLUSIÓN:
- Reverse shell activo通过 PowerShell
- Conexión a C2 server (185.234.72.15)
- DLL inyectada para persistencia en memoria
```

---

## 8. Defensa y detección

### Para Blue Team

| Técnica atacante | Detección | Herramienta |
|---|---|---|
| **Reverse shell** | Conexiones inusuales en RAM | Volatility netscan |
| **Mimikatz** | Código inyectado en lsass | Volatility malfind |
| **PowerShell ofuscado** | Argumentos base64 en cmdline | Volatility cmdline |
| **DLL injection** | Memoria RWX en procesos legítimos | Volatility malfind |
| **Proceso huérfano** | Proceso sin padre legítimo | Volatility pstree |

### Monitoreo preventivo

```bash
# 1. Habilitar Logging avanzado de PowerShell
# (Group Policy > Administrative Templates > Windows Components)

# 2. Monitorear eventos de creación de procesos
# Event ID 4688: Process Creation

# 3. Monitorear inyección de código
# Event ID 8: CreateRemoteThread

# 4. Habilitar Sysmon
# (System Monitor de Microsoft)
```

---

## 9. Referencias

| Recurso | URL |
|---|---|
| **Volatility 3** | [https://github.com/volatilityfoundation/volatility3](https://github.com/volatilityfoundation/volatility3) |
| **Volatility 2** | [https://github.com/volatilityfoundation/volatility](https://github.com/volatilityfoundation/volatility) |
| **avml** | [https://github.com/microsoft/avml](https://github.com/microsoft/avml) |
| **winpmem** | [https://github.com/Velocidex/winpmem](https://github.com/Velocidex/winpmem) |
| **SANS FOR508** | [https://www.sans.org/cyber-security-courses/advanced-incident-response/](https://www.sans.org/cyber-security-courses/advanced-incident-response/) |
| **Volatility Lab** | [https://www.win4n6.com/](https://www.win4n6.com/) |

---

## 📝 Entregable de portafolio

```markdown
# Análisis de Memoria — Caso INC-2026-0847

## Contexto
- Volcado: memory.raw (16GB, Windows 10 19041)
- Sospecha: workstation comprometida
- Herramienta: Volatility 3

## Hallazgos
1. **Procesos anómalos:**
   - powershell.exe (PID 5567) con argumentos base64
   - Conexión a 185.234.72.15:443 (C2 server)

2. **Código inyectado:**
   - Memoria RWX en PID 5567 (shellcode de 400 bytes)
   - DLL memory.dll (no encontrada en disco)

3. **Credenciales comprometidas:**
   - NTLM hash de administrator extraído
   - Hash de 3 usuarios más

## Conclusión
- Reverse shell activo通过 PowerShell
- Conexión a C2 server confirmada
- DLL inyectada para persistencia en memoria

## Evidencia
- Volcado: /evidencia/caso001/memory.raw (SHA-256: 4b3a9f...e2c1)
- Extracciones: /evidencia/caso001/volatility/
- Reporte: /evidencia/caso001/analisis_memoria.pdf
```

---

**[⬅ Volver al módulo](../README.md)** · **[→ Herramientas de Memoria](./02-herramientas-memoria.md)**
