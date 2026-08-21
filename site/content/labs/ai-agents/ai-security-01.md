---
title: "🤖 Lab ai-security-01: Seguridad de IA"
description: "🤖 Lab ai-security-01: Seguridad de IA"
---

# 🤖 Lab ai-security-01: Seguridad de IA

> Aprende a proteger sistemas de IA y a atacar modelos de machine learning.

## 🎯 Objetivos de Aprendizaje

Al completar este lab podrás:

- [ ] Identificar vulnerabilidades en sistemas de IA
- [ ] Ejecutar ataques contra modelos ML
- [ ] Implementar defensas para IA
- [ ] Auditar sistemas de IA
- [ ] Generar reportes de seguridad de IA

## ⏱️ Información del Lab

| Campo | Valor |
|-------|-------|
| **Dificultad** | 🟡 Intermedio |
| **Tiempo estimado** | 90 minutos |
| **XP en juego** | 450 puntos |
| **Herramientas** | Python, adversarial-robustness-toolbox, custom scripts |
| **Flags** | 8 |

## 🚀 Inicio Rápido

```bash
# Levantar el entorno
cd labs/ai-agents/ai-security-01/
docker compose up -d
```

## 📋 Ejercicios

### Ejercicio 1: Auditoría de Modelo (60 XP)

Audita un modelo de ML:

```python
#!/usr/bin/env python3
# model_auditor.py

import numpy as np
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split

class ModelAuditor:
    def __init__(self, model, X_test, y_test):
        self.model = model
        self.X_test = X_test
        self.y_test = y_test
    
    def evaluate_performance(self):
        """Evaluar rendimiento del modelo"""
        accuracy = self.model.score(self.X_test, self.y_test)
        return {
            'accuracy': accuracy,
            'samples': len(self.X_test)
        }
    
    def check_bias(self):
        """Verificar sesgo en el modelo"""
        predictions = self.model.predict(self.X_test)
        # Analizar distribución de predicciones
        unique, counts = np.unique(predictions, return_counts=True)
        return dict(zip(unique, counts))
    
    def adversarial_robustness(self, epsilon=0.1):
        """Probar robustez adversarial"""
        # Generar ejemplos adversariales simples
        noise = np.random.uniform(-epsilon, epsilon, self.X_test.shape)
        X_adversarial = self.X_test + noise
        
        # Evaluar en ejemplos adversariales
        robust_accuracy = self.model.score(X_adversarial, self.y_test)
        return {
            'original_accuracy': self.model.score(self.X_test, self.y_test),
            'adversarial_accuracy': robust_accuracy,
            'degradation': self.model.score(self.X_test, self.y_test) - robust_accuracy
        }
    
    def generate_report(self):
        """Generar reporte de auditoría"""
        performance = self.evaluate_performance()
        bias = self.check_bias()
        robustness = self.adversarial_robustness()
        
        report = "# Model Audit Report\n\n"
        report += "## Performance\n"
        report += f"- Accuracy: {performance['accuracy']:.2%}\n"
        report += f"- Samples: {performance['samples']}\n\n"
        
        report += "## Bias Analysis\n"
        report += f"- Class distribution: {bias}\n\n"
        
        report += "## Adversarial Robustness\n"
        report += f"- Original accuracy: {robustness['original_accuracy']:.2%}\n"
        report += f"- Adversarial accuracy: {robustness['adversarial_accuracy']:.2%}\n"
        report += f"- Degradation: {robustness['degradation']:.2%}\n"
        
        return report

# Ejecutar auditoría
from sklearn.datasets import load_iris
data = load_iris()
X_train, X_test, y_train, y_test = train_test_split(data.data, data.target, test_size=0.2)

model = RandomForestClassifier(n_estimators=100)
model.fit(X_train, y_train)

auditor = ModelAuditor(model, X_test, y_test)
print(auditor.generate_report())
```

**Flag:** `[___]`

---

### Ejercicio 2: Ataques Adversariales (80 XP)

Ejecuta ataques contra modelos:

```python
#!/usr/bin/env python3
# adversarial_attack.py

import numpy as np

class AdversarialAttacker:
    def __init__(self, model, epsilon=0.3):
        self.model = model
        self.epsilon = epsilon
    
    def fgsm_attack(self, image, label):
        """Fast Gradient Sign Method"""
        # Calcular gradiente
        image_tensor = np.expand_dims(image, axis=0)
        predictions = self.model.predict(image_tensor)
        
        # Simular ataqueFGSM
        perturbation = self.epsilon * np.sign(image)
        adversarial_image = image + perturbation
        
        return adversarial_image
    
    def pgd_attack(self, image, label, iterations=10):
        """Projected Gradient Descent"""
        adversarial_image = image.copy()
        
        for _ in range(iterations):
            # Simular PGD
            perturbation = self.epsilon * np.sign(np.random.randn(*image.shape))
            adversarial_image = image + perturbation
            adversarial_image = np.clip(adversarial_image, 0, 1)
        
        return adversarial_image
    
    def transfer_attack(self, source_model, target_image):
        """Transfer learning attack"""
        # Usar modelo fuente para generar adversarial
        perturbation = self.epsilon * np.sign(np.random.randn(*target_image.shape))
        adversarial_image = target_image + perturbation
        
        return adversarial_image
    
    def evaluate_attack(self, original_image, adversarial_image, true_label):
        """Evaluar efectividad del ataque"""
        orig_pred = self.model.predict(original_image.reshape(1, -1))[0]
        adv_pred = self.model.predict(adversarial_image.reshape(1, -1))[0]
        
        return {
            'original_prediction': orig_pred,
            'adversarial_prediction': adv_pred,
            'attack_successful': orig_pred != adv_pred
        }

# Ejecutar ataque
attacker = AdversarialAttacker(model, epsilon=0.3)
adversarial = attacker.fgsm_attack(X_test[0], y_test[0])
result = attacker.evaluate_attack(X_test[0], adversarial, y_test[0])
print(f"Attack successful: {result['attack_successful']}")
```

**Flag:** `[___]`

---

### Ejercicio 3: Defensa contra Ataques (60 XP)

Implementa defensas:

```python
#!/usr/bin/env python3
# defense_agent.py

import numpy as np

class DefenseAgent:
    def __init__(self, model):
        self.model = model
    
    def adversarial_training(self, X_train, y_train, epsilon=0.3):
        """Entrenamiento adversarial"""
        # Generar ejemplos adversariales
        X_adversarial = X_train + epsilon * np.sign(np.random.randn(*X_train.shape))
        
        # Combinar datos originales y adversariales
        X_combined = np.vstack([X_train, X_adversarial])
        y_combined = np.hstack([y_train, y_train])
        
        # Re-entrenar modelo
        self.model.fit(X_combined, y_combined)
        
        return self.model
    
    def input_validation(self, input_data):
        """Validar entrada"""
        # Verificar rango de valores
        if np.any(input_data < 0) or np.any(input_data > 1):
            raise ValueError("Input out of range")
        
        # Verificar distribución
        if np.std(input_data) > 2:
            raise ValueError("Input distribution suspicious")
        
        return True
    
    def ensemble_defense(self, X_test, n_models=5):
        """Defensa por ensemble"""
        predictions = []
        
        for _ in range(n_models):
            # Crear modelo con ruido
            noisy_pred = self.model.predict(X_test + np.random.normal(0, 0.1, X_test.shape))
            predictions.append(noisy_pred)
        
        # Votación mayoritaria
        final_pred = np.round(np.mean(predictions, axis=0)).astype(int)
        
        return final_pred
    
    def certified_defense(self, input_data, epsilon=0.1):
        """Defensa certificada"""
        # Verificar certificación de robustez
        min_distance = np.min(np.abs(input_data))
        
        return {
            'certified': min_distance > epsilon,
            'radius': min_distance
        }

# Implementar defensas
defender = DefenseAgent(model)
defended_model = defender.adversarial_training(X_train, y_train)
```

**Flag:** `[___]`

---

### Ejercicio 4: Detección de Ataques (60 XP)

Detecta intentos de ataque:

```python
#!/usr/bin/env python3
# attack_detector.py

import numpy as np

class AttackDetector:
    def __init__(self, model, threshold=0.5):
        self.model = model
        self.threshold = threshold
    
    def detect_anomaly(self, input_data):
        """Detectar anomalías en entradas"""
        # Calcular estadísticas
        mean_val = np.mean(input_data)
        std_val = np.std(input_data)
        
        # Detectar outliers
        is_anomaly = abs(mean_val - 0.5) > self.threshold or std_val > 1.0
        
        return {
            'is_anomaly': is_anomaly,
            'mean': mean_val,
            'std': std_val
        }
    
    def detect_adversarial(self, original, adversarial):
        """Detectar ejemplos adversariales"""
        # Calcular diferencia
        diff = np.abs(adversarial - original)
        max_diff = np.max(diff)
        
        is_adversarial = max_diff > 0.1
        
        return {
            'is_adversarial': is_adversarial,
            'max_perturbation': max_diff
        }
    
    def monitor_predictions(self, predictions):
        """Monitorear predicciones"""
        # Detectar cambios drásticos
        unique, counts = np.unique(predictions, return_counts=True)
        
        # Verificar distribución
        expected_ratio = 1.0 / len(unique)
        actual_ratio = counts / len(predictions)
        
        is_suspicious = np.any(actual_ratio < expected_ratio * 0.1)
        
        return {
            'is_suspicious': is_suspicious,
            'distribution': dict(zip(unique, actual_ratio))
        }

# Detectar ataques
detector = AttackDetector(model)
anomaly_result = detector.detect_anomaly(adversarial)
print(f"Anomaly detected: {anomaly_result['is_anomaly']}")
```

**Flag:** `[___]`

---

### Ejercicio 5: Auditoría de Sesgo (60 XP)

Detecta sesgo en modelos:

```python
#!/usr/bin/env python3
# bias_detector.py

import numpy as np

class BiasDetector:
    def __init__(self, model, sensitive_features):
        self.model = model
        self.sensitive_features = sensitive_features
    
    def demographic_parity(self, X_test, sensitive_attr):
        """Paridad demográfica"""
        predictions = self.model.predict(X_test)
        
        # Calcular tasa de selección por grupo
        groups = np.unique(sensitive_attr)
        selection_rates = {}
        
        for group in groups:
            mask = sensitive_attr == group
            selection_rates[group] = np.mean(predictions[mask])
        
        # Verificar paridad
        max_diff = max(selection_rates.values()) - min(selection_rates.values())
        
        return {
            'selection_rates': selection_rates,
            'disparity': max_diff,
            'fair': max_diff < 0.1
        }
    
    def equalized_odds(self, X_test, y_test, sensitive_attr):
        """Odds equalizados"""
        predictions = self.model.predict(X_test)
        
        groups = np.unique(sensitive_attr)
        tpr_by_group = {}
        fpr_by_group = {}
        
        for group in groups:
            mask = sensitive_attr == group
            group_pred = predictions[mask]
            group_true = y_test[mask]
            
            # True Positive Rate
            tpr_by_group[group] = np.mean(group_pred[group_true == 1])
            # False Positive Rate
            fpr_by_group[group] = np.mean(group_pred[group_true == 0])
        
        return {
            'tpr': tpr_by_group,
            'fpr': fpr_by_group
        }
    
    def generate_report(self, results):
        """Generar reporte de sesgo"""
        report = "# Bias Audit Report\n\n"
        
        if 'demographic_parity' in results:
            dp = results['demographic_parity']
            report += "## Demographic Parity\n"
            report += f"- Disparity: {dp['disparity']:.2%}\n"
            report += f"- Fair: {dp['fair']}\n\n"
        
        return report

# Detectar sesgo
detector = BiasDetector(model, sensitive_features)
dp_result = detector.demographic_parity(X_test, sensitive_attr)
print(f"Demographic parity fair: {dp_result['fair']}")
```

**Flag:** `[___]`

---

### Ejercicio 6: Protección de Datos (60 XP)

Implementa protección de datos:

```python
#!/usr/bin/env python3
# data_protection.py

import numpy as np

class DataProtector:
    def __init__(self):
        self.privacy_budget = 1.0
    
    def differential_privacy(self, data, epsilon=0.1):
        """Privacidad diferencial"""
        # Agregar ruido Laplace
        sensitivity = np.max(data) - np.min(data)
        noise = np.random.laplace(0, sensitivity / epsilon, data.shape)
        
        private_data = data + noise
        
        return private_data
    
    def federated_learning(self, local_models):
        """Aprendizaje federado"""
        # Promediar modelos locales
        global_weights = {}
        
        for layer in local_models[0].get_weights():
            layer_weights = [model.get_weights()[i] for model in local_models]
            global_weights[layer] = np.mean(layer_weights, axis=0)
        
        return global_weights
    
    def secure_aggregation(self, shares):
        """Agregación segura"""
        # Suma secreta
        result = np.sum(shares, axis=0)
        
        return result
    
    def model_encryption(self, model_weights):
        """Cifrar pesos del modelo"""
        # Simular cifrado
        key = np.random.randint(0, 256, model_weights.shape)
        encrypted = model_weights ^ key
        
        return encrypted, key

# Proteger datos
protector = DataProtector()
private_data = protector.differential_privacy(X_train, epsilon=0.1)
print(f"Privacy budget: {protector.privacy_budget}")
```

**Flag:** `[___]`

---

### Ejercicio 7: Reporte de Seguridad (60 XP)

Genera reporte completo:

```markdown
# AI Security Report

## Executive Summary
- Model audited: RandomForestClassifier
- Accuracy: 95%
- Vulnerabilities found: 3
- Bias detected: Yes

## Findings

### 1. Adversarial Vulnerability (HIGH)
- **Issue:** Model vulnerable to FGSM attacks
- **Impact:** Misclassification with 90% success rate
- **Recommendation:** Implement adversarial training

### 2. Data Poisoning Risk (MEDIUM)
- **Issue:** No input validation
- **Impact:** Model could be poisoned
- **Recommendation:** Implement input validation

### 3. Bias in Predictions (HIGH)
- **Issue:** Demographic parity violation
- **Impact:** Unfair predictions for certain groups
- **Recommendation:** Re-train with balanced data

## Recommendations
1. Implement adversarial training
2. Add input validation
3. Regular bias audits
4. Monitor model performance
5. Implement privacy-preserving ML

## Appendix
- Model architecture
- Training data statistics
- Evaluation metrics
```

**Flag:** `[___]`

---

### Ejercicio 8: Monitoreo Continuo (40 XP)

Implementa monitoreo:

```python
#!/usr/bin/env python3
# monitoring_agent.py

import time
from datetime import datetime

class MonitoringAgent:
    def __init__(self, model):
        self.model = model
        self.metrics_history = []
    
    def collect_metrics(self, X_test, y_test):
        """Recopilar métricas"""
        accuracy = self.model.score(X_test, y_test)
        predictions = self.model.predict(X_test)
        
        metrics = {
            'timestamp': datetime.now().isoformat(),
            'accuracy': accuracy,
            'prediction_distribution': dict(zip(*np.unique(predictions, return_counts=True)))
        }
        
        self.metrics_history.append(metrics)
        
        return metrics
    
    def detect_drift(self, window_size=10):
        """Detectar drift del modelo"""
        if len(self.metrics_history) < window_size:
            return {'drift_detected': False}
        
        recent = self.metrics_history[-window_size:]
        accuracies = [m['accuracy'] for m in recent]
        
        # Calcular tendencia
        drift = np.polyfit(range(len(accuracies)), accuracies, 1)[0]
        
        return {
            'drift_detected': abs(drift) > 0.01,
            'drift_magnitude': drift
        }
    
    def alert_on_degradation(self, threshold=0.8):
        """Alertar en degradación"""
        if not self.metrics_history:
            return {'alert': False}
        
        current_accuracy = self.metrics_history[-1]['accuracy']
        
        return {
            'alert': current_accuracy < threshold,
            'current_accuracy': current_accuracy,
            'threshold': threshold
        }

# Monitorear modelo
monitor = MonitoringAgent(model)
metrics = monitor.collect_metrics(X_test, y_test)
drift = monitor.detect_drift()
alert = monitor.alert_on_degradation()
print(f"Drift detected: {drift['drift_detected']}")
```

**Flag:** `[___]`

## 🏁 Validación

```bash
./scripts/validate.sh
```

## 📝 Criterios de Éxito

| Ejercicio | Criterio | Puntos | Estado |
|-----------|----------|--------|--------|
| 1 | Auditoría ejecutada | 60 | ⬜ |
| 2 | Ataques ejecutados | 80 | ⬜ |
| 3 | Defensas implementadas | 60 | ⬜ |
| 4 | Detección configurada | 60 | ⬜ |
| 5 | Sesgo detectado | 60 | ⬜ |
| 6 | Datos protegidos | 60 | ⬜ |
| 7 | Reporte generado | 60 | ⬜ |
| 8 | Monitoreo activo | 40 | ⬜ |
| **Total** | | **450** | ⬜ |

---

*Lab creado para CyberDefense Labs — Nivel Intermedio*
