# 🛡️ Patrones básicos de hardening web

> La idea no es convertirte en dev full stack, sino entender qué cosas pedir y validar.

---

## 1. Parametrización de consultas

- Evitar concatenar input del usuario en SQL.
- Usar consultas preparadas / parámetros.
- Validar tipos (números, longitudes, formatos).

---

## 2. Validación y normalización de entradas

- Validar lado servidor (no solo frontend).
- Usar whitelists cuando sea posible.
- Normalizar entradas (trim, lower/upper, etc.).

---

## 3. Control de acceso por recurso

- No confiar solo en "estar logueado".
- Verificar que el recurso solicitado pertenece al usuario o al rol autorizado.
- Revisar rutas tipo `/user/{id}` y APIs con IDs predecibles.

---

## 4. Headers de seguridad

- `Content-Security-Policy`
- `X-Frame-Options`
- `X-Content-Type-Options`
- `Referrer-Policy`
- `Strict-Transport-Security` (cuando aplique)

---

## 5. Logging y monitoreo

- Registrar intentos frecuentes de payloads sospechosos.
- Registrar accesos a recursos ajenos.
- Construir alertas básicas a partir de patrones.

---

**[← Flujo responsable](./02-flujo-explotacion-responsable.md)** · **[→ SQLi en DVWA](../explotacion/sqli-dvwa.md)**
