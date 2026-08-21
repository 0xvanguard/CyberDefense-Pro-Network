# 🛠️ Herramientas Forenses — Guía Completa

> *"Elegir la herramienta correcta es tan importante como saber usarla. Cada herramienta tiene su lugar en el flujo de trabajo forense."*

---

## 📋 Tabla de contenido

1. [Visión general del ecosistema](#1-visión-general-del-ecosistema)
2. [Herramientas de adquisición](#2-herramientas-de-adquisición)
3. [Herramientas de análisis de disco](#3-herramientas-de-análisis-de-disco)
4. [Herramientas de análisis de memoria](#4-herramientas-de-análisis-de-memoria)
5. [Herramientas de timeline](#5-herramientas-de-timeline)
6. [Herramientas de análisis de red](#6-herramientas-de-análisis-de-red)
7. [Herramientas de metadatos](#7-herramientas-de-metadatos)
8. [Distros forenses](#8-distros-forenses)
9. [Comparativa final](#9-comparativa-final)
10. [Flujos de trabajo recomendados](#10-flujos-de-trabajo-recomendados)
11. [Referencias](#11-referencias)

---

## 1. Visión general del ecosistema

### Herramientas por fase del análisis

```
┌─────────────────────────────────────────────────────────────────┐
│                    FLUJO DE TRABAJO FORENSE                      │
├─────────────────────────────────────────────────────────────────┤
│                                                                  │
│  1. ADQUISICIÓN          2. ANÁLISIS           3. REPORTE       │
│  ┌──────────────┐       ┌──────────────┐      ┌──────────────┐ │
│  │ dc3dd        │       │ Volatility 3 │      │ Autopsy      │ │
│  │ FTK Imager   │──────▶│ The Sleuth K.│─────▶│ Timeline     │ │
│  │ avml         │       │ plaso        │      │ Explorer     │ │
│  │ winpmem      │       │ Wireshark    │      │ Reportes     │ │
│  └──────────────┘       └──────────────┘      └──────────────┘ │
│                                                                  │
└─────────────────────────────────────────────────────────────────┘
```

---

## 2. Herramientas de adquisición

### Comparativa

| Herramienta | Plataforma | Tipo | Hash integrado | Precio |
|---|---|---|---|---|
| **dc3dd** | Linux | CLI | ✅ SHA-256, MD5 | Gratis |
| **dd** | Linux/macOS | CLI | ❌ | Gratis |
| **FTK Imager** | Windows | GUI | ✅ MD5, SHA1 | Gratis |
| **Guymager** | Linux | GUI | ✅ | Gratis |
| **avml** | Linux | CLI | ❌ | Gratis |
| **winpmem** | Windows | CLI | ❌ | Gratis |
| **DumpIt** | Windows | CLI | ❌ | Gratis |

### Recomendaciones

| Necesidad | Herramienta |
|---|---|
| **Adquisición de disco en Linux** | dc3dd |
| **Adquisición de disco en Windows** | FTK Imager |
| **Adquisición de RAM en Linux** | avml |
| **Adquisición de RAM en Windows** | winpmem o DumpIt |
| **Adquisición con GUI en Linux** | Guymager |

---

## 3. Herramientas de análisis de disco

### Comparativa

| Herramienta | Tipo | Plataforma | Uso principal |
|---|---|---|---|
| **The Sleuth Kit** | CLI | Multi | Análisis programático |
| **Autopsy** | GUI | Multi | Análisis visual completo |
| **FTK (AccessData)** | GUI | Windows | Análisis profesional |
| **X-Ways Forensics** | GUI/CLI | Windows | Análisis avanzado |
| **Magnet AXIOM** | GUI | Windows | Análisis cloud+local |
| **Belkasoft** | GUI | Windows | Análisis profesional |

### The Sleuth Kit (TSK)

```bash
# Comandos esenciales
mmls imagen.dd          # Ver particiones
fls -r -o 2048 imagen.dd    # Listar archivos
icat -o 2048 imagen.dd <inode>  # Extraer archivo
tsk_recover -o 2048 imagen.dd /salida/  # Recuperar borrados
```

### Autopsy

```
Ventajas:
- GUI intuitiva
- Módulos automáticos (Recent Activity, Deleted Files)
- Soporte para múltiples formatos
- Exportación de reportes

Desventajas:
- Requiere más recursos que TSK CLI
- Menos flexible para análisis personalizado
```

---

## 4. Herramientas de análisis de memoria

### Comparativa

| Herramienta | Plataforma | Velocidad | Comunidad |
|---|---|---|---|
| **Volatility 3** | Multi | Media | ⭐⭐⭐⭐⭐ |
| **Volatility 2** | Multi | Media | ⭐⭐⭐⭐ |
| **Rekall** | Multi | Rápida | ⭐⭐ |
| **Volatility Workbench** | Windows | Media | ⭐⭐⭐ |

### Volatility 3

```bash
# Plugins más usados
vol -f mem.raw windows.info
vol -f mem.raw windows.pslist
vol -f mem.raw windows.pstree
vol -f mem.raw windows.cmdline
vol -f mem.raw windows.netscan
vol -f mem.raw windows.malfind
vol -f mem.raw windows.hashdump
```

---

## 5. Herramientas de timeline

### Comparativa

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

### Flujo de trabajo

```bash
# 1. Crear timeline con plaso
log2timeline.py --storage-file timeline.plaso imagen.dd

# 2. Exportar a CSV
psort.py -o l2tcsv -w timeline.csv timeline.plaso

# 3. Visualizar en Timeline Explorer
# File > Open > timeline.csv
```

---

## 6. Herramientas de análisis de red

### Comparativa

| Herramienta | Uso | Plataforma |
|---|---|---|
| **Wireshark** | Análisis GUI de paquetes | Multi |
| **tshark** | Análisis CLI de paquetes | Multi |
| **tcpdump** | Captura de paquetes | Linux |
| **Zeek (Bro)** | Análisis de red | Linux |
| **Suricata** | IDS/IPS | Linux |
| **NetworkMiner** | Análisis forense de red | Windows |
| **NGrep** | Búsqueda en tráfico | Linux |

### Wireshark

```
Filtros esenciales:
- ip.addr == 10.10.10.100
- tcp.port == 443
- http.request
- dns
- tls.handshake.type == 1

Funciones clave:
- Follow TCP Stream
- Export Objects > HTTP
- Statistics > Conversations
- Statistics > Protocol Hierarchy
```

### Zeek

```bash
# Ejecutar Zeek
zeek -i eth0

# Logs generados:
# conn.log → Conexiones de red
# dns.log → Queries DNS
# http.log → Peticiones HTTP
# ssl.log → Conexiones TLS
# files.log → Archivos transferidos
```

---

## 7. Herramientas de metadatos

### Comparativa

| Herramienta | Uso | Plataforma |
|---|---|---|
| **exiftool** | Metadatos EXIF | Multi |
| **ExifToolGUI** | GUI para exiftool | Windows |
| **steghide** | Esteganografía | Linux |
| **stegsolve** | Análisis de capas | Multi (Java) |
| **binwalk** | Firma de archivos | Linux |
| **TrID** | Identificación de archivos | Multi |
| **Mat2** | Limpieza de metadatos | Linux |

### exiftool

```bash
# Extraer todos los metadatos
exiftool imagen.jpg

# Extraer solo GPS
exiftool -gps:all -n imagen.jpg

# Extraer de todos los archivos en directorio
exiftool -r /evidencia/

# Exportar a JSON
exiftool -r -json /evidencia/ > metadatos.json

# Eliminar metadatos
exiftool -all= imagen.jpg
```

---

## 8. Distros forenses

### Comparativa

| Distros | Uso principal | Basada en |
|---|---|---|
| **CAINE** | Live forensics | Ubuntu |
| **Kali Linux** | Pentesting + forensics | Debian |
| **Paladin** | Adquisición de evidencia | Ubuntu |
| **SIFT Workstation** | Análisis forense | Ubuntu |
| **DEFT** | Live forensics | Ubuntu |
| **CSI Linux** | Investigación OSINT | Ubuntu |

### CAINE (Computer Aided Investigative Environment)

```
Ventajas:
- Distro live (no instala nada en el disco)
- Herramientas forenses preinstaladas
- Write-blocker integrado
- Interfaz intuitiva

Herramientas incluidas:
- Autopsy, The Sleuth Kit
- Volatility
- Wireshark
- exiftool
- FTK Imager
```

### SIFT Workstation

```
Ventajas:
- Creada por SANS (líder en formación forense)
- Herramientas actualizadas regularmente
- Scripts de automatización incluidos
- Ideal para análisis en laboratorio

Herramientas incluidas:
- Volatility, Plaso
- log2timeline
- YARA
- Thor (IOC scanner)
```

---

## 9. Comparativa final

### Herramientas por categoría

| Categoría | Herramienta #1 | Herramienta #2 | Herramienta #3 |
|---|---|---|---|
| **Adquisición disco** | dc3dd | FTK Imager | Guymager |
| **Adquisición RAM** | avml | winpmem | DumpIt |
| **Análisis disco** | Autopsy | The Sleuth Kit | X-Ways |
| **Análisis memoria** | Volatility 3 | Volatility 2 | Rekall |
| **Timeline** | plaso | MFTECmd | Timeline Explorer |
| **Análisis red** | Wireshark | Zeek | tshark |
| **Metadatos** | exiftool | binwalk | TrID |
| **Recuperación** | PhotoRec | Recuva | foremost |

### ¿Cuándo usar qué?

| Escenario | Herramientas recomendadas |
|---|---|
| **Triage rápido** | FTK Imager + Volatility 3 |
| **Análisis completo** | Autopsy + Volatility 3 + plaso |
| **Análisis de red** | Wireshark + Zeek |
| **Investigación de malware** | Volatility 3 + YARA + binwalk |
| **Recuperación de archivos** | PhotoRec + The Sleuth Kit |
| **Presentación en tribunal** | Autopsy + Timeline Explorer |

---

## 10. Flujos de trabajo recomendados

### Flujo 1: Investigación rápida (1-2 horas)

```
1. ADQUISICIÓN (15 min)
   └─ FTK Imager: crear imagen de disco
   └─ winpmem: capturar RAM

2. ANÁLISIS RÁPIDO (30 min)
   └─ Autopsy: Recent Activity module
   └─ Volatility: pslist, netscan, cmdline

3. HALLAZGOS (30 min)
   └─ Documentar hallazgos clave
   └─ Exportar evidencia
```

### Flujo 2: Investigación completa (8-16 horas)

```
1. PREPARACIÓN (1 hora)
   └─ Autorización legal
   └─ Herramientas listas

2. ADQUISICIÓN (1-2 horas)
   └─ RAM primero (avml)
   └─ Disco con dc3dd
   └─ Verificar hashes

3. ANÁLISIS DE DISCO (3-4 horas)
   └─ Autopsy: crear caso
   └─ Eric Zimmerman tools
   └─ Recuperación de archivos

4. ANÁLISIS DE MEMORIA (2-3 horas)
   └─ Volatility 3 completo
   └─ IOC extraction

5. ANÁLISIS DE RED (1-2 horas)
   └─ Wireshark/tshark
   └─ Logs de firewall/DNS

6. TIMELINE (1-2 horas)
   └─ plaso: super timeline
   └─ Timeline Explorer

7. REPORTE (2 horas)
   └─ Documentar hallazgos
   └─ Crear reporte profesional
```

### Flujo 3: Investigación de malware (4-8 horas)

```
1. ANÁLISIS ESTÁTICO (1-2 horas)
   └─ file: identificar tipo
   └─ strings: buscar URLs, IPs
   └─ YARA: matching de patrones
   └─ binwalk: archivos embebidos

2. ANÁLISIS DINÁMICO (2-3 horas)
   └─ Sandbox (Cuckoo, Any.Run)
   └─ Monitoreo de red
   └─ Monitoreo de procesos

3. ANÁLISIS DE MEMORIA (1-2 horas)
   └─ Volatility: malfind, netscan
   └─ Extraer IOC

4. REPORTE (1 hora)
   └─ Documentar hallazgos
   └─ Crear reglas YARA
```

---

## 11. Referencias

| Recurso | URL |
|---|---|
| **The Sleuth Kit** | [https://www.sleuthkit.org/](https://www.sleuthkit.org/) |
| **Autopsy** | [https://www.sleuthkit.org/autopsy/](https://www.sleuthkit.org/autopsy/) |
| **Volatility 3** | [https://github.com/volatilityfoundation/volatility3](https://github.com/volatilityfoundation/volatility3) |
| **plaso** | [https://plaso.readthedocs.io/](https://plaso.readthedocs.io/) |
| **Wireshark** | [https://www.wireshark.org/](https://www.wireshark.org/) |
| **Zeek** | [https://zeek.org/](https://zeek.org/) |
| **CAINE** | [https://www.caine-live.net/](https://www.caine-live.net/) |
| **SIFT** | [https://www.sans.org/tools/sift-workstation/](https://www.sans.org/tools/sift-workstation/) |
| **Eric Zimmerman Tools** | [https://ericzimmerman.github.io/](https://ericzimmerman.github.io/) |
| **SANS FOR508** | [https://www.sans.org/cyber-security-courses/advanced-incident-response/](https://www.sans.org/cyber-security-courses/advanced-incident-response/) |

---

## 📝 Checklist de herramientas para laboratorio

```markdown
## Equipo mínimo para análisis forense

### Hardware
- [ ] Estación de trabajo con 16GB+ RAM
- [ ] Disco SSD de 1TB para evidencia
- [ ] USB booteable con CAINE/SIFT
- [ ] Write-blocker (hardware o software)

### Software
- [ ] Volatility 3 instalado
- [ ] The Sleuth Kit instalado
- [ ] Autopsy instalado
- [ ] Wireshark instalado
- [ ] Eric Zimmerman Tools
- [ ] plaso instalado
- [ ] exiftool instalado
- [ ] FTK Imager (Windows)

### Formación
- [ ] SANS FOR508 completado
- [ ] CyberDefenders: 3+ casos resueltos
- [ ] Volatility: 2+ volcados analizados
- [ ] Autopsy: 5+ casos creados
```

---

**[⬅ Timeline y Reporte](../timeline-reporte/01-construccion-timeline.md)** · **[Volver al módulo](../README.md)**
