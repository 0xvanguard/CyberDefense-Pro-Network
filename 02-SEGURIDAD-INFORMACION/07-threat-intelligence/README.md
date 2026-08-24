# 🎯 Módulo 07 — Threat Intelligence

> **Objetivo principal:** Comprender y aplicar inteligencia de amenazas (CTI) para detectar, prevenir y responder a incidentes de seguridad utilizando MITRE ATT&CK, feeds de amenazas e indicadores de compromiso (IOCs).

[![Nivel](https://img.shields.io/badge/Nivel-Intermedio%20→%20Avanzado-orange?style=flat-square)]()
[![Enfoque](https://img.shields.io/badge/Enfoque-Blue%20Team%20%7C%20Threat%20Hunting-green?style=flat-square)]()
[![Frameworks](https://img.shields.io/badge/Frameworks-MITRE%20ATT%26CK%20%7C%20STIX%20%7C%20TAXII-blue?style=flat-square)]()

---

## 📋 Resumen del módulo

| Atributo | Detalle |
|---|---|
| 🏷️ **Nivel** | Intermedio → Avanzado |
| ⏱️ **Duración estimada** | 4–5 semanas |
| 🎯 **Resultado esperado** | Crear y operar un proceso de CTI, integrar feeds de amenazas en SIEM, realizar threat hunting |
| 🧪 **Práctica verificable** | Threat landscape report, IOC feeds configurados, threat hunts documentados |
| 🗂️ **Portafolio** | CTI report + threat hunts + detection rules |
| 🔗 **Requiere** | Blue Team basics, SIEM (Wazuh/ELK) |
| 🔗 **Conduce a** | Threat Hunting, Incident Response, Purple Team |

---

## 🎯 Qué aprenderás

- [ ] Entender los tipos y ciclos de Threat Intelligence
- [ ] Aplicar MITRE ATT&CK para mapear adversarios
- [ ] Recopilar, analizar y distribuir IOCs
- [ ] Configurar y utilizar feeds de amenazas (OSINT, STIX/TAXII)
- [ ] Realizar threat hunting proactivo
- [ ] Crear detection rules basadas en intelligence

---

## 📚 Contenido del módulo

### FASE 1 — Fundamentos de CTI (Semana 1)

#### 1.1 Tipos de Threat Intelligence

| Tipo | Audiencia | Contenido | Ejemplo |
|------|-----------|-----------|---------|
| **Estratégica** | Executivos, CISO | Tendencias, landscape | "El ransomware dirigido a salud aumentó 300%" |
| **Táctica** | SOC, IR | TTPs de adversarios | "APT29 usa phishing con macros VBA" |
| **Operativa** | Analysts | Campañas activas | "Campaña de phishing contra sector financiero LATAM" |
| **Técnica** | Engineers | IOCs, signatures | "Hash: abc123, IP: 1.2.3.4, Domain: evil.com" |

#### 1.2 Intelligence Cycle
```
1. Planificación → ¿Qué necesitamos saber?
2. Recopilación → Fuentes OSINT, feeds, dark web
3. Procesamiento → Limpiar, normalizar, correlacionar
4. Análisis → Contextualizar, patrones, attribution
5. Difusión → Distribuir al equipo correcto
6. Retroalimentación → Evaluar utilidad, refinar
```

---

### FASE 2 — MITRE ATT&CK (Semana 2)

#### 2.1 Matriz ATT&CK Enterprise

| Táctica | ID | Descripción | Ejemplos de Técnicas |
|---------|-----|-------------|---------------------|
| **Initial Access** | TA0001 | Primera entrada | Phishing (T1566), Exploit Public App (T1190) |
| **Execution** | TA0002 | Ejecutar código | Command Script (T1059), PowerShell (T1059.001) |
| **Persistence** | TA0003 | Mantener acceso | Registry Run Key (T1547.001), Scheduled Task (T1053) |
| **Privilege Escalation** | TA0004 | Obtener más permisos | Exploitation for PE (T1068) |
| **Defense Evasion** | TA0005 | Evadir detección | Obfuscated Files (T1027), Disable Defender (T1562) |
| **Credential Access** | TA0006 | Robar credenciales | Brute Force (T1110), Credential Dumping (T1003) |
| **Discovery** | TA0007 | Explorar entorno | Network Service Scan (T1046) |
| **Lateral Movement** | TA0008 | Moverse en la red | Remote Services (T1021), Pass the Hash (T1550) |
| **Collection** | TA0009 | Recopilar datos | Data from Local (T1005) |
| **Exfiltration** | TA0010 | Sacar datos | Exfil over C2 (T1041) |
| **Impact** | TA0040 | Causar daño | Data Encrypted (T1486), Defacement (T1491) |

#### 2.2 Grupos de Adversarios Conocidos

| Grupo | Atribución | Sector Objetivo | Tácticas Principales |
|-------|-----------|-----------------|---------------------|
| **APT29** (Cozy Bear) | Rusia (SVR) | Gobiernos, think tanks | Supply Chain, Steal Web App Credentials |
| **APT41** (Double Dragon) | China (MSS) | Telecom, salud | Supply Chain, Ransomware |
| **Lazarus Group** | Corea del Norte | Financiero, crypto | Phishing, Custom Crypto |
| **FIN7** | Rusia | Retail, hospitalidad | Phishing, Lateral Movement |
| **Conti** | Rusia (Crim) | Multi-sector | Ransomware, Data Encrypted |

---

### FASE 3 — IOC y Feeds de Amenazas (Semana 3)

#### 3.1 Tipos de IOCs

| Tipo | Descripción | Ejemplo |
|------|-------------|---------|
| **IP Address** | Dirección del atacante | `185.220.101.45` |
| **Domain** | Dominio malicioso | `evil-phishing.com` |
| **URL** | URL de descarga | `http://evil.com/payload.exe` |
| **File Hash** | Hash del malware | `SHA256: abc123...` |
| **Email Address** | Remitente de phishing | `admin@evil.com` |
| **YARA Rule** | Firma de malware | Regla que detecta patrones |
| **Sigma Rule** | Firma de log | Detección en SIEM |

#### 3.2 Fuentes de feeds de amenazas

| Fuente | Tipo | Costo | Calidad |
|--------|------|-------|---------|
| **AlienVault OTX** | Open | Gratis | Media |
| **AbuseIPDB** | IP Reputation | Freemium | Alta |
| **URLhaus** | Malicious URLs | Gratis | Alta |
| **MalwareBazaar** | Malware Samples | Gratis | Alta |
| **PhishTank** | Phishing URLs | Gratis | Media |
| **MISP** | Platform | Gratis (self-hosted) | Muy Alta |
| **VirusTotal** | Multi-source | Freemium | Muy Alta |
| **Recorded Future** | Commercial | Pago | Muy Alta |

#### 3.3 STIX/TAXII
```json
{
  "type": "indicator",
  "spec_version": "2.1",
  "id": "indicator--a1b2c3d4",
  "created": "2026-01-15T10:00:00Z",
  "pattern": "[domain-name:value = 'evil-phishing.com']",
  "pattern_type": "stix",
  "valid_from": "2026-01-15T10:00:00Z",
  "labels": ["malicious-activity", "phishing"]
}
```

---

### FASE 4 — Threat Hunting (Semana 4-5)

#### 4.1 Hipótesis de Threat Hunting

| Hipótesis | Técnica | Herramienta |
|-----------|---------|-------------|
| "¿Hay beaconing a C2?" | Análisis de intervalos DNS | RITA, JA3 |
| "¿PowerShell obfuscado?" | Búsqueda destrings-encoded | Sigma, YARA |
| "¿Movimiento lateral?" | Login analysis across hosts | Wazuh, ELK |
| "¿Data exfil via DNS?" | DNS query volume analysis | Zeek, Suricata |
| "¿Credential dumping?" | LSASS access monitoring | Sysmon, ETW |

#### 4.2 Threat Hunting Process
```
1. Hipótesis → "Creo que hay X porque Y"
2. Datos → ¿Qué logs necesito?
3. Investigación → Buscar evidencia
4. Análisis → ¿Confirmar o refutar?
5. Documentación → Writeup + detection rule
6. Automatización → SIEM rule para detección continua
```

---

## 🧪 Laboratorios

| Lab | Descripción | Nivel |
|-----|-------------|-------|
| `lab-01` | Mapear un ataque real a MITRE ATT&CK | Básico |
| `lab-02` | Configurar MISP + feeds de amenazas | Intermedio |
| `lab-03` | Threat hunt: detectar beaconing C2 | Avanzado |
| `lab-04` | Crear Sigma rules desde un APT report | Avanzado |

---

## 🔗 Referencias

- [MITRE ATT&CK](https://attack.mitre.org/)
- [MISP Project](https://www.misp-project.org/)
- [STIX/TAXII](https://oasis-open.github.io/cti-documentation/)
- [Threat Hunter Playbook](https://github.com/OTRF/ThreatHunter-Playbook)
- [Sigma Rules](https://github.com/SigmaHQ/sigma)
- [Recorded Future](https://www.recordedfuture.com/)

---

*Última actualización: Agosto 2026*
