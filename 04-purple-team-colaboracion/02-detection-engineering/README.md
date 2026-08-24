# 🔍 Detection Engineering

> *"El SOC promedio ve 11,000 alertas al día. El detection engineer ve 11 y todas son reales."*

[![Nivel](https://img.shields.io/badge/Nivel-Avanzado-green?style=flat-square)]()
[![Herramientas](https://img.shields.io/badge/Tools-Sysmon%20%7C%20Sigma%20%7C%20Wazuh%20%7C%20ELK-blue?style=flat-square)]()
[![Framework](https://img.shields.io/badge/Framework-MITRE%20ATT%26CK-red?style=flat-square)]()

---

## 📋 Resumen

| Atributo | Detalle |
|---|---|
| 🏷️ **Nivel** | Avanzado |
| ⏱️ **Duración** | 4–6 semanas |
| 🎯 **Objetivo** | Crear detecciones de calidad, reducir falsos positivos, medir cobertura |

---

## 📚 Contenido

### 1. Principios de Detection Engineering

```
┌─────────────────────────────────────────────────────────────┐
│              DETECTION ENGINEERING CYCLE                     │
│                                                             │
│  1. THREAT INTEL → ¿Qué técnicas usa el adversario?        │
│         ↓                                                   │
│  2. HYPOTHESIS → "Si el adversario hace X, veré Y"         │
│         ↓                                                   │
│  3. DATA SOURCES → ¿Tengo los logs necesarios?             │
│         ↓                                                   │
│  4. DETECTION → Crear rule (Sigma/YARA/SIEM)               │
│         ↓                                                   │
│  5. TEST → Ejecutar Atomic Red Team, validar               │
│         ↓                                                   │
│  6. TUNE → Reducir falsos positivos                        │
│         ↓                                                   │
│  7. DEPLOY → Prod → Monitorear → Mejorar                   │
└─────────────────────────────────────────────────────────────┘
```

### 2. Data Sources — Qué logs necesitas

| Fuente | Eventos Clave | Herramienta |
|--------|---------------|-------------|
| **Process Creation** | New process, parent-child | Sysmon Event 1 |
| **Network Connection** | Outbound connections | Sysmon Event 3 |
| **File Creation** | New files, modifications | Sysmon Event 11 |
| **Registry Modification** | Autorun keys, services | Sysmon Event 13 |
| **WMI Activity** | WMI subscriptions | Sysmon Event 19-21 |
| **DNS Queries** | DNS requests | Sysmon Event 22 |
| **PowerShell Logging** | Script block, module | PowerShell logging |
| **Windows Event Logs** | 4624/4625 (logon), 4720 (user created) | Windows Events |

### 3. Sysmon — La piedra angular

#### 3.1 Configuración base
```xml
<Sysmon schemaversion="4.90">
  <HashAlgorithms>sha256,imphash</HashAlgorithms>
  <CheckRevocation/>
  
  <!-- Process Creation -->
  <RuleGroup name="" groupRelation="or">
    <ProcessCreate onmatch="include">
      <Name condition="is">powershell.exe</Name>
      <Name condition="is">cmd.exe</Name>
      <Name condition="is">wscript.exe</Name>
      <Name condition="is">mshta.exe</Name>
      <ParentImage condition="end with">winword.exe</ParentImage>
      <ParentImage condition="end with">excel.exe</ParentImage>
    </ProcessCreate>
  </RuleGroup>
  
  <!-- Network Connections -->
  <RuleGroup name="" groupRelation="or">
    <NetworkConnect onmatch="include">
      <DestinationPort condition="is">4444</DestinationPort>
      <DestinationPort condition="is">5555</DestinationPort>
      <Image condition="end with">powershell.exe</Image>
      <Image condition="end with">cmd.exe</Image>
    </NetworkConnect>
  </RuleGroup>
  
  <!-- Registry Modifications -->
  <RuleGroup name="" groupRelation="or">
    <RegistryEvent onmatch="include">
      <TargetObject condition="contains">CurrentVersion\Run</TargetObject>
      <TargetObject condition="contains">CurrentVersion\RunOnce</TargetObject>
      <TargetObject condition="contains">Services</TargetObject>
    </RegistryEvent>
  </RuleGroup>
  
  <!-- File Creation -->
  <RuleGroup name="" groupRelation="or">
    <FileCreate onmatch="include">
      <TargetFilename condition="end with">.exe</TargetFilename>
      <TargetFilename condition="end with">.dll</TargetFilename>
      <TargetFilename condition="contains">\AppData\</TargetFilename>
    </FileCreate>
  </RuleGroup>
</Sysmon>
```

### 4. Sigma Rules — Detección portable

#### 4.1 Estructura de una Sigma Rule
```yaml
title: Suspicious PowerShell Encoded Command
id: 12345678-1234-1234-1234-123456789abc
status: stable
description: Detects PowerShell with encoded command (common in attacks)
references:
  - https://attack.mitre.org/techniques/T1059/001/
author: Purple Team
date: 2026/01/15
modified: 2026/01/20
tags:
  - attack.execution
  - attack.t1059.001
  - attack.defense_evasion
  - attack.t1027
logsource:
  category: process_creation
  product: windows
detection:
  selection:
    EventID: 1
    Image|endswith:
      - '\powershell.exe'
      - '\pwsh.exe'
    CommandLine|contains:
      - '-enc'
      - '-EncodedCommand'
      - '-e '
  condition: selection
falsepositives:
  - Legitimate admin scripts
  - SCCM tasks
level: high
```

#### 4.2 Sigma Rules Críticas

| Rule | Táctica | Severidad | Falso Positivo |
|------|---------|-----------|-----------------|
| Encoded PowerShell | Execution | High | Medio |
| LSASS Access | Credential Access | Critical | Bajo |
| Scheduled Task Creation | Persistence | Medium | Medio |
| Service Installation | Persistence | Medium | Medio |
| WMI Process Creation | Execution | High | Bajo |
| DNS C2 | Command & Control | High | Bajo |
| Registry Autorun | Persistence | Medium | Medio |
| Named Pipe Creation | Lateral Movement | Medium | Bajo |
| SMB Lateral | Lateral Movement | High | Medio |
| Data Staging | Collection | High | Bajo |

### 5. Reducción de Falsos Positivos

```yaml
# Estrategias de tuning:

# 1. Whitelist por contexto
falsepositives:
  - Process: "C:\Windows\System32\*"
  - ParentImage: "C:\Program Files\*"

# 2. Correlación multi-evento
detection:
  selection1:
    EventID: 1
    Image|endswith: '\mimikatz.exe'
  selection2:
    EventID: 3
    DestinationPort: 4444
  condition: selection1 and selection2

# 3. Threshold-based
detection:
  selection:
    EventID: 4625
  condition: selection | count(TargetUserName) by IpAddress > 10
  timeframe: 5m

# 4. Exclusion patterns
detection:
  selection:
    EventID: 1
    Image|endswith: '\svchost.exe'
  filter:
    ParentImage|endswith: 'services.exe'
  condition: selection and not filter
```

---

## 🧪 Laboratorios

| Lab | Descripción | Nivel |
|-----|-------------|-------|
| `lab-01` | Instalar Sysmon + crear config personalizada | Básico |
| `lab-02` | Crear 10 Sigma rules para techniques comunes | Intermedio |
| `lab-03` | Deployment Wazuh + Sigma integration | Intermedio |
| `lab-04` | Detection engineering pipeline completo | Avanzado |

---

## 🔗 Referencias

- [Sysmon](https://docs.microsoft.com/en-us/sysinternals/downloads/sysmon)
- [Sigma Rules](https://github.com/SigmaHQ/sigma)
- [SwiftOnSecurity Sysmon Config](https://github.com/SwiftOnSecurity/sysmon-config)
- [Detection Engineering](https://www.activecountermeasures.com/)

---

*Última actualización: Agosto 2026*
