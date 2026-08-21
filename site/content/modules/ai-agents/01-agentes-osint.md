---
title: 01 – Agentes OSINT para Empresa Ficticia
description: 01 – Agentes OSINT para Empresa Ficticia
---

# 01 – Agentes OSINT para Empresa Ficticia

> **Objetivo Principal:** Al finalizar este módulo podrás usar agentes de IA y herramientas OSINT para perfilar una **empresa ficticia vulnerable**, desde nivel principiante hasta avanzado, y generar un informe profesional para tu portafolio.

La empresa objetivo será siempre **ficticia** (por ejemplo, `acmebank-testing.com` o similar). Nunca se realizarán actividades sobre empresas reales sin autorización.

---

## 1. Teoría Mínima Viable (TMV)

- **¿Qué es OSINT?**
  OSINT (Open Source Intelligence) es la recolección y análisis de información a partir de fuentes públicas y abiertas (internet, redes sociales, registros públicos, etc.), sin vulnerar sistemas ni romper la ley.

- **Empresa objetivo ficticia:**
  Trabajaremos con una empresa inventada ("AcmeBank Testing") con dominios, servicios y perfiles simulados, de forma que puedas practicar sin riesgos legales.

- **Superficie de ataque vista desde OSINT:**
  Todo lo que un atacante puede aprender de una organización sin enviar un solo paquete malicioso: dominios, subdominios, stack tecnológico visible, errores de exposición de información, huella en redes.

- **IA como copiloto, no como atacante:**
  Los modelos (Perplexity, Claude, etc.) se usan para estructurar búsquedas, interpretar datos y mejorar informes, pero **no sustituyen** tu criterio ni ejecutan acciones por ti.

- **Límites legales y éticos básicos:**
  - Solo se usa información pública.
  - No se intenta explotar vulnerabilidades, solo identificarlas a nivel teórico.
  - Nada de fuzzing agresivo, DoS, fuerza bruta, ni acceso a datos privados.

---

## 2. Herramientas del Oficio

| Herramienta              | Caso de Uso Principal                                      |
|--------------------------|------------------------------------------------------------|
| Perplexity / Claude      | Diseñar estrategias de búsqueda, resumir resultados, redactar informes |
| Navegador web            | Navegar sitio principal de la empresa ficticia             |
| `whois` / servicios WHOIS| Información de registro de dominio                         |
| `nslookup` / `dig`       | Resolución DNS básica (IP, registros)                      |
| Buscadores (Google, etc.)| Búsqueda de subdominios, perfiles, noticias                |
| Herramientas tipo BuiltWith / Wappalyzer | Identificar tecnologías visibles (CMS, servidor, etc.) |

No necesitas usar todas desde el primer día; se proponen por niveles.

---

## 3. Práctica Guiada (Laboratorio)

### Prerrequisitos

- [ ] Tener un navegador web.
- [ ] Tener acceso a una terminal (Linux, WSL o similar) para usar `whois`, `nslookup` o herramientas equivalentes online.
- [ ] Tener una cuenta en al menos un modelo IA (Perplexity, Claude, etc.).

La empresa ficticia la llamaremos **AcmeBank Testing** (`acmebank-testing.com`) o nombre similar que tú definas en tu informe.

---

### Nivel 1 — Principiante: Perfil básico de la empresa

1. **Definir el escenario con IA:**
   - Pide a tu modelo IA que te ayude a definir un contexto ficticio para "AcmeBank Testing" (qué tipo de banco es, en qué país opera, qué servicios ofrece). Aclara que es un ejercicio educativo.

2. **Identificar presencia pública mínima:**
   - Supón que existe `https://www.acmebank-testing.com` (no hace falta que exista de verdad para el ejercicio de documentación).
   - Escribe qué secciones tendría su web pública (home, login, blog, soporte, etc.).

3. **Recoger datos básicos simulados:**
   - Nombre de la empresa.
   - País y ciudad sede.
   - Sector (banca, fintech, etc.).
   - Servicios principales.

4. **Documentar en una tabla:**
   - Crea una tabla simple en Markdown con estos campos y rellénala con lo que definiste.

**Mini-entregable nivel 1:** sección "Perfil básico" de tu informe OSINT.

---

### Nivel 2 — Intermedio: Huella técnica inicial

1. **Dominios y subdominios (simulados):**
   - Imagina posibles subdominios: `app.acmebank-testing.com`, `api.acmebank-testing.com`, `support.acmebank-testing.com`, etc.
   - Usa IA para que te sugiera subdominios típicos en bancos/fintech (solo a nivel teórico).

2. **Stack tecnológico visible (simulado):**
   - Usando BuiltWith/Wappalyzer sobre cualquier sitio similar (no ataques, solo análisis público), observa qué tipo de tecnologías salen (ej: Nginx, Cloudflare, React, etc.).
   - Traslada esa idea a tu empresa ficticia (ej: "AcmeBank Testing probablemente usa un frontend React y un backend en Node detrás de un Nginx").

3. **Mapa técnico inicial:**
   - Define:
     - Qué dominios/subdominios conoces.
     - Qué tecnologías supones (frontend/backend/infraestructura básica).
     - Qué servicios públicos tendría (web principal, API pública, panel de clientes, etc.).

4. **Documentar en tu informe:**
   - Añade una sección "Mapa técnico inicial" con texto y, si quieres, un pequeño diagrama.

**Mini-entregable nivel 2:** sección "Mapa técnico inicial" de tu informe OSINT.

---

### Nivel 3 — Avanzado: Análisis de riesgos OSINT

1. **Identificar posibles riesgos OSINT:**
   - Pide a la IA que te liste riesgos típicos basados en huella OSINT para bancos/fintech (ej: exposición de paneles admin, leaks en repos públicos, phishing, etc.).
   - Elige de 3 a 5 riesgos que tengan sentido en el contexto que tú definiste para AcmeBank Testing.

2. **Analizar impacto:**
   - Para cada riesgo elegido, responde:
     - ¿Qué podría pasar si un atacante lo explota?
     - ¿Qué tipo de datos o sistemas se verían afectados?

3. **Proponer contramedidas (vista Purple Team):**
   - Para cada riesgo, describe al menos una medida de mitigación (hardening, controles, monitoreo, capacitación, etc.).

4. **Redactar informe ejecutivo + técnico ayudado por IA:**
   - Pide a tu modelo IA que te ayude a estructurar el informe en:
     - Resumen ejecutivo (no técnico, para directivos).
     - Detalle técnico (para equipo de seguridad).
   - Revisa y corrige el texto: tú tienes la última palabra.

**Mini-entregable nivel 3:** sección "Análisis de riesgos OSINT" con hallazgos y contramedidas.

---

## 4. Evidencia y Portafolio

- **Reto final:**
  Arma un **informe único** llamado por ejemplo `informe-osint-acmebank-testing.md` donde unas los tres niveles:
  - Perfil básico de la empresa.
  - Mapa técnico inicial.
  - Análisis de riesgos OSINT con contramedidas.

- **Entregable:**
  - El archivo Markdown (o PDF generado desde él) con tu informe completo.
  - Opcional: un post corto en LinkedIn/Medium resumiendo el ejercicio (sin mencionar empresas reales).

- **Para tu Portafolio:**
  - Sube el informe a un repositorio público (por ejemplo, una carpeta `osint-labs/empresa-ficticia-acmebank-testing/`).
  - Incluye una breve descripción en tu `PORTAFOLIO.md` dentro de esta plataforma.

---

## 5. Siguiente Paso

Una vez domines este módulo, tienes dos caminos naturales:

👉 **Ofensiva asistida por IA:**
   Continúa con `../02-agentes-pentest/` para ver cómo un agente puede ayudarte a organizar fases de pentest (reconocimiento, análisis de findings, priorización), siempre manteniendo la ética profesional.

👉 **Seguridad de LLM:**
   Si te interesa más la parte de IA, salta a `../03-llm-security/` para entender riesgos y pruebas de seguridad específicos de modelos de lenguaje.
