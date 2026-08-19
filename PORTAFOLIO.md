# 🗂️ Portafolio — Guía para estudiantes

> Un portafolio no es un "extra" al final del curso: **es el producto principal de esta plataforma**. Cada módulo que completes debe generar evidencia pública que un reclutador pueda abrir, leer y verificar.

---

## ¿Por qué un portafolio y no solo un certificado?

Las empresas de ciberseguridad contratan por **evidencia de criterio**, no por papeles:

- Un certificado dice *"vi las diapositivas"*.
- Un portafolio dice *"encontré esto, lo expliqué así, lo remedié de esta forma"*.

En un mercado con millones de vacantes y candidatos que "completaron cursos", el portafolio es tu diferenciador. Además, en esta plataforma **el portafolio ES el sistema de evaluación**: si no hay evidencia publicada, el módulo no está completo.

---

## 📦 Qué debe contener tu portafolio

### 1. Tu perfil base (imprescindible)
- README personal en GitHub con: quién eres, tu enfoque (Red/Blue/DevSecOps/IA), stack y **3 proyectos destacados**.
- Perfil de LinkedIn sincronizado con tu GitHub.

### 2. Proyectos reales (3–5 mínimo)
Cada proyecto debe incluir:

| Elemento | Qué es | Ejemplo |
|---|---|---|
| **Contexto** | Qué problema resolviste y bajo qué alcance autorizado | "Pentest externo del lab NovaPay (10.20.30.0/24)" |
| **Metodología** | Qué marco seguiste | PTES · OWASP WSTG · MITRE ATT&CK |
| **Evidencia** | Capturas, comandos, logs, artefactos | Salida de nmap, request HTTP, hash crackeado |
| **Análisis** | Qué encontraste y por qué importa | CVSS, impacto, probabilidad |
| **Remediación** | Cómo se arregla | Config, parche, control compensatorio |
| **Lecciones** | Qué aprendiste y qué harías distinto | Reflexión honesta |

### 3. Tipos de entregables por módulo

| Módulo | Entregable sugerido |
|---|---|
| OSINT | [Informe de reconocimiento](01-CIBERSEGURIDAD/01-reconocimiento-osint/portafolio/TEMPLATE-reporte-osint.md) |
| Pentesting / Red Team | [Informe de pentest](01-CIBERSEGURIDAD/02-pentesting-red-team/portafolio/TEMPLATE-reporte-pentest.md) |
| SOC / Blue Team | [Ficha de evento SOC](03-blue-team-defensa/portafolio/TEMPLATE-ficha-evento-soc.md) |
| Automatización | Script o pipeline publicado en GitHub con README |
| DevSecOps | Pipeline CI/CD documentado (diagrama + repo) |
| IA / MLSecOps | Post educativo + repo de pruebas LLM + guía de pipeline |

---

## 🧱 Estructura recomendada para cada repositorio de proyecto

```text
mi-proyecto/
├── README.md            ← Contexto, alcance, resultados en 2 minutos
├── metodologia/         ← Marco usado y pasos seguidos
├── evidencias/          ← Capturas, logs, artefactos (anónimos)
├── informe/
│   ├── ejecutivo.pdf    ← Para gerentes (1 página)
│   └── tecnico.md       ← Para ingenieros (detallado)
└── remediacion/         ← Scripts, configs, recomendaciones
```

> ⚠️ **Anonimiza siempre**: usa seudónimos de empresa (NovaPay Labs), enmascara IPs reales y elimina datos personales. Un informe profesional nunca filtra información del cliente.

---

## ✍️ Cómo escribir un buen informe

1. **Empieza por el resumen ejecutivo**: qué se probó, qué se encontró, qué tan grave es, qué hacer primero.
2. **Sé específico**: "Puerto 445 expuesto con SMBv1 habilitado (CVSS 7.5)" > "hay vulnerabilidades".
3. **Muestra evidencia reproducible**: el lector debe poder verificar tu hallazgo.
4. **Separa hallazgos de opiniones**: usa CVSS para objetivar.
5. **Termina con remediación priorizada**: crítica → alta → media → baja.

---

## 📢 Cómo publicar y difundir

1. Sube cada proyecto a GitHub con README impecable (usa [`TEMPLATE-MODULO.md`](./TEMPLATE-MODULO.md) como referencia de calidad).
2. Añade un **post de LinkedIn** por entregable (con captura y resultado):
   > *"Completé el Módulo 02 de Pentesting de la Plataforma de Estudio de Ciberseguridad — aquí está mi primer reporte de prueba de penetración completo, desde reconocimiento hasta reporte ejecutivo. 7 fases PTES, CVSS scoring y remediaciones incluidas. #Pentesting #RedTeam #CyberSecurity #OpenToWork"*
3. Mantén tu README de GitHub con los **3 mejores proyectos** arriba.
4. Actualiza tu portafolio **cada vez que completes un módulo**, no al final.

---

## 🤖 Ejemplos de portafolio IA / MLSecOps

Como parte del módulo de MLSecOps y seguridad de LLM, se recomiendan estos entregables públicos:

1. **Post educativo**
   - Tema sugerido: "Qué es MLSecOps (y por qué importa a los juniors de ciberseguridad)".
   - Objetivo: demostrar que puedes explicar conceptos complejos en lenguaje claro.

2. **Repositorio de pruebas de seguridad LLM**
   - Contenido: casos de prueba documentados, resultados y, opcionalmente, scripts.
   - Objetivo: evidenciar que sabes diseñar y ejecutar pruebas contra modelos.

3. **Guía/diagrama de pipeline seguro con LLM**
   - Contenido: diagrama de arquitectura + descripción de controles por etapa.
   - Objetivo: mostrar que entiendes el ciclo de vida de sistemas con IA y dónde entra la seguridad.

Incorpora estos entregables a tu portafolio general y enlázalos desde tu README personal o perfil de LinkedIn.

---

## ✅ Checklist antes de publicar

- [ ] ¿El alcance está claro y es legal (lab propio o plataforma autorizada)?
- [ ] ¿Toda la información sensible está anonimizada?
- [ ] ¿Hay evidencia reproducible (comandos, capturas, artefactos)?
- [ ] ¿Los hallazgos tienen severidad (CVSS) y remediación?
- [ ] ¿El README se entiende en 2 minutos?
- [ ] ¿Está publicado en GitHub y difundido en LinkedIn?

---

*[← Volver al README](./README.md) · [🗺️ Ver Rutas](./RUTAS.md) · [📋 Ver Módulos](./MODULOS.md)*
