# 🔍 Metadatos Forenses

> *"Cada archivo digital es más que su contenido: tiene una historia oculta en sus metadatos que puede revelar quién lo creó, cuándo, dónde y cómo."*

---

## 📋 Tabla de contenido

1. [¿Qué son los metadatos?](#1-qué-son-los-metadatos)
2. [Metadatos EXIF (imágenes)](#2-metadatos-exif-imágenes)
3. [Metadatos de documentos](#3-metadatos-de-documentos)
4. [Metadatos de sistema operativo](#4-metadatos-de-sistema-operativo)
5. [Steganography](#5-steganography)
6. [Fingerprinting de archivos](#6-fingerprinting-de-archivos)
7. [Herramientas](#7-herramientas)
8. [Defensa y detección](#8-defensa-y-detección)
9. [Referencias](#9-referencias)

---

## 1. ¿Qué son los metadatos?

### Definición

Los **metadatos** son datos sobre datos. Son información adicional que describe las características de un archivo sin ser el contenido en sí.

### Tipos de metadatos

| Tipo | Descripción | Ejemplo |
|---|---|---|
| **Descriptivos** | Título, autor, descripción | Autor de un PDF |
| **Estructurales** | Cómo está organizado el archivo | Capítulos de un libro |
| **Administrativos** | Permisos, fechas, tamaño | Fecha de modificación |
| **Técnicos** | Formato, resolución, códec | Resolución de una foto |
| **Ocultos** | Datos embebidos no visibles | GPS coordinates en EXIF |

### ¿Por qué importan en forense?

- **Identificar autor:** quién creó un documento
- **Establecer timeline:** cuándo se creó/modificó
- **Ubicar evidencia:** dónde se tomó una foto
- **Detectar manipulación:** si un archivo fue alterado
- **Recuperar información:** datos que el usuario no sabía que estaban ahí

---

## 2. Metadatos EXIF (imágenes)

### ¿Qué es EXIF?

**EXIF (Exchangeable Image File Format)** es un estándar que almacena metadatos en imágenes JPEG y TIFF.

### Metadatos EXIF típicos

| Campo | Descripción | Ejemplo |
|---|---|---|
| **Camera Make** | Marca de la cámara | Canon, Nikon, Apple |
| **Camera Model** | Modelo de la cámara | iPhone 15 Pro, Canon EOS R5 |
| **Date/Original** | Fecha de captura | 2026-08-20 14:30:00 |
| **GPS Latitude** | Latitud GPS | -34.603684 |
| **GPS Longitude** | Longitud GPS | -58.381559 |
| **GPS Altitude** | Altitud | 25m |
| **Exposure** | Configuración de exposición | f/2.8, 1/125s, ISO 400 |
| **Focal Length** | Distancia focal | 50mm |
| **Software** | Software de edición | Adobe Photoshop 25.0 |
| **Image Width/Height** | Dimensiones | 4032x3024 |
| **Orientation** | Orientación | Horizontal |

### Extraer metadatos EXIF

```bash
# Con exiftool (RECOMENDADO)
exiftool imagen.jpg

# Output ejemplo:
# Camera Make           : Apple
# Camera Model          : iPhone 15 Pro
# Date/Original         : 2026:08:20 14:30:00
# GPS Latitude          : 37 deg 46' 29.04" N
# GPS Longitude         : 122 deg 25' 9.84" W
# Software              : Adobe Photoshop 25.0
# Image Width           : 4032
# Image Height          : 3024

# Extraer solo GPS
exiftool -gps:all imagen.jpg

# Extraer solo fechas
exiftool -date:all imagen.jpg

# Buscar todas las imágenes en un directorio
exiftool -r /evidencia/imagenes/

# Guardar output en archivo
exiftool -r -json /evidencia/imagenes/ > exif_report.json
```

### Análisis forense de EXIF

```bash
# 1. Buscar coordenadas GPS
exiftool -gps:all -n imagen.jpg
# -n: formato numérico (no grados/minutos/segundos)

# 2. Verificar si fue editado
exiftool -Software imagen.jpg
# Si dice "Photoshop" o "GIMP" → fue editado

# 3. Comparar fechas
exiftool -DateTimeOriginal -CreateDate -ModifyDate imagen.jpg
# Si CreateDate != DateTimeOriginal → manipulación

# 4. Buscar imágenes con GPS en un caso
exiftool -r -gps:all -n /evidencia/ | grep -v "^$"

# 5. Convertir coordenadas a Google Maps
# Lat: 37.774733, Lon: -122.418389
# URL: https://www.google.com/maps?q=37.774733,-122.418389
```

---

## 3. Metadatos de documentos

### PDF

```bash
# Extraer metadatos de PDF
exiftool documento.pdf

# Output:
# File Size           : 1.2 MB
# PDF Version         : 1.7
# Creator             : Adobe InDesign 25.0
# Producer            : Adobe PDF Library 15.0
# Create Date         : 2026:08:20 10:00:00
# Modify Date         : 2026:08:20 12:00:00
# Author              : John Garcia
# Title               : Incident Report INC-0847
# Subject             : Security Analysis
# Creator Tool        : Adobe InDesign 25.0
# Pages               : 15

# Buscar PDFs modificados
exiftool -r -CreateDate -ModifyDate /evidencia/*.pdf
# Si ModifyDate > CreateDate → fue modificado después de crearlo
```

### Microsoft Office (docx, xlsx, pptx)

```bash
# Los archivos Office son ZIP files con XML interno
# Metadatos en docProps/core.xml y docProps/app.xml

# Extraer metadatos
exiftool documento.docx

# Output:
# Title               : Report
# Author              : John Garcia
# Last Modified By    : John Garcia
# Create Date         : 2026:08:20 10:00:00
# Modify Date         : 2026:08:20 14:30:00
# Revision Number     : 5
# Total Edit Time     : 4.5 hours
# Application         : Microsoft Office Word

# Analizar XML interno
unzip -o documento.docx -d extracted/
cat extracted/docProps/core.xml
cat extracted/docProps/app.xml
```

### Imágenes PNG

```bash
# PNG tiene chunks de metadatos
exiftool imagen.png

# Chunks importantes:
# tEXt: información de texto
# iTXt: texto internacional
# zTXt: texto comprimido

# Buscar metadatos ocultos en PNG
exiftool -v imagen.png
```

---

## 4. Metadatos de sistema operativo

### Timestamps NTFS (MAC times)

| Timestamp | Significado | Actualización |
|---|---|---|
| **MFT Entry** | Cuándo se creó la entrada $MFT | Al crear archivo |
| **$STANDARD_INFO** | Modificado por el sistema | Al crear/modificar |
| **$FILE_NAME** | Modificado por el explorer | Al crear/modificar |
| **Created** | Cuándo se creó el archivo | Al crear |
| **Modified** | Cuándo se modificó contenido | Al guardar cambios |
| **Accessed** | Cuándo se abrió por última vez | Al abrir |

### Timestomping: detección

```bash
# El atacante puede modificar timestamps para evadir detección
# Detección: comparar timestamps de diferentes fuentes

# Con Autopsy
# 1. Ver timestamps del $MFT
# 2. Ver timestamps del $UsnJrnl
# 3. Si difieren → timestomping

# Con MFTECmd
MFTECmd.exe -f imagen.dd --csv Output/
# Comparar timestamps de $STANDARD_INFO vs $FILE_NAME

# Con RegRipper
rip.pl -r NTUSER.DAT -p userassist
# UserAssist tiene timestamps cifrados pero verificables
```

### Windows Registry timestamps

```bash
# Registry keys tienen timestamps propios
# HKLM\SOFTWARE\Microsoft\Windows\CurrentVersion\Run
# (Run keys → persistencia)

# Extraer con RegRipper
rip.pl -r SYSTEM -p selfdel
rip.pl -r NTUSER.DAT -p userassist
```

---

## 5. Steganography

### ¿Qué es?

La **esteganografía** es ocultar datos dentro de otros archivos (imágenes, audio, video) sin alterar aparentemente el archivo contenedor.

### Técnicas comunes

| Técnica | Descripción | Dificultad de detección |
|---|---|---|
| **LSB (Least Significant Bit)** | Modificar bits menos significativos | Media |
| **Embedding en headers** | Datos en metadatos no usados | Baja |
| **Append data** | Datos al final del archivo | Baja |
| **DCT coefficients** | Modificar coeficientes de imagen | Alta |
| **Spread spectrum** | Distribuir datos en frecuencias | Muy alta |

### Detección de esteganografía

```bash
# Con steghide (JPEG)
steghide info imagen.jpg
steghide extract -sf imagen.jpg

# Con stegdetect
stegdetect imagen.jpg

# Con binwalk
binwalk imagen.jpg
binwalk -e imagen.jpg

# Con exiftool (buscar anomalías en metadatos)
exiftool -v imagen.jpg

# Análisis de entropía
# Los datos esteganográficos tienen alta entropía
ent imagen.jpg
```

### Herramientas de esteganografía

| Herramienta | Tipo | Uso |
|---|---|---|
| **steghide** | JPEG/BMP | Insertar/extraer datos |
| **stegsolve** | Imágenes | Análisis visual por capas |
| **zsteg** | PNG/BMP | Detección de LSB |
| **OpenStego** | Multi | Esteganografía general |
| **DeepSound** | Audio | Ocultar en audio |

---

## 6. Fingerprinting de archivos

### ¿Qué es?

El **fingerprinting** identifica el tipo real de un archivo, sin importar su extensión.

### Magic numbers

```bash
# Cada tipo de archivo tiene una firma (magic number)
# al inicio del archivo

# JPEG: FF D8 FF
# PNG: 89 50 4E 47
# PDF: 25 50 44 46 (%PDF)
# ZIP: 50 4B 03 04 (PK..)
# EXE: 4D 5A (MZ)
# ELF: 7F 45 4C 46

# Verificar con file
file malware.exe
# Output: PE32+ executable (GUI) x86-64

# Verificar magic number
xxd -l 16 malware.exe
# Output: 00000000: 4d5a 9000 0300 0000 0400 0000 ffff 0000
# MZ = Windows PE executable

# Buscar magic numbers en directorio
find /evidencia/ -exec file {} \; | grep -v "ASCII\|UTF-8"
```

### Firma de archivos

```bash
# Calcular hash de un archivo
sha256sum malware.exe
# Output: 8f7e6d5c...a1b2

# Buscar en VirusTotal
# https://www.virustotal.com/
# Subir archivo o buscar por hash

# Buscar en MalwareBazaar
# https://bazaar.abuse.ch/
# Buscar por hash
```

---

## 7. Herramientas

### Comparativa

| Herramienta | Uso | Plataforma | Precio |
|---|---|---|---|
| **exiftool** | Metadatos EXIF | Multi | Gratis |
| **ExifToolGUI** | GUI para exiftool | Windows | Gratis |
| **steghide** | Esteganografía | Linux | Gratis |
| **stegsolve** | Análisis de capas | Multi (Java) | Gratis |
| **binwalk** | Firma de archivos | Linux | Gratis |
| **TrID** | Identificación de archivos | Multi | Gratis |
| **MediaInfo** | Metadatos multimedia | Multi | Gratis |
| **Mat2** | Limpieza de metadatos | Linux | Gratis |

### Instalación

```bash
# exiftool
sudo apt-get install exiftool

# steghide
sudo apt-get install steghide

# stegsolve
wget http://www.caesum.com/handbook/StegSolve.jar
java -jar StegSolve.jar

# binwalk
sudo apt-get install binwalk

# TrID
wget https://mark0.net/download/trid_linux_64.zip
unzip trid_linux_64.zip
```

---

## 8. Defensa y detección

### Para Blue Team

| Técnica atacante | Detección | Mitigación |
|---|---|---|
| **Timestomping** | Comparar timestamps múltiples | File Integrity Monitoring |
| **Steganography** | Análisis de entropía, stegdetect | Monitoreo de tráfico |
| **Metadatos ocultos** | exiftool, análisis forense | Limpieza de metadatos antes de compartir |
| **Falsificar extensiones** | file, TrID | Políticas de ejecución |
| **Borrado seguro** | Análisis de disco, journal | Logs centralizados |

### Limpieza de metadatos

```bash
# Eliminar metadatos de imagen
exiftool -all= imagen.jpg

# Eliminar metadatos de PDF
exiftool -all= documento.pdf

# Eliminar metadatos de Office
mat2 documento.docx

# Verificar limpieza
exiftool imagen.jpg
# Solo debe mostrar: File Size, File Permissions, etc.
```

---

## 9. Referencias

| Recurso | URL |
|---|---|
| **ExifTool** | [https://exiftool.org/](https://exiftool.org/) |
| **steghide** | [https://steghide.sourceforge.net/](https://steghide.sourceforge.net/) |
| **binwalk** | [https://github.com/ReFirmLabs/binwalk](https://github.com/ReFirmLabs/binwalk) |
| **TrID** | [https://mark0.net/software-trid-online/](https://mark0.net/software-trid-online/) |
| **SANS FOR585** | [https://www.sans.org/cyber-security-courses/advanced-incident-response-threat-hunting/](https://www.sans.org/cyber-security-courses/advanced-incident-response-threat-hunting/) |

---

## 📝 Entregable de portafolio

```markdown
# Análisis de Metadatos — Caso INC-2026-0847

## Contexto
- Evidencia: 50 imágenes JPEG, 12 PDFs, 8 documentos Office
- Sospecha: exfiltración de datos via esteganografía

## Hallazgos
1. **Imágenes con GPS:**
   - 23 imágenes con coordenadas GPS
   - Ubicación: oficinas de la víctima
   - Fecha: 2026-08-18 (2 días antes del incidente)

2. **Documentos modificados:**
   - 3 PDFs con ModifyDate > CreateDate
   - Autor: "John Garcia" (empleado de TI)
   - Software: Adobe Acrobat Pro

3. **Esteganografía detectada:**
   - 1 imagen JPEG con datos ocultos (steghide)
   - Contenido: credenciales de VPN (452 bytes)

4. **Timestomping:**
   - 5 archivos con timestamps manipulados
   - $UsnJrnl muestra actividad real

## Conclusión
- Atacante usó steganografía para ocultar credenciales
- Timestomping para evadir detección
- GPS confirma ubicación física del atacante

## Evidencia
- Imágenes: /evidencia/caso001/imagenes/
- Reporte EXIF: /evidencia/caso001/exif_report.json
- Archivos estego: /evidencia/caso001/esteganografia/
```

---

**[⬅ Análisis de Red](../analisis-red/01-forense-red.md)** · **[Volver al módulo](../README.md)**
