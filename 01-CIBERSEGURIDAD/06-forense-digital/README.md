# 🔬 Forense Digital — Guía profesional (DFIR)

> **Nivel:** Intermedio → Avanzado · **Marco:** [NIST SP 800-86](https://csrc.nist.gov/pubs/sp/800/86/final) · [RFC 3227](https://www.rfc-editor.org/rfc/rfc3227)
>
> Objetivo: reconstruir **qué pasó** en un sistema tras un incidente, con **evidencia íntegra y admisible**. Forense no es "abrir archivos": es método, orden y cadena de custodia.

---

## Índice

1. [El proceso DFIR (4 fases)](#1-el-proceso-dfir-4-fases)
2. [Cadena de custodia e integridad](#2-cadena-de-custodia-e-integridad)
3. [Orden de volatilidad (qué capturar primero)](#3-orden-de-volatilidad-qué-capturar-primero)
4. [Forense de disco](#4-forense-de-disco)
5. [Forense de memoria (Volatility 3)](#5-forense-de-memoria-volatility-3)
6. [Timeline forense (plaso)](#6-timeline-forense-plaso)
7. [Triage rápido (KAPE)](#7-triage-rápido-kape)
8. [Reporte forense](#8-reporte-forense)
9. [Referencias](#9-referencias)

---

## 1. El proceso DFIR (4 fases)

Según NIST SP 800-86, todo análisis forense sigue:

```
1. Collection      → adquirir evidencia SIN alterarla
2. Examination     → extraer y filtrar datos relevantes
3. Analysis        → responder las preguntas del caso
4. Reporting       → documentar hallazgos y método
```

> **Principio rector:** nunca trabajes sobre la evidencia original. Trabaja siempre sobre una **copia** (imagen).

---

## 2. Cadena de custodia e integridad

La evidencia solo vale si se puede demostrar que **no fue alterada**. Dos mecanismos:

### 2.1 Hashing (integridad)

```bash
# Calcular hash ANTES y DESPUÉS de cualquier análisis
sha256sum evidencia.dd
# Debe dar IDÉNTICO resultado al final → integridad probada
```

### 2.2 Cadena de custodia (quién/tuvo/qué/cuándo)

Cada movimiento de la evidencia se registra:

```text
Fecha/Hora | Quién | Acción | Hash (sha256) | Ubicación
-----------|-------|--------|---------------|----------
2026-08-20 10:00 | J.C. | Adquisición | 4b3a... | Sala segura A
2026-08-20 11:30 | J.C. | Traslado a lab | 4b3a... | Lab forense
```

> **Regla:** si el hash cambia, la cadena de custodia se rompe y la evidencia pierde valor legal.

---

## 3. Orden de volatilidad (qué capturar primero)

Lo más volátil se captura **primero** (RFC 3227):

| Orden | Evidencia | Ejemplo de herramienta |
|---|---|---|
| 1 | Registros CPU, caché | (poco práctico) |
| 2 | **Memoria RAM** | winpmem, DumpIt, avml |
| 3 | Estado de red (conexiones, ARP) | netstat, Volatility netscan |
| 4 | Procesos en ejecución | Volatility pslist |
| 5 | Disco (imagen) | dc3dd, dd |
| 6 | Logs remotos / backups | SIEM, syslog |

> La memoria **siempre antes** que el disco: un sistema apagado pierde la RAM para siempre.

---

## 4. Forense de disco

### 4.1 Adquirir una imagen (bit a bit)

```bash
# Linux — imagen física con hash integrado (dc3dd recomendado)
dc3dd if=/dev/sdb of=/evidencia/imagen.dd hash=sha256 log=hash.log

# Alternativa con dd (más universal)
dd if=/dev/sdb of=/evidencia/imagen.dd bs=4M conv=sync status=progress
```

> Windows: usa **FTK Imager** (GUI) para crear imágenes E01/DD.

### 4.2 Analizar con The Sleuth Kit (TSK)

```bash
# Ver particiones de la imagen
mmls imagen.dd

# Listar archivos de una partición (-o = offset de la partición)
fls -r -o 2048 imagen.dd

# Extraer un archivo por inode
icat -o 2048 imagen.dd <inode> > archivo_recuperado

# Recuperar archivos borrados
tsk_recover -o 2048 imagen.dd /salida/
```

### 4.3 Análisis con Autopsy (GUI)

- Abre la imagen `.dd`/`.E01`.
- Navega: **Deleted Files**, **File Types**, **Timeline**, **Keyword Search**.
- Extrae reportes con hash de cada artefacto.

### 4.4 Artefactos clave en Windows

| Artefacto | Qué revela | Herramienta |
|---|---|---|
| `Prefetch` (`C:\Windows\Prefetch`) | Ejecución de programas | PECmd |
| `Amcache.hve` / ShimCache | Historial de ejecución | AmcacheParser |
| `NTUSER.DAT` (Registry) | Run keys, MRU, USB | RegRipper |
| `$MFT` / `UsnJrnl` | Archivos creados/borrados | MFTECmd |
| LNK files | Archivos abiertos, rutas | LECmd |
| Browser history (SQLite) | Navegación | DB Browser / plaso |

---

## 5. Forense de memoria (Volatility 3)

### 5.1 Adquirir la RAM

```bash
# Linux (avml — recomendado)
avml memory.lime

# Windows
winpmem_3.0.exe memory.raw
```

### 5.2 Comandos esenciales de Volatility 3

```bash
# Info del sistema y perfil
vol -f memory.raw windows.info

# Lista de procesos
vol -f memory.raw windows.pslist

# Árbol de procesos (detecta procesos hijos sospechosos)
vol -f memory.raw windows.pstree

# Líneas de comando de cada proceso (oro puro)
vol -f memory.raw windows.cmdline

# Conexiones de red activas
vol -f memory.raw windows.netscan

# DLLs cargadas por un proceso
vol -f memory.raw windows.dlllist --pid 1234

# Detección de código inyectado (malfind)
vol -f memory.raw windows.malfind

# Archivos abiertos en memoria
vol -f memory.raw windows.filescan

# Hashes de credenciales (requiere privilegios)
vol -f memory.raw windows.hashdump
```

### 5.3 Qué buscar en memoria

| Indicador de compromiso | Plugin |
|---|---|
| Proceso sin padre legítimo | `pstree` |
| `cmd.exe`/`powershell` con base64 | `cmdline` |
| Conexión a IP externa no habitual | `netscan` |
| DLL inyectada en proceso legítimo | `malfind`, `dlllist` |
| `mimikatz`/`lsass` accediendo a SAM | `malfind`, `hashdump` |

---

## 6. Timeline forense (plaso)

Une **todos** los artefactos en una sola línea de tiempo ordenada:

```bash
# Generar la timeline desde la imagen/evidencia
log2timeline.py timeline.plaso imagen.dd

# Ver un resumen
pinfo.py timeline.plaso

# Filtrar y exportar (ej. eventos entre dos fechas)
psort.py -o l2tcsv -w salida.csv timeline.plaso "date > '2026-08-20 00:00:00'"
```

> Con la timeline CSV (usa **Timeline Explorer** de Eric Zimmerman para visualizar) puedes reconstruir la secuencia exacta: descarga → ejecución → persistencia → conexión.

---

## 7. Triage rápido (KAPE)

**KAPE** recolecta artefactos clave en minutos (para responder sin imagen completa):

```powershell
# Recolectar artefactos de un host Windows
kape.exe --tsource C: --target KapeTriage --tdest C:\evidencia

# Con módulos de parsing (procesa los artefactos)
kape.exe --tsource C:\evidencia --target KapeTriage --tdest C:\output --module KapeTriage
```

> Alternativa enterprise: **Velociraptor** (recolección remota de endpoints).

---

## 8. Reporte forense

Un reporte profesional responde, **sin tecnicismos innecesarios**:

1. **Alcance** — qué se analizó y qué preguntas se debían responder.
2. **Metodología** — herramientas, versión, proceso (NIST 800-86).
3. **Hallazgos** — qué se encontró, con hash y ubicación exacta.
4. **Timeline** — secuencia de eventos reconstruida.
5. **Conclusiones** — respuesta directa a las preguntas del caso.
6. **Cadena de custodia** — anexo con hashes y trazabilidad.

> **Entregable de portafolio:** un caso forense completo (p.ej. de [CyberDefenders](https://cyberdefenders.org/) o BlueTeamLabs Online) resuelto y documentado con este formato.

---

## 9. Referencias

- [NIST SP 800-86 — Guide to Integrating Forensic Techniques](https://csrc.nist.gov/pubs/sp/800/86/final)
- [RFC 3227 — Evidence Collection and Archiving](https://www.rfc-editor.org/rfc/rfc3227)
- [Volatility 3 Documentation](https://volatility3.readthedocs.io/)
- [The Sleuth Kit / Autopsy](https://www.sleuthkit.org/)
- [plaso (log2timeline)](https://plaso.readthedocs.io/)
- [KAPE (Kroll)](https://www.kroll.com/en/services/cyber-risk/incident-response-litigation-support/kroll-artifact-parser-extractor-kape)

---

**[⬅ Volver al módulo de Ciberseguridad](../../README.md)**
