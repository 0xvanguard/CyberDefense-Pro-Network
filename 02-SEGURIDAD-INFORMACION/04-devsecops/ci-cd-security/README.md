# 🔄 Seguridad del Pipeline CI/CD — Guía profesional

> **Nivel:** Avanzado · **Herramientas:** GitHub Actions, Cosign, Syft, SLSA
>
> Objetivo: que el propio pipeline sea **seguro** (no solo que escanee el código). El pipeline es un objetivo de ataque de alto valor: si lo comprometes, comprometes todo lo que despliega.

---

## Índice

1. [El modelo de amenaza del pipeline](#1-el-modelo-de-amenaza-del-pipeline)
2. [Hardening del pipeline](#2-hardening-del-pipeline)
3. [OIDC (adiós a los secretos de larga vida)](#3-oidc-adiós-a-los-secretos-de-larga-vida)
4. [Supply chain: SLSA, SBOM y firma](#4-supply-chain-slsa-sbom-y-firma)
5. [Ejemplo de pipeline DevSecOps completo](#5-ejemplo-de-pipeline-devsecops-completo)
6. [Referencias](#6-referencias)

---

## 1. El modelo de amenaza del pipeline

```
Atacante → ¿repo comprometido? → ¿PR maliciosa? → ¿secrets en CI?
        → build → push imagen → deploy
```

Vectores típicos:

| Vector | Mitigación |
|---|---|
| Commit con secretos | Secret scanning (Gitleaks) |
| Dependencia maliciosa | SCA + pinning + SBOM |
| PR maliciosa | Revisión obligatoria + `pull_request_target` controlado |
| Token de CI filtrado | OIDC (sin secretos de larga vida) |
| Imagen alterada | Firma con Cosign + verificación |
| Build no reproducible | SLSA + provenance |

---

## 2. Hardening del pipeline

- [ ] **Ramas protegidas**: `main` solo acepta PRs con revisión aprobada.
- [ ] **Least privilege** en tokens del CI (scope mínimo).
- [ ] **No loggear secretos** (mascara `***` en logs).
- [ ] **Pin actions por SHA** (no por tag, para evitar que cambien).
- [ ] Workflows de `pull_request` **sin** acceso a secretos sensibles (usa `pull_request_target` solo si sabes lo que haces).
- [ ] Entornos separados (stage/prod) con aprobación manual para prod.

---

## 3. OIDC (adiós a los secretos de larga vida)

En vez de guardar un `AWS_ACCESS_KEY` en el repo, usa **OIDC** para que GitHub Actions asuma un rol temporal:

```yaml
# .github/workflows/deploy.yml (fragmento)
permissions:
  id-token: write        # necesario para OIDC
  contents: read

jobs:
  deploy:
    runs-on: ubuntu-latest
    steps:
      - uses: aws-actions/configure-aws-credentials@v4
        with:
          role-to-assume: arn:aws:iam::123456789012:role/github-actions-role
          aws-region: us-east-1
      # Sin llaves de larga vida: credenciales efímeras vía OIDC
```

> Configura el **trust policy** del rol AWS para aceptar solo el `sub` de tu repo (audience + subject). Lo mismo aplica a Azure (federated credentials) y GCP (Workload Identity Federation).

---

## 4. Supply chain: SLSA, SBOM y firma

### 4.1 SLSA (Supply-chain Levels for Software Artifacts)

| Nivel | Qué garantiza |
|---|---|
| **L1** | Build documentado (provenance) |
| **L2** | Build versionado + controlado (CI/CD con revisiones) |
| **L3** | Build **resistente** (aislado, reproducible) |
| **L4** | Máxima garantía (dos personas, revisión hermética) |

> Meta alcanzable para la mayoría: **SLSA L2-L3**.

### 4.2 SBOM (Software Bill of Materials)

```bash
# Generar SBOM con Syft
syft miapp:latest -o spdx-json > sbom.json

# También lo genera Trivy
trivy image --format cyclonedx miapp:latest > sbom.json
```

> El SBOM te dice **qué librerías hay dentro**, para responder rápido ante un CVE (ej. Log4Shell).

### 4.3 Firma de artefactos + provenance

```bash
# Firmar la imagen (keyless con OIDC)
cosign sign miapp:latest

# Firmar con attestation de la build (provenance)
cosign attest --predicate provenance.json --type slsaprovenance miapp:latest

# Verificar en el deploy
cosign verify --certificate-identity-regexp '.*' --certificate-oidc-issuer-regexp '.*' miapp:latest
```

---

## 5. Ejemplo de pipeline DevSecOps completo

```yaml
# .github/workflows/ci.yml
name: DevSecOps Pipeline
on:
  pull_request:
  push:
    branches: [main]

permissions:
  contents: read
  id-token: write

jobs:
  security:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
        with:
          fetch-depth: 0        # Gitleaks necesita el historial

      # 1. Secret scanning
      - name: Gitleaks
        uses: gitleaks/gitleaks-action@v2
        env:
          GITHUB_TOKEN: ${{ secrets.GITHUB_TOKEN }}

      # 2. SAST
      - name: Semgrep
        run: |
          pip install semgrep
          semgrep ci --config auto

      # 3. SCA (dependencias)
      - name: Trivy fs scan
        uses: aquasecurity/trivy-action@master
        with:
          scan-type: fs
          exit-code: 1
          severity: CRITICAL

      # 4. Build imagen
      - name: Build image
        run: docker build -t miapp:${{ github.sha }} .

      # 5. Escanear imagen
      - name: Trivy image scan
        uses: aquasecurity/trivy-action@master
        with:
          image: miapp:${{ github.sha }}
          exit-code: 1
          severity: HIGH,CRITICAL

      # 6. Firmar (solo en main)
      - name: Cosign sign
        if: github.ref == 'refs/heads/main'
        run: |
          cosign sign --yes miapp:${{ github.sha }}
          cosign attest --yes --type slsaprovenance miapp:${{ github.sha }}
```

> Flujo: **secretos → SAST → SCA → build → imagen → firma**. Cada paso falla el build si hay problema.

---

## 6. Referencias

- [GitHub Actions security hardening](https://docs.github.com/en/actions/security-guides/security-hardening-for-github-actions)
- [SLSA](https://slsa.dev/) · [Sigstore/Cosign](https://docs.sigstore.dev/)
- [Syft (SBOM)](https://github.com/anchore/syft)
- [OWASP CI/CD Security Cheat Sheet](https://cheatsheetseries.owasp.org/cheatsheets/CI_CD_Security_Cheat_Sheet.html)

---

**[⬅ Kubernetes Security](../kubernetes-security/)** · **[→ Secret Scanning](../secret-scanning/)** · **[⬅ Volver al módulo](../README.md)**
