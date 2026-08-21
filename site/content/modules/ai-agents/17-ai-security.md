---
title: "17 — AI Security"
description: "17 — AI Security"
---

# 17 — AI Security

> 🎯 **Objetivo:** dominar la seguridad de sistemas de IA: cómo proteger modelos de machine learning, detectar ataques adversariales y asegurar la privacidad en sistemas de IA.

## 1. Fundamentos de AI Security

### 1.1 ¿Qué es AI Security?

AI Security es el conjunto de técnicas para proteger sistemas de inteligencia artificial contra ataques, garantizar su privacidad y mantener su integridad.

```
┌─────────────────────────────────────────────────────────┐
│               AMENAZAS A SISTEMAS DE IA                 │
├─────────────────────────────────────────────────────────┤
│                                                         │
│  DATA POISONING         ADVERSARIAL EXAMPLES           │
│  ├── Envenenar datos    ├── Perturbaciones sutiles     │
│  ├── Backdoor attacks   ├── Evasion de detección       │
│  └── Label flipping     └── Model fooling              │
│                                                         │
│  MODEL STEALING         PRIVACY LEAKAGE                │
│  ├── Model extraction   ├── Membership inference       │
│  ├── Function stealing  ├── Model inversion            │
│  └── API abuse          └── Training data extraction   │
│                                                         │
│  INFERENCE ATTACKS       DENIAL OF SERVICE              │
│  ├── Model prediction   ├── Resource exhaustion        │
│  ├── Confidence scores  ├── Latency attacks            │
│  └── Side-channel       └── Availability bypass        │
│                                                         │
└─────────────────────────────────────────────────────────┘
```

### 1.2 Modelo de Amenazas para IA

| Fase | Amenazas | Impacto |
|------|----------|---------|
| **Training** | Data poisoning, backdoor injection | Modelo comprometido |
| **Inference** | Adversarial examples, evasion | Predicciones incorrectas |
| **Deployment** | Model stealing, API abuse | Pérdida de propiedad intelectual |
| **Data** | Privacy leakage, membership inference | Violación de privacidad |

### 1.3 CIA para IA

```
┌─────────────────────────────────────────────────────────┐
│                CIA PARA SISTEMAS DE IA                  │
├─────────────────────────────────────────────────────────┤
│                                                         │
│  CONFIDENCIALIDAD         INTEGRIDAD                   │
│  ├── Datos de entrenamiento├── Modelo no modificado     │
│  ├── Predicciones         ├── Outputs correctos        │
│  └── Parámetros del modelo└── Sin manipulación         │
│                                                         │
│  DISPONIBILIDAD           PRIVACIDAD                   │
│  ├── Modelo accesible    ├── Datos personales          │
│  ├── Respuesta oportuna  ├── Información sensible      │
│  └── Sin denegación      └── Differential privacy      │
│                                                         │
└─────────────────────────────────────────────────────────┘
```

## 2. Ataques Adversariales

### 2.1 Tipos de Ataques

#### Ataques de Evasión (Inference Time)

```python
# Fast Gradient Sign Method (FGSM)
import torch

def fgsm_attack(model, image, label, epsilon=0.3):
    """Generar ejemplo adversarial con FGSM"""
    image.requires_grad = True
    
    output = model(image)
    loss = torch.nn.functional.cross_entropy(output, label)
    model.zero_grad()
    loss.backward()
    
    # Crear perturbación
    perturbation = epsilon * image.grad.data.sign()
    adversarial_image = image + perturbation
    
    return adversarial_image

# Projected Gradient Descent (PGD)
def pgd_attack(model, image, label, epsilon=0.3, iterations=10):
    """Generar ejemplo adversarial con PGD"""
    adversarial_image = image.clone().detach()
    
    for _ in range(iterations):
        adversarial_image.requires_grad = True
        output = model(adversarial_image)
        loss = torch.nn.functional.cross_entropy(output, label)
        loss.backward()
        
        # Gradient ascent
        adversarial_image = adversarial_image + epsilon * adversarial_image.grad.sign()
        adversarial_image = torch.clamp(adversarial_image, 0, 1)
    
    return adversarial_image
```

#### Ataques de Envenenamiento (Training Time)

```python
# Data Poisoning
def poison_training_data(X_train, y_train, poison_rate=0.1):
    """Envenenar datos de entrenamiento"""
    n_poison = int(len(X_train) * poison_rate)
    indices = np.random.choice(len(X_train), n_poison, replace=False)
    
    # Modificar etiquetas
    y_poisoned = y_train.copy()
    y_poisoned[indices] = 1 - y_poisoned[indices]  # Flip labels
    
    return X_train, y_poisoned

# Backdoor Attack
def inject_backdoor(X_train, y_train, trigger_size=3):
    """Inyectar backdoor en datos"""
    # Agregar trigger a algunas muestras
    for i in range(len(X_train)):
        if np.random.random() < 0.1:
            # Agregar cuadrado negro como trigger
            X_train[i, :trigger_size, :trigger_size] = 0
            y_train[i] = 1  # Clase objetivo
    
    return X_train, y_train
```

#### Ataques de Extracción

```python
# Model Extraction
def extract_model(api_model, n_samples=1000):
    """Extraer modelo a través de API"""
    X_query = np.random.uniform(0, 1, (n_samples, input_dim))
    y_query = []
    
    for x in X_query:
        pred = api_model.predict(x.reshape(1, -1))
        y_query.append(pred[0])
    
    # Entrenar modelo sustituto
    substitute_model = RandomForestClassifier()
    substitute_model.fit(X_query, y_query)
    
    return substitute_model
```

### 2.2 Métricas de Robustez

```python
def evaluate_robustness(model, X_test, y_test, epsilon=0.3):
    """Evaluar robustez del modelo"""
    # Accuracy original
    original_acc = model.score(X_test, y_test)
    
    # Accuracy bajo ataque FGSM
    X_adversarial = fgsm_attack(model, X_test, y_test, epsilon)
    fgsm_acc = model.score(X_adversarial, y_test)
    
    # Accuracy bajo ataque PGD
    X_pgd = pgd_attack(model, X_test, y_test, epsilon)
    pgd_acc = model.score(X_pgd, y_test)
    
    return {
        'original_accuracy': original_acc,
        'fgsm_accuracy': fgsm_acc,
        'pgd_accuracy': pgd_acc,
        'robustness_gap': original_acc - fgsm_acc
    }
```

## 3. Defensas contra Ataques

### 3.1 Entrenamiento Adversarial

```python
def adversarial_training(model, X_train, y_train, epsilon=0.3, epochs=10):
    """Entrenamiento adversarial"""
    for epoch in range(epochs):
        for i in range(len(X_train)):
            # Generar ejemplo adversarial
            x_adv = fgsm_attack(model, X_train[i], y_train[i], epsilon)
            
            # Entrenar con ejemplo original y adversarial
            model.fit(np.vstack([X_train[i], x_adv]), 
                     np.array([y_train[i], y_train[i]]))
    
    return model
```

### 3.2 Detección de Adversariales

```python
class AdversarialDetector:
    def __init__(self, model, threshold=0.5):
        self.model = model
        self.threshold = threshold
    
    def detect(self, input_data):
        """Detectar ejemplos adversariales"""
        # Calcular incertidumbre
        predictions = []
        for _ in range(10):
            pred = self.model.predict(input_data + np.random.normal(0, 0.01, input_data.shape))
            predictions.append(pred)
        
        # Medir varianza
        variance = np.var(predictions)
        
        return variance > self.threshold

    def statistical_detection(self, input_data):
        """Detección estadística"""
        # Analizar distribución de características
        mean = np.mean(input_data)
        std = np.std(input_data)
        
        # Detectar outliers
        is_outlier = abs(mean - 0.5) > 2 * std
        
        return is_outlier
```

### 3.3 Privacidad Diferencial

```python
def differential_privacy_training(model, X_train, y_train, epsilon=1.0):
    """Entrenamiento con privacidad diferencial"""
    # Agregar ruido a los gradientes
    sensitivity = 1.0
    noise_scale = sensitivity / epsilon
    
    # Entrenar con ruido
    noisy_X = X_train + np.random.laplace(0, noise_scale, X_train.shape)
    model.fit(noisy_X, y_train)
    
    return model

def private_prediction(model, x, epsilon=0.1):
    """Predicción con privacidad diferencial"""
    # Agregar ruido a la predicción
    prediction = model.predict(x)
    noise = np.random.laplace(0, 1/epsilon)
    
    return prediction + noise
```

### 3.4 Certificación de Robustez

```python
def certified_robustness(model, x, epsilon=0.1):
    """Certificar robustez del modelo"""
    # Interval Bound Propagation (simplificado)
    lower_bound = x - epsilon
    upper_bound = x + epsilon
    
    # Verificar que todas las predicciones en el intervalo son iguales
    pred_lower = model.predict(lower_bound)
    pred_upper = model.predict(upper_bound)
    
    is_certified = pred_lower == pred_upper
    
    return {
        'certified': is_certified,
        'radius': epsilon if is_certified else 0
    }
```

## 4. Seguridad de Datos de Entrenamiento

### 4.1 Protección de Datos

```python
class DataProtection:
    def __init__(self):
        self.epsilon = 1.0
    
    def anonymize_data(self, data):
        """Anonimizar datos"""
        # Generalización
        anonymized = data.copy()
        anonymized[:, 0] = np.round(anonymized[:, 0], -1)  # Redondear edad
        
        return anonymized
    
    def federated_learning(self, local_models):
        """Aprendizaje federado"""
        # Promediar modelos sin compartir datos
        global_weights = np.mean([m.get_weights() for m in local_models], axis=0)
        
        return global_weights
    
    def secure_aggregation(self, shares):
        """Agregación segura"""
        # Suma secreta
        result = np.sum(shares, axis=0)
        
        return result
```

### 4.2 Membership Inference

```python
def membership_inference_attack(model, target_sample, threshold=0.8):
    """Ataque de inferencia de membresía"""
    # Entrenar modelo de ataque
    attack_model = RandomForestClassifier()
    
    # Predecir probabilidad
    prob = model.predict_proba(target_sample.reshape(1, -1))[0]
    confidence = np.max(prob)
    
    # Decidir si fue miembro
    is_member = confidence > threshold
    
    return {
        'is_member': is_member,
        'confidence': confidence
    }
```

## 5. Auditoría de Sistemas IA

### 5.1 Framework de Auditoría

```python
class AIAuditor:
    def __init__(self, model):
        self.model = model
        self.findings = []
    
    def audit_performance(self, X_test, y_test):
        """Auditar rendimiento"""
        accuracy = self.model.score(X_test, y_test)
        self.findings.append({
            'category': 'Performance',
            'metric': 'Accuracy',
            'value': accuracy,
            'status': 'PASS' if accuracy > 0.8 else 'FAIL'
        })
    
    def audit_bias(self, X_test, sensitive_attr):
        """Auditar sesgo"""
        predictions = self.model.predict(X_test)
        
        # Calcular disparidad
        groups = np.unique(sensitive_attr)
        rates = []
        for group in groups:
            mask = sensitive_attr == group
            rates.append(np.mean(predictions[mask]))
        
        disparity = max(rates) - min(rates)
        self.findings.append({
            'category': 'Bias',
            'metric': 'Demographic Parity',
            'value': disparity,
            'status': 'PASS' if disparity < 0.1 else 'FAIL'
        })
    
    def audit_robustness(self, X_test, y_test, epsilon=0.3):
        """Auditar robustez"""
        # Evaluar contra FGSM
        X_adv = fgsm_attack(self.model, X_test, y_test, epsilon)
        robust_acc = self.model.score(X_adv, y_test)
        
        self.findings.append({
            'category': 'Robustness',
            'metric': 'FGSM Accuracy',
            'value': robust_acc,
            'status': 'PASS' if robust_acc > 0.7 else 'FAIL'
        })
    
    def generate_report(self):
        """Generar reporte de auditoría"""
        report = "# AI Audit Report\n\n"
        
        for finding in self.findings:
            status_icon = "✅" if finding['status'] == 'PASS' else "❌"
            report += f"{status_icon} **{finding['category']}** - {finding['metric']}: {finding['value']:.2%}\n"
        
        return report
```

### 5.2 Métricas de Calidad

| Métrica | Descripción | Objetivo |
|---------|-------------|----------|
| **Accuracy** | Precisión general | > 90% |
| **Robustness** | Resistencia a adversariales | > 70% |
| **Fairness** | Equidad entre grupos | Disparidad < 10% |
| **Privacy** | Protección de datos | ε < 1.0 |
| **Explainability** | Interpretabilidad | Modelo explicable |

## 6. Ejercicios Prácticos

### Ejercicio 1: Evaluar Robustez (60 XP)

```python
# 1. Cargar modelo
model = load_model('my_model.h5')

# 2. Evaluar accuracy original
original_acc = model.evaluate(X_test, y_test)

# 3. Generar adversariales FGSM
X_adv = fgsm_attack(model, X_test, y_test, epsilon=0.3)

# 4. Evaluar bajo ataque
adversarial_acc = model.evaluate(X_adv, y_test)

# 5. Calcular gap de robustez
robustness_gap = original_acc - adversarial_acc
print(f"Robustness gap: {robustness_gap:.2%}")
```

### Ejercicio 2: Entrenamiento Adversarial (80 XP)

```python
# 1. Entrenar modelo base
model = RandomForestClassifier()
model.fit(X_train, y_train)

# 2. Aplicar entrenamiento adversarial
defended_model = adversarial_training(model, X_train, y_train, epsilon=0.3)

# 3. Evaluar defensa
original_robust = evaluate_robustness(model, X_test, y_test)
defended_robust = evaluate_robustness(defended_model, X_test, y_test)

print(f"Original robustness: {original_robust['fgsm_accuracy']:.2%}")
print(f"Defended robustness: {defended_robust['fgsm_accuracy']:.2%}")
```

### Ejercicio 3: Detección de Adversariales (60 XP)

```python
# 1. Crear detector
detector = AdversarialDetector(model)

# 2. Detectar en ejemplos normales
normal_detection = detector.detect(X_test[:10])

# 3. Detectar en ejemplos adversariales
X_adv = fgsm_attack(model, X_test[:10], y_test[:10])
adversarial_detection = detector.detect(X_adv)

# 4. Calcular métricas
true_positives = np.sum(adversarial_detection)
false_positives = np.sum(normal_detection)

print(f"True positives: {true_positives}")
print(f"False positives: {false_positives}")
```

### Ejercicio 4: Auditoría Completa (80 XP)

```python
# 1. Crear auditor
auditor = AIAuditor(model)

# 2. Ejecutar auditorías
auditor.audit_performance(X_test, y_test)
auditor.audit_bias(X_test, sensitive_attr)
auditor.audit_robustness(X_test, y_test)

# 3. Generar reporte
report = auditor.generate_report()
print(report)
```

## 7. Referencias

| Recurso | Descripción |
|---------|-------------|
| [Adversarial Robustness Toolbox](https://github.com/Trusted-AI/adversarial-robustness-toolbox) | Framework de robustez |
| [CleverHans](https://github.com/cleverhans-lab/cleverhans) | Ataques adversariales |
| [IBM AI Fairness 360](https://github.com/Trusted-AI/AIF360) | Detección de sesgo |
| [Google What-If Tool](https://pair-code.github.io/what-if-tool/) | Análisis de modelos |
| [SHAP](https://github.com/slundberg/shap) | Explicabilidad |

## 📌 Checkpoint final

- [ ] Evaluar robustez de modelos
- [ ] Implementar entrenamiento adversarial
- [ ] Detectar ejemplos adversariales
- [ ] Realizar auditoría completa de IA
- [ ] Proteger datos con privacidad diferencial

> ⏭️ **Siguiente:** Proyectos avanzados y certificaciones.
