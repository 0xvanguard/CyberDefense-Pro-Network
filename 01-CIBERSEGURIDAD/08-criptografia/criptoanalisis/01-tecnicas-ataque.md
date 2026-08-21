# ⚔️ Técnicas de Criptoanalisis

> *"Criptoanalisis no es romper criptografía: es encontrar debilidades en su implementación. La mayoría de ataques no atacan el algoritmo, sino cómo se usa."*

---

## 📋 Tabla de contenido

1. [¿Qué es el criptoanalisis?](#1-qué-es-el-criptoanalisis)
2. [Ataques a hashes](#2-ataques-a-hashes)
3. [Ataques a cifrado simétrico](#3-ataques-a-cifrado-simétrico)
4. [Ataques a cifrado asimétrico](#4-ataques-a-cifrado-asimétrico)
5. [Ataques a implementaciones](#5-ataques-a-implementaciones)
6. [Padding Oracle Attack](#6-padding-oracle-attack)
7. [Ataques de timing](#7-ataques-de-timing)
8. [Criptoanalisis cuántico](#8-criptoanalisis-cuántico)
9. [Referencias](#9-referencias)

---

## 1. ¿Qué es el criptoanalisis?

### Definición

El **criptoanalisis** es el estudio de técnicas para romper o eludir sistemas criptográficos sin acceso a la clave.

### Tipos de ataques

| Tipo | Acceso del atacante | Objetivo |
|---|---|---|
| **Solo ciphertext** | Solo ve ciphertext | Descifrar mensaje |
| **Ciphertext conocido** | Tiene pares (plaintext, ciphertext) | Encontrar clave |
| **Texto plano conocido** | Sabe el contenido de algunos mensajes | Descifrar otros |
| **Texto plano elegido** | Elige qué mensajes cifrar | Encontrar clave |
| **Texto plano adaptativo** | Elige mensajes según respuestas anteriores | Romper el sistema |

---

## 2. Ataques a hashes

### Fuerza bruta

```python
import hashlib
import itertools
import string
import time

def brute_force_md5(target_hash, max_length=6):
    """Fuerza bruta para MD5 (solo fines educativos)"""
    chars = string.ascii_lowercase + string.digits
    attempts = 0
    start_time = time.time()
    
    for length in range(1, max_length + 1):
        for combo in itertools.product(chars, repeat=length):
            password = "".join(combo)
            attempts += 1
            if hashlib.md5(password.encode()).hexdigest() == target_hash:
                elapsed = time.time() - start_time
                print(f"¡Encontrado! '{password}' en {attempts} intentos ({elapsed:.2f}s)")
                return password
    
    print(f"No encontrado en {attempts} intentos")
    return None

# Ejemplo
target = hashlib.md5(b"hello").hexdigest()
brute_force_md5(target, max_length=5)
```

### Dictionary attack

```bash
# hashcat
hashcat -m 0 -a 0 hash.txt rockyou.txt
# -m 0: MD5
# -a 0: modo diccionario

# John the Ripper
john --wordlist=rockyou.txt hash.txt

# Reglas de hashcat (mutaciones)
hashcat -m 0 -a 0 hash.txt rockyou.txt -r rules/best64.rule
# best64.rule: agrega números, mayúsculas, símbolos
```

### Rainbow tables

```python
# Rainbow tables: tabla precomputada de hashes
# Vulnerable a: SALT

# Sin salt:
# password → e10adc3949ba59abbe56e057f20f883e
# password → e10adc3949ba59abbe56e057f20f883e  (¡mismo hash!)

# Con salt:
# salt1 + password → a1b2c3d4e5f6...
# salt2 + password → f6e5d4c3b2a1...  (¡hash diferente!)
```

### Ataques específicos

| Algoritmo | Ataque | Método |
|---|---|---|
| **MD5** | Colisión | Ataque de.Messages (2^18) |
| **SHA-1** | Colisión | SHAttered (2^63) |
| **bcrypt** | Fuerza bruta | Limitado por factor de costo |
| **Argon2** | Fuerza bruta | Limitado por memoria + CPU |

---

## 3. Ataques a cifrado simétrico

### ECB pattern leakage

```python
from Crypto.Cipher import AES
from PIL import Image
import numpy as np

# ECB revela patrones porque bloques idénticos → ciphertext idéntico

# Ejemplo: cifrar imagen con ECB
def ecb_pattern_leakage(image_path):
    """
    Dado un ciphertext ECB, se pueden ver patrones
    porque bloques de pixels similares producen
    ciphertext similar.
    """
    img = Image.open(image_path)
    img_array = np.array(img)
    
    # Cifrar cada bloque de 16 bytes con ECB
    key = os.urandom(32)
    cipher = AES.new(key, AES.MODE_ECB)
    
    # El patrón original se mantiene visible en el ciphertext
    # ¡ECB es inseguro para datos estructurados!
```

### Revenge attack (ciphertext malleability)

```python
# Si se usa ECB o CBC sin autenticación,
# un atacante puede modificar el ciphertext

# Ejemplo: XOR de un byte específico
# plaintext: "Transfer $1000 to Alice"
# ciphertext: [C1][C2][C3][C4]...
# Modificar C2 para cambiar "$1000" → "$9000"

# DEFENSA: usar GCM o Poly1305 (autenticación)
```

---

## 4. Ataques a cifrado asimétrico

### RSA: petits modulo attack

```python
# Si p y q son muy diferentes, se puede factorizar
# usando Fermat's factorization

def fermat_factor(n):
    """Factoriza n si p y q son cercanos"""
    import math
    a = math.isqrt(n) + 1
    b2 = a*a - n
    while not is_perfect_square(b2):
        a += 1
        b2 = a*a - n
    b = math.isqrt(b2)
    return (a - b, a + b)

# Si p ≈ q (muy cercanos), se puede factorizar rápido
# DEFENSA: generar p y q con diferencia significativa
```

### RSA: Wiener's attack

```python
# Si d es muy pequeño (d < n^0.25), se puede atacar
# con continued fractions

def wiener_attack(e, n):
    """Ataque de Wiener para RSA con d pequeño"""
    # Usar continued fractions para aproximar e/n
    # Si d es pequeño, el ataque funciona
    pass

# DEFENSA: asegurar que d > n^0.25
# O mejor: usar d = e⁻¹ mod φ(n) (que siempre genera d grande)
```

### DH: Logjam attack

```bash
# Logjam (2015): ataque a DH con grupos de 1024 bits
# Usa la "number field sieve" para factorizar

# DEFENSA:
# - Usar DH de 2048+ bits
# - O mejor: usar ECDH
```

---

## 5. Ataques a implementaciones

### Padding Oracle Attack

```python
"""
Padding Oracle Attack: explota una fuga de información
sobre si el padding del descifrado es válido.
"""

def padding_oracle_attack(oracle, ciphertext, block_size=16):
    """
    Descifrar ciphertext usando un oracle que revela
    si el padding es válido.
    
    oracle: función que retorna True si el padding es válido
    ciphertext: el ciphertext a descifrar
    """
    n_blocks = len(ciphertext) // block_size
    plaintext = b""
    
    for block_idx in range(n_blocks - 1, -1, -1):
        block = ciphertext[block_idx * block_size:(block_idx + 1) * block_size]
        decrypted_block = b""
        
        for byte_idx in range(block_size - 1, -1, -1):
            padding_byte = block_size - byte_idx
            
            # Crear prefix para controlar el padding
            prefix = bytearray(os.urandom(byte_idx))
            
            for guess in range(256):
                prefix[byte_idx] = guess
                test = bytes(prefix) + block
                
                if oracle(test):
                    # Verificar que no es falso positivo
                    if byte_idx == block_size - 1:
                        # Cambiar el byte anterior para confirmar
                        prefix[byte_idx - 1] ^= 1
                        if oracle(bytes(prefix) + block):
                            continue
                    
                    decrypted_byte = guess ^ padding_byte
                    decrypted_block = bytes([decrypted_byte]) + decrypted_block
                    break
        
        plaintext = decrypted_block + plaintext
    
    return plaintext
```

### Ataque a CBC (BEAST)

```python
"""
BEAST (Browser Exploit Against SSL/TLS)
Ataque a CBC en TLS 1.0
"""
# El ataque explota la predecibilidad del IV en TLS 1.0
# DEFENSA: usar TLS 1.2+ con GCM
```

---

## 6. Padding Oracle Attack

### Explicación detallada

```
En CBC, el descifrado de cada bloque depende del anterior:

P_i = D_k(C_i) XOR C_{i-1}

Si el padding es PKCS#7 y el servidor revela "padding válido/inválido":
1. Modificar C_{i-1} byte por byte
2. Cuando el oracle dice "válido", sabemos P_i XOR C_{i-1} XOR guess
3. Calcular P_i = guess XOR padding_byte
```

### Ejemplo completo

```python
import os
from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad

class VulnerableServer:
    """Servidor vulnerable a Padding Oracle"""
    def __init__(self, key):
        self.key = key
    
    def encrypt(self, plaintext):
        iv = os.urandom(16)
        cipher = AES.new(self.key, AES.MODE_CBC, iv)
        ciphertext = cipher.encrypt(pad(plaintext, 16))
        return iv + ciphertext
    
    def decrypt_and_check_padding(self, ciphertext):
        """VULNERABLE: revela si el padding es válido"""
        try:
            iv = ciphertext[:16]
            ct = ciphertext[16:]
            cipher = AES.new(self.key, AES.MODE_CBC, iv)
            plaintext = unpad(cipher.decrypt(ct), 16)
            return True  # Padding válido
        except ValueError:
            return False  # Padding inválido

# Simular ataque
key = os.urandom(32)
server = VulnerableServer(key)

# Mensaje secreto
secret = b"Password: SuperSecret123!"
ciphertext = server.encrypt(secret)

# Padding Oracle Attack
print(f"Ciphertext original: {ciphertext.hex()[:64]}...")
print("Atacante puede descifrar usando el oracle...")
```

### Defensa contra Padding Oracle

```python
# SOLUCIÓN: usar GCM en lugar de CBC
from cryptography.hazmat.primitives.ciphers.aead import AESGCM

key = AESGCM.generate_key()
aesgcm = AESGCM(key)
nonce = os.urandom(12)

# GCM es autenticado: no hay padding oracle
ciphertext = aesgcm.encrypt(nonce, plaintext, associated_data)
# El tag de autenticación detecta cualquier modificación
```

---

## 7. Ataques de timing

### ¿Qué es?

Un **ataque de timing** mide cuánto tiempo toma una operación criptográfica para deducir información secreta.

### Ejemplo: comparación de strings

```python
# MAL: comparación timing-vulnerable
def vulnerable_compare(a, b):
    if len(a) != len(b):
        return False
    for i in range(len(a)):
        if a[i] != b[i]:
            return False  # ¡Retorna inmediatamente!
    return True

# Un atacante puede medir cuánto tiempo tarda
# y deducir byte por byte de la clave

# BIEN: comparación constante-time
def secure_compare(a, b):
    result = 0
    for x, y in zip(a, b):
        result |= x ^ y  # XOR no revela timing
    return result == 0 and len(a) == len(b)
```

### Ejemplo: RSA timing attack

```python
# En RSA, si la implementación revela timing durante
# la exponenciación modular, se puede deducir la clave privada

# DEFENSA: usar implementaciones constant-time
# (Python's cryptography library es constant-time)
```

---

## 8. Criptoanalisis cuántico

### Algoritmo de Shor

```python
"""
Algoritmo de Shor (1994):
- Factoriza números grandes en tiempo polinómico
- Rompe RSA, DH y ECC
- Requiere computadora cuántica con ~4000 qubits (estimado)
"""
# No implementable aún, pero amenaza futura

# Impacto:
# - RSA-2048: vulnerable a Shor
# - DH-2048: vulnerable a Shor
# - ECC-256: vulnerable a Shor
# - AES-256: resistente (Shor no lo afecta directamente)
# - SHA-256: resistente (Grojer reduce a 128 bits)
```

### Algoritmo de Grover

```python
"""
Algoritmo de Grover (1996):
- Busca en una base de datos no estructurada en √N
- Reduce la seguridad de hashes y cifrado simétrico a la mitad

Impacto:
- AES-128 → 64 bits de seguridad (insuficiente)
- AES-256 → 128 bits de seguridad (seguro)
- SHA-256 → 128 bits de seguridad (seguro)
"""
# DEFENSA: usar claves el doble de grandes
# AES-256 sigue siendo seguro contra computadoras cuánticas
```

### Post-quantum cryptography

| Algoritmo | Tipo | NIST Status |
|---|---|---|
| **CRYSTALS-Kyber** | Key encapsulation | ✅ Estándar |
| **CRYSTALS-Dilithium** | Firmas | ✅ Estándar |
| **FALCON** | Firmas | ✅ Estándar |
| **SPHINCS+** | Firmas (hash-based) | ✅ Estándar |

---

## 9. Referencias

| Recurso | URL |
|---|---|
| **CryptoHack** | [https://cryptohack.org/](https://cryptohack.org/) |
| **Cryptopals** | [https://cryptopals.com/](https://cryptopals.com/) |
| **hashcat wiki** | [https://hashcat.net/wiki/doku.php](https://hashcat.net/wiki/doku.php) |
| **Padding Oracle** | [https://en.wikipedia.org/wiki/Padding_oracle_attack](https://en.wikipedia.org/wiki/Padding_oracle_attack) |
| **Post-Quantum Crypto** | [https://csrc.nist.gov/projects/post-quantum-cryptography](https://csrc.nist.gov/projects/post-quantum-cryptography) |

---

## 📝 Entregable de portafolio

```markdown
# Criptoanalisis — Ejercicios

## Ejercicio 1: Padding Oracle
- Implementar Padding Oracle Attack
- Descifrar un ciphertext sin conocer la clave
- Documentar el proceso paso a paso

## Ejercicio 2: ECB Pattern
- Cifrar una imagen con ECB
- Mostrar que los patrones son visibles
- Comparar con CBC y GCM

## Ejercicio 3: Hash cracking
- Crear hashes MD5 de 10 contraseñas comunes
- Crackear con hashcat en modo diccionario
- Medir tiempos y documentar resultados

## Ejercicio 4: Timing attack
- Implementar ataque de timing a una comparación
- Medir la diferencia de tiempo
- Implementar versión constant-time
```

---

**[⬅ Hash y Firmas](../hash-y-digitales/01-hash-y-firmas.md)** · **[→ Herramientas de Criptoanalisis](./02-herramientas-criptoanalisis.md)**
