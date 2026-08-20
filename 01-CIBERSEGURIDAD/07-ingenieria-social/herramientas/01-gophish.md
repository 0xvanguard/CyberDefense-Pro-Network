# 🎣 GoPhish — Framework de Phishing Simulado

> *GoPhish es la herramienta de código abierto más utilizada para campañas de phishing educativas y de prueba. Permite crear, ejecutar y rastrear campañas completas con reportes profesionales.*

---

## 📋 Tabla de contenido

1. [Qué es GoPhish](#1-qué-es-gophish)
2. [Instalación](#2-instalación)
3. [Configuración inicial](#3-configuración-inicial)
4. [Crear plantillas de email](#4-crear-plantillas-de-email)
5. [Configurar landing pages](#5-configurar-landing-pages)
6. [Crear grupos de objetivos](#6-crear-grupos-de-objetivos)
7. [Ejecutar una campaña](#7-ejecutar-una-campaña)
8. [Analizar resultados](#8-analizar-resultados)
9. [Ejemplo completo paso a paso](#9-ejemplo-completo-paso-a-paso)
10. [Defensa y remediación](#10-defensa-y-remediación)
11. [Referencias](#11-referencias)

---

## 1. Qué es GoPhish

GoPhish es un framework de código abierto diseñado para:
- **Campañas de phishing simulado** para concientización de seguridad
- **Entrenamiento de empleados** en detección de phishing
- **Medición de la efectividad** de programas de seguridad humana
- **Generación de reportes** profesionales para auditorías

### Características principales

| Característica | Descripción |
|---|---|
| **Templates de email** | Crear emails de phishing personalizados |
| **Landing pages** | Páginas de login falsas para capturar credenciales |
| **Rastreo** | Monitorear aperturas, clics y envíos de credenciales |
| **Reportes** | Dashboards con métricas detalladas |
| **API** | Integración con otros sistemas |

### Casos de uso legítimos

| Caso | Descripción |
|---|---|
| **Concientización** | Enseñar a empleados a detectar phishing |
| **Auditoría** | Evaluar la postura de seguridad humana |
| **Compliance** | Cumplir requisitos de entrenamiento (PCI-DSS, ISO 27001) |
| **Medición** | Demostrar ROI del programa de seguridad |

---

## 2. Instalación

### Desde binario

```bash
# Descargar la última versión
wget https://github.com/gophish/gophish/releases/latest/download/gophish-linux-amd64.zip

# Descomprimir
unzip gophish-linux-amd64.zip
chmod +x gophish

# Ejecutar
./gophish
```

### Desde Docker

```bash
# Crear directorio de datos
mkdir -p gophish-data

# Ejecutar
docker run -d \
  --name gophish \
  -p 3333:3333 \
  -p 8080:8080 \
  -v $(pwd)/gophish-data:/opt/gophish \
  -e GOPHISH_ADMIN_PASSWORD=your-secure-password \
  gophish/gophish:latest
```

### Puertos

| Puerto | Servicio | Descripción |
|---|---|---|
| **3333** | Admin UI | Interfaz de administración |
| **8080** | SMTP | Servidor de envío de emails |
| **80** | Landing pages | Páginas de phishing (opcional) |

---

## 3. Configuración inicial

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

---

## 4. Crear plantillas de email

### Tipos de plantillas

| Tipo | Objetivo | Ejemplo |
|---|---|---|
| **Urgencia** | Presionar para actuar rápido | "Tu cuenta será bloqueada en 24 horas" |
| **Curiosidad** | Despertar interés | "Han compartido un documento contigo" |
| **Autoridad** | Suplantar a superiores | "El CEO necesita esto urgentemente" |
| **Miedo** | Generar pánico | "Tu cuenta ha sido comprometida" |

### Crear plantilla

```html
<!-- Plantilla de phishing: Actualización de contraseña -->
Subject: Acción requerida: Actualiza tu contraseña

<div style="font-family: Arial, sans-serif; max-width: 600px; margin: 0 auto;">
  <div style="background-color: #f8f9fa; padding: 20px; border-bottom: 3px solid #dc3545;">
    <h2 style="color: #dc3545;">⚠️ Acción Requerida</h2>
  </div>
  
  <div style="padding: 20px;">
    <p>Estimado empleado,</p>
    
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

### Variables disponibles en GoPhish

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

---

## 5. Configurar landing pages

### Landing page de login

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

### Variables en landing pages

| Variable | Descripción |
|---|---|
| `{{.URL}}` | URL de rastreo (enviar credenciales a GoPhish) |
| `{{.RId}}` | ID de rastreo único |

---

## 6. Crear grupos de objetivos

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
3. Nombre: "Empleados TI"
4. Importar CSV
5. Mapear columnas

---

## 7. Ejjecutar una campaña

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

---

## 8. Analizar resultados

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

---

## 9. Ejemplo completo paso a paso

### Escenario: Campaña de concientización para empresa de 50 empleados

```bash
# 1. Instalar GoPhish
wget https://github.com/gophish/gophish/releases/latest/download/gophish-linux-amd64.zip
unzip gophish-linux-amd64.zip
chmod +x gophish
./gophish

# 2. Configurar SMTP (Gmail)
# Settings → Sending Profile → Add
# Host: smtp.gmail.com:587
# Username: seguridad@empresa.com
# Password: [contraseña de aplicación]

# 3. Crear plantilla de email
# Email Templates → Add
# Nombre: "Actualización de Contraseña"
# Asunto: "⚠️ Acción requerida: Actualiza tu contraseña"
# [Pegar HTML de la plantilla]

# 4. Crear landing page
# Landing Pages → Add
# Nombre: "Login Corporativo"
# [Pegar HTML de landing page]

# 5. Crear grupo de objetivos
# Users & Groups → Add Group
# Nombre: "Empleados TI"
# Importar CSV con 50 empleados

# 6. Ejecutar campaña
# Campaigns → New Campaign
# Configurar y enviar

# 7. Esperar 24-48 horas

# 8. Analizar resultados
# Campaigns → Ver métricas
# Exportar reporte para auditoría
```

---

## 10. Defensa y remediación

### Para Blue Team / Equipo de Seguridad

| Vector | Detección | Mitigación |
|---|---|---|
| **Email de phishing** | Analizar headers, remitente, URLs | DMARC, DKIM, SPF |
| **Landing page** | Verificar URLs, certificados SSL | MFA, password managers |
| **Credenciales comprometidas** | Monitorear logins anómalos | Alertas de geolocalización |
| **Empleados que caen** | Campañas de concientización | Entrenamiento regular |

### Configurar DMARC/DKIM/SPF

```dns
# SPF (en DNS del dominio)
v=spf1 include:_spf.google.com ~all

# DKIM (configurar en Google Admin)
# Domain Keys → Generate

# DMARC
_dmarc.empresa.com. IN TXT "v=DMARC1; p=quarantine; rua=mailto:dmarc@empresa.com"
```

### Entrenamiento continuo

| Actividad | Frecuencia | Responsable |
|---|---|---|
| Campañas de phishing | Mensual | Equipo de Seguridad |
| Entrenamiento interactivo | Trimestral | RRHH + Seguridad |
| Simulacros de incidente | Semestral | Equipo de Seguridad |
| Evaluación de resultados | Post-campaña | Management |

---

## 11. Referencias

### Fuentes primarias

| Recurso | URL |
|---|---|
| **GoPhish Official** | [https://getgophish.com](https://getgophish.com) |
| **GoPhish GitHub** | [https://github.com/gophish/gophish](https://github.com/gophish/gophish) |
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
# Campaña de Phishing Simulado — [Nombre de la empresa]

## Contexto
- Objetivo: 50 empleados del departamento de TI
- Herramienta: GoPhish
- Duración: 2 semanas

## Diseño de la campaña
- Tipo: Actualización de contraseña
- Urgencia: 24 horas
- Landing page: Login corporativo falso

## Resultados
- Emails enviados: 50
- Emails abiertos: 35 (70%)
- Clics: 15 (30%)
- Credenciales: 8 (16%)
- Reportes: 10 (20%)

## Análisis
- El 16% de los empleados entregó credenciales
- Solo el 20% reportó el intento
- Departamento con más caídas: Desarrollo (5 de 8)

## Recomendaciones
1. Entrenamiento trimestral obligatorio
2. Implementar MFA en todos los sistemas
3. Bloquear dominios similares al corporativo
4. Crear proceso de reporte de phishing

## Evidencia
- Dashboard de GoPhish: [enlace]
- Reporte exportado: [enlace]
- Screenshot: [enlace]
```

---

**[⬅ Volver al módulo](../README.md)** · **[→ SET Toolkit](./02-set-toolkit.md)**
