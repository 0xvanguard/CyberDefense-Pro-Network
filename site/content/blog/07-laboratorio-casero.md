---
title: "Cómo crear tu laboratorio de ciberseguridad"
description: "Hardware mínimo, software recomendado y labs con Docker"
---

# Cómo crear tu laboratorio de ciberseguridad

## ¿Por qué un lab propio?

Un laboratorio personal te permite:
- **Practicar sin riesgo** — Nada se rompe
- **Experimentar** — Prueba herramientas libremente
- **Aprender haciendo** — La mejor forma de aprender
- **Construir portafolio** — Documenta tus labs

## Hardware mínimo

```
CPU: 4 cores (Intel i5 / AMD Ryzen 5)
RAM: 16 GB (mínimo 8 GB)
Disco: 256 GB SSD
Red: Tarjeta Ethernet + WiFi
```

**Presupuesto:** ~€500-800 si compras nuevo, menos si usas un servidor refurbished

## Software recomendado

| Software | Para qué | Gratis |
|----------|----------|--------|
| VirtualBox / VMware | VMs | ✅ |
| Kali Linux | Atacar | ✅ |
| Metasploitable | Victima | ✅ |
| DVWA | Web vulnerable | ✅ |
| TryHackMe | Plataforma | ✅/€10 |
| Docker | Containers | ✅ |

## Lab con Docker (el más fácil)

```bash
# Clonar lab vulnerable
git clone https://github.com/digininja/DVWA.git
cd DVWA

# Levantar
docker compose up -d

# Acceder
# http://localhost:8080
```

## Topología sugerida

```
┌─────────────────────────────────────────┐
│           TU RED DE LABORATORIO         │
├─────────────────────────────────────────┤
│  🖥️ Kali Linux (atacante)              │
│  🖥️ Metasploitable (víctima)           │
│  🖥️ DVWA (web vulnerable)              │
│  🖥️ Windows Server (AD)                │
│  🌐 Router (pfSense)                   │
└─────────────────────────────────────────┘
```

## Tips de presupuesto

- **Servidor refurbished**: Dell OptiPlex (~€150) con 16GB RAM
- **Mini PC**: Intel NUC (~€300) — silencioso y eficiente
- **Cloud**: AWS Free Tier / GCP Free Tier para labs temporales

## Conclusión

No necesitas equipo caro. Con €300 y Docker puedes tener un lab funcional. Lo importante es **empezar y practicar**.

---

*Artículo publicado en el Blog CDPN — Semana 7*
