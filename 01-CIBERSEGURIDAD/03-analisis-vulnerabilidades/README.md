# 🧠 Módulo 03 — Análisis de Vulnerabilidades

> **Objetivo Principal:** Identificar, priorizar, validar y comunicar vulnerabilidades de forma profesional usando la tríada CIA, el ciclo de gestión de vulnerabilidades y un enfoque operativo combinado de **Red Team, Blue Team y Purple Team**.

[![Nivel](https://img.shields.io/badge/Nivel-Intermedio%20→%20Avanzado-red?style=flat-square)]()
[![Enfoque](https://img.shields.io/badge/Enfoque-Red%20%7C%20Blue%20%7C%20Purple-purple?style=flat-square)]()
[![Modelo](https://img.shields.io/badge/Modelo-CIA%20Triad%20%2B%20VM%20Lifecycle-blue?style=flat-square)]()
[![Lab Docker](https://img.shields.io/badge/Lab-Docker%20incluido-orange?style=flat-square)](./laboratorio/)
[![Portafolio](https://img.shields.io/badge/Entregable-Vulnerability%20Assessment-green?style=flat-square)](./portafolio/)

---

## 📋 Resumen del módulo

| Atributo | Detalle |
|---|---|
| 🏷️ **Nivel** | Intermedio → Avanzado |
| ⏱️ **Duración estimada** | 4–6 semanas (6–8h por semana) |
| 🎯 **Resultado esperado** | Ejecutar un análisis de vulnerabilidades completo y producir un reporte con severidad, impacto CIA, validación técnica, remediación y priorización por rol |
| 🧪 **Práctica verificable** | Lab Docker con activos web y servicios vulnerables, escaneo, validación y reporte |
| 🗂️ **Portafolio** | Vulnerability Assessment Report con matriz CIA + CVSS + SLA de remediación |
| 🔗 **Requiere** | [Módulo 01 — Reconocimiento OSINT](../01-reconocimiento-osint/) · [Módulo 02 — Pentesting / Red Team](../02-pentesting-red-team/) |
| 🔗 **Conduce a** | [Módulo 04 — Explotación Web](../04-explotacion-web/) |

---

## 🎯 Qué aprenderás

- [ ] Diferenciar **hallazgo**, **debilidad**, **vulnerabilidad**, **riesgo** e **impacto**.
- [ ] Clasificar hallazgos usando la tríada **Confidencialidad, Integridad y Disponibilidad**.
- [ ] Aplicar un ciclo real de **vulnerability management**: descubrir, priorizar, remediar, validar y reportar.
- [ ] Pensar un mismo hallazgo desde 3 perspectivas: **Red Team**, **Blue Team** y **Purple Team**.
- [ ] Usar `Nuclei`, `OpenVAS/GVM`, `Nmap` y `searchsploit` para obtener y validar evidencia.
- [ ] Producir un reporte profesional con **CVSS**, impacto CIA, explotación controlada y plan de remediación.

---

## 🧭 Tres perspectivas, un solo hallazgo

| Equipo | Pregunta central | Resultado esperado |
|---|---|---|
| 🔴 **Red Team** | ¿Se puede explotar de forma realista? | Validación técnica del impacto |
| 🔵 **Blue Team** | ¿Qué activos afecta y cómo lo detecto o mitigo? | Priorización y plan defensivo |
| 🟣 **Purple Team** | ¿Cómo convertimos este hallazgo en una mejora medible? | Corrección validada + aprendizaje compartido |

---

## 🗺️ Contenido del módulo

```text
03-analisis-vulnerabilidades/
├── README.md
├── teoria/
│   ├── 01-cia-triad-y-severidad.md
│   ├── 02-vulnerability-management-lifecycle.md
│   └── 03-red-blue-purple-operando-juntos.md
├── herramientas/
│   ├── nuclei.md
│   ├── openvas-gvm.md
│   └── searchsploit.md
├── laboratorio/
│   ├── README-lab.md
│   └── docker-compose.yml
└── portafolio/
    └── TEMPLATE-reporte-vulnerabilidades.md
```

---

## 🚀 Inicio rápido

```bash
# 1. Ir al módulo
cd 01-CIBERSEGURIDAD/03-analisis-vulnerabilidades/

# 2. Leer teoría base
cat teoria/01-cia-triad-y-severidad.md
cat teoria/02-vulnerability-management-lifecycle.md

# 3. Levantar el lab
cd laboratorio/
docker compose up -d

# 4. Descubrir servicios
nmap -sV -sC 172.31.0.0/24

# 5. Escaneo rápido con Nuclei
nuclei -u http://localhost:8082 -severity low,medium,high,critical
```

---

## 📈 Salida profesional del módulo

Al finalizar deberías ser capaz de entregar un documento con:
- Resumen ejecutivo.
- Inventario de activos revisados.
- Hallazgos ordenados por criticidad.
- Impacto sobre **C**, **I** y **A**.
- Evidencia del escaneo y de la validación técnica.
- Remediación priorizada por SLA.
- Observaciones separadas por Red, Blue y Purple Team.

---

## ⚖️ Aviso ético

> El análisis de vulnerabilidades es una actividad autorizada, controlada y documentada. La validación técnica debe realizarse solo contra activos propios, laboratorios locales o plataformas permitidas. Nunca uses scanners o validación ofensiva contra terceros sin permiso escrito.

---

**[⬆ Volver al inicio](../../README.md)** · **[📖 Leer teoría →](./teoria/01-cia-triad-y-severidad.md)** · **[🧪 Ir al lab →](./laboratorio/README-lab.md)**
