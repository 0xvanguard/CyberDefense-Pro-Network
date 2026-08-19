<div align="center">

# 🌐 Seguridad de Redes

**CISSP Domain · Network Security**

*"El perímetro ya no existe — pero la red sigue siendo el campo de batalla."*

![Tier](https://img.shields.io/badge/tier%20salarial-B-blue) ![Demanda](https://img.shields.io/badge/demanda-alta-green) ![Entry](https://img.shields.io/badge/entry%20level-amigable-success)

</div>

---

## 📋 Descripción

Disciplina enfocada en **proteger la infraestructura de red** — desde el datacenter clásico hasta arquitecturas Zero Trust modernas. Cubre diseño seguro, segmentación, detección de tráfico malicioso, control de acceso y respuesta a incidentes de red.

Es una de las ramas de entrada más sólidas a ciberseguridad porque conecta directamente con la base de cualquier sysadmin: TCP/IP, routing, firewalls, VPN. La evolución 2024-2026 está empujando hacia **SASE, ZTNA y microsegmentación**, dejando atrás el modelo de "castillo y foso".

---

## 👤 Roles típicos

- **Network Security Engineer** — diseña, implementa y mantiene firewalls, IDS/IPS, VPN
- **Firewall Administrator** — gestión BAU de reglas, change management, auditoría
- **SOC Tier 2 Network** — investigación de alertas de tráfico (IDS/IPS, NetFlow)
- **Zero Trust Architect** *(senior)* — diseño de arquitecturas ZTNA/SASE
- **NOC/SecOps Hybrid** — entornos pequeños donde se combinan funciones

---

## 🛠️ Stack y herramientas

| Categoría | Herramientas |
|---|---|
| **Firewalls (NGFW)** | Palo Alto · Fortinet FortiGate · Cisco Firepower · pfSense · OPNsense · Check Point |
| **IDS/IPS** | Suricata · Snort · Zeek (antes Bro) · Cisco Stealthwatch |
| **VPN / ZTNA** | OpenVPN · WireGuard · Cisco AnyConnect · Cloudflare Access · Tailscale · Twingate |
| **NAC** | Cisco ISE · Aruba ClearPass · FortiNAC · packetfence |
| **Análisis de tráfico** | Wireshark · tshark · tcpdump · nfdump · Arkime (Moloch) |
| **Pentest red** | Nmap · Masscan · Responder · MITM6 · Bettercap |
| **Segmentación** | VLANs · 802.1X · VXLAN · Calico (k8s) · Illumio · Guardicore |

---

## 🎓 Certificaciones recomendadas

| Nivel | Certificación | Vendor | Costo (USD) | Notas |
|---|---|---|---|---|
| Entry | CompTIA Network+ | CompTIA | ~$370 | Base obligatoria si no vienes de redes |
| Entry | CompTIA Security+ | CompTIA | ~$400 | Pareja del Network+ |
| Mid | CCNA Security *(legacy)* / CCNP Security | Cisco | ~$300-600 | Estándar enterprise |
| Mid | Fortinet NSE 4-5 | Fortinet | ~$400 | Muy demandado en LATAM |
| Mid | Palo Alto PCNSA → PCNSE | Palo Alto | ~$200-400 | Top tier en mercado |
| Senior | CISSP | (ISC)² | ~$750 | Exige 5 años de experiencia |
| Senior | GIAC GCIA / GCNF | SANS | ~$2,500+ | Análisis profundo de red |

---

## 🗺️ Roadmap (12 meses)

### Fase 1 — Fundamentos (0-3 meses)
- [ ] CCNA o equivalente: subnetting, routing, VLANs, ACLs
- [ ] Lab con pfSense + Suricata en VirtualBox
- [ ] Wireshark a nivel de captura y filtrado
- [ ] Network+ o Security+ aprobado

### Fase 2 — Especialización (3-6 meses)
- [ ] FortiGate o Palo Alto en modo lab (versión eval)
- [ ] OpenVPN + WireGuard montados desde cero
- [ ] Detección de túneles DNS / C2 con Suricata + reglas ET Open
- [ ] Documentar 3 incidentes de red en `casos-uso/`

### Fase 3 — Profesional (6-12 meses)
- [ ] Diseño de arquitectura segmentada (DMZ + zonas internas + ZTNA)
- [ ] Cisco ISE / Aruba ClearPass para 802.1X
- [ ] PCNSA o NSE 4 aprobado
- [ ] Caso real: deploy ZTNA en pyme (Cloudflare Access / Twingate)

---

## 💰 Salarios en Colombia (USD/mes)

| Nivel | Local 🇨🇴 | Remoto 🌎 | Notas |
|---|---|---|---|
| Junior (0-2 años) | $700 - $1,300 | $1,200 - $2,200 | Mercado bancario y telco |
| Mid (2-5 años) | $1,700 - $3,200 | $3,000 - $5,500 | NGFW + ZTNA aumenta el rango |
| Senior (5+ años) | $4,000 - $7,500 | $6,000 - $11,000 | Architect ZT/SASE = top de banda |

> **Tip:** los certificados Fortinet/Palo Alto pesan más que el título universitario en LATAM.

---

## 🔗 Conexión con otras ramas

- **`arquitecto-seguridad`** → la red es la base del diseño Zero Trust
- **`seguridad-nube`** → VPC, peering, transit gateway, CloudFront, security groups
- **`threat-hunter`** → NetFlow + Zeek son sus mejores amigos
- **`incident-responder`** → contención de red en primera línea
- **`seguridad-defensiva-blue-team`** → Suricata + Wazuh + Zeek = stack defensivo

---

## 📂 Estructura

```
seguridad-redes/
├── herramientas/    # Configs de pfSense, Suricata, FortiGate, etc.
├── recursos/        # Cheatsheets, papers, RFCs clave
├── laboratorios/    # Labs reproducibles (compose con red aislada)
└── casos-uso/       # Detección de C2, exfiltración DNS, MITM, etc.
```

---

<div align="center">

**[⬅ Volver a Ciberseguridad](../README.md)**

</div>
