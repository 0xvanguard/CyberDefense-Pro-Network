---
title: "🤖 Lab ai-recon-01: Agentes OSINT"
description: "🤖 Lab ai-recon-01: Agentes OSINT"
---

# 🤖 Lab ai-recon-01: Agentes OSINT

> Usa agentes de IA para automatizar reconocimiento OSINT y descubrir información de objetivos.

## 🎯 Objetivos de Aprendizaje

Al completar este lab podrás:

- [ ] Usar agentes de IA para reconocimiento automatizado
- [ ] Automatizar recopilación de OSINT con scripts
- [ ] Analizar resultados con IA
- [ ] Generar reportes automáticos
- [ ] Integrar múltiples fuentes de datos

## ⏱️ Información del Lab

| Campo | Valor |
|-------|-------|
| **Dificultad** | 🟡 Intermedio |
| **Tiempo estimado** | 90 minutos |
| **XP en juego** | 450 puntos |
| **Herramientas** | Python, APIs de IA, subfinder, amass |
| **Flags** | 8 |

## 🚀 Inicio Rápido

```bash
# Levantar el entorno
cd labs/ai-agents/ai-recon-01/
docker compose up -d

# Verificar servicios
docker compose ps
```

## 📋 Ejercicios

### Ejercicio 1: Configurar Agente OSINT (60 XP)

Crea un agente de reconocimiento con Python:

```python
#!/usr/bin/env python3
# agent_osint.py

import subprocess
import json
from datetime import datetime

class OSINTAgent:
    def __init__(self, target):
        self.target = target
        self.results = {}
    
    def subdomain_enum(self):
        """Enumerar subdominios con subfinder"""
        cmd = f"subfinder -d {self.target} -silent"
        result = subprocess.run(cmd, shell=True, capture_output=True, text=True)
        self.results['subdomains'] = result.stdout.strip().split('\n')
        return self.results['subdomains']
    
    def port_scan(self, host):
        """Escanear puertos con nmap"""
        cmd = f"nmap -sV -p- --open {host}"
        result = subprocess.run(cmd, shell=True, capture_output=True, text=True)
        self.results['ports'] = result.stdout
        return result.stdout
    
    def generate_report(self):
        """Generar reporte JSON"""
        report = {
            'target': self.target,
            'timestamp': datetime.now().isoformat(),
            'subdomains': len(self.results.get('subdomains', [])),
            'results': self.results
        }
        
        with open(f'report_{self.target}.json', 'w') as f:
            json.dump(report, f, indent=2)
        
        return report

# Ejecutar agente
agent = OSINTAgent("example.com")
subdomains = agent.subdomain_enum()
print(f"Found {len(subdomains)} subdomains")
agent.generate_report()
```

**Flag:** `[___]`

---

### Ejercicio 2: Enumeración Automatizada (60 XP)

Ejecuta enumeración completa:

```bash
# 1. Subdomain enumeration
subfinder -d target.com -silent | tee subdomains.txt

# 2. Port scanning
nmap -sV -p- --open -iL subdomains.txt | tee nmap_results.txt

# 3. Web technology detection
whatweb -i subdomains.txt | tee technologies.txt

# 4. DNS enumeration
for sub in $(cat subdomains.txt); do
  dig +short $sub | head -1
done | sort -u > ips.txt

# 5. Documentar hallazgos
echo "=== OSINT Results ===" > osint_report.txt
echo "Target: target.com" >> osint_report.txt
echo "Subdomains: $(wc -l < subdomains.txt)" >> osint_report.txt
echo "IPs: $(wc -l < ips.txt)" >> osint_report.txt
```

**Flag:** `[___]`

---

### Ejercicio 3: Análisis con IA (60 XP)

Usa IA para analizar resultados:

```python
#!/usr/bin/env python3
# ai_analyzer.py

import json
from typing import Dict, List

class AIAnalyzer:
    def __init__(self):
        self.threat_indicators = []
    
    def analyze_ports(self, port_data: str) -> Dict:
        """Analizar puertos abiertos con IA"""
        analysis = {
            'open_ports': [],
            'services': [],
            'risks': []
        }
        
        for line in port_data.split('\n'):
            if '/tcp' in line and 'open' in line:
                port_info = line.strip()
                analysis['open_ports'].append(port_info)
                
                # Detectar servicios riesgosos
                if any(s in port_info.lower() for s in ['ftp', 'telnet', 'ssh']):
                    analysis['risks'].append(f"Remote access: {port_info}")
                if 'http' in port_info.lower():
                    analysis['services'].append(f"Web: {port_info}")
        
        return analysis
    
    def analyze_subdomains(self, subdomains: List[str]) -> Dict:
        """Analizar subdominios"""
        analysis = {
            'total': len(subdomains),
            'categories': {
                'web': [],
                'api': [],
                'admin': [],
                'dev': []
            }
        }
        
        for sub in subdomains:
            if 'api' in sub:
                analysis['categories']['api'].append(sub)
            elif 'admin' in sub:
                analysis['categories']['admin'].append(sub)
            elif 'dev' in sub or 'test' in sub:
                analysis['categories']['dev'].append(sub)
            else:
                analysis['categories']['web'].append(sub)
        
        return analysis
    
    def generate_threat_report(self, analysis: Dict) -> str:
        """Generar reporte de amenazas"""
        report = "# AI Threat Analysis Report\n\n"
        report += f"## Summary\n"
        report += f"- Total subdomains: {analysis.get('total', 0)}\n"
        report += f"- High-risk services: {len(analysis.get('risks', []))}\n\n"
        
        if analysis.get('risks'):
            report += "## High Risk Items\n"
            for risk in analysis['risks']:
                report += f"- ⚠️ {risk}\n"
        
        return report

# Ejecutar análisis
analyzer = AIAnalyzer()
# Load data and analyze
```

**Flag:** `[___]`

---

### Ejercicio 4: Reporte Automático (80 XP)

Genera reporte completo:

```python
#!/usr/bin/env python3
# report_generator.py

import json
from datetime import datetime

class ReportGenerator:
    def __init__(self, target):
        self.target = target
        self.findings = []
    
    def add_finding(self, category, finding, severity):
        self.findings.append({
            'category': category,
            'finding': finding,
            'severity': severity
        })
    
    def generate_markdown(self):
        report = f"# OSINT Report: {self.target}\n\n"
        report += f"**Generated:** {datetime.now().isoformat()}\n\n"
        
        # Executive Summary
        critical = sum(1 for f in self.findings if f['severity'] == 'critical')
        high = sum(1 for f in self.findings if f['severity'] == 'high')
        medium = sum(1 for f in self.findings if f['severity'] == 'medium')
        
        report += "## Executive Summary\n\n"
        report += f"- **Critical:** {critical}\n"
        report += f"- **High:** {high}\n"
        report += f"- **Medium:** {medium}\n\n"
        
        # Findings
        report += "## Findings\n\n"
        for i, finding in enumerate(self.findings, 1):
            report += f"### {i}. {finding['category']}\n"
            report += f"**Severity:** {finding['severity'].upper()}\n"
            report += f"**Description:** {finding['finding']}\n\n"
        
        return report

# Generar reporte
generator = ReportGenerator("example.com")
generator.add_finding("Subdomain", "api.example.com found", "medium")
generator.add_finding("Port", "FTP open on 21", "high")
print(generator.generate_markdown())
```

**Flag:** `[___]`

---

### Ejercicio 5: Multi-Source Intelligence (60 XP)

Integra múltiples fuentes:

```bash
# 1. OSINT Framework
# Usar theHarvester para emails
theHarvester -d target.com -b google,linkedin

# 2. Certificate Transparency
curl -s "https://crt.sh/?q=%.target.com" | grep -oP '[^"]+\.target\.com' | sort -u

# 3. DNS Records
dig target.com ANY +noall +answer
dig target.com MX +noall +answer
dig target.com NS +noall +answer

# 4. Social Media
# Buscar en LinkedIn, GitHub, etc.

# 5. Integrar resultados
cat > intel_report.json << 'EOF'
{
  "target": "target.com",
  "sources": {
    "subdomains": [],
    "emails": [],
    "ips": [],
    "technologies": []
  }
}
EOF
```

**Flag:** `[___]`

---

### Ejercicio 6: Automatización con Cron (40 XP)

Automatiza el reconocimiento:

```bash
#!/bin/bash
# auto_recon.sh

TARGET=$1
OUTPUT_DIR="/tmp/recon_$(date +%Y%m%d)"

mkdir -p $OUTPUT_DIR

# Subdomain enum
subfinder -d $TARGET -silent > $OUTPUT_DIR/subdomains.txt

# Port scan
nmap -sV -p- --open -iL $OUTPUT_DIR/subdomains.txt > $OUTPUT_DIR/nmap.txt

# Generate report
python3 report_generator.py $TARGET > $OUTPUT_DIR/report.md

echo "Recon complete: $OUTPUT_DIR"
```

**Flag:** `[___]`

---

### Ejercicio 7: Dashboard de Resultados (40 XP)

Crea dashboard para visualizar resultados:

```html
<!-- dashboard.html -->
<!DOCTYPE html>
<html>
<head>
    <title>OSINT Dashboard</title>
    <style>
        .card { border: 1px solid #ccc; padding: 20px; margin: 10px; }
        .critical { border-color: red; }
        .high { border-color: orange; }
        .medium { border-color: yellow; }
    </style>
</head>
<body>
    <h1>OSINT Dashboard</h1>
    <div class="card">
        <h3>Summary</h3>
        <p>Subdomains: <span id="subdomains">0</span></p>
        <p>Open Ports: <span id="ports">0</span></p>
    </div>
    <div class="card critical">
        <h3>Critical Findings</h3>
        <ul id="critical"></ul>
    </div>
</body>
</html>
```

**Flag:** `[___]`

---

### Ejercicio 8: Reporte Final (60 XP)

Genera reporte ejecutivo:

```markdown
# OSINT Report - AI Agent

## Executive Summary
- Target: target.com
- Subdomains found: 15
- Open ports: 23
- Critical findings: 2
- High findings: 5

## Key Findings
1. **api.target.com** - API endpoint sin autenticación
2. **admin.target.com** - Panel de administración expuesto
3. **dev.target.com** - Servidor de desarrollo accesible

## Recommendations
1. Implementar autenticación en APIs
2. Restringir acceso a paneles admin
3. Aislar servidores de desarrollo

## Appendix
- Full subdomain list
- Port scan results
- Technology fingerprinting
```

**Flag:** `[___]`

## 🏁 Validación

```bash
./scripts/validate.sh
```

## 📝 Criterios de Éxito

| Ejercicio | Criterio | Puntos | Estado |
|-----------|----------|--------|--------|
| 1 | Agente configurado | 60 | ⬜ |
| 2 | Enumeración ejecutada | 60 | ⬜ |
| 3 | Análisis con IA | 60 | ⬜ |
| 4 | Reporte generado | 80 | ⬜ |
| 5 | Multi-source integrado | 60 | ⬜ |
| 6 | Automatización | 40 | ⬜ |
| 7 | Dashboard creado | 40 | ⬜ |
| 8 | Reporte final | 60 | ⬜ |
| **Total** | | **450** | ⬜ |

---

*Lab creado para CyberDefense Labs — Nivel Intermedio*
