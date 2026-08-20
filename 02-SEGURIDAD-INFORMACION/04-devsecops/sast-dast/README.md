# 🔍 SAST y DAST — Guía profesional

> **Nivel:** Avanzado · **Herramientas:** Semgrep, CodeQL, Bandit (SAST) · OWASP ZAP (DAST)
>
> Objetivo: detectar vulnerabilidades **en el código** (SAST) y **en la app corriendo** (DAST). Son complementarios, no intercambiables.

---

## Índice

1. [SAST vs DAST (y cuándo cada uno)](#1-sast-vs-dast-y-cuándo-cada-uno)
2. [SAST: Semgrep](#2-sast-semgrep)
3. [SAST: CodeQL](#3-sast-codeql)
4. [SAST: Bandit (Python)](#4-sast-bandit-python)
5. [DAST: OWASP ZAP](#5-dast-owasp-zap)
6. [Referencias](#6-referencias)

---

## 1. SAST vs DAST (y cuándo cada uno)

| | SAST | DAST |
|---|---|---|
| **Analiza** | Código fuente (sin ejecutar) | App ejecutándose |
| **Detecta** | SQLi, XSS, hardcoded secrets, lógica | Configs, runtime, auth rota |
| **Etapa** | Early (al escribir código) | Staging/prod |
| **Falsos positivos** | Más | Menos |
| **Requiere** | Acceso al código | URL de la app |

> **Regla:** SAST en cada PR (rápido, barato), DAST en staging (periódico). Juntos cubren el ciclo.

---

## 2. SAST: Semgrep

Semgrep busca **patrones de código** (reglas) y es muy rápido:

```bash
# Instalar
pip install semgrep

# Escanear con reglas por defecto
semgrep --config auto .

# Escanear con reglas específicas (p.ej. OWASP Top 10)
semgrep --config "p/owasp-top-ten" .

# En CI (usa la config del repo + PR diffs)
semgrep ci
```

Ejemplo de regla Semgrep propia (detectar SQL concat):

```yaml
rules:
  - id: sql-string-concat
    message: "SQL construida por concatenación — usa parámetros"
    severity: ERROR
    languages: [python]
    patterns:
      - pattern: cursor.execute("..." + $X)
```

---

## 3. SAST: CodeQL

CodeQL hace **análisis de flujo de datos** (dataflow), más profundo que Semgrep:

```yaml
# .github/workflows/codeql.yml (fragmento)
- uses: github/codeql-action/init@v3
  with:
    languages: python, javascript
- run: make build
- uses: github/codeql-action/analyze@v3
```

> CodeQL rastrea datos "sucios" (user input) hasta lugares "peligrosos" (SQL, eval), detectando inyecciones que una simple regex no ve.

---

## 4. SAST: Bandit (Python)

Bandit escanea código Python por malas prácticas de seguridad:

```bash
pip install bandit
bandit -r . -f json -o bandit.json

# Solo errores de severidad alta/media
bandit -r . -ll
```

Detecta: `pickle` inseguro, `eval`, `subprocess` con shell=True, passwords hardcodeados, etc.

---

## 5. DAST: OWASP ZAP

ZAP ataca la app **desde fuera**, como un atacante real.

### 5.1 Levantar ZAP y escanear

```bash
# Con Docker
docker run -t owasp/zap2docker-stable zap-baseline.py -t http://miapp.com -r report.html
```

### 5.2 Modos de escaneo

| Modo | Uso | Velocidad |
|---|---|---|
| `zap-baseline.py` | Escaneo pasivo (spider + checks pasivos) | Minutos |
| `zap-full-scan.py` | Escaneo activo completo | Horas |
| `zap-api-scan.py` | Escanear una API (OpenAPI/Swagger) | Minutos |

### 5.3 Escanear una API

```bash
docker run -t owasp/zap2docker-stable zap-api-scan.py \
  -t http://miapp.com/openapi.json -f openapi -r api-report.html
```

### 5.4 Integrar en el pipeline

```yaml
- name: DAST ZAP
  run: |
    docker run -t owasp/zap2docker-stable zap-baseline.py \
      -t http://staging.miapp.com \
      -r zap-report.html \
      -I   # -I = ignorar warnings, fallar solo con errores
```

---

## 6. Referencias

- [Semgrep](https://semgrep.dev/) · [CodeQL](https://codeql.github.com/)
- [Bandit](https://bandit.readthedocs.io/)
- [OWASP ZAP](https://www.zaproxy.org/) · [ZAP Docker](https://www.zaproxy.org/docs/docker/)

---

**[← Secret Scanning](../secret-scanning/)** · **[⬅ Volver al módulo DevSecOps](../README.md)**
