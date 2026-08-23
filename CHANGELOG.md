# Changelog

Todos los cambios notables en CyberDefense Pro Network.

El formato se basa en [Keep a Changelog](https://keepachangelog.com/es/1.0.0/),
y el proyecto adhiere a [Semantic Versioning](https://semver.org/lang/es/).

---

## [1.1.0] - 2026-08-23

### ✨ Added

#### Dashboard Educativo de Jailbreaking
- Nueva página `docs/jailbreaking-education.html` con dashboard interactivo completo
- 8 categorías de ataques documentadas: Role Play, Prompt Injection, Encoding, Multi-turn, Adversarial Suffix, Payload Splitting, Many-shot, Virtual Context
- Timeline de evolución de técnicas (2022-2025)
- Demo interactiva de pipeline de defensa en capas
- Referencia a frameworks de evaluación: HarmBench, JailbreakBench, promptfoo
- Métricas de evaluación: ASR, TCS, PSS, FPR, Refusal Rate, Latency
- Estrategias defensivas: System Prompt Hardening, Input/Output Filtering, Monitoring, Training
- OWASP LLM Top 10 (2025) con mapeo a prompt injection
- Integración de GovLLM-Sentinel para sector público
- Links a plataformas educativas: Gandalf, HackAPrompt, promptfoo

#### Laboratorio Interactivo
- Nuevo lab `docs/labs/jailbreak-01.html` con 10 ejercicios y 400 XP
- Score tracker en tiempo real con barra de progreso
- 6 preguntas con validación de respuestas
- 4 técnicas expandibles con ejemplos de ataque y defensa
- Checklists para cada ejercicio
- Prompt examples educativos (no maliciosos)
- Responsive para mobile

#### Módulo de Documentación
- Nuevo `site/content/modules/ai-agents/05-prompt-injection-y-jailbreaks.md` (372 líneas)
- Referencia profesional sobre prompt injection y jailbreaking
- 8 categorías de técnicas documentadas con defensas
- Frameworks de evaluación: HarmBench, JailbreakBench, promptfoo
- Métricas de evaluación detalladas
- 4 estrategias defensivas con implementación
- OWASP LLM Top 10 con tabla de relaciones
- Referencias académicas y plataformas educativas
- Conexión con labs y roles del proyecto

#### Catálogo de Labs
- Nueva sección "AI Security Labs" en `docs/labs.html`
- 2 labs de AI Security vinculados directamente
- Hero stats actualizado: "8+" → "10+" labs

### 🔧 Fixed
- Link roto a `ruta-ai-security/` corregido a `ruta-ai-security.html` en `jailbreaking-education.html`

### 📦 Built
- Campus site reconstruido con el nuevo módulo `05-prompt-injection-y-jailbreaks`
- 160+ archivos HTML regenerados en `docs/campus/`
- Sidebar links corregidos para clean URLs

### 📝 Documentation
- Nueva sesión documentada: `docs/sesiones/sesion-2026-08-23-jailbreaking-education.md`
- CHANGELOG creado

---

## [1.0.0] - 2026-08-21

### ✨ Added
- Plataforma completa de ciberseguridad en español
- 12 módulos de aprendizaje (Fundamentos, Red Team, Blue Team, Purple Team, AI Agents)
- Labs interactivos con Docker
- Herramientas profesionales documentadas
- Sistema de retos y gamificación
- Campus con VitePress
- Soporte multiidioma (10 idiomas)
- Roles profesionales con salarios

### 🔒 Security
- XSS sanitization en todas las páginas
- CSP headers configurados
- SRI en dependencias externas
- rel=noopener en links externos

---

*Este changelog se actualiza con cada release.*
