---
title: "Reverse Engineering: desensamblar binarios sin morir en el intento"
description: "Introducción práctica a reverse engineering con Ghidra, radare2 y ejemplos reales"
author: Equipo CDPN
date: 2026-07-27
tags: [reverse-engineering, ghidra, binarios, malware]
readingTime: 6 min
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

# Reverse Engineering: desensamblar binarios sin morir en el intento

<div class="article-meta">
  <span class="accent">📝 Equipo CDPN</span>
  <span>📅 27 Julio 2026</span>
  <span>📖 6 min de lectura</span>
  <span>🏷️ Reverse Engineering</span>
  <span>🏷️ Ghidra</span>
</div>

## ¿Qué es Reverse Engineering?

**Reverse Engineering** (RE) es el proceso de analizar un sistema para entender cómo funciona, partiendo de su resultado final. En ciberseguridad, significa desensamblar o descompilar binarios para entender su comportamiento.

### ¿Para qué sirve?

- **Análisis de malware** — Entender qué hace un virus sin ejecutarlo
- **CTF Challenges** — Resolver retos de tipo Pwn y RE
- **Auditoría de software** — Buscar vulnerabilidades en binarios cerrados
- **Protección de propiedad intelectual** — Detectar plagio o cracking

## Herramientas esenciales

| Herramienta | Tipo | Precio | Nivel |
|-------------|------|--------|-------|
| **Ghidra** | Descompilador + desensamblador | Gratis (NSA) | Intermedio |
| **radare2** | Framework de análisis | Gratis | Avanzado |
| **IDA Free** | Desensamblador | Gratis | Intermedio |
| **x64dbg** | Debugger (Windows) | Gratis | Intermedio |
| **Binary Ninja** | Descompilador | $299 | Avanzado |
| **GDB** | Debugger (Linux) | Gratis | Avanzado |

## Conceptos clave

### Assembly (x86/x64)

```
; x86 básico — las instrucciones que necesitas conocer
mov eax, 5          ; Mover valor 5 al registro EAX
add eax, 3          ; Sumar 3 a EAX (eax = 8)
sub eax, 1          ; Restar 1 de EAX (eax = 7)
cmp eax, 10         ; Comparar EAX con 10
je  0x401000        ; Saltar si EAX == 10
jmp 0x401000        ; Saltar siempre
push ebp            ; Guardar registro en pila
pop ebp             ; Recuperar registro de pila
call 0x401000       ; Llamar a función
ret                 ; Retornar de función
```

### Convenciones de llamada

```
┌─────────────────────────────────────────────┐
│  System V AMD64 (Linux/macOS)               │
│  Argumentos: RDI, RSI, RDX, RCX, R8, R9    │
│  Retorno: RAX                               │
│  Caller-saved: RAX, RCX, RDX, RSI, RDI...  │
├─────────────────────────────────────────────┤
│  Microsoft x64 (Windows)                    │
│  Argumentos: RCX, RDX, R8, R9              │
│  Retorno: RAX                               │
│  Shadow space: 32 bytes en pila             │
└─────────────────────────────────────────────┘
```

## Primer paso: Ghidra

### Instalación

```bash
# Descargar Ghidra (requiere Java 17+)
# https://ghidra-sre.org/

# Linux/Mac
wget https://github.com/NationalSecurityAgency/ghidra/releases/latest
unzip ghidra_*.zip
./ghidra_*/ghidraRun
```

### Análisis básico

```
1. File → Import File → Seleccionar el binario
2. Ghidra analiza automáticamente (puedes aceptar defaults)
3. Ve a "Symbol Tree" → Functions para ver todas las funciones
4. Double-click en una función para ver el desensamblaje
5. Usa Decompiler (panel izquierdo) para ver pseudocódigo en C
```

### Tips para principiantes

1. **Empieza por funciones conocidas** — Busca `main`, `printf`, `system`
2. **Busca strings** — `Strings` panel revela mucho del comportamiento
3. **Sigue el flujo** — Las llamadas a sistema (syscalls) son clave
4. **Nombra las variables** — Renombra `iVar1` por algo descriptivo

## Ejercicio práctico

### Analizar un crackme simple

```c
// Compilar con: gcc -o crackme crackme.c
#include <stdio.h>
#include <string.h>

int main() {
    char password[32];
    printf("Enter password: ");
    scanf("%s", password);
    
    if (strcmp(password, "s3cur1ty") == 0) {
        printf("Access granted!\n");
    } else {
        printf("Access denied!\n");
    }
    return 0;
}
```

### Qué buscar en Ghidra:

1. **Strings** — Busca "Access granted" y "Access denied"
2. **strcmp** — La función de comparación revela la password
3. **Flujo** — El `je` (jump if equal) después de `strcmp` te dice dónde va cada caso

## Recursos para aprender

| Recurso | Tipo | Link |
|---------|------|------|
| **Reverse Engineering for Beginners** | Libro gratis | begin.re |
| **crackmes.one** | Prácticas | crackmes.one |
| **Malware Unicorn** | Workshop | malwareunicorn.org |
| **0xRick RE series** | Blog | 0xrick.github.io |
| **Ghidra Book** | Libro | No Starch Press |

## Conclusión

Reverse Engineering es como resolver un rompecabezas: al principio parece imposible, pero con práctica y las herramientas correctas, descubres que **todo binario tiene una historia que contar**.

---

*Artículo publicado en el Blog CDPN — Semana 9*
