# 🛠️ Herramientas Criptográficas

> *"Elegir la herramienta correcta es tan importante como entender el algoritmo. Cada herramienta tiene su lugar en el ecosistema criptográfico."*

---

## 📋 Tabla de contenido

1. [Visión general](#1-visión-general)
2. [OpenSSL](#2-openssl)
3. [hashcat](#3-hashcat)
4. [John the Ripper](#4-john-the-ripper)
5. [CyberChef](#5-cyberchef)
6. [Python cryptography](#6-python-cryptography)
7. [GPG / age](#7-gpg--age)
8. [Comparativa final](#8-comparativa-final)
9. [Referencias](#9-referencias)

---

## 1. Visión general

### Herramientas por categoría

```
┌─────────────────────────────────────────────────────────────────┐
│                  ECOSISTEMA CRIPTOGRÁFICO                       │
├─────────────────────────────────────────────────────────────────┤
│                                                                  │
│  CIFRADO/DESCIFRADO        HASHING              ANÁLISIS        │
│  ┌──────────────┐         ┌──────────────┐     ┌──────────────┐│
│  │ OpenSSL      │         │ hashcat      │     │ CyberChef    ││
│  │ GPG          │         │ John         │     │ hash-analyzer││
│  │ age          │         │ Python       │     │              ││
│  │ Python crypt │         │              │     │              ││
│  └──────────────┘         └──────────────┘     └──────────────┘│
│                                                                  │
│  IMPLEMENTACIÓN           FIRMAS               CONTRASEÑAS      │
│  ┌──────────────┐         ┌──────────────┐     ┌──────────────┐│
│  │ Python crypt │         │ GPG          │     │ Argon2       ││
│  │ OpenSSL      │         │ OpenSSL      │     │ bcrypt       ││
│  │ Bouncy Castle│         │ SSH keys     │     │ scrypt       ││
│  └──────────────┘         └──────────────┘     └──────────────┘│
│                                                                  │
└─────────────────────────────────────────────────────────────────┘
```

---

## 2. OpenSSL

### ¿Qué es?

**OpenSSL** es la suite de criptografía más completa y ampliamente utilizada. Es la base de la seguridad en internet (TLS/SSL).

### Instalación

```bash
# Linux
sudo apt-get install openssl

# macOS
brew install openssl

# Windows
# Descargar desde https://www.openssl.org/
```

### Comandos esenciales

#### Generación de claves

```bash
# RSA 2048 bits
openssl genpkey -algorithm RSA -out private.pem -pkeyopt rsa_keygen_bits:2048
openssl rsa -pubout -in private.pem -out public.pem

# RSA 4096 bits
openssl genpkey -algorithm RSA -out private.pem -pkeyopt rsa_keygen_bits:4096

# ECC (P-256)
openssl ecparam -genkey -name prime256v1 -noout -out ec_private.pem
openssl ec -in ec_private.pem -pubout -out ec_public.pem

# X25519
openssl genpkey -algorithm X25519 -out x25519_private.pem
openssl pkey -in x25519_private.pem -pubout -out x25519_public.pem
```

#### Cifrado/Descifrado

```bash
# AES-256-GCM (RECOMENDADO)
openssl enc -aes-256-gcm -in plaintext.txt -out ciphertext.bin -k "password123"
openssl enc -aes-256-gcm -d -in ciphertext.bin -out plaintext.txt -k "password123"

# AES-256-CBC
openssl enc -aes-256-cbc -in plaintext.txt -out ciphertext.bin -k "password123" -pbkdf2

# ChaCha20-Poly1305
openssl enc -chacha20-poly1305 -in plaintext.txt -out ciphertext.bin -k "password123"

# RSA (cifrado máximo ~245 bytes para RSA-2048)
openssl pkeyutl -encrypt -pubin -inkey public.pem -in secreto.txt -out secreto.enc
openssl pkeyutl -decrypt -inkey private.pem -in secreto.enc -out secreto.txt
```

#### Hashing

```bash
# SHA-256
echo -n "password" | openssl dgst -sha256

# SHA-512
echo -n "password" | openssl dgst -sha512

# HMAC-SHA256
echo -n "message" | openssl dgst -sha256 -hmac "secret_key"

# File hash
openssl dgst -sha256 archivo.zip
```

#### Firmas

```bash
# Firmar
openssl dgst -sha256 -sign private.pem -out firma.sig archivo.txt

# Verificar
openssl dgst -sha256 -verify public.pem -signature firma.sig archivo.txt

# Output: Verified OK
```

#### Certificados

```bash
# Generar certificado autofirmado
openssl req -x509 -newkey rsa:2048 -keyout key.pem -out cert.pem -days 365 -nodes

# Generar CSR (Certificate Signing Request)
openssl req -new -newkey rsa:2048 -keyout key.pem -out csr.pem

# Verificar certificado
openssl x509 -in cert.pem -text -noout
```

---

## 3. hashcat

### Referencia rápida de modos

| Modo | Algoritmo | Ejemplo hash |
|---|---|---|
| `0` | MD5 | `e10adc3949ba59abbe56e057f20f883e` |
| `100` | SHA-1 | `7c4a8d09ca3762af61e59520943dc26494f8941b` |
| `1400` | SHA-256 | `ef92b778bafe771e89245b89ecbc08a44a4e166c...` |
| `1800` | SHA-512 | `b109f3bbce284dc...` |
| `3200` | bcrypt | `$2b$12$LJ3m4ys3...` |
| `1000` | NTLM | `a4f49c406510bdc...` |
| `1800` | sha512crypt | `$6$rounds=5000$salt$hash...` |
| `3200` | bcrypt | `$2b$12$...` |

### Referencia rápida de ataques

```bash
# Diccionario
hashcat -m 0 -a 0 hash.txt rockyou.txt

# Fuerza bruta
hashcat -m 0 -a 3 hash.txt ?a?a?a?a?a?a

# Reglas
hashcat -m 0 -a 0 hash.txt rockyou.txt -r rules/best64.rule

# Hibrido
hashcat -m 0 -a 6 hash.txt rockyou.txt ?a?a?a

# Combinaciones
hashcat -m 0 -a 1 hash.txt word1.txt word2.txt
```

### Caraktersets para fuerza bruta

```
?a  = todos los caracteres (a-z A-Z 0-9 símbolos)
?l  = minúsculas (a-z)
?u  = mayúsculas (A-Z)
?d  = dígitos (0-9)
?s  = símbolos (!@#$%^&*)
?b  = binario (0x00-0xff)

Ejemplo: ?u?l?l?l?l?l = 2 mayúsculas + 4 minúsculas
```

---

## 4. John the Ripper

### Formatos comunes

```bash
# Auto-detectar
john hash.txt

# Especificar formato
john --format=raw-md5 hash.txt
john --format=raw-sha256 hash.txt
john --format=bcrypt hash.txt
john --format=nt hash.txt
john --format=sha512crypt shadow.txt
```

### Modos de ataque

```bash
# Diccionario
john --wordlist=rockyou.txt hash.txt

# Fuerza bruta
john --incremental hash.txt

# Single (basado en username)
john --single hash.txt

# Rules
john --wordlist=rockyou.txt --rules hash.txt
```

### Ver resultados

```bash
# Mostrar hashes crackeados
john --show hash.txt

# Output:
# user1:password1
# user2:password2
```

---

## 5. CyberChef

### Operaciones más usadas

| Operación | Uso |
|---|---|
| **From Base64** | Decodificar Base64 |
| **To Base64** | Codificar Base64 |
| **From Hex** | Decodificar hexadecimal |
| **AES Encrypt/Decrypt** | Cifrar/descifrar AES |
| **RSA Encrypt/Decrypt** | Cifrar/descifrar RSA |
| **XOR** | Operación XOR |
| **SHA2/SHA3** | Calcular hash |
| **Gunzip** | Descomprimir |
| **Regex** | Buscar patrones |
| **Entropy** | Medir entropía |

### Cadena de operaciones típica

```
1. Análisis de malware:
   Input → From Base64 → Gunzip → AES Decrypt → Output

2. Decodificar payload:
   Input → From Hex → XOR → Strings → Output

3. Analizar hash:
   Input → SHA256 → To Hex → Output
```

---

## 6. Python cryptography

### Ejemplos completos

```python
from cryptography.hazmat.primitives.ciphers.aead import AESGCM, ChaCha20Poly1305
from cryptography.hazmat.primitives.asymmetric import rsa, padding
from cryptography.hazmat.primitives import hashes, serialization
from cryptography.hazmat.backends import default_backend
import os

# === AES-256-GCM ===
key = AESGCM.generate_key(bit_length=256)
aesgcm = AESGCM(key)
nonce = os.urandom(12)

# Cifrar
ct = aesgcm.encrypt(nonce, b"mensaje", b"metadata")

# Descifrar
pt = aesgcm.decrypt(nonce, ct, b"metadata")

# === RSA ===
private_key = rsa.generate_private_key(
    public_exponent=65537,
    key_size=2048,
    backend=default_backend()
)
public_key = private_key.public_key()

# Cifrar
ct = public_key.encrypt(
    b"mensaje",
    padding.OAEP(
        mgf=padding.MGF1(algorithm=hashes.SHA256()),
        algorithm=hashes.SHA256(),
        label=None
    )
)

# Descifrar
pt = private_key.decrypt(
    ct,
    padding.OAEP(
        mgf=padding.MGF1(algorithm=hashes.SHA256()),
        algorithm=hashes.SHA256(),
        label=None
    )
)

# === Firmar ===
from cryptography.hazmat.primitives.asymmetric import utils

message = b"documento"
signature = private_key.sign(
    message,
    padding.PSS(
        mgf=padding.MGF1(hashes.SHA256()),
        salt_length=padding.PSS.MAX_LENGTH
    ),
    hashes.SHA256()
)

# Verificar
public_key.verify(
    signature,
    message,
    padding.PSS(
        mgf=padding.MGF1(hashes.SHA256()),
        salt_length=padding.PSS.MAX_LENGTH
    ),
    hashes.SHA256()
)
```

---

## 7. GPG / age

### GPG

```bash
# Generar clave
gpg --gen-key

# Listar claves
gpg --list-keys

# Cifrar
gpg --encrypt --recipient email@domain.com archivo.txt

# Descifrar
gpg --decrypt archivo.txt.gpg > archivo.txt

# Firmar
gpg --sign archivo.txt

# Verificar
gpg --verify archivo.txt.sig
```

### age

```bash
# Generar clave
age-keygen -o key.txt
# Public key: age1...

# Cifrar
age -r age1... -o archivo.age archivo.txt

# Descifrar
age -d -i key.txt -o archivo.txt archivo.age
```

---

## 8. Comparativa final

| Herramienta | Categoría | Velocidad | Facilidad | Ideal para |
|---|---|---|---|---|
| **OpenSSL** | Cifrado/Firmas | ⭐⭐⭐⭐⭐ | ⭐⭐ | Suite completa |
| **hashcat** | Cracking | ⭐⭐⭐⭐⭐ | ⭐⭐⭐ | Cracking masivo |
| **John the Ripper** | Cracking | ⭐⭐⭐⭐ | ⭐⭐⭐⭐ | Análisis rápido |
| **CyberChef** | Análisis | ⭐⭐⭐ | ⭐⭐⭐⭐⭐ | Transformaciones |
| **Python crypto** | Implementación | ⭐⭐⭐⭐ | ⭐⭐⭐ | Desarrollo |
| **GPG** | Encriptación | ⭐⭐⭐⭐ | ⭐⭐⭐ | Archivos |
| **age** | Encriptación | ⭐⭐⭐⭐⭐ | ⭐⭐⭐⭐⭐ | Archivos moderno |

### ¿Cuándo usar qué?

| Necesidad | Herramienta |
|---|---|
| **Cifrar archivo** | age o GPG |
| **Cifrar conexión** | OpenSSL (TLS) |
| **Crackear hash** | hashcat (GPU) o John |
| **Analizar ciphertext** | CyberChef |
| **Implementar en código** | Python cryptography |
| **Generar claves** | OpenSSL |
| **Firmar documento** | GPG o OpenSSL |
| **Hash de contraseña** | Argon2 (Python) |

---

## 9. Referencias

| Recurso | URL |
|---|---|
| **OpenSSL** | [https://www.openssl.org/](https://www.openssl.org/) |
| **hashcat** | [https://hashcat.net/hashcat/](https://hashcat.net/hashcat/) |
| **John the Ripper** | [https://www.openwall.com/john/](https://www.openwall.com/john/) |
| **CyberChef** | [https://gchq.github.io/CyberChef/](https://gchq.github.io/CyberChef/) |
| **Python cryptography** | [https://cryptography.io/](https://cryptography.io/) |
| **age** | [https://age-encryption.org/](https://age-encryption.org/) |
| **GPG** | [https://gnupg.org/](https://gnupg.org/) |

---

## 📝 Checklist de herramientas para laboratorio

```markdown
## Herramientas mínimas para criptografía

### Software
- [ ] OpenSSL instalado
- [ ] hashcat instalado (con GPU si es posible)
- [ ] John the Ripper instalado
- [ ] CyberChef bookmarked
- [ ] Python cryptography instalado
- [ ] GPG configurado
- [ ] age instalado

### Wordlists
- [ ] rockyou.txt (o similar)
- [ ] Reglas de hashcat (rules/)
- [ ] Custom wordlists para el contexto

### Hardware
- [ ] GPU NVIDIA (para hashcat)
- [ ] VM con Kali Linux (para herramientas)
- [ ] Conexión a internet (para CyberChef)

### Formación
- [ ] CryptoHack: 5+ retos completados
- [ ] Cryptopals: 3+ sets completados
- [ ] OpenSSL: comandos básicos dominados
- [ ] Python: implementar AES y RSA
```

---

**[⬅ Herramientas de Criptoanalisis](../criptoanalisis/02-herramientas-criptoanalisis.md)** · **[Volver al módulo](../README.md)**
