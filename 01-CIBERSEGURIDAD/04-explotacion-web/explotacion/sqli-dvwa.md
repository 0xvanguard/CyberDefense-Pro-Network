# 💉 SQL Injection en DVWA

> Práctica guiada para entender el impacto y la mitigación básica.

---

## 1. Preparar DVWA

- Nivel de seguridad de DVWA en **Low**.
- Ir al módulo de SQL Injection.

---

## 2. Probar comportamiento normal

- Envía un input válido.
- Observa cómo responde la app.
- Identifica parámetros involucrados (por ejemplo, `id`).

---

## 3. Probar input de prueba

- Envía un `'` o `"` y revisa si hay errores.
- Busca mensajes que sugieran consulta SQL.

---

## 4. Extraer información

- Usa payloads simples para verificar si puedes listar registros.
- Observa qué datos expone y cómo.

---

## 5. Reflexión Red / Blue / Purple

- **Red:** ¿Qué datos obtuviste que no deberías ver?
- **Blue:** ¿Qué controles faltan (parametrización, validación, logging)?
- **Purple:** ¿Qué prueba automatizada podrías dejar para re-testear tras la corrección?

---

**[← Patrones de hardening](../teoria/03-patrones-hardening-web.md)** · **[→ XSS](./xss-dvwa-juice-shop.md)**
