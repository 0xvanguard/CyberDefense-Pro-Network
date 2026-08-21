# 🧮 Matemáticas para Criptografía

> *"La criptografía se construye sobre problemas matemáticos que son fáciles de hacer pero difíciles de deshacer. Entender la matemática es entender por qué la criptografía funciona."*

---

## 📋 Tabla de contenido

1. [Aritmódica modular](#1-aritmódica-modular)
2. [Exponenciación modular](#2-exponenciación-modular)
3. [Problema del logaritmo discreto](#3-problema-del-logaritmo-discreto)
4. [Curvas elípticas](#4-curvas-elípticas)
5. [Números primos y factorización](#5-números-primos-y-factorización)
6. [Aplicación en criptografía](#6-aplicación-en-criptografía)
7. [Referencias](#7-referencias)

---

## 1. Aritmódica modular

### ¿Qué es?

La **aritmódica modular** es el sistema de aritmética donde los números "se envuelven" después de alcanzar un valor módulo. Es la base de RSA, Diffie-Hellman y ECC.

### Definición

```
a ≡ b (mod n) significa que a y b tienen el mismo residuo cuando se dividen por n.

Ejemplos:
17 ≡ 5 (mod 12)    → 17 = 1×12 + 5
25 ≡ 1 (mod 12)    → 25 = 2×12 + 1
-3 ≡ 9 (mod 12)    → -3 = -1×12 + 9
```

### Operaciones modulares

```python
# Suma modular
(7 + 5) % 12 = 0

# Resta modular
(7 - 5) % 12 = 2

# Multiplicación modular
(7 * 5) % 12 = 35 % 12 = 11

# En Python
print((7 + 5) % 12)    # 0
print((7 - 5) % 12)    # 2
print((7 * 5) % 12)    # 11
```

### Inverso modular

```python
# El inverso modular de a (mod n) es un número b tal que:
# a × b ≡ 1 (mod n)

# Ejemplo: inverso de 3 (mod 11)
# 3 × 4 = 12 ≡ 1 (mod 11)
# Por lo tanto, 3⁻¹ ≡ 4 (mod 11)

# En Python
def modinv(a, m):
    """Inverso modular extendido"""
    if gcd(a, m) != 1:
        return None  # No existe inverso
    g, x, _ = extended_gcd(a, m)
    return x % m

from math import gcd

def extended_gcd(a, b):
    if a == 0:
        return b, 0, 1
    g, x, y = extended_gcd(b % a, a)
    return g, y - (b // a) * x, x

# Ejemplo
print(modinv(3, 11))  # 4
print(modinv(7, 11))  # 8 (porque 7 × 8 = 56 ≡ 1 mod 11)
```

---

## 2. Exponenciación modular

### ¿Por qué importa?

La **exponenciación modular** es la operación clave de RSA y Diffie-Hellman:

```
c = m^e (mod n)
```

Es fácil calcular `c` dado `m`, `e` y `n`, pero difícil calcular `m` dado `c`, `e` y `n`.

### Ejemplo

```python
# Exponenciación modular
# 2^10 mod 13 = ?

# Cálculo directo (ineficiente para números grandes)
print(pow(2, 10, 13))  # 1024 mod 13 = 10

# En Python, pow(a, b, m) es eficiente
print(pow(2, 10, 13))  # 10

# Ejemplo más grande
print(pow(7, 256, 13))  # 9
```

### Exponenciación modular eficiente (square-and-multiply)

```python
def mod_pow(base, exp, mod):
    """Exponenciación modular eficiente O(log exp)"""
    result = 1
    base = base % mod
    while exp > 0:
        if exp % 2 == 1:  # Si el bit es 1
            result = (result * base) % mod
        exp = exp >> 1  # Siguiente bit
        base = (base * base) % mod
    return result

# Ejemplo
print(mod_pow(2, 10, 13))  # 10
print(mod_pow(7, 256, 13))  # 9
```

---

## 3. Problema del logaritmo discreto

### Definición

Dado `g`, `h` y `p`, encontrar `x` tal que:

```
g^x ≡ h (mod p)
```

Este problema es **fácil de hacer** (exponenciación modular) pero **difícil de deshacer** (logaritmo discreto).

### Ejemplo

```python
# Fácil: calcular h dado x
g, x, p = 2, 6, 23
h = pow(g, x, p)
print(f"2^6 mod 23 = {h}")  # 64 mod 23 = 18

# Difícil: calcular x dado h
# ¿Cuál es x tal que 2^x ≡ 18 (mod 23)?
# Respuesta: x = 6 (pero encontrarlo sin saberlo es difícil)
```

### Seguridad

| Tamaño de p | Seguridad (bits) | Estado |
|---|---|---|
| 256 bits | ~128 bits | ✅ Seguro |
| 2048 bits | ~112 bits | ✅ Seguro |
| 4096 bits | ~140 bits | ✅ Seguro |

---

## 4. Curvas elípticas

### ¿Qué es una curva elíptica?

Una curva elíptica es el conjunto de puntos `(x, y)` que satisfacen:

```
y² = x³ + ax + b (mod p)
```

donde `4a³ + 27b² ≠ 0` (para evitar singularidades).

### Ejemplo: curva sobre campo finito

```python
# Curva: y² = x³ + 2x + 3 (mod 17)
# Verificar si (5, 1) está en la curva
x, y, a, b, p = 5, 1, 2, 3, 17

# Lado izquierdo
lhs = pow(y, 2, p)  # 1² mod 17 = 1

# Lado derecho
rhs = (pow(x, 3, p) + a * x + b) % p  # (125 + 10 + 3) mod 17 = 138 mod 17 = 1

print(f"lhs = {lhs}, rhs = {rhs}")
print(f"¿Está en la curva? {lhs == rhs}")  # True
```

### Operaciones en curvas elípticas

```python
# Punto infinito (identidad aditiva)
O = None

def ec_add(P, Q, a, p):
    """Suma de dos puntos en curva elíptica"""
    if P is None:
        return Q
    if Q is None:
        return P
    
    x1, y1 = P
    x2, y2 = Q
    
    if x1 == x2 and y1 == y2:
        # Doble de punto
        lam = (3 * x1 * x1 + a) * modinv(2 * y1, p) % p
    elif x1 == x2:
        return None  # P + (-P) = O
    else:
        lam = (y2 - y1) * modinv(x2 - x1, p) % p
    
    x3 = (lam * lam - x1 - x2) % p
    y3 = (lam * (x1 - x3) - y1) % p
    return (x3, y3)

def ec_mul(k, P, a, p):
    """Multiplicación escalar: k × P"""
    result = None
    addend = P
    while k > 0:
        if k & 1:
            result = ec_add(result, addend, a, p)
        addend = ec_add(addend, addend, a, p)
        k >>= 1
    return result
```

### Seguridad de ECC vs RSA

| Curva elíptica | Equivalencia RSA | Tamaño de clave |
|---|---|---|
| P-256 | RSA-3072 | 256 bits |
| P-384 | RSA-7680 | 384 bits |
| P-521 | RSA-15360 | 521 bits |

> **Ventaja de ECC:** misma seguridad con claves mucho más pequeñas → mejor rendimiento.

---

## 5. Números primos y factorización

### ¿Por qué importa?

RSA se basa en que **factorizar un número grande en sus primos es difícil**:

```
n = p × q (fácil)
Dado n, encontrar p y q (difícil para números grandes)
```

### Generar primos grandes

```python
from Crypto.Util.number import getPrime, inverse

# Generar primos de 2048 bits
p = getPrime(2048)
q = getPrime(2048)

# Verificar que son primos (probabilístico)
# Miller-Rabin con k=40 iteraciones

# Calcular n
n = p * q

# Calcular φ(n)
phi_n = (p - 1) * (q - 1)

# Exponente público
e = 65537

# Exponente privado
d = inverse(e, phi_n)

# Verificar: e × d ≡ 1 (mod φ(n))
print(f"e × d mod φ(n) = {(e * d) % phi_n}")  # Debe ser 1
```

### Ataques a la factorización

| Método | Complejidad | Estado |
|---|---|---|
| **Trial division** | O(√n) | ❌ Inútil para RSA |
| **Pollard rho** | O(n^(1/4)) | ❌ Inútil para RSA |
| **Sieving** | L(1/3, (64/9)^(1/3)) | ⚠️ Amenaza para RSA-1024 |
| **Cribado cuántico** | Polynomial | 🔴 Amenaza futura (Shor) |

---

## 6. Aplicación en criptografía

### RSA: resumen del algoritmo

```
1. GENERACIÓN DE CLAVES
   p, q = primos grandes aleatorios
   n = p × q
   φ(n) = (p-1) × (q-1)
   e = 65537 (exponente público)
   d = e⁻¹ mod φ(n) (exponente privado)
   
   Clave pública: (e, n)
   Clave privada: (d, n)

2. CIFRADO
   c = m^e mod n

3. DESCIFRADO
   m = c^d mod n
```

### Diffie-Hellman: resumen del protocolo

```
1. ACUERDO PÚBLICO
   p = primo grande
   g = generador

2. ALICIA
   a = secreto privado de Alice
   A = g^a mod p (envía a Bob)

3. BOB
   b = secreto privado de Bob
   B = g^b mod p (envía a Alice)

4. CLAVE COMPARTIDA
   Alice calcula: s = B^a mod p = g^(ab) mod p
   Bob calcula: s = A^b mod p = g^(ab) mod p
   ¡Ambos tienen la misma clave s!
```

### ECC: resumen

```
1. GENERACIÓN DE CLAVES
   E = curva elíptica
   G = punto generador
   d = número privado (aleatorio)
   Q = d × G (punto público)

2. CIFRADO (ECIES)
   k = número aleatorio
   R = k × G
   S = k × Q
   c = m ⊕ KDF(S)
   Mensaje: (R, c)

3. DESCIFRADO
   S = d × R = d × k × G = k × d × G = k × Q
   m = c ⊕ KDF(S)
```

---

## 7. Referencias

| Recurso | URL |
|---|---|
| **Introduction to Modern Cryptography** | [https://crypto.stanford.edu/~dabo/intropml/](https://crypto.stanford.edu/~dabo/intropml/) |
| **Handbook of Applied Cryptography** | [https://cacr.uwaterloo.ca/hac/](https://cacr.uwaterloo.ca/hac/) |
| **CryptoHack** | [https://cryptohack.org/](https://cryptohack.org/) |
| **NIST SP 800-57** | [https://csrc.nist.gov/publications/detail/sp/800-57-part-1/rev-5/final](https://csrc.nist.gov/publications/detail/sp/800-57-part-1/rev-5/final) |

---

## 📝 Entregable de portafolio

```markdown
# Matemáticas para Criptografía — Ejercicios Resueltos

## Ejercicio 1: Aritmódica Modular
- Calcular 2^100 mod 13
- Solución: pow(2, 100, 13) = 9

## Ejercicio 2: Inverso Modular
- Calcular inverso de 7 mod 11
- Solución: 7 × 8 = 56 ≡ 1 mod 11 → inverso = 8

## Ejercicio 3: RSA manual
- Generar claves RSA con p=61, q=53
- n = 3233, φ(n) = 3120
- e = 17, d = 2753
- Cifrar m=65: c = 65^17 mod 3233 = 2790
- Descifrar: m = 2790^2753 mod 3233 = 65 ✅
```

---

**[⬅ Volver al módulo](../README.md)** · **[→ Cifrado Simétrico](./02-criptografia-simetrica.md)**
