# 🌐 Módulo 04 — Explotación Web y Remediación (SQLi · XSS · IDOR)

> **Objetivo principal:** Explorar y explotar de forma controlada tres vulnerabilidades web críticas (**SQL Injection, Cross-Site Scripting y IDOR**) y luego aplicar controles defensivos (hardening, headers, reglas básicas tipo WAF) y re-testear como Purple Team.

[![Nivel](https://img.shields.io/badge/Nivel-Intermedio%20%E2%86%92%20Avanzado-red?style=flat-square)]()
[![Enfoque](https://img.shields.io/badge/Enfoque-Red%20%7C%20Blue%20%7C%20Purple-purple?style=flat-square)]()
[![Vulns](https://img.shields.io/badge/Vulns-SQLi%20%7C%20XSS%20%7C%20IDOR-orange?style=flat-square)]()
[![Lab Docker](https://img.shields.io/badge/Lab-DVWA%20%7C%20WebGoat%20%7C%20Juice%20Shop-blue?style=flat-square)](./laboratorio/)
[![Portafolio](https://img.shields.io/badge/Entregables-Writeups%20%2B%20Hardening-green?style=flat-square)](./portafolio/)

---

## 📋 Resumen del módulo

| Atributo | Detalle |
|---|---|
| 🏷️ **Nivel** | Intermedio → Avanzado |
| ⏱️ **Duración estimada** | 4–8 semanas (según profundidad) |
| 🎯 **Resultado esperado** | Ser capaz de explotar SQLi, XSS e IDOR en entornos de laboratorio, diseñar mitigaciones básicas y documentar todo el ciclo Red/Blue/Purple |
| 🧪 **Práctica verificable** | Laboratorios guiados sobre DVWA, WebGoat y Juice Shop + ejercicios de hardening |
| 🗂️ **Portafolio** | Writeups de explotación (Red) y change-log de hardening (Blue/Purple) |
| 🔗 **Requiere** | [Módulo 02 — Pentesting / Red Team](../02-pentesting-red-team/) · [Módulo 03 — Análisis de Vulnerabilidades](../03-analisis-vulnerabilidades/) |
| 🔗 **Conduce a** | Módulos de explotación avanzada, AppSec y DevSecOps |

---

## 🎯 Qué aprenderás

- [ ] Identificar puntos de entrada típicos para **SQL Injection**.
- [ ] Explorar diferentes sabores de **XSS** (reflejado y almacenado).
- [ ] Entender y explotar **IDOR / Broken Access Control**.
- [ ] Conectar cada vuln con impacto en la tríada **CIA**.
- [ ] Probar mitigaciones: sanitización, parametrización, controles de acceso, headers de seguridad y reglas básicas tipo WAF/proxy.
- [ ] Escribir writeups ofensivos y registros de cambio defensivos reutilizables en tu portafolio.

---

## 🧭 Tres vulnerabilidades, tres perspectivas

| Vuln | Red Team | Blue Team | Purple Team |
|---|---|---|---|
| **SQL Injection** | Demostrar extracción o manipulación de datos | Revisar queries, parametrización, roles, logging | Diseñar y verificar re-test automático |
| **XSS** | Ejecutar payloads en el navegador víctima | Revisar sanitización, CSP, encoding, input validation | Crear casos de prueba recurrentes |
| **IDOR** | Acceder a recursos ajenos cambiando IDs | Revisar lógica de autorización y controles por recurso | Alinear reglas, logs y tests automáticos |

---

## 🗺️ Estructura del módulo

```text
04-explotacion-web/
├── README.md
├── teoria/
│   ├── 01-owasp-top10-contexto.md
│   ├── 02-flujo-explotacion-responsable.md
│   └── 03-patrones-hardening-web.md
├── explotacion/
│   ├── sqli-dvwa.md
│   ├── xss-dvwa-juice-shop.md
│   └── idor-webgoat-juice-shop.md
├── defensa/
│   ├── headers-seguridad-nginx.md
│   ├── reverse-proxy-nginx-ejemplo.conf
│   └── checklist-hardening-web.md
├── laboratorio/
│   ├── README-lab.md
│   └── docker-compose.yml
└── portafolio/
    ├── TEMPLATE-writeup-exploit.md
    └── TEMPLATE-hardening-change-log.md
```

---

## 🚀 Inicio rápido

```bash
# 1. Ir al módulo
cd 01-CIBERSEGURIDAD/04-explotacion-web/

# 2. Leer contexto
cat teoria/01-owasp-top10-contexto.md
cat teoria/02-flujo-explotacion-responsable.md

# 3. Levantar el lab
cd laboratorio/
docker compose up -d

# 4. Practicar una vuln (ejemplo SQLi DVWA)
cd ../explotacion/
cat sqli-dvwa.md
```

---

## 📈 Salida profesional del módulo

Al terminar deberías poder mostrar en tu portafolio:
- Writeups claros de al menos **1 SQLi, 1 XSS y 1 IDOR** en laboratorio.
- Un `reverse-proxy` de ejemplo con headers y ajustes de hardening documentados.
- Un change-log defensivo donde expliques cómo mitigaste lo que explotaste.

---

## ⚖️ Aviso ético

> Todo lo que practiques en este módulo debe permanecer dentro de laboratorios, entornos controlados o plataformas donde tengas autorización explícita. Nunca ejecutes payloads ni pruebas de explotación sobre sistemas de terceros sin permiso formal.

---

**[⬆ Volver al índice](../../README.md)** · **[📖 Teoría](./teoria/01-owasp-top10-contexto.md)** · **[🧪 Lab](./laboratorio/README-lab.md)**
