# 🟣 Red, Blue y Purple Team operando juntos

> *"La madurez no está en encontrar más hallazgos, sino en convertirlos en mejora continua."*

---

## Qué hace cada equipo

| Equipo | Misión | Entregable típico |
|---|---|---|
| 🔴 Red Team | Simular al atacante y validar explotabilidad | Evidencia técnica, PoC, cadena de ataque |
| 🔵 Blue Team | Detectar, contener, mitigar y monitorear | Reglas, hardening, plan de remediación |
| 🟣 Purple Team | Alinear ofensiva y defensa para aprender más rápido | Validación cruzada y mejora de controles |

---

## Cómo se reparte el trabajo en este módulo

### Red Team
- Descubre superficie técnica.
- Ejecuta scanners y validación controlada.
- Confirma qué hallazgos son reales y cuáles son falsos positivos.
- Estima impacto técnico y rutas de explotación.

### Blue Team
- Mapea activos afectados.
- Prioriza según riesgo, exposición y criticidad.
- Define correcciones y compensating controls.
- Diseña cómo detectar intentos similares.

### Purple Team
- Reúne hallazgos y respuesta en una sola mesa.
- Convierte cada hallazgo en una mejora verificable.
- Repite escaneo o validación tras corregir.
- Documenta lecciones aprendidas.

---

## Ejemplo de flujo Purple

```text
Nuclei detecta panel expuesto
→ Red Team valida acceso no autorizado
→ Blue Team restringe acceso por autenticación/IP
→ Red Team reintenta y confirma cierre del vector
→ Blue Team agrega monitoreo y alerta
→ Purple Team documenta la mejora y el tiempo de respuesta
```

---

## Qué diferencia a un analista junior de uno elite

| Junior | Elite |
|---|---|
| Entrega salida del scanner | Entiende contexto y negocio |
| Reporta todo igual | Prioriza lo que realmente importa |
| Mira CVSS aislado | Cruza CIA, exposición y exploitabilidad |
| Piensa por rol separado | Coordina Red, Blue y Purple |
| Cierra ticket | Valida que la corrección funcione |

---

**[← VM Lifecycle](./02-vulnerability-management-lifecycle.md)** · **[→ Herramienta: Nuclei](../herramientas/nuclei.md)**
