---
title: � Módulo 08 — Criptografía
description: � Módulo 08 — Criptografía
---

# 🔐 Módulo 08 — Criptografía

> **Nivel:** Intermedio → Avanzado · **Objetivo:** dominar los principios criptográficos que protegen (y a veces fallan en proteger) la información digital: cifrado, hashing, firmas digitales y criptoanalisis.

[![Nivel](https://img.shields.io/badge/Nivel-Intermedio→Avanzado-orange?style=flat-square)]()
[![Enfoque](https://img.shields.io/badge/Enfoque-Blue%20Team%20|%20Red%20Team-purple?style=flat-square)]()
[![Prerequisito](https://img.shields.io/badge/Prerequisito-Matemáticas%20básicas-blue?style=flat-square)]()

---

## 📋 Resumen

| Atributo | Detalle |
|---|---|
| 🎯 **Resultado** | Comprender, aplicar y atacar sistemas criptográficos de forma profesional |
| 🧪 **Práctica** | OpenSSL, hashcat, John the Ripper, CyberChef, Python cryptography |
| 🗂️ **Portafolio** | Resolución de retos CTF de criptografía + análisis de implementaciones reales |
| 🔗 **Requiere** | Conocimientos básicos de matemáticas (aritmódica modular, exponenciación) |

---

## 🎯 Objetivos de aprendizaje

Al completar este módulo deberías ser capaz de:

- **Cifrado simétrico:** entender AES, DES, ChaCha20 y sus modos de operación (ECB, CBC, CTR, GCM).
- **Cifrado asimétrico:** dominar RSA, ECC, Diffie-Hellman y el problema del intercambio de claves.
- **Hashing:** comprender SHA-256, bcrypt, scrypt y por qué MD5/SHA-1 están destruidos.
- **Firmas digitales:** crear y verificar firmas con RSA y ECDSA.
- **Criptoanalisis:** atacar cifrados débiles (ECB, padding oracle, XOR, frequency analysis).
- **Aplicación práctica:** implementar cifrado correcto en aplicaciones reales (TLS, encrypt-at-rest).

---

## 🗂️ Estructura del módulo

| Carpeta | Contenido | Estado |
|---|---|---|
| [`fundamentos/`](./fundamentos/) | Matemáticas, cifrado simétrico y asimétrico | ✅ Completado |
| [`hash-y-digitales/`](./hash-y-digitales/) | Hashing y firmas digitales | ✅ Completado |
| [`criptoanalisis/`](./criptoanalisis/) | Técnicas de ataque y herramientas | ✅ Completado |
| [`practica/`](./practica/) | Desafíos CTF y ejercicios prácticos | ✅ Completado |
| [`herramientas/`](./herramientas/) | Comparativa de herramientas criptográficas | ✅ Completado |

### 📚 Contenido detallado

#### 1. Fundamentos

| Archivo | Contenido |
|---|---|
| [`01-matematicas-crypto.md`](./fundamentos/01-matematicas-crypto.md) | Aritmódica modular, exponenciación modular, problema del logaritmo discreto, curvas elípticas |
| [`02-criptografia-simetrica.md`](./fundamentos/02-criptografia-simetrica.md) | DES, 3DES, AES, ChaCha20, modos de operación (ECB, CBC, CTR, GCM), padding |
| [`03-criptografia-asimetrica.md`](./fundamentos/03-criptografia-asimetrica.md) | RSA, Diffie-Hellman, ECC, curvas elípticas, intercambio de claves |

#### 2. Hash y Firmas Digitales

| Archivo | Contenido |
|---|---|
| [`01-hash-y-firmas.md`](./hash-y-digitales/01-hash-y-firmas.md) | MD5, SHA-1, SHA-256, SHA-3, bcrypt, scrypt, Argon2, firmas RSA/ECDSA |

#### 3. Criptoanalisis

| Archivo | Contenido |
|---|---|
| [`01-tecnicas-ataque.md`](./criptoanalisis/01-tecnicas-ataque.md) | Fuerza bruta, diccionario, frequency analysis, padding oracle, ECB, XOR |
| [`02-herramientas-criptoanalisis.md`](./criptoanalisis/02-herramientas-criptoanalisis.md) | hashcat, John the Ripper, CyberChef, attack mode reference |

#### 4. Práctica

| Archivo | Contenido |
|---|---|
| [`01-desafios-criptografia.md`](./practica/01-desafios-criptografia.md) | Retos CTF organizados por dificultad, con soluciones paso a paso |

#### 5. Herramientas

| Archivo | Contenido |
|---|---|
| [`01-herramientas-crypto.md`](./herramientas/01-herramientas-crypto.md) | OpenSSL, hashcat, John, CyberChef, Python cryptography, comparativa |

---

## 🛠️ Herramientas principales

| Herramienta | Categoría | Uso principal |
|---|---|---|
| **OpenSSL** | Cifrado/Hash | Suite completa de criptografía CLI |
| **hashcat** | Criptoanalisis | Cracking de hashes con GPU |
| **John the Ripper** | Criptoanalisis | Cracking de hashes con CPU/GPU |
| **CyberChef** | Análisis | Transformaciones criptográficas online |
| **Python cryptography** | Implementación | Librería de criptografía en Python |
| **GPG** | Firmas/Encriptación | Encriptación de archivos y firmas |
| **age** | Encriptación | Encriptación moderna de archivos |
| **Signal Protocol** | Protocolo | Encriptación de mensajería |
| **TLS 1.3** | Protocolo | Encriptación de tráfico web |

---

## ⚖️ Aviso ético

La criptografía **se estudia y practica** con:

- ✅ Datos propios o de práctica (CTFs, laboratorios)
- ✅ Entornos aislados (VMs, containers)
- ✅ Plataformas autorizadas (Cryptopals, CryptoHack)
- ❌ Nada de atacar sistemas reales sin autorización
- ❌ Nada de robar claves o credenciales
- ❌ Nada de implementar criptografía casera para producción

> **Regla de oro:** nunca inventes tu propio algoritmo criptográfico. Usa estándares probados (AES-256-GCM, ChaCha20-Poly1305).

---

## 🔗 Encaje del módulo en la ruta

Dentro de la **Ruta 3 (Blue Team)**, este módulo es la **Fase D**:

1. `01-reconocimiento-osint/` ← Reconocimiento
2. `02-pentesting-red-team/` ← Pentesting
3. `03-analisis-vulnerabilidades/` ← Análisis
4. `04-explotacion-web/` ← Explotación
5. `05-post-explotacion/` ← Post-explotación
6. `06-forense-digital/` ← Forense digital
7. `07-ingenieria-social/` ← Ingeniería social
8. **`08-criptografia/`** ← **Este módulo** (Fase D)

---

## ✅ Checkpoint

¿Puedes hacer lo siguiente sin guía?

- [ ] Explicar la diferencia entre cifrado simétrico y asimétrico
- [ ] Cifrar y descifrar un archivo con OpenSSL (AES-256-GCM)
- [ ] Generar un par de claves RSA y firmar/verificar un documento
- [ ] Identificar el algoritmo de un hash por su longitud
- [ ] Cracker un hash MD5 con hashcat usando una wordlist
- [ ] Detectar y explotar un cifrado ECB (pattern leakage)
- [ ] Implementar un padding oracle attack básico
- [ ] Explicar por qué TLS 1.3 es más seguro que TLS 1.2

Si todo es ✅, estás listo para aplicar criptografía en proyectos reales.

---

## 📚 Recursos complementarios

| Recurso | URL |
|---|---|
| **CryptoHack** | [https://cryptohack.org/](https://cryptohack.org/) |
| **Cryptopals** | [https://cryptopals.com/](https://cryptopals.com/) |
| **OWASP Crypto Cheat Sheet** | [https://cheatsheetseries.owasp.org/cheatsheets/Cryptographic_Cheat_Sheet.html](https://cheatsheetseries.owasp.org/cheatsheets/Cryptographic_Cheat_Sheet.html) |
| **NIST SP 800-57** | [https://csrc.nist.gov/publications/detail/sp/800-57-part-1/rev-5/final](https://csrc.nist.gov/publications/detail/sp/800-57-part-1/rev-5/final) |

---

**[⬅ Volver a Ciberseguridad](../README.md)** · **[🗺️ Ver Rutas](../../RUTAS.md)**
