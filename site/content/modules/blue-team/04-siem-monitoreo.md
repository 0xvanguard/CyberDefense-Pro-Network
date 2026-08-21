---
title: "Módulo 04 — SIEM y Monitoreo de Seguridad"
---

# 📊 Módulo 04 — SIEM y Monitoreo de Seguridad

> **Objetivo Principal:** Configurar y usar sistemas SIEM (Splunk, ELK, Wazuh) para detectar amenazas en tiempo real.

[![Nivel](https://img.shields.io/badge/Nivel-Intermedio-orange?style=flat-square)]()
[![Duración](https://img.shields.io/badge/Duración-2%20meses-blue?style=flat-square)]()

---

## 📋 Resumen del módulo

| Atributo | Detalle |
|----------|---------|
| **Pre-requisitos** | Módulo 01 completado |
| **Herramientas** | Wazuh, ELK Stack, Splunk Free |
| **Entregable** | Dashboard de monitoreo funcional |
| **Nivel** | Intermedio |

---

## 1. 🧠 Teoría: ¿Qué es un SIEM?

**SIEM** = Security Information and Event Management

Un SIEM recopila, analiza y correlaciona eventos de seguridad de toda la infraestructura.

### Arquitectura típica

```
┌─────────────────────────────────────────────────────┐
│                    SIEM Architecture                  │
├─────────────────────────────────────────────────────┤
│  [Endpoints] [Network] [Cloud] [Applications]       │
│       ↓          ↓        ↓          ↓              │
│  ┌─────────────────────────────────────────┐        │
│  │         Log Collection Layer             │        │
│  │    (Agents, Syslog, API, Beats)          │        │
│  └─────────────────────────────────────────┘        │
│                     ↓                                │
│  ┌─────────────────────────────────────────┐        │
│  │         Parsing & Normalization          │        │
│  └─────────────────────────────────────────┘        │
│                     ↓                                │
│  ┌─────────────────────────────────────────┐        │
│  │         Correlation Engine               │        │
│  │    (Rules, ML, Behavioral Analytics)     │        │
│  └─────────────────────────────────────────┘        │
│                     ↓                                │
│  ┌─────────────────────────────────────────┐        │
│  │    Dashboards, Alerts, Reports           │        │
│  └─────────────────────────────────────────┘        │
└─────────────────────────────────────────────────────┘
```

### SIEM Comparison

| Característica | Wazuh | ELK Stack | Splunk Free |
|---------------|-------|-----------|-------------|
| **Costo** | Gratis | Gratis | Gratis (500MB/día) |
| **Facilidad** | ⭐⭐⭐⭐ | ⭐⭐⭐ | ⭐⭐⭐⭐ |
| **Detección** | ⭐⭐⭐⭐⭐ | ⭐⭐⭐ | ⭐⭐⭐⭐ |
| **Integraciones** | ⭐⭐⭐⭐ | ⭐⭐⭐⭐⭐ | ⭐⭐⭐⭐⭐ |
| **Escalabilidad** | ⭐⭐⭐⭐ | ⭐⭐⭐⭐⭐ | ⭐⭐⭐⭐⭐ |

---

## 2. 🛠️ Wazuh: SIEM Gratuito y Open Source

### Instalación con Docker

```bash
# Clonar repositorio oficial
git clone https://github.com/wazuh/wazuh-docker.git
cd wazuh-docker/single-node

# Configurar variables de entorno
cp .env.example .env

# Iniciar Wazuh
docker compose up -d

# Verificar estado
docker compose ps
```

### Configuración básica

```xml
<!-- /var/ossec/etc/ossec.conf -->
<ossec_config>
  <global>
    <email_notification>yes</email_notification>
    <email_to>admin@company.com</email_to>
    <smtp_server>smtp.company.com</smtp_server>
    <email_from>wazuh@company.com</email_from>
  </global>

  <alerts>
    <log_alert_level>1</log_alert_level>
    <email_alert_level>10</email_alert_level>
  </alerts>
</ossec_config>
```

---

## 3. 🔬 Práctica Guiada: Detectar Brute Force

### Paso 1: Configurar monitoreo SSH

```bash
# En Wazuh agent (Linux)
# /var/ossec/etc/ossec.conf
<localfile>
  <log_format>syslog</log_format>
  <location>/var/log/auth.log</location>
</localfile>
```

### Paso 2: Regla de detección

```xml
<!-- Regla para detectar intentos de brute force -->
<group name="authentication_failures,">
  <rule id="100200" level="10">
    <if_sid>1002</if_sid>
    <field name="srcip" />
    <description>Multiple authentication failures from same IP</description>
    <group>pci_dss_10.2.4,gdpr_IV_32.1,</group>
  </rule>
</group>
```

### Paso 3: Dashboard en Wazuh

```
Visitas: https://wazuh.company.com:443
Credenciales: admin/admin

1. Ir a "Security Events"
2. Crear filtro: rule.id = 100200
3. Crear dashboard con gráficos de:
   - Top 10 IPs con más intentos
   - Timeline de intentos fallidos
   - Usuarios target
```

---

## 4. 📊 Métricas Clave de SIEM

| Métrica | Descripción | Objetivo |
|---------|-------------|----------|
| **Eventos por segundo (EPS)** | Volumen de logs procesados | Capacidad adecuada |
| **Tiempo de detección** | Tiempo entre evento y alerta | < 5 minutos |
| **Tasa de falsos positivos** | Alertas incorrectas | < 5% |
| **Cobertura de activos** | % de sistemas monitoreados | > 95% |

---

## 5. 🎯 Mini-Entregable

**Tarea:** Configurar Wazuh o ELK Stack y crear un dashboard que muestre:

1. **Intentos de autenticación** fallidos
2. **Procesos sospechosos** ejecutados
3. **Conexiones de red** inusuales
4. **Alertas de severity** alta

---

## 6. 🔗 Recursos Adicionales

- [Wazuh Documentation](https://documentation.wazuh.com/)
- [Elastic SIEM Guide](https://www.elastic.co/guide/en/siem/current/index.html)
- [Splunk Free Training](https://www.splunk.com/en_us/training.html)

---

> **Siguiente paso:** Continúa con el [Módulo 05 — Hardening y Seguridad](../blue-team/05-hardening) para aprender a proteger sistemas.
