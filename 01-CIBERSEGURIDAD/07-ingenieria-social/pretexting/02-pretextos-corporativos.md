# 🏢 Pretextos Corporativos

> *Este documento contiene scripts y escenarios de pretexting específicos para entornos corporativos. Cada pretexto incluye el escenario, el script, el objetivo y las defensas correspondientes.*

---

## 📋 Tabla de contenido

1. [Pretextos por departamento](#1-pretextos-por-departamento)
2. [Pretextos por vector](#2-pretextos-por-vector)
3. [Scripts completos](#3-scripts-completos)
4. [Adaptación a culturas](#4-adaptación-a-culturas)
5. [Defensa y remediación](#5-defensa-y-remediación)
6. [Referencias](#6-referencias)

---

## 1. Pretextos por departamento

### Departamento de TI

#### Soporte técnico remoto

```markdown
## Pretexting: Soporte técnico de Microsoft

### Escenario
Llamar a empleados haciéndose pasar por soporte de Microsoft

### Script
"Buenos días, soy Juan del soporte técnico de Microsoft. 
Estamos detectando actividad sospechosa en cuentas de 
Microsoft 365 de varias empresas. 

¿Podrías confirmarme tu correo electrónico para verificar 
tu cuenta?"

### Preguntas de seguimiento
- "¿Cuál es tu contraseña? Es para verificar que no estás 
  comprometido."
- "¿Puedes abrir tu navegador y seguir mis instrucciones?"

### Objetivo
Obtener credenciales de Microsoft 365

### Defensa
- Microsoft NUNCA llama para pedir credenciales
- Verificar con el help desk interno
- Nunca dar contraseñas por teléfono
```

#### Administrador de sistemas

```markdown
## Pretexting: Auditor de seguridad

### Escenario
Hacerse pasar por auditor de seguridad interno

### Script
"Hola, soy el auditor de seguridad de la empresa. 
Estamos realizando una auditoría inesperada de acceso. 

¿Puedes confirmarme tu usuario y contraseña para verificar 
que tienes los permisos correctos?"

### Preguntas de seguimiento
- "¿Cuál es tu contraseña de administrator?"
- "¿Puedes darme acceso al servidor de producción?"

### Objetivo
Obtener credenciales privilegiadas

### Defensa
- Los auditores nunca piden credenciales directamente
- Verificar con el departamento de auditoría
- Usar credenciales de auditoría dedicadas
```

### Departamento de RRHH

#### Nuevo empleado

```markdown
## Pretexting: Empleado nuevo

### Escenario
Hacerse pasar por un empleado nuevo que necesita ayuda

### Script
"Hola, soy nuevo aquí. Me asignaron a la oficina 301 
pero no encuentro la sala de servidores. 

¿Podrías ayudarme a llegar? También necesito acceso 
a la red, ¿sabes quién me puede dar las credenciales?"

### Preguntas de seguimiento
- "¿Dónde está el archivo de contraseñas?"
- "¿Quién es el administrador de sistemas?"

### Objetivo
Acceso físico a la sala de servidores

### Defensa
- Verificar con RRHH antes de ayudar a desconocidos
- Pedir identificación oficial
- Acompañar al visitante
```

#### Auditoría de RRHH

```markdown
## Pretexting: Auditoría de RRHH

### Escenario
Simular una auditoría de recursos humanos

### Script
"Hola, soy el auditor de RRHH. Estamos verificando 
la información de todos los empleados. 

¿Puedes confirmarme tu número de seguro social 
para verificar tu expediente?"

### Preguntas de seguimiento
- "¿Cuál es tu salario anual?"
- "¿Cuáles son tus beneficios?"

### Objetivo
Obtener información personal sensible

### Defensa
- RRHH nunca pide información sensible por teléfono
- Verificar con el departamento de RRHH
- Usar portales seguros para información personal
```

### Departamento Financiero

#### Transferencia bancaria

```markdown
## Pretexting: Transferencia urgente

### Escenario
Simular una transferencia bancaria urgente del CEO

### Script
"[Con urgencia] Hola, soy el CEO. Necesito que hagas 
una transferencia bancaria urgente a un proveedor. 

Es confidencial, no lo discutas con nadie. ¿Puedes 
hacerlo ahora?"

### Preguntas de seguimiento
- "¿Cuál es el número de cuenta?"
- "¿Puedes hacerlo antes de las 3 pm?"

### Objetivo
Transferencia fraudulenta

### Defensa
- NUNCA hacer transferencias sin verificación
- Llamar al CEO para confirmar
- Usar procesos de doble autorización
```

#### Auditoría financiera

```markdown
## Pretexting: Auditoría financiera

### Escenario
Simular una auditoría financiera externa

### Script
"Hola, soy el auditor externo de Deloitte. Estamos 
realizando la auditoría anual y necesito acceder 
a los estados financieros. 

¿Puedes darme acceso al servidor de contabilidad?"

### Preguntas de seguimiento
- "¿Cuál es la contraseña del servidor?"
- "¿Dónde están los archivos de impuestos?"

### Objetivo
Acceso a información financiera sensible

### Defensa
- Verificar con el departamento financiero
- Usar credenciales de auditoría dedicadas
- Limitar acceso al mínimo necesario
```

### Departamento de Ventas

#### Cliente potencial

```markdown
## Pretexting: Cliente potencial

### Escenario
Hacerse pasar por un cliente interesado en comprar

### Script
"Hola, estoy interesado en sus productos. ¿Podrías 
enviarme información detallada y precios? 

También necesito acceder a su portal de clientes 
para ver el catálogo completo."

### Preguntas de seguimiento
- "¿Cuáles son sus descuentos para grandes volúmenes?"
- "¿Puedo acceder a su intranet?"

### Objetivo
Acceso a información comercial y clientes

### Defensa
- Verificar identidad del cliente
- Usar portales públicos para información
- No dar acceso a sistemas internos
```

---

## 2. Pretextos por vector

### Pretexting por email

```markdown
## Ejemplo: Email de IT

Asunto: Acción requerida: Actualización de seguridad

Estimado empleado,

Estamos realizando una actualización de seguridad urgente 
en todos los equipos. Necesitamos verificar tus credenciales 
para continuar con la actualización.

Por favor, responde a este email con:
1. Tu usuario
2. Tu contraseña actual
3. Tu número de empleado

Si no respondes en las próximas 2 horas, tu cuenta será 
bloqueada temporalmente.

Atentamente,
Departamento de TI
```

### Pretexting por teléfono (Vishing)

```markdown
## Ejemplo: Llamada de soporte

Llamador: "Hola, soy Juan del soporte técnico de Microsoft. 
Estamos detectando actividad sospechosa en tu cuenta de 
Microsoft 365. ¿Puedes confirmarme tu contraseña para 
verificar?"

Víctima: "¿Cómo sé que eres de Microsoft?"

Llamador: "Puedo darte mi número de empleado: 12345. 
También puedes llamar a Microsoft directamente para 
verificar, pero eso tomaría más tiempo y el problema 
es urgente."

Víctima: "Bueno, mi contraseña es..."

Llamador: "Gracias. Ahora necesito que abras tu navegador 
y vayas a esta página para completar la verificación..."
```

### Pretexting presencial

```markdown
## Ejemplo: Visitante en la oficina

Visitante: "[Sonrisa amable] Hola, soy nuevo aquí. 
Me asignaron a la oficina 301 pero no encuentro 
la sala de servidores. ¿Podrías ayudarme a llegar?"

Empleado: "¿De qué departamento eres?"

Visitante: "Soy de TI, me asignaron al proyecto de migración. 
Es mi primer día y estoy un poco perdido."

Empleado: "Déjame llamar a TI para verificar..."

Visitante: "No es necesario, puedo llamar yo mismo. 
Solo necesito que me abrás la puerta del tercer piso."
```

---

## 3. Scripts completos

### Script 1: Soporte técnico completo

```markdown
## Pretexting: Soporte técnico de Microsoft

### Fase 1: Apertura
"Buenos días, soy Juan del soporte técnico de Microsoft. 
¿Puedo hablar con el titular de esta cuenta?"

### Fase 2: Verificación (falsa)
"Para verificar que eres el titular, ¿cuál es tu 
correo electrónico completo?"

### Fase 3: Urgencia
"Hemos detectado actividad sospechosa en tu cuenta. 
Hay un intento de acceso desde Rusia. Necesitamos 
verificar tu identidad inmediatamente."

### Fase 4: Obtención de credenciales
"¿Puedes confirmarme tu contraseña para verificar 
que no estás comprometido?"

### Fase 5: Escalamiento
"Ahora necesito que abras tu navegador y vayas a 
esta página para completar la verificación de seguridad..."

### Respuestas a objeciones
- "¿Por qué debo darme mi contraseña?"
  → "Es un procedimiento estándar de emergencia. Si no lo 
  haces ahora, tu cuenta será bloqueada."

- "¿Cómo sé que eres de Microsoft?"
  → "Puedo darte mi número de empleado: 12345. 
  También puedes llamar a Microsoft para verificar."

- "Prefiero llamar al help desk"
  → "Por supuesto, pero eso tomaría más tiempo y el problema 
  es urgente. Si quieres, puedo pasarte mi número de empleado."
```

### Script 2: Auditoría de seguridad

```markdown
## Pretexting: Auditoría de seguridad

### Fase 1: Apertura
"Hola, soy el auditor de seguridad de la empresa. 
Estamos realizando una auditoría inesperada de acceso."

### Fase 2: Verificación (falsa)
"¿Puedes confirmarme tu usuario para verificar que 
estás en la lista de auditados?"

### Fase 3: Urgencia
"La auditoría debe completarse antes de las 5 pm. 
Si no verificamos tu acceso, será un hallazgo crítico."

### Fase 4: Obtención de credenciales
"¿Puedes confirmarme tu contraseña para verificar 
que tienes los permisos correctos?"

### Fase 5: Escalamiento
"Ahora necesito que accedas al servidor de producción 
para verificar la configuración de seguridad..."

### Respuestas a objeciones
- "¿Por qué no sabía de esta auditoría?"
  → "Es una auditoría sorpresa, por eso no se anunció. 
  Es parte del programa de seguridad."

- "¿Quién autorizó esto?"
  → "El director de TI. Si quieres, puedo pasarte 
  su número para que verifiques."

- "Prefiero verificar con mi supervisor"
  → "Por supuesto, pero la auditoría es urgente. 
  Si no se completa hoy, será un hallazgo crítico."
```

### Script 3: Nuevo empleado

```markdown
## Pretexting: Empleado nuevo

### Fase 1: Apertura
"[Sonrisa amable] Hola, soy nuevo aquí. Me asignaron 
a la oficina 301 pero no encuentro la sala de servidores."

### Fase 2: Conexión personal
"Es mi primer día y estoy un poco perdido. 
¿Podrías ayudarme?"

### Fase 3: Escalamiento
"También necesito acceso a la red. ¿Sabes quién 
me puede dar las credenciales?"

### Fase 4: Obtención de acceso
"¿Puedes abrirme la puerta del tercer piso? 
Necesito instalar un servidor."

### Fase 5: Escalamiento
"¿Dónde está el archivo de contraseñas? 
Necesito verificar la configuración."

### Respuestas a objeciones
- "¿Por qué no preguntas a RRHH?"
  → "Ya pregunté, pero me dijeron que fuera directo a TI. 
  Estoy un poco confundido."

- "¿Cuál es tu nombre?"
  → "Soy Carlos Mendoza. ¿Puedes verificar con RRHH 
  si estoy en el sistema?"

- "Necesito ver tu identificación"
  → "Claro, aquí está mi credencial de empleado."
```

---

## 4. Adaptación a culturas

### Cultura occidental (EEUU, Europa)

```markdown
# Características:
- Formal pero amigable
- Respeto por la jerarquía
- Enfoque en eficiencia
- Uso de nombres y cargos

# Ejemplo:
"Hello, I'm John from IT Support. We're conducting 
a security audit. Can you verify your credentials?"
```

### Cultura latina (Latinoamérica)

```markdown
# Características:
- Más informal y cercana
- Énfasis en relación personal
- Uso de diminutivos
- Respeto por la edad

# Ejemplo:
"Hola, buenas tardes. Soy Juan del departamento de TI. 
¿Me podrías ayudar con una cosita? Es una emergencia."
```

### Cultura asiática

```markdown
# Características:
- Extrema formalidad
- Respeto por la autoridad
- Evitar el conflicto
- Uso de títulos

# Ejemplo:
"Bonjour, je suis le Directeur de la Sécurité. 
Nous devons vérifier votre compte immédiatement."
```

---

## 5. Defensa y remediación

### Para Blue Team / Equipo de Seguridad

| Vector | Detección | Mitigación |
|---|---|---|
| **Pretexting por email** | Analizar headers, remitente | Entrenamiento, verificación |
| **Pretexting telefónico** | Verificar identidad del llamante | Políticas de verificación |
| **Pretexting presencial** | Pedir identificación | Badges, acceso controlado |
| **Urgencia artificial** | Cuestionar la urgencia | Políticas de verificación |

### Políticas de verificación

```markdown
## Política de Verificación de Identidad

1. NUNCA dar información sensible sin verificar
2. SIEMPRE pedir identificación oficial
3. SIEMPRE llamar al departamento para verificar
4. NUNCA ceder a presión o urgencia
5. SIEMPRE reportar intentos sospechosos
```

### Entrenamiento continuo

| Actividad | Frecuencia | Responsable |
|---|---|---|
| Simulacros de pretexting | Trimestral | Equipo de Seguridad |
| Entrenamiento en verificación | Mensual | RRHH + Seguridad |
| Evaluación de resultados | Post-simulacro | Management |

---

## 6. Referencias

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
# Prueba de Pretexting Corporativo — [Nombre de la empresa]

## Contexto
- Objetivo: Departamento de TI y RRHH
- Autorización: Firmada por CISO
- Duración: 2 semanas

## Pretextos utilizados
1. Soporte técnico de Microsoft (por teléfono)
2. Auditor de seguridad (presencial)
3. Nuevo empleado (presencial)

## Resultados
- Empleados contactados: 20
- Empleados que cedieron: 8 (40%)
- Información obtenida: Credenciales, acceso físico

## Análisis
- El 40% de los empleados cedió información
- La urgencia fue el factor principal de éxito
- Solo el 30% verificó la identidad del llamante

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

**[⬅ Principios del Pretexting](./01-pretexting-principios.md)** · **[⬅ Volver al módulo](../README.md)** · **[→ Vishing](./03-vishing.md)**
