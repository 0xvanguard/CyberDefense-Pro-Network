# 🔑 Secret Scanning — Guía profesional

> **Nivel:** Avanzado · **Herramientas:** Gitleaks, TruffleHog, detect-secrets
>
> Objetivo: detectar secretos (API keys, passwords, tokens) **antes** de que entren al repositorio. Un secreto commiteado es un incidente, no un aviso.

---

## Índice

1. [Por qué los secretos en git son críticos](#1-por-qué-los-secretos-en-git-son-críticos)
2. [Gitleaks (el estándar)](#2-gitleaks-el-estándar)
3. [TruffleHog (verificación)](#3-trufflehog-verificación)
4. [Pre-commit (bloquear antes del commit)](#4-pre-commit-bloquear-antes-del-commit)
5. [Qué hacer si un secreto se filtró](#5-qué-hacer-si-un-secreto-se-filtró)
6. [Referencias](#6-referencias)

---

## 1. Por qué los secretos en git son críticos

- El historial de git **conserva todo para siempre** (incluso si borras el commit).
- Los atacantes **escanean GitHub** en tiempo real buscando keys válidas.
- Un `AWS_ACCESS_KEY` filtrado = facturación + exfiltración en minutos.

> **Regla:** los secretos **nunca** van en el repo. Van en un gestor (Vault, AWS Secrets Manager) o en variables de entorno del CI.

---

## 2. Gitleaks (el estándar)

### 2.1 Instalar

```bash
# macOS
brew install gitleaks
# Linux (binario)
curl -sSfL https://github.com/gitleaks/gitleaks/releases/latest/download/gitleaks-linux-amd64 -o gitleaks
chmod +x gitleaks && sudo mv gitleaks /usr/local/bin/
```

### 2.2 Escanear el repo

```bash
# Escanear commits (historial completo)
gitleaks detect --source . --report-path gitleaks-report.json

# Escanear solo el working tree (sin historial)
gitleaks protect --source .

# Verificar un resultado
gitleaks detect -v
```

### 2.3 Config personalizada (`.gitleaks.toml`)

```toml
# Regla custom para un token interno
[[rules]]
id = "mi-token-interno"
description = "Token de la API interna"
regex = '''AKIA[0-9A-Z]{16}'''
[[rules.entropies]]
Min = "3.5"
Max = "8"
```

---

## 3. TruffleHog (verificación)

TruffleHog va más allá de la regex: **verifica si el secreto está vivo**:

```bash
# Escanear un repo remoto
trufflehog github --org=mi-org

# Escanear un repo local (con verificación)
trufflehog filesystem . --only-verified
```

> `--only-verified` muestra solo secretos que TruffleHog pudo **validar contra el servicio** (evita falsos positivos).

---

## 4. Pre-commit (bloquear antes del commit)

### 4.1 Con pre-commit framework

```bash
pip install pre-commit
```

`.pre-commit-config.yaml`:

```yaml
repos:
  - repo: https://github.com/gitleaks/gitleaks
    rev: v8.18.0
    hooks:
      - id: gitleaks
```

```bash
pre-commit install          # se ejecuta en cada commit
pre-commit run --all-files  # o manual
```

> Si un hook pre-commit encuentra un secreto, **bloquea el commit**. Combinado con el escaneo en CI (por si alguien salta el hook), tienes doble barrera.

---

## 5. Qué hacer si un secreto se filtró

Si YA se commiteó un secreto:

```
1. REVOCAR/ROTAR el secreto INMEDIATAMENTE (lo primero, sin excepción).
2. Confirmar que no fue usado (logs del proveedor).
3. Borrar del historial (git filter-repo / BFG) si es posible.
4. Avisar al equipo de seguridad.
```

> ⚠️ **Rotar primero, limpiar después.** Un secreto commiteado debe tratarse como comprometido, aunque lo borres del repo.

---

## 6. Referencias

- [Gitleaks](https://github.com/gitleaks/gitleaks)
- [TruffleHog](https://github.com/trufflesecurity/trufflehog)
- [GitHub secret scanning (oficial)](https://docs.github.com/en/code-security/secret-scanning)

---

**[← CI/CD Security](../ci-cd-security/)** · **[→ SAST/DAST](../sast-dast/)** · **[⬅ Volver al módulo](../README.md)**
