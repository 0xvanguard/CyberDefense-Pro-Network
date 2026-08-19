# 🔓 IDOR en WebGoat y Juice Shop

> Verás cómo cambiar un identificador puede exponer datos de otros usuarios.

---

## 1. Concepto

IDOR (Insecure Direct Object Reference) aparece cuando la app expone IDs directos de recursos y no valida si el usuario actual debe acceder a ellos.

---

## 2. WebGoat

- Localiza los retos relacionados con Broken Access Control / Insecure Direct Object Reference.
- Observa cómo cambiar parámetros de ID afecta los datos mostrados.

---

## 3. Juice Shop

- Busca secciones donde se carguen recursos por ID.
- Prueba variaciones de IDs para ver si accedes a datos de otros usuarios.

---

## 4. Mitigación

- Verificar siempre la propiedad del recurso.
- Usar IDs no predecibles cuando tenga sentido.
- Aplicar checks de autorización consistentes en backend.

---

**[← XSS](./xss-dvwa-juice-shop.md)** · **[→ Headers y hardening](../defensa/headers-seguridad-nginx.md)**
