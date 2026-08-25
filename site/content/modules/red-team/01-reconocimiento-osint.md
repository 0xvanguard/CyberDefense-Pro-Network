---
title: 01 — Reconocimiento OSINT (Clásico, sin IA)
description: 01 — Reconocimiento OSINT (Clásico, sin IA)
---

# 01 — Reconocimiento OSINT (Clásico, sin IA)

> **Objetivo del módulo:** Dominar las técnicas clásicas de reconocimiento y OSINT técnico para mapear la superficie de ataque de un objetivo, sin usar IA, de forma sistemática, legal y reproducible.

Este módulo es la **puerta de entrada práctica** a el Área 1. Aquí aprendes a descubrir **qué existe**, **dónde está** y **cómo se ve** un objetivo antes de pensar en explotar nada.

---

## 🎯 Objetivos de aprendizaje

Al completar este módulo deberías ser capaz de:

- Explicar la diferencia entre **OSINT general** y **reconocimiento técnico aplicado a pentesting**.
- Identificar el **scope autorizado** (dominios, rangos IP, assets en nube, subdominios).
- Usar herramientas clásicas (whois, dig, Nmap, etc.) para:
  - Resolver dominios, registrar DNS y obtener información de registros.
  - Descubrir hosts activos en un rango de red.
  - Enumerar puertos y servicios expuestos.
- Organizar tus hallazgos en un formato estructurado (tablas, notas, diagramas simples).
- Generar un **informe de reconocimiento** claro y reutilizable para siguientes fases del pentest.

---

## 📚 Teoría mínima

Este módulo asume que te concentras en **OSINT técnico y recon activo básico** sobre objetivos autorizados.

### OSINT vs Reconocimiento técnico

- **OSINT (Open Source Intelligence):**
  - Información obtenida de fuentes públicas: buscadores, redes sociales, registros públicos, leaks, etc.
  - Puede incluir datos humanos (personas, roles), de negocio y técnicos.

- **Reconocimiento técnico aplicado a pentesting:**
  - Se centra en la **superficie técnica**: dominios, subdominios, IPs, puertos, servicios, tecnologías visibles.
  - Incluye recon pasivo (sin tocar directamente al objetivo) y recon activo controlado (como Nmap) dentro del scope autorizado.

### Fases típicas de recon

1. **Definición de scope**
   - Qué dominios, subdominios, rangos de IP y aplicaciones están autorizados.
   - Qué está explícitamente fuera de alcance.

2. **Reconocimiento pasivo**
   - WHOIS, registros DNS, certificados (CRT), datos de OSINT general.
   - Sin enviar tráfico directo al objetivo (o lo mínimo posible).

3. **Descubrimiento de hosts**
   - Identificar qué IPs están activas dentro del rango autorizado.

4. **Enumeración de puertos y servicios**
   - Identificar qué puertos están abiertos y qué servicios parecen correr allí.

5. **Organización de hallazgos**
   - Tablas por host, servicio, versión y posibles vectores de ataque a investigar.

---

## 🗂 Estructura del módulo

```text
01-reconocimiento-osint/
├── teoria/
│   └── 01-fundamentos-osint.md   ← Conceptos base, metodología, fases
│
├── herramientas/
│   ├── whois/                    ← Uso básico + ejemplos
│   ├── dig-dns/                  ← Consultas DNS típicas
│   ├── nmap/                     ← Escaneos host discovery + puertos
│   └── otros/                    ← Otras herramientas de apoyo
│
├── tecnicas/
│   ├── 01-definir-scope.md          ← Cómo delimitar scope de forma profesional
│   ├── 02-recon-pasivo-dns-whois.md ← Procedimiento paso a paso
│   ├── 03-host-discovery-nmap.md    ← Descubrimiento de hosts
│   └── 04-enumeracion-puertos.md    ← Puertos/servicios básicos
│
├── laboratorios/
│   ├── lab-01-mapeo-superficie-basico/
│   │   ├── enunciado.md           ← Planteamiento del lab
│   │   ├── guia-paso-a-paso.md    ← Opcional, solo si se necesita apoyo
│   │   └── entregables.md         ← Qué debe producir el estudiante
│   └── (futuros labs...)
│
└── portafolio/
    └── TEMPLATE-informe-recon.md  ← Plantilla de informe de reconocimiento
```

> Todos los labs utilizarán una **empresa ficticia** y entornos controlados (rango de IPs de laboratorio, dominios simulados, etc.). Nunca se practicarán técnicas sobre objetivos reales sin autorización.

---

## 📂 Tipos de entregables del módulo

En este módulo se esperan entregables clásicos de recon, por ejemplo:

- **`informe-recon-inicial.md`**
  - Resumen del objetivo, scope, metodología y hallazgos clave.

- **Tablas de hosts y servicios**
  - Host/IP, puertos abiertos, servicios detectados, notas.

- **Notas técnicas de comandos**
  - Colección de comandos usados (whois, dig, Nmap) con comentarios.

- **Diagrama simple de superficie de ataque** (opcional)
  - Puede ser un esquema en texto o una imagen sencilla mostrando hosts y servicios principales.

Estos entregables se podrán luego enlazar desde `PORTAFOLIO.md` como evidencia de habilidades de reconocimiento.

---

## 🔗 Encaje del módulo en el área y la ruta

Dentro de el Área 1, este módulo es el **primer paso** de la ruta ofensiva:

1. `01-reconocimiento-osint/`  ← Este módulo (recon clásico)
2. `02-pentesting-red-team/`   ← Ciclo completo de pentest sobre labs
3. `03-analisis-vulnerabilidades/`
4. `04-explotacion-web/` y `05-post-explotacion/`
5. Otros módulos ofensivos (forense, ingeniería social, criptografía)

También alimenta directamente:

- Rutas de **Pentester / Red Team**.
- Rutas de **Analista SOC / Blue Team**, que necesitan entender qué se expone.
- Área 3, donde más adelante podrás automatizar parte de este recon con IA, pero sobre una base clásica sólida.

---

## ✅ Próximos pasos dentro de este módulo

Los siguientes pasos naturales serán:

- Crear `teoria/01-fundamentos-osint.md` con la teoría resumida que soporte estas prácticas.
- Definir el **Lab 01 — Mapeo de superficie básico** en `laboratorios/lab-01-mapeo-superficie-basico/`.
- Crear `portafolio/TEMPLATE-informe-recon.md` para unificar cómo presentas tus hallazgos.

Con eso, el módulo quedará listo para empezar a añadir ejercicios concretos y ejemplos de alta calidad para tu portafolio.
