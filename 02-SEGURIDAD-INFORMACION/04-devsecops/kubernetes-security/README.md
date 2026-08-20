# ☸️ Seguridad de Kubernetes — Guía profesional

> **Nivel:** Avanzado · **Herramientas:** kubectl, Kubescape, kube-bench, Falco, OPA/Gatekeeper, Kyverno
>
> Objetivo: asegurar el cluster en las **4 C** de Kubernetes: **C**loud, **C**luster, **C**ontainer y **C**ode.

---

## Índice

1. [Las 4 C de Kubernetes](#1-las-4-c-de-kubernetes)
2. [RBAC (control de acceso)](#2-rbac-control-de-acceso)
3. [Seguridad de Pods (securityContext)](#3-seguridad-de-pods-securitycontext)
4. [Network Policies](#4-network-policies)
5. [Secretos (no en texto plano)](#5-secretos-no-en-texto-plano)
6. [Detección en runtime (Falco)](#6-detección-en-runtime-falco)
7. [Policy as code (OPA/Kyverno)](#7-policy-as-code-opakyverno)
8. [Auditoría y escaneo (kube-bench, Kubescape)](#8-auditoría-y-escaneo-kube-bench-kubescape)
9. [Referencias](#9-referencias)

---

## 1. Las 4 C de Kubernetes

```
┌─────────────────────────────────────────┐
│ Cloud      → red, IAM, cifrado del CSP  │
│  Cluster   → RBAC, admission, secrets   │
│   Container → imágenes, no-root, límites │
│    Code     → SAST, SCA, IaC scan       │
└─────────────────────────────────────────┘
```

> Cada capa es una barrera. Si falla una, las demás te salvan.

---

## 2. RBAC (control de acceso)

Principio: **least privilege** para cada ServiceAccount.

### 2.1 Role mínimo (solo leer pods de un namespace)

```yaml
apiVersion: rbac.authorization.k8s.io/v1
kind: Role
metadata:
  namespace: default
  name: pod-reader
rules:
- apiGroups: [""]
  resources: ["pods"]
  verbs: ["get", "list"]
```

### 2.2 Verificar permisos reales

```bash
# ¿Puede la serviceaccount "sa" listar secrets?
kubectl auth can-i list secrets --as=system:serviceaccount:default:sa
```

> **Auditoría clave:** busca `RoleBindings` que den `cluster-admin` a cuentas que no lo necesitan.

---

## 3. Seguridad de Pods (securityContext)

### 3.1 Pod seguro

```yaml
apiVersion: v1
kind: Pod
metadata:
  name: app-segura
spec:
  securityContext:
    runAsNonRoot: true
    runAsUser: 10001
    seccompProfile:
      type: RuntimeDefault
  containers:
  - name: app
    image: miapp:latest
    securityContext:
      allowPrivilegeEscalation: false
      readOnlyRootFilesystem: true
      capabilities:
        drop: ["ALL"]
```

### 3.2 Pod Security Standards (Admission)

K8s define 3 niveles: **privileged** → **baseline** → **restricted**. Aplica el más estricto:

```yaml
apiVersion: v1
kind: Namespace
metadata:
  name: produccion
  labels:
    pod-security.kubernetes.io/enforce: restricted
    pod-security.kubernetes.io/warn: baseline
```

> Meta profesional: **`restricted`** en producción. Bloquea pods privilegiados, root y sin seccomp.

---

## 4. Network Policies

Por defecto, **todo pod habla con todo**. Las Network Policies aplican **deny por defecto + allowlist**:

```yaml
apiVersion: networking.k8s.io/v1
kind: NetworkPolicy
metadata:
  name: deny-all
spec:
  podSelector: {}          # todos los pods
  policyTypes: [Ingress, Egress]

---
apiVersion: networking.k8s.io/v1
kind: NetworkPolicy
metadata:
  name: allow-solo-db
spec:
  podSelector:
    matchLabels: { app: db }
  ingress:
  - from:
    - podSelector:
        matchLabels: { app: backend }
    ports:
    - port: 5432
```

> Necesitas un CNI que las soporte (Calico, Cilium). Cilium añade inspección L7 (HTTP, DNS).

---

## 5. Secretos (no en texto plano)

Los `Secret` nativos están **solo codificados en base64** (no cifrados). Buenas prácticas:

```yaml
# ❌ secret hardcodeado en el manifiesto
stringData:
  password: "supersecreto"

# ✅ referencia a un gestor externo (External Secrets Operator / Vault)
apiVersion: external-secrets.io/v1beta1
kind: ExternalSecret
metadata:
  name: db-credentials
spec:
  secretStoreRef:
    name: vault-backend
    kind: SecretStore
  target:
    name: db-credentials
  data:
  - secretKey: password
    remoteRef:
      key: secret/db
      property: password
```

> Alternativas: **External Secrets Operator**, **Sealed Secrets** o **HashiCorp Vault**. Nunca commits de secretos.

---

## 6. Detección en runtime (Falco)

**Falco** detecta comportamiento anómalo en tiempo real (llamadas al kernel):

```bash
# Instalar vía Helm
helm repo add falcosecurity https://falcosecurity.github.io/charts
helm install falco falcosecurity/falco

# Reglas por defecto detectan: exec en contenedor, escritura en /etc, shells inesperados
kubectl logs -l app=falco
```

Ejemplos de lo que Falco alerta:

```text
"Shell in a container"               → alguien abrió una shell en el pod
"Write below /etc"                   → modificación de config
"Contact K8s API from container"     → el pod intenta tocar la API
```

---

## 7. Policy as code (OPA/Kyverno)

Bloquea configuraciones inseguras **antes** de que se desplieguen (admission control).

### 7.1 Kyverno (más simple, nativo YAML)

```yaml
apiVersion: kyverno.io/v1
kind: ClusterPolicy
metadata:
  name: require-non-root
spec:
  validationFailureAction: Enforce
  rules:
  - name: check-root
    match:
      any:
      - resources:
          kinds: [Pod]
    validate:
      message: "Los pods deben correr como non-root"
      pattern:
        spec:
          securityContext:
            runAsNonRoot: true
```

### 7.2 OPA/Gatekeeper (rego)

```rego
# ConstraintTemplate: bloquea pods con privilegios
package k8srequiredlabels
violation[{"msg": msg}] {
  input.review.object.spec.containers[c].securityContext.privileged
  msg := "Pods privilegiados no permitidos"
}
```

---

## 8. Auditoría y escaneo (kube-bench, Kubescape)

### 8.1 kube-bench (CIS Kubernetes Benchmark)

```bash
# Ejecutar contra el cluster
docker run --pid=host -v /etc:/etc:ro -v /var:/var:ro -t aquasec/kube-bench:latest --version 1.8
```

### 8.2 Kubescape (postura + cumplimiento)

```bash
# Escanear el cluster contra marcos (NSA, MITRE, CIS)
kubescape scan --submit=false
kubescape scan framework nsa
```

> **Entregable:** reporte de postura del cluster + correcciones aplicadas + políticas Kyverno/OPA desplegadas.

---

## 9. Referencias

- [Kubernetes Security (oficial)](https://kubernetes.io/docs/concepts/security/)
- [CIS Kubernetes Benchmark](https://www.cisecurity.org/benchmark/kubernetes)
- [Falco](https://falco.org/) · [Kyverno](https://kyverno.io/) · [OPA/Gatekeeper](https://open-policy-agent.github.io/gatekeeper/)
- [Kubescape](https://github.com/kubescape/kubescape)

---

**[⬅ Docker Security](../docker-security/)** · **[→ CI/CD Security](../ci-cd-security/)**
