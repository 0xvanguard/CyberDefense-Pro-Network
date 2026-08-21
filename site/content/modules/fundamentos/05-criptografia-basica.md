---
title: "05 — Criptografía básica"
---

# 05 — Criptografía básica

> 🎯 **Objetivo:** entender los conceptos suficientes para no meter la pata. No vas a ser criptoanalista hoy, pero sí vas a saber qué algoritmo usar, cuándo y por qué.

## 1. Las 3 cosas que la criptografía protege

- **Confidencialidad** — nadie más lee
- **Integridad** — nadie alteró sin permiso
- **Autenticidad** — séquién lo envió y que no fue alterado

## 2. Hash — la huella digital de un dato

Un **hash** toma cualquier cantidad de datos y devuelve una cadena fija de tamaño.

```
"hola"      → 4d...uo  (SHA-256)
"hola."     → d8...xq  (distinto aunque cambies 1 carácter)
```

**Propiedades:**
- Determinista: misma entrada → mismo hash
- Rápido de calcular
- Irreversible: del hash no recuperas la entrada
- Resistente a colisiones (casi imposible encontrar 2 entradas con mismo hash)

**Algoritmos comunes:**
| Algoritmo | Tamaño | Estado |
|---|---|---|
| MD5 | 128 bits | ❌ Roto. Solo para legacy. |
| SHA-1 | 160 bits | ❌ Roto. No uses. |
| SHA-256 | 256 bits | ✅ Estándar actual. |
| SHA-3 | 256+ bits | ✅ Más nuevo, alternativas. |
| BLAKE2 | variable | ✅ Muy rápido. |

**¿Para qué se usa un hash?**
- Guardar contraseñas: `hash(sal + password)` (no se guarda el password en claro)
- Verificar integridad de archivos (un checksum descargado)
- Firmas digitales (firmas sobre el hash, no el documento entero)
- Blockchain / Bitcoin

> ⚠️ **Error común**: usar SHA-256 directamente sobre la contraseña. Correcto es usar un algoritmo lento y con sal: **bcrypt, scrypt, Argon2** (ver `01-CIBERSEGURIDAD/08-criptografia/`).

```bash
# Calcular hash de un archivo
sha256sum archivo.txt          # Linux
Get-FileHash archivo.txt       # Windows PowerShell
```

## 3. Cifrado simétrico — misma clave para cifrar y descifrar

```
   ┌──── mensaje ────┐
        clave K
   └──── mismo K ────┘
   cifrado         descifrado
```

**Algoritmos recomendados:**
- **AES-256-GCM** — estándar de facto
- **ChaCha20-Poly1305** — alternativa moderna, móvil-friendly

**Problema:** ¿cómo compartes la clave sin que la intercepten?

## 4. Cifrado asimétrico — un par de claves (pública + privada)

```
  Clave pública (cualquiera la ve)
            ↓ cifra
        mensaje cifrado
            ↓ descifra con clave privada
        mensaje original

  Clave privada (solo tú)
```

**Algoritmos:**
- **RSA** — clásico, usa factores primos grandes
- **ECC / Curve25519** — más moderno, menor tamaño de clave
- **Ed25519** — para firmas digitales

**¿Para qué sirve?**
- Cifrar: cualquiera cifra con tu pública, solo tú descifras con tu privada
- Firmar: tú firmas con tu privada, cualquiera verifica con tu pública
- HTTPS usa esto para acordar una clave simétrica y luego todo va cifrado con AES

## 5. Firmas digitales — autenticidad

```
1. Hash del documento
2. Cifras el hash con tu clave privada → firma
3. Adjuntas firma al documento
4. Receptor: descifra la firma con tu pública → compara con hash del documento
   → si coinciden: íntegro y auténtico
```

## 6. Certificados y PKI

Un **certificado digital** (`X.509`) ata una identidad (ej: dominio `google.com`) a una clave pública. Lo firma una **CA (Certificate Authority)** de confianza (Let's Encrypt, DigiCert, etc.).

**Cadena de confianza:** tu certificado → CA intermedia → CA raíz (que tu navegador ya confía).

```bash
# Ver el certificado de una web
openssl s_client -connect github.com:443 -showcerts

# Extraer info
echo | openssl s_client -connect github.com:443 2>/dev/null | openssl x509 -noout -subject -issuer -dates
```

## 7. HTTPS — qué pasa realmente

1. **Tu navegador** → "Hola, quiero HTTPS"
2. **Servidor** → "Aquí mi certificado (clave pública)"
3. **Tu navegador** → verifica la cadena
4. Ambos acuerdan un **algoritmo** y generan una **clave simétrica** (TLS handshake)
5. A partir de ahí, todo va cifrado con AES (clave simétrica)

La asimétrica solo se usa al principio para acordar la clave simétrica. Luego va rápido porque AES es más eficiente.

## 8. Errores comunes que vas a ver (y debes reconocer)

| Error | Significado |
|---|---|
| `certificate expired` | El servidor忘记 renovar. O un atacante. |
| `self-signed certificate` | Servidor firmó su propio cert. Confiar = riesgo. |
| `hostname mismatch` | El cert es para otro dominio. Sospechoso. |
| `untrusted CA` | CA no está en la lista de CAs confiables. |
| `mixed content` | Página HTTPS carga recursos HTTP. Mal. |

## 9. Conceptos adicionales que vas a oír

- **Sal (salt)** — string aleatorio añadido al password antes de hashear. Evita rainbow tables.
- **PBKDF2 / bcrypt / scrypt / Argon2** — funciones de hash lentas a propósito para passwords.
- **Nonce** — número único por mensaje que evita replay attacks.
- **KDF** — Key Derivation Function: convierte una contraseña débil en clave criptográfica fuerte.
- **HSM** — Hardware Security Module: hardware dedicado a claves criptográficas.
- **Quantum-safe crypto** — Algoritmos resistentes a computación cuántica (CRYSTALS-Kyber, etc.).

## 📌 Dónde profundizar

| Tema | Carpeta |
|---|---|
| Cripto aplicada | [`01-CIBERSEGURIDAD/08-criptografia/`](../01-CIBERSEGURIDAD/08-criptografia/) |
| Seguridad de cadena de suministro | [`01-CIBERSEGURIDAD/seguridad-cadena-suministro/`](../01-CIBERSEGURIDAD/seguridad-cadena-suministro/) |
| Forense y descifrado | [`01-CIBERSEGURIDAD/forense-digital/`](../01-CIBERSEGURIDAD/forense-digital/) |
| Cryptographer role | [`01-CIBERSEGURIDAD/cryptographer/`](../01-CIBERSEGURIDAD/cryptographer/) |

## ✏️ Ejercicios

1. **Hash:** hashea dos archivos iguales y compara. Cambia un byte y vuelve a hashear. Mira cómo cambia completamente el hash.
2. **Cifrado simétrico:** cifra un mensaje tuyo con `openssl enc -aes-256-gcm -salt -in msg.txt -out msg.enc`. Descífralo.
3. **Genera claves SSH:** `ssh-keygen -t ed25519`. Mira tu pública (`cat ~/.ssh/id_ed25519.pub`).
4. **Verifica un cert:** visita `https://github.com`, click en el candado → mira "Connection is secure" → "Certificate is valid".

> ⏭️ **Siguiente:** [`06-vulnerabilidades.md`](./06-vulnerabilidades.md) — qué es una vulnerabilidad y cómo se clasifica.
