---
title: "Módulo 02 — Blue Team / Defensa"
---

# 🛡️ Módulo 02 — Blue Team / Defensa

> **Objetivo:** Detectar, contener y erradicar amenazas en tiempo real usando herramientas y técnicas de defensa.

[![Nivel](https://img.shields.io/badge/Nivel-Intermedio-orange?style=flat-square)]()
[![Duración](https://img.shields.io/badge/Duración-2%20meses-blue?style=flat-square)]()

---

## 📋 Resumen del módulo

| Atributo | Detalle |
|----------|---------|
| **Pre-requisitos** | Módulo 01 completado |
| **Stack** | Wazuh, Suricata, Sigma, YARA, Sysmon |
| **Entregable** | Stack defensivo funcional |
| **Nivel** | Intermedio |

---

## 1. 🧠 Teoría: El stack defensivo

### Arquitectura de detección

```
┌─────────────────────────────────────────────────────┐
│              STACK DEFENSIVO                          │
├─────────────────────────────────────────────────────┤
│  [Endpoints]  →  Sysmon / Wazuh Agent               │
│  [Red]        →  Suricata IDS/IPS                    │
│  [Cloud]      →  CloudTrail / Activity Log           │
│  [Apps]       →  WAF / Application Logs              │
├─────────────────────────────────────────────────────┤
│              SIEM (Wazuh / ELK)                       │
│  - Correlación de eventos                            │
│  - Reglas de detección (Sigma)                       │
│  - Dashboards y alertas                              │
├─────────────────────────────────────────────────────┤
│              RESPUESTA                                │
│  - Contención automática                             │
│  - Investigación (Velociraptor)                      │
│  - Reporte de incidentes                             │
└─────────────────────────────────────────────────────┘
```

---

## 2. 🔧 Stack principal

### Wazuh — SIEM + XDR

```bash
# Instalación con Docker
git clone https://github.com/wazuh/wazuh-docker.git
cd wazuh-docker/single-node
docker compose up -d

# Configurar agente en endpoint
wget https://packages.wazuh.com/4.x/apt/pool/main/w/wazuh-agent/wazuh-agent_4.7.0-1_amd64.deb
sudo dpkg -i wazuh-agent_4.7.0-1_amd64.deb
sudo systemctl enable wazuh-agent
sudo systemctl start wazuh-agent
```

### Suricata — IDS/IPS de red

```bash
# Instalar
sudo apt install suricata

# Actualizar reglas
sudo suricata-update

# Ejecutar en modo IDS
sudo suricata -c /etc/suricata/suricata.yaml -i eth0
```

### Sigma — Reglas de detección

```yaml
# Ejemplo: Detección de PowerShell sospechoso
title: Suspicious PowerShell Download
id: 12345678-1234-1234-1234-123456789abc
status: experimental
description: Detects PowerShell downloading content from internet
logsource:
    category: process_creation
    product: windows
detection:
    selection:
        Image|endswith: '\powershell.exe'
        CommandLine|contains:
            - 'Invoke-WebRequest'
            - 'DownloadString'
            - 'Net.WebClient'
    condition: selection
level: high
tags:
    - attack.execution
    - attack.t1059.001
```

---

## 3. 📊 Detection Engineering

### Proceso de ingeniería de detección

```
1. Identificar TTP → MITRE ATT&CK
2. Crear regla Sigma → vendor-agnostic
3. Convertir a formato SIEM → Wazuh/Splunk
4. Probar con datos sintéticos → Atomic Red Team
5. Deploy en producción → Monitorear falsos positivos
6. Medir cobertura → % ATT&CK cubierto
```

### Métricas clave

| Métrica | Descripción | Objetivo |
|---------|-------------|----------|
| **Cobertura ATT&CK** | % de técnicas detectadas | > 60% |
| **MTTD** | Tiempo promedio de detección | < 30 min |
| **Tasa de falsos positivos** | Alertas incorrectas | < 5% |
| **Precisión** | Alertas correctas / total | > 90% |

---

## 4. 🔬 Práctica: Configurar Wazuh

### Paso 1: Instalar servidor

```bash
# Docker compose
curl -sO https://packages.wazuh.com/4.7/docker/wazuh-docker.tar.tar
tar -xzf wazuh-docker.tar.tar
cd wazuh-docker/single-node
docker compose up -d
```

### Paso 2: Configurar reglas custom

```xml
<!-- /var/ossec/etc/rules/local_rules.xml -->
<group name="custom,">
  <rule id="100100" level="10">
    <if_sid>1002</if_sid>
    <field name="srcip" />
    <description>Custom: Multiple auth failures from same IP</description>
  </rule>
</group>
```

### Paso 3: Dashboard

```
Accede a https://wazuh.company.com:443
Credenciales: admin/admin

Ir a:
- Security Events → Alertas en tiempo real
- Integrity Monitoring → Cambios en archivos
- Regulatory Compliance → PCI DSS, GDPR
```

---

## 5. ✏️ Ejercicios prácticos

### Ejercicio 1: Instalar Wazuh (30 min)

1. Instala Wazuh con Docker
2. Registra un agente (tu máquina o VM)
3. Genera una alerta (login fallido repetido)
4. Verifica la alerta en el dashboard

### Ejercicio 2: Crear regla Sigma (20 min)

1. Elige una técnica de MITRE ATT&CK
2. Escribe una regla Sigma para detectarla
3. Convierte a formato Wazuh
4. Prueba con Atomic Red Team

### Ejercicio 3: Medir cobertura (30 min)

1. Lista las técnicas de ATT&CK que tu equipo detecta
2. Calcula el porcentaje de cobertura
3. Identifica las 3 brechas más críticas
4. Prioriza qué detectar primero

---

> **Siguiente:** [Módulo 03 — SOC Operations](./03-soc-operations)
