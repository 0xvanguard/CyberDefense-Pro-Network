---
title: "Módulo 03 — SOC Operations"
---

# 🚨 Módulo 03 — SOC Operations

> **Objetivo:** Operar un Security Operations Center con procesos repetibles, métricas y mejora continua.

[![Nivel](https://img.shields.io/badge/Nivel-Intermedio--Avanzado-orange?style=flat-square)]()
[![Duración](https://img.shields.io/badge/Duración-2%20meses-blue?style=flat-square)]()

---

## 📋 Resumen del módulo

| Atributo | Detalle |
|----------|---------|
| **Pre-requisitos** | Módulo 02 completado |
| **Procesos** | NIST 800-61, ITIL |
| **Herramientas** | TheHive, Cortex, Shuffle |
| **Nivel** | Intermedio-Avanzado |

---

## 1. 🧠 Teoría: Estructura de un SOC

### Modelo de tiers

```
┌─────────────────────────────────────────────────────┐
│                    SOC TIERS                          │
├─────────────────────────────────────────────────────┤
│  Tier 1 — Triage                                      │
│  - Monitoreo 24/7                                     │
│  - Alertas iniciales                                  │
│  - Escalado a Tier 2                                  │
├─────────────────────────────────────────────────────┤
│  Tier 2 — Investigación                               │
│  - Análisis profundo                                  │
│  - Contención                                         │
│  - Análisis forense básico                            │
├─────────────────────────────────────────────────────┤
│  Tier 3 — Avanzado                                    │
│  - Threat Hunting                                     │
│  - Análisis de malware                                │
│  - Forense avanzado                                   │
│  - Respuesta a incidentes complejos                   │
└─────────────────────────────────────────────────────┘
```

---

## 2. 📋 Playbooks de respuesta

### Playbook: Ransomware

```markdown
## Playbook: Ransomware

### Fase 1: Detección (0-15 min)
1. [ ] Alerta de SIEM/EDR confirmada
2. [ ] Identificar sistema afectado
3. [ ] Determinar alcance (¿cuántos sistemas?)
4. [ ] Escalar a Tier 2/3

### Fase 2: Contención (15-60 min)
1. [ ] Aislar sistema de la red (no apagar)
2. [ ] Bloquear IP/dominio del C2
3. [ ] Deshabilitar cuentas comprometidas
4. [ ] Notificar al equipo de respuesta

### Fase 3: Erradicación (1-24 horas)
1. [ ] Identificar vector de entrada
2. [ ] Eliminar malware
3. [ ] Parchear vulnerabilidad explotada
4. [ ] Cambiar credenciales comprometidas

### Fase 4: Recuperación (24-72 horas)
1. [ ] Restaurar desde backups verificados
2. [ ] Verificar integridad de sistemas
3. [ ] Monitoreo intensivo post-recuperación
4. [ ] Documentar lecciones aprendidas
```

---

## 3. 📊 Métricas SOC

| Métrica | Fórmula | Objetivo |
|---------|---------|----------|
| **MTTD** | Tiempo promedio de detección | < 30 min |
| **MTTR** | Tiempo promedio de respuesta | < 4 horas |
| **MTTC** | Tiempo promedio de contención | < 1 hora |
| **Tasa de falsos positivos** | FP / (FP + TN) | < 5% |
| **Cobertura ATT&CK** | Técnicas detectadas / Total | > 60% |
| **Tickets por analista** | Total tickets / Analistas | Benchmark |

---

## 4. 🔧 Herramientas SOC

### TheHive — Gestión de incidentes

```bash
# Instalar con Docker
docker run -d --name thehive \
  -p 9000:9000 \
  -v /path/to/data:/opt/thp/thehive/database \
  thehiveproject/thehive4:latest
```

### Cortex — Análisis automatizado

```bash
# Conecta con TheHive para analizar observables
# Analyzers: VirusTotal, AbuseIPDB, Shodan
# Responders: MISP, Slack, Email
```

### Shuffle — SOAR ligero

```bash
# Automatización de playbooks
docker run -d -p 3001:3001 --name shuffle \
  ghcr.io/shuffle/shuffle-backend:latest
```

---

## 5. ✏️ Ejercicios prácticos

### Ejercicio 1: Crear playbook (30 min)

1. Elige un escenario (ransomware, phishing, DDoS)
2. Escribe un playbook paso a paso
3. Incluye checklists para cada fase
4. Define roles y responsabilidades

### Ejercicio 2: Configurar TheHive (40 min)

1. Instala TheHive con Docker
2. Crea un caso de prueba
3. Registra observables (IP, hash, email)
4. Asigna tareas al equipo

### Ejercicio 3: Medir métricas (20 min)

1. Define 5 métricas para tu SOC
2. Crea un dashboard simple (Excel o dashboard SIEM)
3. Establece objetivos para cada métrica

---

> **Siguiente:** [Módulo 04 — DevSecOps](./04-devsecops)
