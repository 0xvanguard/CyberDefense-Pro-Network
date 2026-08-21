---
title: "Módulo 06 — Forense de Endpoint y EDR"
---

# 🔎 Módulo 06 — Forense de Endpoint y EDR

> **Objetivo Principal:** Aprender a investigar endpoints comprometidos usando herramientas EDR y técnicas de forense de memoria y disco.

[![Nivel](https://img.shields.io/badge/Nivel-Avanzado-red?style=flat-square)]()
[![Duración](https://img.shields.io/badge/Duración-2%20meses-blue?style=flat-square)]()

---

## 📋 Resumen del módulo

| Atributo | Detalle |
|----------|---------|
| **Pre-requisitos** | Módulos 01-05 completados |
| **Herramientas** | Velociraptor, GRR, Volatility, Autopsy |
| **Entregable** | Análisis forense completo de endpoint |
| **Nivel** | Avanzado |

---

## 1. 🧠 Teoría: Forense de Endpoint

### Fuentes de evidencia en un endpoint

| Fuente | Qué revela | Volatilidad |
|--------|------------|-------------|
| **RAM (memoria)** | Procesos activos, contraseñas, conexiones | Muy alta |
| **Disco** | Archivos, logs, historial | Media |
| **Registry (Windows)** | Configuración, persistencia | Baja |
| **Event Logs** | Actividad del sistema | Baja |
| **MFT (NTFS)** | Metadatos de archivos | Baja |

### Orden de adquisición de evidencia

```
1. RAM (memoria volátil)
2. Disco (imagen forense)
3. Network (tráfico capturado)
4. Logs (eventos del sistema)
5. Cloud (logs de servicios)
```

---

## 2. 🛠️ Herramientas

### Velociraptor - EDR Open Source

```bash
# Artefactos útiles para forense
# Windows.Forensics.ProcessInfo    → Info de procesos
# Windows.Forensics.FileDownload   → Archivos descargados
# Windows.Forensics.UserAccess     → Historial de usuarios
# Windows.System.Pstree            → Árbol de procesos
```

### Volatility - Análisis de Memoria

```bash
# Listar procesos
volatility -f memory.dump pslist

# Buscar inyección de código
volatility -f memory.dump malfind

# Extraer archivos de memoria
volatility -f memory.dump dumpfiles -D output/

# Ver conexiones de red
volatility -f memory.dump netscan
```

---

## 3. 🔬 Práctica Guiada: Investigar Endpoint Comprometido

### Escenario: Estación de trabajo con sospecha de compromiso

#### Paso 1: Adquisición de memoria

```bash
# Usar WinPmem para capturar memoria
winpmem_mini_x64.exe memory_dump.raw

# Verificar tamaño (debe ser igual a RAM instalada)
ls -lh memory_dump.raw
```

#### Paso 2: Análisis de procesos

```bash
# Identificar procesos sospechosos
volatility -f memory.dump pslist | grep -E "(svchost|explorer|cmd|powershell)"

# Ver árbol de procesos
volatility -f memory.dump pstree

# Buscar procesos ocultos
volatility -f memory.dump psxview
```

#### Paso 3: Extraer artefactos

```bash
# Extraer archivos sospechosos
volatility -f memory.dump dumpfiles -Q [offset] -D extracted/

# Analizar con YARA
yara -r rules/ extracted/
```

---

## 4. 📊 Matriz de Análisis Forense

| Categoría | Qué buscar | Herramienta |
|-----------|------------|-------------|
| **Procesos** | Inyección de código, procesos fantasma | Volatility |
| **Red** | Conexiones C2, DNS tunneling | Volatility, Wireshark |
| **Archivos** | Archivos ocultos, alternate data streams | Autopsy |
| **Registro** | Keys de persistencia, RUN keys | Registry Explorer |
| **Cookies/Sesiones** | Tokens robados | Browser forensics |

---

## 5. 🎯 Mini-Entregable

**Tarea:** Analizar una imagen de memoria proporcionada y crear un reporte que incluya:

1. **Lista de procesos** activos al momento de la captura
2. **Procesos sospechosos** identificados
3. **Conexiones de red** activas
4. **Archivos extraídos** de memoria
5. **Indicadores de compromiso (IOCs)** encontrados

---

## 6. 🔗 Recursos Adicionales

- [Volatility Foundation](https://www.volatilityfoundation.org/)
- [Velociraptor Documentation](https://docs.velociraptor.app/)
- [Autopsy Digital Forensics](https://www.autopsy.com/)

---

> **Módulo completado.** Ahora tienes habilidades de Blue Team intermedias-avanzadas. Considera especializarte en [Incident Response](../blue-team/02-analisis-incidentes) o [Threat Hunting](../blue-team/03-threat-hunting).
