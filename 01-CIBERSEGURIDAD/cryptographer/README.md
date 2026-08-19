<div align="center">

# 🔢 Cryptographer

**NIST NICE · Cryptographic Specialist**

*"La criptografía no es magia. Pero implementarla mal, sí maldice tu producto."*

![Tier](https://img.shields.io/badge/tier%20salarial-S-purple) ![Demanda](https://img.shields.io/badge/demanda-baja%20pero%20premium-orange) ![Entry](https://img.shields.io/badge/entry%20level-experto-critical)

</div>

---

## 📋 Descripción

Rol **académico-aplicado**. Diseña y/o evalúa primitivas criptográficas, protocolos seguros y sus implementaciones. Cubre desde análisis de side-channel hasta diseño post-cuántico (PQC), pasando por TLS hardening, hash functions, KDFs, MPC, ZKPs y homomorphic encryption.

**Es de los nichos más escasos y mejor pagados**. Salidas: investigación, fintech/cripto, defensa, big tech (security teams), startups PQC. Suele requerir maestría/PhD en matemáticas o CS — pero también hay engineers self-taught con foco aplicado (libsodium, Tink, age).

---

## 👤 Roles típicos

- **Applied Cryptographer** — implementación segura en producto
- **Cryptography Researcher** — academia / labs / Big Tech research
- **Crypto Engineer** *(crypto-currency)* — fintech, blockchain
- **PQC Migration Engineer** *(emergente)* — NIST PQC standardization
- **Hardware Security / HSM Engineer** — Yubico, Thales, Entrust

---

## 🛠️ Stack y herramientas

| Categoría | Herramientas / libs |
|---|---|
| **Libraries seguras** | libsodium · Google Tink · BouncyCastle · NaCl · ring (Rust) |
| **Modernas low-level** | RustCrypto · age · OpenSSL 3.x · BoringSSL |
| **Análisis** | CryptoVerif · ProVerif · Tamarin · EasyCrypt |
| **PQC** | liboqs · CRYSTALS-Kyber · CRYSTALS-Dilithium · SPHINCS+ |
| **HSM / KMS** | YubiHSM · Thales Luna · AWS CloudHSM · Microsoft HSM |
| **Side-channel** | ChipWhisperer · power analysis tools |
| **CTF tools** | RsaCtfTool · CyberChef · sage · pycryptodome |
| **Standards** | NIST FIPS 140-3 · NIST PQC · RFC 8446 (TLS 1.3) · IETF drafts |
| **Audit / formal** | TLS-N · Project Wycheproof · Cryptol |

---

## 🎓 Certificaciones / formación

| Nivel | Vía | Costo | Notas |
|---|---|---|---|
| Entry | Cryptography I/II (Coursera, Dan Boneh) | $0-50 | **Imprescindible** |
| Entry | Cryptopals challenges | $0 | Learn-by-breaking, mejor recurso |
| Mid | EC-Council ECES *(básica)* | ~$700 | Limitada pero da papelito |
| Mid | Real-world Crypto (libro) | ~$60 | David Wong, gold standard |
| Senior | Maestría aplicada (CS / matemáticas) | $$$ | Para investigación |
| Senior | Publicaciones IACR / contribuciones a NIST PQC | $0 | Reputación >> certificación |

---

## 🗺️ Roadmap (12 meses)

### Fase 1 — Fundamentos (0-3 meses)
- [ ] Cryptography I (Boneh) completado
- [ ] Cryptopals sets 1-3 resueltos
- [ ] Lectura *Real-World Cryptography* de David Wong
- [ ] Implementar (no usar) AES, SHA-256 para entender (educativo, **nunca prod**)

### Fase 2 — Especialización (3-6 meses)
- [ ] Cryptopals 4-6
- [ ] TLS 1.3 a nivel de wire (Wireshark + draft RFC 8446)
- [ ] PQC: implementar Kyber con liboqs
- [ ] Side-channel intro con ChipWhisperer (lab si tienes hw)

### Fase 3 — Profesional (6-12 meses)
- [ ] Cryptopals 7-8 (avanzados, ECC + lattice)
- [ ] Audit cripto a un proyecto open source (reporte público)
- [ ] Contribución a libsodium / RustCrypto / age
- [ ] Charla técnica o paper (workshop IACR / Real World Crypto)

---

## 💰 Salarios en Colombia (USD/mes)

| Nivel | Local 🇨🇴 | Remoto 🌎 | Notas |
|---|---|---|---|
| Junior (0-2 años) | $1,000 - $2,000 | $2,000 - $4,000 | Casi siempre vía academia |
| Mid (2-5 años) | $2,500 - $5,000 | $5,000 - $9,000 | Crypto eng en fintech |
| Senior (5+ años) | $6,000 - $12,000 | $11,000 - $22,000 | PQC + research = top mundial |

> **Tip:** este nicho está **3-5× sobre el promedio**. Pero exige profundidad real — no se finge con un curso de 6 semanas.

---

## 🔗 Conexión con otras ramas

- **`seguridad-informacion-datos`** → tú haces el primitivo, ellos lo aplican
- **`seguridad-cadena-suministro`** → firma de artefactos (Cosign, Sigstore)
- **`malware-analyst`** → reverse de cripto en samples
- **`pentester-red-team`** → CTF crypto challenges
- **`ai-security`** → privacy-preserving ML (FHE, MPC) overlap creciente

---

## 📂 Estructura

```
cryptographer/
├── herramientas/    # Notebooks pycryptodome/sage, scripts Cryptopals
├── recursos/        # Boneh notes, Real-World Crypto chapters
├── laboratorios/    # Cryptopals progress, PQC playground
└── casos-uso/       # Audits cripto, vulns descubiertas, papers leídos
```

---

<div align="center">

**[⬅ Volver a Ciberseguridad](../README.md)**

</div>
