---
title: "Módulo 04 — DevSecOps"
---

# ⚙️ Módulo 04 — DevSecOps

> **Objetivo:** Integrar seguridad en cada fase del ciclo de desarrollo de software sin frenar la entrega.

[![Nivel](https://img.shields.io/badge/Nivel-Intermedio-orange?style=flat-square)]()
[![Duración](https://img.shields.io/badge/Duración-1.5%20meses-blue?style=flat-square)]()

---

## 📋 Resumen del módulo

| Atributo | Detalle |
|----------|---------|
| **Pre-requisitos** | Fundamentos completados |
| **Stack** | GitHub Actions, Trivy, Semgrep, Gitleaks |
| **Entregable** | Pipeline CI/CD seguro |
| **Nivel** | Intermedio |

---

## 1. 🧠 Teoría: DevSecOps

### El pipeline seguro

```
commit → secret-scan → SAST → build → image-scan → sign → DAST → deploy
```

### Principios clave

| Principio | Descripción |
|-----------|-------------|
| **Shift-left** | Seguridad desde el commit |
| **Automation** | Todo automatizado, nada manual |
| **Policy-as-Code** | Reglas como código versionado |
| **Least Privilege** | Permisos mínimos necesarios |
| **Supply Chain** | Seguridad de dependencias |

---

## 2. 🔧 Herramientas

### Secret Scanning

```bash
# Gitleaks - detectar secrets en repos
gitleaks detect --source . --report-format json

# Pre-commit hook
pip install gitleaks
gitleaks protect --staged
```

### SAST (Static Analysis)

```bash
# Semgrep - análisis estático
semgrep --config=auto .

# Bandit - Python security
bandit -r src/

# CodeQL - análisis profundo (GitHub)
# Configurar en .github/workflows/codeql-analysis.yml
```

### Container Security

```bash
# Trivy - escaneo de imágenes
trivy image nginx:latest

# Grype - alternativa
grype nginx:latest

# Hadolint - linting de Dockerfiles
hadolint Dockerfile
```

### DAST (Dynamic Analysis)

```bash
# OWASP ZAP - testing dinámico
zap-baseline.py -t https://target.com

# Nuclei - escaneo de vulnerabilidades
nuclei -target https://target.com
```

---

## 3. 📋 Pipeline de referencia

### GitHub Actions

```yaml
name: Security Pipeline
on: [push, pull_request]

jobs:
  secret-scan:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - name: Gitleaks
        uses: gitleaks/gitleaks-action@v2

  sast:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - name: Semgrep
        uses: semgrep/semgrep-action@v1

  container-scan:
    runs-on: ubuntu-latest
    steps:
      - name: Build image
        run: docker build -t myapp:${{ github.sha }} .
      - name: Trivy scan
        uses: aquasecurity/trivy-action@master
        with:
          image-ref: myapp:${{ github.sha }}
          severity: CRITICAL,HIGH
```

---

## 4. ✏️ Ejercicios prácticos

### Ejercicio 1: Secret scanning (15 min)

1. Crea un repo con un "secreto" falso (`API_KEY=sk-1234567890`)
2. Configura Gitleaks
3. Verifica que detecta el secreto

### Ejercicio 2: SAST con Semgrep (20 min)

1. Instala Semgrep
2. Ejecuta contra un proyecto Python
3. Revisa los hallazgos y prioriza

### Ejercicio 3: Container scanning (20 min)

1. Crea un Dockerfile intencionalmente inseguro
2. Ejecuta Trivy contra la imagen
3. Corrige los hallazgos críticos

---

> **Siguiente:** [Módulo 05 — Hardening](./05-hardening)
