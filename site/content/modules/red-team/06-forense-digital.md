---
title: � Módulo 06 — Forense Digital
description: � Módulo 06 — Forense Digital
---

# 🔬 Módulo 06 — Forense Digital

> **Nivel:** Intermedio → Avanzado · **Objetivo:** reconstruir qué pasó en un sistema tras un incidente con evidencia íntegra y admisible usando el marco NIST SP 800-86.

[![Nivel](https://img.shields.io/badge/Nivel-Intermedio→Avanzado-orange?style=flat-square)]()
[![Enfoque](https://img.shields.io/badge/Enfoque-Blue%20Team-blue?style=flat-square)]()
[![Marco](https://img.shields.io/badge/Marco-NIST%20800--86-green?style=flat-square)]()

---

## 📋 Resumen

| Atributo | Detalle |
|---|---|
| 🎯 **Resultado** | Adquirir, analizar y reportar evidencia digital de forma forensemente válida |
| 🧪 **Práctica** | Volatility 3, The Sleuth Kit, Autopsy, plaso, KAPE, FTK Imager |
| 🗂️ **Portafolio** | Caso forense completo con metodología documentada |
| 🔗 **Requiere** | [Módulo 05 — Post-Explotación](../05-post-explotacion/) (conocimiento de persistencia y movimiento lateral) |

---

## 🎯 Objetivos de aprendizaje

Al completar este módulo deberías ser capaz de:

- **Cadena de custodia:** establecer y mantener la integridad de la evidencia con hashing y documentación.
- **Adquisición:** crear imágenes bit a bit de discos y memoria RAM sin alterar evidencia.
- **Análisis de disco:** identificar archivos borrados, artefactos de Windows (Prefetch, Registry, $MFT) y reconstruir actividades.
- **Análisis de memoria:** extraer procesos, conexiones de red, inyecciones de código y credenciales de volcados de RAM.
- **Timeline:** construir una línea de tiempo unificada que reconstruya la secuencia de eventos.
- **Reporte:** documentar hallazgos de forma clara, profesional y legalmente sólida.
- **Defensa:** entender cómo se detecta y previene la evasión forense.

---

## 🗂️ Estructura del módulo

| Carpeta | Contenido | Estado |
|---|---|---|
| [`adquisicion-preservacion/`](./adquisicion-preservacion/) | Cadena de custodia, volatilidad y adquisición | ✅ Completado |
| [`analisis-disco/`](./analisis-disco/) | Sistemas de archivos, particiones y herramientas de disco | ✅ Completado |
| [`analisis-memoria/`](./analisis-memoria/) | Volatility 3 y análisis de RAM | ✅ Completado |
| [`analisis-red/`](./analisis-red/) | Forense de tráfico de red | ✅ Completado |
| [`analisis-metadatos/`](./analisis-metadatos/) | Metadatos ocultos en archivos | ✅ Completado |
| [`timeline-reporte/`](./timeline-reporte/) | Línea de tiempo y reportes forenses | ✅ Completado |
| [`herramientas/`](./herramientas/) | Comparativa y guía de herramientas forenses | ✅ Completado |

### 📚 Contenido detallado

#### 1. Adquisición y Preservación

| Archivo | Contenido |
|---|---|
| [`01-cadena-custodia-adquisicion.md`](./adquisicion-preservacion/01-cadena-custodia-adquisicion.md) | Cadena de custodia, hashing, orden de volatilidad, adquisición de disco y memoria, protocolos legales |

#### 2. Análisis de Disco

| Archivo | Contenido |
|---|---|
| [`01-sistemas-archivos-img.md`](./analisis-disco/01-sistemas-archivos-img.md) | Sistemas de archivos (NTFS, EXT4, APFS), particiones, $MFT, UsnJrnl, archivos borrados |
| [`02-herramientas-disco.md`](./analisis-disco/02-herramientas-disco.md) | The Sleuth Kit, Autopsy, FTK Imager, Recuva, PhotoRec, dd vs dc3dd |

#### 3. Análisis de Memoria

| Archivo | Contenido |
|---|---|
| [`01-volatilidad-ram.md`](./analisis-memoria/01-volatilidad-ram.md) | Conceptos de volatilidad, adquisición de RAM, artefactos en memoria |
| [`02-herramientas-memoria.md`](./analisis-memoria/02-herramientas-memoria.md) | Volatility 3 completo, Volatility 2, Rekall, imageinfo, pslist, malfind, hashdump |

#### 4. Análisis de Red

| Archivo | Contenido |
|---|---|
| [`01-forense-red.md`](./analisis-red/01-forense-red.md) | Captura de tráfico, análisis de paquetes, detección de C2, DNS forense, firewall logs |

#### 5. Análisis de Metadatos

| Archivo | Contenido |
|---|---|
| [`01-metadatos-forenses.md`](./analisis-metadatos/01-metadatos-forenses.md) | EXIF, metadatos de documentos, steganography, fingerprinting de archivos |

#### 6. Timeline y Reporte

| Archivo | Contenido |
|---|---|
| [`01-construccion-timeline.md`](./timeline-reporte/01-construccion-timeline.md) | plaso/log2timeline, super timeline, filtrado por evento, correlación |
| [`02-reporte-forense.md`](./timeline-reporte/02-reporte-forense.md) | Estructura de reporte forense, plantilla profesional, ejemplos |

#### 7. Herramientas

| Archivo | Contenido |
|---|---|
| [`01-herramientas-forenses.md`](./herramientas/01-herramientas-forenses.md) | Comparativa completa, flujos de trabajo, KAPE, Velociraptor, CAINE |

---

## 🛠️ Herramientas principales

| Herramienta | Categoría | Uso principal |
|---|---|---|
| **Volatility 3** | Memoria | Análisis de volcados de RAM |
| **The Sleuth Kit / Autopsy** | Disco | Análisis de imágenes de disco |
| **FTK Imager** | Adquisición | Creación de imágenes bit a bit |
| **plaso / log2timeline** | Timeline | Super timeline unificada |
| **KAPE** | Triage | Recolección rápida de artefactos |
| **dc3dd** | Adquisición | dd con hashing integrado |
| **Velociraptor** | Enterprise | Recolección remota de endpoints |
| **CAINE** | Live forensics | Distro Linux forense |
| **exiftool** | Metadatos | Extracción y edición de metadatos |
| **Wireshark** | Red | Análisis de tráfico de red |

---

## ⚖️ Aviso ético

La forense digital **solo** se practica con:

- ✅ Autorización legal explícita (orden judicial, contrato de investigación)
- ✅ Cadena de custodia documentada
- ✅ Trabajo sobre copias, nunca sobre evidencia original
- ✅ Herramientas forenses certificadas y validadas
- ❌ Nada de acceder a sistemas sin autorización legal
- ❌ Nada de alterar evidencia (incluso accidentalmente)
- ❌ Nada de usar evidencia para beneficio personal

> **Importante:** en muchos países, la recopilación y análisis de evidencia digital sin autorización constituye un delito grave. Siempre verifica la legalidad antes de iniciar un análisis forense.

---

## 🔗 Encaje del módulo en la ruta

Dentro de la **Ruta 3 (Blue Team)**, este módulo es la **Fase C**:

1. `01-reconocimiento-osint/` ← Reconocimiento
2. `02-pentesting-red-team/` ← Pentesting
3. `03-analisis-vulnerabilidades/` ← Análisis
4. `04-explotacion-web/` ← Explotación
5. `05-post-explotacion/` ← Post-explotación
6. **`06-forense-digital/`** ← **Este módulo** (Fase C)
7. `07-ingenieria-social/` ← Ingeniería social
8. `08-criptografia/` ← Criptografía

---

## ✅ Checkpoint

¿Puedes hacer lo siguiente sin guía?

- [ ] Crear una imagen bit a bit de un disco con dc3dd y verificar integridad con SHA-256
- [ ] Documentar una cadena de custodia completa para una evidencia digital
- [ ] Analizar una imagen de disco con Autopsy y recuperar archivos borrados
- [ ] Analizar un volcado de memoria con Volatility 3 (pslist, netscan, malfind)
- [ ] Construir una super timeline con plaso desde múltiples artefactos
- [ ] Redactar un reporte forense profesional que responda preguntas del caso
- [ ] Explicar cómo cada fase del proceso forense se relaciona con NIST SP 800-86

Si todo es ✅, estás listo para el siguiente paso: **[Módulo 07 — Ingeniería Social](../07-ingenieria-social/)**.

---

**[⬅ Volver a Ciberseguridad](../README.md)** · **[🗺️ Ver Rutas](../../RUTAS.md)**
