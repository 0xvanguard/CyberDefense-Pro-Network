# 🔐 Cifrado Asimétrico

> *"El cifrado asimétrico resolvió el problema milenario de cómo dos personas que nunca se han hablado pueden acordar un secreto de forma segura."*

---

## 📋 Tabla de contenido

1. [¿Qué es el cifrado asimétrico?](#1-qué-es-el-cifrado-asimétrico)
2. [RSA](#2-rsa)
3. [Diffie-Hellman](#3-diffie-hellman)
4. [Curvas Elípticas (ECC)](#4-curvas-elípticas-ecc)
5. [Intercambio de claves](#5-intercambio-de-claves)
6. [Cifrado híbrido](#6-cifrado-híbrido)
7. [Implementación práctica](#7-implementación-práctica)
8. [Defensa: ataques a criptografía asimétrica](#8-defensa-ataques-a-criptografía-asimétrica)
9. [Referencias](#9-referencias)

---

## 1. ¿Qué es el cifrado asimétrico?

### Definición

El **cifrado asimétrico** usa **dos claves** relacionadas matemáticamente:

```
Clave pública:  se comparte libremente (para cifrar)
Clave privada:  se mantiene secreta (para descifrar)
```

### Analogía

```
BOB genera un par de claves:
├── Clave pública → la pone en su buzón (todos pueden dejar cartas)
└── Clave privada → la tiene solo él (solo él puede abrir las cartas)

ALICIA quiere enviar un secreto a Bob:
1. Toma la clave pública de Bob
2. Cifra el mensaje con ella
3. Envía el ciphertext a Bob
4. Solo Bob puede descifrarlo con su clave privada
```

### Ventajas y desventajas

| Aspecto | Asimétrico | Simétrico |
|---|---|---|
| **Velocidad** | ⭐⭐ Lento (~1000x) | ⭐⭐⭐⭐⭐ Rápido |
| **Distribución** | ✅ No hay problema | ❌ Problema de distribución |
| **Escalabilidad** | ✅ n(n-1)/2 claves | ❌ n² claves |
| **Uso típico** | Intercambio de claves, firmas | Datos, disco, tráfico |

---

## 2. RSA

### El algoritmo

```
1. GENERACIÓN DE CLAVES
   Seleccionar primos grandes p, q
   n = p × q
   φ(n) = (p-1) × (q-1)
   Seleccionar e coprimo con φ(n) (típicamente e = 65537)
   Calcular d = e⁻¹ mod φ(n)
   
   Clave pública:  (e, n)
   Clave privada:  (d, n)

2. CIFRADO
   c = m^e mod n

3. DESCIFRADO
   m = c^d mod n
```

### Ejemplo manual

```python
from Crypto.Util.number import getPrime, inverse, GCD

# Paso 1: Generar primos (en producción usar 2048+ bits)
p = 61
q = 53

# Paso 2: Calcular n y φ(n)
n = p * q          # 3233
phi_n = (p-1)*(q-1)  # 3120

# Paso 3: Seleccionar e
e = 17
assert GCD(e, phi_n) == 1  # Verificar coprimo

# Paso 4: Calcular d
d = inverse(e, phi_n)  # 2753

print(f"Clave pública: ({e}, {n})")   # (17, 3233)
print(f"Clave privada: ({d}, {n})")   # (2753, 3233)

# Paso 5: Cifrar
m = 65  # Mensaje
c = pow(m, e, n)  # 2790
print(f"Cifrado: {c}")

# Paso 6: Descifrar
m_descifrado = pow(c, d, n)  # 65
print(f"Descifrado: {m_descifrado}")
assert m == m_descifrado
```

### Generar claves RSA con Python

```python
from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_OAEP
from Crypto.Signature import pkcs1_15
from Crypto.Hash import SHA256

# Generar par de claves (2048 bits)
key = RSA.generate(2048)

# Exportar claves
private_key = key.export_key()
public_key = key.publickey().export_key()

# Guardar en archivos
with open("private.pem", "wb") as f:
    f.write(private_key)
with open("public.pem", "wb") as f:
    f.write(public_key)

# Cifrar con clave pública
cipher = PKCS1_OAEP.new(RSA.import_key(public_key))
ciphertext = cipher.encrypt(b"Hello, RSA!")

# Descifrar con clave privada
cipher = PKCS1_OAEP.new(RSA.import_key(private_key))
plaintext = cipher.decrypt(ciphertext)
print(plaintext.decode())  # "Hello, RSA!"
```

### Firmar con RSA

```python
# Firmar
message = b"Documento importante"
h = SHA256.new(message)
signature = pkcs1_15.new(RSA.import_key(private_key)).sign(h)

# Verificar
try:
    pkcs1_15.new(RSA.import_key(public_key)).verify(h, signature)
    print("Firma válida ✅")
except (ValueError, TypeError):
    print("Firma inválida ❌")
```

### Tamaños de clave RSA

| Tamaño | Seguridad | Estado |
|---|---|---|
| 1024 bits | ~80 bits | ❌ INSEGURO |
| 2048 bits | ~112 bits | ✅ Seguro hasta 2030 |
| 3072 bits | ~128 bits | ✅ Seguro hasta 2030+ |
| 4096 bits | ~140 bits | ✅ Seguro a largo plazo |

---

## 3. Diffie-Hellman

### El problema que resuelve

¿Cómo pueden Alice y Bob acordar una clave secreta por un canal inseguro?

### Protocolo

```
ACUERDO PÚBLICO (inseguro):
   p = primo grande
   g = generador

ALICIA:
   a = secreto privado (aleatorio)
   A = g^a mod p → envía a Bob

BOB:
   b = secreto privado (aleatorio)  
   B = g^b mod p → envía a Alice

CLAVE COMPARTIDA:
   Alice calcula: s = B^a mod p = g^(ab) mod p
   Bob calcula:   s = A^b mod p = g^(ab) mod p
   ¡Ambos tienen la misma s!
```

### Ejemplo

```python
import random

# Acuerdo público
p = 23  # Primo (en producción: 2048+ bits)
g = 5   # Generador

# Alice
a = random.randint(1, p-1)  # Secreto privado
A = pow(g, a, p)            # Clave pública

# Bob
b = random.randint(1, p-1)  # Secreto privado
B = pow(g, b, p)            # Clave pública

# Intercambio (canal inseguro)
# Alice envía A a Bob, Bob envía B a Alice

# Calcular clave compartida
s_alice = pow(B, a, p)
s_bob = pow(A, b, p)

print(f"Alice calcula: {s_alice}")
print(f"Bob calcula: {s_bob}")
print(f"¿Iguales? {s_alice == s_bob}")  # True
```

### Seguridad de DH

| Tamaño de p | Seguridad | Estado |
|---|---|---|
| 1024 bits | ~80 bits | ❌ INSEGURO (Logjam) |
| 2048 bits | ~112 bits | ✅ Seguro |
| 4096 bits | ~140 bits | ✅ Seguro |

---

## 4. Curvas Elípticas (ECC)

### ¿Por qué ECC?

ECC ofrece la **misma seguridad que RSA con claves mucho más pequeñas**:

| Seguridad | RSA | ECC |
|---|---|---|
| 80 bits | 1024 bits | 160 bits |
| 128 bits | 3072 bits | 256 bits |
| 192 bits | 7680 bits | 384 bits |
| 256 bits | 15360 bits | 521 bits |

### ECDSA (Firma Digital sobre Curvas Elípticas)

```python
from Crypto.PublicKey import ECC
from Crypto.Signature import DSS
from Crypto.Hash import SHA256

# Generar clave ECC
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

### ECDH (Intercambio de claves sobre Curvas Elípticas)

```python
from Crypto.PublicKey import ECC
from Crypto.Cipher import AES
from Crypto.Hash import SHA256
import os

# Alice genera su par de claves
alice_key = ECC.generate(curve='P-256')

# Bob genera su par de claves
bob_key = ECC.generate(curve='P-256')

# Alice calcula punto compartido
shared_point_alice = alice_key.d * bob_key.pointQ

# Bob calcula punto compartido
shared_point_bob = bob_key.d * alice_key.pointQ

# ¡Ambos tienen el mismo punto!
# Derivar clave AES del punto compartido
shared_secret = SHA256.new(str(shared_point_alice.x).encode()).digest()
aes_key = shared_secret[:32]

# Cifrar con AES
cipher = AES.new(aes_key, AES.MODE_GCM)
ciphertext, tag = cipher.encrypt_and_digest(b"Hello, ECC!")
```

### Curvas populares

| Curva | Tamaño | Uso |
|---|---|---|
| **P-256** (secp256r1) | 256 bits | TLS, SSH, firmas |
| **P-384** (secp384r1) | 384 bits | Alto seguridad |
| **P-521** (secp521r1) | 521 bits | Ultra seguridad |
| **Curve25519** | 256 bits | TLS 1.3, Signal, WireGuard |
| **Curve448** | 448 bits | Alto seguridad |

---

## 5. Intercambio de claves

### TLS 1.3: cómo se intercambian claves

```
1. Client Hello
   └─ Soporta: TLS_AES_256_GCM_SHA384, ChaCha20-Poly1305

2. Server Hello
   └─ Selecciona: TLS_AES_256_GCM_SHA384
   └─ Clave pública ECDHE (ephemeral)
   └─ Firma digital del certificado

3. Verificación
   └─ Cliente verifica certificado con CA
   └─ Calcula clave compartida ECDHE

4. Clave de sesión
   └─ Derivada de ECDHE via HKDF
   └─ Única para esta sesión (Perfect Forward Secrecy)
```

### Perfect Forward Secrecy (PFS)

```
CON PFS (ECDHE):
- Cada sesión usa claves efímeras
- Si la clave privada del servidor se compromete mañana,
  las sesiones pasadas NO se pueden descifrar

SIN PFS (RSA key exchange):
- La misma clave se usa para todas las sesiones
- Si la clave privada se compromete, TODAS las sesiones pasadas
  se pueden descifrar
```

---

## 6. Cifrado híbrido

### ¿Por qué híbrido?

El cifrado asimétrico es lento. En la práctica se usa **híbrido**:

```
1. Usar asimétrico para intercambiar una clave simétrica
2. Usar simétrico para cifrar los datos
```

### TLS 1.3

```
1. ECDHE: intercambiar clave simétrica
2. AES-256-GCM: cifrar el tráfico HTTP
3. ChaCha20-Poly1305: alternativa para dispositivos sin AES-NI
```

### Signal Protocol

```
1. X3DH: intercambio de claves asimétrico
2. Double Ratchet: clave simétrica que cambia por mensaje
3. AES-256-CBC + HMAC-SHA256: cifrar cada mensaje
```

---

## 7. Implementación práctica

### Cifrar archivo con RSA (OpenSSL)

```bash
# Generar par de claves RSA
openssl genpkey -algorithm RSA -out private.pem -pkeyopt rsa_keygen_bits:2048
openssl rsa -pubout -in private.pem -out public.pem

# Cifrar con clave pública
openssl pkeyutl -encrypt -pubin -inkey public.pem -in secreto.txt -out secreto.enc

# Descifrar con clave privada
openssl pkeyutl -decrypt -inkey private.pem -in secreto.enc -out secreto.txt
```

### Cifrar archivo con GPG

```bash
# Generar clave GPG
gpg --gen-key

# Cifrar para alguien (usando su clave pública)
gpg --encrypt --recipient email@domain.com archivo.txt

# Descifrar (usando tu clave privada)
gpg --decrypt archivo.txt.gpg > archivo.txt

# Firmar archivo
gpg --sign archivo.txt

# Verificar firma
gpg --verify archivo.txt.sig
```

### SSH: cifrado de conexión

```bash
# Generar par de claves SSH
ssh-keygen -t ed25519 -C "email@domain.com"

# Copiar clave pública al servidor
ssh-copy-id user@server

# Conectar (cifrado automático via ECDH)
ssh user@server

# Verificar cifrado de la conexión
ssh -vv user@server | grep "cipher"
```

---

## 8. Defensa: ataques a criptografía asimétrica

### Ataques comunes

| Ataque | Objetivo | Defensa |
|---|---|---|
| **Factoring (RSA)** | Factorizar n en p×q | Usar claves ≥2048 bits |
| **Logaritmo discreto (DH)** | Encontrar x tal que g^x ≡ h | Usar primos ≥2048 bits |
| **Punto del curva (ECC)** | Resolver ECDLP | Usar curvas estándar |
| **Side-channel** | Timing, power analysis | Implementaciones constante-time |
| **Man-in-the-middle** | Interceptar claves | Verificar certificados (PKI) |
| **Quantum (Shor)** | Resolver todos los anteriores | Post-quantum crypto |

### Post-quantum cryptography

```python
# NIST está estandarizando algoritmos resistentes a cuánticos:
# - CRYSTALS-Kyber (key encapsulation)
# - CRYSTALS-Dilithium (firmas)
# - FALCON (firmas)
# - SPHINCS+ (firmas basadas en hash)

# Ejemplo con liboqs (Open Quantum Safe)
# pip install liboqs-python
import oqs

# Generar clave
kem = oqs.KeyEncapsulation("Kyber512")
keypair = kem.generate_keypair()

# Ciphertext y shared secret
ciphertext, shared_secret = encapsulate(keypair)
```

---

## 9. Referencias

| Recurso | URL |
|---|---|
| **NIST SP 800-57** | [https://csrc.nist.gov/publications/detail/sp/800-57-part-1/rev-5/final](https://csrc.nist.gov/publications/detail/sp/800-57-part-1/rev-5/final) |
| **RFC 8446 (TLS 1.3)** | [https://datatracker.ietf.org/doc/html/rfc8446](https://datatracker.ietf.org/doc/html/rfc8446) |
| **CryptoHack** | [https://cryptohack.org/](https://cryptohack.org/) |
| **P-256 vs Curve25519** | [https://safecurves.cr.yp.to/](https://safecurves.cr.yp.to/) |
| **Post-Quantum Cryptography** | [https://csrc.nist.gov/projects/post-quantum-cryptography](https://csrc.nist.gov/projects/post-quantum-cryptography) |

---

## 📝 Entregable de portafolio

```markdown
# Cifrado Asimétrico — Ejercicios

## Ejercicio 1: RSA manual
- Generar claves RSA con p=61, q=53
- Cifrar y descifrar un mensaje
- Documentar cada paso matemático

## Ejercicio 2: Diffie-Hellman
- Implementar DH en Python
- Demostrar que ambos calculan la misma clave
- Mostrar que un eavesdropper no puede calcularla

## Ejercicio 3: ECDH
- Generar claves ECC con curve P-256
- Calcular shared secret
- Cifrar mensaje con AES usando shared secret

## Ejercicio 4: Comparar RSA vs ECC
- Generar claves de 128 bits de seguridad
- Comparar tiempos de generación
- Comparar tamaños de clave
```

---

**[⬅ Cifrado Simétrico](./02-criptografia-simetrica.md)** · **[→ Hash y Firmas](../hash-y-digitales/01-hash-y-firmas.md)**
