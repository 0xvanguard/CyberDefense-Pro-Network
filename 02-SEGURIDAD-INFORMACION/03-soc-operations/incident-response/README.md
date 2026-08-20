# 🚨 Respuesta a Incidentes — Metodología profesional (NIST SP 800-61)

> **Nivel:** Intermedio → Avanzado · **Marco:** [NIST SP 800-61 Rev. 2](https://csrc.nist.gov/pubs/sp/800/61/r2/final)
>
> Objetivo: manejar un incidente de seguridad con **método, roles y documentación**, no a punta de improvisación. Esto es lo que separa a un SOC amateur de uno profesional.

---

## Índice

1. [El ciclo de vida de un incidente](#1-el-ciclo-de-vida-de-un-incidente)
2. [Roles y responsabilidades](#2-roles-y-responsabilidades)
3. [Clasificación y severidad](#3-clasificación-y-severidad)
4. [Documentación: la timeline y el 5W+H](#4-documentación-la-timeline-y-el-5wh)
5. [Las 4 fases en detalle](#5-las-4-fases-en-detalle)
6. [Referencias](#6-referencias)

---

## 1. El ciclo de vida de un incidente

```
┌────────────────────────────────────────────────────────────┐
│ 1. Preparation          → estar listo ANTES del incidente  │
│ 2. Detection & Analysis → detectar y confirmar             │
│ 3. Containment,         → parar el daño, borrar, recuperar │
│    Eradication & Recovery                                   │
│ 4. Post-Incident         → lecciones aprendidas            │
└────────────────────────────────────────────────────────────┘
```

> Regla clave: **la preparación (fase 1) es la que más se ignora y la que más salva vidas.** Sin playbooks, contactos y herramientas listas, un incidente real se convierte en caos.

---

## 2. Roles y responsabilidades

| Rol | Responsabilidad |
|---|---|
| **Incident Commander (IC)** | Único dueño de decisiones; coordina |
| **Lead Investigator** | Dirige el análisis técnico |
| **SOC Analyst (T1/T2)** | Triage, análisis, contención inicial |
| **Forensics/DFIR** | Evidencia, imágenes, cadena de custodia |
| **Comms / Legal / PR** | Comunicación interna/externa, cumplimiento |
| **IT / Sysadmin** | Acceso, backups, parches |

> En equipos pequeños, una persona asume varios roles, pero **siempre debe haber un único IC** para evitar decisiones contradictorias.

---

## 3. Clasificación y severidad

| Severidad | Definición | Ejemplo | Tiempo de respuesta |
|---|---|---|---|
| **S1 — Crítico** | Datos sensibles comprometidos, impacto masivo | Ransomware activo en prod | Inmediato (24/7) |
| **S2 — Alto** | Compromiso confirmado, alcance limitado | Cuenta admin comprometida | < 1 h |
| **S3 — Medio** | Sospecha o malware aislado | Phishing clickeado sin credenciales | < 4 h |
| **S4 — Bajo** | Evento anómalo, sin confirmación | Escaneo de puertos | Horario laboral |

---

## 4. Documentación: la timeline y el 5W+H

Todo incidente profesional se registra como una **timeline** (línea de tiempo) con eventos ordenados. Cada evento responde al **5W+H**:

| Pregunta | Qué documentar |
|---|---|
| **Who** | Usuario, host, cuenta, IP |
| **What** | Qué pasó (acción, técnica) |
| **When** | Timestamp exacto (UTC) |
| **Where** | Sistema, ruta, archivo |
| **Why** | Causa raíz / vector de entrada |
| **How** | Cómo se detectó y cómo se explotó |

Ejemplo de entrada de timeline:

```text
2026-08-20 14:32:11 UTC | WHO: user@corp.com | WHAT: login fallido x12 | WHERE: vpn.corp.com | WHY: fuerza bruta | HOW: alerta SIEM #44321
```

---

## 5. Las 4 fases en detalle

### 5.1 Preparation (preparación)

- [ ] Playbooks escritos (phishing, ransomware, compromiso de credenciales).
- [ ] Contactos de escalamiento (IC, legal, PR, dueños de sistemas).
- [ ] Herramientas listas (SIEM, EDR, forense, sandbox).
- [ ] Backups verificados y aislados (offline/immutable).
- [ ] Canales de comunicación fuera de banda (por si el correo está comprometido).
- [ ] Roles asignados y probados (tabletop exercises).

### 5.2 Detection & Analysis (detección y análisis)

Pasos:

1. **Identificar** el vector de entrada (phishing, RDP, web, USB...).
2. **Confirmar** el incidente (no toda alerta es incidente).
3. **Determinar alcance** (¿qué hosts/usuarios/datos están afectados?).
4. **Documentar** la timeline desde el primer indicador.

Preguntas clave de análisis:

- ¿Es un falso positivo o un evento real?
- ¿Cuál es el indicador primario (hash, IP, cuenta, técnica)?
- ¿Cuántos sistemas han sido tocados (blast radius)?
- ¿El atacante sigue dentro (activo) o ya no?

### 5.3 Containment, Eradication & Recovery

| Sub-fase | Acciones | Herramientas |
|---|---|---|
| **Containment** (corto plazo) | Aislar hosts (red/EDR), deshabilitar cuentas, bloquear IOCs | EDR, firewall, SIEM active response |
| **Containment** (largo plazo) | Segmentar red, cambiar credenciales, imagen forense | Firewall, DFIR |
| **Eradication** | Borrar malware, cerrar la vuln, eliminar persistencia | AV/EDR, parches |
| **Recovery** | Restaurar backups, re-online gradual, monitorear | Backup, SIEM |

> **Decisión crítica:** ¿contención inmediata (destruir evidencia) o forense primero (preservar evidencia)? Se decide según el riesgo vs. valor legal. **Documenta siempre la decisión y el porqué.**

### 5.4 Post-Incident Activity (lecciones aprendidas)

Reunión post-mortem **sin culpar personas** (blameless). Documentar:

1. Qué pasó (timeline final).
2. Qué funcionó bien.
3. Qué falló (proceso, detección, comunicación).
4. Acciones correctivas con **dueño y fecha**.
5. Actualizar playbooks y reglas de detección.

**Entregable:** informe post-incident + playbook actualizado.

---

## 6. Referencias

- [NIST SP 800-61 Rev. 2 — Computer Security Incident Handling Guide](https://csrc.nist.gov/pubs/sp/800/61/r2/final)
- [SANS Incident Handler's Handbook](https://www.sans.org/white-papers/33901/)
- [NIST SP 800-86 — Guide to Integrating Forensic Techniques into IR](https://csrc.nist.gov/pubs/sp/800/86/final)

---

**[⬅ Volver al módulo SOC](../README.md)** · **[→ Playbook de phishing](../playbooks/playbook-phishing.md)**
