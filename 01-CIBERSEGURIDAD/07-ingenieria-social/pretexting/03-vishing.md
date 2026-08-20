# 📞 Vishing — Voice Phishing

> *Vishing es la ingeniería social por teléfono. Los atacantes usan llamadas telefónicas para manipular a las víctimas y obtener información sensible. Este documento cubre técnicas, scripts y defensa.*

---

## 📋 Tabla de contenido

1. [Qué es el vishing](#1-qué-es-el-vishing)
2. [Técnicas de vishing](#2-técnicas-de-vishing)
3. [Scripts de vishing](#3-scripts-de-vishing)
4. [Herramientas para vishing](#4-herramientas-para-vishing)
5. [Ejemplos reales](#5-ejemplos-reales)
6. [Defensa y remediación](#6-defensa-y-remediación)
7. [Referencias](#7-referencias)

---

## 1. Qué es el vishing

Vishing (voice + phishing) es el uso del teléfono para:
- **Obtener credenciales** de usuarios
- **Suplantar identidades** de empresas o personas
- **Manipular emociones** para que la víctima actúe
- **Obtener acceso** a sistemas o información

### Comparativa con otras técnicas

| Técnica | Vector | Ventaja para el atacante |
|---|---|---|
| **Phishing** | Email | Alcance masivo |
| **Vishing** | Teléfono | Interacción en tiempo real |
| **Pretexting** | Cualquier medio | Escenario elaborado |
| **Smishing** | SMS | Acceso inmediato al teléfono |

### ¿Por qué funciona el vishing?

1. **Urgencia:** El teléfono crea presión inmediata
2. **Autoridad:** Una voz confiante impone respeto
3. **Emociones:** Miedo, curiosidad o empatía se manipulan fácilmente
4. **Verificación:** Es más difícil verificar identidad por teléfono

---

## 2. Técnicas de vishing

### Técnica 1: Urgencia artificial

```markdown
# Crear presión para que la víctima actúe rápido

"Hay un problema urgente con tu cuenta. Si no lo resolvemos 
en los próximos 15 minutos, tu cuenta será bloqueada."
```

### Técnica 2: Autoridad falsa

```markdown
# Usar un cargo o nombre que dé autoridad

"Soy el director de TI de la empresa. El CEO me pidió 
que verificara todas las cuentas de forma inmediata."
```

### Técnica 3: Miedo

```markdown
# Generar pánico para que la víctima actúe sin pensar

"Hemos detectado que tu cuenta ha sido comprometida. 
Hay actividad sospechosa desde Rusia. Necesitamos 
verificar tu identidad inmediatamente."
```

### Técnica 4: Empatía

```markdown
# Crear una conexión emocional

"Entiendo que estás ocupado. Solo necesito 2 minutos 
para verificar tu cuenta. Sé que no es conveniente, 
pero es urgente."
```

### Técnica 5: Prueba social

```markdown
# Usar la presión social

"Todos los demás departamentos ya completaron la verificación. 
Solo falta tu departamento. ¿Podemos hacerlo ahora?"
```

### Técnica 6: Reciprocidad

```markdown
# Crear una obligación de devolver favores

"Te ayudé la semana pasada con tu laptop, ¿recuerdas? 
Necesito que me des acceso a tu cuenta para verificar 
una configuración."
```

---

## 3. Scripts de vishing

### Script 1: Soporte técnico

```markdown
## Vishing: Soporte técnico de Microsoft

### Apertura
"Buenos días, soy Juan del soporte técnico de Microsoft. 
¿Puedo hablar con el titular de esta cuenta?"

### Verificación (falsa)
"Para verificar que eres el titular, ¿cuál es tu 
correo electrónico completo?"

### Urgencia
"Hemos detectado actividad sospechosa en tu cuenta. 
Hay un intento de acceso desde Rusia. Necesitamos 
verificar tu identidad inmediatamente."

### Obtención de credenciales
"¿Puedes confirmarme tu contraseña para verificar 
que no estás comprometido?"

### Escalamiento
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

### Script 2: Banco

```markdown
## Vishing: Banco falso

### Apertura
"Hola, soy María del departamento de seguridad del Banco. 
¿Puedo hablar con el titular de la cuenta?"

### Verificación (falsa)
"Para verificar tu identidad, ¿cuál es tu número de cuenta?"

### Urgencia
"Hemos detectado actividad sospechosa en tu cuenta bancaria. 
Hay un intento de transferencia no autorizado."

### Obtención de credenciales
"¿Puedes confirmarme tu contraseña para verificar 
que no estás comprometido?"

### Obtención de dinero
"Necesitamos transferir tu saldo a una cuenta segura 
temporalmente. ¿Puedes darme los datos de tu cuenta?"
```

### Script 3: IT interno

```markdown
## Vishing: IT interno

### Apertura
"Hola, soy el nuevo técnico de TI. Me asignaron 
al proyecto de migración."

### Conexión personal
"Es mi primer día y estoy un poco perdido. 
¿Podrías ayudarme?"

### Obtención de acceso
"Necesito acceso al servidor de producción para 
verificar la configuración. ¿Puedes darme las credenciales?"

### Escalamiento
"También necesito acceso a la red de los clientes. 
¿Dónde está el archivo de contraseñas?"
```

### Script 4: Auditoría

```markdown
## Vishing: Auditoría de seguridad

### Apertura
"Hola, soy el auditor de seguridad de la empresa. 
Estamos realizando una auditoría inesperada de acceso."

### Verificación (falsa)
"¿Puedes confirmarme tu usuario para verificar que 
estás en la lista de auditados?"

### Urgencia
"La auditoría debe completarse antes de las 5 pm. 
Si no verificamos tu acceso, será un hallazgo crítico."

### Obtención de credenciales
"¿Puedes confirmarme tu contraseña para verificar 
que tienes los permisos correctos?"
```

---

## 4. Herramientas para vishing

### Spoofing de número

```bash
# Con Twilio (para pruebas autorizadas)
# https://www.twilio.com/docs/usage/api/caller-id

# Con SipVicious (para pentesting)
# https://github.com/EnableSecurity/sipvicious

# Configurar caller ID
svcroute -s 10.10.14.5 -d 5551234567 --caller-id "5559876543"
```

### Grabación de llamadas

```bash
# Con Asterisk
# Configurar grabación automática
# /etc/asterisk/extensions.conf

exten => _X.,1,Answer()
same => n,Monitor(wav)
same => n,Dial(SIP/${EXTEN})
same => n,Hangup()
```

### Herramientas de scripting

```bash
# Con Python y Twilio
from twilio.rest import Client

client = Client("account_sid", "auth_token")

call = client.calls.create(
    to="+1234567890",
    from_="+0987654321",
    url="http://tudominio.com/script.xml"
)

print(call.sid)
```

### Scripts XML para Twilio

```xml
<?xml version="1.0" encoding="UTF-8"?>
<Response>
  <Say voice="alice">
    Hola, soy Juan del soporte técnico de Microsoft. 
    Hemos detectado actividad sospechosa en tu cuenta.
    Por favor, presiona 1 para verificar tu identidad.
  </Say>
  <Gather numDigits="1" action="/verify">
    <Say>Presiona 1 para continuar</Say>
  </Gather>
</Response>
```

---

## 5. Ejemplos reales

### Ejemplo 1: Ataque a empresa de tecnología

```markdown
## Caso real (anonimizado)

### Escenario
Atacante llama haciéndose pasar por soporte de Microsoft

### Desarrollo
1. Llama al departamento de TI
2. Se identifica como soporte de Microsoft
3. Dice que hay actividad sospechosa en cuentas
4. Pide credenciales para verificar

### Resultado
- 3 empleados entregaron credenciales
- Atacante accedió a 15 cuentas de Microsoft 365
- Se robaron datos de 500 clientes

### Lecciones aprendidas
- Falta de entrenamiento en verificación
- No hay política de "nunca dar credenciales por teléfono"
- No hay monitoreo de accesos anómalos
```

### Ejemplo 2: Ataque a banco

```markdown
## Caso real (anonimizado)

### Escenario
Atacante llama haciéndose pasar por banco

### Desarrollo
1. Llama a clientes del banco
2. Dice que hay actividad sospechosa
3. Pide credenciales para verificar
4. Transfiere dinero a cuentas externas

### Resultado
- 20 clientes fueron víctimas
- Se transfirieron $50,000 USD
- El banco fue multado por no proteger a clientes

### Lecciones aprendidas
- Los bancos nunca piden credenciales por teléfono
- Verificar siempre con el banco directamente
- Usar aplicaciones oficiales para verificar
```

### Ejemplo 3: Ataque a empresa de seguros

```markdown
## Caso real (anonimizado)

### Escenario
Atacante llama haciéndose pasar por auditor

### Desarrollo
1. Llama al departamento de TI
2. Se identifica como auditor de seguridad
3. Dice que hay una auditoría inesperada
4. Pide credenciales para verificar

### Resultado
- 2 técnicos entregaron credenciales
- Atacante accedió a sistemas de producción
- Se robaron datos de 10,000 clientes

### Lecciones aprendidas
- Los auditores nunca piden credenciales
- Verificar siempre con el departamento de auditoría
- Usar credenciales de auditoría dedicadas
```

---

## 6. Defensa y remediación

### Para Blue Team / Equipo de Seguridad

| Vector | Detección | Mitigación |
|---|---|---|
| **Vishing por teléfono** | Verificar identidad del llamante | Políticas de verificación |
| **Spoofing de número** | Monitorear llamadas sospechosas | Bloquear números desconocidos |
| **Urgencia artificial** | Cuestionar la urgencia | Políticas de verificación |
| **Suplantación de autoridad** | Verificar con el departamento | Procesos de verificación |

### Políticas de verificación

```markdown
## Política de Verificación Telefónica

1. NUNCA dar información sensible por teléfono
2. SIEMPRE colgar y llamar al número oficial
3. SIEMPRE verificar con el departamento
4. NUNCA ceder a presión o urgencia
5. SIEMPRE reportar intentos sospechosos
```

### Entrenamiento continuo

| Actividad | Frecuencia | Responsable |
|---|---|---|
| Simulacros de vishing | Trimestral | Equipo de Seguridad |
| Entrenamiento en verificación | Mensual | RRHH + Seguridad |
| Evaluación de resultados | Post-simulacro | Management |

### Herramientas de detección

```bash
# Monitorear llamadas sospechosas
# Configurar Asterisk para detectar caller ID falso

# Usar servicios de verificación
# Twilio Lookup API para verificar números

# Bloquear números conocidos de estafa
# Configurar firewall de voz
```

---

## 7. Referencias

### Fuentes primarias

| Recurso | URL |
|---|---|
| **MITRE ATT&CK — Vishing** | [https://attack.mitre.org/techniques/T1598/001/](https://attack.mitre.org/techniques/T1598/001/) |
| **NIST SP 800-50** | Building an IT Security Awareness Program |
| **SANS Security Awareness** | [https://www.sans.org/security-awareness-training/](https://www.sans.org/security-awareness-training/) |
| **FTC - Vishing** | [https://www.consumer.ftc.gov/articles/how-spot-avoid-and-report-fake-phishing-scams](https://www.consumer.ftc.gov/articles/how-spot-avoid-and-report-fake-phishing-scams) |

### Frameworks de referencia

| Framework | Uso |
|---|---|
| **MITRE ATT&CK** | Tácticas y técnicas de adversarios |
| **NIST CSF** | Marco de seguridad |
| **ISO 27001** | Gestión de seguridad |

---

## 📝 Entregable de portafolio

```markdown
# Prueba de Vishing — [Nombre de la empresa]

## Contexto
- Objetivo: Departamento de TI y finanzas
- Autorización: Firmada por CISO
- Duración: 1 semana

## Técnicas utilizadas
1. Soporte técnico de Microsoft (urgencia)
2. Auditor de seguridad (autoridad)
3. Banco falso (miedo)

## Resultados
- Empleados contactados: 15
- Empleados que cedieron: 5 (33%)
- Información obtenida: Credenciales, datos financieros

## Análisis
- El 33% de los empleados cedió información
- La urgencia fue el factor principal de éxito
- Solo el 20% verificó la identidad del llamante

## Recomendaciones
1. Entrenamiento en verificación telefónica
2. Política de "nunca dar credenciales por teléfono"
3. Proceso de verificación con supervisor
4. Simulacros trimestrales

## Evidencia
- Autorización firmada: [enlace]
- Grabaciones (anonimizadas): [enlace]
- Reporte: [enlace]
```

---

**[⬅ Pretextos corporativos](./02-pretextos-corporativos.md)** · **[⬅ Volver al módulo](../README.md)** · **[→ Phishing](../phishing/01-landings-phishing.md)**
