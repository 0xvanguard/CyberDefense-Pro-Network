---
title: "Phishing: cómo detectar y prevenir el ataque más efectivo"
description: "Tipos de phishing, técnicas de detección y herramientas de protección"
author: Equipo CDPN
date: 2026-08-03
tags: [phishing, ingenieria-social, seguridad, prevencion]
readingTime: 5 min
---

<script setup>
import { useData } from 'vitepress'
const { frontmatter } = useData()
</script>

<style>
.article-meta { display:flex; gap:0.8rem; flex-wrap:wrap; margin:0.8rem 0 1.5rem; font-size:0.85rem; color:var(--vp-c-text-3); }
.article-meta span { background:var(--vp-c-default-soft); padding:2px 10px; border-radius:6px; }
.article-meta .accent { background:var(--vp-c-brand-soft); color:var(--vp-c-brand-1); }
</style>

# Phishing: cómo detectar y prevenir el ataque más efectivo

<div class="article-meta">
  <span class="accent">📝 Equipo CDPN</span>
  <span>📅 3 Agosto 2026</span>
  <span>📖 5 min de lectura</span>
  <span>🏷️ Phishing</span>
  <span>🏷️ Ingeniería Social</span>
</div>

## ¿Qué es el Phishing?

**Phishing** es una técnica de ingeniería social donde el atacante se hace pasar por una entidad confiable para engañar a la víctima y robar información sensible (credenciales, datos bancarios, etc.).

### Datos que asustan

| Dato | Cifra |
|------|-------|
| Ataques de phishing en 2025 | **3.4 mil millones/día** |
| Empresas víctimas de phishing | **74%** |
| Coste promedio de un breach por phishing | **$4.9 millones** |
| Phishing como vector de breach | **16% de todos los breaches** |

## Tipos de phishing

### 1. Email Phishing (el clásico)
```
De: soporte@banco-seguro.com (dominio falso)
Asunto: ⚠️ Tu cuenta ha sido comprometida
Body: Haz clic aquí para verificar tu identidad
→ Te lleva a una web falsa que roba tus credenciales
```

### 2. Spear Phishing (dirigido)
- El atacante **investiga a la víctima** (LinkedIn, redes sociales)
- Personaliza el mensaje con datos reales (nombre, empresa, cargo)
- **Tasa de éxito: 10x mayor** que el phishing genérico

### 3. Whaling (objetivos de alto valor)
- Dirigido a **C-levels** (CEO, CFO, CISO)
- Suele suplantar a un abogado, socio o regulador
- Incluye documentos oficiales falsos

### 4. Smishing / Vishing
- **Smishing** — Phishing vía SMS
- **Vishing** — Phishing vía teléfono (voice)
- Ejemplo: "Su paquete tiene un problema, pulse 1 para hablar con un agente"

### 5. Clone Phishing
- Copia exacta de un email legítimo que la víctima recibió
- Reemplaza el enlace/adjunto con uno malicioso
- Muy difícil de detectar a simple vista

## Cómo detectar phishing

### Checklist de seguridad

```
☐ El remitente es exactamente quién dice ser?
   → soporte@google.com ≠ soporte@g00gle.com
☐ El enlace apunta al dominio correcto?
   → Pasa el cursor por encima, NO hagas clic
☐ Hay urgencia artificial?
   → "Tu cuenta será cerrada en 24 horas"
☐ Errores ortográficos o gramaticales?
   → Empresas reales revisan sus emails
☐ Te piden datos sensibles por email?
   → Ninguna empresa legítima hace esto
☐ El email usa attachments inusuales?
   → .html, .js, .zip sospechosos
```

### Verificar el dominio

```bash
# Verificar dominio real detrás de un enlace
# 1. No hagas clic — copia el enlace
# 2. Usa un URL analyzer

# Herramientas gratuitas:
# - urlscan.io — Análisis completo
# - virustotal.com — Verificación de malware
# - phishtank.com — Base de datos de phishing
```

### Analizar headers del email

```bash
# En Gmail: Ver original del email
# Busca: "Received:" headers
# El primer "Received:" es el servidor real que envió el email

# Ejemplo de header falso:
# Received: from mail.banco.com (192.168.1.1)  ← SERVIDOR REAL
# Received: from mx.banco-seguro.com             ← DOMINIO FALSO
```

## Herramientas anti-phishing

| Herramienta | Tipo | Uso |
|-------------|------|-----|
| **Pi-hole** | DNS Filtering | Bloquear dominios maliciosos |
| **uBlock Origin** | Browser extension | Bloquear popups y redirects |
| **PhishTool** | Análisis de emails | Análisis automático de phishing |
| **GoPhish** | Simulación | Enviar campañas de phishing simulado |
| **DMARC/DKIM/SPF** | Email auth | Verificar autenticidad de emails |

## Prevención para organizaciones

### 1. Capacitación continua
- Simulacros de phishing trimestrales
- Consequences para quienes fallan repetidamente
- Gamificación: recompensar a quienes detectan phishing

### 2. Autenticación de email
```
# Configurar DMARC, DKIM y SPF en tu dominio
# Esto impide que otros envíen emails como tú

# SPF: "Solo estos servidores pueden enviar emails por mi dominio"
# DKIM: "Los emails legítimos tienen esta firma digital"
# DMARC: "Si no pasa SPF/DKIM, rechaza o pone en cuarentena"
```

### 3. Zero Trust para email
- **Nunca confíes** en un email solo porque parece legítimo
- **Verifica siempre** por un canal separado (llamada, Slack)
- **No hagas clic** en enlaces — navega directamente al sitio

## Conclusión

El phishing funciona porque **explota la confianza y la urgencia**, no vulnerabilities técnicas. La mejor defensa es **educación + verificación constante**.

---

*Artículo publicado en el Blog CDPN — Semana 10*
