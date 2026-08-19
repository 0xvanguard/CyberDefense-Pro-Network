# 🧩 OWASP Top 10 — Contexto rápido para SQLi, XSS e IDOR

> Este módulo no pretende cubrir todo OWASP Top 10, sino dar contexto a tres vulnerabilidades clave.

---

## OWASP Top 10 (visión general)

OWASP mantiene una lista de las categorías de riesgo más críticas en aplicaciones web. Dentro de esa lista, SQLi, XSS e IDOR aparecen como ejemplos directos o indirectos de:

- **Inyección**
- **Broken Access Control**
- **Vulnerabilidades en diseño / lógica**

---

## SQL Injection

Cuando una aplicación construye consultas SQL concatenando datos del usuario sin parametrización, un atacante puede:

- leer datos que no debería ver,
- modificar o borrar registros,
- escalar privilegios,
- incluso tomar control del servidor en ciertos entornos.

---

## Cross-Site Scripting (XSS)

XSS ocurre cuando una aplicación permite que código (generalmente JavaScript) controlado por el atacante se ejecute en el navegador de otras personas.

Consecuencias típicas:

- robo de cookies/sesiones,
- modificación maliciosa del DOM,
- redirecciones a sitios de phishing,
- keylogging en la página vulnerable.

---

## IDOR / Broken Access Control

IDOR (Insecure Direct Object Reference) es un caso típico de controles de acceso rotos: el sistema permite acceder a recursos cambiando identificadores (por ejemplo, `/profile/123` por `/profile/124`) sin verificar si el usuario está autorizado.

Esto impacta la **Confidencialidad** y, en muchos casos, la **Integridad** de los datos.

---

## Cómo se conectan con CIA

- **SQLi:** C e I (exfiltración y manipulación de datos) +, en algunos casos, A.
- **XSS:** C e I desde la perspectiva del usuario (sesiones, acciones en su nombre).
- **IDOR:** C e I directamente sobre otros usuarios o recursos.

**[← Volver al módulo](../README.md)** · **[→ Flujo de explotación responsable](./02-flujo-explotacion-responsable.md)**
