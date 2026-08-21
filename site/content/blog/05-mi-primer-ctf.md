---
title: "Mi primer CTF: lo que aprendí"
description: "Experiencia personal, tips para empezar y recursos recomendados"
author: Equipo CDPN
date: 2026-06-29
tags: [ctf, practica, competiciones, experiencia]
readingTime: 4 min
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

# Mi primer CTF: lo que aprendí

<div class="article-meta">
  <span class="accent">📝 Equipo CDPN</span>
  <span>📅 29 Junio 2026</span>
  <span>📖 4 min de lectura</span>
  <span>🏷️ CTF</span>
  <span>🏷️ Práctica</span>
</div>

## ¿Qué es un CTF?

**CTF** (Capture The Flag) es una competencia donde debes encontrar "flags" (texto oculto) resolviendo retos de ciberseguridad. Es la mejor forma de aprender practicando.

## Mi experiencia

Cuando empecé en mi primer CTF, no sabía ni qué era Nmap. Hoy puedo decirte que **los CTFs cambiaron mi carrera**.

### Lo que encontré:
- **Crypto** — Descifrar mensajes con César, Vigenère, RSA
- **Web** — SQL injection, XSS, IDOR
- **Forensics** — Analizar imágenes de disco, pcaps
- **Reverse Engineering** — Desensamblar binarios
- **Pwn** — Explotar binaries con buffer overflow

### Lo que aprendí:
1. **Google es tu mejor herramienta** — Todos buscan soluciones
2. **Leer es clave** — Los writesups son oro
3. **Practicar todos los días** — Aunque sea 30 minutos
4. **No rendirse** — El primer reto que resuelves es addictivo

## Tips para empezar

```
1. Elige una plataforma: TryHackMe (principiante) o HTB (intermedio)
2. Empieza por la ruta "Beginner"
3. Lee el writeup SIEMPRE después de resolver
4. Únete a un equipo (.twimg, Reddit)
5. Documenta todo en tu portafolio
```

## Recursos gratuitos

| Plataforma | Nivel | Precio |
|------------|-------|--------|
| TryHackMe | Principiante | Gratis / $10/mes |
| HackTheBox | Intermedio | Gratis / $14/mes |
| PicoCTF | Principiante | Gratis |
| OverTheWire | Intermedio | Gratis |
| CTFtime | Todos | Gratis |

## Conclusión

Los CTFs no son solo competencias. Son **entrenamiento real** que te prepara para el mundo laboral. Cada reto que resuelves te hace mejor.

---

*Artículo publicado en el Blog CDPN — Semana 5*
