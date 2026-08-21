---
title: "Módulo 03 — Threat Hunting"
---

# 🎯 Módulo 03 — Threat Hunting

> **Objetivo Principal:** Aprender a buscar amenazas proactivamente en la red antes de que causen daño, usando hipótesis, datos y herramientas de caza.

[![Nivel](https://img.shields.io/badge/Nivel-Intermedio--Avanzado-orange?style=flat-square)]()
[![Duración](https://img.shields.io/badge/Duración-2%20meses-blue?style=flat-square)]()

---

## 📋 Resumen del módulo

| Atributo | Detalle |
|----------|---------|
| **Pre-requisitos** | Módulos 01 y 02 completados |
| **Herramientas** | Sigma, YARA, Velociraptor, ELK, MITRE ATT&CK |
| **Entregable** | Informe de Threat Hunting |
| **Nivel** | Intermedio-Avanzado |

---

## 1. 🧠 Teoría: ¿Qué es Threat Hunting?

Threat Hunting es la práctica de **buscar proactivamente** amenazas en una red, en lugar de esperar a que las alertas se activen. Se basa en:

### Metodología de Hunting

```
┌─────────────────────────────────────────────────────┐
│           CICLO DE THREAT HUNTING                      │
├─────────────┬──────────────┬────────────┬───────────┤
│  1. Hipótesis│ 2. Recolección│ 3. Análisis │ 4. Acción │
│  (¿Qué busco?)│ de Datos     │             │           │
├──────────────┼──────────────┼─────────────┼───────────┤
│ 5. Automatizar│ 6. Medir     │             │           │
│ Detección    │ Resultados   │             │           │
└──────────────┴──────────────┴─────────────┴───────────┘
```

### Tipos de Threat Hunting

| Tipo | Descripción | Ejemplo |
|------|-------------|---------|
| **Basado en Inteligencia** | Usa CTI para buscar IOCs específicos | Buscar hashes de malware conocido |
| **Basado en Comportamiento** | Usa TTPs de ATT&CK | Buscar Lateral Movement |
| **Basado en Anomalías** | Usa ML/estadística | Detectar cambios en patrones de red |
| **Basado en Hipótesis** | Investigar escenarios hipotéticos | "¿Qué pasaría si un atacante obtiene credenciales?" |

---

## 2. 🗺️ MITRE ATT&CK como Base

### Tácticas más cazadas por Blue Team

| Táctica | Técnicas Comunes | Herramientas de Detección |
|---------|------------------|---------------------------|
| **Reconocimiento** | Active Scanning | Network logs, DNS logs |
| **Acceso Inicial** | Phishing, Exploit Public | Email logs, Web logs |
| **Ejecución** | Command and Scripting | Process logs, Sysmon |
| **Persistencia** | Registry Run Keys | Sysmon, Autoruns |
| **Elevación de Privilegios** | Exploitation | Process creation logs |
| **Evasión** | Obfuscated Files | YARA, Antivirus logs |
| **Acceso a Credenciales** | LSASS Memory | Credential Guard, Sysmon |
| **Movimiento Lateral** | Remote Services | Network logs, Windows Event Logs |
| **Exfiltración** | Exfiltration Over C2 | Network traffic analysis |

---

## 3. 🛠️ Herramientas de Threat Hunting

### Velociraptor

```bash
# Instalar Velociraptor
wget https://docs.velociraptor.app/downloads/velociraptor_linux_amd64
chmod +x velociraptor_linux_amd64

# Crear servidor
./velociraptor_linux_amd64 gui

# Artefactos útiles para hunting
# Windows.Detection.Yara.Yara
# Windows.EventLogs.EvtxHunter
# Windows.System.Pstree
```

### Sigma Rules para Hunting

```yaml
# Ejemplo: Detectar PowerShell sospechoso
title: Suspicious PowerShell Command
status: experimental
logsource:
    category: process_creation
    product: windows
detection:
    selection:
        Image|endswith: '\powershell.exe'
        CommandLine|contains:
            - 'Invoke-Expression'
            - 'DownloadString'
            - 'Invoke-WebRequest'
            - 'Net.WebClient'
    condition: selection
level: high
```

---

## 4. 🔬 Práctica Guiada (Laboratorio)

### Escenario: Cazar un Emisor DNS Sospechoso

**Hipótesis:** "Un atacante está usando DNS tunneling para exfiltrar datos"

#### Paso 1: Recolectar datos DNS

```bash
# Capturar tráfico DNS
tcpdump -i eth0 port 53 -w dns_capture.pcap

# Analizar consultas DNS inusuales
tshark -r dns_capture.pcap -Y "dns.qry.name" -T fields -e dns.qry.name | \
  sort | uniq -c | sort -rn | head -20
```

#### Paso 2: Identificar anomalías

```bash
# Buscar dominios con nombres muy largos (tunneling)
tshark -r dns_capture.pcap -Y "dns.qry.name.len > 50" | head -20

# Buscar consultinas TXT inusuales
tshark -r dns_capture.pcap -Y "dns.txt" | head -10
```

#### Paso 3: Crear regla Sigma

```yaml
title: DNS Tunneling Detection
logsource:
    category: dns
detection:
    selection:
        query_name|re: '^[a-zA-Z0-9]{50,}\.'
    condition: selection
level: high
```

---

## 5. 📊 Métricas de Threat Hunting

| Métrica | Descripción | Objetivo |
|---------|-------------|----------|
| **Tiempo de detección (MTTD)** | Tiempo desde implantación hasta detección | < 24 horas |
| **Tiempo de respuesta (MTTR)** | Tiempo desde detección hasta contención | < 4 horas |
| **Cobertura de ATT&CK** | % de técnicas con detección | > 60% |
| **Falsos positivos** | Alertas que no son incidentes reales | < 10% |

---

## 6. 🎯 Mini-Entregable

**Tarea:** Realizar un ejercicio de Threat Hunting que incluya:

1. **Hipótesis** basada en un escenario dado
2. **Plan de recolección** de datos
3. **Análisis** de hallazgos
4. **Recomendaciones** de detección automática

---

## 7. 🔗 Recursos Adicionales

- [MITRE ATT&CK Navigator](https://attack.mitre.org/navigator/)
- [Threat Hunting Playbook](https://threathunterplaybook.com/)
- [Velociraptor Documentation](https://docs.velociraptor.app/)

---

> **Siguiente paso:** Continúa con el [Módulo 04 — SIEM y Monitoreo](../blue-team/04-siem-monitoreo) para aprender a configurar sistemas de detección.
