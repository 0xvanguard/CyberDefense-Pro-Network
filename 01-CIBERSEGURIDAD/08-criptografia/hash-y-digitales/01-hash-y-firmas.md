# #️⃣ Hashing y Firmas Digitales

> *"Un hash es la huella digital de los datos: único, determinista e irreversible. Una firma digital es la prueba de que algo vino de quien dice venir."*

---

## 📋 Tabla de contenido

1. [¿Qué es un hash?](#1-qué-es-un-hash)
2. [Algoritmos de hash](#2-algoritmos-de-hash)
3. [Hashing seguro de contraseñas](#3-hashing-seguro-de-contraseñas)
4. [Firmas digitales](#4-firmas-digitales)
5. [Certificados digitales y PKI](#5-certificados-digitales-y-pki)
6. [Integridad de datos](#6-integridad-de-datos)
7. [Ataques a hashes](#7-ataques-a-hashes)
8. [Referencias](#8-referencias)

---

## 1. ¿Qué es un hash?

### Definición

Una **función hash** transforma datos de tamaño arbitrario en una cadena de tamaño fijo:

```
hash("hola") = "ce55e428bd79a70e10f26b1a7a6e3e7e"
hash("hola!") = "9d5ed638a81e38a7d1d4e9a8c7b2f1a3"
```

### Propiedades de un hash criptográfico

| Propiedad | Significado |
|---|---|
| **Determinista** | Mismo input → siempre mismo output |
| **Rápido de calcular** | Eficiente incluso para datos grandes |
| **Irreversible** | No se puede obtener el input del hash |
| **Avalanche** | Un bit cambiado → hash completamente diferente |
| **Sin colisiones** | Difícil encontrar dos inputs con mismo hash |

### Avalanche effect

```python
import hashlib

# Diferencia de 1 bit produce hash completamente diferente
h1 = hashlib.sha256(b"hello").hexdigest()
h2 = hashlib.sha256(b"hellp").hexdigest()

print(f"hello: {h1}")
print(f"hellp: {h2}")
# Output: hashes completamente diferentes
```

---

## 2. Algoritmos de hash

### Comparativa

| Algoritmo | Tamaño | Velocidad | Seguridad | Estado |
|---|---|---|---|---|
| **MD5** | 128 bits | ⭐⭐⭐⭐⭐ | ❌ | DESTRUIDO |
| **SHA-1** | 160 bits | ⭐⭐⭐⭐ | ❌ | DESTRUIDO |
| **SHA-256** | 256 bits | ⭐⭐⭐ | ✅ | ✅ Estándar |
| **SHA-384** | 384 bits | ⭐⭐⭐ | ✅ | ✅ Seguro |
| **SHA-512** | 512 bits | ⭐⭐⭐ | ✅ | ✅ Seguro |
| **SHA3-256** | 256 bits | ⭐⭐ | ✅ | ✅ Moderno |
| **BLAKE2b** | 512 bits | ⭐⭐⭐⭐⭐ | ✅ | ✅ Rápido |
| **BLAKE3** | 256 bits | ⭐⭐⭐⭐⭐ | ✅ | ✅ Muy rápido |

### MD5 — ❌ DESTRUIDO

```python
import hashlib

# MD5 tiene colisiones conocidas desde 2004
h = hashlib.md5(b"test").hexdigest()
print(f"MD5: {h}")

# Ejemplo de colisión (dos archivos diferentes, mismo hash):
# file1.pdf → 8e3a5f3a8b5c7d2e1f0a9b8c7d6e5f4a
# file2.pdf → 8e3a5f3a8b5c7d2e1f0a9b8c7d6e5f4a
# ¡Mismo hash! → No se puede confiar
```

### SHA-1 — ❌ DESTRUIDO

```python
import hashlib

# Google demostró colisiones prácticas en 2017 (SHAttered)
h = hashlib.sha1(b"test").hexdigest()
print(f"SHA-1: {h}")

# GitHub dejó de aceptar SHA-1 para firmas en 2020
# Git migra a SHA-256
```

### SHA-256 — ✅ ESTÁNDAR

```python
import hashlib

h = hashlib.sha256(b"test").hexdigest()
print(f"SHA-256: {h}")
print(f"Longitud: {len(h)} caracteres hex (256 bits)")
```

### BLAKE3 — ✅ RÁPIDO

```python
# BLAKE3 es 10x más rápido que SHA-256
import blake3

h = blake3.blake3(b"test").hexdigest()
print(f"BLAKE3: {h}")
```

### Uso de cada algoritmo

| Algoritmo | Uso recomendado | Uso NO recomendado |
|---|---|---|
| **MD5** | Checksums no-críticos | Firmas, contraseñas |
| **SHA-1** | Git internamente | Firmas, SSL |
| **SHA-256** | Firmas, contraseñas, Bitcoin | — |
| **SHA-512** | Contraseñas, alto seguridad | — |
| **BLAKE2b/3** | Checksums rápidos, archivos | — |
| **Argon2** | Contraseñas (con salt) | Datos generales |
| **bcrypt** | Contraseñas (legacy) | Datos generales |

---

## 3. Hashing seguro de contraseñas

### ¿Por qué no usar SHA-256 directo?

```python
# MAL: SHA-256 para contraseñas
import hashlib
password_hash = hashlib.sha256(b"password123").hexdigest()
# Problemas:
# 1. Sin salt → rainbow tables
# 2. Rápido → brute force factible
# 3. Sin key stretching → sin defensa
```

### Solución: algoritmos KDF

| Algoritmo | Velocidad | Memoria | Estado |
|---|---|---|---|
| **PBKDF2** | configurable | baja | ✅ Mínimo aceptable |
| **bcrypt** | 100ms | 4KB | ✅ Legado aceptable |
| **scrypt** | configurable | configurable | ✅ Bueno |
| **Argon2** | configurable | configurable | ✅ Recomendado |

### Argon2 (recomendado)

```python
# pip install argon2-cffi
from argon2 import PasswordHasher

ph = PasswordHasher(
    time_cost=3,        # Iteraciones
    memory_cost=65536,  # 64MB de memoria
    parallelism=4       # 4 hilos
)

# Hash de contraseña
password = "MiContraseñaSegura123!"
password_hash = ph.hash(password)
print(f"Hash: {password_hash}")

# Verificar
try:
    ph.verify(password_hash, password)
    print("Contraseña válida ✅")
except Exception:
    print("Contraseña inválida ❌")
```

### bcrypt

```python
# pip install bcrypt
import bcrypt

password = b"MiContraseñaSegura123!"

# Hash (con salt automático)
password_hash = bcrypt.hashpw(password, bcrypt.gensalt(rounds=12))
print(f"Hash: {password_hash}")

# Verificar
if bcrypt.checkpw(password, password_hash):
    print("Contraseña válida ✅")
else:
    print("Contraseña inválida ❌")
```

### PBKDF2

```python
import hashlib
import os

password = b"MiContraseñaSegura123!"
salt = os.urandom(16)

# Hash con 100,000 iteraciones
password_hash = hashlib.pbkdf2_hmac(
    'sha256',
    password,
    salt,
    100000  # iteraciones
)
print(f"Hash: {password_hash.hex()}")
```

---

## 4. Firmas digitales

### ¿Qué es?

Una **firma digital** prueba que:
1. El emisor es quien dice ser (autenticación)
2. El mensaje no fue alterado (integridad)
3. El emisor no puede negar haber enviado el mensaje (no repudio)

### Proceso

```
FIRMAR:
1. Calcular hash del mensaje
2. Cifrar el hash con la clave privada del emisor
3. Firma = hash_cifrado

VERIFICAR:
1. Calcular hash del mensaje
2. Descifrar la firma con la clave pública del emisor
3. Comparar: hash_calculado == hash_descifrado
4. Si son iguales → firma válida ✅
```

### Firmar con RSA (Python)

```python
from Crypto.PublicKey import RSA
from Crypto.Signature import pkcs1_15
from Crypto.Hash import SHA256

# Generar claves
key = RSA.generate(2048)
private_key = key.export_key()
public_key = key.publickey().export_key()

# Firmar
message = b"Documento importante"
h = SHA256.new(message)
signature = pkcs1_15.new(RSA.import_key(private_key)).sign(h)
print(f"Firma: {signature.hex()[:64]}...")

# Verificar
try:
    pkcs1_15.new(RSA.import_key(public_key)).verify(h, signature)
    print("Firma válida ✅")
except (ValueError, TypeError):
    print("Firma inválida ❌")
```

### Firmar con ECDSA (Python)

```python
from Crypto.PublicKey import ECC
from Crypto.Signature import DSS
from Crypto.Hash import SHA256

# Generar claves ECC
key = ECC.generate(curve='P-256')

# Firmar
message = b"Documento importante"
h = SHA256.new(message)
signer = DSS.new(key, 'fips-186-3')
signature = signer.sign(h)

# Verificar
verifier = DSS.new(key.public_key(), 'fips-186-3')
try:
    verifier.verify(h, signature)
    print("Firma válida ✅")
except ValueError:
    print("Firma inválida ❌")
```

### Firmar con OpenSSL (CLI)

```bash
# Generar claves
openssl genpkey -algorithm RSA -out private.pem -pkeyopt rsa_keygen_bits:2048
openssl rsa -pubout -in private.pem -out public.pem

# Firmar archivo
openssl dgst -sha256 -sign private.pem -out firma.sig archivo.txt

# Verificar firma
openssl dgst -sha256 -verify public.pem -signature firma.sig archivo.txt
# Output: Verified OK
```

### Firmar con GPG

```bash
# Firmar archivo
gpg --clearsign documento.txt
# Crea documento.txt.asc con firma

# Verificar firma
gpg --verify documento.txt.asc

# Firmar binariamente
gpg --sign documento.txt
# Crea documento.txt.gpg
```

---

## 5. Certificados digitales y PKI

### ¿Qué es un certificado?

Un **certificado digital** es un documento electrónico que vincula una clave pública con una identidad:

```
Certificado:
├── Nombre: example.com
├── Clave pública: (e, n)
├── Válido desde: 2026-01-01
├── Válido hasta: 2026-12-31
├── Emisor: Let's Encrypt
└── Firma del emisor: [firma digital]
```

### PKI (Public Key Infrastructure)

```
CA (Certificate Authority)
├── Emite certificados
├── Verifica identidad
└── Firma certificados con su clave privada

Intermediate CA
├── Emite certificados de usuario
└── Firma con su clave privada (respaldada por Root CA)

Root CA
├── Raíz de confianza
├── Auto-firmado
└── Preinstalado en navegadores/OS
```

### Cadena de confianza

```
Root CA (auto-firmado, preinstalado)
└── Intermediate CA (firmado por Root)
    └── Certificado de example.com (firmado por Intermediate)
        └── Verificado por el navegador ✅
```

---

## 6. Integridad de datos

### Checksums con SHA-256

```bash
# Calcular hash de un archivo
sha256sum archivo.zip
# Output: 8f7e6d5c4b3a2f1e0d9c8b7a6f5e4d3c2b1a0f9e8d7c6b5a4f3e2d1c0b9a8f7e  archivo.zip

# Verificar integridad (si tienes el hash conocido)
sha256sum -c hash.txt
# archivo.zip: OK
```

### Software signing

```bash
# Firmar paquete de software
gpg --sign paquete.deb

# Verificar firma antes de instalar
gpg --verify paquete.deb.sig paquete.deb
```

### Blockchain y Bitcoin

```python
import hashlib

# Bitcoin usa SHA-256 doble
block_data = b"datos del bloque"
hash1 = hashlib.sha256(block_data).digest()
hash2 = hashlib.sha256(hash1).digest()
print(f"Bitcoin hash: {hash2.hex()}")
```

---

## 7. Ataques a hashes

### Rainbow tables

```
TABLA PRECOMPUTADA:
password → hash
123456   → e10adc3949ba59abbe56e057f20f883e
password → 5f4dcc3b5aa765d61d8327deb882cf99
admin    → 21232f297a57a5a743894a0e4a801fc3

ATAQUE:
1. Obtener hash de la víctima
2. Buscar en la rainbow table
3. ¡Encontrado! → 123456

DEFENSA: SALT (número aleatorio único por hash)
```

### Brute force

```python
# Fuerza bruta: probar todas las combinaciones
import itertools
import hashlib

target = "e10adc3949ba59abbe56e057f20f883e"  # Hash de "123456"

# Probar combinaciones de 6 dígitos
for combo in itertools.product("0123456789", repeat=6):
    password = "".join(combo)
    if hashlib.md5(password.encode()).hexdigest() == target:
        print(f"¡Encontrado! {password}")
        break
# Output: ¡Encontrado! 123456
```

### Dictionary attack

```bash
# hashcat: fuerza bruta con diccionario
hashcat -m 0 hash.txt rockyou.txt
# -m 0: modo MD5
# hash.txt: archivo con hashes
# rockyou.txt: wordlist

# john the ripper
john --wordlist=rockyou.txt hash.txt
```

---

## 8. Referencias

| Recurso | URL |
|---|---|
| **OWASP Password Storage** | [https://cheatsheetseries.owasp.org/cheatsheets/Password_Storage_Cheat_Sheet.html](https://cheatsheetseries.owasp.org/cheatsheets/Password_Storage_Cheat_Sheet.html) |
| **NIST SP 800-63B** | [https://pages.nist.gov/800-63-3/sp800-63b.html](https://pages.nist.gov/800-63-3/sp800-63b.html) |
| **hashcat** | [https://hashcat.net/hashcat/](https://hashcat.net/hashcat/) |
| **John the Ripper** | [https://www.openwall.com/john/](https://www.openwall.com/john/) |
| **CryptoHack** | [https://cryptohack.org/](https://cryptohack.org/) |

---

## 📝 Entregable de portafolio

```markdown
# Hashing y Firmas — Ejercicios

## Ejercicio 1: Hash de contraseña
- Hashear "password123" con SHA-256, bcrypt y Argon2
- Comparar tiempos de ejecución
- Explicar por qué bcrypt/Argon2 son más seguros

## Ejercicio 2: Firma digital
- Generar par de claves RSA
- Firmar un archivo
- Modificar el archivo (1 byte)
- Verificar que la firma falla

## Ejercicio 3: Crack de hash
- Crear hash MD5 de "123456"
- Crackear con hashcat usando rockyou.txt
- Documentar tiempo requerido

## Ejercicio 4: Certificado SSL
- Generar certificado autofirmado con OpenSSL
- Verificar cadena de confianza
- Explicar por qué los certificados de Let's Encrypt son gratuitos
```

---

**[⬅ Cifrado Asimétrico](../fundamentos/03-criptografia-asimetrica.md)** · **[→ Criptoanalisis](../criptoanalisis/01-tecnicas-ataque.md)**
