---
title: "Módulo 07 — Threat Intelligence"
---

# 🕵️ Módulo 07 — Threat Intelligence

> **Objetivo:** Anticipar ataques con inteligencia operativa, táctica y estratégica usando CTI.

[![Nivel](https://img.shields.io/badge/Nivel-Intermedio--Avanzado-orange?style=flat-square)]()
[![Duración](https://img.shields.io/badge/Duración-2%20meses-blue?style=flat-square)]()

---

## 📋 Resumen del módulo

| Atributo | Detalle |
|----------|---------|
| **Pre-requisitos** | Módulos 01-06 completados |
| **Herramientas** | MISP, OpenCTI, MITRE ATT&CK |
| **Fuentes** | OTX, AlienVault, AbuseIPDB |
| **Nivel** | Intermedio-Avanzado |

---

## 1. 🧠 Teoría: Niveles de Threat Intelligence

| Nivel | Pregunta | Audiencia | Ejemplo |
|-------|----------|-----------|---------|
| **Estratégica** | ¿Quién y por qué? | C-Suite, Directivos | Informes APT, geopolítica |
| **Operativa** | ¿Cómo atacan? | SOC, Red Team | TTPs, campañas activas |
| **Táctica** | ¿Qué herramientas usan? | Analistas | Técnicas específicas |
| **Técnica** | ¿Qué IOCs específicos? | SIEM, IDS | IPs, hashes, dominios |

---

## 2. 🔧 Herramientas

### MISP — Threat Intelligence Platform

```bash
# Instalar con Docker
git clone https://github.com/MISP/MISP.git
cd MISP
docker-compose up -d

# Acceder: https://misp.local
# Credenciales: admin@admin.test / admin
```

### OpenCTI

```bash
# Instalar
git clone https://github.com/OpenCTI-Platform/opencti.git
cd opencti/docker
docker-compose up -d

# Conectores:
# - MITRE ATT&CK
# - AlienVault OTX
# - VirusTotal
```

### MITRE ATT&CK

```bash
# Navegador ATT&CK
https://attack.mitre.org/navigator/

# Descargar matrices
https://attack.mitre.org/matrices/enterprise/
```

---

## 3. 📊 Fuentes de CTI

### Fuentes abiertas

| Fuente | Tipo | Costo |
|--------|------|-------|
| **AlienVault OTX** | IOC feeds | Gratis |
| **AbuseIPDB** | IPs maliciosas | Freemium |
| **VirusTotal** | Malware IOCs | Freemium |
| **URLhaus** | URLs maliciosas | Gratis |
| **PhishTank** | Phishing | Gratis |
| **MISP Galaxy** | Atributos de actores | Gratis |

### Formatos de intercambio

| Formato | Descripción |
|---------|-------------|
| **STIX** | Structured Threat Information |
| **TAXII** | Transport for sharing CTI |
| **OpenIOC** | Indicators of Compromise |
| **MISP** | Formato nativo de MISP |

---

## 4. 📋 Ciclo de CTI

```
1. Recopilar → Fuentes OSINT, feeds, reports
2. Procesar → Normalizar, correlacionar, enriquecer
3. Analizar → Contextualizar, priorizar
4. Distribuir → STIX/TAXII, MISP, SIEM
5. Consumir → Detección, hunting, respuesta
6. Retroalimentar → Actualizar fuentes y reglas
```

---

## 5. ✏️ Ejercicios prácticos

### Ejercicio 1: Investigar actor amenaza (30 min)

1. Elige un APT (ej: APT29, Lazarus Group)
2. Busca en MITRE ATT&CK sus TTPs
3. Documenta:
   - País de origen
   - Sectores objetivo
   - Técnicas principales
   - Campañas conocidas

### Ejercicio 2: Configurar MISP (40 min)

1. Instala MISP con Docker
2. Crea un evento con 5 IOCs
3. Comparte con un feed externo
4. Importa IOCs de AlienVault OTX

### Ejercicio 3: Crear regla Sigma desde CTI (30 min)

1. Busca un IOC reciente (hash, IP, dominio)
2. Crea una regla Sigma para detectarlo
3. Convierte a formato Wazuh
4. Valida con datos de prueba

---

## 6. 📊 Reporte de CTI

```markdown
## Reporte de Inteligencia - [Fecha]

### Resumen Ejecutivo
- **Activo:** [actor/campaña]
- **Nivel de confianza:** Alto/Medio/Bajo
- **Urgencia:** Alta/Media/Baja

### Hallazgos
1. **IOC principal:** [hash/IP/dominio]
2. **TTPs:** [ATT&CK IDs]
3. **Sectores afectados:** [sectores]
4. **Evidencia:** [fuentes]

### Recomendaciones
1. [ ] Bloquear IOCs en firewall
2. [ ] Actualizar reglas de detección
3. [ ] Monitorear actividad sospechosa

### Fuentes
- [fuente 1]
- [fuente 2]
```

---

> **Módulo completado.** Has completado el track de Seguridad de la Información. Ahora tienes conocimientos de gestión de riesgos, defensa, SOC, DevSecOps, hardening, compliance y threat intelligence.
