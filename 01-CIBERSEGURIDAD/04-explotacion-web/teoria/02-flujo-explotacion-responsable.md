# ⚙️ Flujo de explotación responsable

> No es solo "romper" cosas: es seguir un ciclo ordenado, documentado y reproducible.

---

## 1. Confirmar alcance y entorno

En este módulo:
- solo usamos **DVWA**, **WebGoat** y **Juice Shop** levantados en local,
- no escaneamos ni atacamos sistemas externos,
- seguimos siempre la lógica de laboratorio + evidencia + lecciones aprendidas.

---

## 2. Enumerar superficie y puntos de entrada

Antes de lanzar payloads:
- identifica formularios,
- parámetros en URLs,
- puntos donde se refleja input,
- endpoints que manejan IDs de recursos.

---

## 3. Probar hipótesis, no comandos sueltos

Cada payload debe responder a una pregunta:
- "¿Este parámetro se inyecta en SQL?"
- "¿Este campo se refleja sin sanitizar?"
- "¿Esta ruta valida que el recurso me pertenece?"

---

## 4. Documentar paso a paso

Para cada hallazgo:
- anota URL, parámetro, payload y respuesta,
- guarda capturas o salidas relevantes,
- anota qué parte de **CIA** está en juego,
- relaciona con controles defensivos posibles.

---

## 5. Proponer mitigación inmediata

Incluso en laboratorio, piensa:
- cómo parametrizar consultas,
- cómo validar/normalizar input,
- cómo reforzar controles de acceso,
- qué headers de seguridad ayudarían,
- qué alertas o logs deberían generarse.

---

## 6. Re-test (Purple Team)

Una vez aplicada la mitigación en el lab:
- vuelve a lanzar las mismas pruebas,
- verifica que el fallo ya no es explotable,
- actualiza el writeup y el change-log.

---

**[← OWASP contexto](./01-owasp-top10-contexto.md)** · **[→ Patrones de hardening web](./03-patrones-hardening-web.md)**
