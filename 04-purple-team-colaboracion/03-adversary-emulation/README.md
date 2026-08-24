# 🟣 Adversary Emulation — Purple Team

> *"Si no sabes cómo ataca el adversario real, tu detección es solo una suposición."*

[![Nivel](https://img.shields.io/badge/Nivel-Avanzado-purple?style=flat-square)]()
[![Framework](https://img.shields.io/badge/Framework-MITRE%20ATT%26CK-red?style=flat-square)]()
[![Herramientas](https://img.shields.io/badge/Tools-Atomic%20Red%20Team%20%7C%20Caldera%20%7C%20MITRE%20ATT%26CK-blue?style=flat-square)]()

---

## 📋 Resumen del módulo

| Atributo | Detalle |
|---|---|
| 🏷️ **Nivel** | Avanzado |
| ⏱️ **Duración** | 6–8 semanas |
| 🎯 **Objetivo** | Emular adversarios reales, validar detecciones, medir cobertura |
| 🧪 **Práctica** | Atomic Red Team + Caldera + SIEM integration |
| 🗂️ **Portafolio** | Adversary emulation plan + detection gap analysis |

---

## 🎯 Qué aprenderás

- [ ] Diseñar planes de emulación de adversarios basados en MITRE ATT&CK
- [ ] Ejecutar Atomic Tests para validar detecciones
- [ ] Configurar MITRE Caldera para automatizar emulaciones
- [ ] Medir cobertura de detección (detection coverage)
- [ ] Crear rules de Sigma desde emulaciones
- [ ] Generar reportes ejecutivos de Purple Team

---

## 📚 Contenido

### 1. ¿Qué es Adversary Emulation?

La emulación de adversarios es el proceso de **simular tácticas, técnicas y procedimientos (TTPs)** de grupos de amenazas reales para:
- Validar que las detecciones funcionan
- Identificar gaps en visibilidad
- Probar la respuesta del SOC
- Medir la efectividad de controles

```
┌─────────────────────────────────────────────────────────────┐
│                   PURPLE TEAM PROCESS                       │
│                                                             │
│  1. PLANIFICACIÓN                                           │
│     ├─ Seleccionar adversario (APT29, Lazarus, FIN7)       │
│     ├─ Mapear TTPs a MITRE ATT&CK                          │
│     └─ Definir alcance y reglas de engagement              │
│                                                             │
│  2. EJECUCIÓN                                               │
│     ├─ Red Team ejecuta técnicas del adversario            │
│     ├─ Blue Team monitorea y detecta                       │
│     └─ Se registra qué se detectó y qué no                │
│                                                             │
│  3. ANÁLISIS                                                │
│     ├─ Gap analysis: ¿Qué faltó detectar?                 │
│     ├─ Timing: ¿Cuánto tiempo en detectar?                │
│     └─ Impacto: ¿Qué podría haber pasado?                 │
│                                                             │
│  4. MEJORA                                                  │
│     ├─ Crear nuevas detection rules                        │
│     ├─ Ajustar alertas existentes                          │
│     └─ Documentar lecciones aprendidas                     │
└─────────────────────────────────────────────────────────────┘
```

---

### 2. Atomic Red Team — Ejecución Directa

#### 2.1 Instalación
```powershell
# Instalar Atomic Red Team en Windows
IEX (IWR 'https://raw.githubusercontent.com/redcanaryco/invoke-atomicredteam/master/install-atomicredteam.ps1' -UseBasicParsing)
Install-AtomicRedTeam

# Linux
git clone https://github.com/redcanaryco/atomic-red-team.git
cd atomic-red-team
sudo bash install.sh
```

#### 2.2 Ejecutar Tests por Táctica

```powershell
# Listar todos los tests para una técnica
Invoke-AtomicRedTeam T1059.001 -ShowDetailsBrief

# Ejecutar test específico
Invoke-AtomicRedTeam T1059.001 -TestNumbers 1,2,3

# Ejecutar con cleanup automático
Invoke-AtomicRedTeam T1059.001 -Cleanup

# Ejecutar todas las técnicas de una táctica
Invoke-AtomicRedTeam T1059 -TestNumbers 1-20
```

#### 2.3 Atomic Tests por Táctica MITRE

| Táctica | Técnica | Test Atómico | Qué detecta |
|---------|---------|--------------|-------------|
| **Initial Access** | T1566.001 | Spearphishing Attachment | Malicious email opened |
| **Execution** | T1059.001 | PowerShell encoded command | Encoded PS execution |
| **Persistence** | T1547.001 | Registry Run Key | Autorun persistence |
| **Privilege Escalation** | T1068 | Exploitation for PE | Unquoted service path |
| **Defense Evasion** | T1562.001 | Disable Defender | AMSI bypass |
| **Credential Access** | T1003.001 | LSASS Memory Dump | Credential dumping |
| **Discovery** | T1087.001 | Account Discovery | net user enumeration |
| **Lateral Movement** | T1021.002 | SMB/Windows Admin Shares | Pass the hash |
| **Collection** | T1005 | Data from Local System | File collection |
| **Exfiltration** | T1041 | Exfil Over C2 Channel | Data exfiltration |
| **Impact** | T1486 | Data Encrypted for Impact | Ransomware simulation |

---

### 3. MITRE Caldera — Automatización

#### 3.1 Setup
```bash
# Clonar Caldera
git clone https://github.com/mitre/caldera.git --recursive
cd caldera

# Instalar dependencias
pip3 install -r requirements.txt

# Iniciar
python3 server.py --insecure --hostname 0.0.0.0

# Acceso: http://localhost:8888
# Default creds: admin / admin
```

#### 3.2 Crear un Plan de Emulación
```yaml
# adversary-emulation-plan.yml
name: "APT29 Cozy Bear Emulation"
description: "Emulación de APT29 basada en CISA advisory AA23-108A"

adversary:
  name: "APT29 (Cozy Bear)"
  description: "Russian SVR - Foreign Affairs"

operations:
  - name: "Initial Compromise"
    tactic: "initial-access"
    techniques:
      - technique_id: "T1566.002"
        name: "Spearphishing Link"
        description: "Enviar link malicioso via email"

  - name: "Execute Payload"
    tactic: "execution"
    techniques:
      - technique_id: "T1059.001"
        name: "PowerShell"
        description: "Ejecutar payload via PowerShell"

  - name: "Establish Persistence"
    tactic: "persistence"
    techniques:
      - technique_id: "T1053.005"
        name: "Scheduled Task"
        description: "Crear tarea programada persistente"

  - name: "Lateral Movement"
    tactic: "lateral-movement"
    techniques:
      - technique_id: "T1021.002"
        name: "SMB/Windows Admin Shares"
        description: "Moverse lateralmente via SMB"

  - name: "Data Exfiltration"
    tactic: "exfiltration"
    techniques:
      - technique_id: "T1041"
        name: "Exfil Over C2"
        description: "Exfiltrar datos via canal C2"
```

---

### 4. Detection Gap Analysis

#### 4.1 Matriz de Cobertura

```
                    DETECTADO    NO DETECTADO    PARCIAL
                   ┌───────────┬───────────────┬─────────┐
Initial Access     │           │               │    X    │
Execution          │     X     │               │         │
Persistence        │           │      X        │         │
Priv Esc           │     X     │               │         │
Defense Evasion    │           │      X        │         │
Credential Access  │           │               │    X    │
Discovery          │     X     │               │         │
Lateral Movement   │           │      X        │         │
Collection         │           │               │    X    │
Exfiltration       │     X     │               │         │
Impact             │     X     │               │         │
                   └───────────┴───────────────┴─────────┘

COBERTURA TOTAL: 45% (5/11 full, 3/11 partial)
```

#### 4.2 Detection Rules desde Emulación

```yaml
# sigma-rule-credential-dumping.yml
title: Credential Dumping via Mimikatz
id: a1b2c3d4-5678-90ab-cdef-1234567890ab
status: experimental
description: Detects Mimikatz execution based on process creation and command line
references:
  - https://attack.mitre.org/techniques/T1003/001/
author: Purple Team
date: 2026/01/15
tags:
  - attack.credential_access
  - attack.t1003.001
logsource:
  category: process_creation
  product: windows
detection:
  selection:
    EventID: 1
    Image|endswith:
      - '\mimikatz.exe'
      - '\mimikatz_x64.exe'
    CommandLine|contains:
      - 'sekurlsa::logonpasswords'
      - 'sekurlsa::wdigest'
      - 'lsadump::sam'
      - 'kerberos::golden'
  condition: selection
falsepositives:
  - Legitimate security testing
level: critical
```

---

### 5. Reporte Ejecutivo de Purple Team

#### 5.1 Plantilla
```markdown
# Purple Team Report — [Fecha]

## Resumen Ejecutivo
- **Adversario emulado:** APT29 (Cozy Bear)
- **Técnicas evaluadas:** 15
- **Cobertura de detección:** 45%
- **Tiempo promedio de detección:** 12 minutos
- **Riesgo residual:** ALTO

## Resultados por Táctica

| Táctica | Técnicas | Detectadas | Cobertura | Tiempo Prom. |
|---------|----------|------------|-----------|--------------|
| Initial Access | 2 | 1 | 50% | 0s |
| Execution | 3 | 3 | 100% | 5s |
| Persistence | 2 | 0 | 0% | N/A |
| Defense Evasion | 3 | 0 | 0% | N/A |
| Credential Access | 2 | 1 | 50% | 30s |
| Lateral Movement | 2 | 0 | 0% | N/A |
| Exfiltration | 1 | 1 | 100% | 15s |

## Gaps Críticos
1. **Persistence** — No hay detección de Scheduled Task creation
2. **Defense Evasion** — AMSI bypass no detectado
3. **Lateral Movement** — SMB lateral no monitoreado

## Recomendaciones
1. Implementar Sysmon para detección de persistence
2. Agregar Sigma rules para AMSI bypass
3. Configurar Wazuh para monitoreo SMB
4. Entrenar SOC en detección de lateral movement

## Plan de Acción
| # | Acción | Prioridad | Responsable | Fecha |
|---|--------|-----------|-------------|-------|
| 1 | Instalar Sysmon con config de SwiftOnSecurity | Crítica | Blue Team | Semana 1 |
| 2 | Deploy Sigma rules para persistence | Alta | SOC | Semana 2 |
| 3 | Configurar Wazuh para SMB monitoring | Alta | SOC | Semana 2 |
| 4 | Entrenamiento SOC en lateral movement | Media | Training | Semana 3 |
```

---

## 🧪 Laboratorios

| Lab | Descripción | Nivel |
|-----|-------------|-------|
| `lab-01` | Atomic Red Team: ejecutar tests de cada táctica | Básico |
| `lab-02` | Caldera: crear y ejecutar adversary plan | Intermedio |
| `lab-03` | Detection gap analysis completo | Intermedio |
| `lab-04` | Emulación completa de APT29 | Avanzado |
| `lab-05` | Crear Sigma rules desde resultados | Avanzado |

---

## 🔗 Referencias

- [Atomic Red Team](https://github.com/redcanaryco/atomic-red-team)
- [MITRE Caldera](https://github.com/mitre/caldera)
- [MITRE ATT&CK Navigator](https://mitre-attack.github.io/attack-navigator/)
- [Sigma Rules](https://github.com/SigmaHQ/sigma)
- [Purple Team Excellence](https://purpleteam.io/)
- [Detection Engineering](https://www.activecountermeasures.com/blog/)

---

*Última actualización: Agosto 2026*
