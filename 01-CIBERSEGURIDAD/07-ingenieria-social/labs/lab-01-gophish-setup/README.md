# 🎣 Lab 01: Configuración de GoPhish

## Objetivo

Configurar y usar GoPhish para realizar campañas de phishing educativas en un entorno controlado.

## Escenario

Eres un profesional de seguridad configurando una herramienta de phishing para una campaña de concientización en tu organización.

## Entorno

- **Sistema:** Ubuntu 22.04 LTS con GoPhish instalado
- **URL de GoPhish:** https://localhost:3333
- **Credenciales admin:** admin / gophish123

## Inicio Rápido

```bash
# Levantar el entorno
docker compose up -d

# Verificar que GoPhish está corriendo
docker compose logs -f gophish

# Acceder a la interfaz web
# Abrir https://localhost:3333 en el navegador
```

## Instrucciones

### Paso 1: Configurar Sending Profile

1. Ir a **Sending Profiles** → **Add New**
2. Configurar:
   - **Name:** Lab SMTP Server
   - **From:** phishing@lab.local
   - **Host:** mailhog:1025 (sin autenticación para el lab)
   - **Username:** (vacío)
   - **Password:** (vacío)
3. Guardar y probar la conexión

### Paso 2: Crear Landing Page

1. Ir a **Landing Pages** → **Add New**
2. Diseñar una página de phishing educativa
3. Ejemplo de HTML:

```html
<!DOCTYPE html>
<html>
<head>
    <title>Portal de Empleados</title>
    <style>
        body { font-family: Arial, sans-serif; max-width: 400px; margin: 100px auto; }
        .login-box { padding: 20px; border: 1px solid #ccc; border-radius: 5px; }
        input { width: 100%; padding: 10px; margin: 5px 0; box-sizing: border-box; }
        button { width: 100%; padding: 10px; background: #007bff; color: white; border: none; }
    </style>
</head>
<body>
    <div class="login-box">
        <h2>Portal de Empleados</h2>
        <form action="" method="post">
            <input type="email" name="email" placeholder="Email corporativo" required>
            <input type="password" name="password" placeholder="Contraseña" required>
            <button type="submit">Iniciar Sesión</button>
        </form>
        <p style="text-align: center; color: #666; font-size: 12px;">
            ¿Problemas? Contacta a soporte@empresa.com
        </p>
    </div>
</body>
</html>
```

### Paso 3: Crear Email Template

1. Ir a **Email Templates** → **Add New**
2. Configurar:
   - **Name:** Alerta de Seguridad
   - **From:** seguridad@empresa.com
   - **Subject:** Acción requerida: Actualiza tu contraseña
   - **Body:** (usar plantilla HTML proporcionada)

### Paso 4: Definir Objetivos (Users)

1. Ir a **Users & Groups** → **Add Group**
2. Agregar usuarios de prueba:
   - user1@test.com
   - user2@test.com
   - user3@test.com

### Paso 5: Crear y Ejecutar Campaña

1. Ir to **Campaigns** → **New Campaign**
2. Configurar:
   - **Name:** Campaña Educativa Q1
   - **Email Template:** Alerta de Seguridad
   - **Landing Page:** Portal de Empleados
   - **Sending Profile:** Lab SMTP Server
   - **Users:** Grupo de prueba
   - **Send Date:** Ahora
3. Lanzar campaña

### Paso 6: Analizar Resultados

1. Ir a **Dashboard** para ver métricas:
   - Emails enviados
   - Emails abiertos
   - Links clickeados
   - Credenciales capturadas
2. Revisar detalles de cada objetivo

## Métricas de la Campaña

| Métrica | Objetivo |
|---------|----------|
| Tasa de apertura | > 50% |
| Tasa de clickeo | > 30% |
| Tasa de captura | > 20% |

## Criterios de Éxito

- [ ] Configurar sending profile correctamente
- [ ] Crear landing page funcional
- [ ] Ejecutar campaña exitosamente
- [ ] Analizar resultados en el dashboard
- [ ] Documentar lecciones aprendidas

## Limpieza

```bash
# Detener y eliminar el entorno
docker compose down -v --rmi all
```

---

*Lab creado para fines educativos — CyberDefense-Pro-Network*
