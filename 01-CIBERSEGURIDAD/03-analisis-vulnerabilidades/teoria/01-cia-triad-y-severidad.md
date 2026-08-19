# 🔺 CIA Triad y Severidad de Hallazgos

> *"Una vulnerabilidad no importa solo por existir, sino por lo que compromete."*

---

## ¿Qué es la tríada CIA?

La tríada **CIA** representa los tres objetivos centrales de seguridad:

| Pilar | Qué protege | Pregunta clave |
|---|---|---|
| **Confidentiality** | Información sensible y acceso a datos | ¿Quién puede ver esto? |
| **Integrity** | Exactitud y confianza de los datos/sistemas | ¿Quién puede cambiar esto? |
| **Availability** | Continuidad del servicio | ¿Quién puede tumbar o degradar esto? |

Un mismo hallazgo puede afectar uno, dos o los tres pilares a la vez.

---

## Cómo pensar un hallazgo con CIA

### Ejemplo 1 — Bucket o directorio expuesto
- **Confidentiality:** Alto, porque expone datos a terceros.
- **Integrity:** Bajo/medio si además permite escritura.
- **Availability:** Bajo, salvo que afecte operación crítica.

### Ejemplo 2 — Panel admin con credenciales por defecto
- **Confidentiality:** Alto, acceso a datos.
- **Integrity:** Alto, modificación no autorizada.
- **Availability:** Medio/alto, posible borrado o interrupción.

### Ejemplo 3 — DoS por configuración deficiente
- **Confidentiality:** Bajo.
- **Integrity:** Bajo.
- **Availability:** Crítico.

---

## Severidad no es lo mismo que CVE

Muchos estudiantes creen que una CVE crítica siempre significa riesgo crítico. Error.

La severidad real depende de:
1. Exposición del activo.
2. Probabilidad de explotación.
3. Impacto sobre la tríada CIA.
4. Controles compensatorios existentes.
5. Valor de negocio del sistema afectado.

---

## Matriz de lectura rápida

| Tipo de hallazgo | C | I | A | Comentario |
|---|---|---|---|---|
| Directory listing | Medio | Bajo | Bajo | Puede exponer archivos sensibles |
| SQL Injection | Alto | Alto | Medio | Exfiltración y manipulación de datos |
| XSS almacenado | Medio | Alto | Bajo | Robo de sesión y manipulación de interfaz |
| RCE autenticado | Alto | Alto | Alto | Control casi total del sistema |
| SSH débil | Alto | Alto | Alto | Acceso directo al host |
| Rate limiting ausente | Bajo | Bajo | Medio | Aumenta viabilidad de fuerza bruta/DoS |

---

## Del hallazgo al riesgo

```text
Debilidad → Vulnerabilidad → Explotación posible → Impacto CIA → Riesgo → Prioridad
```

Ejemplo:

```text
Password por defecto
→ acceso no autorizado
→ compromiso del panel
→ afecta C e I de forma alta
→ riesgo alto
→ prioridad inmediata
```

---

## Cómo documentarlo profesionalmente

Para cada hallazgo responde:
- ¿Qué se encontró?
- ¿Cómo se identificó?
- ¿Qué parte de CIA afecta?
- ¿Qué tan fácil es explotarlo?
- ¿Cuál sería el peor escenario razonable?
- ¿Qué debe hacer el Blue Team ya mismo?
- ¿Cómo validará el Purple Team que quedó corregido?

---

**[← Volver al módulo](../README.md)** · **[→ VM Lifecycle](./02-vulnerability-management-lifecycle.md)**
