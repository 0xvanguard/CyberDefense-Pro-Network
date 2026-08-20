# 🛡️ Medidas de Defensa contra Phishing

> *La defensa contra phishing requiere un enfoque múltiple: tecnología, procesos y personas. Este documento cubre las mejores prácticas para prevenir, detectar y responder a ataques de phishing.*

---

## 📋 Tabla de contenido

1. [Defensa en capas](#1-defensa-en-capas)
2. [Medidas técnicas](#2-medidas-técnicas)
3. [Medidas de proceso](#3-medidas-de-proceso)
4. [Medidas de persona](#4-medidas-de-persona)
5. [Detección y respuesta](#5-detección-y-respuesta)
6. [Herramientas de defensa](#6-herramientas-de-defensa)
7. [Buenas prácticas](#7-buenas-prácticas)
8. [Referencias](#8-referencias)

---

## 1. Defensa en capas

### Modelo de defensa

```
┌─────────────────────────────────────────────────────┐
│                    PERSONAS                          │
│  Entrenamiento, concientización, reporte            │
├─────────────────────────────────────────────────────┤
│                   PROCESOS                          │
│  Políticas, procedimientos, verificación            │
├─────────────────────────────────────────────────────┤
│                  TECNOLOGÍA                         │
│  Email filters, MFA, monitoring                     │
└─────────────────────────────────────────────────────┘
```

### Por qué defensa en capas

- **Ninguna medida es 100% efectiva** por sí sola
- **Los atacantes evolucionan** constantemente
- **Los errores humanos** son inevitables
- **Múltiples capas** aumentan la dificultad del atacante

---

## 2. Medidas técnicas

### Email filtering

```yaml
# Configurar filtros de email
# Microsoft 365: Exchange Online Protection (EOP)
# Google Workspace: Google Admin Console

# Filtros recomendados:
- Spam filtering: High
- Phishing protection: Enabled
- Safe Links: Enabled
- Safe Attachments: Enabled
- Anti-spoofing: Enabled
```

### DMARC/DKIM/SPF

```dns
# SPF (en DNS del dominio)
# Verificar que solo los servidores autorizados envían emails
v=spf1 include:_spf.google.com include:spf.protection.outlook.com ~all

# DKIM (configurar en Google Admin / Microsoft 365)
# Firma digital de emails para verificar autenticidad
selector._domainkey.empresa.com. IN TXT "v=DKIM1; k=rsa; p=MIIBI..."

# DMARC
# Política de manejo de emails fallidos
_dmarc.empresa.com. IN TXT "v=DMARC1; p=quarantine; rua=mailto:dmarc@empresa.com; pct=100"
```

### MFA (Multi-Factor Authentication)

```yaml
# Implementar MFA en todos los sistemas críticos
# Microsoft 365: Azure AD MFA
# Google Workspace: Google 2-Step Verification

# Métodos recomendados (en orden de seguridad):
1. FIDO2 / Hardware tokens (YubiKey)
2. Authenticator apps (Google Authenticator, Authy)
3. SMS (menos seguro, evitar si es posible)
```

### Password managers

```yaml
# Implementar password manager corporativo
# Herramientas recomendadas:
- 1Password Business
- LastPass Enterprise
- Bitwarden Enterprise

# Beneficios:
- Detectan sitios de phishing automáticamente
- No autofill en dominios sospechosos
- Generan contraseñas seguras
```

### Browser security

```yaml
# Configurar navegador corporativo
- Safe Browsing: Enabled
- Phishing protection: Enabled
- Extensions: Bloquear extensiones no autorizadas
- Updates: Automáticos
```

---

## 3. Medidas de proceso

### Políticas de seguridad

```markdown
## Política de Seguridad de Email

1. NUNCA abrir adjuntos de remitentes desconocidos
2. NUNCA hacer clic en enlaces de emails sospechosos
3. SIEMPRE verificar el remitente antes de responder
4. SIEMPRE reportar emails sospechosos
5. NUNCA enviar credenciales por email
```

### Procedimiento de verificación

```markdown
## Procedimiento de Verificación de Email Sospechoso

1. NO hacer clic en ningún enlace
2. NO abrir adjuntos
3. Verificar remitente real (no solo el nombre)
4. Verificar URLs sin hacer clic (hover)
5. Reportar al equipo de seguridad
6. Si se hizo clic, cambiar contraseña inmediatamente
```

### Proceso de reporte

```markdown
## Proceso de Reporte de Phishing

1. Identificar email sospechoso
2. No eliminar el email
3. Reportar using:
   - Botón "Report phishing" en Outlook/Gmail
   - Email a seguridad@empresa.com
   - Formulario web de reporte
4. Proporcionar:
   - Screenshot del email
   - Headers del email
   - Descripción de lo que se hizo (si se hizo clic)
```

---

## 4. Medidas de persona

### Entrenamiento continuo

| Actividad | Frecuencia | Duración | Responsable |
|---|---|---|---|
| Campañas de phishing | Mensual | 1 día | Equipo de Seguridad |
| Entrenamiento interactivo | Trimestral | 1 hora | RRHH + Seguridad |
| Simulacros avanzados | Semestral | 1 semana | Equipo de Seguridad |
| Evaluación de resultados | Post-campaña | 1 día | Management |

### Contenido del entrenamiento

```markdown
## Temas de entrenamiento

1. **Identificar phishing:**
   - Remitente sospechoso
   - Urgencia artificial
   - Errores ortográficos
   - URLs sospechosas

2. **Reportar phishing:**
   - Cómo reportar
   - Qué información incluir
   - Qué hacer después

3. **Respuesta a incidentes:**
   - Qué hacer si se hizo clic
   - Cómo cambiar contraseñas
   - A quién reportar
```

### Gamificación

```markdown
## Programa de Gamificación

1. **Puntos por reportar:**
   - Email phishing reportado: 10 puntos
   - Phishing detectado antes de clic: 20 puntos
   - Reporte completo con evidencia: 30 puntos

2. **Recompensas:**
   - 100 puntos: Gift card de $10
   - 500 puntos: Día libre
   - 1000 puntos: Reconocimiento público

3. **Ranking mensual:**
   - Top 3: Reconocimiento + recompensa
   - Peor departamento: Entrenamiento adicional
```

---

## 5. Detección y respuesta

### Monitoreo activo

```yaml
# Configurar monitoreo de phishing
# Herramientas:
- Microsoft Defender for Office 365
- Google Workspace Security
- Proofpoint
- Mimecast

# Alertas configuradas:
- Email phishing detectado
- Clic en enlace sospechoso
- Credenciales comprometidas
- Login anómalo
```

### Respuesta a incidentes

```markdown
## Procedimiento de Respuesta a Phishing

### Fase 1: Detección
1. Alerta de sistema o reporte de usuario
2. Verificar si es phishing real
3. Clasificar por severidad

### Fase 2: Contención
1. Bloquear email en todos los buzones
2. Bloquear dominio/URL malicioso
3. Revocar sesiones comprometidas
4. Cambiar credenciales comprometidas

### Fase 3: Erradicación
1. Eliminar email de todos los buzones
2. Bloquear remitente
3. Actualizar reglas de filtrado
4. Escanear sistemas comprometidos

### Fase 4: Recuperación
1. Restaurar servicios afectados
2. Verificar integridad de datos
3. Comunicar a empleados afectados
4. Documentar lecciones aprendidas

### Fase 5: Lecciones aprendidas
1. Analizar qué falló
2. Actualizar procedimientos
3. Implementar mejoras
4. Entrenar a empleados
```

---

## 6. Herramientas de defensa

### Email security

| Herramienta | Uso |
|---|---|
| **Microsoft Defender** | Protección de email en Microsoft 365 |
| **Google Workspace** | Protección de email en Google |
| **Proofpoint** | Email security avanzado |
| **Mimecast** | Email security y archivado |

### Phishing detection

| Herramienta | Uso |
|---|---|
| **PhishTank** | Base de datos de phishing |
| **URLScan.io** | Análisis de URLs |
| **VirusTotal** | Análisis de archivos y URLs |
| **Google Safe Browsing** | Detección de sitios maliciosos |

### Security awareness

| Herramienta | Uso |
|---|---|
| **GoPhish** | Campañas de phishing simulado |
| **KnowBe4** | Plataforma de entrenamiento |
| **Proofpoint Security Awareness** | Entrenamiento interactivo |
| **SANS Security Awareness** | Contenido de entrenamiento |

---

## 7. Buenas prácticas

### Para administradores

```markdown
## Checklist de seguridad de email

- [ ] DMARC configurado y en modo quarantine/reject
- [ ] DKIM configurado y funcionando
- [ ] SPF configurado correctamente
- [ ] MFA habilitado para todos los usuarios
- [ ] Filtros de email configurados
- [ ] Safe Links habilitado
- [ ] Safe Attachments habilitado
- [ ] Monitoreo de phishing activo
- [ ] Procedimiento de respuesta documentado
- [ ] Entrenamiento continuo programado
```

### Para usuarios

```markdown
## Checklist de usuario seguro

- [ ] No hacer clic en enlaces sospechosos
- [ ] Verificar remitente antes de responder
- [ ] No abrir adjuntos de desconocidos
- [ ] Reportar emails sospechosos
- [ ] Usar password manager
- [ ] Habilitar MFA en cuentas personales
- [ ] Mantener software actualizado
- [ ] No enviar credenciales por email
```

### Métricas de éxito

| Métrica | Objetivo |
|---|---|
| **Tasa de clics en phishing** | < 5% |
| **Tasa de reporte** | > 50% |
| **Tiempo de respuesta** | < 1 hora |
| **Empleados entrenados** | 100% |
| **MFA habilitado** | 100% |

---

## 8. Referencias

### Fuentes primarias

| Recurso | URL |
|---|---|
| **NIST SP 800-177** | Trustworthy Email |
| **MITRE ATT&CK — Phishing** | [https://attack.mitre.org/techniques/T1566/](https://attack.mitre.org/techniques/T1566/) |
| **CISA Phishing Guide** | [https://www.cisa.gov/phishing](https://www.cisa.gov/phishing) |
| **SANS Security Awareness** | [https://www.sans.org/security-awareness-training/](https://www.sans.org/security-awareness-training/) |

### Frameworks de referencia

| Framework | Uso |
|---|---|
| **MITRE ATT&CK** | Tácticas y técnicas de adversarios |
| **NIST CSF** | Marco de seguridad |
| **ISO 27001** | Gestión de seguridad |
| **PCI-DSS** | Requisitos de seguridad de datos |

---

## 📝 Entregable de portafolio

```markdown
# Medidas de Defensa contra Phishing — [Nombre de la empresa]

## Contexto
- Objetivo: Reducir tasa de clics en phishing
- Duración: 6 meses
- Resultado: Reducción del 35% al 5%

## Medidas implementadas

### Técnicas
- DMARC/DKIM/SPF configurado
- MFA habilitado para todos los usuarios
- Filtros de email avanzados
- Password manager corporativo

### Procesos
- Procedimiento de verificación documentado
- Proceso de reporte de phishing
- Respuesta a incidentes documentada

### Personas
- Entrenamiento mensual
- Gamificación del programa
- Simulacros trimestrales

## Resultados
- Tasa de clics: 35% → 5% (reducción del 86%)
- Tasa de reporte: 15% → 65% (aumento del 333%)
- Tiempo de respuesta: 24h → 1h (reducción del 96%)

## Lecciones aprendidas
1. La tecnología no es suficiente sin personas
2. El entrenamiento continuo es clave
3. La gamificación aumenta la participación
4. Los procesos claros reducen la confusión

## Evidencia
- Dashboard de métricas: [enlace]
- Reporte ejecutivo: [enlace]
- Screenshot de mejoras: [enlace]
```

---

**[⬅ Configurar campaña](./02-configuracion-gophish.md)** · **[⬅ Volver al módulo](../README.md)**
