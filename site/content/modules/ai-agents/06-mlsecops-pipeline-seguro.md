---
title: MLSecOps Pipeline Seguro — Datos, Modelo, Despliegue y Operación
description: Pipeline completo de seguridad para sistemas LLM: desde la recolección de datos hasta la operación en producción con monitoreo continuo.
---

# 🔒 MLSecOps Pipeline Seguro

> **Nivel:** Intermedio → Avanzado · **Área:** AI Security
>
> Pipeline completo de seguridad para sistemas LLM: desde la recolección de datos hasta la operación en producción con monitoreo continuo y herramientas de red teaming automatizado.

[![Nivel](https://img.shields.io/badge/Nivel-Intermedio%20%E2%86%92%20Avanzado-orange?style=flat-square)]()
[![Marco](https://img.shields.io/badge/Marco-MLSecOps-red?style=flat-square)]()
[![Enfoque](https://img.shields.io/badge/Enfoque-DevSecOps-blue?style=flat-square)]()

---

## 📋 Resumen

| Atributo | Detalle |
|---|---|
| 🎯 **Resultado** | Diseñar e implementar un pipeline MLSecOps completo para LLMs |
| 🧪 **Práctica** | Configurar guardrails, red teaming automatizado y monitoreo |
| 🗂️ **Portafolio** | Diagrama de pipeline + suite de pruebas + configuración de monitoreo |
| 🔗 **Requiere** | `04-owasp-llm-top10-2025.md` + `05-prompt-injection-y-jailbreaks.md` |

---

## ⚖️ Aviso Ético

> **Este documento es puramente educativo.** Las herramientas y técnicas documentadas se presentan para fines de **defensa y evaluación de seguridad**. El uso malicioso de estas técnicas viola los términos de servicio de las plataformas y puede tener consecuencias legales.

---

## 1. ¿Qué es MLSecOps?

**MLSecOps** (Machine Learning Security Operations) es la disciplina que integra seguridad en todo el ciclo de vida de los sistemas de ML/LLM. Combina las prácticas de DevSecOps con consideraciones específicas de IA.

### Pilares de MLSecOps

```
┌─────────────────────────────────────────────────────────────┐
│                    MLSecOps Pipeline                         │
├─────────────┬─────────────┬─────────────┬─────────────────┤
│   DATOS     │   MODELO    │ DESPLIEGUE  │   OPERACIÓN     │
│             │             │             │                 │
│ • Validación│ • Evaluación│ • Guardrails│ • Monitoreo     │
│ • Limpieza  │ • Red team  │ • Filtros   │ • Alertas       │
│ • Auditoría │ • Hardening │ • Aislamiento│ • Respuesta    │
│ • Lineage   │ • Versionado│ • rollout   │ • Mejora continua│
└─────────────┴─────────────┴─────────────┴─────────────────┘
```

---

## 2. Fase 1: Datos

### 2.1 Validación de Datos de Entrenamiento

| Checkpoint | Descripción | Herramienta |
|------------|-------------|-------------|
| **Provenance** | Verificar origen de los datos | DVC, LakeFS |
| **Calidad** | Detectar datos corruptos o incompletos | Great Expectations |
| **Sesgos** | Identificar sesgos en el dataset | AI Fairness 360 |
| **Privacidad** | Eliminar PII y datos sensibles | Presidio, spaCy |
| ** Poisoning** | Detectar datos manipulados | Custom validators |

### 2.2 Checklist de Seguridad de Datos

```markdown
## Datos de Entrenamiento — Checklist

- [ ] Origen documentado y verificable
- [ ] PII eliminado o anonimizado
- [ ] Sesgos evaluados y documentados
- [ ] Licencias de uso verificadas
- [ ] Tamaño suficiente para el caso de uso
- [ ] Representatividad del dominio objetivo
- [ ] Versión controlada (DVC/Git LFS)
- [ ] Auditoría de calidad completada
```

### 2.3 Herramientas Recomendadas

| Herramienta | Caso de Uso | Licencia |
|-------------|-------------|----------|
| **DVC** | Versionado de datos | Apache 2.0 |
| **Great Expectations** | Validación de datos | Apache 2.0 |
| **Presidio** | Anonimización de PII | MIT |
| **AI Fairness 360** | Detección de sesgos | Apache 2.0 |

---

## 3. Fase 2: Modelo

### 3.1 Evaluación de Seguridad

| Checkpoint | Descripción | Herramienta |
|------------|-------------|-------------|
| **Robustez** | Resistencia a ataques adversariales | Garak, HarmBench |
| **Alighment** | Alineación con valores y políticas | Constitutional AI |
| **Privacidad** | No memorización de datos sensibles | Membership inference |
| **Calidad** | Métricas de rendimiento estándar | BLEU, ROUGE, human eval |

### 3.2 Red Teaming Automatizado

#### Garak (NVIDIA)

Framework de evaluación de LLMs que detecta vulnerabilidades automáticamente.

```bash
# Instalación
pip install garak

# Escaneo básico
garak --model_type openai --model_name gpt-3.5-turbo

# Escaneo específico
garak --model_type openai --model_name gpt-3.5-turbo \
  --probes promptinject --generations 3

# Reporte
garak --model_type openai --model_name gpt-3.5-turbo \
  --report_prefix garak_report
```

**Categorías de probes:**
- `promptinject` — Prompt injection
- `dan` — Do Anything Now
- `encoding` — Codificaciones evasivas
- `leak` — Extracción de información
- `misleading` — Información engañosa

#### PyRIT (Microsoft)

Herramienta de red teaming automatizado para LLMs.

```python
from pyrit.orchestrator import PromptSendingOrchestrator
from pyrit.prompt_target import OpenAIChatTarget

# Configurar target
target = OpenAIChatTarget(
    deployment_name="gpt-35-turbo",
    endpoint="https://your-openai.openai.azure.com/"
)

# Ejecutar red teaming
orchestrator = PromptSendingOrchestrator(
    prompt_target=target,
    attack_strategy="iterative"  # or "flip", "sequential"
)

# Resultados
results = orchestrator.get_results()
```

### 3.3 Hardening del Modelo

| Técnica | Descripción | Efectividad |
|---------|-------------|-------------|
| **System Prompt Hardening** | Instrucciones robustas del sistema | Alta |
| **RLHF adversarial** | Entrenamiento con datos adversariales | Alta |
| **Constitutional AI** | Principios éticos integrados | Media-Alta |
| **Fine-tuning defensivo** | Ajuste con ejemplos defensivos | Media |

### 3.4 Checklist de Seguridad del Modelo

```markdown
## Modelo — Checklist

- [ ] Evaluación con Garak/PyRIT completada
- [ ] Vulnerabilidades documentadas y priorizadas
- [ ] System prompt hardening implementado
- [ ] Guardrails configurados (input/output)
- [ ] Pruebas de alineación realizadas
- [ ] Benchmark de rendimiento establecido
- [ ] Versión del modelo documentada
- [ ] Rollback plan definido
```

---

## 4. Fase 3: Despliegue

### 4.1 Arquitectura de Guardrails

```
┌─────────────────────────────────────────────────────────────┐
│                    Pipeline de Despliegue                    │
├─────────────────────────────────────────────────────────────┤
│                                                             │
│  Usuario ──→ [Input Filter] ──→ [LLM] ──→ [Output Filter] ──→ Respuesta  │
│                  │                  │                  │              │
│                  ▼                  ▼                  ▼              │
│            Detección          System Prompt        Revisión         │
│            de patrones        robusto              de contenido     │
│            maliciosos                                                     │
│                  │                  │                  │              │
│                  ▼                  ▼                  ▼              │
│            [Logging]          [Policy Check]      [DLP Scan]        │
│                                                             │
└─────────────────────────────────────────────────────────────┘
```

### 4.2 Componentes del Pipeline

| Componente | Descripción | Herramienta |
|------------|-------------|-------------|
| **Input Filter** | Filtra prompts maliciosos antes del LLM | Guardrails AI, NeMo |
| **Output Filter** | Revisa la respuesta antes de entregarla | Custom validators |
| **Rate Limiting** | Limita solicitudes por usuario/IP | API Gateway |
| **Content Policy** | Políticas de contenido configurables | Custom rules |
| **Logging** | Registra todas las interacciones | ELK, Datadog |

### 4.3 Guardrails AI

```python
from guardrails import Guard

# Configurar guard
guard = Guard()

# Definir reglas
guard(
    prompt="""No reveles información sensible. 
    No ejecutes código malicioso.
    No generes contenido ofensivo.""",
    llm_api=OpenAIChat(),
)

# Usar en el pipeline
response = guard(
    user_input=user_prompt,
    llm_api=OpenAIChat(),
)
```

### 4.4 Checklist de Despliegue

```markdown
## Despliegue — Checklist

- [ ] Input filter configurado y probado
- [ ] Output filter configurado y probado
- [ ] Rate limiting implementado
- [ ] Content policy definida
- [ ] Logging habilitado
- [ ] Aislamiento de red configurado
- [ ] Secrets management implementado
- [ ] Rollback plan documentado
- [ ] Health checks configurados
- [ ] Auto-scaling con límites definidos
```

---

## 5. Fase 4: Operación

### 5.1 Monitoreo Continuo

| Métrica | Descripción | Umbral |
|---------|-------------|--------|
| **ASR** | Attack Success Rate | < 5% |
| **Refusal Rate** | Solicitudes legítimas rechazadas | < 10% |
| **Latency** | Tiempo de respuesta del filtro | < 200ms |
| **Error Rate** | Errores del sistema | < 1% |
| **Cost per Request** | Costo promedio por solicitud | Definir según presupuesto |

### 5.2 Alertas

```yaml
# Ejemplo de alertas
alerts:
  - name: "Alto ASR detectado"
    condition: "asr > 0.10"
    action: "Escalar a equipo de seguridad"
    
  - name: "Refusal rate elevado"
    condition: "refusal_rate > 0.15"
    action: "Revisar filtros de input"
    
  - name: "Latencia alta"
    condition: "latency_p99 > 500ms"
    action: "Revisar infraestructura"
    
  - name: "Costo excesivo"
    condition: "daily_cost > budget_limit"
    action: "Limitar solicitudes"
```

### 5.3 Respuesta a Incidentes

| Severidad | Descripción | Tiempo de Respuesta |
|-----------|-------------|---------------------|
| **Crítica** | Data breach, sistema comprometido | < 1 hora |
| **Alta** | Jailbreak exitoso, datos expuestos | < 4 horas |
| **Media** | Intento detectado, sin impacto | < 24 horas |
| **Baja** | Anomalía menor, sin impacto | < 72 horas |

### 5.4 Mejora Continua

```
┌─────────────────────────────────────────────────────────────┐
│                 Ciclo de Mejora Continua                     │
├─────────────────────────────────────────────────────────────┤
│                                                             │
│  Monitoreo ──→ Análisis ──→ Mejora ──→ Despliegue ──→ ... │
│      │              │            │              │          │
│      ▼              ▼            ▼              ▼          │
│  Métricas      Hallazgos    Guardrails    Validación      │
│  Alertas       Tendencias   Filtros       Testing         │
│  Logs          Root cause   Model tuning  Rollout         │
│                                                             │
└─────────────────────────────────────────────────────────────┘
```

---

## 6. GovLLM-Sentinel

### Integración con el Pipeline

**GovLLM-Sentinel** es un framework diseñado para evaluar y fortalecer modelos de lenguaje en entornos gubernamentales.

### Componentes

| Componente | Función |
|------------|---------|
| **Evaluator** | Ejecuta benchmarks de seguridad |
| **Hardener** | Aplica configuraciones de seguridad |
| **Dashboard** | Visualiza métricas de evaluación |
| **Reporter** | Genera informes de cumplimiento |

### Uso en el Pipeline

```
┌─────────────────────────────────────────────────────────────┐
│              GovLLM-Sentinel en el Pipeline                  │
├─────────────────────────────────────────────────────────────┤
│                                                             │
│  Fase 2 (Modelo) ──→ GovLLM-Sentinel Evaluator             │
│                          │                                  │
│                          ▼                                  │
│                    Benchmark de seguridad                   │
│                          │                                  │
│                          ▼                                  │
│                    GovLLM-Sentinel Hardener                 │
│                          │                                  │
│                          ▼                                  │
│                    Configuración segura                     │
│                          │                                  │
│                          ▼                                  │
│                    Fase 3 (Despliegue)                      │
│                                                             │
└─────────────────────────────────────────────────────────────┘
```

### Referencia
- **Repo:** `github.com/0xvanguard/GovLLM-Sentinel`
- **Dashboard:** Solo lectura para gobierno y comunidad

---

## 7. Diagrama Completo del Pipeline

```
┌─────────────────────────────────────────────────────────────────────────────┐
│                         MLSecOps Pipeline Completo                          │
├─────────────────────────────────────────────────────────────────────────────┤
│                                                                             │
│  ┌──────────┐    ┌──────────┐    ┌──────────┐    ┌──────────┐             │
│  │  DATOS   │───→│  MODELO  │───→│DESPLIEGUE│───→│OPERACIÓN │───→ ...     │
│  └──────────┘    └──────────┘    └──────────┘    └──────────┘             │
│       │               │               │               │                    │
│       ▼               ▼               ▼               ▼                    │
│  ┌──────────┐    ┌──────────┐    ┌──────────┐    ┌──────────┐             │
│  │Validación│    │Red Team  │    │Guardrails│    │Monitoreo │             │
│  │Calidad   │    │Garak     │    │Filtros   │    │Alertas   │             │
│  │Privacidad│    │PyRIT     │    │Rate Limit│    │Métricas  │             │
│  │Lineage   │    │Hardening │    │Logging   │    │Incidents │             │
│  └──────────┘    └──────────┘    └──────────┘    └──────────┘             │
│       │               │               │               │                    │
│       ▼               ▼               ▼               ▼                    │
│  ┌──────────────────────────────────────────────────────────────────┐     │
│  │                    GovLLM-Sentinel (评估)                         │     │
│  │  • Benchmark de seguridad    • Hardening automático              │     │
│  │  • Dashboard de métricas     • Reportes de cumplimiento         │     │
│  └──────────────────────────────────────────────────────────────────┘     │
│                                                                             │
└─────────────────────────────────────────────────────────────────────────────┘
```

---

## 8. Labs Relacionados

| Lab | Descripción | Fase del Pipeline |
|---|---|---|
| [`jailbreak-01.html`](../../../../docs/labs/jailbreak-01.html) | Evaluación de guardrails | Modelo + Despliegue |
| [`jailbreaking-education.html`](../../../../docs/jailbreaking-education.html) | Dashboard educativo | Referencia |

---

## 9. Herramientas del Pipeline

### Resumen

| Herramienta | Fase | Caso de Uso | Licencia |
|-------------|------|-------------|----------|
| **DVC** | Datos | Versionado | Apache 2.0 |
| **Great Expectations** | Datos | Validación | Apache 2.0 |
| **Presidio** | Datos | Anonimización PII | MIT |
| **Garak** | Modelo | Red teaming | Apache 2.0 |
| **PyRIT** | Modelo | Red teaming | MIT |
| **Guardrails AI** | Despliegue | Filtros | Apache 2.0 |
| **promptfoo** | Modelo/Despliegue | Testing | MIT |
| **GovLLM-Sentinel** | Modelo | Evaluación gubernamental | Propio |

---

## 10. Siguiente Paso

Tras estudiar este módulo, estás listo para:

👉 Implementar un **pipeline MLSecOps** en un proyecto real.

👉 Explorar roles como `../roles/ml-security-engineer/` y `../roles/ai-red-teamer/`.

👉 Usar **GovLLM-Sentinel** para evaluar modelos en entornos gubernamentales.

👉 Revisar la **Fase 4 del ROADMAP** para integrar estas prácticas en tu carrera.

---

**[⬅ Volver al área IA](../README.md)**
