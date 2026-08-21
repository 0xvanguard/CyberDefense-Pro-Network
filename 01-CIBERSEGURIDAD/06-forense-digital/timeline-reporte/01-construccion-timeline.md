# ⏱️ Construcción de Timeline Forense

> *"La timeline es el mapa del crimen digital. Cada evento, cada timestamp, cada acción construye la narrativa de lo que ocurrió."*

---

## 📋 Tabla de contenido

1. [¿Qué es una timeline forense?](#1-qué-es-una-timeline-forense)
2. [Fuentes de timestamps](#2-fuentes-de-timestamps)
3. [Super timeline con plaso](#3-super-timeline-con-plaso)
4. [Análisis de timeline](#4-análisis-de-timeline)
5. [Correlación de eventos](#5-correlación-de-eventos)
6. [Caso práctico](#6-caso-práctico)
7. [Herramientas](#7-herramientas)
8. [Defensa y detección](#8-defensa-y-detección)
9. [Referencias](#9-referencias)

---

## 1. ¿Qué es una timeline forense?

### Definición

Una **timeline forense** es una representación cronológica de todos los eventos relevantes en un sistema durante un periodo de tiempo específico. Permite reconstruir la secuencia exacta de acciones de un atacante.

### ¿Por qué es fundamental?

```
Sin timeline:
"Atacante entró en algún momento y hizo cosas malas."

Con timeline:
10:00:00 - Atacante descargó herramienta (HTTP GET)
10:00:15 - Ejecutó PowerShell con payload
10:00:20 - Creó reverse shell a 185.234.72.15
10:01:00 - Escaló privilegios con exploit
10:02:00 - Creó usuario persistente
10:05:00 - Exfiltró datos via DNS
10:10:00 - Borró logs para cubrir huellas
```

### Tipos de timeline

| Tipo | Descripción | Herramienta |
|---|---|---|
| **Super timeline** | Todos los artefactos combinados | plaso |
| **Mini timeline** | Solo artefactos clave | MFTECmd, LECmd |
| **Volatilidad timeline** | Basada en RAM | Volatility |
| **Red timeline** | Basada en logs de red | Wireshark, Zeek |

---

## 2. Fuentes de timestamps

### Artefactos con timestamps

| Artefacto | Timestamps | Herramienta |
|---|---|---|
| **$MFT** | $STANDARD_INFO, $FILE_NAME, Created, Modified, Accessed | MFTECmd |
| **$UsnJrnl** | Cada cambio con timestamp | JLnPParser |
| **Prefetch** | Last run, run count | PECmd |
| **LNK files** | Created, modified, accessed, last visited | LECmd |
| **Jump Lists** | Created, modified | JLECmd |
| **Amcache** | Created, modified | AmcacheParser |
| **Browser history** | Visit timestamps | Hindsight, DB Browser |
| **Event Logs** | Event creation time | EvtxECmd |
| **Registry** | Last write time | RegRipper |
| **File system** | atime, mtime, ctime | stat, tsk |

### Formato de timestamps

```bash
# Timestamps NTFS (Windows)
2026-08-20 14:30:00.1234567 (UTC)

# Timestamps EXT4 (Linux)
2026-08-20 14:30:00.1234567890 +0000

# Timestamps Unix
1724178600 (seconds since epoch)

# Converir timestamp Unix
date -d @1724178600
# Output: Wed Aug 20 14:30:00 UTC 2026
```

---

## 3. Super timeline con plaso

### ¿Qué es plaso?

**plaso** (Personal Log Analysis and Search Tool) es la herramienta estándar para crear super timelines. Reúne artefactos de múltiples fuentes en una sola línea de tiempo unificada.

### Instalación

```bash
# Con pip
pip install plaso

# Con Docker
docker pull log2timeline/plaso

# Verificar instalación
log2timeline.py --version
```

### Crear super timeline

```bash
# Paso 1: Crear timeline desde imagen de disco
log2timeline.py --storage-file timeline.plaso imagen.dd

# Paso 2: Crear timeline desde múltiples fuentes
log2timeline.py --storage-file timeline.plaso \
    imagen.dd \
    memory.raw \
    /evidencia/logs/

# Paso 3: Ver información de la timeline
pinfo.py timeline.plaso

# Paso 4: Filtrar eventos
# Solo eventos de un día específico
psort.py -o l2tcsv -w timeline_20260820.csv \
    timeline.plaso "date > '2026-08-20 00:00:00' AND date < '2026-08-20 23:59:59'"

# Solo eventos de tipos específicos
psort.py -o l2tcsv -w timeline_filesystem.csv \
    timeline.plaso "type is 'file_stat'"

# Paso 5: Exportar a CSV para análisis
psort.py -o l2tcsv -w full_timeline.csv timeline.plaso
```

### Formatos de salida

| Formato | Extensión | Uso |
|---|---|---|
| **L2TCsv** | `.csv` | Análisis en Timeline Explorer |
| **JSON** | `.json` | Procesamiento programático |
| **Dynamic** | `.plaso` | Almacenamiento interno |
| **ElasticSearch** | — | SIEM integration |

---

## 4. Análisis de timeline

### Timeline Explorer (Eric Zimmerman)

```
1. Abrir Timeline Explorer
2. File > Open > seleccionar CSV de plaso
3. Navegar eventos cronológicamente
4. Filtrar por:
   - Tipo de evento
   - Timestamp (rango de fechas)
   - Nombre de archivo
   - Usuario
5. Buscar patrones de actividad
```

### Qué buscar en la timeline

| Evento | Significado | Prioridad |
|---|---|---|
| **Descarga de herramienta** | Preparación del ataque | ⭐⭐⭐⭐⭐ |
| **Ejecución de PowerShell** | Payload ejecutado | ⭐⭐⭐⭐⭐ |
| **Creación de usuario** | Persistencia | ⭐⭐⭐⭐⭐ |
| **Modificación de firewall** | Apertura de puertos | ⭐⭐⭐⭐ |
| **Borrado de logs** | Evasión | ⭐⭐⭐⭐ |
| **Conexión de red** | C2 o exfiltración | ⭐⭐⭐⭐ |
| **USB conectado** | Exfiltración física | ⭐⭐⭐ |
| **Archivo modificado** | Manipulación | ⭐⭐⭐ |

### Patrones de ataque en timeline

```
PATRÓN 1: Ataque de día cero
├── 10:00 - Descarga de exploit (HTTP)
├── 10:01 - Ejecución de exploit (Prefetch)
├── 10:01 - Escalada de privilegios (cmdline)
├── 10:02 - Creación de usuario (Registry)
├── 10:05 - Instalación de persistencia (Service)
├── 10:10 - Exfiltración de datos (Network)
└── 10:15 - Borrado de logs (Event Log)

PATRÓN 2: Compromiso de credenciales
├── 08:00 - Login con credenciales válidas (Security Log)
├── 08:05 - Acceso a carpetas sensibles (File System)
├── 08:10 - Descarga de documentos (Browser)
├── 08:15 - Conexión a servidor externo (Network)
└── 08:20 - Logout y borrado de huellas (Event Log)

PATRÓN 3: Malware persistente
├── Día 1: Infección inicial (Prefetch)
├── Día 1: Establecimiento de persistencia (Registry Run)
├── Día 1-7: Beaconing a C2 (Network, cada 30s)
├── Día 3: Escalada de privilegios (cmdline)
├── Día 5: Exfiltración de datos (DNS)
└── Día 7: Borrado de evidencia (File System)
```

---

## 5. Correlación de eventos

### Técnicas de correlación

```bash
# 1. Correlación por timestamp
# Buscar eventos que ocurrieron en ventana de tiempo específica

# 2. Correlación por IP
# Conectar eventos de red con eventos de sistema
grep "185.234.72.15" timeline.csv
grep "443" timeline.csv | grep "ESTABLISHED"

# 3. Correlación por usuario
# Buscar todas las acciones de un usuario específico
grep "admin" timeline.csv

# 4. Correlación por archivo
# Rastrear la vida de un archivo específico
grep "malware.exe" timeline.csv

# 5. Correlación por proceso
# Rastrear todas las acciones de un proceso
grep "PID:5567" timeline.csv
```

### Ejemplo: correlación completa

```bash
# Paso 1: Exportar timeline
psort.py -o l2tcsv -w timeline.csv timeline.plaso

# Paso 2: Buscar eventos de red del C2
grep "185.234.72.15" timeline.csv
# Output:
# 2026-08-20 10:00:00, netscan, powershell.exe → 185.234.72.15:443

# Paso 3: Buscar eventos del proceso que hizo la conexión
grep "powershell.exe" timeline.csv
# Output:
# 2026-08-20 10:00:00, netscan, powershell.exe → 185.234.72.15:443
# 2026-08-20 10:00:00, cmdline, powershell.exe -enc <base64>
# 2026-08-20 09:59:50, file_stat, C:\Users\victim\AppData\Local\Temp\payload.ps1

# Paso 4: Buscar cómo llegó el payload
grep "payload.ps1" timeline.csv
# Output:
# 2026-08-20 09:59:45, file_stat, payload.ps1 created
# 2026-08-20 09:59:40, http, GET http://evil.com/payload.ps1

# PASO 5: Construir narrativa
# 1. Payload descargado desde evil.com
# 2. PowerShell ejecutó payload
# 3. Conexión establecida a C2 server
```

---

## 6. Caso práctico

### Escenario

```
Sistema: Windows 10 workstation
Sospecha: Compromiso con reverse shell
Periodo: 2026-08-20 08:00 - 18:00 UTC
```

### Paso a paso

```bash
# 1. Crear super timeline
log2timeline.py --storage-file timeline.plaso imagen.dd

# 2. Filtrar por el día del incidente
psort.py -o l2tcsv -w timeline_20260820.csv \
    timeline.plaso "date > '2026-08-20 00:00:00' AND date < '2026-08-20 23:59:59'"

# 3. Abrir en Timeline Explorer
# File > Open > timeline_20260820.csv

# 4. Filtrar eventos relevantes
# Usar filtros de Timeline Explorer para:
# - Procesos creados
# - Conexiones de red
# - Archivos creados/modificados
# - Registry changes

# 5. Construir timeline manual
```

### Timeline resultante

```text
2026-08-20 09:45:00 - HTTP GET → evil.com/payload.ps1 (descarga)
2026-08-20 09:59:45 - file_stat: payload.ps1 created
2026-08-20 10:00:00 - cmdline: powershell.exe -enc <base64>
2026-08-20 10:00:00 - netscan: powershell.exe → 185.234.72.15:443
2026-08-20 10:01:00 - cmdline: net user hacker P@ss123 /add
2026-08-20 10:01:05 - cmdline: net localgroup administrators hacker /add
2026-08-20 10:02:00 - registry: Run key created (persistence)
2026-08-20 10:05:00 - file_stat: Documents/config.xlsx copied to Temp
2026-08-20 10:05:10 - http: POST to evil.com/exfil (data upload)
2026-08-20 10:10:00 - file_stat: logs/security.evtx deleted
2026-08-20 10:10:05 - file_stat: logs/system.evtx deleted
```

### Conclusiones

1. **Entry point:** Descarga de payload via HTTP (09:45)
2. **Execution:** PowerShell con base64 (10:00)
3. **Persistence:** Usuario creado + Run key (10:01-10:02)
4. **Exfiltration:** Datos copiados y enviados (10:05)
5. **Evasion:** Logs borrados (10:10)

---

## 7. Herramientas

| Herramienta | Uso | Plataforma |
|---|---|---|
| **plaso** | Crear super timeline | Linux |
| **Timeline Explorer** | Visualizar timeline | Windows |
| **MFTECmd** | Parsear $MFT | Windows |
| **LECmd** | Parsear LNK files | Windows |
| **JLECmd** | Parsear Jump Lists | Windows |
| **PECmd** | Parsear Prefetch | Windows |
| **AmcacheParser** | Parsear Amcache | Windows |
| **EvtxECmd** | Parsear Event Logs | Windows |
| **LogParser** | Consultas SQL sobre logs | Windows |

---

## 8. Defensa y detección

### Para Blue Team

| Técnica atacante | Detección | Implementación |
|---|---|---|
| **Timestomping** | Comparar timestamps múltiples | Timeline con múltiples fuentes |
| **Borrado de logs** | Logs en SIEM remoto | Centralización de logs |
| **Evasión temporal** | Monitoreo 24/7 | Alertas en tiempo real |
| **Ofuscación** | Análisis de patrones | Machine learning en SIEM |

---

## 9. Referencias

| Recurso | URL |
|---|---|
| **plaso** | [https://plaso.readthedocs.io/](https://plaso.readthedocs.io/) |
| **Timeline Explorer** | [https://ericzimmerman.github.io/](https://ericzimmerman.github.io/) |
| **SANS FOR508** | [https://www.sans.org/cyber-security-courses/advanced-incident-response/](https://www.sans.org/cyber-security-courses/advanced-incident-response/) |
| **NIST SP 800-86** | [https://csrc.nist.gov/pubs/sp/800/86/final](https://csrc.nist.gov/pubs/sp/800/86/final) |

---

## 📝 Entregable de portafolio

```markdown
# Timeline Forense — Caso INC-2026-0847

## Contexto
- Sistema: Windows 10 workstation
- Periodo: 2026-08-20 08:00 - 18:00 UTC
- Herramientas: plaso, MFTECmd, PECmd, LECmd

## Timeline reconstruida
| Timestamp | Evento | Fuente |
|---|---|---|
| 09:45:00 | Descarga de payload HTTP | Browser history |
| 09:59:45 | Creación de archivo | $MFT |
| 10:00:00 | Ejecución PowerShell | Prefetch, cmdline |
| 10:00:00 | Conexión a C2 | Netscan |
| 10:01:00 | Creación de usuario | Event Log |
| 10:02:00 | Persistencia Registry | Registry |
| 10:05:00 | Exfiltración de datos | HTTP log |
| 10:10:00 | Borrado de logs | $UsnJrnl |

## Conclusiones
- Ataque completo en 25 minutos
- Persistence: usuario + Run key
- Exfiltración: documentos corporativos
- Evasión: borrado de logs

## Evidencia
- Timeline: /evidencia/caso001/timeline.csv
- Reporte: /evidencia/caso001/timeline_report.pdf
```

---

**[⬅ Volver al módulo](../README.md)** · **[→ Reporte Forense](./02-reporte-forense.md)**
