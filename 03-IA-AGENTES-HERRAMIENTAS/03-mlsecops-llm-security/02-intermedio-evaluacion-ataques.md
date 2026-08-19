# Módulo MLSecOps y Seguridad de LLM — Nivel Intermedio

## 🎯 Objetivos de aprendizaje

Al completar este nivel podrás:

- Identificar y clasificar ataques típicos contra LLM (prompt injection, exfiltración, jailbreaking básico).
- Diseñar y ejecutar un conjunto pequeño de pruebas de seguridad contra un modelo.
- Documentar resultados de pruebas de forma útil para tu equipo.
- Publicar un repositorio simple con tus casos de prueba y hallazgos.

---

## 📚 Temas clave

1. Tipos de ataques a LLM (visión general)
2. Criterios básicos de evaluación de respuestas
3. Diseño de un "mini suite" de pruebas
4. Buenas prácticas de documentación

---

## 🧨 1. Tipos de ataques a LLM (visión general)

Algunos tipos de ataques que debes conocer a este nivel:

- **Prompt injection:** instrucciones ocultas o maliciosas que intentan anular políticas.
- **Data exfiltration:** usar el modelo para extraer información sensible del contexto o del training data.
- **Jailbreaking básico:** intentar que el modelo haga cosas que su política prohíbe.

Tu objetivo aquí no es explotar sistemas reales, sino entender **cómo se verían estos ataques en un entorno controlado**.

---

## 📏 2. Criterios básicos de evaluación

Cuando pruebas un modelo, no basta con "ver qué responde"; necesitas criterios:

- ¿La respuesta cumple políticas de seguridad (no entrega datos sensibles, no explica actividades ilegales)?
- ¿La respuesta es consistente y clara sobre límites?
- ¿La respuesta explica por qué rechaza algo (mejor) o simplemente obedece?

Define 3–5 criterios simples que usarás en tu laboratorio.

---

## 🧪 3. Laboratorio — Mini suite de pruebas

> Objetivo: crear un conjunto de pruebas de seguridad básicas para un LLM y publicarlas.

### Prerrequisitos

- Haber completado el nivel Entry.
- Acceso a algún LLM (local o en la nube).
- Conocimientos básicos de Markdown y, opcionalmente, Python.

### Opción A: Pruebas manuales (sin código)

1. Crea una carpeta `llm-security-tests/` en tu portafolio.
2. Crea un archivo `casos-de-prueba.md` con una tabla:

   - ID de prueba.
   - Tipo de ataque (ej. prompt injection).
   - Prompt.
   - Resultado esperado (seguro/inseguro).
   - Observaciones.

3. Ejecuta cada prueba contra el modelo y rellena las observaciones.
4. Añade un pequeño análisis al final: ¿qué patrón viste?

### Opción B: Pruebas semi-automáticas (con código)

Si sabes algo de Python:

1. Crea un script que lea una lista de prompts desde un archivo.
2. Envíalos al modelo (según la API que uses).
3. Guarde respuestas en un archivo de salida.
4. Revisa manualmente y marca cuáles son seguras o no.

En ambos casos, el foco está en **diseñar las pruebas** y **documentar resultados**, no en la herramienta en sí.

---

## 📂 Entregable público recomendado — Repo de pruebas

> Formato sugerido: Repositorio en GitHub.

Nombre sugerido:

> `llm-security-tests-es` o similar.

Contenido mínimo:

- `README.md` explicando:
  - Objetivo del repo.
  - Qué tipo de modelo usaste (sin exponer credenciales).
  - Lista de casos de prueba incluidos.
- `casos-de-prueba.md` con la tabla de pruebas y resultados.
- (Opcional) Script simple en Python para ejecutar pruebas.

Este repositorio se convierte en evidencia de que **no solo conoces los ataques en teoría**, sino que sabes diseñar y documentar pruebas de seguridad.

---

## ✍️ Buenas prácticas de documentación

Para que tu trabajo sea útil:

- Escribe como si otra persona fuera a usar tus pruebas.
- Sé transparente con limitaciones (modelo usado, número de pruebas, etc.).
- No compartas información sensible ni prompts que violen políticas.

---

## ✅ Checklist de este nivel

Antes de pasar al nivel avanzado, verifica si puedes:

- Explicar al menos 3 tipos de ataques a LLM.
- Mostrar una tabla o archivo con tus propios casos de prueba.
- Justificar por qué consideras una respuesta segura o insegura.
- Compartir el enlace de tu repo de pruebas como parte de tu portafolio.

Si aún no te sientes cómodo explicando tus pruebas a otra persona, repasa la documentación y mejora claridad antes de continuar.
