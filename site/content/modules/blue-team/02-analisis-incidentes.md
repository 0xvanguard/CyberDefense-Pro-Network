---
title: "Módulo 02 — Análisis de Incidentes y Respuesta"
---

# 🚨 Módulo 02 — Análisis de Incidentes y Respuesta

> **Objetivo Principal:** Aprender a detectar, analizar, contener y recuperar sistemas comprometidos siguiendo metodología profesional de Incident Response (NIST SP 800-61).

[![Nivel](https://img.shields.io/badge/Nivel-Intermedio-orange?style=flat-square)]()
[![Duración](https://img.shields.io/badge/Duración-2%20meses-blue?style=flat-square)]()

---

## 📋 Resumen del módulo

| Atributo | Detalle |
|----------|---------|
| **Pre-requisitos** | Módulo 01 completado |
| **Herramientas** | Volatility, Autopsy, YARA, Sigma, TheHive |
| **Entregable** | Reporte de incidente completo |
| **Nivel** | Intermedio |

---

## 1. 🧠 Teoría: Ciclo de Vida de un Incidente

### Fases según NIST SP 800-61

```
┌─────────────────────────────────────────────────────┐
│              CICLO DE INCIDENT RESPONSE               │
├─────────────┬──────────────┬────────────┬───────────┤
│  1. Preparación │ 2. Detección  │ 3. Contención│ 4. Erradicación│
│  y Análisis     │ y Análisis    │              │                │
├───────────────┼──────────────┼──────────────┼───────────────┤
│ 5. Recuperación│ 6. Lecciones  │              │               │
│                │ Aprendidas    │              │               │
└────────────────┴───────────────┴──────────────┴───────────────┘
```

### Tipos de incidentes comunes

| Tipo | Ejemplo | Impacto |
|------|---------|---------|
| **Malware** | Ransomware, Troyano | Alto |
| **Phishing** | Email con payload | Medio-Alto |
| **Compromiso de credenciales** | Credential stuffing | Alto |
| **Data breach** | Exfiltración de datos | Crítico |
| **DoS/DDoS** | Ataque de denegación | Medio |
| **Insider threat** | Empleado malicioso | Crítico |

---

## 2. 🛠️ Herramientas del Oficio

### Herramientas de Análisis Forense

| Herramienta | Uso | Nivel |
|-------------|-----|-------|
| **Volatility 3** | Análisis de memoria RAM | Avanzado |
| **Autopsy** | Forense de disco | Intermedio |
| **YARA** | Detección de malware por patrones | Intermedio |
| **Sigma** | Reglas de detección para SIEM | Intermedio |
| **TheHive** | Gestión de incidentes | Intermedio |

---

## 3. 🔬 Práctica Guiada (Laboratorio)

### Escenario: Detección de Ransomware

**Objetivo:** Analizar un sistema comprometido por ransomware y generar un reporte de incidente completo.

#### Paso 1: Identificación del Incidente

```bash
# Revisar procesos sospechosos
ps aux | grep -i suspicious

# Revisar conexiones de red activas
netstat -tlnp | grep ESTABLISHED

# Revisar archivos modificados recientemente
find / -mtime -1 -type f 2>/dev/null | head -50
```

#### Paso 2: Contención

```bash
# aislar la máquina de la red
iptables -A INPUT -j DROP
iptables -A OUTPUT -j DROP

# preserves evidence
dd if=/dev/sda of=/external/evidence/disk_image.dd bs=4M
```

#### Paso 3: Análisis con YARA

```bash
# Crear regla YARA para detectar ransomware
cat > ransomware_rule.yar << 'EOF'
rule Ransomware_Indicator {
    meta:
        description = "Detects common ransomware behavior"
    strings:
        $s1 = "decrypt" ascii
        $s2 = "bitcoin" ascii
        $s3 = ".encrypted" ascii
        $s4 = "README.txt" ascii
    condition:
        2 of ($s*)
}
EOF

# Escanear directorios
yara ransomware_rule.yar /suspicious/directory/
```

#### Paso 4: Análisis de Memoria con Volatility

```bash
# Listar procesos
volatility -f memory.dump --profile=Win10x64 pslist

# Detectar inyección de código
volatility -f memory.dump --profile=Win10x64 malfind

# Ver conexiones de red
volatility -f memory.dump --profile=Win10x64 netscan
```

---

## 4. 📊 Clasificación de Incidentes

### Matriz de Severidad

| Severidad | Descripción | Tiempo de respuesta |
|-----------|-------------|---------------------|
| **P1 - Crítico** | Ransomware activo, data breach | < 1 hora |
| **P2 - Alto** | Compromiso de servidor | < 4 horas |
| **P3 - Medio** | Malware en estación | < 24 horas |
| **P4 - Bajo** | Phishing bloqueado | < 72 horas |

---

## 5. 📝 Reporte de Incidente (Plantilla)

```markdown
# Reporte de Incidente #001

## Resumen Ejecutivo
- **Fecha de detección:** 2024-01-15
- **Severidad:** P2 - Alto
- **Estado:** Resuelto

## Timeline del Incidente
| Hora | Evento |
|------|--------|
| 09:00 | Alerta de SIEM: proceso sospechoso |
| 09:15 | Confirmación de malware |
| 09:30 | Contención: aislamiento de red |
| 10:00 | Análisis forense completo |
| 12:00 | Erradicación y recuperación |

## Hallazgos
- Malware identificado: Emotet variant
- Vector de entrada: Phishing email
- Sistemas afectados: 3 estaciones de trabajo

## Recomendaciones
1. Implementar sandboxing de emails
2. Actualizar políticas de whitelist
3. Capacitación de usuarios
```

---

## 6. 🎯 Mini-Entregable

**Tarea:** Analizar el escenario proporcionado y crear un reporte de incidente que incluya:

1. **Clasificación** del incidente (tipo y severidad)
2. **Timeline** de eventos
3. **Hallazgos técnicos** (con evidencia)
4. **Acciones de contención** tomadas
5. **Recomendaciones** de remediación

---

## 7. 🔗 Recursos Adicionales

- [NIST SP 800-61 - Computer Security Incident Handling Guide](https://csrc.nist.gov/publications/detail/sp/800-61/rev-2/final)
- [SANS Incident Response Poster](https://www.sans.org/white-papers/incident-response/)
- [TheHive Project](https://thehive-project.org/)

---

> **Siguiente paso:** Continúa con el [Módulo 03 — Threat Hunting](../blue-team/03-threat-hunting) para aprender a buscar amenazas proactivamente.
