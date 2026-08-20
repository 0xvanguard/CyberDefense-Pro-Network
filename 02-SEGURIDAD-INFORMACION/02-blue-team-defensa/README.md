# 🔵 Módulo 02 — Blue Team y Defensa

> **Nivel:** Intermedio → Avanzado · **Objetivo:** defender, detectar y cazar amenazas como un profesional SOC/Blue Team.

[![Nivel](https://img.shields.io/badge/Nivel-Intermedio%20%E2%86%92%20Avanzado-blue?style=flat-square)]()
[![Enfoque](https://img.shields.io/badge/Enfoque-Defensivo-blue?style=flat-square)]()
[![Marcos](https://img.shields.io/badge/Marcos-MITRE%20ATT%26CK%20%7C%20D3FEND-red?style=flat-square)]()

---

## 📋 Resumen

| Atributo | Detalle |
|---|---|
| 🎯 **Resultado** | Montar un SIEM, escribir detección propia (Sigma/YARA/Wazuh) y cazar amenazas con método |
| 🧪 **Práctica** | Wazuh en Docker + Sysmon/Suricata + reglas custom verificadas |
| 🗂️ **Portafolio** | Reglas de detección mapeadas a ATT&CK + hunts documentados |
| 🔗 **Requiere** | [Ruta de Fundamentos](../../00-FUNDAMENTOS/) |
| 🔗 **Conduce a** | [Módulo 03 — SOC Operations](../03-soc-operations/) |

---

## 🗺️ Estructura del módulo

| Carpeta | Contenido | Estado |
|---|---|---|
| [`siem-wazuh/`](./siem-wazuh/) | Guía profesional de Wazuh: arquitectura, reglas, decoders, Sysmon/Suricata, active response | ✅ Completo |
| [`threat-hunting/`](./threat-hunting/) | Metodología de caza (PEAK) + detección con Sigma y YARA | ✅ Completo |
| [`mitre-d3fend/`](./mitre-d3fend/) | Contramedidas MITRE D3FEND (mapear detección → mitigación) | ⬜ Pendiente |
| [`herramientas/`](./herramientas/) | Configs y cheatsheets de herramientas Blue Team | ⬜ Pendiente |

---

## 🚀 Orden de estudio sugerido

1. Lee [`siem-wazuh/`](./siem-wazuh/) y monta tu Wazuh.
2. Lee [`threat-hunting/`](./threat-hunting/) y escribe tus primeras reglas Sigma/YARA.
3. Practica detección end-to-end (ataque → alerta → respuesta).

---

## ⚖️ Aviso

Todas las detecciones se prueban en laboratorios propios o entornos autorizados.

---

**[⬅ Volver al área de Seguridad de la Información](../README.md)**
