# 🛡️ SIEM con Wazuh — Guía profesional

> **Nivel:** Intermedio → Avanzado · **Herramienta:** [Wazuh](https://wazuh.com/) (open source, fork de OSSEC)
>
> Objetivo: montar un SIEM real, escribir **tus propias reglas de detección**, integrar fuentes (Sysmon, Suricata) y ejecutar **respuesta activa** (bloqueo automático). No es "instalar y ver el dashboard": es construir detección profesional.

---

## Índice

1. [Qué es un SIEM y dónde encaja Wazuh](#1-qué-es-un-siem-y-dónde-encaja-wazuh)
2. [Arquitectura](#2-arquitectura)
3. [Instalación (Docker Compose)](#3-instalación-docker-compose)
4. [Agentes y fuentes de logs](#4-agentes-y-fuentes-de-logs)
5. [Decoders y reglas custom (el corazón)](#5-decoders-y-reglas-custom-el-corazón)
6. [Integración: Sysmon y Suricata](#6-integración-sysmon-y-suricata)
7. [Active Response (bloqueo automático)](#7-active-response-bloqueo-automático)
8. [Detección mapeada a MITRE ATT&CK](#8-detección-mapeada-a-mitre-attck)
9. [Lab de verificación end-to-end](#9-lab-de-verificación-end-to-end)
10. [Referencias](#10-referencias)

---

## 1. Qué es un SIEM y dónde encaja Wazuh

Un **SIEM** (Security Information and Event Management) centraliza logs, los **correlaciona** y genera **alertas** sobre comportamientos anómalos. Wazuh hace esto con tres capacidades integradas:

| Capacidad | Qué hace | Equivalente comercial |
|---|---|---|
| **Log collection + analysis** | Recolecta logs y aplica reglas | Splunk/QRadar |
| **FIM** (File Integrity Monitoring) | Detecta cambios en archivos críticos | Tripwire |
| **Active Response** | Ejecuta contramedidas automáticas | SOAR básico |
| **Vulnerability detection** | Correlaciona CVEs con agentes | Qualys/Nessus lite |

Wazuh **no es** un almacén de logs a gran escala (eso es OpenSearch/Elasticsearch), pero como SIEM de detección es excelente para aprender y para entornos medianos.

---

## 2. Arquitectura

```
┌─────────────────────────────────────────────────────┐
│  Wazuh Dashboard (interfaz web)                     │
│         ▲                                           │
│  Wazuh Indexer (OpenSearch)  ← almacena alertas/logs│
│         ▲                                           │
│  Wazuh Manager  ← análisis, correlación, reglas     │
│         ▲                                           │
│  ┌──────┴──────┬──────────┬───────────┐             │
│  Agent (Linux) Agent (Win)  Syslog    Suricata      │
│  /var/log/...  Sysmon      servidores  eve.json     │
└─────────────────────────────────────────────────────┘
```

- **Manager:** análisis + reglas + active response.
- **Indexer:** OpenSearch (almacenamiento + búsqueda).
- **Dashboard:** interfaz (fork de Kibana).
- **Agent:** recolecta logs de cada host (Windows/Linux/macOS).

---

## 3. Instalación (Docker Compose)

La forma más rápida y reproducible es el repo oficial. Usa `-p` para levantar el **single-node**:

```bash
git clone https://github.com/wazuh/wazuh-docker.git -b v4.9.0
cd wazuh-docker/single-node

# Generar certificados y credenciales
docker compose -f generate-indexer-certs.yml run --rm generator

# Levantar el stack (manager + indexer + dashboard)
docker compose up -d
```

Credenciales por defecto: `admin` / `SecretPassword` (cámbialas). Dashboard en `https://localhost`.

> Para producción/multi-nodo, el repo oficial trae `docker-compose.yml` con cluster indexer. Para este repo de estudio, single-node es suficiente.

---

## 4. Agentes y fuentes de logs

### 4.1 Instalar un agente (Linux)

```bash
curl -s https://packages.wazuh.com/4.x/wazuh-install.sh | bash
# o desde el dashboard: Agentes → Deploy new agent → copia el comando generado
```

Puntos clave de `/var/ossec/etc/ossec.conf` en el agente:

```xml
<client>
  <server>
    <address>IP_DEL_MANAGER</address>
    <port>1514</port>
    <protocol>tcp</protocol>
  </server>
</client>
```

### 4.2 Qué logs recolecta por defecto

Wazuh lee por defecto:
- Linux: `/var/log/auth.log`, `syslog`, `secure`, audit logs.
- Windows: Event Viewer (Security, System, Application) vía `eventchannel`.

### 4.3 Añadir un log custom

```xml
<!-- ossec.conf del agente -->
<localfile>
  <location>/var/log/mi-app/app.log</location>
  <log_format>syslog</log_format>
</localfile>
```

---

## 5. Decoders y reglas custom (el corazón)

> **Regla de oro:** Wazuh trae ~3000 reglas por defecto. Tu valor como analista está en crear reglas **propias** sobre fuentes **propias**. Ahí es donde se demuestra nivel profesional.

### 5.1 Decoder — extraer campos de un log custom

Archivo: `/var/ossec/etc/decoders/local_decoder.xml`

Supón un log así: `custom_app: user=admin srcip=203.0.113.50 action=login_failed`

```xml
<decoder name="custom_app">
  <prematch>^custom_app:</prematch>
</decoder>

<decoder name="custom_app_child">
  <parent>custom_app</parent>
  <regex>user=(\S+) srcip=(\S+) action=(\S+)</regex>
  <order>user, srcip, action</order>
</decoder>
```

### 5.2 Regla — detectar un patrón

Archivo: `/var/ossec/etc/rules/local_rules.xml`

```xml
<group name="custom,attack,">

  <!-- Login fallido de la app custom -->
  <rule id="100100" level="5">
    <decoded_as>custom_app</decoded_as>
    <match>action=login_failed</match>
    <description>Custom app: login failed</description>
  </rule>

  <!-- Fuerza bruta: 8 fallos de la misma IP en 2 minutos -->
  <rule id="100101" level="10">
    <if_sid>100100</if_sid>
    <same_source_ip />
    <frequency>8</frequency>
    <timeframe>120</timeframe>
    <description>Posible fuerza bruta contra custom_app</description>
    <mitre>
      <id>T1110</id>  <!-- Brute Force -->
    </mitre>
  </rule>

</group>
```

### 5.3 Niveles de severidad (levels)

| Level | Significado | Uso típico |
|---|---|---|
| 0–3 | Informativo | Eventos normales |
| 4–6 | Bajo | Sospechoso, requiere revisión |
| 7–9 | Medio | Alerta de seguridad |
| 10–12 | Alto | Requiere respuesta |
| 13–15 | Crítico | Incidente confirmado |

### 5.4 Verificar que la regla funciona

```bash
# Testear la configuración
/var/ossec/bin/wazuh-logtest

# Insertar un log de prueba y ver si dispara la regla
echo 'custom_app: user=admin srcip=203.0.113.50 action=login_failed' | /var/ossec/bin/wazuh-logtest
```

---

## 6. Integración: Sysmon y Suricata

### 6.1 Sysmon (Windows) — telemetría de endpoint

Sysmon (de Sysinternals) registra creación de procesos, conexiones de red, carga de DLLs, etc. Es **la fuente más valiosa** para detección de técnicas ofensivas.

Config en el agente Windows (`ossec.conf`):

```xml
<localfile>
  <location>Microsoft-Windows-Sysmon/Operational</location>
  <log_format>eventchannel</log_format>
</localfile>
```

Instala Sysmon con una config de referencia (SwiftOnSecurity o Olaf Hartong):

```powershell
sysmon64 -accepteula -i sysmonconfig.xml
```

> Descarga: [Olaf Hartong Sysmon-modular](https://github.com/olafhartong/sysmon-modular) — configs profesionales mantenidas.

### 6.2 Suricata (red) — detección de tráfico

Config en el agente Linux que corre Suricata:

```xml
<localfile>
  <location>/var/log/suricata/eve.json</location>
  <log_format>json</log_format>
</localfile>
```

Regla Suricata de ejemplo (detecta nmap SYN scan):

```
alert tcp any any -> $HOME_NET any (msg:"Nmap SYN scan"; flags:S; threshold: type both, track by_src, count 30, seconds 5; sid:1000001; rev:1;)
```

---

## 7. Active Response (bloqueo automático)

Permite ejecutar acciones automáticas cuando una regla dispara. Ejemplo: bloquear la IP que hace fuerza bruta.

### 7.1 Configurar el comando (manager)

Archivo: `/var/ossec/etc/ossec.conf`

```xml
<command>
  <name>firewall-drop</name>
  <executable>firewall-drop</executable>
  <timeout_allowed>yes</timeout_allowed>
</command>

<active-response>
  <command>firewall-drop</command>
  <location>local</location>
  <rules_id>100101</rules_id>   <!-- la regla de fuerza bruta -->
  <timeout>600</timeout>         <!-- desbloquear tras 10 min -->
</active-response>
```

### 7.2 Script `firewall-drop` (en el agente)

```bash
#!/bin/bash
# /var/ossec/active-response/bin/firewall-drop
IP=$4
ACTION=$1

if [ "$ACTION" = "add" ]; then
    iptables -I INPUT -s "$IP" -j DROP
elif [ "$ACTION" = "delete" ]; then
    iptables -D INPUT -s "$IP" -j DROP
fi
```

> ⚠️ En producción, valida umbrales para no bloquear tráfico legítimo (false positive → bloqueo de usuarios reales).

---

## 8. Detección mapeada a MITRE ATT&CK

Cada regla custom debería mapearse a una técnica ATT&CK (tag `<mitre>`). Ejemplos de detecciones imprescindibles para un SOC:

| Técnica ATT&CK | Qué detectar | Fuente |
|---|---|---|
| **T1110** Brute Force | `frequency` de login fallidos | auth.log / Security |
| **T1078** Valid Accounts | Login desde IP nueva o geolocalización anómala | auth + geoip |
| **T1547** Boot/Logon Autostart | Cambios en Run keys / servicios (FIM) | Sysmon + FIM |
| **T1059** Command & Scripting | `powershell -enc`, `bash -c` con base64 | Sysmon (EventID 1) |
| **T1003** Credential Dumping | Acceso a `lsass.exe`, `sam`, `ntds.dit` | Sysmon (EventID 10/11) |
| **T1570** Lateral Tool Transfer | Transferencia de archivos entre hosts | Sysmon + Suricata |

---

## 9. Lab de verificación end-to-end

1. Levanta el stack (sección 3).
2. Registra un agente Linux + un Windows (con Sysmon).
3. Crea la regla de fuerza bruta (sección 5.2).
4. Desde otra máquina, lanza `hydra -l admin -P rockyou.txt ssh://IP`.
5. Verifica en el **Dashboard → Security events** que la alerta `100101` dispara.
6. Confirma en el agente que `iptables -L` muestra la IP bloqueada (active response).

**Entregable de portafolio:** captura del dashboard con la alerta + la regla custom + el log del bloqueo. Documenta el ciclo completo (ataque → detección → respuesta).

---

## 10. Referencias

- [Wazuh Documentation (oficial)](https://documentation.wazuh.com/)
- [Wazuh Docker (oficial)](https://github.com/wazuh/wazuh-docker)
- [Sysmon-modular (configs)](https://github.com/olafhartong/sysmon-modular)
- [MITRE ATT&CK](https://attack.mitre.org/)

---

**[⬅ Volver al módulo Blue Team](../README.md)**
