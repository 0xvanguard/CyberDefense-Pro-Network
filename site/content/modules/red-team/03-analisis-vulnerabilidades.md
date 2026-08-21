---
title: � Módulo 03 — Análisis de Vulnerabilidades
description: � Módulo 03 — Análisis de Vulnerabilidades
---

# 🧠 Módulo 03 — Análisis de Vulnerabilidades

> **Objetivo Principal:** Identificar, priorizar, validar y comunicar vulnerabilidades de forma profesional usando la tríada CIA, el ciclo de gestión de vulnerabilidades y un enfoque operativo combinado de **Red Team, Blue Team y Purple Team**.

[![Nivel](https://img.shields.io/badge/Nivel-Intermedio%20→%20Avanzado-red?style=flat-square)]()
[![Enfoque](https://img.shields.io/badge/Enfoque-Red%20%7C%20Blue%20%7C%20Purple-purple?style=flat-square)]()
[![Modelo](https://img.shields.io/badge/Modelo-CIA%20Triad%20%2B%20VM%20Lifecycle-blue?style=flat-square)]()
[![Lab Docker](https://img.shields.io/badge/Lab-Docker%20incluido-orange?style=flat-square)](./laboratorio/)
[![Portafolio](https://img.shields.io/badge/Entregable-Vulnerability%20Assessment-green?style=flat-square)](./portafolio/)

---

## 📋 Resumen del módulo

| Atributo | Detalle |
|---|---|
| 🏷️ **Nivel** | Intermedio → Avanzado |
| ⏱️ **Duración estimada** | 4–6 semanas (6–8h por semana) |
| 🎯 **Resultado esperado** | Ejecutar un análisis de vulnerabilidades completo y producir un reporte con severidad, impacto CIA, validación técnica, remediación y priorización por rol |
| 🧪 **Práctica verificable** | Lab Docker con activos web y servicios vulnerables, escaneo, validación y reporte |
| 🗂️ **Portafolio** | Vulnerability Assessment Report con matriz CIA + CVSS + SLA de remediación |
| 🔗 **Requiere** | [Módulo 01 — Reconocimiento OSINT](../01-reconocimiento-osint/) · [Módulo 02 — Pentesting / Red Team](../02-pentesting-red-team/) |
| 🔗 **Conduce a** | [Módulo 04 — Explotación Web](../04-explotacion-web/) |

---

## 🎯 Qué aprenderás

- [ ] Diferenciar **hallazgo**, **debilidad**, **vulnerabilidad**, **riesgo** e **impacto**.
- [ ] Clasificar hallazgos usando la tríada **Confidencialidad, Integridad y Disponibilidad**.
- [ ] Aplicar un ciclo real de **vulnerability management**: descubrir, priorizar, remediar, validar y reportar.
- [ ] Pensar un mismo hallazgo desde 3 perspectivas: **Red Team**, **Blue Team** y **Purple Team**.
- [ ] Usar `Nuclei`, `OpenVAS/GVM`, `Nmap` y `searchsploit` para obtener y validar evidencia.
- [ ] Producir un reporte profesional con **CVSS**, impacto CIA, explotación controlada y plan de remediación.

---

## 🧭 Tres perspectivas, un solo hallazgo

| Equipo | Pregunta central | Resultado esperado |
|---|---|---|
| 🔴 **Red Team** | ¿Se puede explotar de forma realista? | Validación técnica del impacto |
| 🔵 **Blue Team** | ¿Qué activos afecta y cómo lo detecto o mitigo? | Priorización y plan defensivo |
| 🟣 **Purple Team** | ¿Cómo convertimos este hallazgo en una mejora medible? | Corrección validada + aprendizaje compartido |

---

## 🗺️ Contenido del módulo

```text
03-analisis-vulnerabilidades/
├── README.md
├── teoria/
│   ├── 01-cia-triad-y-severidad.md
│   ├── 02-vulnerability-management-lifecycle.md
│   └── 03-red-blue-purple-operando-juntos.md
├── herramientas/
│   ├── nuclei.md
│   ├── openvas-gvm.md
│   └── searchsploit.md
├── laboratorio/
│   ├── README-lab.md
│   └── docker-compose.yml
└── portafolio/
    └── TEMPLATE-reporte-vulnerabilidades.md
```

---

## 🚀 Inicio rápido

```bash
# 1. Ir al módulo
cd 01-CIBERSEGURIDAD/03-analisis-vulnerabilidades/

# 2. Leer teoría base
cat teoria/01-cia-triad-y-severidad.md
cat teoria/02-vulnerability-management-lifecycle.md

# 3. Levantar el lab
cd laboratorio/
docker compose up -d

# 4. Descubrir servicios
nmap -sV -sC 172.31.0.0/24

# 5. Escaneo rápido con Nuclei
nuclei -u http://localhost:8082 -severity low,medium,high,critical
```

---

## 📈 Salida profesional del módulo

Al finalizar deberías ser capaz de entregar un documento con:
- Resumen ejecutivo.
- Inventario de activos revisados.
- Hallazgos ordenados por criticidad.
- Impacto sobre **C**, **I** y **A**.
- Evidencia del escaneo y de la validación técnica.
- Remediación priorizada por SLA.
- Observaciones separadas por Red, Blue y Purple Team.

---

## ⚖️ Aviso ético

> El análisis de vulnerabilidades es una actividad autorizada, controlada y documentada. La validación técnica debe realizarse solo contra activos propios, laboratorios locales o plataformas permitidas. Nunca uses scanners o validación ofensiva contra terceros sin permiso escrito.

---

---

## 🛠️ Herramientas de análisis de vulnerabilidades

### Nuclei — Scanner basado en plantillas

```bash
# Escaneo básico
nuclei -u http://target.com

# Filtrar por severidad
nuclei -u http://target.com -severity critical,high

# Usar plantillas específicas
nuclei -u http://target.com -t cves/ -t vulnerabilities/

# Output en formato JSON
nuclei -u http://target.com -json -o resultados.json

# Escanear múltiples URLs
echo "http://target1.com" | nuclei -l urls.txt

# Actualizar plantillas
nuclei -update-templates
```

### OpenVAS/GVM — Scanner completo

```bash
# Iniciar GVM
sudo gvm-start

# Crear task
# 1. Login a https://127.0.0.1:9392
# 2. Scan → Tasks → New Task
# 3. Configurar target (IP/rango)
# 4. Seleccionar profile (Full & Fast)
# 5. Ejecutar

# Analizar resultados
# Reports → Seleccionar reporte → Export (PDF/CSV)

# Command line (si disponible)
gvm-cli socket --xml "<get_tasks/>" 2>/dev/null
```

### Searchsploit — Buscar exploits

```bash
# Buscar exploit por nombre
searchsploit apache 2.4.49
searchsploit smb windows

# Buscar por CVE
searchsploit CVE-2021-44228

# Filtrar por tipo
searchsploit --type remote
searchsploit --type local

# Copiar exploit
searchsploit -m 50383   # Copia el exploit a directorio actual

# Ver contenido
cat 50383.py

# Buscar sin Metasploit
searchsploit --exclude="Metasploit" windows smb
```

### Nikto — Scanner web

```bash
# Escaneo básico
nikto -h http://target.com

# Con autenticación
nikto -h http://target.com -id admin:password

# Evitar detección
nikto -h http://target.com -Tuning 1234

# Output a archivo
nikto -h http://target.com -o reporte.html -Format htm
```

### SQLMap — SQL Injection

```bash
# Detectar SQLi
sqlmap -u "http://target.com/page?id=1"

# Enumerar bases de datos
sqlmap -u "http://target.com/page?id=1" --dbs

# Enumerar tablas
sqlmap -u "http://target.com/page?id=1" -D database --tables

# Dump de tablas
sqlmap -u "http://target.com/page?id=1" -D database -T users --dump

# Con cookies
sqlmap -u "http://target.com/page?id=1" --cookie="session=abc123"

# POST request
sqlmap -u "http://target.com/login" --data="user=admin&pass=*"
```

---

## 🧪 Ejercicios prácticos

### Ejercicio 1: Escaneo completo de vulnerabilidades

```bash
# 1. Nmap con scripts de vulnerabilidades
nmap -sV --script=vuln target

# 2. Nuclei con todas las severidades
nuclei -u http://target -severity critical,high,medium -o nuclei-report.txt

# 3. Nikto
nikto -h http://target -o nikto-report.txt

# 4. OpenVAS (si disponible)
# Crear task y ejecutar

# 5. Consolidar resultados
echo "=== Resumen ===" > reporte-vulns.txt
echo "Critical: $(grep -c 'critical' nuclei-report.txt)" >> reporte-vulns.txt
echo "High: $(grep -c 'high' nuclei-report.txt)" >> reporte-vulns.txt
echo "Medium: $(grep -c 'medium' nuclei-report.txt)" >> reporte-vulns.txt
```

### Ejercicio 2: Validación manual de vulnerabilidades

```bash
# Para cada vulnerabilidad encontrada:
# 1. Verificar si es falsa positiva
# 2. Determinar el impacto real
# 3. Documentar evidencia

# Ejemplo: validar XSS
curl -s "http://target/search?q=<script>alert(1)</script>"
# Verificar si el script se ejecuta en el navegador

# Ejemplo: validar SQLi
sqlmap -u "http://target/page?id=1" --batch --is-dba
# Verificar si tenemos acceso a la DB

# Ejemplo: validar servicio vulnerable
nmap -sV -p 445 target --script=smb-vuln-ms17-010
```

### Ejercicio 3: Priorización con CVSS

```markdown
# Matriz de priorización

| Vulnerabilidad | CVSS | Severidad | Activo | Remediación |
|---------------|------|-----------|--------|-------------|
| SQL Injection | 9.8 | CRITICAL | Web App | Parametrizar queries |
| XSS Reflejado | 6.1 | MEDIUM | Web App | Sanitizar inputs |
| Servicio obsoleto | 7.5 | HIGH | Server | Actualizar software |

# Cálculo CVSS v3.1
# Attack Vector: Network (N)
# Attack Complexity: Low (L)
# Privileges Required: None (N)
# User Interaction: None (N)
# Scope: Changed (C)
# CIA Impact: High (H)

# Score: 9.8 (CRITICAL)
```

### Ejercicio 4: Reporte de vulnerabilidades

```markdown
# Reporte de Análisis de Vulnerabilidades

## Resumen Ejecutivo
- Alcance: 192.168.1.0/24
- Total vulnerabilidades: 15
- Críticas: 2 | Altas: 5 | Medias: 6 | Bajas: 2

## Inventario de activos
| IP | Hostname | SO | Servicios |
|----|----------|----|-----------|
| .1 | web01 | Ubuntu 20.04 | HTTP, SSH |
| .2 | db01 | CentOS 8 | MySQL, SSH |

## Hallazgos
### H-001: SQL Injection en login
- CVSS: 9.8 (CRITICAL)
- CIA: C+I+A comprometidos
- Evidencia: sqlmap output
- Remediación: Parametrizar queries, WAF
- SLA: 24 horas

### H-002: XSS reflejado en search
- CVSS: 6.1 (MEDIUM)
- CIA: C impactado
- Evidencia: payload ejecutado
- Remediación: Sanitización, CSP
- SLA: 7 días
```

---

## 📋 Checklist de análisis

- [ ] Inventario de activos completado
- [ ] Escaneo automatizado ejecutado (Nuclei, OpenVAS, Nikto)
- [ ] Vulnerabilidades identificadas
- [ ] Falsos positivos eliminados
- [ ] CVSS calculado para cada hallazgo
- [ ] Impacto CIA documentado
- [ ] Priorización establecida
- [ ] Plan de remediación creado
- [ ] Reporte generado

---

**[⬆ Volver al inicio](../../README.md)** · **[📖 Leer teoría →](./teoria/01-cia-triad-y-severidad.md)** · **[🧪 Ir al lab →](./laboratorio/README-lab.md)**
