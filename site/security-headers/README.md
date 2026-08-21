# 🔒 Security Headers Configuration

## Opción 1: Cloudflare Worker (Recomendado)

### Pasos para configurar:

1. **Crear cuenta en Cloudflare** (gratis)
   - Ve a https://dash.cloudflare.com/sign-up

2. **Agregar dominio**
   - Agrega tu dominio a Cloudflare
   - Actualiza los nameservers en tu registrador

3. **Crear Worker**
   - Ve to Workers & Pages > Create Worker
   - Nombre: `cdpn-security-headers`
   - Pega el código de `worker.js`
   - Deploy

4. **Configurar ruta**
   - Ve to Triggers > Custom Domains
   - Agrega: `campus.0xvanguard.dev` (o tu dominio)
   - O usa Routes: `/*` para el dominio de GitHub Pages

5. **Verificar**
   ```bash
   curl -sI https://tu-dominio.com/ | grep -i "content-security-policy"
   ```

### Headers que agrega:

| Header | Valor | Propósito |
|--------|-------|-----------|
| Content-Security-Policy | Ver abajo | Prevenir XSS |
| X-Frame-Options | DENY | Prevenir clickjacking |
| X-Content-Type-Options | nosniff | Prevenir MIME sniffing |
| Referrer-Policy | strict-origin-when-cross-origin | Control de referrer |
| Permissions-Policy | camera=(), microphone=(), ... | Restringir features |
| Cross-Origin-Opener-Policy | same-origin | Aislamiento |
| Cross-Origin-Resource-Policy | same-origin | Prevenir leaks |
| Strict-Transport-Security | max-age=31536000 | Forzar HTTPS |

---

## Opción 2: Meta Tags (Limitado)

Para GitHub Pages sin Cloudflare, agregar meta tags al `<head>`:

```html
<!-- Security Headers (via meta tags) -->
<meta http-equiv="Content-Security-Policy" content="default-src 'self'; script-src 'self' 'unsafe-inline' https://cdnjs.cloudflare.com; style-src 'self' 'unsafe-inline' https://fonts.googleapis.com https://cdnjs.cloudflare.com; font-src 'self' https://fonts.gstatic.com https://cdnjs.cloudflare.com; img-src 'self' data:; connect-src 'self' https://api.github.com; frame-ancestors 'none'">
<meta http-equiv="X-Content-Type-Options" content="nosniff">
<meta http-equiv="X-Frame-Options" content="DENY">
<meta name="referrer" content="strict-origin-when-cross-origin">
```

**Limitaciones:**
- No funciona para `X-Frame-Options`
- No funciona para `Strict-Transport-Security`
- No funciona para `Cross-Origin-*` headers
- Solo CSP básico

---

## Opción 3: GitHub Actions (Workaround)

Crear un workflow que modifique los archivos HTML:

```yaml
name: Add Security Headers

on:
  push:
    branches: [main]

jobs:
  add-headers:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      
      - name: Add security headers to index.html
        run: |
          sed -i 's/<head>/<head>\n    <meta http-equiv="Content-Security-Policy" content="default-src '\''self'\''; script-src '\''self'\'' '\''unsafe-inline'\'' https:\/\/cdnjs.cloudflare.com; style-src '\''self'\'' '\''unsafe-inline'\'' https:\/\/fonts.googleapis.com https:\/\/cdnjs.cloudflare.com; font-src '\''self'\'' https:\/\/fonts.gstatic.com https:\/\/cdnjs.cloudflare.com; img-src '\''self'\'' data:; connect-src '\''self'\'' https:\/\/api.github.com; frame-ancestors '\''none'\''">/g' docs/index.html
          sed -i 's/<head>/<head>\n    <meta http-equiv="X-Content-Type-Options" content="nosniff">/g' docs/index.html
          sed -i 's/<head>/<head>\n    <meta http-equiv="X-Frame-Options" content="DENY">/g' docs/index.html
```

**Limitaciones:**
- Solo afecta archivos estáticos
- No funciona para respuestas HTTP
- No es ideal

---

## Content-Security-Policy Detallado

```
Content-Security-Policy:
  default-src 'self';
  script-src 'self' 'unsafe-inline' 'unsafe-eval' https://cdnjs.cloudflare.com https://www.googletagmanager.com;
  style-src 'self' 'unsafe-inline' https://fonts.googleapis.com https://cdnjs.cloudflare.com;
  font-src 'self' https://fonts.gstatic.com https://cdnjs.cloudflare.com;
  img-src 'self' data: https: blob:;
  connect-src 'self' https://api.github.com;
  media-src 'self';
  object-src 'none';
  frame-src 'none';
  frame-ancestors 'none';
  form-action 'self';
  base-uri 'self';
  upgrade-insecure-requests
```

### Explicación:

| Directiva | Propósito |
|-----------|-----------|
| `default-src 'self'` | Solo cargar recursos del mismo dominio |
| `script-src 'self' 'unsafe-inline'` | Scripts del mismo dominio + inline (necesario para VitePress) |
| `style-src 'self' 'unsafe-inline'` | Estilos del mismo dominio + inline |
| `font-src` | Fuentes solo de Google Fonts y Cloudflare |
| `img-src 'self' data: https:` | Imágenes de cualquier HTTPS |
| `connect-src 'self' https://api.github.com` | Solo API de GitHub |
| `frame-ancestors 'none'` | No permitir iframes |
| `object-src 'none'` | No permitir plugins |

---

## Verificación

### Test headers locally:
```bash
# Usar curl
curl -sI https://tu-sitio.com/ | grep -i "content-security-policy"

# Usar browser DevTools
# Abre DevTools > Security tab
```

### Test online:
- https://securityheaders.com/
- https://observatory.mozilla.org/
- https://csp-evaluator.withgoogle.com/

---

## Troubleshooting

### Error: "Refused to load the script"
- Agregar dominio del script a `script-src`
- Ejemplo: `script-src 'self' https://cdnjs.cloudflare.com`

### Error: "Refused to load the stylesheet"
- Agregar dominio del CSS a `style-src`
- Ejemplo: `style-src 'self' https://fonts.googleapis.com`

### Error: "Refused to connect"
- Agregar dominio a `connect-src`
- Ejemplo: `connect-src 'self' https://api.github.com`

### Admin.html no carga
- Verificar que CSP permite scripts inline
- Verificar que `unsafe-inline` está en `script-src`

---

## Recursos

- [Content Security Policy](https://csp.withgoogle.com/)
- [OWASP CSP Cheat Sheet](https://cheatsheetseries.owasp.org/cheatsheets/Content_Security_Policy_Cheat_Sheet.html)
- [MDN CSP Documentation](https://developer.mozilla.org/en-US/docs/Web/HTTP/CSP)
- [Cloudflare Workers](https://developers.cloudflare.com/workers/)
