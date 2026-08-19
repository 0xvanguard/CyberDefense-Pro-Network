<div align="center">

# 🔐 Seguridad de la Información y Datos

**CISSP Domain · Asset Security & Cryptography**

*"Los datos son el nuevo petróleo — y el nuevo objetivo."*

![Tier](https://img.shields.io/badge/tier%20salarial-B%2FA-blue) ![Demanda](https://img.shields.io/badge/demanda-creciente-green) ![Entry](https://img.shields.io/badge/entry%20level-medio-yellow)

</div>

---

## 📋 Descripción

Rama enfocada en **proteger los datos a lo largo de su ciclo de vida**: clasificación, cifrado en reposo / tránsito / uso, prevención de fugas (DLP), gestión de identidades y accesos (IAM), y gestión de claves (KMS/HSM).

Es transversal — toca compliance (GDPR, HIPAA, Ley 1581), arquitectura, nube y desarrollo. Con la presión regulatoria de 2024-2026 (DORA en UE, NIS2, CCPA expansion) la demanda **se está disparando**, especialmente perfiles que combinan técnico + regulatorio.

---

## 👤 Roles típicos

- **Data Security Engineer** — implementación de DLP, cifrado, clasificación
- **IAM Engineer** — IdP, SSO, MFA, PAM, lifecycle
- **Encryption / KMS Specialist** — diseño de gestión de claves
- **Privacy Engineer** *(emergente)* — privacy by design, PETs
- **Insider Threat Analyst** — UEBA, detección interna

---

## 🛠️ Stack y herramientas

| Categoría | Herramientas |
|---|---|
| **DLP** | Microsoft Purview · Symantec DLP · Forcepoint · Netskope · Trellix |
| **Clasificación** | Microsoft Information Protection · Varonis · BigID · Spirion |
| **IAM / SSO** | Okta · Microsoft Entra ID · Auth0 · Keycloak · ForgeRock · Ping |
| **PAM** | CyberArk · BeyondTrust · Delinea (Thycotic) · HashiCorp Boundary |
| **KMS / Vault** | HashiCorp Vault · AWS KMS · Azure Key Vault · GCP KMS · YubiHSM |
| **Cifrado** | OpenSSL · age · GPG · Tink · libsodium · Microsoft BitLocker · LUKS |
| **UEBA** | Exabeam · Securonix · Microsoft Sentinel UEBA · Splunk UBA |
| **Database security** | Imperva · Oracle Audit Vault · MongoDB Atlas encryption |

---

## 🎓 Certificaciones recomendadas

| Nivel | Certificación | Vendor | Costo (USD) | Notas |
|---|---|---|---|---|
| Entry | CompTIA Security+ | CompTIA | ~$400 | Base general |
| Entry | Microsoft SC-900 | Microsoft | ~$100 | Muy buena para arrancar |
| Mid | CDPSE | ISACA | ~$575 | Privacy + ingeniería |
| Mid | CIPM / CIPP/E | IAPP | ~$550 ea | Privacy management |
| Mid | Okta Certified Professional / Admin | Okta | ~$150-300 | IAM enterprise |
| Senior | CISSP | (ISC)² | ~$750 | Exige 5y de experiencia |
| Senior | CCSP | (ISC)² | ~$600 | Cloud + datos |

---

## 🗺️ Roadmap (12 meses)

### Fase 1 — Fundamentos (0-3 meses)
- [ ] Conceptos: simétrico vs asimétrico, hash, KDFs, TLS handshake
- [ ] Diferenciar AT REST / IN TRANSIT / IN USE (homomorphic, confidential computing)
- [ ] OWASP Cryptographic Storage Cheat Sheet aplicado en un proyecto
- [ ] Lab: HashiCorp Vault local + dev mode

### Fase 2 — Especialización (3-6 meses)
- [ ] Microsoft Purview o Forcepoint DLP en sandbox
- [ ] IAM lifecycle: Okta o Keycloak con SSO + MFA + SCIM
- [ ] KMS con AWS KMS: encryption context + key rotation
- [ ] CDPSE o CIPP aprobado

### Fase 3 — Profesional (6-12 meses)
- [ ] Implementar PAM básico (Vault Boundary o BeyondTrust)
- [ ] Diseñar matriz de clasificación de datos para una org real
- [ ] CISSP o CCSP empezado
- [ ] Caso de uso documentado: DLP + IAM en pipeline real

---

## 💰 Salarios en Colombia (USD/mes)

| Nivel | Local 🇨🇴 | Remoto 🌎 | Notas |
|---|---|---|---|
| Junior (0-2 años) | $700 - $1,400 | $1,300 - $2,500 | IAM jr es entrada amigable |
| Mid (2-5 años) | $1,800 - $3,500 | $3,200 - $6,000 | DLP + IAM senior es nicho caro |
| Senior (5+ años) | $4,500 - $8,500 | $7,000 - $13,000 | Privacy Engineer remoto = top |

> **Tip:** combinar técnico (Vault/KMS) + regulatorio (CDPSE/CIPP) duplica el rango.

---

## 🔗 Conexión con otras ramas

- **`cryptographer`** → primitivas, mientras tú haces aplicación práctica
- **`grc-compliance`** → política y regulaciones que te guían
- **`data-protection-officer`** *(02)* → tu jefe natural en GRC
- **`seguridad-nube`** → KMS, IAM y DLP nativos cloud
- **`privacy-engineer`** *(02)* → solapamiento técnico-regulatorio

---

## 📂 Estructura

```
seguridad-informacion-datos/
├── herramientas/    # Configs de Vault, Purview, Okta, etc.
├── recursos/        # Standards (FIPS 140-3, NIST 800-57), cheatsheets
├── laboratorios/    # Vault + KMS + DLP en compose
└── casos-uso/       # Migración de claves, DLP en pyme, IAM zero trust
```

---

<div align="center">

**[⬅ Volver a Ciberseguridad](../README.md)**

</div>
