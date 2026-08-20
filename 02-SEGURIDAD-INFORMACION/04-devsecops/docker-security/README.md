# 🐳 Seguridad de Contenedores (Docker) — Guía profesional

> **Nivel:** Avanzado · **Herramientas:** Docker, Trivy, Grype, Cosign
>
> Objetivo: construir y ejecutar contenedores **seguros**, no solo "que funcionen". Un contenedor mal configurado es un vector de escape al host.

---

## Índice

1. [El modelo de amenaza del contenedor](#1-el-modelo-de-amenaza-del-contenedor)
2. [Hardening del Dockerfile](#2-hardening-del-dockerfile)
3. [Escaneo de imágenes (Trivy/Grype)](#3-escaneo-de-imágenes-trivygrype)
4. [Hardening en runtime](#4-hardening-en-runtime)
5. [Firma de imágenes (Cosign)](#5-firma-de-imágenes-cosign)
6. [Auditoría (Docker Bench)](#6-auditoría-docker-bench)
7. [Referencias](#7-referencias)

---

## 1. El modelo de amenaza del contenedor

```
Atacante → app vulnerable dentro del contenedor
        ↓ (si el contenedor tiene privilegios/caps)
        → escape al HOST (kernel compartido)
```

> Los contenedores comparten el **kernel** con el host. La seguridad se logra con **capas**: imagen mínima + runtime restringido + escaneo + firma.

---

## 2. Hardening del Dockerfile

### 2.1 Dockerfile seguro (antes/después)

```dockerfile
# ❌ INSEGURO
FROM ubuntu:latest
RUN apt-get install -y nginx python3
COPY . /app
USER root
CMD ["python3", "/app/server.py"]
```

```dockerfile
# ✅ SEGURO
FROM python:3.12-slim AS builder
RUN pip install --no-cache-dir -r requirements.txt

FROM python:3.12-slim
# Usuario no-root
RUN useradd --create-home --uid 10001 appuser
USER appuser
# Copiar SOLO lo necesario del stage builder
COPY --from=builder /usr/local/lib/python3.12/site-packages /usr/local/lib/python3.12/site-packages
COPY --chown=appuser:appuser app/ /app/
WORKDIR /app
CMD ["python3", "server.py"]
```

### 2.2 Reglas de hardening del Dockerfile

| Regla | Por qué |
|---|---|
| Base **mínima** (`slim`, `alpine`, `distroless`) | Menos superficie de ataque |
| `USER` no-root | Si te comprometen, no eres root |
| **Multi-stage builds** | No dejes herramientas de build en la imagen final |
| Versiones **pineadas** (`python:3.12-slim`, no `latest`) | Reproducibilidad, sin sorpresas |
| `COPY` (no `ADD`) | `ADD` descarga URLs/extrae tarballs (riesgo) |
| Nada de secretos en `ARG`/`ENV` | Quedan en el historial de la imagen |
| `HEALTHCHECK` | Detección de estado |

> Usa **distroless** (Google) o **Chainguard images** para mínima superficie: sin shell, sin package manager.

---

## 3. Escaneo de imágenes (Trivy/Grype)

### 3.1 Trivy (escaneo de vulnerabilidades + IaC + secrets)

```bash
# Instalar
curl -sfL https://raw.githubusercontent.com/aquasecurity/trivy/main/contrib/install.sh | sh

# Escanear una imagen local
trivy image python:3.12-slim

# Escanear con detalle de severidad
trivy image --severity HIGH,CRITICAL miapp:latest

# Escanear el Dockerfile (misconfiguration)
trivy config ./Dockerfile

# Salida JSON para el pipeline
trivy image -f json -o report.json miapp:latest
```

### 3.2 Grype (alternativa)

```bash
grype miapp:latest
grype miapp:latest --fail-on high
```

> **Regla de pipeline:** falla el build si hay vulnerabilidades `CRITICAL` (o `HIGH` según tu política). Usa `--exit-code 1`.

---

## 4. Hardening en runtime

### 4.1 Flags de ejecución seguros

```bash
docker run \
  --user 10001 \                        # no-root
  --read-only \                         # filesystem solo lectura
  --cap-drop ALL \                      # quitar TODAS las capabilities
  --cap-add NET_BIND_SERVICE \          # añadir solo la necesaria
  --security-opt no-new-privileges \    # no escalar privilegios
  --memory 256m --cpus 0.5 \            # límites de recursos
  --tmpfs /tmp \                        # tmp efímero
  miapp:latest
```

### 4.2 Qué evitar SIEMPRE

```bash
# ❌ NUNCA en producción
docker run --privileged miapp          # acceso total al host
docker run -v /:/host miapp            # montar el host entero
docker run --pid=host miapp            # compartir PID del host
```

### 4.3 Docker Compose seguro

```yaml
services:
  app:
    image: miapp:latest
    user: "10001"
    read_only: true
    cap_drop:
      - ALL
    cap_add:
      - NET_BIND_SERVICE
    security_opt:
      - no-new-privileges:true
    tmpfs:
      - /tmp
    mem_limit: 256m
```

---

## 5. Firma de imágenes (Cosign)

Firma las imágenes para garantizar **integridad y procedencia** (supply chain):

```bash
# Generar keypair (una vez)
cosign generate-key-pair

# Firmar la imagen
cosign sign --key cosign.key miapp:latest

# Verificar la firma antes de desplegar
cosign verify --key cosign.pub miapp:latest
```

> Mejor aún: firma con **keyless** (Sigstore + OIDC) para no gestionar keys manualmente: `cosign sign` con proveedor de identidad.

---

## 6. Auditoría (Docker Bench)

**Docker Bench Security** audita el host y daemon contra el CIS Docker Benchmark:

```bash
git clone https://github.com/docker/docker-bench-security.git
cd docker-bench-security
sudo ./docker-bench-security.sh
# → reporte [WARN] / [PASS] / [INFO] por cada check CIS
```

Corrige los `WARN` y repite la auditoría.

---

## 7. Referencias

- [Dockerfile best practices (oficial)](https://docs.docker.com/build/building/best-practices/)
- [CIS Docker Benchmark](https://www.cisecurity.org/benchmark/docker)
- [Trivy](https://github.com/aquasecurity/trivy) · [Grype](https://github.com/anchore/grype)
- [Cosign / Sigstore](https://github.com/sigstore/cosign)

---

**[⬅ Volver al módulo DevSecOps](../README.md)** · **[→ Kubernetes Security](../kubernetes-security/)**
