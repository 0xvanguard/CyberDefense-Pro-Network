# 📜 Módulo 06 — Compliance y Normativas

> **Objetivo principal:** Comprender y aplicar marcos de compliance de seguridad de la información (ISO 27001, GDPR, Ley 1581 de Colombia, NIST CSF) en organizaciones reales.

[![Nivel](https://img.shields.io/badge/Nivel-Intermedio%20→%20Avanzado-orange?style=flat-square)]()
[![Enfoque](https://img.shields.io/badge/Enfoque-GRC%20%7C%20Compliance-red?style=flat-square)]()
[![Frameworks](https://img.shields.io/badge/Frameworks-ISO%2027001%20%7C%20GDPR%20%7C%20NIST%20CSF-blue?style=flat-square)]()

---

## 📋 Resumen del módulo

| Atributo | Detalle |
|---|---|
| 🏷️ **Nivel** | Intermedio → Avanzado |
| ⏱️ **Duración estimada** | 4–6 semanas |
| 🎯 **Resultado esperado** | Implementar un ISMS básico, realizar un gap analysis y crear documentación de compliance |
| 🧪 **Práctica verificable** | Gap analysis real, política de seguridad, Statement of Applicability |
| 🗂️ **Portafolio** | Documentos de compliance listos para revisión |
| 🔗 **Requiere** | Fundamentos de seguridad de la información |
| 🔗 **Conduce a** | Auditoría, GRC, CISO |

---

## 🎯 Qué aprenderás

- [ ] Entender la estructura y requisitos de ISO 27001:2022
- [ ] Implementar un Information Security Management System (ISMS)
- [ ] Aplicar GDPR en el contexto de protección de datos personales
- [ ] Cumplir con la Ley 1581 de 2012 (Colombia) de protección de datos
- [ ] Utilizar NIST Cybersecurity Framework para gestión de riesgos
- [ ] Realizar gap analysis y crear planes de acción

---

## 🗂️ Estructura del módulo

```
06-compliance-normativas/
├── README.md                      ← Este archivo
├── iso-27001/
│   ├── README.md                 ← ISO 27001:2022 completo
│   ├── isms-implementation.md    ← Guía de implementación ISMS
│   ├── statement-of-applicability.md ← SoA template
│   └── internal-audit.md         ← Auditoría interna
├── gdpr/
│   ├── README.md                 ← GDPR explicado
│   ├── data-mapping.md           ← Mapeo de datos personales
│   ├── dpias.md                  ← Data Protection Impact Assessment
│   └── data-breach-response.md   ← Respuesta a brechas
├── colombia-ley-1581/
│   ├── README.md                 ← Ley 1581 de 2012
│   ├── autoridad-proteccion.md   ← SIC Colombia
│   └── politicas-datos.md        ← Políticas de tratamiento
└── portafolio/
    └── template-compliance.md    ← Plantilla de reporte
```

---

## 📚 Contenido del módulo

### FASE 1 — ISO 27001:2022 (Semana 1-2)

#### 1.1 Estructura del Estándar
ISO 27001:2022 sigue la estructura HLS (High Level Structure):

| Cláusula | Contenido |
|----------|-----------|
| 4. Contexto de la organización | Partes interesadas, alcance |
| 5. Liderazgo | Compromiso de la dirección, política |
| 6. Planificación | Evaluación de riesgos, tratamiento |
| 7. Soporte | Recursos, competencia, comunicación |
| 8. Operación | Implementación del ISMS |
| 9. Evaluación del desempeño | Monitoreo, auditoría interna |
| 10. Mejora continua | No conformidades, acciones correctivas |

#### 1.2 Controles de ISO 27001:2022
El nuevo estándar tiene **93 controles** organizados en 4 temas:

| Tema | Controles | Ejemplos |
|------|-----------|----------|
| **Organizacionales** (37) | Politicas, roles, clasificación | A.5.1 Políticas de seguridad |
| **Personas** (8) | Screening, concienciación, contratos | A.6.3 Conciamiento en seguridad |
| **Físicos** (14) | Perímetros, controles de acceso | A.7.1 Seguridad de perímetros |
| **Tecnológicos** (34) | Cifrado, accesos, desarrollo | A.8.1 Dispositivos de usuario |

#### 1.3 Implementación ISMS Paso a Paso
```
1. Definir alcance del ISMS
2. Identificar partes interesadas
3. Definir política de seguridad
4. Realizar evaluación de riesgos
5. Seleccionar controles (SoA)
6. Implementar controles
7. Establecer métricas (KRI/KPI)
8. Realizar auditoría interna
9. Revisión por la dirección
10. Mejora continua (PDCA)
```

---

### FASE 2 — GDPR (Semana 3)

#### 2.1 Principios Clave del GDPR

| Principio | Descripción |
|-----------|-------------|
| **Legalidad** | Base legal para cada tratamiento |
| **Limitación de finalidad** | Solo para fines específicos |
| **Minimización** | Solo datos necesarios |
| **Exactitud** | Datos actualizados |
| **Limitación de almacenamiento** | Solo el tiempo necesario |
| **Integridad y confidencialidad** | Seguridad adecuada |
| **Rendición de cuentas** | Demostrar cumplimiento |

#### 2.2 Derechos del Titular

| Derecho | Descripción | Plazo |
|---------|-------------|-------|
| Acceso | Copia de sus datos | 1 mes |
| Rectificación | Corregir datos inexactos | 1 mes |
| Supresión | "Derecho al olvido" | 1 mes |
| Portabilidad | Obtener datos en formato estructurado | 1 mes |
| Oposición | Oponerse al tratamiento | Sin demora |
| Limitación | Restringir el tratamiento | 1 mes |

#### 2.3 Data Protection Impact Assessment (DIA)
Obligatorio cuando el tratamiento implica:
- Evaluación automatizada con efectos significativos
- Tratamiento a gran escala de datos sensibles
- Monitorización sistemática de áreas públicas

---

### FASE 3 — Ley 1581 de 2012 (Colombia) (Semana 4)

#### 3.1 Alcance
Aplica a todo responsable y encargado del tratamiento de datos personales en Colombia, incluyendo:
- Empresas privadas
- Entidades públicas
- Organizaciones sin ánimo de lucro
- Empresas extranjeras que traten datos de colombianos

#### 3.2 Principios (Art. 4)
1. **Legalidad:** Tratamiento conforme a la ley
2. **Finalidad:** Cumplir una finalidad legítima
3. **Libertad:** Consentimiento previo, expreso e informado
4. **Veracidad:** Información veraz y completa
5. **Transparencia:** Derecho a conocer el tratamiento
6. **Seguridad:** Medidas técnicas y organizativas
7. **Confidencialidad:** Reserva sobre los datos
8. **Acceso restringido:** Solo autorizados

#### 3.3 Obligaciones del Responsable
- Registrar tratamientos en el Registro Nacional
- Implementar políticas de tratamiento
- Designar un encargado de protección de datos
- Informar al titular sobre el tratamiento
- Atender consultas y quejas
- Garantizar derechos ARCO (Acceso, Rectificación, Cancelación, Oposición)

---

### FASE 4 — NIST Cybersecurity Framework (Semana 5)

#### 4.1 Funciones del NIST CSF 2.0

```
Govern → Identify → Protect → Detect → Respond → Recover
  ↑                                                    |
  └────────────────────────────────────────────────────┘
                    (Mejora continua)
```

| Función | Descripción | Categorías |
|---------|-------------|------------|
| **Govern** | Gobernanza de riesgos | Estrategia, Roles, Políticas |
| **Identify** | Entender el entorno | Activos, Riesgos, Supply Chain |
| **Protect** | Implementar protecciones | Identidades, Datos, Plataformas |
| **Detect** | Detectar eventos | Anomalías, Actividades adversas |
| **Respond** | Responder a incidentes | Gestión, Comunicación, Mitigación |
| **Recover** | Recuperarse | Planes de recuperación, Mejoras |

---

## 🧪 Laboratorios

| Lab | Descripción | Nivel |
|-----|-------------|-------|
| `lab-01` | Gap analysis ISO 27001 en empresa ficticia | Básico |
| `lab-02` | Crear Statement of Applicability (SoA) | Intermedio |
| `lab-03` | Data mapping para GDPR | Intermedio |
| `lab-04` | Simulacro de respuesta a data breach | Avanzado |
| `lab-05` | NIST CSF assessment completo | Avanzado |

---

## 📊 Métricas de éxito

| Métrica | Objetivo |
|---------|----------|
| ISO 27001 gap analysis | Completado |
| SoA creado | 93 controles evaluados |
| GDPR data mapping | Datos personales identificados |
| Ley 1581 compliance checklist | 100% cumplido |
| NIST CSF score | > 3.0 en todas las funciones |

---

## 🔗 Referencias

- [ISO 27001:2022](https://www.iso.org/standard/27001)
- [GDPR Official Text](https://gdpr-info.eu/)
- [Ley 1581 de 2012 - Colombia](https://www.funcionpublica.gov.co/eva/gestornormativo/norma.php?i=44344)
- [NIST CSF 2.0](https://www.nist.gov/cyberframework)
- [CIS Controls v8](https://www.cisecurity.org/controls)
- [SIC Colombia - Superintendencia](https://www.sic.gov.co/)

---

*Última actualización: Agosto 2026*
*CyberDefense-Pro-Network — Aprende haciendo. Demuestra con evidencia.*
