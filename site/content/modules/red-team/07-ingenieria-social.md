---
title: 🎭 Módulo 07 — Ingeniería Social
description: 🎭 Módulo 07 — Ingeniería Social
---

# 🎭 Módulo 07 — Ingeniería Social

> **Nivel:** Intermedio · **Objetivo:** entender, simular y defender contra ataques de ingeniería social (phishing, pretexting, vishing) de forma ética y controlada.

[![Nivel](https://img.shields.io/badge/Nivel-Intermedio-orange?style=flat-square)]()
[![Enfoque](https://img.shields.io/badge/Enfoque-Red%20Team-red?style=flat-square)]()

---

## 📋 Resumen

| Atributo | Detalle |
|---|---|
| 🎯 **Resultado** | Diseñar y ejecutar campañas de ingeniería social con autorización |
| 🧪 **Práctica** | GoPhish, SET, Evilginx2, pretexting, vishing |
| 🗂️ **Portafolio** | Campaña documentada con análisis de resultados |
| 🔗 **Requiere** | [Módulo 02 — Pentesting / Red Team](../02-pentesting-red-team/) |

---

## 🎯 Objetivos de aprendizaje

Al completar este módulo deberías ser capaz:

- **Phishing:** crear campañas de phishing simulado con GoPhish y otras herramientas
- **Pretexting:** diseñar escenarios creíbles para obtener información o acceso
- **Vishing:** ejecutar ataques de ingeniería social por teléfono
- **Landing pages:** crear páginas falsas de login para capturar credenciales
- **Defensa:** implementar medidas técnicas y de proceso contra phishing
- **Ética:** entender y aplicar el marco ético de la ingeniería social

---

## 🗂️ Estructura del módulo

| Carpeta | Contenido | Estado |
|---|---|---|
| [`herramientas/`](./herramientas/) | GoPhish, SET, Evilginx2 y más | ✅ Completado |
| [`pretexting/`](./pretexting/) | Principios, pretextos y vishing | ✅ Completado |
| [`phishing/`](./phishing/) | Landing pages, campañas y defensa | ✅ Completado |

### 📚 Contenido detallado

#### 1. Herramientas

| Archivo | Contenido |
|---|---|
| [`01-gophish.md`](./herramientas/01-gophish.md) | Instalación, configuración y uso de GoPhish para campañas de phishing |
| [`02-set-toolkit.md`](./herramientas/02-set-toolkit.md) | Social Engineering Toolkit: credential harvester, website attacks, USB drops |
| [`03-herramientas-fishing.md`](./herramientas/03-herramientas-fishing.md) | King Phisher, Evilginx2, SocialFish, CredSniper y comparativa |

#### 2. Pretexting

| Archivo | Contenido |
|---|---|
| [`01-pretexting-principios.md`](./pretexting/01-pretexting-principios.md) | Principios psicológicos, fases, componentes y marco ético |
| [`02-pretextos-corporativos.md`](./pretexting/02-pretextos-corporativos.md) | Scripts y escenarios por departamento (TI, RRHH, Finanzas, Ventas) |
| [`03-vishing.md`](./pretexting/03-vishing.md) | Vishing: técnicas, scripts, herramientas y ejemplos reales |

#### 3. Phishing

| Archivo | Contenido |
|---|---|
| [`01-landings-phishing.md`](./phishing/01-landings-phishing.md) | Templates de landing pages (Google, Microsoft, LinkedIn) |
| [`02-configuracion-gophish.md`](./phishing/02-configuracion-gophish.md) | Configuración paso a paso de campañas en GoPhish |
| [`03-medidas-defensa.md`](./phishing/03-medidas-defensa.md) | Defensa técnica, de proceso y de persona contra phishing |

---

## 🛠️ Herramientas principales

| Herramienta | Uso principal |
|---|---|
| **GoPhish** | Campañas de phishing empresarial |
| **SET** | Phishing rápido, credential harvester, USB drops |
| **Evilginx2** | Bypass de MFA (Multi-Factor Authentication) |
| **King Phisher** | Campañas con análisis avanzado |
| **SocialFish** | Phishing de redes sociales |
| **CredSniper** | Captura de credenciales + MFA |

---

## ⚖️ Aviso ético

La ingeniería social **solo** se practica con:
- ✅ Autorización escrita explícita del responsable de seguridad
- ✅ Personal que ha consentido el ejercicio
- ✅ Entornos controlados y documentados
- ❌ Nada de suplantar identidades reales sin permiso
- ❌ Nada de atacar a terceros sin autorización
- ❌ Nada de usar la información para beneficio personal

---

## 🔗 Encaje del módulo en la ruta

Dentro de la **Ruta 2 (Red Team)**, este módulo complementa la **Fase B**:

1. `01-reconocimiento-osint/` ← Reconocimiento
2. `02-pentesting-red-team/` ← Ciclo de pentest
3. `03-analisis-vulnerabilidades/` ← Análisis
4. `04-explotacion-web/` ← Explotación
5. `05-post-explotacion/` ← Post-explotación
6. **`07-ingenieria-social/`** ← **Este módulo** (complemento)

---

## ✅ Checkpoint

¿Puedes hacer lo siguiente sin guía?

- [ ] Crear una campaña de phishing con GoPhish
- [ ] Diseñar un pretexto creíble para un departamento
- [ ] Ejecutar un vishing y obtener credenciales
- [ ] Crear una landing page que parezca legítima
- [ ] Explicar las medidas de defensa contra phishing
- [ ] Documentar una campaña con análisis de resultados

Si todo es ✅, estás listo para el siguiente paso: **[Módulo 08 — Criptografía](../08-criptografia/)**.

---

**[⬅ Volver a Ciberseguridad](../README.md)** · **[🗺️ Ver Rutas](../../RUTAS.md)**
