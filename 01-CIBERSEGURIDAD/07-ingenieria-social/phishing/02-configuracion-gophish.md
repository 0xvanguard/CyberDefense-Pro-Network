# ⚙️ Configuración de Campañas en GoPhish

> *Este documento cubre la configuración paso a paso de campañas de phishing en GoPhish, desde la configuración inicial hasta el análisis de resultados.*

---

## 📋 Tabla de contenido

1. [Configuración inicial](#1-configuración-inicial)
2. [Crear plantillas de email](#2-crear-plantillas-de-email)
3. [Configurar landing pages](#3-configurar-landing-pages)
4. [Crear grupos de objetivos](#4-crear-grupos-de-objetivos)
5. [Ejecutar campañas](#5-ejecutar-campañas)
6. [Analizar resultados](#6-analizar-resultados)
7. [Buenas prácticas](#7-buenas-prácticas)
8. [Ejemplo completo](#8-ejemplo-completo)
9. [Referencias](#9-referencias)

---

## 1. Configuración inicial

### Primer login

1. Abrir `https://localhost:3333` en el navegador
2. Aceptar el certificado SSL auto-firmado
3. Login con las credenciales por defecto:
   - **Email:** admin@example.com
   - **Password:** gophish

4. **Cambiar contraseña inmediatamente**

### Configurar SMTP

```yaml
# Configurar servidor SMTP para enviar emails
# En la UI: Settings → Sending Profile

Host: smtp.gmail.com:587
Username: tu-email@gmail.com
Password: tu-password-de-app
From: IT Support <it-support@empresa.com>
```

### Gmail: configurar contraseña de aplicación

1. Ir a [https://myaccount.google.com/apppasswords](https://myaccount.google.com/apppasswords)
2. Crear nueva contraseña de aplicación
3. Usar esa contraseña en GoPhish

### Configurar dominio

```yaml
# Configurar dominio para URLs
# En la UI: Settings → General

URL: https://tudominio.com
# Esta URL se usará en los emails de phishing
```

---

## 2. Crear plantillas de email

### Tipos de plantillas

| Tipo | Objetivo | Ejemplo |
|---|---|---|
| **Urgencia** | Presionar para actuar rápido | "Tu cuenta será bloqueada en 24 horas" |
| **Curiosidad** | Despertar interés | "Han compartido un documento contigo" |
| **Autoridad** | Suplantar a superiores | "El CEO necesita esto urgentemente" |
| **Miedo** | Generar pánico | "Tu cuenta ha sido comprometida" |

### Crear plantilla

1. Ir a **Email Templates**
2. Click **Add Template**
3. Configurar:

| Campo | Valor |
|---|---|
| **Name** | Actualización de contraseña |
| **Subject** | ⚠️ Acción requerida: Actualiza tu contraseña |
| **From** | IT Support <it-support@empresa.com> |
| **HTML** | [Pegar HTML de la plantilla] |

### Variables disponibles

| Variable | Descripción |
|---|---|
| `{{.URL}}` | URL de rastreo única por destinatario |
| `{{.RId}}` | ID de rastreo único |
| `{{.From}}` | Nombre del remitente |
| `{{.Subject}}` | Asunto del email |
| `{{.FirstName}}` | Nombre del destinatario |
| `{{.LastName}}` | Apellido del destinatario |
| `{{.Email}}` | Email del destinatario |
| `{{.Position}}` | Cargo del destinatario |

### Ejemplo de plantilla

```html
Subject: Acción requerida: Actualiza tu contraseña

<div style="font-family: Arial, sans-serif; max-width: 600px; margin: 0 auto;">
  <div style="background-color: #f8f9fa; padding: 20px; border-bottom: 3px solid #dc3545;">
    <h2 style="color: #dc3545;">⚠️ Acción Requerida</h2>
  </div>
  
  <div style="padding: 20px;">
    <p>Estimado/a {{.FirstName}},</p>
    
    <p>Por motivos de seguridad, es necesario que actualices tu contraseña 
    antes del <strong>{{.Expires}}</strong>.</p>
    
    <p>Si no actualizas tu contraseña, tu cuenta será bloqueada temporalmente.</p>
    
    <a href="{{.URL}}" style="
      display: inline-block;
      background-color: #dc3545;
      color: white;
      padding: 12px 24px;
      text-decoration: none;
      border-radius: 4px;
      margin: 20px 0;
    ">Actualizar Contraseña</a>
    
    <p style="color: #6c757d; font-size: 12px;">
      Si no solicitaste este cambio, contacta al equipo de IT inmediatamente.
    </p>
  </div>
  
  <div style="background-color: #f8f9fa; padding: 10px; text-align: center; font-size: 11px;">
    © 2024 Empresa S.A. | Departamento de TI
  </div>
</div>
```

---

## 3. Configurar landing pages

### Crear landing page

1. Ir a **Landing Pages**
2. Click **Add Page**
3. Configurar:

| Campo | Valor |
|---|---|
| **Name** | Login corporativo |
| **HTML** | [Pegar HTML de la landing page] |
| **Redirect to** | https://www.google.com (redirigir después del login) |

### Variables en landing pages

| Variable | Descripción |
|---|---|
| `{{.URL}}` | URL de rastreo (enviar credenciales a GoPhish) |
| `{{.RId}}` | ID de rastreo único |

### Ejemplo de landing page

```html
<!-- Landing page: Login corporativo falso -->
<!DOCTYPE html>
<html>
<head>
  <title>Portal Corporativo - Login</title>
  <style>
    body {
      font-family: Arial, sans-serif;
      background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
      display: flex;
      justify-content: center;
      align-items: center;
      min-height: 100vh;
      margin: 0;
    }
    .login-box {
      background: white;
      padding: 40px;
      border-radius: 8px;
      box-shadow: 0 4px 6px rgba(0,0,0,0.1);
      width: 100%;
      max-width: 400px;
    }
    .logo {
      text-align: center;
      margin-bottom: 30px;
    }
    .form-group {
      margin-bottom: 20px;
    }
    label {
      display: block;
      margin-bottom: 5px;
      color: #333;
    }
    input {
      width: 100%;
      padding: 12px;
      border: 1px solid #ddd;
      border-radius: 4px;
      box-sizing: border-box;
    }
    button {
      width: 100%;
      padding: 12px;
      background-color: #667eea;
      color: white;
      border: none;
      border-radius: 4px;
      cursor: pointer;
      font-size: 16px;
    }
    button:hover {
      background-color: #5a6fd6;
    }
    .footer {
      text-align: center;
      margin-top: 20px;
      color: #666;
      font-size: 12px;
    }
  </style>
</head>
<body>
  <div class="login-box">
    <div class="logo">
      <h1>🏢 Portal Corporativo</h1>
    </div>
    
    <form action="{{.URL}}" method="POST">
      <div class="form-group">
        <label for="email">Correo Electrónico</label>
        <input type="email" id="email" name="email" required 
               placeholder="usuario@empresa.com">
      </div>
      
      <div class="form-group">
        <label for="password">Contraseña</label>
        <input type="password" id="password" name="password" required>
      </div>
      
      <button type="submit">Iniciar Sesión</button>
    </form>
    
    <div class="footer">
      <p>¿Olvidaste tu contraseña? Contacta a IT</p>
      <p>© 2024 Empresa S.A.</p>
    </div>
  </div>
</body>
</html>
```

---

## 4. Crear grupos de objetivos

### Formato CSV

```csv
Email,FirstName,LastName,Position
john.doe@empresa.com,John,Doe,Analista
jane.smith@empresa.com,Jane,Smith,Manager
bob.johnson@empresa.com,Bob,Johnson,Developer
```

### Importar en GoPhish

1. Ir a **Users & Groups**
2. Click **Add Group**
3. Configurar:

| Campo | Valor |
|---|---|
| **Name** | Empleados TI |
| **Import CSV** | [Seleccionar archivo CSV] |

4. Mapear columnas:
   - Email → Email
   - FirstName → First Name
   - LastName → Last Name
   - Position → Position

### Crear grupo manualmente

1. Ir a **Users & Groups**
2. Click **Add Group**
3. Click **Add User**
4. Completar campos:
   - Email: usuario@empresa.com
   - First Name: Juan
   - Last Name: Pérez
   - Position: Analista

---

## 5. Ejecutar campañas

### Crear campaña

1. Ir a **Campaigns**
2. Click **New Campaign**
3. Configurar:

| Campo | Valor |
|---|---|
| **Name** | Phishing Test Q1 2024 |
| **Email Template** | Plantilla de actualización contraseña |
| **Landing Page** | Login corporativo |
| **URL** | https://tudominio.com (debe ser accesible) |
| **Send Date** | Ahora o programar |
| **Groups** | Empleados TI |

4. Click **Send Campaign**

### URL pública

Para que los emails funcionen, necesitas una URL pública:
- **Opción 1:** Usar un servidor VPS (recomendado)
- **Opción 2:** Usar ngrok para exponer localmente

```bash
# Con ngrok
ngrok http 8080

# Usar la URL generada en GoPhish
# https://abc123.ngrok.io
```

### Programar campaña

```yaml
# En la UI: Campaigns → New Campaign → Send Date
# Seleccionar fecha y hora de envío

# Ejemplo: enviar lunes a las 9am
Send Date: 2024-01-15 09:00:00
```

---

## 6. Analizar resultados

### Métricas principales

| Métrica | Descripción | Meta típica |
|---|---|---|
| **Emails enviados** | Total de emails enviados | 100% |
| **Emails entregados** | Emails que llegaron al destinatario | >95% |
| **Emails abiertos** | Destinatarios que abrieron el email | 40-60% |
| **Clics** | Destinatarios que hicieron clic en el enlace | 10-30% |
| **Credenciales** | Destinatarios que enviaron credenciales | 5-15% |
| **Reportes** | Empleados que reportaron el phishing | >50% |

### Dashboard de GoPhish

```
📊 Resumen de Campaña: Phishing Test Q1 2024

Emails Enviados:     100
Emails Entregados:    98 (98%)
Emails Abiertos:      65 (65%)
Clics:                28 (28%)
Credenciales:         12 (12%)
Reportes:             15 (15%)
```

### Analizar por departamento

```bash
# Exportar datos y analizar
# GoPhish exporta resultados en CSV

# Ejemplo de análisis
cat results.csv | awk -F',' '{print $5}' | sort | uniq -c | sort -rn
```

### Exportar reporte

1. Ir a **Campaigns**
2. Seleccionar campaña
3. Click **Export**
4. Seleccionar formato (CSV, PDF)
5. Descargar reporte

---

## 7. Buenas prácticas

### Antes de la campaña

- [ ] **Obtener autorización escrita** del CISO o responsable
- [ ] **Definir objetivos** y métricas claras
- [ ] **Configurar SMTP** correctamente
- [ ] **Probar la landing page** en diferentes dispositivos
- [ ] **Verificar la URL** pública y certificado SSL
- [ ] **Preparar mensaje de comunicaciones** para empleados

### Durante la campaña

- [ ] **Monitorear resultados** en tiempo real
- [ ] **Verificar que los emails se entregan** correctamente
- [ ] **Responder a consultas** de empleados
- [ ] **Documentar hallazgos** importantes

### Después de la campaña

- [ ] **Analizar resultados** por departamento
- [ ] **Identificar áreas de mejora**
- [ ] **Preparar reporte ejecutivo**
- [ ] **Comunicar resultados** a la dirección
- [ ] **Planificar próxima campaña**

### Frecuencia recomendada

| Actividad | Frecuencia |
|---|---|
| Campañas de phishing | Mensual |
| Entrenamiento interactivo | Trimestral |
| Evaluación de resultados | Post-campaña |
| Simulacros avanzados | Semestral |

---

## 8. Ejemplo completo

### Campaña: Phishing de Microsoft 365

```markdown
## 1. Configuración inicial
- SMTP: smtp.gmail.com:587
- URL: https://login-empresa.com
- SSL: Let's Encrypt

## 2. Plantilla de email
- Asunto: ⚠️ Acción requerida: Actualiza tu contraseña
- Remitente: IT Support <it-support@empresa.com>
- Contenido: Urgencia + enlace a landing page

## 3. Landing page
- Template: Microsoft 365 Login
- URL: https://login-empresa.com
- Redirección: https://www.microsoft.com

## 4. Grupo de objetivos
- 100 empleados del departamento de TI
- CSV con email, nombre, apellido, cargo

## 5. Ejecución
- Fecha: Lunes 9:00 AM
- Duración: 1 semana
- Monitoreo: Dashboard de GoPhish

## 6. Resultados
- Emails enviados: 100
- Emails abiertos: 65 (65%)
- Clics: 28 (28%)
- Credenciales: 12 (12%)
- Reportes: 15 (15%)

## 7. Análisis
- Departamento con más caídas: Desarrollo (8 de 12)
- Factor principal: Urgencia
- Tiempo promedio de clic: 5 minutos

## 8. Recomendaciones
1. Implementar MFA en Microsoft 365
2. Entrenamiento trimestral en detección de phishing
3. Crear proceso de reporte fácil
4. Bloquear dominios similares
```

---

## 9. Referencias

### Fuentes primarias

| Recurso | URL |
|---|---|
| **GoPhish Official** | [https://getgophish.com](https://getgophish.com) |
| **GoPhish Documentation** | [https://docs.getgophish.com](https://docs.getgophish.com) |
| **MITRE ATT&CK — Phishing** | [https://attack.mitre.org/techniques/T1566/](https://attack.mitre.org/techniques/T1566/) |
| **NIST SP 800-177** | Trustworthy Email |

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
# Configuración de Campaña de Phishing — [Nombre de la empresa]

## Contexto
- Objetivo: 100 empleados del departamento de TI
- Herramienta: GoPhish
- Duración: 1 semana

## Configuración
- SMTP: smtp.gmail.com:587
- URL: https://login-empresa.com
- SSL: Let's Encrypt

## Plantilla de email
- Asunto: ⚠️ Acción requerida: Actualiza tu contraseña
- Remitente: IT Support <it-support@empresa.com>
- Contenido: Urgencia + enlace a landing page

## Landing page
- Template: Microsoft 365 Login
- URL: https://login-empresa.com
- Redirección: https://www.microsoft.com

## Grupo de objetivos
- 100 empleados del departamento de TI
- CSV con email, nombre, apellido, cargo

## Resultados
- Emails enviados: 100
- Emails abiertos: 65 (65%)
- Clics: 28 (28%)
- Credenciales: 12 (12%)
- Reportes: 15 (15%)

## Análisis
- Departamento con más caídas: Desarrollo (8 de 12)
- Factor principal: Urgencia
- Tiempo promedio de clic: 5 minutos

## Recomendaciones
1. Implementar MFA en Microsoft 365
2. Entrenamiento trimestral en detección de phishing
3. Crear proceso de reporte fácil
4. Bloquear dominios similares

## Evidencia
- Dashboard de GoPhish: [enlace]
- Reporte exportado: [enlace]
- Screenshot: [enlace]
```

---

**[⬅ Landing pages](./01-landings-phishing.md)** · **[⬅ Volver al módulo](../README.md)** · **[→ Medidas de defensa](./03-medidas-defensa.md)**
