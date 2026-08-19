<div align="center">

# 📚 05 — RECURSOS

**Cheatsheets · Certificaciones · Libros · Cursos**

*Referencia rápida y biblioteca curada.*

</div>

---

## 🎯 Propósito

Esta sección es el **índice de referencia** del repositorio. Aquí vive todo el material consultivo: cheatsheets para no buscar dos veces lo mismo, seguimiento de certificaciones, notas de lectura y cursos validados.

---

## 📂 Estructura

| Carpeta | Contenido |
|---|---|
| [`cheatsheets/`](./cheatsheets/) | Hojas de referencia rápida (un `.md` por herramienta/tema) |
| [`certificaciones/`](./certificaciones/) | Tracker personal de certificaciones · notas de estudio |
| [`libros/`](./libros/) | Resúmenes y notas de libros leídos |
| [`cursos-recomendados/`](./cursos-recomendados/) | Rutas formativas validadas (gratuitas y de pago) |

---

## 🃏 Cheatsheets — convención de naming

```
cheatsheets/
├── nmap.md
├── burp-suite.md
├── sqlmap.md
├── linux-privesc.md
├── windows-privesc.md
├── active-directory.md
├── docker-security.md
├── wazuh-rules.md
├── osint-basics.md
└── ...
```

> Cada cheatsheet incluye: comandos esenciales · flags más usadas · ejemplos reales · referencias oficiales.

---

## 🎓 Certificaciones — tracker

| Certificación | Vendor | Estado | Fecha objetivo | Notas |
|---|---|---|---|---|
| Hacking Social | _propia_ | 🟡 En curso | — | Fase 1 |
| eJPT | INE Security | 🔲 Planificada | T+3 meses | Fase 2 |
| CompTIA Security+ | CompTIA | 🔲 Planificada | T+6 meses | Fase 3 |
| OSCP | OffSec | 🎯 Objetivo final | T+12 meses | Fase 4 |

**Para cada certificación, dentro de `certificaciones/<nombre>/`:**
- `README.md` — temario oficial mapeado
- `notas/` — apuntes por dominio
- `simulacros/` — preguntas tipo
- `recursos.md` — links curados

---

## 📖 Libros — formato de notas

```markdown
# [Título]
**Autor:** ...
**Editorial · Año:** ...
**ISBN:** ...
**Estado:** Leído / En progreso / Por leer
**Calificación:** ★★★★☆

## TL;DR
3 líneas.

## Mapa mental
- Capítulo 1: ...
- Capítulo 2: ...

## Conceptos clave
- ...

## Aplicación práctica
¿Cómo aplico esto en mi día a día?

## Citas memorables
> "..."

## Recursos relacionados
```

**Lecturas recomendadas para empezar:**
- *The Web Application Hacker's Handbook* — Stuttard & Pinto
- *Penetration Testing: A Hands-On Introduction to Hacking* — Georgia Weidman
- *Blue Team Field Manual* — Alan White
- *Red Team Field Manual* — Ben Clark
- *Practical Malware Analysis* — Sikorski & Honig
- *Designing Secure Software* — Loren Kohnfelder

---

## 🎬 Cursos recomendados — formato

```markdown
# [Nombre del curso]
**Plataforma:** TryHackMe / HTB Academy / Udemy / Pluralsight / ...
**Instructor:** ...
**Duración:** Xh
**Costo:** Gratis / X USD
**Estado:** Completado / En progreso / Pendiente

## Por qué este curso
- ...

## Pre-requisitos
- ...

## Lo que aprenderás
- ...

## Notas personales
- ...
```

**Plataformas con tracker:**
- 🎓 [TryHackMe](https://tryhackme.com) — paths gamificados
- 🎓 [HackTheBox Academy](https://academy.hackthebox.com) — orientado a CPTS/CBBH
- 🎓 [PortSwigger Web Security Academy](https://portswigger.net/web-security) — gratis y excelente
- 🎓 [INE](https://ine.com) — eJPT/eCPPT
- 🎓 [OffSec](https://www.offensive-security.com) — OSCP

---

<div align="center">

**[⬅ Volver al README principal](../README.md)** · **[🗺️ Ver Roadmap](../ROADMAP.md)**

</div>
