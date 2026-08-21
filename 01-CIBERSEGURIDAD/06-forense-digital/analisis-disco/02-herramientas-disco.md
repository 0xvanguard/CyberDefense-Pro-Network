# 🛠️ Herramientas de Análisis de Disco Forense

> *"Las herramientas no hacen al forense, pero un forense sin herramientas está ciego."*

---

## 📋 Tabla de contenido

1. [Herramientas de línea de comandos](#1-herramientas-de-línea-de-comandos)
2. [The Sleuth Kit (TSK)](#2-the-sleuth-kit-tsk)
3. [Autopsy (GUI)](#3-autopsy-gui)
4. [FTK Imager](#4-ftk-imager)
5. [Herramientas de Eric Zimmerman](#5-herramientas-de-eric-zimmerman)
6. [Recuperación de archivos](#6-recuperación-de-archivos)
7. [Comparativa de herramientas](#7-comparativa-de-herramientas)
8. [Flujos de trabajo](#8-flujos-de-trabajo)
9. [Referencias](#9-referencias)

---

## 1. Herramientas de línea de comandos

### dd vs dc3dd

```bash
# dd: el clásico (no incluye hashing)
dd if=/dev/sda of=img.dd bs=4M status=progress

# dc3dd: dd con hashing integrado (RECOMENDADO)
dc3dd if=/dev/sda of=img.dd hash=sha256 log=hash.log
# Parámetros:
#   hash=sha256     → calcula SHA-256 durante la copia
#   log=hash.log    → guarda el hash en archivo
#   -bn2            → reporta bad blocks pero continúa
```

### grep forense

```bash
# Buscar strings en un disco completo
strings -n 8 imagen.dd | grep -i "password"
strings -n 8 imagen.dd | grep -i "secret"
strings -n 8 imagen.dd | grep -E "[0-9]{3}-[0-9]{2}-[0-9]{4}"  # SSN

# Buscar emails
strings -n 8 imagen.dd | grep -E "[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}"

# Buscar URLs
strings -n 8 imagen.dd | grep -E "https?://[a-zA-Z0-9./]+"

# Buscar IPs
strings -n 8 imagen.dd | grep -E "[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}"
```

### binwalk

```bash
# Detectar archivos embebidos en una imagen
binwalk imagen.dd

# Extraer archivos embebidos
binwalk -e imagen.dd

# Firma de archivos
binwalk -A imagen.dd
```

### foremost / scalpel

```bash
# foremost: recuperar archivos por tipo desde imagen
foremost -i imagen.dd -o /salida/

# scalpel: recuperación más detallada
scalpel imagen.dd -o /salida/
```

---

## 2. The Sleuth Kit (TSK)

### Instalación

```bash
# Linux
sudo apt-get install sleuthkit

# macOS
brew install sleuthkit

# Windows
# Descargar desde https://www.sleuthkit.org/sleuthkit/download.php
```

### Comandos esenciales

#### Información de la imagen

```bash
# Verificar tipo de imagen
img_stat imagen.dd

# Ver particiones
mmls imagen.dd

# Verificar sistema de archivos de una partición
fsstat -f ntfs -o 2048 imagen.dd
```

#### Navegación de archivos

```bash
# Listar archivos recursivamente
fls -r -o 2048 imagen.dd

# Listar solo archivos borrados
fls -d -r -o 2048 imagen.dd

# Ver metadata de un archivo
fstat -o 2048 imagen.dd 12345

# Buscar un archivo por nombre
ffind -o 2048 imagen.dd -n "documento.pdf"

# Extraer un archivo por inode
icat -o 2048 imagen.dd 12345 > archivo_extraido
```

#### Recuperación

```bash
# Recuperar archivos borrados
tsk_recover -o 2048 imagen.dd /salida/

# Recuperar archivos de tipo específico
tsk_recover -o 2048 -e imagen.dd /salida/  # Solo no-SYS files
```

#### Análisis de strings

```bash
# Buscar strings en un archivo específico
tsk_loimg -f ntfs -o 2048 imagen.dd <inode> | strings

# Buscar en disco completo
strings imagen.dd | grep -i "evidence"
```

### Ejemplo completo: análisis de imagen NTFS

```bash
# Paso 1: Verificar imagen
img_stat imagen.dd
# Type: Raw (dd)

# Paso 2: Ver particiones
mmls imagen.dd
# Slot 003: GPT:0  00004096  41943006  Microsoft basic data

# Paso 3: Listar archivos
fls -r -o 2048 imagen.dd
# Output:
#   r/r 12345:    Documents/confidential.docx
#   r/r *12346:   Documents/deleted_report.xlsx  (* = borrado)
#   d/d 12347:    Temp/
#   r/r 12348:    Temp/malware.exe

# Paso 4: Extraer archivo borrado
icat -o 2048 imagen.dd 12346 > deleted_report.xlsx

# Paso 5: Extraer ejecutable sospechoso
icat -o 2048 imagen.dd 12348 > malware.exe

# Paso 6: Verificar hash del extraído
sha256sum malware.exe
```

---

## 3. Autopsy (GUI)

### Instalación

```bash
# Linux (Debian/Ubuntu)
wget https://github.com/sleuthkit/autopsy/releases/latest/download/autopsy-*.deb
sudo dpkg -i autopsy-*.deb
sudo apt-get install -f  # Instalar dependencias

# Windows
# Descargar desde https://www.sleuthkit.org/autopsy/
# Instalador con wizard
```

### Crear caso paso a paso

```
1. File > New Case
   ├── Case Name: INC-2026-0847
   ├── Case Number: INC-0847
   ├── Examiner: J. García
   └── Base Directory: /evidencia/casos/

2. Add Data Source
   ├── Type: Disk Image or VM File
   ├── Image Path: /evidencia/imagen.dd
   ├── Time Zone: (usar zona horaria del sistema)
   └── Click "Add"

3. Esperar procesamiento automático
   ├── File Type Identification
   ├── Deleted Files Recovery
   ├── Keyword Search
   ├── Recent Activity
   └── Email Parser
```

### Módulos de análisis

| Módulo | Descripción | Prioridad |
|---|---|---|
| **Recent Activity** | Extrae ejecuciones recientes, navegación, USB | ⭐⭐⭐⭐⭐ |
| **Deleted Files** | Recupera archivos eliminados | ⭐⭐⭐⭐⭐ |
| **Keyword Search** | Búsqueda de texto libre | ⭐⭐⭐⭐ |
| **File Type ID** | Identifica tipos reales de archivo | ⭐⭐⭐⭐ |
| **Timeline** | Crea línea de tiempo | ⭐⭐⭐⭐ |
| **Registry Analyzer** | Analiza NTUSER.DAT, SYSTEM | ⭐⭐⭐⭐ |
| **Email Parser** | Extrae correos (.pst, .mbox) | ⭐⭐⭐ |
| **Extension Mismatch** | Detecta extensiones falsas | ⭐⭐⭐ |

### Navegación en Autopsy

```
Tree View (panel izquierdo):
├── Data Sources
│   └── imagen.dd
│       └── Partition 1 (NTFS)
│           ├── [Deleted Files]
│           ├── [File Types]
│           ├── Windows/
│           ├── Users/
│           └── ...
├── Views
│   ├── File Types by Extension
│   ├── File Types by MIME Type
│   ├── Deleted Files
│   ├── Keyword Hits
│   └── ...
└── Results
    ├── Recent Activity
    ├── Web Artifacts
    ├── Email Messages
    └── ...
```

---

## 4. FTK Imager

### Instalación (Windows)

```
1. Descargar desde https://www.exterro.com/ftk-imager
2. Instalar con wizard
3. Ejecutar como Administrator
```

### Crear imagen de disco

```
1. File > Create Disk Image
2. Select Source:
   └── Physical Drive → seleccionar disco
3. Select Image Type:
   └── Raw (dd) — más compatible
4. Select Destination:
   └── Ruta de almacenamiento
5. Start para iniciar adquisición
6. Verificar hash al finalizar
```

### Análisis con FTK Imager

```
1. File > Image Mounting
   └── Seleccionar imagen .E01 o .dd
   └── Mount Type: Physical & Logical

2. Navegar archivos en el panel izquierdo

3. File > Export Files
   └── Exportar archivos relevantes

4. Evidence -> Right Click > Export
   └── Exportar con hash
```

### Verificar integridad

```
1. Tools > Verify Drive/Image
2. Seleccionar imagen
3. Verificar hash contra conocido
4. Resultado: PASS o FAIL
```

---

## 5. Herramientas de Eric Zimmerman

### Suite completa (Windows)

| Herramienta | Uso | Comando |
|---|---|---|
| **MFTECmd** | Parsear $MFT | `MFTECmd.exe -f MFT --json Output/` |
| **LECmd** | Parsear LNK files | `LECmd.exe -d "C:\Users" --csv Output/` |
| **JLECmd** | Parsear Jump Lists | `JLECmd.exe -d "C:\Users" --csv Output/` |
| **PECmd** | Parsear Prefetch | `PECmd.exe -d "C:\Windows\Prefetch" --csv Output/` |
| **AmcacheParser** | Parsear Amcache.hve | `AmcacheParser.exe -f Amcache.hve --csv Output/` |
| **RegRipper** | Parsear Registry | `rip.pl -r NTUSER.DAT -p all` |
| **ShellBagsExplorer** | Parsear Shellbags | GUI — arrastrar carpeta |
| **WxTCmd** | Parsear Timeline | `WxTCmd.exe -f "C:\Users" --csv Output/` |
| **SDBParser** | Parsear ShimCache | `SDBParser.exe -f AppCompat --csv Output/` |
| **SumrPlorer** | Resumen de evidencia | GUI — agregar fuentes |

### Ejemplo: análisis completo con Zimmerman tools

```bash
# Crear directorio de salida
mkdir Output/

# Parsear $MFT
MFTECmd.exe -f imagen.dd --csv Output/ --csvf MFT.csv

# Parsear Prefetch
PECmd.exe -d "C:\Windows\Prefetch" --csv Output/ --csvf Prefetch.csv

# Parsear LNK files
LECmd.exe -d "C:\Users" --csv Output/ --csvf LNK.csv

# Parsear Amcache
AmcacheParser.exe -f "C:\Windows\appcompat\Programs\Amcache.hve" --csv Output/ --csvf Amcache.csv

# Parsear Jump Lists
JLECmd.exe -d "C:\Users" --csv Output/ --csvf JumpLists.csv

# Parsear Registry
RegRipper.exe -r "C:\Users\victim\NTUSER.DAT" -a > Output/Registry_victim.txt
```

---

## 6. Recuperación de archivos

### PhotoRec

```bash
# Recuperar archivos por tipo desde imagen
photorec /d /salida imagen.dd

# Seleccionar:
# 1. Partición a analizar
# 2. Sistema de archivos (o [Unknown])
# 3. Directorio de salida
# 4. Tipos de archivo (All, jpg, pdf, docx, etc.)
```

### Recuva (Windows, GUI)

```
1. Abrir Recuva
2. Seleccionar unidad o imagen montada
3. Tipo de archivo: All Files
4. Modo: Deep Scan
5. Escanear
6. Seleccionar archivos a recuperar
7. Recuperar a ubicación segura
```

### TestDisk

```bash
# Recuperar particiones borradas
testdisk imagen.dd

# Pasos:
# 1. Seleccionar tipo de tabla de particiones
# 2. Analizar estructura de particiones
# 3. Si partición encontrada: Write (escribir tabla)
# 4. Recuperar archivos
```

---

## 7. Comparativa de herramientas

| Herramienta | Tipo | Plataforma | Precio | Ideal para |
|---|---|---|---|---|
| **The Sleuth Kit** | CLI | Linux/macOS/Win | Gratis | Análisis programático |
| **Autopsy** | GUI | Linux/Windows | Gratis | Análisis visual completo |
| **FTK Imager** | GUI | Windows | Gratis | Adquisición y verificación |
| **Eric Zimmerman** | CLI/GUI | Windows | Gratis | Artefactos Windows |
| **PhotoRec** | CLI | Todo | Gratis | Recuperación de archivos |
| **Recuva** | GUI | Windows | Gratis | Recuperación simple |
| **Belkasoft** | GUI | Windows | Pago | Análisis profesional |
| **Magnet AXIOM** | GUI | Windows | Pago | Análisis cloud + local |
| **X-Ways Forensics** | GUI/CLI | Windows | Pago | Análisis avanzado |

### ¿Cuándo usar cada una?

| Necesidad | Herramienta recomendada |
|---|---|
| **Adquisición de disco** | dc3dd (Linux), FTK Imager (Windows) |
| **Análisis rápido de artefactos Windows** | Eric Zimmerman tools |
| **Análisis completo visual** | Autopsy |
| **Análisis programático (scripts)** | The Sleuth Kit CLI |
| **Recuperación de archivos borrados** | PhotoRec, Recuva |
| **Verificar integridad de imagen** | FTK Imager, sha256sum |

---

## 8. Flujos de trabajo

### Flujo 1: Análisis rápido (triage)

```bash
# 1. Montar imagen (solo lectura)
mount -o ro,loop imagen.dd /mnt/evidence

# 2. Buscar artefactos clave
find /mnt/evidence -name "*.lnk" -o -name "*.prefetch" -o -name "NTUSER.DAT"

# 3. Verificar USB conectados
cat /mnt/evidence/Windows/System32/config/SYSTEM | strings | grep -i "USBSTOR"

# 4. Verificar ejecuciones recientes
find /mnt/evidence -path "*/AppData/Local/Microsoft/Windows/Recent/*"

# 5. Documentar hallazgos
echo "Hallazgos: [listar archivos encontrados]" > hallazgos.txt
```

### Flujo 2: Análisis completo (laboratorio)

```
1. ADQUISICIÓN
   └─ Crear imagen con dc3dd + hash

2. VERIFICACIÓN
   └─ Verificar hash de imagen

3. ANÁLISIS INICIAL
   └─ Autopsy: crear caso, agregar imagen
   └─ Esperar procesamiento automático

4. ANÁLISIS PROFUNDO
   └─ Eric Zimmerman tools para artefactos Windows
   └─ RegRipper para Registry
   └─ PECmd para Prefetch

5. RECUPERACIÓN
   └─ PhotoRec para archivos borrados
   └─ tsk_recover para recuperación TSK

6. BÚSQUEDA
   └─ Keyword search en Autopsy
   └─ grep strings para datos sensibles

7. TIMELINE
   └─ Exportar timestamps de MFT, Prefetch, LNK
   └─ Crear timeline en spreadsheet

8. REPORTE
   └─ Exportar hallazgos de Autopsy
   └─ Documentar en formato forense
```

---

## 9. Referencias

| Recurso | URL |
|---|---|
| **The Sleuth Kit** | [https://www.sleuthkit.org/](https://www.sleuthkit.org/) |
| **Autopsy** | [https://www.sleuthkit.org/autopsy/](https://www.sleuthkit.org/autopsy/) |
| **Eric Zimmerman Tools** | [https://ericzimmerman.github.io/](https://ericzimmerman.github.io/) |
| **FTK Imager** | [https://www.exterro.com/ftk-imager](https://www.exterro.com/ftk-imager) |
| **PhotoRec** | [https://www.cgsecurity.org/wiki/PhotoRec](https://www.cgsecurity.org/wiki/PhotoReg) |
| **SANS FOR508** | [https://www.sans.org/cyber-security-courses/advanced-incident-response/](https://www.sans.org/cyber-security-courses/advanced-incident-response/) |

---

**[⬅ Análisis de Disco: Sistemas](./01-sistemas-archivos-img.md)** · **[Volver al módulo](../README.md)**
