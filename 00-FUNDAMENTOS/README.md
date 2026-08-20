# 🚀 FUNDAMENTOS — Base para principiantes

> **Si estás empezando desde cero, empieza aquí.** Esta carpeta es tu puerta de entrada al repositorio. Está pensada para que cualquier persona, sin experiencia previa, pueda construir una base sólida antes de saltar a los módulos especializados.

## ¿Qué vas a encontrar aquí?

Una **base pequeña pero completa**: los conceptos que necesitas entender antes de leer pentesting, blue team, IA ofensiva o criptografía aplicada. Cada archivo es autónomo y enlaza con el resto del repo cuando llega el momento.

## 🗺️ Índice de la base

| # | Archivo | Qué cubre | Tiempo estimado |
|---|---|---|---|
| 01 | [`01-que-es-ciberseguridad.md`](./01-que-es-ciberseguridad.md) | El campo, los roles, las especializaciones | 15 min |
| 02 | [`02-glosario.md`](./02-glosario.md) | ~80 términos que vas a ver 1000 veces | Referencia |
| 03 | [`03-internet-y-redes.md`](./03-internet-y-redes.md) | Cómo funciona internet, TCP/IP, DNS, HTTP | 30 min |
| 04 | [`04-sistema-operativo-y-terminal.md`](./04-sistema-operativo-y-terminal.md) | Linux y Windows a nivel defensivo, terminal básica | 45 min |
| 05 | [`05-criptografia-basica.md`](./05-criptografia-basica.md) | Hash, cifrado simétrico/asimétrico, firmas | 30 min |
| 06 | [`06-vulnerabilidades.md`](./06-vulnerabilidades.md) | Qué es una vulnerabilidad, OWASP Top 10, CVEs | 25 min |
| 07 | [`07-etica-y-leyes.md`](./07-etica-y-leyes.md) | Hacking ético, qué puedes y qué NO debes hacer | 15 min |
| 08 | [`08-herramientas-esenciales.md`](./08-herramientas-esenciales.md) | nmap, Wireshark, Burp, Metasploit y compañía | 40 min |
| 09 | [`09-como-seguir-este-repo.md`](./09-como-seguir-este-repo.md) | Rutas de aprendizaje según tu interés | 10 min |

## 🧭 Rutas recomendadas (elige la tuya)

| Si te interesa… | Empieza por | Cae en |
|---|---|---|
| 🛡️ Defender sistemas (Blue Team) | [`rutas/ruta-defensor.md`](./rutas/ruta-defensor.md) | `03-blue-team-defensa/`, `02-SEGURIDAD-INFORMACION/02-blue-team-defensa/` |
| ⚔️ Atacar y entender al atacante (Red Team) | [`rutas/ruta-atacante.md`](./rutas/ruta-atacante.md) | `02-pentesting-red-team/`, `01-CIBERSEGURIDAD/02-pentesting-red-team/` |
| 🤖 Seguridad de IA | [`rutas/ruta-ai-security.md`](./rutas/ruta-ai-security.md) | `03-IA-AGENTES-HERRAMIENTAS/`, `03-AI-AGENTS-TOOLS/` |
| 🧪 Practicar en labs primero | [`04-LABORATORIOS/`](./../04-LABORATORIOS/) | labs propios, HTB, THM, docker-labs |

## ⚠️ Antes de empezar

1. **No te apures.** Mejor leer con calma 1 archivo por día que tragarte 8 en una noche.
2. **Toma notas en papel.** Las bases se olvidan rápido si no las escribes a mano al menos una vez.
3. **Practica después de leer.** Cada tema enlaza con algo del repo. La teoría sin práctica no entra.
4. **Pregunta sin miedo.** Abre un issue, manda un PR, o edita lo que creas que falta. Este repo mejora cuando la comunidad lo toca.

## 📚 Cómo está organizado este repo (resumen rápido)

```
(raíz)/
├── 00-FUNDAMENTOS/         ← ESTÁS AQUÍ (base para principiantes)
├── 01-CIBERSEGURIDAD/      ← Roles profesionales y temas generales
├── 02-SEGURIDAD-INFORMACION/  ← GRC, riesgo, cumplimiento
├── 02-pentesting-red-team/ ← Red team + labs específicos
├── 03-AI-AGENTS-TOOLS/     ← Seguridad de IA (en inglés)
├── 03-IA-AGENTES-HERRAMIENTAS/ ← Seguridad de IA (en español)
├── 03-blue-team-defensa/   ← Defensa, SOC, fundamentos blue team
├── 04-LABORATORIOS/        ← Labs propios, CTFs, HTB/THM
├── 04-purple-team-colaboracion/  ← Colaboración red + blue
├── 05-RECURSOS/            ← Libros, certificaciones, cursos, cheatsheets
└── docs/                   ← El sitio web publicado en GitHub Pages
```

Cuando termines la base, salta a la ruta que más te interese. 🚀

---

> 💡 **Tip:** Si un archivo de la base te queda corto o quieres profundizar, busca el tema en `04-LABORATORIOS/` (teoría con práctica) o en `01-CIBERSEGURIDAD/` (roles profesionales).
