# 💾 Análisis de Disco — Sistemas de Archivos e Imágenes Forenses

> *"El disco duro es la memoria del sistema. Cada archivo borrado, cada movimiento, cada error留下了 rastros."*

---

## 📋 Tabla de contenido

1. [Sistemas de archivos](#1-sistemas-de-archivos)
2. [Particiones y estructura del disco](#2-particiones-y-estructura-del-disco)
3. [NTFS: artefactos forenses clave](#3-ntfs-artefactos-forenses-clave)
4. [EXT4: artefactos forenses](#4-ext4-artefactos-forenses)
5. [Archivos borrados: recuperación](#5-archivos-borrados-recuperación)
6. [Análisis de disco con The Sleuth Kit](#6-análisis-de-disco-con-the-sleuth-kit)
7. [Análisis con Autopsy](#7-análisis-con-autopsy)
8. [Artefactos de Windows](#8-artefactos-de-windows)
9. [Defensa y detección](#9-defensa-y-detección)
10. [Referencias](#10-referencias)

---

## 1. Sistemas de archivos

### Comparativa forense

| Característica | NTFS | EXT4 | APFS | FAT32 | exFAT |
|---|---|---|---|---|---|
| **Usado en** | Windows | Linux | macOS | Universal | USB/moderno |
| **Journal** | ✅ $LogFile | ✅ journaled | ✅ copy-on-write | ❌ | ❌ |
| **Cifrado** | EFS | eCryptfs | FileVault | ❌ | ❌ |
| **Permisos** | ACLs POSIX | POSIX | ACLs | ❌ | ❌ |
| **Tamaño máx archivo** | 16 EB | 16 TB | 8 EB | 4 GB | 16 EB |
| **Forensicmente** | Muy rico | Rico | complejo | Simple | Simple |

### ¿Por qué importa el sistema de archivos?

- **NTFS:** tiene $MFT, $LogFile, $UsnJrnl, $I30 — mucho artefacto
- **EXT4:** tiene journal, inodes, extents — menos artefactos pero valiosos
- **APFS:** copy-on-write complica la recuperación pero preserva más datos
- **FAT32/exFAT:** simple, sin journal — menos artefactos pero más fácil de analizar

---

## 2. Particiones y estructura del disco

### Layout típico de un disco

```
┌─────────────────────────────────────────────────────────┐
│                    MBR / GPT Header                      │
├──────────────┬──────────────┬──────────────┬────────────┤
│  Partición 1 │  Partición 2 │  Partición 3 │  Partición │
│  (EFI/Boot)  │  (Windows)   │  (Linux)     │  (Datos)   │
│  ~500MB      │  ~200GB      │  ~200GB      │  ~600GB    │
└──────────────┴──────────────┴──────────────┴────────────┘
```

### MBR vs GPT

| Característica | MBR | GPT |
|---|---|---|
| **Máx disco** | 2 TB | 9.4 ZB |
| **Particiones máx** | 4 (primarias) | 128 |
| **Backup** | ❌ No | ✅ Sí (al final del disco) |
| **Integridad** | CRC32 | CRC32 + Backup |
| **Uso actual** | Legacy | Estándar (UEFI) |

### Verificar particiones de una imagen

```bash
# Con The Sleuth Kit
mmls imagen.dd

# Output ejemplo (GPT):
# Slot    Start        End          Length       Description
# 000:  -----  00000000  00000000  00000001  Safety Table
# 001:  -----  00000001  00002047  00002047  EFI GPT
# 002:  -----  00002048  00004095  00002047  EFI System
# 003:  GPT:0  00004096  41943006  41938911  Microsoft basic data
# 004:  GPT:1  41943007  83886046  41943040  Linux filesystem

# Con fdisk
fdisk -l imagen.dd
```

---

## 3. NTFS: artefactos forenses clave

### El Master File Table ($MFT)

El $MFT es el **corazón de NTFS**: cada archivo tiene una entrada de 1024 bytes.

```bash
# Localizar el $MFT en una imagen
fls -r -o 2048 imagen.dd | head -20

# Extraer el $MFT
icat -o 2048 imagen.dd 0 > MFT_raw

# Parsear con MFTECmd (Eric Zimmerman)
MFTECmd.exe -f MFT_raw --json Output/
```

### Artefactos NTFS detallados

| Artefacto | Ubicación | Qué revela | Herramienta |
|---|---|---|---|
| **$MFT** | Raíz de partición | Cada archivo creado/modificado/borrado | MFTECmd |
| **$UsnJrnl** | `C:\$UsnJrnl` | Historial de cambios en archivos | JLnPParser |
| **$LogFile** | Raíz de partición | Journal de transacciones NTFS | LogFileParser |
| **$I30** (INDEX) | Directorios | Lista de archivos en directorio | LECmd |
| **$Secure** | Raíz | Permisos de cada archivo | — |
| **$Extend** | Raíz | Metadatos extendidos | — |

### $MFT: estructura de un registro

```
┌─────────────────────────────────────────┐
│ Registro del $MFT (1024 bytes)          │
├─────────────────────────────────────────┤
│ 0x00-0x03: "FILE" signature             │
│ 0x04-0x05: Offset al primer attribute   │
│ 0x16-0x17: Flag: activo/inactivo        │
│ 0x20-0x27: MFT entry number             │
│ 0x2C-0x2F: Size del primer attribute    │
│ 0x40-0x47: MFT reference del padre      │
│ 0x48-0x4F: Timestamp $STANDARD_INFO     │
│ 0x50-0x57: Timestamp $FILE_NAME         │
│ 0x80-0x87: $DATA attribute (contenido)  │
└─────────────────────────────────────────┘
```

### $UsnJrnl: historial de cambios

```bash
# El $UsnJrnl registra cada cambio en archivos
# Formato de cada entrada:
# - Nombre del archivo
# - Timestamp
# - Tipo de cambio (CREATE, DELETE, MODIFY, RENAME, etc.)
# - Reason (DATA_OVERWRITE, DATA_EXTEND, etc.)

# Parsear con JLnPParser
JLnPParser.exe -f "C:\$UsnJrnl:$J" --csv Output/

# Filtrar por archivos eliminados
grep -i "DELETE" Output/UsnJrnl.csv
```

---

## 4. EXT4: artefactos forenses

### Estructura de EXT4

```bash
# Verificar sistema de archivos
fsstat -f ext4 -o 2048 imagen.dd

# Verificar superblock
dcat -f ext4 -o 2048 imagen.dd 1 > superblock.txt
```

### Inodes: la unidad básica

```bash
# Listar archivos con sus inodes
fls -f ext4 -r -o 2048 imagen.dd

# Ver info de un inode específico
istat -f ext4 -o 2048 imagen.dd 12345

# Output:
# Inode: 12345
# Allocated: Yes
# Root: No
# Size: 4096
# Permissions: rwxr-xr-x
# Owner: 1000
# Group: 1000
# Access Time: 2026-08-20 10:00:00
# Inode Change: 2026-08-20 09:55:00
# Modify Time: 2026-08-20 09:50:00
# Deleted: No
```

### Journal: recuperar datos borrados

```bash
# El journal de EXT4 registra transacciones
# Puede contener datos de archivos borrados

# Extraer journal
dcat -f ext4 -o 2048 imagen.dd 8 > journal.img

# Analizar journal
fls -f journal -r journal.img
```

---

## 5. Archivos borrados: recuperación

### ¿Cómo se borran archivos?

| Método | NTFS | EXT4 | Recuperable |
|---|---|---|---|
| **Delete (Papelera)** | Flag $MFT | Removed from dir | ✅ Sí |
| **Shift+Delete** | Flag $MFT, espacio marcado libre | Removed from dir | ⚠️ Parcialmente |
| **Format** | Nuevo $MFT | Nuevo journal | ⚠️ Con tools especiales |
| **Secure erase** | Sobreescrito múltiples veces | Sobreescrito | ❌ No |

### Recuperación con The Sleuth Kit

```bash
# Listar archivos borrados (marcador = deleted)
fls -r -d -o 2048 imagen.dd
# Output:
#   r/r 12345:    del_doc_secreto.pdf
#   r/r 12346:    del_informe.xlsx
#   d/d 12347:    del_carpeta_backup

# Extraer un archivo borrado por inode
icat -o 2048 imagen.dd 12345 > doc_recuperado.pdf

# Recuperar TODOS los archivos borrados de una partición
tsk_recover -o 2048 imagen.dd /salida_recuperacion/
ls /salida_recuperacion/
```

### Recuperación con photorec

```bash
# PhotoRec: recupera archivos por tipo (no por nombre)
photorec /d /salida imagen.dd

# Seleccionar:
# 1. Partición a analizar
# 2. Sistema de archivos (o [Unknown])
# 3. Directorio de salida
# 4. Tipos de archivo a recuperar
```

### Recuperación con Recuva (Windows, GUI)

```
1. Abrir Recuva
2. Seleccionar unidad o imagen
3. Tipo de archivo: All Files
4. Modo: Deep Scan
5. Escanear y recuperar
```

---

## 6. Análisis de disco con The Sleuth Kit

### Comandos esenciales

```bash
# 1. Ver particiones
mmls imagen.dd

# 2. Listar archivos recursivamente
fls -r -o 2048 imagen.dd
# -r: recursivo
# -o: offset de la partición

# 3. Listar archivos borrados
fls -d -r -o 2048 imagen.dd

# 4. Ver metadata de un archivo
fstat -o 2048 imagen.dd 12345

# 5. Extraer un archivo por inode
icat -o 2048 imagen.dd 12345 > archivo_extraido

# 6. Buscar archivos por nombre
ffind -o 2048 imagen.dd -n "documento.pdf"

# 7. Buscar archivos por contenido (grep en disco)
grep -o "password" imagen.dd | head -20

# 8. Recuperar archivos borrados
tsk_recover -o 2048 imagen.dd /salida/
```

### Flujo de trabajo completo

```bash
# Paso 1: Verificar que la imagen es válida
mmls imagen.dd
# Debe mostrar particiones

# Paso 2: Listar archivos
fls -r -o 2048 imagen.dd > archivos.txt
wc -l archivos.txt
# Verificar cantidad de archivos

# Paso 3: Buscar archivos borrados
fls -d -r -o 2048 imagen.dd > borrados.txt
cat borrados.txt

# Paso 4: Buscar artefactos clave
ffind -o 2048 imagen.dd -n "NTUSER.DAT"
ffind -o 2048 imagen.dd -n "Amcache.hve"
ffind -o 2048 imagen.dd -n "Prefetch"

# Paso 5: Extraer archivos relevantes
icat -o 2048 imagen.dd <inode_prefetch> > prefetch/
```

---

## 7. Análisis con Autopsy

### Instalación

```bash
# Linux
wget https://github.com/sleuthkit/autopsy/releases/latest/download/autopsy-*.deb
sudo dpkg -i autopsy-*.deb

# Windows
# Descargar desde https://www.sleuthkit.org/autopsy/
```

### Crear un caso

```
1. File > New Case
2. Case Name: INC-2026-0847
3. Base Directory: /evidencia/casos/
4. Insertar metadatos del caso

5. Add Data Source
   - Tipo: Disk Image or VM File
   - Archivo: imagen.dd
   - Paso a paso: aceptar defaults

6. Autopsy procesará automáticamente:
   - File Type Identification
   - Deleted Files
   - Keyword Search
   - File Analysis
   - Email Parser
   - Recent Activity
```

### Módulos de Autopsy más útiles

| Módulo | Qué hace | Prioridad |
|---|---|---|
| **Recent Activity** | Extrae ejecuciones recientes, navegación, USB | ⭐⭐⭐⭐⭐ |
| **Deleted Files** | Recupera archivos eliminados | ⭐⭐⭐⭐⭐ |
| **Keyword Search** | Búsqueda de texto libre en el disco | ⭐⭐⭐⭐ |
| **File Type ID** | Identifica tipos de archivo reales | ⭐⭐⭐⭐ |
| **Timeline** | Crea timeline de eventos | ⭐⭐⭐⭐ |
| **Email Parser** | Extrae correos (.pst, .mbox) | ⭐⭐⭐ |
| **Registry Analyzer** | Analiza Registry hives | ⭐⭐⭐⭐ |

---

## 8. Artefactos de Windows

### Artefactos de ejecución

| Artefacto | Ubicación | Qué revela | Herramienta |
|---|---|---|---|
| **Prefetch** | `C:\Windows\Prefetch` | Programas ejecutados, frecuencia, timestamps | PECmd |
| **Amcache.hve** | `C:\Windows\appcompat\Programs\` | Historial de ejecución completo | AmcacheParser |
| **ShimCache** | Registry `CurrentVersion\AppCompat` | Programas ejecutados | — |
| **BAM/DAM** | Registry `UserConservation` | Actividad de aplicaciones por usuario | — |

### Artefactos de usuario

| Artefacto | Ubicación | Qué revela | Herramienta |
|---|---|---|---|
| **NTUSER.DAT** | `C:\Users\<usuario>\` | Run keys, MRU, USB history | RegRipper |
| **LNK files** | `C:\Users\<usuario>\AppData\Roaming\Microsoft\Windows\Recent\` | Archivos abiertos, rutas | LECmd |
| **Jump Lists** | `C:\Users\<usuario>\AppData\Roaming\Microsoft\Windows\Recent\AutomaticDestinations\` | Actividad de tareas recientes | JLECmd |
| **Shellbags** | `C:\Users\<usuario>\AppData\Local\Microsoft\Windows\Shell\` | Carpetas visitadas | ShellBagsExplorer |
| **Browser history** | `C:\Users\<usuario>\AppData\Local\<browser>\` | Navegación web | DB Browser, Hindsight |

### Artefactos de red

| Artefacto | Ubicación | Qué revela | Herramienta |
|---|---|---|---|
| **hosts file** | `C:\Windows\System32\drivers\etc\hosts` | Redirecciones DNS maliciosas | Text editor |
| **DNS cache** | `C:\Windows\System32\drivers\etc\` | DNS consultados recientemente | ipconfig /displaydns |
| **WiFi profiles** | `C:\ProgramData\Microsoft\Wlansvc\Profiles\` | Redes WiFi conocidas | — |
| **Network icon cache** | `C:\Users\<usuario>\AppData\Local\Microsoft\Windows\Explorer\` | Iconos de red | — |

### Artefactos de USB

```bash
# Registry keys que registran USB devices
# NTUSER.DAT\Software\Microsoft\Windows\CurrentVersion\Explorer\MountPoints2
# SYSTEM\CurrentControlSet\Enum\USBSTOR
# SYSTEM\CurrentControlSet\Enum\USB

# Parsear con RegRipper
rip.pl -r NTUSER.DAT -p usb
rip.pl -r SYSTEM -p usbstor
```

---

## 9. Defensa y detección

### Para Blue Team / Administradores

| Técnica atacante | Detección | Mitigación |
|---|---|---|
| **Borrado de archivos** | Logs de auditoría, $UsnJrnl | Logs centralizados, SIEM |
| **Timestomping** | Comparar timestamps múltiples | Monitoreo de integridad |
| **Borrado de Prefetch** | Logs de borrado, Amcache | File Integrity Monitoring |
| **Cifrado de disco** | Detección de patrones de cifrado | Forzar shutdown para RAM |
| **Anti-forensics** | Análisis de entropía | Monitoreo de actividad |
| **Escritura a discos** | Write-blockers, monitoreo | Control de acceso físico |

### Monitoreo de integridad

```bash
# Instalar AIDE (Linux)
sudo apt-get install aide

# Inicializar base de datos
sudo aideinit

# Verificar cambios
sudo aide --check
```

---

## 10. Referencias

| Recurso | URL |
|---|---|
| **The Sleuth Kit** | [https://www.sleuthkit.org/](https://www.sleuthkit.org/) |
| **Autopsy** | [https://www.sleuthkit.org/autopsy/](https://www.sleuthkit.org/autopsy/) |
| **SANS FOR508** | [https://www.sans.org/cyber-security-courses/advanced-incident-response/](https://www.sans.org/cyber-security-courses/advanced-incident-response/) |
| **Eric Zimmerman Tools** | [https://ericzimmerman.github.io/](https://ericzimmerman.github.io/) |
| **NIST SP 800-86** | [https://csrc.nist.gov/pubs/sp/800/86/final](https://csrc.nist.gov/pubs/sp/800/86/final) |

---

## 📝 Entregable de portafolio

```markdown
# Análisis de Disco — Caso INC-2026-0847

## Contexto
- Imagen: imagen.dd (1TB, formato RAW)
- Partición: NTFS, offset 2048
- Herramientas: The Sleuth Kit, Autopsy, MFTECmd

## Hallazgos
1. **Archivos borrados recuperados:** 47 archivos (docs, PDFs, imágenes)
2. **Artefactos de ejecución:**
   - Prefetch: PowerShell.exe ejecutado 23 veces en las últimas 48h
   - Amcache: processhacker.exe ejecutado (herramienta de evasión)
3. **USB conectados:** 3 dispositivos diferentes (posible exfiltración)
4. **Browser history:** descargas de herramientas de hacking

## Conclusiones
- El atacante ejecutó PowerShell con comandos ofuscados
- Usó processhacker para evadir detección
- Conectó USB para exfiltrar datos antes del borrado

## Evidencia
- Imagen: /evidencia/caso001/imagen.dd (SHA-256: 8f7e6d5c...a1b2)
- Archivos recuperados: /evidencia/caso001/recuperados/
- Reporte Autopsy: /evidencia/caso001/autopsy_report.pdf
```

---

**[⬅ Volver al módulo](../README.md)** · **[→ Herramientas de Disco](./02-herramientas-disco.md)**
