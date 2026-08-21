---
title: "Módulo 07 — Threat Intelligence Driven Purple Team"
---

# 🕵️ Módulo 07 — Threat Intelligence Driven Purple Team

> **Objetivo Principal:** Usar inteligencia de amenazas (CTI) para dirigir ejercicios purple team y validar defensas contra actores amenaza específicos.

[![Nivel](https://img.shields.io/badge/Nivel-Avanzado-red?style=flat-square)]()
[![Duración](https://img.shields.io/badge/Duración-2%20meses-blue?style=flat-square)]()

---

## 📋 Resumen del módulo

| Atributo | Detalle |
|----------|---------|
| **Pre-requisitos** | Módulos 01-06 completados |
| **Herramientas** | MISP, OpenCTI, MITRE ATT&CK, Sigma |
| **Entregable** | Ejercicio purple team basado en CTI |
| **Nivel** | Avanzado |

---

## 1. 🧠 Teoría: CTI + Purple Team

### ¿Por qué usar CTI en Purple Team?

| Enfoque tradicional | Con CTI |
|--------------------|---------|
| Testea técnicas genéricas | Testea TTPs de actores reales |
| Sin contexto de amenaza | Contextualizado |
| Priorización arbitraria | Priorizado por riesgo real |

### Fuentes de CTI

| Fuente | Tipo | Costo |
|--------|------|-------|
| **MITRE ATT&CK** | TTPs | Gratis |
| **MISP** | IOC sharing | Gratis |
| **AlienVault OTX** | IOC feeds | Gratis |
| **VirusTotal** | Malware IOCs | Freemium |
| ** Recorded Future** | CTI completa | $$$ |

---

## 2. 🛠️ Herramientas

### MISP - Threat Intelligence Platform

```bash
# Instalar MISP con Docker
git clone https://github.com/MISP/MISP.git
cd MISP
docker-compose up -d

# Acceder a la interfaz
# https://misp.local
# admin@admin.test / admin
```

### OpenCTI

```bash
# Instalar OpenCTI
git clone https://github.com/OpenCTI-Platform/opencti.git
cd opencti/docker
docker-compose up -d

# Configurar conectores
# - MITRE ATT&CK Connector
- AlienVault OTX Connector
- VirusTotal Connector
```

---

## 3. 🔬 Práctica Guiada: Purple Team basado en CTI

### Escenario: Defender contra APT29 (Cozy Bear)

#### Paso 1: Recopilar TTPs de APT29

```bash
# Usar MITRE ATT&CK para obtener TTPs
# https://attack.mitre.org/groups/G0016/

# TTPs principales de APT29:
# T1566.001 - Spearphishing Attachment
# T1059.001 - PowerShell
# T1003.001 - LSASS Memory
# T1021.002 - SMB/Windows Admin Shares
# T1053.005 - Scheduled Task
```

#### Paso 2: Crear reglas de detección

```yaml
# Sigma rule para detectar T1566.001
title: APT29 Phishing Attachment
status: stable
logsource:
    category: file_event
    product: windows
detection:
    selection:
        TargetFilename|endswith:
            - '.exe'
            - '.dll'
            - '.js'
        Image|endswith:
            - '\outlook.exe'
            - '\thunderbird.exe'
    condition: selection
level: high
```

#### Paso 3: Ejecutar simulación

```bash
# Usar Atomic Red Team para simular APT29
Invoke-AtomicRedTeam -TestIDs T1566.001  # Spearphishing
Invoke-AtomicRedTeam -TestIDs T1059.001  # PowerShell
Invoke-AtomicRedTeam -TestIDs T1003.001  # Credential Dump

# Medir detección para cada técnica
```

---

## 4. 📊 Análisis de Resultados

### Matriz de cobertura vs. APT29

| TTP APT29 | Detectado | MTTD | Herramienta |
|-----------|-----------|------|-------------|
| T1566.001 Spearphishing | ✅ Sí | 1 min | Email Gateway |
| T1059.001 PowerShell | ✅ Sí | 2 min | Wazuh |
| T1003.001 LSASS | ❌ No | - | - |
| T1021.002 SMB | ✅ Sí | 3 min | Network SIEM |
| T1053.005 Scheduled Task | ✅ Sí | 5 min | Sysmon |

### Brechas identificadas

1. **LSASS Memory Dump** no detectado → Implementar Credential Guard
2. **MTTD alto** para Scheduled Task → Optimizar reglas Sigma

---

## 5. 🎯 Mini-Entregable

**Tarea:** Ejecutar un ejercicio purple team basado en CTI que incluya:

1. **Selección** de actor amenaza (APT grupo)
2. **Recopilación** de TTPs de MITRE ATT&CK
3. **Simulación** de TTPs con Atomic Red Team
4. **Validación** de detecciones
5. **Reporte** de brechas y recomendaciones

---

## 6. 🔗 Recursos Adicionales

- [MITRE ATT&CK Groups](https://attack.mitre.org/groups/)
- [MISP Project](https://www.misp-project.org/)
- [OpenCTI](https://www.opencti.io/)
- [Atomic Red Team](https://github.com/redcanaryco/atomic-red-team)

---

> **Módulo completado.** Has completado el track de Purple Team. Ahora tienes habilidades para diseñar y ejecutar ejercicios purple team basados en inteligencia de amenazas.
