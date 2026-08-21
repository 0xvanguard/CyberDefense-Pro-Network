---
title: "🔍 Lab detection-01: Detection Engineering"
description: "🔍 Lab detection-01: Detection Engineering"
---

# 🔍 Lab detection-01: Detection Engineering

> Diseña, implementa y valida reglas de detección para identificar amenazas en tu entorno.

## 🎯 Objetivos de Aprendizaje

Al completar este lab podrás:

- [ ] Crear reglas de detección con Sigma
- [ ] Implementar reglas en Wazuh SIEM
- [ ] Validar efectividad de detecciones
- [ ] Optimizar reglas para reducir falsos positivos
- [ ] Documentar cobertura de detección

## ⏱️ Información del Lab

| Campo | Valor |
|-------|-------|
| **Dificultad** | 🟡 Intermedio |
| **Tiempo estimado** | 75 minutos |
| **XP en juego** | 400 puntos |
| **Herramientas** | Sigma, Wazuh, YARA, custom scripts |
| **Flags** | 6 |

## 🚀 Inicio Rápido

```bash
# Levantar el entorno
cd labs/purple-team/detection-01/
docker compose up -d

# Verificar servicios
docker compose ps
```

## 📋 Ejercicios

### Ejercicio 1: Crear Reglas Sigma (60 XP)

Diseña reglas de detección:

```yaml
# Brute Force Detection
title: Brute Force Authentication Attempt
id: 12345678-1234-1234-1234-123456789012
status: experimental
description: Detects multiple failed authentication attempts
references:
  - https://attack.mitre.org/techniques/T1110/
author: Purple Team Lab
date: 2024/01/15
tags:
  - attack.credential_access
  - attack.t1110
logsource:
  product: linux
  service: sshd
detection:
  selection:
    event_type: authentication
    status: failed
  condition: selection
level: medium
falsepositives:
  - Legitimate user typos

---
# PowerShell Execution Detection
title: Suspicious PowerShell Execution
id: 12345678-1234-1234-1234-123456789013
status: experimental
description: Detects suspicious PowerShell commands
author: Purple Team Lab
date: 2024/01/15
tags:
  - attack.execution
  - attack.t1059
logsource:
  category: process_creation
  product: windows
detection:
  selection:
    Image|endswith: '\powershell.exe'
    CommandLine|contains:
      - 'IEX'
      - 'Invoke-Expression'
      - 'DownloadString'
      - 'Net.WebClient'
  condition: selection
level: high
```

**Flag:** `[___]`

---

### Ejercicio 2: Implementar en Wazuh (60 XP)

Implementa reglas en el SIEM:

```bash
# 1. Copiar reglas a Wazuh
cp custom_rules.xml /var/ossec/etc/rules/

# 2. Reiniciar Wazuh
systemctl restart wazuh-manager

# 3. Verificar reglas cargadas
curl -k -u admin:admin https://localhost:55000/rules | jq '.data.items[] | select(.id == 100001)'

# 4. Probar regla
# Generar evento que active la regla
ssh admin@10.0.2.20 "invalid_command"

# 5. Verificar alerta
tail -f /var/ossec/logs/alerts/alerts.log | grep "100001"
```

**Flag:** `[___]`

---

### Ejercicio 3: Validar Detecciones (60 XP)

Valida efectividad de reglas:

```bash
# 1. Ejecutar técnica que debería detectarse
# Brute force SSH
for i in {1..10}; do
  sshpass -p "wrong" ssh admin@10.0.2.20 2>/dev/null
done

# 2. Verificar si se generó alerta
curl -k -u admin:admin https://localhost:55000/alerts | jq '.data.items[] | select(.rule.id == 100001)'

# 3. Medir MTTD
# Timestamp del ataque vs timestamp de alerta

# 4. Documentar resultados
cat > validation_report.md << 'EOF'
# Detection Validation Report

## Rule: Brute Force Detection
- Test: 10 failed SSH attempts
- Expected: Alert generated
- Actual: Alert generated
- MTTD: 2 minutes
- Status: PASS

## Rule: PowerShell Suspicious
- Test: IEX command execution
- Expected: Alert generated
- Actual: Alert generated
- MTTD: 5 minutes
- Status: PASS
EOF
```

**Flag:** `[___]`

---

### Ejercicio 4: Optimizar Reglas (60 XP)

Reduce falsos positivos:

```yaml
# Regla optimizada con whitelist
title: Brute Force Authentication Attempt (Optimized)
id: 12345678-1234-1234-1234-123456789012
status: stable
detection:
  selection:
    event_type: authentication
    status: failed
  filter:
    user|contains:
      - 'test'
      - 'scanner'
  condition: selection and not filter
level: medium
```

**Flag:** `[___]`

---

### Ejercicio 5: Cobertura ATT&CK (60 XP)

Mapea cobertura de detección:

```yaml
# coverage_map.yml
coverage:
  initial_access:
    - T1566 Phishing: 80%
    - T1190 Exploit Public-Facing: 70%
  
  execution:
    - T1059 PowerShell: 90%
    - T1053 Scheduled Task: 85%
  
  persistence:
    - T1547 Autostart: 60%
    - T1053 Scheduled Task: 85%
  
  privilege_escalation:
    - T1548 UAC Bypass: 50%
    - T1068 Exploitation: 40%
  
  credential_access:
    - T1003 Credential Dumping: 75%
    - T1558 Kerberoasting: 65%

overall_coverage: 72%
gaps:
  - "UAC Bypass detection"
  - "Kernel exploitation detection"
```

**Flag:** `[___]`

---

### Ejercicio 6: Reporte Final (100 XP)

Genera reporte de detección:

```markdown
# Detection Engineering Report

## Resumen
- Reglas creadas: 5
- Cobertura ATT&CK: 72%
- Falsos positivos: 2%
- MTTD promedio: 3.5 min

## Reglas Implementadas
| # | Regla | Cobertura | MTTD |
|---|-------|-----------|------|
| 1 | Brute Force SSH | 90% | 2 min |
| 2 | PowerShell Suspicious | 85% | 5 min |
| 3 | Scheduled Task | 80% | 3 min |
| 4 | Registry Modification | 70% | 4 min |
| 5 | Network Connection | 75% | 3 min |

## Gaps Identificados
1. UAC Bypass - 50% cobertura
2. Kernel Exploitation - 40% cobertura

## Recomendaciones
1. Agregar detección de UAC bypass
2. Implementar monitoreo de kernel
3. Optimizar reglas existentes

## Próximos Pasos
1. [Acción 1]
2. [Acción 2]
3. [Acción 3]
```

**Flag:** `[___]`

## 🏁 Validación

```bash
./scripts/validate.sh
```

## 📝 Criterios de Éxito

| Ejercicio | Criterio | Puntos | Estado |
|-----------|----------|--------|--------|
| 1 | Reglas Sigma creadas | 60 | ⬜ |
| 2 | Reglas implementadas | 60 | ⬜ |
| 3 | Detecciones validadas | 60 | ⬜ |
| 4 | Reglas optimizadas | 60 | ⬜ |
| 5 | Cobertura mapeada | 60 | ⬜ |
| 6 | Reporte generado | 100 | ⬜ |
| **Total** | | **400** | ⬜ |

---

*Lab creado para CyberDefense Labs — Nivel Intermedio*
