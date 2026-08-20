# ⚙️ Módulo 04 — DevSecOps

> **Nivel:** Avanzado · **Objetivo:** integrar seguridad en todo el ciclo de vida del software (SDLC), desde el código hasta producción.

[![Nivel](https://img.shields.io/badge/Nivel-Avanzado-red?style=flat-square)]()
[![Enfoque](https://img.shields.io/badge/Enfoque-Automatizaci%C3%B3n%20%7C%20C%C3%B3digo-purple?style=flat-square)]()

---

## 📋 Resumen

| Atributo | Detalle |
|---|---|
| 🎯 **Resultado** | Un pipeline CI/CD que bloquea secretos, vulnerabilidades e imágenes inseguras automáticamente |
| 🧪 **Práctica** | GitHub Actions + Trivy + Semgrep + ZAP + Cosign |
| 🗂️ **Portafolio** | Pipeline DevSecOps funcional y documentado |
| 🔗 **Requiere** | Saber programar + nociones de CI/CD y Docker |
| 🔗 **Conduce a** | [Seguridad en la Nube](../../01-CIBERSEGURIDAD/seguridad-nube/) |

---

## 🧭 Qué es DevSecOps (shift-left)

DevSecOps mueve la seguridad **hacia la izquierda** (al inicio del ciclo), integrándola como **código** en cada etapa:

```
Código → Build → Test → Release → Deploy → Operación
   │       │       │      │         │         │
  SAST   SCA     DAST   Firma     IaC      Runtime
  secret  build   IAST   (Cosign)  scan     (Falco)
```

> **Principio:** la seguridad no es un "gate" al final que bloquea todo; es una **serie de controles automatizados y rápidos** que dan feedback temprano al desarrollador.

---

## 🗺️ Mapa de herramientas por etapa

| Etapa | Qué busca | Herramientas |
|---|---|---|
| **Código** | Secretos en el repo | Gitleaks, TruffleHog, detect-secrets |
| **Código** | Bugs/vulns (SAST) | Semgrep, CodeQL, Bandit, SpotBugs |
| **Dependencias** | Vulns de librerías (SCA) | Dependabot, Snyk, OSV, Trivy |
| **Build** | Imágenes inseguras | Trivy, Grype, Clair |
| **IaC** | Config cloud insegura | Checkov, tfsec, KICS |
| **Test/Stage** | Vulnerabilidades en runtime (DAST) | OWASP ZAP, Burp |
| **Release** | Integridad/firma | Cosign + Sigstore, SLSA, SBOM (Syft) |
| **Operación** | Amenazas en runtime | Falco, Tetragon, Kubescape |

---

## 🗂️ Estructura del módulo

| Carpeta | Contenido | Estado |
|---|---|---|
| [`docker-security/`](./docker-security/) | Hardening de imágenes y contenedores (Docker) | ✅ Completo |
| [`kubernetes-security/`](./kubernetes-security/) | Seguridad de Kubernetes (RBAC, pods, Falco, OPA) | ✅ Completo |
| [`ci-cd-security/`](./ci-cd-security/) | Pipeline CI/CD seguro (SLSA, OIDC, firma) | ✅ Completo |
| [`secret-scanning/`](./secret-scanning/) | Gitleaks + TruffleHog | ✅ Completo |
| [`sast-dast/`](./sast-dast/) | Semgrep/CodeQL (SAST) + ZAP (DAST) | ✅ Completo |

---

## 🚀 Orden de estudio

1. [`docker-security/`](./docker-security/) — containers (la base de todo lo demás)
2. [`kubernetes-security/`](./kubernetes-security/) — orquestación
3. [`ci-cd-security/`](./ci-cd-security/) — el pipeline que une todo
4. [`secret-scanning/`](./secret-scanning/) + [`sast-dast/`](./sast-dast/) — los escáneres del pipeline

---

## ⚖️ Aviso

Todos los pipelines se prueban en repositorios propios y entornos de laboratorio.

---

**[⬅ Volver al área de Seguridad de la Información](../README.md)**
