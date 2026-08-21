# 📄 Reporte Forense

> *"Un hallazgo sin documentación es un hallazgo perdido. El reporte forense es la culminación de todo el análisis."*

---

## 📋 Tabla de contenido

1. [Importancia del reporte](#1-importancia-del-reporte)
2. [Estructura de un reporte forense](#2-estructura-de-un-reporte-forense)
3. [Plantilla profesional](#3-plantilla-profesional)
4. [Guía de escritura](#4-guía-de-escritura)
5. [Ejemplo completo](#5-ejemplo-completo)
6. [Presentación en tribunal](#6-presentación-en-tribunal)
7. [Errores comunes](#7-errores-comunes)
8. [Referencias](#8-referencias)

---

## 1. Importancia del reporte

### ¿Por qué es crítico?

| Razón | Descripción |
|---|---|
| **Evidencia legal** | Un reporte bien hecho es admisible en tribunal |
| **Comunicación** | Explica hallazgos técnicos a audiencias no técnicas |
| **Documentación** | Permite que otros forenses reproduzcan el análisis |
| **Accountability** | Demuestra profesionalismo y método |
| **Remediación** | Guía las acciones correctivas |

### Audiencias del reporte

| Audiencia | Necesita saber |
|---|---|
| **Gerencia** | Impacto económico, riesgo reputacional |
| **Legal** | Admisibilidad de evidencia, cadena de custodia |
| **Técnico** | Detalles del ataque, IOC, remediación |
| **Prensa** (si aplica) | Resumen ejecutivo sin tecnicismos |
| **Tribunal** | Evidencia clara, métodos validados |

---

## 2. Estructura de un reporte forense

### Estructura estándar (NIST SP 800-86)

```
1. Resumen Ejecutivo
2. Alcance y Metodología
3. Hallazgos Detallados
4. Timeline de Eventos
5. Conclusiones
6. Recomendaciones
7. Anexos (Cadena de custodia, hashes, herramientas)
```

### Cada sección en detalle

#### 1. Resumen Ejecutivo (1-2 páginas)

- **Qué pasó:** descripción general del incidente
- **Cuándo:** timeframe del ataque
- **Impacto:** datos comprometidos, sistemas afectados
- **Acciones inmediatas:** qué se hizo para contener

> **Regla:** el resumen ejecutivo debe poder leerse en 5 minutos y dar una comprensión completa del incidente.

#### 2. Alcance y Metodología

- **Qué se analizó:** discos, memoria, logs, dispositivos
- **Qué NO se analizó:** y por qué
- **Herramientas utilizadas:** nombre, versión, configuración
- **Metodología seguida:** NIST 800-86, RFC 3227
- **Cadena de custodia:** integridad de la evidencia

#### 3. Hallazgos Detallados

- **Estructurados por área:** disco, memoria, red, metadatos
- **Cada hallazgo incluye:**
  - Qué se encontró
  - Dónde se encontró (ruta exacta, hash)
  - Cómo se encontró (herramienta, método)
  - Qué significa (impacto)
- **Soporte visual:** screenshots, tablas, gráficos

#### 4. Timeline de Eventos

- **Cronología visual** de todos los eventos relevantes
- **Correlacionado** entre diferentes fuentes de evidencia
- **Marcadores claros** de las acciones del atacante

#### 5. Conclusiones

- **Respuesta directa** a las preguntas del caso
- **Confianza en los hallazgos** (alta/media/baja)
- **Limitaciones** del análisis

#### 6. Recomendaciones

- **Inmediatas** (contención)
- **Corto plazo** (remediación)
- **Largo plazo** (prevención)

#### 7. Anexos

- Cadena de custodia completa
- Hashes de evidencia
- Herramientas y versiones
- Logs de análisis
- Glosario de términos técnicos

---

## 3. Plantilla profesional

```markdown
# REPORTE DE ANÁLISIS FORENSE DIGITAL

## Información del Caso

| Campo | Valor |
|---|---|
| **ID del caso** | INC-2026-0847 |
| **Fecha del reporte** | 20 de Agosto, 2026 |
| **Clasificación** | CONFIDENCIAL |
| **Autor** | J. García, Forense Senior |
| **Revisado por** | M. López, Director de Seguridad |

---

## 1. Resumen Ejecutivo

[Descripción general del incidente en 1-2 párrafos]

**Puntos clave:**
- **Fecha del incidente:** [fecha]
- **Sistemas afectados:** [lista]
- **Datos comprometidos:** [tipo y volumen]
- **Estado actual:** [contenido/mitigado]

---

## 2. Alcance y Metodología

### 2.1 Alcance del análisis

| Elemento | Descripción |
|---|---|
| **Dispositivo analizado** | [Descripción del equipo] |
| **Disco duro** | [Marca, modelo, capacidad, S/N] |
| **RAM** | [Capacidad] |
| **Sistema operativo** | [Versión completa] |
| **Periodo analizado** | [Fecha inicio - Fecha fin] |

### 2.2 Metodología

Este análisis sigue el marco:
- **NIST SP 800-86** — Guide to Integrating Forensic Techniques
- **RFC 3227** — Guidelines for Evidence Collection

### 2.3 Herramientas utilizadas

| Herramienta | Versión | Uso |
|---|---|---|
| dc3dd | 20210813 | Adquisición de disco |
| Volatility 3 | 2.5.0 | Análisis de memoria |
| The Sleuth Kit | 4.12.1 | Análisis de disco |
| Autopsy | 4.21.0 | Análisis GUI |
| plaso | 20240101 | Timeline |
| Eric Zimmerman Tools | 2024.02 | Artefactos Windows |

### 2.4 Cadena de custodia

| # | Fecha | Responsable | Acción | Hash SHA-256 |
|---|---|---|---|---|
| 1 | 2026-08-20 10:00 | J. García | Adquisición | 4b3a9f...e2c1 |
| 2 | 2026-08-20 11:30 | J. García | Traslado | 4b3a9f...e2c1 |
| 3 | 2026-08-20 14:00 | M. López | Análisis | 4b3a9f...e2c1 |

---

## 3. Hallazgos Detallados

### 3.1 Hallazgo: Reverse Shell Activo

| Campo | Detalle |
|---|---|
| **Severidad** | CRÍTICA |
| **Categoría** | Compromiso de sistema |
| **Fecha detectada** | 2026-08-20 |

**Descripción:**
Se detectó una conexión de red activa desde el sistema comprometido hacia el servidor C2 en 185.234.72.15:443.

**Evidencia:**
- Volatility netscan muestra conexión ESTABLISHED desde powershell.exe (PID 5567)
- Comando ejecutado: `powershell.exe -enc <payload base64>`
- Duración: 14 horas (10:00 - 00:00)

**Impacto:**
El atacante tenía acceso remoto completo al sistema durante 14 horas.

**Hallazgo ID:** EVD-001
**Hash de evidencia:** 8f7e6d5c...a1b2

---

### 3.2 Hallazgo: Persistencia Establishada

[Similar estructura]

---

## 4. Timeline de Eventos

| Timestamp | Evento | Fuente | Hallazgo |
|---|---|---|---|
| 09:45:00 | Descarga de payload HTTP | Browser history | EVD-001 |
| 09:59:45 | Creación de archivo | $MFT | EVD-001 |
| 10:00:00 | Ejecución PowerShell | Prefetch | EVD-001 |
| 10:00:00 | Conexión a C2 | Netscan | EVD-001 |
| 10:01:00 | Creación de usuario | Event Log | EVD-002 |
| 10:02:00 | Persistencia Registry | Registry | EVD-002 |
| 10:05:00 | Exfiltración de datos | HTTP log | EVD-003 |
| 10:10:00 | Borrado de logs | $UsnJrnl | EVD-004 |

---

## 5. Conclusiones

### Respuesta a preguntas del caso

| Pregunta | Respuesta | Confianza |
|---|---|---|
| ¿Cómo entró el atacante? | Via phishing → descarga de payload | Alta |
| ¿Qué hizo después? | Escaló privilegios, creó persistencia | Alta |
| ¿Exfiltró datos? | Sí, documentos corporativos | Media |
| ¿Borró evidencia? | Sí, logs del sistema | Alta |
| ¿Cuánto tiempo estuvo activo? | 14 horas | Alta |

### Limitaciones

- No se pudo analizar la memoria completa (parcialmente corrupta)
- Logs del firewall estaban rotados
- Algunos archivos estaban cifrados

---

## 6. Recomendaciones

### Inmediatas (0-24 horas)

1. **Aislar** el sistema comprometido de la red
2. **Resetear** todas las credenciales del usuario
3. **Bloquear** la IP del C2 en el firewall
4. **Notificar** al equipo de respuesta a incidentes

### Corto plazo (1-7 días)

1. **Remover** malware y persistencia
2. **Parchar** vulnerabilidades explotadas
3. **Revisar** sistemas similares en la red
4. **Implementar** monitoreo de los IOC detectados

### Largo plazo (1-30 días)

1. **Implementar** EDR en todos los endpoints
2. **Habilitar** logging avanzado de PowerShell
3. **Capacitar** usuarios contra phishing
4. **Implementar** segmentación de red

---

## 7. Anexos

### Anexo A: Cadena de custodia completa
[Ver sección 2.4]

### Anexo B: Hashes de evidencia

| Evidencia | SHA-256 |
|---|---|
| imagen.dd | 8f7e6d5c...a1b2 |
| memory.raw | 4b3a9f2c...e2c1 |

### Anexo C: Configuración de herramientas

### Anexo D: Glosario

| Término | Definición |
|---|---|
| **C2** | Command and Control — servidor del atacante |
| **Beaconing** | Conexiones periódicas al C2 |
| **Reverse shell** | Conexión de shell remota al atacante |
| **Persistence** | Acceso que sobrevive reinicios |

---

## 8. Firma del Reporte

| Campo | Valor |
|---|---|
| **Elaborado por** | J. García, Forense Senior |
| **Fecha** | 20 de Agosto, 2026 |
| **Revisado por** | M. López, Director de Seguridad |
| **Aprobado por** | [Nombre del responsable legal] |
| **Clasificación** | CONFIDENCIAL |
```

---

## 4. Guía de escritura

### Principios de redacción

| Principio | Ejemplo |
|---|---|
| **Ser preciso** | "powershell.exe ejecutó payload base64" ≠ "algo raro pasó" |
| **Ser objetivo** | "Se detectó X" ≠ "El atacante malicioso hizo X" |
| **Ser completo** | Incluir herramienta, versión, hash, timestamp |
| **Ser claro** | Evitar jerga innecesaria, definir términos |
| **Ser verificable** | Cada afirmación debe tener evidencia |

### Cómo describir hallazgos

```markdown
# MAL:
"Encontramos algo sospechoso en la memoria."

# BIEN:
"Volatility 3 (versión 2.5.0) detectó código inyectado en el 
proceso explorer.exe (PID 3456). El código se encuentra en la 
dirección de memoria 0x000002a4c8d00000 con permisos RWX 
(Read-Write-Execute). El análisis del shellcode indica que se 
trata de un reverse shell de 400 bytes que establece conexión 
con el servidor 185.234.72.15 en el puerto 443.

Evidencia: memory.raw (SHA-256: 4b3a9f2c...e2c1)
Extracción: volatility/malfind.PID3456.0x2a4c8d00000.dmp"
```

### Uso de screenshots

```markdown
## Hallazgo: Conexión de red sospechosa

![Wireshark: Conexión a C2](screenshots/wireshark_c2.png)
*Figura 1: Captura de Wireshark mostrando conexión establecida 
a 185.234.72.15:443 desde powershell.exe (PID 5567)*
```

---

## 5. Ejemplo completo

### Caso: Robo de credenciales

```markdown
# RESUMEN EJECUTIVO

El 20 de Agosto de 2026, se detectó actividad sospechosa en la 
estación de trabajo del empleado John Smith (departamento de 
Finanzas). El análisis forense reveló que el sistema fue 
comprometido el 18 de Agosto a las 14:30 UTC mediante un archivo 
adjunto malicioso en un correo electrónico de phishing.

**Impacto:**
- 15 documentos financieros accedidos (50MB)
- Credenciales de VPN comprometidas
- Acceso remoto activo durante 48 horas

**Estado:** Sistema aislado, credenciales reseteadas, malware removido.
```

---

## 6. Presentación en tribunal

### Preparación

| Aspecto | Consejo |
|---|---|
| **Conocer la audiencia** | Jueces, jurados, abogados |
| **Simplificar** | Usar analogías, evitar jerga |
| **Visualizar** | Diagramas, timelines, screenshots |
| **Practicar** | Ensayar explicaciones de 5 minutos |
| **Anticipar preguntas** | Preparar respuestas a objeciones |

### Cómo explicar conceptos técnicos

```markdown
# MAL:
"El atacante utilizó PowerShell con codificación base64 para 
ejecutar un reverse shell que estableció una conexión TCP 
persistente al servidor C2."

# BIEN:
"El atacante envió un correo electrónico con un archivo adjunto 
que, cuando se abrió, ejecutó código malicioso en el sistema. 
Este código creó una conexión secreta a un servidor controlado 
por el atacante, permitiéndole controlar la computadora 
remotamente durante 48 horas."
```

---

## 7. Errores comunes

| Error | Consecuencia | Cómo evitar |
|---|---|---|
| **Sin metodología** | Evidencia inadmisible | Seguir NIST 800-86 |
| **Sin cadena de custodia** | Impugnación de evidencia | Documentar todo |
| **Lenguaje subjetivo** | Descredibilidad | Ser objetivo y preciso |
| **Sin evidencia** | Hallazgos no verificables | Siempre citar fuentes |
| **Incompleto** | Análisis cuestionado | Cubrir todas las áreas |
| **Sin revisión** | Errores en el reporte | Peer review |

---

## 8. Referencias

| Recurso | URL |
|---|---|
| **NIST SP 800-86** | [https://csrc.nist.gov/pubs/sp/800/86/final](https://csrc.nist.gov/pubs/sp/800/86/final) |
| **RFC 3227** | [https://www.rfc-editor.org/rfc/rfc3227](https://www.rfc-editor.org/rfc/rfc3227) |
| **SANS FOR508** | [https://www.sans.org/cyber-security-courses/advanced-incident-response/](https://www.sans.org/cyber-security-courses/advanced-incident-response/) |
| **EnCase Forensic** | [https://www.opentext.com/products/digital-forensics](https://www.opentext.com/products/digital-forensics) |

---

**[⬅ Timeline Forense](./01-construccion-timeline.md)** · **[Volver al módulo](../README.md)**
