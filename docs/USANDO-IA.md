# 🤖 Cómo Usar IA como Copiloto en esta plataforma

> La IA no hace el trabajo por ti — acelera tu aprendizaje si sabes cómo usarla.

---

## Principio fundamental

```
Perplexity → Investigar y estructurar
Claude / GPT → Implementar y refactorizar
Tú → Criterio técnico, ética y responsabilidad final
```

La IA es una herramienta de amplificación. Si la usas sin entender lo que produce, aprenderás nada. Si la usas como acelerador de lo que ya estás aprendiendo, avanzas 3x más rápido.

---

## Perplexity — Motor de investigación

Usa Perplexity para:

### 1. Investigar marcos y frameworks
```
Prompt ejemplo:
"Resume los 14 controles de ISO 27001:2022 en una tabla con nombre, categoría y ejemplo práctico"
```

### 2. Comparar herramientas
```
Prompt ejemplo:
"Compara Wazuh vs Splunk vs ELK para un SOC pequeño con presupuesto limitado. Tabla con: costo, curva de aprendizaje, integraciones y comunidad"
```

### 3. Diseñar planes de estudio
```
Prompt ejemplo:
"Diseña un plan de estudio de 4 semanas para preparar el examen eJPT, con recursos gratuitos y ejercicios prácticos diarios"
```

### 4. Buscar recursos actualizados
```
Prompt ejemplo:
"¿Cuáles son los mejores laboratorios gratuitos de Blue Team disponibles en 2026?"
```

---

## Claude / GPT — Motor de implementación

Usa Claude o GPT para:

### 1. Refactorizar código
```
Prompt ejemplo:
"Revisa este script Python de escaneo Nmap y mejora el manejo de errores, 
agrega logging y hazlo compatible con Python 3.12. El código es:
[pega tu código]"
```

### 2. Generar scaffolding de proyectos
```
Prompt ejemplo:
"Crea la estructura base de un script Python para automatizar búsquedas 
de subdominios usando la API de SecurityTrails. Incluye manejo de 
excepciones, logging y salida en JSON"
```

### 3. Explicar conceptos técnicos
```
Prompt ejemplo:
"Explícame cómo funciona un ataque de Pass-the-Hash en Active Directory, 
como si fuera para alguien que conoce Windows pero nunca ha hecho pentesting"
```

### 4. Revisar y mejorar documentación
```
Prompt ejemplo:
"Mejora este README de mi script de seguridad para que sea profesional 
y publicable en GitHub. Hazlo en español técnico. El README actual es:
[pega tu README]"
```

### 5. Generar plantillas de reportes
```
Prompt ejemplo:
"Crea una plantilla de reporte de pentesting en Markdown con secciones: 
resumen ejecutivo, alcance, hallazgos (por CVSS), evidencias y recomendaciones"
```

---

## Flujos de trabajo recomendados por módulo

### Al empezar un módulo nuevo
1. **Perplexity:** "¿Qué necesito saber antes de empezar con [tema]? Dame los 5 conceptos clave y recursos para cada uno."
2. Lee el material del módulo en este repo.
3. **Claude:** "Genera un lab sencillo en Docker para practicar [técnica] paso a paso."

### Al escribir código
1. Escribe el primer borrador tú mismo (aunque sea imperfecto).
2. **Claude:** "Revisa este código, identifica bugs y mejora la estructura sin cambiar la lógica principal."
3. Entiende cada cambio antes de aceptarlo.

### Al documentar un proyecto
1. Escribe los puntos clave de lo que hiciste.
2. **Claude:** "Convierte estas notas en un README profesional para GitHub en español técnico."
3. Revisa que el README sea 100% correcto técnicamente antes de publicar.

### Al preparar un post de LinkedIn
1. **Perplexity:** "¿Cómo presentan sus proyectos de ciberseguridad los profesionales en LinkedIn? Dame ejemplos."
2. Escribe tu propio post basado en lo que aprendiste.
3. **Claude:** "Mejora la redacción de este post de LinkedIn sobre [proyecto]. Hazlo concreto y profesional."

---

## Lo que la IA NO puede hacer por ti

| Tarea | Por qué debes hacerlo tú |
|---|---|
| Entender conceptos | La comprensión real no se delega |
| Tomar decisiones éticas | La ética en seguridad es tuya |
| Validar que el código funciona | Siempre prueba lo que produces |
| Crear criterio técnico | Solo se desarrolla con práctica |
| Asumir responsabilidad legal | El profesional eres tú |

---

## Stack de IA recomendado para esta plataforma

| Herramienta | Uso | Costo |
|---|---|---|
| **Perplexity** | Investigación y estructuración | Gratis (básico) |
| **Claude (Anthropic)** | Código, refactor, documentación | Gratis con límites |
| **Ollama** | Modelos offline para datos sensibles | Gratis |
| **GitHub Copilot** | Autocompletado en VS Code / IntelliJ | Gratis para estudiantes |
| **ChatGPT** | Alternativa a Claude | Gratis (básico) |

> 💡 Para datos sensibles de laboratorio (IPs reales, tokens, credenciales de prueba), usa siempre **Ollama** con modelos locales. Nunca pegues datos sensibles en servicios cloud.

---

*[← Volver al README](../README.md)*
