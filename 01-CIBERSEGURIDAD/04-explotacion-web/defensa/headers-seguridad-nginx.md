# 🧱 Headers de seguridad en Nginx

> Ejemplo de cómo añadir una capa defensiva delante de una app vulnerable.

---

## Headers recomendados

- `X-Frame-Options: DENY`
- `X-Content-Type-Options: nosniff`
- `Referrer-Policy: strict-origin-when-cross-origin`
- `Content-Security-Policy` adaptada a la app

---

## Integración básica

En este módulo usarás un `reverse-proxy` de ejemplo para añadir estos headers delante de una de las apps de laboratorio.

---

## Relación con las vulns

- Ayudan a reducir impacto de ciertos tipos de XSS.
- Mejoran postura general ante ataques de navegador.

---

**[← IDOR](../explotacion/idor-webgoat-juice-shop.md)** · **[→ reverse-proxy ejemplo](./reverse-proxy-nginx-ejemplo.conf)**
