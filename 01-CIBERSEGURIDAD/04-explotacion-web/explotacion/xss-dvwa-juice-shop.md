# 🧨 XSS en DVWA y Juice Shop

> Entenderás cómo un input aparentemente "inofensivo" termina ejecutando código en otro navegador.

---

## 1. DVWA — XSS reflejado

- Nivel de seguridad **Low**.
- Localiza el módulo de XSS (reflected).
- Envía un payload sencillo y observa si se refleja sin escapar.

---

## 2. DVWA — XSS almacenado

- Cambia al módulo de XSS stored.
- Publica un comentario con un payload.
- Comprueba si se ejecuta para otros usuarios.

---

## 3. Juice Shop — XSS práctico

- Identifica campos de búsqueda, comentarios o similares.
- Prueba entradas que podrían renderizarse sin sanitización.
- Observa efectos sobre la interfaz.

---

## 4. Impacto

- Robo de sesión.
- Modificación de la página.
- Redirecciones a sitios maliciosos.

---

## 5. Mitigación

- Escapar output.
- Validar/limitar input.
- Configurar CSP adecuada.

---

**[← SQLi](./sqli-dvwa.md)** · **[→ IDOR](./idor-webgoat-juice-shop.md)**
