<div align="center">

# 🏹 Bug Bounty Hunting

**Emerging 2024-2026 · Independent Vulnerability Researcher**

*"Cazador autónomo. Sin jefe, sin oficina — pero también sin sueldo fijo."*

![Tier](https://img.shields.io/badge/tier%20salarial-Variable-yellow) ![Demanda](https://img.shields.io/badge/oportunidad-global-brightgreen) ![Entry](https://img.shields.io/badge/entry%20level-medio--alto-yellow)

</div>

---

## 📋 Descripción

Modalidad **freelance global**: encontrar vulnerabilidades en programas de bug bounty (HackerOne, Bugcrowd, Intigriti, YesWeHack, Synack) y cobrar por hallazgo válido. **No es un empleo** — es un negocio personal.

Diferencia con `pentester-red-team`:
- **Pentester**: contrato, scope acotado, paga fija por engagement
- **Bug bounty**: scope público, paga por bug válido, **0 ingresos garantizados**

Se siente glamoroso (top hunters ganan $500K-$1M USD/año) pero es **brutal** estadísticamente: el percentil 50 gana <$5K/año. Es un side hustle excelente, una carrera incierta.

---

## 👤 Modalidades / "roles"

- **Hunter generalista** — programas amplios, dificultad media
- **Web hunter especializado** — IDOR, SSRF, GraphQL, OAuth, race conditions
- **Mobile hunter** — iOS / Android, menos competidos
- **API hunter** — REST + GraphQL + gRPC business logic
- **Recon-heavy hunter** — automation + 1-day patches
- **Private invite hunter** *(top tier)* — Synack Red Team, HackerOne MVH

---

## 🛠️ Stack y herramientas

| Categoría | Herramientas |
|---|---|
| **Recon automation** | Subfinder · Amass · httpx · nuclei · gowitness · gau · waybackurls · ChaosDB |
| **Web exploitation** | Burp Suite Pro · Caido · ZAP · Param Miner · Logger++ · Autorize · Postman |
| **APIs** | Postman · Insomnia · gRPCurl · Burp + custom extensions |
| **Mobile** | Frida · Objection · Burp Mobile · MobSF · jadx · Ghidra |
| **Custom tooling** | Python · Go · Bash · jq · grep |
| **VPS / infra** | DigitalOcean · Hetzner · Linode · auto-deploy with Terraform |
| **Note-taking** | Obsidian · Notion · GitHub private · Markdown |
| **Frameworks de research** | OWASP Web · OWASP API Top 10 · OWASP Mobile · PortSwigger Academy |

---

## 🎓 Certificaciones / formación

| Nivel | Vía | Costo (USD) | Notas |
|---|---|---|---|
| Entry | PortSwigger Web Security Academy | $0 | Gratis y excelente |
| Entry | TryHackMe Web Fundamentals | $10/mes | Puerta de entrada |
| Entry | Bug Bounty Hunter Path (TryHackMe) | $10/mes | 6 meses dedicación |
| Mid | BSCP (Burp Suite Certified Practitioner) | ~$99 | Excelente costo-beneficio |
| Mid | eWPT / eWPTXv2 | ~$400-600 | Web pentest aplicado |
| Senior | OSWE | ~$1,649 | White-box web exploitation |
| Senior | OSWP / OSEP *(opcional)* | ~$450-1,649 | Para diversificar |

---

## 🗺️ Roadmap (12 meses)

### Fase 1 — Fundamentos (0-4 meses)
- [ ] PortSwigger Academy: Apprentice + 50% de Practitioner
- [ ] OWASP Top 10 + API Top 10 estudiados
- [ ] BSCP aprobado
- [ ] 3 reportes informativos (no críticos) submitted en HackerOne

### Fase 2 — Primer hallazgo válido (4-7 meses)
- [ ] Programa elegido y conocido a profundidad (no saltar)
- [ ] Recon automation propio (subfinder + nuclei + diff alerts)
- [ ] Primer bug **válido** (Triaged) — celebrarlo
- [ ] Notas estructuradas tipo "war journal" (Obsidian)

### Fase 3 — Estabilización (7-12 meses)
- [ ] 5+ bugs válidos (mix Low + Med + High)
- [ ] Especializarse en 1 vertical (e.g. SSRF, IDOR, business logic)
- [ ] Public writeups éticos (sin doxing al programa)
- [ ] Decisión: hobby vs full-time vs combo con empleo

---

## 💰 Salarios / ingresos en Colombia (USD)

> **Crítico entender:** bug bounty es **renta variable**. La distribución es Pareto extrema.

| Percentil | Ingreso anual estimado | Realidad |
|---|---|---|
| P10 (bajo) | $0 - $1,500 | La mayoría no llega aquí |
| P50 (mediana) | $2,000 - $8,000 | Side hustle decente |
| P75 | $15,000 - $40,000 | Combo con empleo full-time |
| P90 | $60,000 - $150,000 | Full-time hunter, top 10% |
| P99 | $250,000 - $1M+ | Top 1% mundial, escasos |

> **Tip honesto:** trata bug bounty como **side hustle** los primeros 18 meses. Si después de un año constante estás en P75+, considera full-time. **Nunca** dejes empleo full-time pre-validar 12+ meses de ingresos.

---

## 🔗 Conexión con otras ramas

- **`pentester-red-team`** → mismo skillset, modelo distinto
- **`seguridad-aplicaciones`** → AppSec defensivo desde otra cara
- **`penetration-tester-specialized`** → si te vuelves OSWE-tier, los bounties pagan más
- **`vulnerability-manager`** → tus reportes son su input
- **`malware-analyst`** → si vas hacia 0-days

---

## 📂 Estructura

```
bug-bounty-hunting/
├── herramientas/    # Recon scripts, custom Burp extensions, automation
├── recursos/        # PortSwigger labs notes, OWASP cheatsheets
├── laboratorios/    # PortSwigger Practitioner solved labs
└── casos-uso/       # Reportes públicos / writeups éticos (post-disclosure)
```

---

<div align="center">

**[⬅ Volver a Ciberseguridad](../README.md)**

</div>
