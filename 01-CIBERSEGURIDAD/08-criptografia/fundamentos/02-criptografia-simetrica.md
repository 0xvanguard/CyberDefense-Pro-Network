# 🔑 Cifrado Simétrico

> *"El cifrado simétrico es como una cerradura con la misma llave: quien tiene la llave puede abrir y cerrar. El secreto está en la llave, no en la cerradura."*

---

## 📋 Tabla de contenido

1. [¿Qué es el cifrado simétrico?](#1-qué-es-el-cifrado-simétrico)
2. [DES y 3DES](#2-des-y-3des)
3. [AES (Advanced Encryption Standard)](#3-aes-advanced-encryption-standard)
4. [ChaCha20](#4-chacha20)
5. [Modos de operación](#5-modos-de-operación)
6. [Padding](#6-padding)
7: [Cifrado en la práctica](#7-cifrado-en-la-práctica)
8. [Defensa: mal uso de cifrado](#8-defensa-mal-uso-de-cifrado)
9. [Referencias](#9-referencias)

---

## 1. ¿Qué es el cifrado simétrico?

### Definición

El **cifrado simétrico** usa la **misma clave** para cifrar y descifrar:

```
Cifrado:   plaintext + clave → ciphertext
Descifrado: ciphertext + clave → plaintext
```

### Ventajas y desventajas

| Aspecto | Simétrico | Asimétrico |
|---|---|---|
| **Velocidad** | ⭐⭐⭐⭐⭐ Rápido | ⭐⭐ Lento |
| **Tamaño de clave** | 128-256 bits | 2048-4096 bits |
| **Problema** | Distribución de claves | No tiene |
| **Uso típico** | Datos, disco, tráfico | Intercambio de claves, firmas |

### Algoritmos principales

| Algoritmo | Clave | Bloque | Estado |
|---|---|---|---|
| **DES** | 56 bits | 64 bits | ❌ Inseguro |
| **3DES** | 168 bits | 64 bits | ⚠️ Deprecado |
| **AES** | 128/192/256 bits | 128 bits | ✅ Estándar |
| **ChaCha20** | 256 bits | Stream | ✅ Moderno |
| **Blowfish** | 32-448 bits | 64 bits | ⚠️ Legado |
| **Twofish** | 128-256 bits | 128 bits | ✅ Seguro |

---

## 2. DES y 3DES

### DES (Data Encryption Standard)

```
Clave: 56 bits (8 bits de paridad)
Bloque: 64 bits
Rondas: 16
Estado: ❌ INSEGURO (fuerza bruta en horas)
```

### 3DES (Triple DES)

```
Clave: 112 o 168 bits
Bloque: 64 bits
Operación: DES → DES⁻¹ → DES
Estado: ⚠️ DEPRECADO (NIST, 2023)
```

### Cifrar con 3DES (OpenSSL)

```bash
# Cifrar
openssl enc -des-ede3-cbc -in plaintext.txt -out ciphertext.bin -k "password123"

# Descifrar
openssl enc -des-ede3-cbc -d -in ciphertext.bin -out plaintext.txt -k "password123"
```

> **Nunca usar DES o 3DES en nuevos sistemas. Usar AES-256-GCM.**

---

## 3. AES (Advanced Encryption Standard)

### Especificaciones

| Parámetro | Valor |
|---|---|
| **Nombre** | Rijndael |
| **Bloque** | 128 bits (16 bytes) |
| **Claves** | 128, 192 o 256 bits |
| **Rondas** | 10, 12 o 14 |
| **NIST approval** | 2001 |
| **Estado actual** | ✅ Estándar internacional |

### Rondas de AES

```
1. AddRoundKey      → XOR con subclave
2. SubBytes         → Sustitución no lineal
3. ShiftRows        → Rotación de filas
4. MixColumns       → Mezcla de columnas
5. AddRoundKey      → XOR con subclave
... (repetir 9 veces)
10. AddRoundKey     → XOR con subclave final
```

### Cifrar con AES (OpenSSL)

```bash
# AES-256-GCM (RECOMENDADO: autenticado)
openssl enc -aes-256-gcm -in plaintext.txt -out ciphertext.bin -k "password123"

# Descifrar
openssl enc -aes-256-gcm -d -in ciphertext.bin -out plaintext.txt -k "password123"

# AES-256-CBC (con IV aleatorio)
openssl enc -aes-256-cbc -in plaintext.txt -out ciphertext.bin -k "password123" -pbkdf2

# Descifrar
openssl enc -aes-256-cbc -d -in ciphertext.bin -out plaintext.txt -k "password123" -pbkdf2
```

### Cifrar con Python

```python
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.primitives import padding
from cryptography.hazmat.backends import default_backend
import os

# Generar clave y IV
key = os.urandom(32)  # AES-256
iv = os.urandom(16)

# Cifrar (AES-CBC)
padder = padding.PKCS7(128).padder()
padded_data = padder.update(b"Hello, World!") + padder.finalize()

cipher = Cipher(algorithms.AES(key), modes.CBC(iv), backend=default_backend())
encryptor = cipher.encryptor()
ciphertext = encryptor.update(padded_data) + encryptor.finalize()

print(f"Ciphertext: {ciphertext.hex()}")

# Descifrar
cipher = Cipher(algorithms.AES(key), modes.CBC(iv), backend=default_backend())
decryptor = cipher.decryptor()
padded_plaintext = decryptor.update(ciphertext) + decryptor.finalize()

unpadder = padding.PKCS7(128).unpadder()
plaintext = unpadder.update(padded_plaintext) + unpadder.finalize()

print(f"Plaintext: {plaintext.decode()}")
```

### Cifrar con GCM (autenticado)

```python
from cryptography.hazmat.primitives.ciphers.aead import AESGCM
import os

key = AESGCM.generate_key(bit_length=256)
aesgcm = AESGCM(key)

nonce = os.urandom(12)  # Nonce único por mensaje
associated_data = b"metadata"  # Datos asociados (no cifrados)

ciphertext = aesgcm.encrypt(nonce, b"Secret message", associated_data)
print(f"Ciphertext: {ciphertext.hex()}")

# Descifrar
plaintext = aesgcm.decrypt(nonce, ciphertext, associated_data)
print(f"Plaintext: {plaintext.decode()}")
```

---

## 4. ChaCha20

### ¿Qué es?

**ChaCha20** es un cifrado de flujo desarrollado por Daniel J. Bernstein. Es una variante de Salsa20.

| Característica | ChaCha20 | AES |
|---|---|---|
| **Tipo** | Flujo | Bloque |
| **Clave** | 256 bits | 128/192/256 bits |
| **Velocidad sin AES-NI** | Más rápida | Más lenta |
| **Simplicidad** | Más simple | Más complejo |
| **Uso** | TLS 1.3, WireGuard | TLS 1.3, disco |

### ChaCha20-Poly1305 (autenticado)

```python
from cryptography.hazmat.primitives.ciphers.aead import ChaCha20Poly1305
import os

key = ChaCha20Poly1305.generate_key()
nonce = os.urandom(12)

# Cifrar
cipher = ChaCha20Poly1305(key)
ciphertext = cipher.encrypt(nonce, b"Secret message", b"associated data")

# Descifrar
plaintext = cipher.decrypt(nonce, ciphertext, b"associated data")
print(plaintext.decode())  # "Secret message"
```

### ¿Cuándo usar ChaCha20 vs AES?

| Escenario | Recomendación |
|---|---|
| **Hardware con AES-NI** | AES-256-GCM |
| **Hardware sin AES-NI** (ARM, IoT) | ChaCha20-Poly1305 |
| **TLS 1.3** | Ambos (negociación automática) |
| **WireGuard** | ChaCha20-Poly1305 |
| **Disco encriptado** | AES-XTS |

---

## 5. Modos de operación

### ¿Por qué existen modos?

Un cifrado de bloques solo cifra un bloque de 16 bytes. Los **modos de operación** definen cómo cifrar mensajes más largos.

### Comparativa de modos

| Modo | Paralelizable | Autenticado | Seguro | Uso |
|---|---|---|---|---|
| **ECB** | ✅ | ❌ | ❌ | ❌ NUNCA usar |
| **CBC** | ❌ (descifrado sí) | ❌ | ⚠️ Con padding | Legado |
| **CTR** | ✅ | ❌ | ⚠️ Sin nonce repeat | Legado |
| **GCM** | ✅ | ✅ | ✅ | Recomendado |
| **CCM** | ❌ | ✅ | ✅ | IoT |
| **XTS** | ❌ | ❌ | ✅ | Disco |

### ECB (Electronic Codebook) — ❌ INSEGURO

```python
# ECB cifra cada bloque independientemente
# Bloques idénticos → ciphertext idéntico → PATRÓN VISIBLE

# Ejemplo: cifrar una imagen con ECB
from PIL import Image
import numpy as np
from Crypto.Cipher import AES

# ECB revela patrones en la imagen
# ¡Nunca usar ECB para datos con estructura!
```

### CBC (Cipher Block Chaining)

```
Plaintext:  P1  P2  P3  P4
              │   │   │   │
IV:     ──┐   │   │   │   │
           ▼   ▼   ▼   ▼
        XOR XOR XOR XOR
           │   │   │   │
        AES  AES  AES  AES
           │   │   │   │
Ciphertext: C1  C2  C3  C4
```

### GCM (Galois/Counter Mode) — ✅ RECOMENDADO

```
Plaintext:  P1  P2  P3  P4
              │   │   │   │
Counter:  ──┐ │   │   │   │
           ▼   ▼   ▼   ▼
        AES AES AES AES
           │   │   │   │
        XOR XOR XOR XOR
           │   │   │   │
        GHASH (autenticación)
           │
        Ciphertext + Tag
```

### Ejemplo: ECB vs CBC vs GCM

```python
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.primitives import padding
from cryptography.hazmat.backends import default_backend
import os

key = os.urandom(32)
iv = os.urandom(16)
data = b"A" * 16 + b"A" * 16  # Dos bloques idénticos

# ECB: mismo input → mismo output (INSEGURO)
cipher = Cipher(algorithms.AES(key), modes.ECB(), backend=default_backend())
ectx = cipher.encryptor()
ecb_ct = ectx.update(data) + ectx.finalize()
print(f"ECB: {ecb_ct[:16].hex()} == {ecb_ct[16:].hex()}")  # ¡Idénticos!

# CBC: mismo input → output diferente
cipher = Cipher(algorithms.AES(key), modes.CBC(iv), backend=default_backend())
ectx = cipher.encryptor()
padder = padding.PKCS7(128).padder()
padded = padder.update(data) + padder.finalize()
cbc_ct = ectx.update(padded) + ectx.finalize()
print(f"CBC: diferentes bloques de ciphertext")

# GCM: autenticado
from cryptography.hazmat.primitives.ciphers.aead import AESGCM
aesgcm = AESGCM(key)
gcm_ct = aesgcm.encrypt(iv, data, None)
print(f"GCM: ciphertext + tag de autenticación")
```

---

## 6. Padding

### ¿Qué es?

El **padding** rellena el último bloque para que sea del tamaño correcto.

### PKCS#7 (el más común)

```
Si el bloque tiene 16 bytes y faltan 3:
Padding: 03 03 03

Si el bloque está completo:
Padding: 10 10 10 10 10 10 10 10 10 10 10 10 10 10 10 10
```

### Padding Oracle Attack

```python
# Si el servidor revela si el padding es válido,
# un atacante puede descifrar sin la clave.

# Ejemplo vulnerable:
def vulnerable_decrypt(ciphertext, key):
    plaintext = aes_decrypt(ciphertext, key)
    if is_valid_padding(plaintext):  # ← FUGA DE INFORMACIÓN
        return "padding valid"
    else:
        return "padding invalid"

# El atacante puede:
# 1. Modificar el ciphertext
# 2. Enviar al servidor
# 3. Observar si el padding es válido
# 4. Repetir para descifrar byte por byte
```

---

## 7. Cifrado en la práctica

### Encriptación de disco (Linux: LUKS)

```bash
# Crear volumen cifrado
cryptsetup luksFormat /dev/sdb1

# Abrir volumen
cryptsetup open /dev/sdb1 my_volume

# Crear filesystem
mkfs.ext4 /dev/mapper/my_volume

# Montar
mount /dev/mapper/my_volume /mnt/encrypted

# Cerrar
umount /mnt/encrypted
cryptsetup close my_volume
```

### Encriptación de archivos (OpenSSL)

```bash
# Cifrar archivo
openssl enc -aes-256-gcm -salt -in secreto.txt -out secreto.enc -k "password123"

# Descifrar archivo
openssl enc -aes-256-gcm -d -in secreto.enc -out secreto.txt -k "password123"
```

### Encriptación de archivos (age)

```bash
# age: cifrado moderno y simple
# Instalar
wget https://github.com/FiloSottile/age/releases/latest/download/age-*-linux-amd64.tar.gz

# Generar clave
age-keygen -o key.txt
# Public key: age1...

# Cifrar
age -r age1... -o secreto.age secreto.txt

# Descifrar
age -d -i key.txt -o secreto.txt secreto.age
```

---

## 8. Defensa: mal uso de cifrado

### Errores comunes

| Error | Consecuencia | Solución |
|---|---|---|
| **Usar ECB** | Patrones visibles | Usar GCM o CBC |
| **Reutilizar IV/Nonce** | Compromete la seguridad | Generar nonce único por mensaje |
| **Usar MD5/SHA-1** | Hashes crackeados | Usar SHA-256, bcrypt |
| **Cifrado casero** | Implementación vulnerable | Usar OpenSSL, libs estándar |
| **Clave en código fuente** | Fuga de clave | Usar variables de entorno, vaults |
| **Sin autenticación** | Modificación de ciphertext | Usar GCM, Poly1305 |

### Checklist de cifrado seguro

```markdown
## Checklist de Cifrado Seguro

### Algoritmo
- [ ] AES-256-GCM o ChaCha20-Poly1305
- [ ] NO DES, 3DES, RC4, Blowfish
- [ ] NO cifrado casero

### Claves
- [ ] Generadas con CSPRNG (os.urandom, secrets)
- [ ] Almacenadas en vault (HashiCorp Vault, AWS KMS)
- [ ] NO en código fuente
- [ ] Rotación periódica

### IV/Nonce
- [ ] Generado aleatoriamente por mensaje
- [ ] Nunca reutilizado
- [ ] Almacenado con el ciphertext

### Autenticación
- [ ] GCM, Poly1305 o CCM
- [ ] Verificar tag antes de descifrar
- [ ] NO solo cifrado sin autenticación

### Implementación
- [ ] Usar librerías estándar (OpenSSL, cryptography)
- [ ] NO implementar criptografía manual
- [ ] Peer review del código criptográfico
```

---

## 9. Referencias

| Recurso | URL |
|---|---|
| **NIST AES** | [https://csrc.nist.gov/projects/cryptographic-standards-and-guidelines](https://csrc.nist.gov/projects/cryptographic-standards-and-guidelines) |
| **RFC 8439 (ChaCha20-Poly1305)** | [https://datatracker.ietf.org/doc/html/rfc8439](https://datatracker.ietf.org/doc/html/rfc8439) |
| **OWASP Crypto Cheat Sheet** | [https://cheatsheetseries.owasp.org/cheatsheets/Cryptographic_Cheat_Sheet.html](https://cheatsheetseries.owasp.org/cheatsheets/Cryptographic_Cheat_Sheet.html) |
| **Crypto101** | [https://www.crypto101.io/](https://www.crypto101.io/) |

---

## 📝 Entregable de portafolio

```markdown
# Cifrado Simétrico — Ejercicios

## Ejercicio 1: AES-256-GCM con OpenSSL
```bash
# Generar clave
openssl rand -hex 32 > key.txt

# Cifrar
openssl enc -aes-256-gcm -in secreto.txt -out secreto.enc \
    -K $(cat key.txt) -iv $(openssl rand -hex 16)

# Descifrar
openssl enc -aes-256-gcm -d -in secreto.enc -out secreto.txt \
    -K $(cat key.txt) -iv <IV>
```

## Ejercicio 2: Detectar ECB
- Dado un ciphertext, determinar si fue cifrado con ECB
- Solución: buscar bloques repetidos en el ciphertext

## Ejercicio 3: Comparar modos
- Cifrar el mismo mensaje con ECB, CBC y GCM
- Comparar los ciphertext resultantes
- ECB: bloques idénticos visibles
```

---

**[⬅ Matemáticas Crypto](./01-matematicas-crypto.md)** · **[→ Cifrado Asimétrico](./03-criptografia-asimetrica.md)**
