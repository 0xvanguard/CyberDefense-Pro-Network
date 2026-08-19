# 05 – Automatización con Python + IA para Seguridad

> **Objetivo Principal:** Al finalizar este módulo tendrás al menos **un script real en Python** que use una API de IA para automatizar una tarea de seguridad (por ejemplo, resumir resultados de Nmap o normalizar hallazgos) y podrás mostrarlo en tu portafolio.

Este módulo conecta tu perfil técnico (Python + ciberseguridad) con el uso práctico de modelos de lenguaje como copilotos dentro de scripts y pipelines.

---

## 1. Teoría Mínima Viable (TMV)

- **Automatización en seguridad:**
  Muchas tareas de seguridad son repetitivas: leer resultados de scans, normalizar findings, crear borradores de reportes, clasificar logs, etc. Automatizar parte de esto te ahorra tiempo y reduce errores humanos.

- **LLM como "post-procesador inteligente":**
  En vez de pedirle al modelo que "haga todo", lo usamos para tareas específicas dentro de un flujo:
  - Resumir texto técnico.
  - Clasificar hallazgos por severidad.
  - Proponer descripciones y recomendaciones que luego revisas.

- **Arquitectura típica de un script Python + IA:**
  1. Obtener datos (archivo, salida de herramienta, API, etc.).
  2. Limpiar/parsear.
  3. Enviar a la API de IA con un prompt bien definido.
  4. Recibir respuesta y guardarla (archivo, consola, reporte, etc.).

- **Buenas prácticas básicas:**
  - No enviar datos sensibles reales a servicios externos.
  - Manejar la API key mediante variables de entorno, no hardcodeada.
  - Loggear lo suficiente para depurar, pero sin exponer secretos.

---

## 2. Herramientas del Oficio

| Herramienta / Librería | Caso de Uso Principal                                |
|------------------------|------------------------------------------------------|
| Python 3               | Lenguaje principal del script                        |
| `requests` o SDK oficial de la API de IA | Hacer llamadas HTTP a la API de IA              |
| Nmap (o archivo de resultados de otra herramienta) | Fuente de datos a resumir/normalizar        |
| Editor de código (VS Code, etc.) | Escribir y probar el script                         |

> Nota: No se incluye aquí código de API concreto porque dependerá del proveedor (Anthropic, OpenAI, etc.). Deberás adaptar el ejemplo al SDK que uses.

---

## 3. Práctica Guiada (Laboratorio)

### Prerrequisitos

- [ ] Python 3 instalado.
- [ ] Entorno virtual opcional (`python -m venv venv`).
- [ ] Una API key válida de tu proveedor de IA (ej: `ANTHROPIC_API_KEY` o similar), configurada en variables de entorno.
- [ ] Un archivo de ejemplo con resultados de Nmap u otra herramienta, por ejemplo: `nmap-inicial.txt`.

---

### Lab – Script de resumen de resultados de Nmap con IA

**Objetivo:** Construir un script Python que:
1. Lea un archivo `nmap-inicial.txt`.
2. Envíe el contenido (o la parte relevante) a una API de IA con un prompt claro.
3. Guarde un resumen en `resumen-nmap.md` listo para usar en un informe.

#### Paso 1 – Preparar el entorno

1. Crea una carpeta de trabajo, por ejemplo:
   ```bash
   mkdir ia-automation-nmap
   cd ia-automation-nmap
   ```

2. (Opcional) Crea y activa un entorno virtual:
   ```bash
   python -m venv venv
   # En Linux/macOS
   source venv/bin/activate
   # En Windows (PowerShell)
   .\venv\Scripts\Activate.ps1
   ```

3. Instala dependencias mínimas (por ejemplo `requests`):
   ```bash
   pip install requests
   ```

4. Asegúrate de tener un archivo `nmap-inicial.txt` (puede venir de un lab anterior de pentest o ser simulado).

#### Paso 2 – Esqueleto del script

Crea un archivo `resumir_nmap_con_ia.py` con estructura básica:

```python
import os
import requests

API_KEY = os.getenv("TU_API_KEY_IA")  # Ej: ANTHROPIC_API_KEY, OPENAI_API_KEY, etc.

def leer_resultados_nmap(ruta_archivo: str) -> str:
    with open(ruta_archivo, "r", encoding="utf-8") as f:
        return f.read()

def llamar_api_ia(texto: str) -> str:
    # TODO: Implementar llamada real según el proveedor
    # Pseudocódigo de ejemplo:
    # response = requests.post("https://api.proveedor-ia.com/v1/chat", json={...}, headers={"Authorization": f"Bearer {API_KEY}"})
    # return response.json()["content"]
    return "[Aquí iría la respuesta de la IA con el resumen]"

def guardar_resumen(resumen: str, ruta_salida: str) -> None:
    with open(ruta_salida, "w", encoding="utf-8") as f:
        f.write(resumen)

if __name__ == "__main__":
    nmap_raw = leer_resultados_nmap("nmap-inicial.txt")
    # Aquí podrías limpiar el texto si es muy largo
    resumen = llamar_api_ia(nmap_raw)
    guardar_resumen(resumen, "resumen-nmap.md")
    print("Resumen generado en resumen-nmap.md")
```

> Tu tarea es **reemplazar la función `llamar_api_ia`** con la llamada real a la API que uses, siguiendo la documentación oficial.

#### Paso 3 – Diseñar el prompt con ayuda de IA

1. Abre tu modelo IA (Perplexity, Claude, etc.).
2. Pregunta algo como:
   > "Ayúdame a diseñar un prompt para que un modelo de lenguaje resuma resultados de Nmap en un formato útil para un informe de pentesting (lista de servicios, puertos, posibles vectores)."
3. Adapta el prompt obtenido para que tu script lo use en la llamada a la API.

#### Paso 4 – Probar el script

1. Ejecuta el script:
   ```bash
   python resumir_nmap_con_ia.py
   ```
2. Verifica que se genera `resumen-nmap.md`.
3. Abre el archivo y revisa si el formato te sirve para tu informe.

#### Paso 5 – Mejoras opcionales

- Limitar el texto enviado (por ejemplo, solo puertos abiertos).
- Añadir manejo de errores (sin API key, error HTTP, etc.).
- Incluir argumentos por línea de comandos para elegir archivo de entrada y salida.

---

## 4. Evidencia y Portafolio

- **Reto final:**
  Tener un script funcional `resumir_nmap_con_ia.py` (o nombre similar) que:
  - Lea un archivo de resultados de herramienta de seguridad.
  - Llame a una API de IA con un prompt bien diseñado.
  - Genere un resumen útil para informes.

- **Entregable:**
  - Carpeta `ia-automation-nmap/` con:
    - `resumir_nmap_con_ia.py`
    - `nmap-inicial.txt` (redactado o de un lab de prueba)
    - `resumen-nmap.md`
    - `README.md` corto explicando cómo usar el script.

- **Para tu Portafolio:**
  - Sube esa carpeta a un repo público (por ejemplo, `security-automation-labs`).
  - En tu `PORTAFOLIO.md`, añade una entrada tipo:
    > "Script de automatización en Python que usa IA para resumir resultados de Nmap y acelerar la redacción de informes de pentest."

---

## 5. Siguiente Paso

Después de este módulo puedes:

👉 Integrar el script en un pipeline DevSecOps (por ejemplo, ejecutarlo después de un scan en CI/CD y subir el resumen como artefacto).

👉 Adaptar la misma idea a otras tareas:
   - Normalizar findings de diferentes herramientas.
   - Generar borradores de reportes SOC.
   - Clasificar logs o alertas por severidad con ayuda de IA.

Este módulo se conecta directamente con tu camino de **DevSecOps + MLSecOps**, mostrando código real que mezcla seguridad e IA.
