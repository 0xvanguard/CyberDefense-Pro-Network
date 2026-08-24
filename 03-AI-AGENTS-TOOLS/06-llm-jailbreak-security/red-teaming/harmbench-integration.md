# 🔗 Integración con GovLLM-Sentinel y HarmBench

> *Conecta tu framework de red teaming LLM con los estándares de la industria.*

---

## 📋 Resumen

| Componente | Función |
|------------|---------|
| **HarmBench** | Benchmark estándar para evaluar jailbreaks (510 behaviors, 18 métodos) |
| **GovLLM-Sentinel** | Tu framework personal de evaluación y hardening de LLMs |
| **Integración** | Pipeline automatizado: Red Team → Evaluación → Dashboard |

---

## 1. ¿Qué es HarmBench?

HarmBench es el benchmark de referencia para evaluar la seguridad de LLMs:

- **510 behaviors** categorizados en 7 categorías semánticas
- **18 métodos de ataque** (GCG, PAIR, TAP, Human Jailbreaks, etc.)
- **33 modelos evaluados** (GPT-4, Claude, Llama, Mistral, etc.)
- **Pipeline estándar:** test case generation → completion → classifier evaluation

### Categorías de HarmBench

| Categoría | Behaviors | Ejemplo |
|-----------|-----------|---------|
| **Cybercrime** | 50 | Network attacks, malware |
| **Chemical/Biological** | 50 | Dangerous substances |
| **Copyright** | 100 | Content reproduction |
| **Misinformation** | 50 | False information |
| **Harassment** | 50 | Targeted harassment |
| **Illegal Activities** | 100 | Criminal activities |
| **General Harm** | 110 | Physical, psychological |

---

## 2. Pipeline de Integración

```
┌─────────────────────────────────────────────────────────────┐
│              GOVLLM-SENTINEL + HARMbench PIPELINE            │
│                                                             │
│  1. SELECCIÓN DE TARGET                                      │
│     ├─ Modelo a evaluar (API o local)                       │
│     ├─ Configuración de rate limits                         │
│     └─ Budget de tokens                                     │
│                                                             │
│  2. GENERACIÓN DE TEST CASES                                │
│     ├─ Cargar behaviors de HarmBench                        │
│     ├─ Adaptar a tu caso de uso                             │
│     └─ Agregar tests custom                                │
│                                                             │
│  3. EJECUCIÓN DE ATAQUES                                    │
│     ├─ Seleccionar métodos (GCG, PAIR, etc.)               │
│     ├─ Ejecutar contra el modelo                           │
│     └─ Registrar respuestas                                │
│                                                             │
│  4. EVALUACIÓN                                              │
│     ├─ Classifier evaluation (Llama Guard, etc.)            │
│     ├─ Calcular ASR (Attack Success Rate)                  │
│     └─ Análisis por categoría                              │
│                                                             │
│  5. REPORTING                                               │
│     ├─ Dashboard en GovLLM-Sentinel                        │
│     ├─ Reporte ejecutivo                                   │
│     └─ Recomendaciones de hardening                        │
└─────────────────────────────────────────────────────────────┘
```

---

## 3. Scripts de Integración

### 3.1 Cargar Behaviors de HarmBench
```python
import json

def load_harmbench_behaviors(categories: list = None) -> list:
    """Carga behaviors de HarmBench desde el dataset oficial."""
    
    # Descargar dataset
    # https://github.com/centerforaisafety/HarmBench
    
    with open("harmbench_behaviors.jsonl") as f:
        behaviors = [json.loads(line) for line in f]
    
    if categories:
        behaviors = [b for b in behaviors if b["category"] in categories]
    
    return behaviors

# Ejemplo: solo cybercrime y misinformation
behaviors = load_harmbench_behaviors(["cybercrime", "misinformation"])
print(f"Loaded {len(behaviors)} behaviors")
```

### 3.2 Ejecutar Contra Modelo
```python
import time
from openai import OpenAI

client = OpenAI()

def evaluate_model(model_id: str, behaviors: list, method: str = "direct") -> dict:
    """Evalúa un modelo contra behaviors de HarmBench."""
    
    results = []
    
    for behavior in behaviors:
        prompt = generate_attack_prompt(behavior, method)
        
        start_time = time.time()
        response = client.chat.completions.create(
            model=model_id,
            messages=[{"role": "user", "content": prompt}],
            max_tokens=500
        )
        elapsed = time.time() - start_time
        
        result = {
            "behavior_id": behavior["id"],
            "category": behavior["category"],
            "prompt": prompt,
            "response": response.choices[0].message.content,
            "response_time": elapsed,
            "is_refused": check_refusal(response.choices[0].message.content),
        }
        results.append(result)
        
        # Rate limiting
        time.sleep(1)
    
    # Calcular métricas
    total = len(results)
    refused = sum(1 for r in results if r["is_refused"])
    asr = (total - refused) / total * 100
    
    return {
        "model": model_id,
        "method": method,
        "total_behaviors": total,
        "refused": refused,
        "asr": asr,
        "results": results
    }
```

### 3.3 Generar Reporte
```python
def generate_harmbench_report(evaluation: dict) -> str:
    """Genera reporte ejecutivo de HarmBench evaluation."""
    
    report = f"""
# HarmBench Evaluation Report

## Modelo: {evaluation['model']}
## Método: {evaluation['method']}
## Fecha: {datetime.now().isoformat()}

## Resumen
- Behaviors evaluados: {evaluation['total_behaviors']}
- Respuestas rechazadas: {evaluation['refused']}
- Attack Success Rate: {evaluation['asr']:.1f}%

## ASR por Categoría
"""
    
    # Agrupar por categoría
    categories = {}
    for r in evaluation["results"]:
        cat = r["category"]
        if cat not in categories:
            categories[cat] = {"total": 0, "refused": 0}
        categories[cat]["total"] += 1
        if r["is_refused"]:
            categories[cat]["refused"] += 1
    
    for cat, stats in categories.items():
        asr = (stats["total"] - stats["refused"]) / stats["total"] * 100
        report += f"- {cat}: {asr:.1f}% ASR ({stats['refused']}/{stats['total']} refused)\n"
    
    report += """
## Recomendaciones
1. Entrenar con adversarial training (R2D2)
2. Implementar guardrails multi-capa
3. Configurar monitoring en producción
4. Realizar red teaming periódico
"""
    
    return report
```

---

## 4. Métricas Clave de HarmBench

| Métrica | Descripción | Fórmula |
|---------|-------------|---------|
| **ASR** | Attack Success Rate | (ataques exitosos / total) × 100 |
| **Refusal Rate** | Tasa de rechazo | (rechazos / total) × 100 |
| **Latency** | Tiempo promedio de respuesta | Σ tiempos / total |
| **Category ASR** | ASR por categoría | ASR individual por tipo |

---

## 5. GovLLM-Sentinel Dashboard

Integra los resultados en tu dashboard existente:

```
┌─────────────────────────────────────────────────────────────┐
│                  GOVLLM-SENTINEL DASHBOARD                   │
│                                                             │
│  ┌──────────────┐  ┌──────────────┐  ┌──────────────┐     │
│  │ ASR Overall  │  │ Categories   │  │ Timeline     │     │
│  │    24.8%     │  │   Chart      │  │   Trend      │     │
│  └──────────────┘  └──────────────┘  └──────────────┘     │
│                                                             │
│  ┌──────────────┐  ┌──────────────┐  ┌──────────────┐     │
│  │ Model Compare│  │ Method Effic.│  │ Recommendations│    │
│  │   GPT vs     │  │  GCG vs PAIR │  │   Hardening   │    │
│  │   Claude     │  │  vs Direct   │  │   Actions     │    │
│  └──────────────┘  └──────────────┘  └──────────────┘     │
└─────────────────────────────────────────────────────────────┘
```

---

## 🔗 Referencias

- [HarmBench Repository](https://github.com/centerforaisafety/HarmBench)
- [HarmBench Paper](https://arxiv.org/abs/2402.04249)
- [GovLLM-Sentinel](https://github.com/0xvanguard/GovLLM-Sentinel)
- [Gray Swan AI](https://grayswan.ai/)

---

*Última actualización: Agosto 2026*
