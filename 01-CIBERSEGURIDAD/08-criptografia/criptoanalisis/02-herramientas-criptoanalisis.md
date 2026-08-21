# 🛠️ Herramientas de Criptoanalisis

> *"Las herramientas de criptoanalisis son el martillo del forense: úsalas con cuidado y solo en el contexto correcto."*

---

## 📋 Tabla de contenido

1. [hashcat](#1-hashcat)
2. [John the Ripper](#2-john-the-ripper)
3. [CyberChef](#3-cyberchef)
4. [Ataque con Python](#4-ataque-con-python)
5. [Comparativa de herramientas](#5-comparativa-de-herramientas)
6. [Flujos de trabajo](#6-flujos-de-trabajo)
7. [Referencias](#7-referencias)

---

## 1. hashcat

### Instalación

```bash
# Linux (con GPU NVIDIA)
sudo apt-get install hashcat

# macOS (sin GPU)
brew install hashcat

# Windows
# Descargar desde https://hashcat.net/hashcat/
```

### Modos de hash

| Modo | Algoritmo | Ejemplo |
|---|---|---|
| `0` | MD5 | `e10adc3949ba59abbe56e057f20f883e` |
| `100` | SHA-1 | `7c4a8d09ca3762af61e59520943dc26494f8941b` |
| `1400` | SHA-256 | `ef92b778bafe771e89245b89ecbc08a44a4e166c...` |
| `1800` | SHA-512 | `b109f3bbce284dc...` |
| `3200` | bcrypt | `$2b$12$LJ3m4ys3...` |
| `1000` | NTLM | `a4f49c406510bdc...` |
| `5500` | NetNTLMv1 | `admin::WORKGROUP:...` |
| `5600` | NetNTLMv2 | `admin::WORKGROUP:...` |

### Modos de ataque

```bash
# 1. Diccionario (la más común)
hashcat -m 0 -a 0 hash.txt rockyou.txt

# 2. Fuerza bruta
hashcat -m 0 -a 3 hash.txt ?a?a?a?a?a?a
# ?a = todos los caracteres (a-z, A-Z, 0-9, símbolos)

# 3. Reglas (mutaciones del diccionario)
hashcat -m 0 -a 0 hash.txt rockyou.txt -r rules/best64.rule
hashcat -m 0 -a 0 hash.txt rockyou.txt -r rules/toggles1.rule

# 4. Hibrido (diccionario + fuerza bruta)
hashcat -m 0 -a 6 hash.txt rockyou.txt ?a?a?a

# 5. Combinaciones
hashcat -m 0 -a 1 hash.txt wordlist1.txt wordlist2.txt
```

### Reglas de hashcat

```
# Archivo de reglas (rules/best64.rule):
:               # No hacer nada
l               # Minúsculas
u               # Mayúsculas
c               # Capitalizar primera letra
t               # Toggle case
r               # Revertir string
d               # Duplicar último carácter
$f              # Agregar '$' al final
$1              # Agregar '1' al final
sa@             # Reemplazar 'a' con '@'
so0             # Reemplazar 'o' con '0'

# Ejemplo:
# Palabra: password
# Con regla l: password (sin cambio)
# Con regla c: Password
# Con regla t: pASSWORD
# Con regla $1: password1
# Con regla sa@: p@ssword
```

### Ejemplo completo

```bash
# Crackear hash MD5
hashcat -m 0 -a 0 hash.txt rockyou.txt --force

# Output:
# e10adc3949ba59abbe56e057f20f883e:123456
# Session..........: hashcat
# Status...........: Cracked
# Speed.#1.........: 12345.6 MH/s

# Ver resultados
hashcat -m 0 hash.txt --show
```

---

## 2. John the Ripper

### Instalación

```bash
# Linux
sudo apt-get install john

# macOS
brew install john

# Windows
# Descargar desde https://www.openwall.com/john/
```

### Modos de hash

```bash
# Auto-detectar formato
john --format=raw-md5 hash.txt
john --format=raw-sha256 hash.txt
john --format=bcrypt hash.txt
john --format=nt hash.txt  # NTLM

# Para hashes Linux (/etc/shadow)
john --format=sha512crypt shadow.txt
```

### Modos de ataque

```bash
# 1. Diccionario
john --wordlist=rockyou.txt hash.txt

# 2. Fuerza bruta
john --incremental hash.txt

# 3. Modo single (basado en el nombre de usuario)
john --single hash.txt

# 4. Modo doble (combinaciones)
john --wordlist=rockyou.txt --rules hash.txt

# 5. Personalizado
john --wordlist=rockyou.txt --format=raw-md5 hash.txt
```

### Comparativa John vs hashcat

| Característica | John the Ripper | hashcat |
|---|---|---|
| **GPU** | ⚠️ Soporte limitado | ✅ GPU NVIDIA/AMD |
| **Velocidad (CPU)** | ✅ Rápido | ⚠️ Medio |
| **Velocidad (GPU)** | ⚠️ Lento | ✅ Muy rápido |
| **Formats** | ⭐⭐⭐⭐⭐ | ⭐⭐⭐⭐ |
| **Reglas** | ✅ Integradas | ✅ Más flexibles |
| **Auto-detect** | ✅ Automático | ❌ Manual |
| **Uso ideal** | Análisis rápido | Cracking masivo |

---

## 3. CyberChef

### ¿Qué es?

**CyberChef** es una herramienta web para operaciones criptográficas y de datos:

```
URL: https://gchq.github.io/CyberChef/
```

### Operaciones disponibles

| Categoría | Operaciones |
|---|---|
| **Criptografía** | AES, DES, RSA, XOR, Base64, URL encode |
| **Hashing** | MD5, SHA-1, SHA-256, SHA-512, bcrypt |
| **Compresión** | gzip, bzip2, lzma, zlib |
| **Análisis** | Entropy, Frequency, Hex dump |
| **Transformación** | Replace, Split, Merge, Regex |

### Ejemplos de uso

```
1. Descifrar base64
   Input: "SGVsbG8gV29ybGQ="
   Operation: From Base64
   Output: "Hello World"

2. Cifrar con AES-256-CBC
   Operation: AES Encrypt
   Key: "my-secret-key-123"
   IV: (auto-generado)

3. Calcular hash
   Operation: SHA256
   Input: "password123"

4. XOR con clave
   Operation: XOR
   Key: "secret"
```

### Cadena de operaciones

```
CyberChef permite encadenar operaciones:

Input → Base64 Decode → AES Decrypt → Gunzip → Output

Esto es útil para:
- Decodificar payloads ofuscados
- Analizar malware empaquetado
- Resolver retos CTF
```

---

## 4. Ataque con Python

### Script de cracking de hashes

```python
#!/usr/bin/env python3
"""
crack_hash.py — Cracker de hashes por diccionario
Uso educativo: solo con datos propios o autorizados.
"""

import hashlib
import sys
from pathlib import Path

ALGORITHMS = {
    32: ("MD5", hashlib.md5),
    40: ("SHA-1", hashlib.sha1),
    64: ("SHA-256", hashlib.sha256),
    96: ("SHA-384", hashlib.sha384),
    128: ("SHA-512", hashlib.sha512),
}

def identify_hash(h):
    """Identificar algoritmo por longitud"""
    h = h.strip().lower()
    if not all(c in "0123456789abcdef" for c in h):
        return "desconocido"
    return ALGORITHMS.get(len(h), ("desconocido", None))[0]

def crack_hash(target, wordlist):
    """Crackear hash por diccionario"""
    target = target.strip().lower()
    info = ALGORITHMS.get(len(target))
    
    if not info or not info[1]:
        return None
    
    name, hash_func = info
    
    with open(wordlist, 'r', encoding='utf-8', errors='ignore') as f:
        for word in f:
            word = word.strip()
            if not word:
                continue
            
            # Probar word tal cual
            if hash_func(word.encode()).hexdigest() == target:
                return word
            
            # Probar variaciones comunes
            variations = [
                word.upper(),
                word.capitalize(),
                word + "1",
                word + "123",
                word + "!",
            ]
            for var in variations:
                if hash_func(var.encode()).hexdigest() == target:
                    return var
    
    return None

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print(f"Uso: {sys.argv[0]} <hash> <wordlist>")
        sys.exit(1)
    
    target = sys.argv[1]
    wordlist = sys.argv[2]
    
    print(f"Hash: {target}")
    print(f"Algoritmo: {identify_hash(target)}")
    print(f"Wordlist: {wordlist}")
    print("Buscando...")
    
    result = crack_hash(target, wordlist)
    if result:
        print(f"✅ RESUELTO: {result}")
    else:
        print("❌ No encontrado")
```

### Script de Padding Oracle

```python
#!/usr/bin/env python3
"""
padding_oracle.py — Padding Oracle Attack (educativo)
"""

import os
from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad

def padding_oracle(key, ciphertext):
    """Simula un servidor vulnerable"""
    try:
        iv = ciphertext[:16]
        ct = ciphertext[16:]
        cipher = AES.new(key, AES.MODE_CBC, iv)
        plaintext = unpad(cipher.decrypt(ct), 16)
        return True
    except ValueError:
        return False

def attack(oracle, ciphertext, block_size=16):
    """Padding Oracle Attack"""
    n_blocks = len(ciphertext) // block_size
    plaintext = b""
    
    for block_idx in range(n_blocks - 1, -1, -1):
        block = ciphertext[block_idx * block_size:(block_idx + 1) * block_size]
        intermediate = b""
        
        for byte_idx in range(block_size - 1, -1, -1):
            padding_byte = block_size - byte_idx
            prefix = os.urandom(byte_idx)
            
            for guess in range(256):
                test = bytes([guess]) + intermediate
                # Construir IV de prueba
                test_prefix = prefix + bytes([guess ^ padding_byte])
                for b in intermediate:
                    test_prefix += bytes([b ^ (padding_byte - 1)])
                
                if oracle(test_prefix + block):
                    intermediate = bytes([guess ^ padding_byte]) + intermediate
                    break
        
        plaintext = intermediate + plaintext
    
    return plaintext

# Ejemplo de uso
if __name__ == "__main__":
    key = os.urandom(32)
    secret = b"Password: SuperSecret123!"
    
    # Cifrar
    iv = os.urandom(16)
    cipher = AES.new(key, AES.MODE_CBC, iv)
    ciphertext = iv + cipher.encrypt(pad(secret, 16))
    
    print(f"Secret: {secret}")
    print(f"Ciphertext: {ciphertext.hex()[:64]}...")
    
    # Atacar
    result = attack(lambda ct: padding_oracle(key, ct), ciphertext)
    print(f"Descifrado: {result}")
```

---

## 5. Comparativa de herramientas

| Herramienta | Tipo | Velocidad | Uso ideal |
|---|---|---|---|
| **hashcat** | GPU cracking | ⭐⭐⭐⭐⭐ | Cracking masivo |
| **John the Ripper** | CPU cracking | ⭐⭐⭐⭐ | Análisis rápido |
| **CyberChef** | Análisis web | ⭐⭐⭐ | Transformaciones |
| **Python** | Scripting | ⭐⭐ | Ataques custom |
| **hash-analyzer.py** | Identificación | ⭐⭐⭐ | Identificar hashes |

### ¿Cuándo usar cada una?

| Necesidad | Herramienta |
|---|---|
| **Identificar tipo de hash** | hash-analyzer.py, CyberChef |
| **Crackear MD5/SHA-1/SHA-256** | hashcat (con GPU) |
| **Crackear bcrypt/Argon2** | hashcat (GPU) o John (CPU) |
| **Transformaciones rápidas** | CyberChef |
| **Ataque personalizado** | Python script |
| **Crackear hashes de Windows** | hashcat -m 1000 (NTLM) |
| **Crackear hashes de Linux** | john --format=sha512crypt |

---

## 6. Flujos de trabajo

### Flujo 1: Cracking de hash

```bash
# 1. Identificar hash
hash-analyzer.py -H e10adc3949ba59abbe56e057f20f883e
# Output: MD5

# 2. Preparar wordlist
# rockyou.txt (si no está disponible, usar una pequeña)

# 3. Cracker con hashcat
hashcat -m 0 -a 0 hash.txt rockyou.txt

# 4. Ver resultados
hashcat -m 0 hash.txt --show
```

### Flujo 2: Análisis de ciphertext

```bash
# 1. Abrir CyberChef
# https://gchq.github.io/CyberChef/

# 2. Pegar ciphertext

# 3. Probar operaciones:
# - Base64 Decode
# - Hex Decode
# - AES Decrypt (probar diferentes claves)
# - XOR (probar diferentes claves)

# 4. Si está comprimido, agregar:
# - Gunzip
# - Bzip2 Decompress
```

### Flujo 3: Análisis de malware criptografico

```bash
# 1. Extraer strings del malware
strings malware.exe | grep -E "[0-9a-f]{32}"  # Posibles hashes

# 2. Identificar algoritmos
# Buscar: AES, RSA, DES, XOR en strings

# 3. Usar CyberChef para decodificar payloads
# Si el payload está base64 encoded

# 4. Documentar hallazgos
echo "Algoritmos encontrados: AES-256-CBC, SHA-256" > analysis.txt
```

---

## 7. Referencias

| Recurso | URL |
|---|---|
| **hashcat** | [https://hashcat.net/hashcat/](https://hashcat.net/hashcat/) |
| **John the Ripper** | [https://www.openwall.com/john/](https://www.openwall.com/john/) |
| **CyberChef** | [https://gchq.github.io/CyberChef/](https://gchq.github.io/CyberChef/) |
| **CryptoHack** | [https://cryptohack.org/](https://cryptohack.org/) |
| **hashcat rules** | [https://hashcat.net/wiki/doku.php?id=rule_based_attack](https://hashcat.net/wiki/doku.php?id=rule_based_attack) |

---

**[⬅ Técnicas de Criptoanalisis](./01-tecnicas-ataque.md)** · **[→ Práctica](../practica/01-desafios-criptografia.md)**
