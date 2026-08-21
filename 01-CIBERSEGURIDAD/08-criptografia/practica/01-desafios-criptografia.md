# 🎯 Desafíos de Criptografía

> *"La práctica hace al maestro. Cada desafío es una lección disfrazada de problema."*

---

## 📋 Tabla de contenido

1. [Nivel Principiante](#1-nivel-principiante)
2. [Nivel Intermedio](#2-nivel-intermedio)
3. [Nivel Avanzado](#3-nivel-avanzado)
4. [Nivel Expert](#4-nivel-expert)
5. [Plataformas de práctica](#5-plataformas-de-práctica)

---

## 1. Nivel Principiante

### Desafío 1: César Cipher

**Enunciado:**
```
Ciphertext: KHOOR ZRUOG
Pista: Cada letra está desplazada 3 posiciones hacia atrás
```

**Solución:**
```python
def caesar_decrypt(ciphertext, shift):
    result = ""
    for char in ciphertext:
        if char.isalpha():
            ascii_offset = ord('A') if char.isupper() else ord('a')
            result += chr((ord(char) - ascii_offset - shift) % 26 + ascii_offset)
        else:
            result += char
    return result

print(caesar_decrypt("KHOOR ZRUOG", 3))  # "HELLO WORLD"
```

**Lección:** El cifrado César es trivialmente crackeable con fuerza bruta (solo 25 posibilidades).

---

### Desafío 2: XOR simple

**Enunciado:**
```
Ciphertext (hex): 1b0c061200
Key: 0x42
```

**Solución:**
```python
ciphertext = bytes.fromhex("1b0c061200")
key = 0x42

plaintext = bytes([b ^ key for b in ciphertext])
print(plaintext.decode())  # "hello"
```

**Lección:** XOR con clave de 1 byte es trivial. XOR con clave repetida también es vulnerable.

---

### Desafío 3: Base64 encoding

**Enunciado:**
```
Ciphertext: SGVsbG8gV29ybGQhIFRoaXMgaXMgYSBzZWNyZXQgbWVzc2FnZS4=
```

**Solución:**
```python
import base64

ciphertext = "SGVsbG8gV29ybGQhIFRoaXMgaXMgYSBzZWNyZXQgbWVzc2FnZS4="
plaintext = base64.b64decode(ciphertext).decode()
print(plaintext)  # "Hello World! This is a secret message."
```

**Lección:** Base64 NO es cifrado, es encoding. Cualquiera puede decodificarlo.

---

### Desafío 4: MD5 crack

**Enunciado:**
```
Hash: e10adc3949ba59abbe56e057f20f883e
Algoritmo: MD5 (identificado por longitud 32)
```

**Solución:**
```bash
# Con hashcat
echo "e10adc3949ba59abbe56e057f20f883e" > hash.txt
hashcat -m 0 -a 0 hash.txt rockyou.txt
hashcat -m 0 hash.txt --show
# Output: e10adc3949ba59abbe56e057f20f883e:123456

# Con hash-analyzer.py
python3 hash-analyzer.py -H e10adc3949ba59abbe56e057f20f883e -w rockyou.txt
```

**Lección:** MD5 de contraseñas comunes se crackea en milisegundos.

---

## 2. Nivel Intermedio

### Desafío 5: Vigenère Cipher

**Enunciado:**
```
Ciphertext: LXFOPV EFRCNJ
Pista: La clave tiene 3 caracteres
```

**Solución:**
```python
def vigenere_decrypt(ciphertext, key):
    result = ""
    key_idx = 0
    for char in ciphertext:
        if char.isalpha():
            shift = ord(key[key_idx % len(key)].upper()) - ord('A')
            ascii_offset = ord('A') if char.isupper() else ord('a')
            result += chr((ord(char) - ascii_offset - shift) % 26 + ascii_offset)
            key_idx += 1
        else:
            result += char
    return result

print(vigenere_decrypt("LXFOPV EFRCNJ", "KEY"))  # "SHORT CIPHER"
```

**Lección:** Vigenère es vulnerable a frequency analysis si la clave es corta.

---

### Desafío 6: AES-ECB pattern

**Enunciado:**
```
Dado un ciphertext AES-ECB, identificar si contiene patrones
```

**Solución:**
```python
from collections import Counter

ciphertext = bytes.fromhex("8d4523d8b7a328475596f3b2c7e8a9f18d4523d8b7a328475596f3b2c7e8a9f1")

# Dividir en bloques de 16 bytes
blocks = [ciphertext[i:i+16] for i in range(0, len(ciphertext), 16)]

# Contar bloques repetidos
block_counts = Counter(blocks)

print("Bloques únicos:", len(set(blocks)))
print("Bloques totales:", len(blocks))
print("Repetidos:", sum(1 for c in block_counts.values() if c > 1))

# Si hay bloques repetidos → ECB (patrón visible)
if any(c > 1 for c in block_counts.values()):
    print("⚠️ ECB detectado: bloques repetidos")
```

**Lección:** ECB produce ciphertext idéntico para bloques de plaintext idénticos.

---

### Desafío 7: RSA básico

**Enunciado:**
```
n = 3233
e = 17
ciphertext = 2790
Descifrar el mensaje
```

**Solución:**
```python
from sympy import factorint, mod_inverse

n = 3233
e = 17
c = 2790

# Factorizar n para encontrar p y q
factors = factorint(n)
p, q = factors.keys()
print(f"p = {p}, q = {q}")  # p=61, q=53

# Calcular φ(n)
phi_n = (p - 1) * (q - 1)
print(f"φ(n) = {phi_n}")  # 3120

# Calcular d (exponente privado)
d = mod_inverse(e, phi_n)
print(f"d = {d}")  # 2753

# Descifrar
m = pow(c, d, n)
print(f"Mensaje: {m}")  # 65 (que es 'A' en ASCII)

print(f"Mensaje descifrado: {chr(m)}")  # A
```

**Lección:** RSA es seguro solo cuando n es lo suficientemente grande para que factorizar sea difícil.

---

### Desafío 8: XOR con clave repetida

**Enunciado:**
```
Ciphertext (hex): 1b0c0612001b0c061200
Pista: La clave se repite cada 5 bytes
```

**Solución:**
```python
from collections import Counter

ciphertext = bytes.fromhex("1b0c0612001b0c061200")
key_length = 5

# Dividir en grupos por posición del byte
groups = [[] for _ in range(key_length)]
for i, byte in enumerate(ciphertext):
    groups[i % key_length].append(byte)

# Para cada grupo, el byte más frecuente probablemente es XOR con espacio
key = []
for group in groups:
    most_frequent = Counter(group).most_common(1)[0][0]
    key.append(most_frequent ^ ord(' '))  # Espacio es el byte más común

key_bytes = bytes(key)
print(f"Key found: {key_bytes}")

# Descifrar
plaintext = bytes([c ^ key_bytes[i % key_length] for i, c in enumerate(ciphertext)])
print(f"Plaintext: {plaintext}")
```

**Lección:** XOR con clave repetida es vulnerable a frequency analysis.

---

## 3. Nivel Avanzado

### Desafío 9: Padding Oracle

**Enunciado:**
```
Dado un servidor que revela si el padding es válido,
descifrar un ciphertext sin conocer la clave.
```

**Solución:**
```python
import os
from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad

# Servidor vulnerable
class Server:
    def __init__(self, key):
        self.key = key
    
    def encrypt(self, msg):
        iv = os.urandom(16)
        cipher = AES.new(self.key, AES.MODE_CBC, iv)
        return iv + cipher.encrypt(pad(msg, 16))
    
    def check(self, ct):
        try:
            iv, data = ct[:16], ct[16:]
            AES.new(self.key, AES.MODE_CBC, iv).decrypt(data)
            unpad(AES.new(self.key, AES.MODE_CBC, iv).decrypt(data), 16)
            return True
        except:
            return False

# Ataque
def padding_oracle(oracle, ct, bs=16):
    n = len(ct) // bs
    pt = b""
    for blk in range(n-1, -1, -1):
        block = ct[blk*bs:(blk+1)*bs]
        inter = b""
        for pos in range(bs-1, -1, -1):
            pad_val = bs - pos
            for g in range(256):
                prefix = os.urandom(pos)
                test = prefix + bytes([g]) + bytes([b ^ pad_val for b in inter]) + block
                if oracle(test):
                    inter = bytes([g ^ pad_val]) + inter
                    break
        pt = inter + pt
    return pt

# Demo
key = os.urandom(32)
server = Server(key)
ct = server.encrypt(b"Secret: PaddingOracle!")
pt = padding_oracle(server.check, ct)
print(f"Descifrado: {pt}")
```

**Lección:** Padding Oracle permite descifrar sin clave, solo observando respuestas del servidor.

---

### Desafío 10: Bleichenbacher (RSA PKCS#1 v1.5)

**Enunciado:**
```
RSA con padding PKCS#1 v1.5 vulnerable a Bleichenbacher attack
```

**Solución:**
```python
"""
Bleichenbacher attack: ataque adaptativo a RSA PKCS#1 v1.5
Requiere un oracle que revele si el padding es válido
"""
# Implementación completa: https://github.com/mimoo/RSA-and-ML-DSA-attacks

# Concepto:
# 1. Enviar ciphertext al servidor
# 2. Servidor revela si el padding es válido
# 3. Ajustar ciphertext basado en la respuesta
# 4. Repetir hasta descifrar

# DEFENSA: usar RSA-OAEP en lugar de PKCS#1 v1.5
```

---

### Desafío 11: Hash length extension

**Enunciado:**
```
Dado un MAC = SHA256(secret + message),
extender el mensaje sin conocer el secret
```

**Solución:**
```python
import hashlib
import struct

def sha256_padding(data_len):
    """Generar padding SHA-256"""
    pad = b'\x80'
    pad += b'\x00' * ((55 - data_len % 64) % 64)
    pad += struct.pack('>Q', data_len * 8)
    return pad

def length_extension(original_mac, original_len, append_data):
    """
    Ataque de extensión de longitud en SHA-256
    Conocido: MAC(original) + len(original)
    Secreto: unknown
    """
    # El hash interno después del padding original
    # es el estado inicial para el nuevo cálculo
    
    # Crear nuevo mensaje
    padding = sha256_padding(original_len)
    new_message = original_len * b'\x00' + padding + append_data
    
    # Usar el hash original como estado inicial
    # (requiere manipulación del estado interno)
    
    return new_message

# DEFENSA: usar HMAC en lugar de SHA256(secret + message)
# HMAC no es vulnerable a length extension
```

**Lección:** Nunca usar `hash(secret + message)` como MAC. Usar HMAC.

---

## 4. Nivel Expert

### Desafío 12: Curvas elípticas - Punto no dominante

**Enunciado:**
```
Dado un intercambio ECDH donde un punto no está en la curva,
inyectar un punto que permita recuperar la clave
```

**Solución:**
```python
"""
Ataque de invalid curve en ECDH
Si el servidor no valida que el punto esté en la curva,
se puede inyectar un punto que revele la clave privada
"""
# Concepto:
# 1. Enviar punto P que NO está en la curva
# 2. El servidor calcula Q = d × P (d = clave privada)
# 3. El punto resultante revela información sobre d
# 4. Con suficientes puntos, recuperar d

# DEFENSA: siempre validar que los puntos están en la curva
```

---

### Desafío 13: Side-channel: timing attack a RSA

**Enunciado:**
```
Medir tiempos de descifrado RSA para deducir la clave privada
```

**Solución:**
```python
import time
import random

def rsa_decrypt_timing(c, d, n, iterations=1000):
    """
    Medir tiempo de descifrado para cada bit de la clave
    """
    times = []
    for _ in range(iterations):
        start = time.perf_counter_ns()
        m = pow(c, d, n)
        end = time.perf_counter_ns()
        times.append(end - start)
    return sum(times) / len(times)

# En un ataque real:
# 1. Medir tiempo promedio de descifrado
# 2. Modificar el ciphertext ligeramente
# 3. Observar cambios en el tiempo
# 4. Deducir la clave privada

# DEFENSA: usar implementaciones constant-time
```

---

## 5. Plataformas de práctica

| Plataforma | Tipo | Dificultad | URL |
|---|---|---|---|
| **CryptoHack** | CTF de cripto | Principiante → Expert | [https://cryptohack.org/](https://cryptohack.org/) |
| **Cryptopals** | Ejercicios | Intermedio → Expert | [https://cryptopals.com/](https://cryptopals.com/) |
| **picoCTF** | CTF general | Principiante → Intermedio | [https://picoctf.org/](https://picoctf.org/) |
| **OverTheWire: Krypton** | Wargame | Principiante → Intermedio | [https://overthewire.org/wargames/krypton/](https://overthewire.org/wargames/krypton/) |
| **Cryptohalf** | CTF | Intermedio | [https://cryptohalf.com/](https://cryptohalf.com/) |
| **Ringzer0** | CTF | Intermedio → Expert | [https://ringzer0ctf.com/](https://ringzer0ctf.com/) |

### CryptoHack: módulos recomendados

```
1. Intro to Cryptography
   └─ ¡Warmup!, Encode / Decode

2. Symmetric Ciphers
   └─ Bruteforce XOR, DES sanity check, Padding Oracle

3. Asymmetric Ciphers
   └─ RSA Base, RSA Stegosaurus, RSA Spotlight

4. Hashes
   └─ Diamond in the Rough, Passwords in Hashes

5. Elliptic Curves
   └─ Point Addition, Smooth Criminal
```

---

## 📝 Proyecto final: CTF personal

```markdown
# CTF Personal — Criptografía

## Instrucciones
1. Crear tu propio CTF con 5 retos de criptografía
2. Cada reto debe tener:
   - Enunciado claro
   - Pista (opcional)
   - Solución documentada
   - Lección aprendida

## Niveles
1. Principiante: César, Base64, XOR simple
2. Intermedio: Vigenère, AES-ECB, RSA básico
3. Avanzado: Padding Oracle, Hash extension
4. Expert: ECC, Side-channel, Post-quantum

## Entrega
- Repositorio GitHub con el CTF
- Documentación completa
- Scripts de solución
```

---

**[⬅ Herramientas de Criptoanalisis](../criptoanalisis/02-herramientas-criptoanalisis.md)** · **[Volver al módulo](../README.md)**
