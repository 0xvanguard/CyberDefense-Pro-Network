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

## ✏️ Ejercicios prácticos

### Ejercicio 1: Juega con hashes (10 min)

```bash
# 1. Calcula hash de un texto
echo -n "hola" | sha256sum
# Anota el hash

echo -n "hola." | sha256sum
# ¡Cambia completamente! Solo un punto.

# 2. Crea un archivo y verifícalo
echo "contenido secreto" > secreto.txt
sha256sum secreto.txt > secreto.sha256

# Modifica el archivo
echo "contenido modificado" > secreto.txt

# Verifica (debería fallar)
sha256sum -c secreto.sha256
# Output: secreto.txt: FAILED

# 3. Compara algoritmos
echo "test" | md5sum
echo "test" | sha1sum
echo "test" | sha256sum
# ¡Diferentes tamaños, misma entrada!
```

**Pregunta:** ¿Por qué MD5 es inseguro si produce un hash "único"?

### Ejercicio 2: Cifrado simétrico (15 min)

```bash
# 1. Crea un mensaje secreto
echo "Este es mi secreto: 12345" > secreto.txt

# 2. Cifra con AES-256-GCM
openssl enc -aes-256-gcm -salt -in secreto.txt -out secreto.enc -pbkdf2
# Te pedirá una contraseña

# 3. Intenta leerlo
cat secreto.enc
# ¡Solo ves caracteres raros!

# 4. Descifra
openssl enc -d -aes-256-gcm -in secreto.enc -out secreto_descifrado.txt -pbkdf2

# 5. Verifica
cat secreto_descifrado.txt
# ¡El mensaje original!

# 6. Prueba sin contraseña (contraseña vacía)
openssl enc -aes-256-gcm -in secreto.txt -out secreto2.enc -pbkdf2 -pass pass:
openssl enc -d -aes-256-gcm -in secreto2.enc -out secreto2.txt -pbkdf2 -pass pass:
cat secreto2.txt
```

**Pregunta:** ¿Qué pasa si no usas `-pbkdf2`? ¿Es seguro?

### Ejercicio 3: Cifrado asimétrico (15 min)

```bash
# 1. Genera un par de claves RSA
openssl genpkey -algorithm RSA -out private_key.pem -pkeyopt rsa_keygen_bits:2048
openssl rsa -pubout -in private_key.pem -out public_key.pem

# 2. Cifra con la pública
echo "Mensaje secreto para ti" > mensaje.txt
openssl pkeyutl -encrypt -pubin -inkey public_key.pem -in mensaje.txt -out mensaje_cifrado.bin

# 3. Descifra con la privada
openssl pkeyutl -decrypt -inkey private_key.pem -in mensaje_cifrado.bin -out mensaje_descifrado.txt

# 4. Verifica
cat mensaje_descifrado.txt
```

### Ejercicio 4: Firma digital (10 min)

```bash
# 1. Firma un archivo con tu clave privada
openssl dgst -sha256 -sign private_key.pem -out firma.bin secreto.txt

# 2. Verifica la firma con la pública
openssl dgst -sha256 -verify public_key.pem -signature firma.bin secreto.txt
# Output: Verified OK

# 3. Modifica el archivo y verifica de nuevo
echo "modificado" >> secreto.txt
openssl dgst -sha256 -verify public_key.pem -signature firma.bin secreto.txt
# Output: Verification Failure
```

### Ejercicio 5: Certificados SSL (10 min)

```bash
# 1. Crea un certificado auto-firmado
openssl req -x509 -newkey rsa:2048 -keyout key.pem -out cert.pem -days 365 -nodes
# Llena los campos (Country, State, etc.)

# 2. Examina el certificado
openssl x509 -in cert.pem -text -noout
# Mira: Subject, Issuer, Validity, Public Key

# 3. Verifica un cert real
echo | openssl s_client -connect github.com:443 2>/dev/null | openssl x509 -noout -subject -issuer -dates
```

### Ejercicio 6: Rompe un hash (10 min)

```bash
# 1. Crea un hash MD5 débil
echo -n "password" | md5sum > hash.txt

# 2. Usa hashcat o john para romperlo
# Con john:
john --format=raw-md5 --wordlist=/usr/share/wordlists/rockyou.txt hash.txt

# Si no tienes rockyou.txt:
apt install wordlists
zcat /usr/share/wordlists/rockyou.txt.gz > rockyou.txt

# 3. ¿Cuánto tardó? ¿Encontró la contraseña?
```

**Pregunta:** ¿Por qué contraseñas como "password" se rompen en segundos?

### Ejercicio 7: SSH seguro (10 min)

```bash
# 1. Genera claves Ed25519 (más seguro que RSA)
ssh-keygen -t ed25519 -C "miemail@ejemplo.com"

# 2. Mira tu clave pública
cat ~/.ssh/id_ed25519.pub

# 3. Copia al servidor
ssh-copy-id usuario@servidor

# 4. Deshabilita login por contraseña en el servidor
# En /etc/ssh/sshd_config:
# PasswordAuthentication no
# PermitRootLogin no

# 5. Reinicia SSH
sudo systemctl restart sshd
```

> ⏭️ **Siguiente:** [`06-vulnerabilidades.md`](./06-vulnerabilidades.md) — qué es una vulnerabilidad y cómo se clasifica.
