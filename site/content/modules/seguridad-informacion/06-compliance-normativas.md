---
title: "Módulo 06 — Compliance y Normativas"
---

# 📜 Módulo 06 — Compliance y Normativas

> **Objetivo:** Mapear controles técnicos a requisitos legales y regulatorios (GDPR, ISO 27001, PCI DSS).

[![Nivel](https://img.shields.io/badge/Nivel-Intermedio-orange?style=flat-square)]()
[![Duración](https://img.shields.io/badge/Duración-1.5%20meses-blue?style=flat-square)]()

---

## 📋 Resumen del módulo

| Atributo | Detalle |
|----------|---------|
| **Pre-requisitos** | Fundamentos completados |
| **Marcos** | GDPR, ISO 27001, PCI DSS, HIPAA |
| **Herramientas** | OpenSCAP, Compliance-as-Code |
| **Nivel** | Intermedio |

---

## 1. 🧠 Teoría: ¿Qué es Compliance?

Compliance = **cumplimiento** de leyes, regulaciones y estándares aplicables a tu organización.

### Marcos principales

| Marco | Alcance | Multa máxima |
|-------|---------|--------------|
| **GDPR** | Datos personales UE | €20M o 4% facturación |
| **ISO 27001** | SGSI | Certificación |
| **PCI DSS** | Datos de tarjetas | $500K/mes |
| **HIPAA** | Datos de salud US | $1.5M/año |
| **SOC 2** | Servicios cloud | Pérdida de clientes |
| **Ley 1581 (Colombia)** | Habeas Data | 2000 SMMLV |

---

## 2. 📋 GDPR — Reglamento General de Protección

### Principios clave

1. **Licitud, lealtad y transparencia**
2. **Limitación de finalidad**
3. **Minimización de datos**
4. **Exactitud**
5. **Limitación de conservación**
6. **Integridad y confidencialidad**
7. **Responsabilidad demostrada**

### Derechos del titular

| Derecho | Descripción |
|---------|-------------|
| **Acceso** | Conocer qué datos tengo |
| **Rectificación** | Corregir datos incorrectos |
| **Supresión** | "Derecho al olvido" |
| **Portabilidad** | Llevar mis datos a otro servicio |
| **Oposición** | Negarse al procesamiento |
| **Limitación** | Restringir el procesamiento |

---

## 3. 📋 ISO 27001:2022

### Estructura del estándar

```
Clausa 4  → Contexto de la organización
Clausa 5  → Liderazgo
Clausa 6  → Planificación
Clausa 7  → Apoyo
Clausa 8  → Operación
Clausa 9  → Evaluación del desempeño
Clausa 10 → Mejora continua
Anexo A   → 93 controles de seguridad
```

### Controles del Anexo A

| Categoría | Controles | Ejemplos |
|-----------|-----------|----------|
| **A.5** Organizacionales | 37 | Politicas, roles, concienciación |
| **A.6** Personas | 8 | Screening, contraseñas, teletrabajo |
| **A.7** Físicos | 14 | Perímetros, controles de acceso |
| **A.8** Tecnológicos | 34 | Cifrado, backups, desarrollo seguro |

---

## 4. 📋 PCI DSS v4.0

### 12 requisitos

1. Instalar y mantener controles de seguridad de red
2. Proteger todos los datos de cuentas almacenados
3. Proteger datos almacenados con cifrado
4. Cifrar transmisión de datos en redes públicas
5. Usar y actualizar antivirus regularmente
6. Desarrollar sistemas seguros
7. Restringir acceso por necesidad de negocio
8. Identificar usuarios y autenticar acceso
9. Restringir acceso físico a datos de cuenta
10. Monitorear y probar redes
11. Mantener políticas de seguridad
12. Mantener política de seguridad de información

---

## 5. ✏️ Ejercicios prácticos

### Ejercicio 1: Mapeo GDPR (30 min)

1. Identifica 3 tipos de datos personales que maneja tu organización
2. Para cada uno, documenta:
   - Base legal del procesamiento
   - Período de conservación
   - Medidas de seguridad implementadas
   - Derechos aplicables

### Ejercicio 2: Gap analysis ISO 27001 (40 min)

1. Descarga el checklist de ISO 27001 Annex A
2. Evalúa 10 controles contra tu organización
3. Clasifica: Implementado / Parcial / No implementado
4. Identifica las 3 brechas más críticas

### Ejercicio 3: Crear política de privacidad (30 min)

1. Escribe una política de privacidad básica que incluya:
   - Qué datos recopilas
   - Para qué los usas
   - Con quién los compartes
   - Cómo proteges
   - Cómo ejercer derechos

---

> **Siguiente:** [Módulo 07 — Threat Intelligence](./07-threat-intelligence)
