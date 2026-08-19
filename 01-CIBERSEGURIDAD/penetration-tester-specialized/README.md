<div align="center">

# 🎯 Penetration Tester (Especializado)

**NIST NICE · Penetration Tester (Advanced)**

*"Cuando el OSCP ya no te impresiona y empiezas a buscar lo que rompe."*

![Tier](https://img.shields.io/badge/tier%20salarial-A%2FS-purple) ![Demanda](https://img.shields.io/badge/demanda-alta-green) ![Entry](https://img.shields.io/badge/entry%20level-experto-critical)

</div>

---

## 📋 Descripción

Evolución del pentester generalista hacia un **nicho profundo**: web app exploitation avanzada, exploit development, red teaming con evasión, kernel/driver, mobile, ICS/OT, hardware o AppSec ofensivo. Aquí cada línea de código que escribes vale más — porque pocos lo entienden.

Distinción clave con `pentester-red-team` (rama generalista):
- **Generalista**: cubre web + AD + cloud con metodología
- **Especializado**: domina **un vertical** a profundidad de bypass de mitigaciones (ASLR, DEP, CFG, AMSI, EDR userland hooks)

---

## 👤 Roles típicos

- **Senior Web Application Pentester** — OSWE-tier, white-box reviews
- **Red Team Operator senior** — OSEP, evasion + custom tooling
- **Exploit Developer** — OSED, 0-days, ROP/JOP, kernel
- **Mobile Pentester** — iOS/Android, jailbreak / root
- **ICS/OT Pentester** — protocolos industriales (combo con `seguridad-iot-ot`)
- **Hardware Security Researcher** — embedded, side-channel, JTAG
- **Adversary Emulation Engineer** *(big tech)* — purple-aligned

---

## 🛠️ Stack y herramientas

| Categoría | Herramientas |
|---|---|
| **Exploit dev** | Ghidra · IDA Pro · radare2 · x64dbg · WinDbg · pwntools · ROPgadget · pwndbg |
| **Web avanzado** | Burp Suite Pro · Caido · Param Miner · Logger++ · Autorize · custom Python |
| **AD avanzado** | Rubeus · BloodHound CE · Certipy · ADCS attack tools · NetExec · pyKRB5 |
| **Evasion** | Donut · Sliver custom profiles · Mythic agents · Havoc · syscalls direct |
| **Mobile** | Frida · Objection · MobSF · Burp Mobile · Drozer · iLEAPP · Magisk |
| **Reverse / unpacking** | Ghidra · IDA + Hex-Rays · Binary Ninja · de4dot |
| **Fuzzing** | AFL++ · libFuzzer · honggfuzz · radamsa · BooFuzz (proto) |
| **Kernel** | WinDbg + symbols · LiveKD · IDA + decompilers · Volatility for crash dumps |
| **Hardware** | ChipWhisperer · JTAG · UART · Bus Pirate · Saleae · HackRF |

---

## 🎓 Certificaciones recomendadas

| Nivel | Certificación | Vendor | Costo (USD) | Notas |
|---|---|---|---|---|
| Pre-req | OSCP | OffSec | ~$1,649 | Asumida |
| Mid | OSWE (Web) | OffSec | ~$1,649 | White-box web exploitation |
| Mid | OSEP (Evasion) | OffSec | ~$1,649 | Red team con bypass |
| Mid | OSED (Exploit Dev) | OffSec | ~$1,649 | Windows exploit dev |
| Mid | CRTO / CRTL | Zero-Point Sec | ~$365-500 | Cobalt Strike + C2 ops |
| Mid | OSMR / OSWP | OffSec | ~$450-1,649 | Mobile / Wi-Fi |
| Senior | OSCE3 (OSEP+OSWE+OSED) | OffSec | ~$5,000 | Trinity, top tier |
| Senior | OSEE | OffSec | ~$3,000 | Hardware/embedded |
| Senior | GIAC GXPN | SANS | ~$2,500+ | Exploit dev SANS |

---

## 🗺️ Roadmap (12 meses, post-OSCP)

### Fase 1 — Elegir nicho (0-2 meses)
- [ ] Decidir vertical: web (OSWE) | red team (OSEP) | exploit dev (OSED) | mobile | ICS | hardware
- [ ] Lectura central del nicho (e.g. *The Web App Hacker's Handbook* o *Practical Reverse Engineering*)
- [ ] 5 retos de la vertical en HTB Endgame / Pro Labs / RingZer0

### Fase 2 — Inmersión técnica (2-8 meses)
- [ ] Curso oficial del nicho (OffSec, SANS, INE)
- [ ] 30+ horas en lab dedicado (PG Practice avanzado, exploit.education)
- [ ] Replicar 3 CVEs públicos del último año en el nicho
- [ ] Cert del nicho aprobada (OSWE / OSEP / OSED / etc.)

### Fase 3 — Aporte y reputación (8-12 meses)
- [ ] Bug bounty en el nicho (HackerOne / Bugcrowd) con al menos 1 hallazgo válido
- [ ] Charla técnica o write-up de 0-day reproducido
- [ ] Contribución a una herramienta open source del nicho
- [ ] Networking en cons (DEF CON, BSides, Ekoparty 🇦🇷, Andsec 🇨🇴)

---

## 💰 Salarios en Colombia (USD/mes)

| Nivel | Local 🇨🇴 | Remoto 🌎 | Notas |
|---|---|---|---|
| Mid (post-OSCP, 1 cert avanzada) | $2,500 - $5,000 | $5,000 - $9,000 | OSWE/OSEP es palanca |
| Senior (3+ certs avanzadas) | $5,500 - $10,000 | $9,000 - $16,000 | OSCE3 = top tier LATAM |
| Principal / Researcher | $8,000 - $15,000+ | $14,000 - $25,000+ | 0-day discoverers, big tech |

> **Tip:** este nicho **se paga por reputación demostrable** (0-days, CVEs, charlas). El cv pesa menos que el GitHub público.

---

## 🔗 Conexión con otras ramas

- **`pentester-red-team`** → tu base previa
- **`malware-analyst`** → reverse engineering overlap profundo
- **`bug-bounty-hunting`** → ingreso variable complementario
- **`seguridad-iot-ot`** → si vas hardware/ICS
- **`cryptographer`** → si te metes en CTF crypto / TLS exploitation
- **`ai-red-teamer`** *(03)* → AI red team es un nicho emergente especializado

---

## 📂 Estructura

```
penetration-tester-specialized/
├── herramientas/    # Custom payloads, evasion templates, exploit POCs
├── recursos/        # Papers, blogs (Project Zero, Phrack, Tenable Research)
├── laboratorios/    # PG Practice notes, HTB Pro Labs writeups
└── casos-uso/       # CVEs reproducidos, 0-days éticos, write-ups técnicos
```

---

<div align="center">

**[⬅ Volver a Ciberseguridad](../README.md)**

</div>
