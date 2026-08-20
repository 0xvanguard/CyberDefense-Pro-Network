# 🔍 Threat Hunting + Detección con Sigma y YARA

> **Nivel:** Intermedio → Avanzado
>
> Objetivo: pasar de "reaccionar a alertas" a **cazar proactivamente** y **escribir detección como código** (detection-as-code). Aquí vives dos disciplinas: **threat hunting** (metodología) y **Sigma/YARA** (los lenguajes de detección).

---

## Índice

1. [Threat hunting: qué es y qué no es](#1-threat-hunting-qué-es-y-qué-no-es)
2. [Metodología de caza (hipótesis → PEAK)](#2-metodología-de-caza-hipótesis--peak)
3. [Sigma: detección universal](#3-sigma-detección-universal)
4. [YARA: firmas de malware y patrones](#4-yara-firmas-de-malware-y-patrones)
5. [Pipeline de detection-as-code](#5-pipeline-de-detection-as-code)
6. [Referencias](#6-referencias)

---

## 1. Threat hunting: qué es y qué no es

| | Es | No es |
|---|---|---|
| **Threat hunting** | Búsqueda **proactiva** de amenazas basada en hipótesis, partiendo de la suposición de que ya hay un compromiso | Esperar alertas del SIEM |
| **Detection engineering** | Construir/mejorar reglas para detectar lo que cazaste | Escribir reglas sin validar |

> **Filosofía:** el hunting busca lo que **no** disparó una alerta. La regla de oro: *"el atacante ya está dentro; demuéstrame que no."*

---

## 2. Metodología de caza (hipótesis → PEAK)

El modelo más usado en la industria es **PEAK** (de Splunk/SANS) y el clásico **TaHiTI**. En esencia, toda caza sigue:

```
1. Hipótesis   → "Si un atacante hiciera X, ¿cómo se vería en mis datos?"
2. Datos       → ¿Tengo la telemetría para responderla? (Sysmon, auth, DNS, proxy)
3. Query       → Escribir la búsqueda que confirma/refuta
4. Resultado   → ¿Encontré algo? → alerta nueva o investigación
```

### Plantilla de hipótesis (profesional)

```text
HIPÓTESIS: El atacante usa PowerShell codificado en base64 para evadir detección (T1059.001).

FUENTES: Sysmon EventID 1 (process creation), proxy logs.

QUERY (concepto):
  process_name = "powershell.exe"
  AND command_line CONTAINS "-enc" OR "-encodedcommand"

RESULTADO ESPERADO: procesos powershell con payload base64 largos.
```

### Técnicas de caza clásicas (empezar por estas)

| Técnica | Hipótesis | Fuente principal |
|---|---|---|
| **Stacking** | Conteos anómalos (ej. 1 host hace 500 consultas DNS) | DNS/proxy |
| **Rare / outlier** | Algo que casi nunca pasa (ej. `whoami` en una estación) | Sysmon |
| **IOC hunt** | Buscar hashes/IPs/dominios conocidos | TI + logs |
| **TTP hunt** | Buscar comportamiento (no IOCs, que rotan) | Sysmon/EDR |

---

## 3. Sigma: detección universal

**Sigma** es un formato **YAML** para describir detecciones de forma agnóstica al SIEM. Una regla Sigma se puede **traducir** a Wazuh, Splunk (SPL), Sentinel (KQL), QRadar, Elastic, etc. con `sigmac` o `pySigma`.

### 3.1 Estructura de una regla Sigma

```yaml
title: PowerShell encoded command execution
id: 4b3a1d7f-1f2e-4c5d-9a1b-000000000001
status: test
description: Detecta PowerShell con comandos codificados en base64 (evasión clásica)
logsource:
  category: process_creation
  product: windows
detection:
  selection:
    Image|endswith: '\powershell.exe'
    CommandLine|contains:
      - '-enc'
      - '-encodedcommand'
  condition: selection
level: high
falsepositives:
  - Scripts legítimos que usan -encodedcommand
tags:
  - attack.execution
  - attack.t1059.001
```

### 3.2 Reglas reales por técnica (kit mínimo SOC)

#### T1003.001 — Dumping de LSASS (credential dumping)

```yaml
title: LSASS memory dump access
logsource:
  category: process_access
  product: windows
detection:
  selection:
    TargetImage|endswith: '\lsass.exe'
    GrantedAccess|contains: '0x1FFFFF'   # acceso total
  condition: selection
level: critical
tags:
  - attack.credential_access
  - attack.t1003.001
```

#### T1053.005 — Scheduled Task como persistencia

```yaml
title: New scheduled task via schtasks
logsource:
  category: process_creation
  product: windows
detection:
  selection:
    Image|endswith: '\schtasks.exe'
    CommandLine|contains: '/create'
  condition: selection
level: medium
tags:
  - attack.persistence
  - attack.execution
  - attack.t1053.005
```

#### T1078 — Login desde IP no habitual (con geolocalización)

```yaml
title: Successful login from new country
logsource:
  category: authentication
  product: windows
detection:
  selection:
    EventID: 4624
    LogonType: 10            # RDP
  filter:
    Country: 'Colombia'      # tu baseline
  condition: selection and not filter
level: high
tags:
  - attack.initial_access
  - attack.t1078
```

### 3.3 Convertir Sigma a tu SIEM

```bash
# Instalar pySigma
pip install pysigma sigma-cli

# Convertir a Splunk (SPL)
sigma convert -t splunk -p sysmon regla.yml

# Convertir a Sentinel (KQL)
sigma convert -t sentinel -p sysmon regla.yml

# Convertir a Wazuh (no hay backend oficial → mapear manualmente a <rule>)
```

> Para Wazuh no existe backend Sigma maduro: traduce **manualmente** la lógica a `<rule>` XML (ver [`../siem-wazuh/README.md`](../siem-wazuh/README.md)).

---

## 4. YARA: firmas de malware y patrones

**YARA** es el estándar para **identificar y clasificar malware** (y patrones de archivos en general) mediante reglas basadas en strings, regex y condiciones.

### 4.1 Estructura de una regla YARA

```yara
rule Deteccion_Ransomware_Generica
{
    meta:
        description = "Detecta notas de rescate y strings típicos"
        author = "0xvanguard"
        date = "2026-08-20"
        tlp = "white"

    strings:
        $nota1 = "your files have been encrypted" nocase wide ascii
        $nota2 = "bitcoin" nocase
        $ext   = ".locked" nocase
        $crypt = "CryptEncrypt" nocase

    condition:
        uint16(0) == 0x5A4D and   // MZ header (PE)
        2 of ($nota*, $crypt)
}
```

### 4.2 Reglas más avanzadas

```yara
rule Suspicious_Powershell_Dropper
{
    meta:
        description = "Script/dropper con descarga y ejecución"

    strings:
        $dl1 = "DownloadString" nocase
        $dl2 = "DownloadFile" nocase
        $ex  = "Invoke-Expression" nocase
        $b64 = /[A-Za-z0-9+\/]{200,}={0,2}/   // base64 largo

    condition:
        2 of ($dl*) and $ex and $b64
}
```

### 4.3 Escanear con YARA

```bash
# Escaneo simple de un archivo
yara regla.yara sospechoso.exe

# Escaneo recursivo de un directorio
yara -r reglas/ /ruta/a/muestras/

# Ver strings que matchearon
yara -s regla.yara muestra.bin
```

### 4.4 Buenas prácticas de reglas YARA

| Práctica | Por qué |
|---|---|
| Usar `nocase` y `wide ascii` | Malware en Unicode/ASCII |
| Anclar con `uint16(0) == 0x5A4D` | Confirmar que es un PE |
| Preferir strings **únicos**, no genéricos | Evitar falsos positivos |
| `tlp` y metadatos | Compartir de forma responsable |
| Probar contra **muestras limpias** | Medir false positive rate |

---

## 5. Pipeline de detection-as-code

El ciclo profesional de una detección (de idea a alerta en producción):

```
1. Investigar técnica (ATT&CK) + generar hipótesis
        ↓
2. Recolectar/validar telemetría disponible (Sysmon, auth, DNS)
        ↓
3. Escribir regla (Sigma/YARA/Wazuh XML)
        ↓
4. Probar contra datos reales (TP) y baseline (FP)
        ↓
5. Versionar en git (detection-as-code) + PR review
        ↓
6. Desplegar al SIEM + medir (alertas vs falsos positivos)
        ↓
7. Iterar: afinar umbrales, añadir exclusiones
```

**Entregable de portafolio:** un repo con 5-10 reglas Sigma + YARA propias, mapeadas a ATT&CK, con su test y su resultado documentado.

---

## 6. Referencias

- [SigmaHQ (repositorio oficial de reglas)](https://github.com/SigmaHQ/sigma)
- [pySigma (conversión)](https://github.com/SigmaHQ/pySigma)
- [YARA Documentation](https://yara.readthedocs.io/)
- [PEAK Threat Hunting Framework (Splunk)](https://www.splunk.com/en_us/blog/security/peak-threat-hunting-framework.html)
- [MITRE ATT&CK](https://attack.mitre.org/)

---

**[⬅ Volver al módulo Blue Team](../README.md)**
