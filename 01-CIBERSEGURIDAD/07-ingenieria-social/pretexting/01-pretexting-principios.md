# 🎭 Principios del Pretexting

> *El pretexting es la técnica de ingeniería social donde el atacante crea un escenario falso (pretexto) para manipular a la víctima. Este documento cubre los principios psicológicos, técnicas y éticas del pretexting profesional.*

---

## 📋 Tabla de contenido

1. [Qué es el pretexting](#1-qué-es-el-pretexting)
2. [Principios psicológicos](#2-principios-psicológicos)
3. [Fases de un pretexting](#3-fases-de-un-pretexting)
4. [Componentes de un buen pretexto](#4-componentes-de-un-buen-pretexto)
5. [Técnicas de manipulación](#5-técnicas-de-manipulación)
6. [Errores comunes](#6-errores-comunes)
7. [Marco ético](#7-marco-ético)
8. [Ejemplos prácticos](#8-ejemplos-prácticos)
9. [Defensa y remediación](#9-defensa-y-remediación)
10. [Referencias](#10-referencias)

---

## 1. Qué es el pretexting

El pretexting es una forma avanzada de ingeniería social donde el atacante:

- **Crea un escenario creíble** (pretexto) para justificar su interacción
- **Suplanta una identidad** o rol para ganar confianza
- **Manipula emociones** para que la víctima actúe en su contra
- **Obtiene información o acceso** de forma no autorizada

### Diferencia con otras técnicas

| Técnica | Enfoque | Objetivo |
|---|---|---|
| **Phishing** | Email masivo | Credenciales |
| **Vishing** | Teléfono | Información sensible |
| **Pretexting** | Escenario elaborado | Acceso/información |
| **Baiting** | Cebo físico | Infección/robo |
| **Tailgating** | Seguir al objetivo | Acceso físico |

---

## 2. Principios psicológicos

### Los 6 principios de Cialdini

Robert Cialdini identificó 6 principios de persuasión que los atacantes explotan:

#### 1. Reciprocidad

```markdown
# El ser humano siente la obligación de devolver favores

# Ejemplo de pretexting:
"Hola, soy Juan de IT. Te ayudé la semana pasada con tu laptop, 
¿recuerdas? Necesito que me des acceso a tu cuenta para 
verificar una configuración."
```

#### 2. Compromiso y consistencia

```markdown
# Las personas quieren ser consistentes con lo que ya dijeron o hicieron

# Ejemplo:
"Anoche en la reunión mencionaste que tenías problemas con tu cuenta. 
¿Puedes darme tus credenciales para verificarlo?"
```

#### 3. Prueba social

```markdown
# Las personas siguen lo que hacen los demás

# Ejemplo:
"Todos los demás departamentos ya actualizaron sus contraseñas. 
¿Puedes confirmarme la tuya para verificar que estás al día?"
```

#### 4. Autoridad

```markdown
# Las personas obedecen a figuras de autoridad

# Ejemplo:
"Soy el director de TI. Necesito que me des acceso inmediato 
a tu cuenta para una auditoría urgente."
```

#### 5. Escasez

```markdown
# Las personas valoran más lo que es escaso o limitado

# Ejemplo:
"Esta oferta de actualización solo está disponible por 2 horas. 
Si no actualizas ahora, perderás el acceso."
```

#### 6. Simpatía

```markdown
# Las personas son más susceptibles a quienes les agradan

# Ejemplo:
"[Sonrisa amable] Hola, soy nuevo aquí. Me perdí un poco, 
¿podrías ayudarme a encontrar la sala de servidores?"
```

---

## 3. Fases de un pretexting

### Fase 1: Investigación

```markdown
# Recopilar información sobre el objetivo:
- Nombre, cargo, departamento
- Redes sociales (LinkedIn, Facebook)
- Estructura organizacional
- Tecnologías que usan
- Eventos recientes de la empresa
```

### Fase 2: Diseño del pretexto

```markdown
# Crear un escenario creíble:
- ¿Quién soy? (identidad suplantada)
- ¿Por qué estoy aquí? (justificación)
- ¿Qué necesito? (objetivo)
- ¿Qué decir si preguntan? (contingencias)
```

### Fase 3: Ejecución

```markdown
# Implementar el pretexto:
- Contactar a la víctima
- Mantener la coherencia del personaje
- Responder a objeciones
- Obtener la información/acceso deseado
```

### Fase 4: Exfiltración

```markdown
# Obtener el objetivo sin levantar sospechas:
- Confirmar que tienes la información/acceso
- Agradecer y despedirte
- Documentar el hallazgo
- Salir de forma natural
```

---

## 4. Componentes de un buen pretexto

### Estructura de un pretexto

```markdown
## Pretexting Script: Soporte Técnico

### Identidad
- Nombre: Carlos Mendoza
- Cargo: Técnico de Soporte Nivel 2
- Departamento: IT
- Empresa: CorpTech Solutions

### Escenario
- Situación: Se detectó un problema de seguridad en tu cuenta
- Urgencia: Alta (requiere acción inmediata)
- Justificación: Auditoría de seguridad programada

### Objetivo
- Obtener credenciales de acceso
- Verificar configuración de seguridad

### Script de apertura
"Hola, buenos días. Soy Carlos del departamento de TI. 
Estamos realizando una auditoría de seguridad y detectamos 
actividad sospechosa en tu cuenta. ¿Podrías confirmarme 
tus credenciales para verificar?"

### Respuestas a objeciones
- "¿Por qué debo darte mis credenciales?"
  → "Es un procedimiento estándar de auditoría. Si no puedes 
  hacerlo ahora, puedo pasar más tarde, pero es urgente."

- "¿Cómo sé que eres de TI?"
  → "Puedo pasarte mi número de empleado o transferirte 
  con mi supervisor."

- "Prefiero llamar al help desk"
  → "Por supuesto, pero eso tomaría más tiempo y el problema 
  es urgente. Si quieres, puedo pasarte mi número de empleado 
  para que verifiques."
```

### Checklist de un buen pretexto

- [ ] **Credible:** ¿Alguien caería en esto?
- [ ] **Consistente:** ¿Todas las partes del pretexto encajan?
- [ ] **Urgente:** ¿Hay presión para actuar rápido?
- [ ] **Específico:** ¿Incluye detalles que lo hagan real?
- [ ] **Flexible:** ¿Tiene respuestas para objeciones?
- [ ] **Natural:** ¿Fluye como una conversación real?

---

## 5. Técnicas de manipulación

### Técnica 1: Urgencia artificial

```markdown
# Crear presión para que la víctima actúe rápido

"El problema de seguridad es urgente. Si no lo resolvemos 
en los próximos 30 minutos, tu cuenta será bloqueada 
y necesitarás contactar a tu supervisor."
```

### Técnica 2: Autoridad falsa

```markdown
# Usar un cargo o nombre que dé autoridad

"Soy el director de Seguridad de la información. 
El CEO me pidió que verificara todas las cuentas 
de forma inmediata."
```

### Técnica 3: Credibilidad incremental

```markdown
# Empezar con algo pequeño y escalar

Paso 1: "Solo necesito confirmar tu nombre"
Paso 2: "¿Puedes verificar tu departamento?"
Paso 3: "¿Cuál es tu número de empleado?"
Paso 4: "¿Puedes darme tus credenciales para verificar?"
```

### Técnica 4: Simpatía y conexión

```markdown
# Crear un vínculo personal

"Hola, soy nuevo aquí. Me asignaron al proyecto de migración. 
Es mi primer día y estoy un poco perdido. ¿Podrías ayudarme 
a acceder al servidor de datos?"
```

### Técnica 5: Presión de grupo

```markdown
# Usar la presión social

"Todos los demás departamentos ya completaron la verificación. 
Solo falta tu departamento. ¿Podemos hacerlo ahora?"
```

---

## 6. Errores comunes

### Error 1: Falta de coherencia

```markdown
# Mal:
"Hola, soy Juan de IT... ah, perdón, soy María de RRHH... 
bueno, en realidad soy el director de TI"

# Bueno:
Mantener una identidad coherente durante toda la interacción
```

### Error 2: Urgencia excesiva

```markdown
# Mal:
"¡Hazlo AHORA o serás despedido! ¡Es una emergencia!"

# Bueno:
"Es importante resolver esto pronto, pero entiendo si 
necesitas verificar con tu supervisor primero."
```

### Error 3: Falta de información previa

```markdown
# Mal:
No saber el nombre de la víctima, su cargo, o la empresa

# Bueno:
Investigar antes y mencionar detalles específicos
```

### Error 4: Presionar demasiado

```markdown
# Mal:
Insistir cuando la víctima claramente no quiere participar

# Bueno:
Respetar un "no" y tener alternativas preparadas
```

### Error 5: No tener plan B

```markdown
# Mal:
No saber qué hacer si el pretexto falla

# Bueno:
Tener respuestas preparadas para cada objeción
```

---

## 7. Marco ético

### ⚠️ Reglas de oro

```markdown
1. SIEMPRE tener autorización escrita antes de cualquier pretexting
2. NUNCA suplantar a personas reales específicas (usar roles genéricos)
3. NUNCA presionar más allá de lo cómodo para la víctima
4. SIEMPRE documentar qué se hizo y qué se obtuvo
5. NUNCA usar la información para beneficio personal
6. SIEMPRE reportar los hallazgos al equipo de seguridad
7. NUNCA causar daño psicológico o emocional
```

### Formulario de autorización

```markdown
# Autorización para Prueba de Ingeniería Social

Fecha: _______________
Autorizado por: _______________
Cargo: _______________
Alcance: _______________
Fecha de inicio: _______________
Fecha de fin: _______________

## Técnicas autorizadas:
- [ ] Phishing de email
- [ ] Vishing (llamadas telefónicas)
- [ ] Pretexting presencial
- [ ] USB drops

## Objetivos:
- [ ] Departamento de TI
- [ ] Departamento de RRHH
- [ ] Todos los empleados

## Límites:
- Nada de acoso o intimidación
- Nada de suplantación de autoridades legales
- Nada de acceso físico no autorizado
- Respetar un "no" inmediatamente

Firma del autorizado: _______________
Firma del tester: _______________
```

---

## 8. Ejemplos prácticos

### Ejemplo 1: Soporte técnico

```markdown
## Pretexting: Soporte de Microsoft

### Escenario
Llamar a empleados haciéndose pasar por soporte de Microsoft

### Script
"Buenos días, soy Juan del soporte técnico de Microsoft. 
Estamos detectando actividad sospechosa en cuentas de 
Microsoft 365 de varias empresas. ¿Podrías confirmarme 
tu correo electrónico para verificar tu cuenta?"

### Objetivo
Obtener credenciales de Microsoft 365

### Defensa
Microsoft NUNCA llama para pedir credenciales
```

### Ejemplo 2: Auditoría de seguridad

```markdown
## Pretexting: Auditoría de TI

### Escenario
Hacerse pasar por auditor de seguridad interno

### Script
"Hola, soy el auditor de seguridad de la empresa. 
Estamos realizando una auditoría inesperada de acceso. 
¿Puedes confirmarme tu usuario y contraseña para verificar 
que tienes los permisos correctos?"

### Objetivo
Obtener credenciales de usuario

### Defensa
Los auditores nunca piden credenciales directamente
```

### Ejemplo 3: Nuevo empleado

```markdown
## Pretexting: Empleado nuevo

### Escenario
Hacerse pasar por un empleado nuevo perdido

### Script
"Hola, soy nuevo aquí. Me asignaron a la oficina 301 
pero no encuentro la sala de servidores. ¿Podrías 
ayudarme a llegar? También necesito acceso a la red, 
¿sabes quién me puede dar las credenciales?"

### Objetivo
Acceso físico a la sala de servidores

### Defensa
Verificar con RRHH antes de ayudar a desconocidos
```

### Ejemplo 4: IT Urgente

```markdown
## Pretexting: Emergencia de TI

### Escenario
Simular una emergencia de seguridad

### Script
"[Con urgencia] Hola, necesito tu ayuda. Hay un virus 
en la red y necesito verificar tu cuenta inmediatamente. 
¿Cuál es tu contraseña? Es para verificar que no estás 
comprometido."

### Objetivo
Obtener credenciales bajo presión

### Defensa
IT nunca pide contraseñas por teléfono
```

---

## 9. Defensa y remediación

### Para Blue Team / Equipo de Seguridad

| Vector | Detección | Mitigación |
|---|---|---|
| **Pretexting por email** | Analizar headers, remitente | Entrenamiento, verificación |
| **Pretexting telefónico** | Verificar identidad del llamante | Políticas de verificación |
| **Pretexting presencial** | Pedir identificación | Badges, acceso controlado |
| **Urgencia artificial** | Cuestionar la urgencia | Políticas de verificación |

### Entrenamiento

| Actividad | Frecuencia | Responsable |
|---|---|---|
| Simulacros de pretexting | Trimestral | Equipo de Seguridad |
| Entrenamiento en verificación | Mensual | RRHH + Seguridad |
| Evaluación de resultados | Post-simulacro | Management |

### Políticas de verificación

```markdown
## Política de Verificación de Identidad

1. NUNCA dar información sensible sin verificar
2. SIEMPRE pedir identificación oficial
3. SIEMPRE llamar al departamento para verificar
4. NUNCA ceder a presión o urgencia
5. SIEMPRE reportar intentos sospechosos
```

---

## 10. Referencias

### Fuentes primarias

| Recurso | URL |
|---|---|
| **MITRE ATT&CK — Pretexting** | [https://attack.mitre.org/techniques/T1598/](https://attack.mitre.org/techniques/T1598/) |
| **NIST SP 800-50** | Building an IT Security Awareness Program |
| **SANS Security Awareness** | [https://www.sans.org/security-awareness-training/](https://www.sans.org/security-awareness-training/) |
| **Cialdini - Influence** | Libro: "Influence: The Psychology of Persuasion" |

### Frameworks de referencia

| Framework | Uso |
|---|---|
| **MITRE ATT&CK** | Tácticas y técnicas de adversarios |
| **NIST CSF** | Marco de seguridad |
| **ISO 27001** | Gestión de seguridad |

---

## 📝 Entregable de portafolio

```markdown
# Prueba de Pretexting — [Nombre de la empresa]

## Contexto
- Objetivo: Departamento de TI
- Autorización: Firmada por CISO
- Duración: 1 semana

## Pretexto utilizado
- Identidad: Soporte técnico de Microsoft
- Escenario: Emergencia de seguridad
- Urgencia: Alta

## Resultados
- Empleados contactados: 10
- Empleados que cedieron: 4 (40%)
- Información obtenida: Credenciales de Microsoft 365

## Análisis
- El 40% de los empleados cedió credenciales
- La urgencia fue el factor principal de éxito
- Solo el 20% verificó la identidad del llamante

## Recomendaciones
1. Entrenamiento en verificación de identidad
2. Política de "nunca dar credenciales por teléfono"
3. Proceso de verificación con supervisor
4. Simulacros trimestrales

## Evidencia
- Autorización firmada: [enlace]
- Grabaciones (anonimizadas): [enlace]
- Reporte: [enlace]
```

---

**[⬅ Herramientas](../herramientas/03-herramientas-fishing.md)** · **[⬅ Volver al módulo](../README.md)** · **[→ Pretextos corporativos](./02-pretextos-corporativos.md)**
