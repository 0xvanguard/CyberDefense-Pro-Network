# 🎯 Módulo 02 — Detection Engineering y Métricas de Detección

> **Nivel:** Avanzado · **Área:** Purple Team
>
> Objetivo: convertir conocimiento ofensivo (ATT&CK) en **detecciones de producción**, y **medir** si de verdad funcionan. Esto es el puente profesional entre Red y Blue.

---

## Índice

1. [Qué es Detection Engineering](#1-qué-es-detection-engineering)
2. [El ciclo de vida de una detección](#2-el-ciclo-de-vida-de-una-detección)
3. [Fuentes de telemetría (qué datos necesitas)](#3-fuentes-de-telemetría-qué-datos-necesitas)
4. [Tipos de detección](#4-tipos-de-detección)
5. [Métricas de detección (medir si sirve)](#5-métricas-de-detección-medir-si-sirve)
6. [Coverage ATT&CK (cobertura)](#6-coverage-attck-cobertura)
7. [Detection-as-code](#7-detection-as-code)
8. [Referencias](#8-referencias)

---

## 1. Qué es Detection Engineering

> *"Una detección que nadie probó y que nadie mide, es una promesa, no una defensa."*

**Detection engineering** es la disciplina de **diseñar, probar, desplegar y mantener** detecciones de seguridad. A diferencia del threat hunting (buscar ad hoc), el detection engineer:

- Convierte una técnica ATT&CK en una **regla reproducible**.
- La **valida** (¿dispara con un ataque real? ¿da falsos positivos?).
- La **mide** (¿cuánto ruido genera? ¿detecta lo que debe?).
- La **mantiene** (ajusta umbrales, exclusiones).

---

## 2. El ciclo de vida de una detección

```
┌────────────────────────────────────────────────────────────┐
│ 1. Requirement   ← ¿Qué amenaza/ técnica queremos detectar? │
│ 2. Data          ← ¿Tenemos la telemetría necesaria?        │
│ 3. Detection     ← Escribir la regla (Sigma/YARA/SIEM)      │
│ 4. Test          ← Validar con emulación (Atomic/CALDERA)   │
│ 5. Deploy        ← Publicar al SIEM/EDR                    │
│ 6. Measure        ← MTTD, FP rate, cobertura               │
│ 7. Tune           ← Ajustar umbrales, exclusiones          │
└────────────────────────────────────────────────────────────┘
```

> La mayoría de equipos solo hace los pasos 1–5 y **nunca mide ni afina**. Ahí se acumula el ruido y muere el SOC.

---

## 3. Fuentes de telemetría (qué datos necesitas)

| Capa | Fuente | Qué te da |
|---|---|---|
| **Endpoint** | Sysmon, EDR (CrowdStrike, S1, Defender) | Procesos, comandos, DLLs, red de host |
| **Red** | Suricata, Zeek, NetFlow | Conexiones, protocolos, payloads |
| **Identidad** | AD/Entra ID, logs de auth | Logins, privilegios, cambios |
| **Aplicación** | WAF, logs web | Ataques web, rutas, payloads |
| **Cloud** | CloudTrail, Azure Activity | Acciones de API, cambios IAM |

> **Regla:** si no tienes la telemetría, **primero habilítala** (ej. Sysmon con buena config), o tu detección será ciega. Ver [`../siem-wazuh`](../../02-SEGURIDAD-INFORMACION/02-blue-team-defensa/siem-wazuh/) para Sysmon/Suricata.

---

## 4. Tipos de detección

| Tipo | Cómo funciona | Pros | Contras |
|---|---|---|---|
| **Signature-based** | Busca un patrón exacto (hash, string, IOC) | Preciso, barato | Se evade fácil (IOC rota) |
| **Behavior-based** | Busca comportamiento (parent/child, flags, secuencia) | Resistente a evasión | Más complejo, más FP |
| **Anomaly-based** | Busca desviación del baseline | Detecta lo desconocido | Ruido, requiere baseline |
| **Correlation** | Une múltiples eventos en una historia | Detecta ataques multi-paso | Complejo de mantener |

> La tendencia profesional: **behavior y correlation** sobre **Sysmon/EDR**, no solo hashes e IOCs.

---

## 5. Métricas de detección (medir si sirve)

Usa la **matriz de confusión** como base:

| | Realmente ataque | Realmente benigno |
|---|---|---|
| **Alerta disparada** | TP (True Positive) | FP (False Positive) |
| **Sin alerta** | FN (False Negative) | TN (True Negative) |

### 5.1 Métricas clave

| Métrica | Fórmula | Qué significa | Meta típica |
|---|---|---|---|
| **Precision (PPV)** | `TP / (TP + FP)` | De las alertas, ¿cuántas eran reales? | > 70% |
| **Recall / Sensitivity** | `TP / (TP + FN)` | De los ataques, ¿cuántos detecté? | > 80% |
| **False Positive Rate** | `FP / (FP + TN)` | Ruido generado | < 1% |
| **MTTD** (Mean Time To Detect) | tiempo medio desde compromiso a detección | Velocidad de detección | minutos/horas |
| **MTTR** (Mean Time To Respond) | tiempo medio de detección a contención | Velocidad de respuesta | horas |

### 5.2 Ejemplo práctico

Una regla de fuerza bruta disparó 100 alertas en una semana:

```
TP = 70 (fuerzas brutas reales)
FP = 30 (usuarios que olvidaron su password)
FN = 10 (fuerzas brutas no detectadas)

Precision = 70 / (70+30) = 70%
Recall    = 70 / (70+10) = 87.5%
```

→ La regla es buena en recall pero genera 30% de ruido. **Acción:** subir el umbral (de 5 a 10 intentos) y excluir IPs internas conocidas.

### 5.3 El trade-off fundamental

```
Subir umbral (más estricto)  →  menos FP (más precision), pero más FN (menos recall)
Bajar umbral (más sensible)  →  más TP (más recall), pero más FP (menos precision)
```

No hay detección perfecta: **eliges** el punto de operación según tu tolerancia al ruido.

---

## 6. Coverage ATT&CK (cobertura)

La cobertura responde: **¿qué porcentaje de técnicas ATT&CK tenemos cubierto por al menos una detección?**

### 6.1 Método

1. Toma las técnicas relevantes para tu organización (no todas las ~200).
2. Marca por cada técnica: `detectada` / `parcial` / `no detectada`.
3. Usa **ATT&CK Navigator** para visualizarlo.

```bash
# ATT&CK Navigator (web): https://mitre-attack.github.io/attack-navigator/
# Exporta tu layer JSON y guárdalo versionado en el repo
```

### 6.2 Tabla de cobertura (plantilla)

| Técnica | Detección | Fuente | Estado | Cobertura |
|---|---|---|---|---|
| T1059.001 PowerShell | Regla Sigma `powershell_encoded` | Sysmon EID 1 | Activa | ✅ |
| T1110 Brute Force | Regla Wazuh `100101` | auth.log | Activa | ✅ |
| T1003.001 LSASS dump | Regla Sigma `lsass_access` | Sysmon EID 10 | En test | 🟡 |
| T1547 Registry Run | — | — | Sin cobertura | ❌ |

> **Métrica:** `cobertura = técnicas detectadas / técnicas relevantes`. Meta inicial: cubrir el **ATT&CK Top 10** de técnicas más usadas.

---

## 7. Detection-as-code

Las detecciones deben tratarse como **código**: versionadas, revisadas y desplegadas con CI/CD.

```text
reglas/
├── sigma/
│   ├── windows/
│   │   └── powershell_encoded.yml
│   └── linux/
├── wazuh/
│   └── local_rules.xml
├── yara/
│   └── ransomware.yar
└── tests/
    └── atomic_test_cases.md
```

Workflow:

```bash
# 1. Escribir regla en git
# 2. PR review (otro analista valida lógica y umbrales)
# 3. CI valida sintaxis (pySigma, yara -c)
# 4. Deploy al SIEM
# 5. Medir (sección 5) y documentar
```

**Entregable de portafolio:** repo de detecciones versionado + tabla de cobertura ATT&CK + métricas de al menos 3 reglas (precision/recall).

---

## 8. Referencias

- [MITRE ATT&CK Navigator](https://mitre-attack.github.io/attack-navigator/)
- [SigmaHQ](https://github.com/SigmaHQ/sigma)
- [Atomic Red Team (para validar detecciones)](https://github.com/redcanaryco/atomic-red-team) → ver [`../03-adversary-emulation`](../03-adversary-emulation/)
- [Detection Engineering (libro de referencia)](https://www.detectionengineering.net/)

---

**[⬅ Volver al README de Purple Team](../README.md)** · **[→ Adversary Emulation](../03-adversary-emulation/)**
