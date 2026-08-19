<div align="center">

# 🏭 Seguridad IoT / OT

**CISSP Domain · Industrial Control & IoT Security**

*"Cuando el ataque deja de ser bytes y empieza a ser kilovatios."*

![Tier](https://img.shields.io/badge/tier%20salarial-A-orange) ![Demanda](https://img.shields.io/badge/demanda-creciente-green) ![Entry](https://img.shields.io/badge/entry%20level-medio--alto-yellow)

</div>

---

## 📋 Descripción

Disciplina que protege **dispositivos conectados (IoT)** e **infraestructura crítica (OT/ICS)**: redes industriales, SCADA, PLCs, edificios inteligentes, dispositivos médicos, automotive. Es donde la ciberseguridad cruza con la seguridad física — un fallo aquí no roba datos, **detiene una planta o un hospital**.

Nicho premium con demanda explosiva por NIS2 (UE), CIRCIA (US) y los estándares IEC 62443. Profesional ideal: alguien con base en redes/sistemas + dispuesto a aprender protocolos industriales (Modbus, DNP3, OPC UA, BACnet).

---

## 👤 Roles típicos

- **OT/ICS Security Engineer** — diseño y operación en plantas industriales
- **IoT Security Engineer** — productos conectados, embedded
- **ICS Pentester** *(senior, escaso)* — pentest seguro en entornos OT
- **OT SOC Analyst** — alertas con Claroty / Nozomi / Dragos
- **Healthcare Device Security** *(MDM2)* — dispositivos médicos conectados

---

## 🛠️ Stack y herramientas

| Categoría | Herramientas |
|---|---|
| **OT visibility / IDS** | Claroty · Nozomi Networks · Dragos · Tenable.OT · Microsoft Defender for IoT · Forescout |
| **Protocolos** | Modbus · DNP3 · OPC UA · BACnet · IEC 61850 · S7Comm · CIP/EtherNet-IP |
| **Pentest IoT** | Firmware Mod Kit · binwalk · firmadyne · radare2 · Ghidra · attify · routersploit |
| **Hardware hacking** | JTAG · UART · SPI · Bus Pirate · Saleae · ChipWhisperer · HackRF |
| **Wireless** | Aircrack-ng · Kismet · BLE: bettercap, gatttool · Zigbee: KillerBee |
| **Embedded** | OpenWrt · Yocto · QEMU · GDB · binwalk |
| **Healthcare** | Medigate (Claroty) · Cynerio · MedCrypt |
| **Standards refs** | IEC 62443 · ISA-99 · NIST SP 800-82 · NERC CIP · IEC 27019 |

---

## 🎓 Certificaciones recomendadas

| Nivel | Certificación | Vendor | Costo (USD) | Notas |
|---|---|---|---|---|
| Entry | CompTIA Security+ | CompTIA | ~$400 | Base general |
| Mid | GICSP | SANS / GIAC | ~$2,500+ | Estándar OT |
| Mid | IEC 62443 Cybersecurity Specialist | ISA | ~$2,000 | Familia completa |
| Mid | OPSWAT OT Cybersecurity | OPSWAT | ~$200 | Buena puerta de entrada |
| Senior | GRID (GIAC Response and Industrial Defense) | SANS | ~$2,500+ | IR en OT |
| Senior | OSEE (hardware/embedded) | OffSec | ~$3,000 | Top tier ofensivo |

---

## 🗺️ Roadmap (12 meses)

### Fase 1 — Fundamentos (0-3 meses)
- [ ] Diferencias TI vs OT (CIA vs availability-first, parcheo, lifecycles 20+ años)
- [ ] Lectura: *Industrial Network Security* (Knapp & Langill)
- [ ] Lab: ConPot (honeypot ICS) + Wireshark capturando Modbus
- [ ] Security+ aprobado

### Fase 2 — Especialización (3-6 meses)
- [ ] Configurar pfSense con segmentación zonas IEC 62443 (Purdue)
- [ ] Análisis de firmware con binwalk + radare2 (router casero)
- [ ] Trial de Claroty / Nozomi (cuando haya disponibilidad)
- [ ] GICSP empezado o IEC 62443 Specialist

### Fase 3 — Profesional (6-12 meses)
- [ ] Hardware hacking básico: leer firmware vía SPI con Bus Pirate
- [ ] Pentest controlado a un dispositivo IoT comercial (con autorización)
- [ ] Diseño de red OT segmentada (IT/OT DMZ + Purdue Levels)
- [ ] GICSP aprobado

---

## 💰 Salarios en Colombia (USD/mes)

| Nivel | Local 🇨🇴 | Remoto 🌎 | Notas |
|---|---|---|---|
| Junior (0-2 años) | $800 - $1,500 | $1,500 - $2,800 | Pocas vacantes, alto pago |
| Mid (2-5 años) | $2,200 - $4,200 | $3,800 - $7,000 | GICSP duplica el rango |
| Senior (5+ años) | $5,000 - $9,500 | $8,500 - $15,000 | Energía/oil & gas remoto = top |

> **Tip:** sectores con mayor demanda en CO: energía, oil & gas, manufactura, agua, salud.

---

## 🔗 Conexión con otras ramas

- **`seguridad-redes`** → segmentación Purdue + DMZ industrial
- **`incident-responder`** → IR en OT exige protocolos distintos (no parchear sin coordinación)
- **`forense-digital`** → forense de PLCs y HMIs
- **`malware-analyst`** → familias específicas (Industroyer, Triton, Stuxnet)
- **`grc-compliance`** → NIS2, IEC 62443, NERC CIP

---

## 📂 Estructura

```
seguridad-iot-ot/
├── herramientas/    # Configs ConPot, scripts binwalk, hardware notes
├── recursos/        # IEC 62443, NIST 800-82, Purdue model
├── laboratorios/    # ConPot + Wireshark + Modbus traffic
└── casos-uso/       # Triton, Industroyer reverse, IoT firmware analysis
```

---

<div align="center">

**[⬅ Volver a Ciberseguridad](../README.md)**

</div>
