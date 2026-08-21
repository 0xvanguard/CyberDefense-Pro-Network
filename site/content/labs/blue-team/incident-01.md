---
title: "🚨 Lab incident-01: Incident Response"
description: "🚨 Lab incident-01: Incident Response"
---

# 🚨 Lab incident-01: Incident Response

> Responde a incidentes de seguridad reales: desde la detección hasta la recuperación completa.

## 🎯 Objetivos de Aprendizaje

Al completar este lab podrás:

- [ ] Seguir el marco NIST SP 800-61 para respuesta a incidentes
- [ ] Clasificar incidentes por severidad y tipo
- [ ] Ejecutar procedimientos de contención
- [ ] Recopilar y preservar evidencia digital
- [ ] Erradicar amenazas y recuperar servicios
- [ ] Documentar incidentes profesionalmente

## ⏱️ Información del Lab

| Campo | Valor |
|-------|-------|
| **Dificultad** | 🟡 Intermedio |
| **Tiempo estimado** | 120 minutos |
| **XP en juego** | 500 puntos |
| **Herramientas** | volatility, autopsy, yara, custom scripts |
| **Flags** | 10 |

## 📋 Ejercicios

### Ejercicio 1: Clasificación de Incidentes (50 XP)

Clasifica los siguientes escenarios por severidad:

| Escenario | Severidad | Tipo |
|-----------|-----------|------|
| Brute force SSH exitoso | `[___]` | `[___]` |
| Malware detectado en PC de usuario | `[___]` | `[___]` |
| DDoS contra servidor web | `[___]` | `[___]` |
| Datos exfiltrados a IP externa | `[___]` | `[___]` |
| Phishing con credenciales comprometidas | `[___]` | `[___]` |

---

### Ejercicio 2: Contención (80 XP)

Ejecuta procedimientos de contención:

```bash
# 1. Aislar host comprometido
iptables -A INPUT -s 10.0.2.50 -j DROP
iptables -A OUTPUT -s 10.0.2.50 -j DROP

# 2. Bloquear IP atacante
iptables -A INPUT -s 185.x.x.x -j DROP

# 3. Deshabilitar cuenta comprometida
passwd -l usuario_comprometido

# 4. Reducir superficie de ataque
# Deshabilitar servicios innecesarios
systemctl stop cups
systemctl disable cups
```

**Flag:** `[___]`

---

### Ejercicio 3: Recolección de Evidencia (80 XP)

Recopila evidencia digital de forma forense:

```bash
# 1. Capturar tráfico de red
tcpdump -i eth0 -w evidence_$(date +%Y%m%d_%H%M%S).pcap

# 2. Capturar memoria (si LiME disponible)
insmod lime.ko "path=/tmp/memdump.lime format=lime"

# 3. Adquirir disco
dd if=/dev/sda of=/evidence/disk_image.dd bs=4M

# 4. Hash de evidencia
sha256sum evidence.pcap > evidence.pcap.sha256

# 5. Documentar cadena de custodia
cat > chain_of_custody.md << 'EOF'
# Cadena de Custodia

## Evidencia #001
- Tipo: Captura de red
- Archivo: evidence_20240101_143022.pcap
- Hash SHA256: [hash]
- Recopilado por: [Nombre]
- Fecha: [Fecha]
- Almacenamiento: /evidence/
EOF
```

**Flag:** `[___]`

---

### Ejercicio 4: Erradicación (80 XP)

Elimina la amenaza del sistema:

```bash
# 1. Identificar malware
yara -r /path/to/rules/ /tmp/suspicious/

# 2. Eliminar archivos maliciosos
rm -f /tmp/backdoor
rm -f /var/www/html/shell.php

# 3. Limpiar persistencia
crontab -r
rm -f /etc/systemd/system/backdoor.service

# 4. Restaurar configuración
cp /backup/config.conf /etc/app/config.conf

# 5. Actualizar sistema
apt update && apt upgrade -y
```

**Flag:** `[___]`

---

### Ejercicio 5: Recuperación (60 XP)

Restaura servicios a estado normal:

```bash
# 1. Restaurar de backup
rsync -avz /backup/ /var/www/html/

# 2. Verificar integridad
sha256sum -c checksums.sha256

# 3. Monitorear actividad
tail -f /var/log/auth.log
tail -f /var/log/syslog

# 4. Verificar servicios
systemctl status apache2
systemctl status mysql

# 5. Pruebas de funcionalidad
curl -I http://localhost
```

**Flag:** `[___]`

---

### Ejercicio 6: Documentación (60 XP)

Crea reporte completo del incidente:

```markdown
# Reporte de Incidente #IR-2024-001

## Resumen Ejecutivo
- Fecha: [Fecha]
- Severidad: [HIGH]
- Tipo: [Malware]
- Estado: [Resuelto]

## Timeline
| Hora | Evento |
|------|--------|
| 14:30 | Alerta de antivirus |
| 14:35 | Investigación inicial |
| 14:45 | Contención ejecutada |
| 15:00 | Evidencia recopilada |
| 15:30 | Erradicación completada |
| 16:00 | Servicios restaurados |

## Análisis
- Vector de ataque: [Phishing email]
- Malware: [Trojan.GenericKD]
- Impacto: [1 workstation affected]

## Acciones Tomadas
1. Host aislado de red
2. Evidencia preservada
3. Malware eliminado
4. Sistema restaurado
5. Usuario notificado

## Lecciones Aprendidas
1. [Lección 1]
2. [Lección 2]
3. [Lección 3]

## Recomendaciones
1. [Recomendación 1]
2. [Recomendación 2]
```

**Flag:** `[___]`

---

### Ejercicio 7: Post-Incidente (50 XP)

Implementa mejoras después del incidente:

```bash
# 1. Actualizar reglas de detección
# Agregar IOC a SIEM
# Crear regla de alerta

# 2. Mejorar controles
# Implementar MFA
# Actualizar políticas
# Capacitar usuarios

# 3. Verificar efectividad
# Simular ataque similar
# Verificar que se detecta
# Documentar mejoras
```

**Flag:** `[___]`

---

### Ejercicio 8: Lessons Learned (50 XP)

Conducta post-incidente:

```markdown
# Lessons Learned Meeting

## Participantes
- [Lista de participantes]

## Discusión
### ¿Qué salió bien?
1. [Punto 1]
2. [Punto 2]

### ¿Qué mejoró?
1. [Punto 1]
2. [Punto 2]

### Acciones Correctivas
| # | Acción | Responsable | Fecha |
|---|--------|-------------|-------|
| 1 | [Acción] | [Nombre] | [Fecha] |
| 2 | [Acción] | [Nombre] | [Fecha] |

## Métricas
- Tiempo de detección: [X] min
- Tiempo de contención: [X] min
- Tiempo de recuperación: [X] min
- Costo estimado: $[X]
```

**Flag:** `[___]`

---

### Ejercicio 9: Forensics Básico (60 XP)

Analiza evidencia digital:

```bash
# 1. Analizar captura de red
tcpdump -r evidence.pcap -A | grep -i "password\|flag\|secret"

# 2. Analizar memoria con Volatility
volatility -f memory.dmp imageinfo
volatility -f memory.dmp --profile=Win7SP1x64 pslist
volatility -f memory.dmp --profile=Win7SP1x64 filescan

# 3. Buscar artefactos
# Archivos recientes
find / -mtime -1 -type f 2>/dev/null

# Procesos sospechosos
ps auxf | grep -v "\[" | grep -v "ps auxf"

# Conexiones activas
netstat -tulnp
```

**Flag:** `[___]`

---

### Ejercicio 10: Reporte Final (60 XP)

Genera reporte ejecutivo:

```markdown
# Reporte Ejecutivo - Incidente #IR-2024-001

## Para Dirección General

### Resumen
Un incidente de seguridad afectó nuestra infraestructura el [Fecha]. El equipo de seguridad detectó, contuvo y erradicó la amenaza en [X] horas.

### Impacto
- Servicios afectados: [X]
- Usuarios impactados: [X]
- Datos comprometidos: [Ninguno/Parcial/Total]
- Pérdida financiera estimada: $[X]

### Respuesta
- Tiempo de detección: [X] minutos
- Tiempo de contención: [X] minutos
- Tiempo de recuperación: [X] minutos

### Mejoras Implementadas
1. [Mejora 1]
2. [Mejora 2]
3. [Mejora 3]

### Inversión Requerida
- Tecnología: $[X]
- Personal: $[X]
- Capacitación: $[X]

### Próximos Pasos
1. [Paso 1]
2. [Paso 2]
3. [Paso 3]
```

**Flag:** `[___]`

## 🏁 Validación

```bash
./scripts/validate.sh
```

## 📝 Criterios de Éxito

| Ejercicio | Criterio | Puntos | Estado |
|-----------|----------|--------|--------|
| 1 | Clasificación correcta | 50 | ⬜ |
| 2 | Contención ejecutada | 80 | ⬜ |
| 3 | Evidencia recopilada | 80 | ⬜ |
| 4 | Amenaza erradicada | 80 | ⬜ |
| 5 | Servicios restaurados | 60 | ⬜ |
| 6 | Documentación completa | 60 | ⬜ |
| 7 | Mejoras implementadas | 50 | ⬜ |
| 8 | Lessons learned | 50 | ⬜ |
| 9 | Forensics ejecutado | 60 | ⬜ |
| 10 | Reporte final | 60 | ⬜ |
| **Total** | | **500** | ⬜ |

---

*Lab creado para CyberDefense Labs — Nivel Intermedio*
