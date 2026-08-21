---
title: "Módulo 05 — Breach & Attack Simulation (BAS)"
---

# 🎯 Módulo 05 — Breach & Attack Simulation (BAS)

> **Objetivo Principal:** Usar herramientas de Breach and Attack Simulation para validar automáticamente las defensas contra técnicas del MITRE ATT&CK.

[![Nivel](https://img.shields.io/badge/Nivel-Avanzado-red?style=flat-square)]()
[![Duración](https://img.shields.io/badge/Duración-2%20meses-blue?style=flat-square)]()

---

## 📋 Resumen del módulo

| Atributo | Detalle |
|----------|---------|
| **Pre-requisitos** | Módulos 01-04 completados |
| **Herramientas** | Atomic Red Team, MITRE CALDERA, Infection Monkey |
| **Entregable** | Reporte de brechas de detección |
| **Nivel** | Avanzado |

---

## 1. 🧠 Teoría: Breach & Attack Simulation

BAS permite **ejecutar simulaciones controladas** de ataques para validar que las defensas funcionan correctamente.

### Ciclo de BAS

```
┌─────────────────────────────────────────────────────┐
│              CICLO DE BAS                             │
├─────────────┬──────────────┬────────────┬───────────┤
│  1. Planificar│ 2. Ejecutar  │ 3. Medir   │ 4. Mejorar│
│  escenarios  │ ataques      │ cobertura  │ defensas  │
└──────────────┴──────────────┴────────────┴───────────┘
```

### Herramientas BAS

| Herramienta | Tipo | Costo |
|-------------|------|-------|
| **Atomic Red Team** | Open Source | Gratis |
| **MITRE CALDERA** | Open Source | Gratis |
| **Infection Monkey** | Open Source | Gratis |
| **SafeBreach** | Comercial | $$$ |
| **AttackIQ** | Comercial | $$$ |

---

## 2. 🛠️ Atomic Red Team

### Instalación

```bash
# Clonar repositorio
git clone https://github.com/redcanaryco/atomic-red-team.git
cd atomic-red-team

# Instalar dependencias
pip install -r requirements.txt

# Ejecutar test específico
Invoke-AtomicRedTeam -TestIDs T1003.001
```

### Ejemplo: Credential Dumping (T1003.001)

```yaml
# atomic-red-team/atomics/T1003.001/T1003.001.yaml
attack_technique: T1003.001
display_name: "OS Credential Dumping: LSASS Memory"

atomic_tests:
- name: Dump LSASS with comsvcs.dll
  supported_platforms:
  - windows
  executor:
    name: command_prompt
    elevation_required: true
    command: rundll32.exe C:\Windows\System32\comsvcs.dll, MiniDump (Get-Process lsass).Id C:\temp\lsass.dmp
```

---

## 3. 🔬 Práctica Guiada: Ejecutar BAS

### Escenario: Validar defensas contra TTPs comunes

#### Paso 1: Ejecutar tests de Atomic Red Team

```bash
# Ejecutar tests de ejecución (Execution)
Invoke-AtomicRedTeam -TestIDs T1059.001  # PowerShell
Invoke-AtomicRedTeam -TestIDs T1059.003  # Windows Command Shell

# Ejecutar tests de persistencia
Invoke-AtomicRedTeam -TestIDs T1547.001  # Registry Run Keys

# Ejecutar tests de elevación de privilegios
Invoke-AtomicRedTeam -T1548.002  # Bypass UAC
```

#### Paso 2: Medir detección

```bash
# Verificar en SIEM/Wazuh si se generaron alertas
# Para cada test, documentar:
# - ¿Se detectó? (Sí/No)
# - ¿En cuánto tiempo? (MTTD)
# - ¿Qué herramienta detectó? (EDR/SIEM/Manual)
```

#### Paso 3: Análisis de brechas

```markdown
## Reporte de Brechas de Detección

| Técnica | Descripción | Detectado | MTTD | Herramienta |
|---------|-------------|-----------|------|-------------|
| T1059.001 | PowerShell Execution | ✅ Sí | 2 min | Wazuh |
| T1547.001 | Registry Run Keys | ✅ Sí | 5 min | Sysmon |
| T1003.001 | LSASS Dump | ❌ No | - | - |
| T1021.001 | RDP | ✅ Sí | 1 min | Network SIEM |
```

---

## 4. 📊 Métricas de BAS

| Métrica | Descripción | Objetivo |
|---------|-------------|----------|
| **Cobertura ATT&CK** | % de técnicas con test | > 50% |
| **Tasa de detección** | % de tests detectados | > 80% |
| **MTTD promedio** | Tiempo promedio de detección | < 10 min |
| **Brechas identificadas** | Técnicas no detectadas | Documentar todas |

---

## 5. 🎯 Mini-Entregable

**Tarea:** Ejecutar un ejercicio BAS que incluya:

1. **Planificación** de 5-10 técnicas ATT&CK a testear
2. **Ejecución** de tests con Atomic Red Team o CALDERA
3. **Medición** de detección (¿qué se detectó?)
4. **Reporte** de brechas con recomendaciones

---

## 6. 🔗 Recursos Adicionales

- [Atomic Red Team](https://github.com/redcanaryco/atomic-red-team)
- [MITRE CALDERA](https://github.com/mitre/caldera)
- [Infection Monkey](https://github.com/guardicore/monkey)

---

> **Siguiente paso:** Continúa con el [Módulo 06 — Automated Compliance Testing](../purple-team/06-automated-compliance) para aprender a automatizar pruebas de cumplimiento.
