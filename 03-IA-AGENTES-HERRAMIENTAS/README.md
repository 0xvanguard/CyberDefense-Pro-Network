> 🚀 **¿Eres principiante?** Antes de este módulo, revisa la **[base común del repo](../fundamentos/)** (1 carpeta atrás). La seguridad de IA asume que ya entiendes vulnerabilidades, redes y herramientas generales.
>
> Elige tu ruta de aprendizaje: 🛡️ [Defensor](../fundamentos/rutas/ruta-defensor.md) · ⚔️ [Atacante](../fundamentos/rutas/ruta-atacante.md) · 🤖 [AI Security](../fundamentos/rutas/ruta-ai-security.md)

# 🤖 Área 3 — IA, Agentes y Automatización en Ciberseguridad

Bienvenido a la **Área de IA Aplicada a Seguridad**, donde se entrena el "cerebro adicional" de un Purple Team / DevSecOps moderno: agentes, automatización y seguridad de modelos de lenguaje.

Aquí no solo aprendes a usar IA como usuario final; aprendes a **diseñar agentes, pipelines y automatizaciones** que apoyan ofensiva, defensa y gobernanza.

---

## 🎯 Objetivo de el área

Formarte para que seas capaz de:

- Diseñar y usar **agentes de IA** para OSINT, pentesting y respuesta a incidentes.
- Evaluar y reforzar la **seguridad de LLM** (prompt injection, exfiltración, jailbreaks, etc.).
- Construir **automatizaciones en Python** que conecten herramientas de seguridad con modelos de IA.
- Entender los **roles emergentes** alrededor de IA en ciberseguridad (MLSecOps, AI Incident Responder, AI Governance, etc.) y qué portafolio necesitas para cada uno.

Esta área está pensada como complemento natural a tu perfil de **Purple Team Engineer + DevSecOps**.

---

## 🧱 Módulos principales

Los módulos se numeran para sugerir un orden, pero puedes saltar según tu nivel.

### 01️⃣ Agentes OSINT

Ruta de entrada para usar IA en recolección y análisis de información pública.

- **Nivel sugerido:** Entry → Intermedio
- **Enfoque:**
  - Diseñar flujos donde un agente ayude con OSINT (pero tú controlas fuentes y criterios).
  - Generar reportes limpios sin filtrar, respetando límites éticos y legales.
- **Entregables típicos:**
  - Prompt pack para agente OSINT.
  - Informe OSINT asistido por IA con metodología clara.

Carpeta: `./01-agentes-osint/`

---

### 02️⃣ Agentes para Pentest

Uso de IA para apoyar fases del pentesting / Red Team (sin reemplazar el criterio humano).

- **Nivel sugerido:** Intermedio
- **Enfoque:**
  - Apoyo en reconocimiento, análisis de resultados de escáneres, generación de payload ideas.
  - Uso responsable: IA como copiloto, nunca como auto-hacker.
- **Entregables típicos:**
  - Colección de prompts para fases de pentest.
  - Mini-playbook donde IA ayuda a priorizar findings.

Carpeta: `./02-agentes-pentest/`

---

### 03️⃣ Seguridad LLM y MLSecOps

Especialización en **seguridad de modelos de lenguaje** y en cómo se integran en pipelines reales.

- **Nivel sugerido:** Entry → Avanzado
- **Enfoque por niveles:**
  - Entry: fundamentos de IA, riesgos básicos y qué es MLSecOps.
  - Intermedio: diseño de pruebas de seguridad para LLM (prompt injection, exfiltración, jailbreaks controlados).
  - Avanzado: diseño de pipelines MLSecOps con controles en datos, modelo, despliegue y operación.
- **Entregables típicos:**
  - Post educativo sobre MLSecOps.
  - Repo con suite de pruebas de seguridad para LLM.
  - Diagrama/guía de pipeline MLSecOps.

Carpetas:
- `./03-llm-security/`
- `./03-mlsecops-llm-security/`

---

### 04️⃣ Herramientas IA «trending» para seguridad

Análisis y curaduría de herramientas IA nuevas que pueden apoyar tareas de seguridad.

- **Nivel sugerido:** Entry → Intermedio
- **Enfoque:**
  - Evaluar herramientas, no solo listarlas.
  - Documentar casos de uso concretos y riesgos de uso.
- **Entregables típicos:**
  - Fichas de herramientas con pros/contr as.
  - Scripts o flujos de ejemplo donde se integran.

Carpeta: `./04-herramientas-trending/`

---

### 05️⃣ Automatización con Python + IA

Conecta scripts de seguridad con modelos de lenguaje para crear **pipelines realmente útiles**.

- **Nivel sugerido:** Intermedio → Avanzado
- **Enfoque:**
  - Automatizar tareas repetitivas (parsing de logs, normalización de findings, generación de reportes iniciales).
  - Diseñar mini-servicios o herramientas CLI que llamen a APIs de IA.
- **Entregables típicos:**
  - Script Python documentado que automatice una tarea de seguridad usando IA.
  - CLI o pequeño servicio que otros pueden reutilizar.

Carpeta: `./05-automatizacion-python/`

---

## 🧩 Roles emergentes en IA + Ciberseguridad

Además de los módulos técnicos, esta área incluye una sección de **roles y trayectorias profesionales** relacionados con IA en seguridad.

Cada rol tiene su propia carpeta dentro de `./roles/` con:
- Descripción del rol.
- Skillset técnico recomendado.
- Módulos de esta plataforma que mejor lo alimentan.
- Lista de proyectos/entregables recomendados para tu portafolio.

Roles incluidos (por ahora):

- `agentic-security-developer/`
- `ai-governance-officer/`
- `ai-incident-responder/`
- `ai-red-teamer/`
- `ai-supply-chain-security/`
- `ml-security-engineer/`
- `prompt-engineer-security/`

Carpeta: `./roles/`

---

## 📦 Estructura de esta área

```text
03-IA-AGENTES-HERRAMIENTAS/
│
├── README.md                       ← Esta guía
├── 01-agentes-osint/               ← Módulo 1: Agentes para OSINT
├── 02-agentes-pentest/             ← Módulo 2: Agentes para Pentest
├── 03-llm-security/                ← Módulo 3A: Seguridad básica de LLM
├── 03-mlsecops-llm-security/       ← Módulo 3B: MLSecOps avanzado
├── 04-herramientas-trending/       ← Módulo 4: Herramientas IA trending
├── 05-automatizacion-python/       ← Módulo 5: Automatización con Python + IA
└── roles/                          ← Perfiles profesionales en IA + Ciberseguridad
    ├── agentic-security-developer/
    ├── ai-governance-officer/
    ├── ai-incident-responder/
    ├── ai-red-teamer/
    ├── ai-supply-chain-security/
    ├── ml-security-engineer/
    └── prompt-engineer-security/
```

---

## 🧪 Cómo trabajar cada módulo

Todos los módulos de esta área deben seguir el formato de `TEMPLATE-MODULO.md` desde la raíz del repositorio:

1. **Objetivos claros** (qué sabrás hacer cuando termines).
2. **Teoría mínima** necesaria para no memorizar, sino entender.
3. **Práctica guiada** (laboratorio, reto o mini-proyecto).
4. **Entregable de portafolio** (repo, script, post, informe, pipeline, etc.).
5. **Siguiente paso sugerido** para seguir creciendo en la plataforma.

Cuando edites o crees un módulo dentro de esta área, copia el `TEMPLATE-MODULO.md` a su carpeta y adáptalo.

---

## 🔗 Relación con otras áreaes

Esta área se conecta directamente con:

- `01-CIBERSEGURIDAD/` → Apoya con agentes OSINT y pentest.
- `02-SEGURIDAD-INFORMACION/` → Apoya con automatización, detección y respuesta.
- `04-LABORATORIOS/` → Muchos labs pueden tener una variante "con IA" además de la manual.

La idea es que **no te conviertas en "solo prompt engineer"**, sino en alguien que entiende ofensiva, defensiva, automatización y puede usar IA como acelerador.

---

## 🚀 Siguiente paso recomendado

Si estás empezando en esta área:

1. Lee el `README.md` de `01-agentes-osint/`.
2. Completa la práctica básica de un agente OSINT asistido por IA.
3. Publica tu primer entregable (por ejemplo, un reporte OSINT documentado) y enlázalo en tu portafolio.
4. Luego pasa a `02-agentes-pentest/` o a `03-llm-security/` según tus intereses.
