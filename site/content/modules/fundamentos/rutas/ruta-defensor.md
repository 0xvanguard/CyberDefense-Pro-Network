---
title: "🛡️ Ruta: Defensor (Blue Team)"
---

# 🛡️ Ruta: Defensor (Blue Team)

> **Para quién es esto:** gente que disfruta encontrar al malo, mirar logs, configurar detecciones y responder a incidentes. No te gusta destruir, te gusta proteger.

## Mentalidad

> "Los atacantes tienen que acertar UNA vez. Yo tengo que acertar SIEMPRE."

Eso suena injusto, pero también significa que tu trabajo se nota cuando funciona (nada se rompe) y se nota MUCHO cuando no funciona (algo se rompe enorme). Por eso defender bien es difícil y por eso se paga bien.

## Paso 1 — Refuerza la base

Si vienes de [`../01-que-es-ciberseguridad.md`](../01-que-es-ciberseguridad.md), ya sabes que Blue Team tiene roles como:
- Analista SOC
- Threat Hunter
- Incident Responder
- Threat Intelligence
- Forense
- Malware Analyst

Lee sus definiciones en [`../../01-CIBERSEGURIDAD/`](../../01-CIBERSEGURIDAD/) (busca las subcarpetas con esos nombres).

## Paso 2 — Aprende lo técnico defensivo

### Redes (lo más importante)
- Lee [`../03-internet-y-redes.md`](../03-internet-y-redes.md) si aún no lo hiciste.
- Aprende a leer PCAPs con Wireshark.
- Entiende cómo se mueve un atacante lateralmente.

### Logs (donde vive la verdad)
- [`../04-sistema-operativo-y-terminal.md`](../04-sistema-operativo-y-terminal.md) tiene las ubicaciones de logs en Linux y los Event IDs clave en Windows.
- Practica filtrar: `grep`, `awk`, `jq`, Splunk Search Processing Language (SPL).

### Herramientas
- Wazuh / OSSEC — HIDS
- Splunk / ELK — SIEM
- Velociraptor — endpoint DFIR
- MISP / OpenCTI — Threat Intel

## Paso 3 — Recorre las carpetas del repo relevantes

En orden sugerido:

| Carpeta | Qué aporta |
|---|---|
| [`../../03-blue-team-defensa/`](../../03-blue-team-defensa/) | Punto de entrada Blue Team con labs específicos |
| [`../../03-blue-team-defensa/01-fundamentos-blue-team-y-soc/`](../../03-blue-team-defensa/01-fundamentos-blue-team-y-soc/) | SOC fundamentals + labs de logs |
| [`../../02-SEGURIDAD-INFORMACION/02-blue-team-defensa/`](../../02-SEGURIDAD-INFORMACION/02-blue-team-defensa/) | SIEM Wazuh, threat hunting, MITRE D3FEND |
| [`../../01-CIBERSEGURIDAD/seguridad-defensiva-blue-team/`](../../01-CIBERSEGURIDAD/seguridad-defensiva-blue-team/) | Hardening, casos de uso, herramientas |
| [`../../01-CIBERSEGURIDAD/analista-soc/`](../../01-CIBERSEGURIDAD/analista-soc/) | Vista de un analista SOC |
| [`../../01-CIBERSEGURIDAD/threat-hunter/`](../../01-CIBERSEGURIDAD/threat-hunter/) | Hunting proactivo |
| [`../../01-CIBERSEGURIDAD/incident-responder/`](../../01-CIBERSEGURIDAD/incident-responder/) | Pasos de respuesta a incidentes |
| [`../../01-CIBERSEGURIDAD/malware-analyst/`](../../01-CIBERSEGURIDAD/malware-analyst/) | Análisis reversible |
| [`../../01-CIBERSEGURIDAD/forense-digital/`](../../01-CIBERSEGURIDAD/forense-digital/) | Forensia digital |
| [`../../01-CIBERSEGURIDAD/security-analyst/`](../../01-CIBERSEGURIDAD/security-analyst/) | Rol generalista |
| [`../../04-purple-team-colaboracion/`](../../04-purple-team-colaboracion/) | Colaboración con red team |

## Paso 4 — Practica con labs

| Lab | Para qué |
|---|---|
| [`../../04-LABORATORIOS/labs-propios/`](../../04-LABORATORIOS/labs-propios/) | Labs diseñados por este repo |
| [`../../02-blue-team-defensa/01-fundamentos-blue-team-y-soc/laboratorios/`](../../03-blue-team-defensa/01-fundamentos-blue-team-y-soc/laboratorios/) | Lectura interpretación logs SOC |
| TryHackMe SOC path | [tryhackme.com/path/outline/soc](https://tryhackme.com/) |
| Blue Team Labs Online | [blueteamlabs.online](https://blueteamlabs.online/) |

## Paso 5 — Aprende el marco MITRE

- **MITRE ATT&CK** — cómo piensa y actúa un atacante
- **MITRE D3FEND** — técnicas defensivas para contrarrestar
- **MITRE Caldera** — emular atacantes en tu entorno

Útil: lee [`../../01-CIBERSEGURIDAD/threat-intelligence/`](../../01-CIBERSEGURIDAD/threat-intelligence/) para Threat Intel básico.

## Paso 6 — Certificaciones (opcional pero útil)

Orden sugerido:

1. **BTL1** (Blue Team Level 1) —基础的, excelente para empezar.
2. **CompTIA Security+** — base general.
3. **SC-200** (Microsoft Security Operations Analyst) — Azure + Sentinel.
4. **GCIH** (GIAC Certified Incident Handler) — respuesta a incidentes.
5. **GCFA** (GIAC Certified Forensic Analyst) — forense.
6. **CISSP** — cuando tengas experiencia.

Más recursos en [`../../05-RECURSOS/certificaciones/`](../../05-RECURSOS/certificaciones/).

## Paso 7 — Haz "home labs" reales

- Monta un SIEM casero (ELK o Wazuh + VMs).
- Levanta un endpoint y prueba detecciones.
- Genera tráfico malicioso controlado y mira qué loggea.
- Escribe detecciones propias y mide falsos positivos.

## ✏️ Plan de 30 días para empezar

- **Semana 1:** relee [`../02-glosario.md`](../02-glosario.md) y abre [`../../03-blue-team-defensa/`](../../03-blue-team-defensa/).
- **Semana 2:** completa 2 labs en [`../../03-blue-team-defensa/01-fundamentos-blue-team-y-soc/laboratorios/`](../../03-blue-team-defensa/01-fundamentos-blue-team-y-soc/laboratorios/).
- **Semana 3:** monta Wazuh o ELK en tu VM y configura detección básica.
- **Semana 4:** lee todo lo de [`../../02-SEGURIDAD-INFORMACION/02-blue-team-defensa/`](../../02-SEGURIDAD-INFORMACION/02-blue-team-defensa/) y elige una de las áreas (SOC, hunting, forense) para profundizar.

> 🟣 **Bonus:** si haces Red Team además de Blue Team, mira [`../../04-purple-team-colaboracion/`](../../04-purple-team-colaboracion/). El perfil completo Blue+Red es muy buscado.

---

> ⏪ **Volver al mapa:** [`../09-como-seguir-este-repo.md`](../09-como-seguir-este-repo.md)
> ⚔️ **Otra ruta:** [`./ruta-atacante.md`](./ruta-atacante.md) si te interesa el lado ofensivo.
