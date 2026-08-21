---
title: "Hashing y cracking de contraseñas: lo que todo hacker debe saber"
description: "Cómo funciona el hashing, tipos de algoritmos y herramientas como John the Ripper y Hashcat"
author: Equipo CDPN
date: 2026-08-24
tags: [hashing, cracking, john, hashcat, passwords]
readingTime: 5 min
---

<script setup>
import { useData } from 'vitepress'
const { frontmatter } = useData()
</script>

<style>
.article-meta { display:flex; gap:0.8rem; flex-wrap:wrap; margin:0.8rem 0 1.5rem; font-size:0.85rem; color:var(--vp-c-text-3); }
.article-meta span { background:var(--vp-c-default-soft); padding:2px 10px; border-radius:6px; }
.article-meta .accent { background:var(--vp-c-brand-soft); color:var(--vp-c-brand-1); }
</style>

# Hashing y cracking de contraseñas: lo que todo hacker debe saber

<div class="article-meta">
  <span class="accent">📝 Equipo CDPN</span>
  <span>📅 24 Agosto 2026</span>
  <span>📖 5 min de lectura</span>
  <span>🏷️ Hashing</span>
  <span>🏷️ Cracking</span>
</div>

## ¿Qué es el hashing?

Un **hash** es una función unidireccional que convierte cualquier dato en una cadena de longitud fija. No se puede "deshacer" — solo puedes verificar si un hash coincide con el input original.

```
Input: "password123"
SHA-256: ef92b778bafe771e89245b89ecbc08a44a4e166c06659911881f383d4473e94f
```

### Propiedades del hashing

| Propiedad | Significado |
|-----------|-------------|
| **Determinista** | Mismo input → mismo hash siempre |
| **Unidireccional** | No puedes obtener el input desde el hash |
| **Avalanche** | Un bit de cambio → hash completamente diferente |
| **Sin colisiones** | Diferentes inputs → diferentes hashes (idealmente) |

## Algoritmos de hashing

| Algoritmo | Velocidad | Seguridad | Uso actual |
|-----------|-----------|-----------|------------|
| **MD5** | ⚡ Muy rápido | ❌ Inseguro | Solo checksums |
| **SHA-1** | ⚡ Rápido | ❌ Roto | Deprecado |
| **SHA-256** | 🐢 Medio | ✅ Seguro | General |
| **bcrypt** | 🐌 Lento | ✅ Muy seguro | Passwords |
| **Argon2** | 🐌 Lento | ✅ El más seguro | Passwords (recomendado) |
| **NTLM** | ⚡ Rápido | ⚠️ Medio | Windows hashes |

### Comparación visual

```bash
# MD5 — se puede cracker en segundos
echo -n "password123" | md5sum
# 482c811da5d5b4bc6d497ffa98491e38

# SHA-256 — más lento de crackear
echo -n "password123" | sha256sum
# ef92b778bafe771e89245b89ecbc08a4...

# bcrypt — cada hash toma ~100ms en generar
# Un billón de passwords tomaría ~3000 años
```

## Formatos de hash comunes

```
# MD5
5f4dcc3b5aa765d61d8327deb882cf99

# SHA-1
5baa61e4c9b93f3f0682250b6cf8331b7ee68fd8

# bcrypt
$2b$12$LJ3m4ys1Lz3YqXXY5Z5QzO3dP1X2V8X9X7X5X3X1X9X7X5X3X1X9X

# NTLM (Windows)
aad3b435b51404eeaad3b435b51404ee:31d6cfe0d16ae931b73c59d7e0c089c0

# Linux /etc/shadow
$6$rounds=5000$salt$hash
```

## Herramientas de cracking

### John the Ripper (JtR)

```bash
# Instalar
sudo apt install john

# Crackear un hash MD5
echo "5f4dcc3b5aa765d61d8327deb882cf99" > hash.txt
john --format=raw-md5 hash.txt

# Crackear con wordlist
john --wordlist=/usr/share/wordlists/rockyou.txt hash.txt

# Ver resultados
john --show hash.txt
```

### Hashcat

```bash
# Instalar (requiere GPU para máxima velocidad)
sudo apt install hashcat

# Crackear MD5
hashcat -m 0 hash.txt /usr/share/wordlists/rockyou.txt

# Crackear SHA-256
hashcat -m 1400 hash.txt rockyou.txt

# Crackear bcrypt
hashcat -m 3200 hash.txt rockyou.txt

# Modo brute force (lento pero efectivo)
hashcat -m 0 -a 3 hash.txt ?a?a?a?a?a?a
# ?a = todos los caracteres
# 6 caracteres = 308 millones de combinaciones
```

### Ataques disponibles

| Ataque | Comando JtR | Velocidad |
|--------|-------------|-----------|
| **Dictionary** | `--wordlist=rockyou.txt` | 🚀 Rápido |
| **Rule-based** | `--wordlist=rockyou.txt --rules` | 🚀 Rápido |
| **Brute force** | `--incremental` | 🐢 Lento |
| **Mask** | `--mask=?a?a?a?a?a` | 🐢 Medio |
| **Rainbow tables** | Pre-computed | ⚡ Instantáneo |

## Proteger contraseñas

```python
# MAL ❌ — MD5 es inseguro
import hashlib
hash = hashlib.md5(b"password123").hexdigest()

# BIEN ✅ — bcrypt con salt
import bcrypt
salt = bcrypt.gensalt(rounds=12)
hashed = bcrypt.hashpw(b"password123", salt)

# MUY BIEN ✅ — Argon2 (el más seguro)
from argon2 import PasswordHasher
ph = PasswordHasher(time_cost=3, memory_cost=65536, parallelism=4)
hashed = ph.hash("password123")
```

## Tips de seguridad

1. **Nunca almacenes passwords en texto plano** — Usa bcrypt/Argon2
2. **Usa salt único por password** — Impide rainbow tables
3. **Configura cost factor alto** — bcrypt rounds ≥ 12
4. **Implementa rate limiting** — Bloquear después de 5 intentos
5. **Requiere MFA** — El hash más fuerte se puede crackear con tiempo

## Conclusión

Entender el hashing es fundamental para ciberseguridad. Si proteges contraseñas con MD5, un atacante puede crackerlas en segundos. Si usas Argon2 con salt, necesitaría milenios.

---

*Artículo publicado en el Blog CDPN — Semana 13*
