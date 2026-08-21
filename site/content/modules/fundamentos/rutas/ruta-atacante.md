---
title: "⚔️ Ruta: Atacante (Red Team / Pentest)"
---

# ⚔️ Ruta: Atacante (Red Team / Pentest)

> **Para quién es esto:** gente curiosa por saber cómo se rompen las cosas, que disfruta un reto técnico y quiere entender al adversario. **Con responsabilidad**: ética primero, ley primero,siempre.

## Mentalidad

> "Si rompo esto aquí, ¿qué roto en producción? ¿Quién se entera? ¿Cómo se defiende?"

Antes de empezar, lee [`../07-etica-y-leyes.md`](../07-etica-y-leyes.md). Si no estás cómodo con ese marco, esta ruta no es para ti.

## Paso 1 — Roles y caminos

El red team tiene varios sub-roles:
- **Pentester** — auditorías cortas (1-2 semanas)
- **Red Teamer** — simulación prolongada de un adversary (semanas-meses)
- **Bug Bounty Hunter** — freelance, trabaja por recompensa
- **Exploit Developer** — escribe los exploits que otros usan

## Paso 2 — Refuerza la base técnica

- Lee [`../03-internet-y-redes.md`](../03-internet-y-redes.md) — profunda: TCP, HTTP, DNS, TLS.
- Lee [`../04-sistema-operativo-y-terminal.md`](../04-sistema-operativo-y-terminal.md) — vive en la terminal.
- Aprende algo de scripting: **Python es obligatorio**, Bash también.
- Repasa [`../06-vulnerabilidades.md`](../06-vulnerabilidades.md) — entiende OWASP, CVEs, CWE.

## Paso 3 — Recorre las carpetas relevantes

En orden sugerido:

| Carpeta | Qué aporta |
|---|---|
| [`../../02-pentesting-red-team/`](../../02-pentesting-red-team/) | Punto de entrada en español con labs específicos |
| [`../../02-pentesting-red-team/teoria/`](../../02-pentesting-red-team/teoria/) | Metodología pentest vs red team |
| [`../../02-pentesting-red-team/laboratorios/`](../../02-pentesting-red-team/laboratorios/) | Lab concreto: pentest web |
| [`../../01-CIBERSEGURIDAD/02-pentesting-red-team/`](../../01-CIBERSEGURIDAD/02-pentesting-red-team/) | Pentest desde el superset |
| [`../../01-CIBERSEGURIDAD/01-reconocimiento-osint/`](../../01-CIBERSEGURIDAD/01-reconocimiento-osint/) | OSINT y reconocimiento |
| [`../../01-CIBERSEGURIDAD/03-analisis-vulnerabilidades/`](../../01-CIBERSEGURIDAD/03-analisis-vulnerabilidades/) | Análisis de bugs |
| [`../../01-CIBERSEGURIDAD/04-explotacion-web/`](../../01-CIBERSEGURIDAD/04-explotacion-web/) | Explotación web |
| [`../../01-CIBERSEGURIDAD/05-post-explotacion/`](../../01-CIBERSEGURIDAD/05-post-explotacion/) | Qué hacer después |
| [`../../01-CIBERSEGURIDAD/07-ingenieria-social/`](../../01-CIBERSEGURIDAD/07-ingenieria-social/) | Social engineering |
| [`../../01-CIBERSEGURIDAD/bug-bounty-hunting/`](../../01-CIBERSEGURIDAD/bug-bounty-hunting/) | Carrera bug bounty |
| [`../../01-CIBERSEGURIDAD/pentester-red-team/`](../../01-CIBERSEGURIDAD/pentester-red-team/) | Rol pentester |

## Paso 4 — Practica con labs externos y propios

Orden de dificultad creciente:

| Plataforma | Lab nivel introductorio |
|---|---|
| [TryHackMe](https://tryhackme.com/) | "Jr Penetration Tester" path |
| [HackTheBox](https://www.hackthebox.com/) | Starting Point (gratis) |
| [PortSwigger Web Security Academy](https://portswigger.net/web-security) | Labs web GRATIS |
| [PentesterLab](https://pentesterlab.com/) | Web + binary |
| DVWA / WebGoat / OWASP Juice Shop (Docker) | Apps vulnerables locales |

Para labs propios del repo: [`../../04-LABORATORIOS/labs-propios/`](../../04-LABORATORIOS/labs-propios/), [`../../04-LABORATORIOS/docker-labs/`](../../04-LABORATORIOS/docker-labs/) y writeups en [`../../04-LABORATORIOS/ctf-writeups/`](../../04-LABORATORIOS/ctf-writeups/).

## Paso 5 — Aprende las fases

Las que usan marcos como PTES, OWASP y NIST:

1. **Pre-engagement** — contrato, scope, reglas
2. **Reconocimiento** (pasivo / activo)
3. **Enumeración** — servicios, versiones, users
4. **Análisis de vulnerabilidades**
5. **Explotación**
6. **Post-explotación** — pivot, persistencia
7. **Reporte**

Las herramientas por fase:

```
nmap → masscan → rustscan
├── whatweb → Wappalyzer
├── gobuster → feroxbuster
├── Burp Suite / ZAP
├── Metasploit / searchsploit
├── LinPEAS / WinPEAS (priv esc)
└── BloodHound (Active Directory)
```

## Paso 6 — Reporte — la mitad del trabajo

El éxito de un pentest se mide **por el reporte, no por los hallazgos**.

Boilerplate útil en [`../../02-pentesting-red-team/portafolio/`](../../02-pentesting-red-team/portafolio/) y templates de informe.

Estructura recomendada:
1. Resumen ejecutivo (1 página, sin jerga, para CISO)
2. Metodología
3. Hallazgos
   - Título + severidad + CVE/CWE/CVSS
   - Descripción
   - Pasos para reproducir
   - Impacto
   - Evidencia (screenshots, HTTP requests)
   - Recomendación
4. Conclusiones

## Paso 7 — Certificaciones (opcional pero muy útil)

Orden sugerido:

1. **eJPT** (eLearnSecurity Junior Penetration Tester) — primer paso accesible.
2. **CompTIA PenTest+** — base general.
3. **PNPT** (Practical Network Penetration Tester) — práctico.
4. **OSCP** — la referencia de facto en pentest.
5. **OSWE** — si te enfocas en web.
6. **CRTO** — si te enfocas en red team moderno.
7. **CRTP** — Active Directory.

Ve [`../../05-RECURSOS/certificaciones/`](../../05-RECURSOS/certificaciones/) y [`../../05-RECURSOS/cheatsheets/`](../../05-RECURSOS/cheatsheets/).

## Paso 8 — Tu carrera / especialízate

- **Web**: bug bounty, PortSwigger Academy, HackerOne
- **Redes/Infrastructure**: OSCP, CRTP
- **Active Directory**: BloodHound, Mimikatz (en labs)
- **Mobile**: Android, iOS
- **Hardware/IoT**: cosas raras
- **Social engineering**: phishing, vishing (ojo: solo autorizado)

## ✏️ Plan de 30 días para empezar

- **Semana 1:** instala Kali o tira una VM Ubuntu. Aprende 5 comandos diarios. Termina [`../04-sistema-operativo-y-terminal.md`](../04-sistema-operativo-y-terminal.md).
- **Semana 2:** completa TryHackMe "Jr Penetration Tester" path hasta la mitad. Lee [`../08-herramientas-esenciales.md`](../08-herramientas-esenciales.md).
- **Semana 3:** resuelve 3 retos de PortSwigger Academy (XSS, SQLi, SSRF). Lee [`../06-vulnerabilidades.md`](../06-vulnerabilidades.md) a fondo.
- **Semana 4:** abre [`../../02-pentesting-red-team/`](../../02-pentesting-red-team/) y haz el lab de [`../../02-pentesting-red-team/laboratorios/`](../../02-pentesting-red-team/laboratorios/). Escribe tu primer mini-reporte.

> 🟣 **Bonus:** combina Red+Blue en [`../../04-purple-team-colaboracion/`](../../04-purple-team-colaboracion/).

---

> ⏪ **Volver al mapa:** [`../09-como-seguir-este-repo.md`](../09-como-seguir-este-repo.md)
> 🛡️ **Otra ruta:** [`./ruta-defensor.md`](./ruta-defensor.md) si quieres defender.
