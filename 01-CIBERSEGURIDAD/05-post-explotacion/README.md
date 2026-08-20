# 🕳️ Módulo 05 — Post-Explotación

> **Nivel:** Avanzado · **Objetivo:** dominar lo que ocurre **después** de obtener acceso: escalada de privilegios, persistencia y movimiento lateral.

[![Nivel](https://img.shields.io/badge/Nivel-Avanzado-red?style=flat-square)]()
[![Enfoque](https://img.shields.io/badge/Enfoque-Red%20Team-red?style=flat-square)]()

---

## 📋 Resumen

| Atributo | Detalle |
|---|---|
| 🎯 **Resultado** | Escalar privilegios, mantener persistencia y moverse lateralmente de forma controlada |
| 🧪 **Práctica** | LinPEAS/WinPEAS, Mimikatz, Impacket, HTB/THM |
| 🗂️ **Portafolio** | Writeup con metodología documentada |
| 🔗 **Requiere** | [Módulo 04 — Explotación Web](../04-explotacion-web/) |

---

## 🎯 Objetivos de aprendizaje

Al completar este módulo deberías ser capaz de:

- **Escalada de privilegios:** identificar y explotar vectores de escalada en Linux (SUID, sudo, capabilities, kernel) y Windows (services, tokens, UAC, potato attacks).
- **Persistencia:** establecer acceso persistente que sobreviva reinicios en ambos sistemas operativos.
- **Movimiento lateral:** moverte por la red usando pass-the-hash, WinRM, PsExec, Kerberoasting y pivoting.
- **Detección:** entender cómo cada técnica se detecta desde el lado defensivo (Blue Team).
- **Herramientas:** dominar LinPEAS, WinPEAS, Mimikatz, Impacket, CrackMapExec y BloodHound.

---

## 🗂️ Estructura del módulo

| Carpeta | Contenido | Estado |
|---|---|---|
| [`privilege-escalation/`](./privilege-escalation/) | Escalada Linux/Windows | ✅ Completado |
| [`persistence/`](./persistence/) | Persistencia Linux/Windows | ✅ Completado |
| [`lateral-movement/`](./lateral-movement/) | Movimiento lateral | ✅ Completado |

### 📚 Contenido detallado

#### 1. Escalada de Privilegios

| Archivo | Contenido |
|---|---|
| [`01-linux-privesc.md`](./privilege-escalation/01-linux-privesc.md) | SUID, sudo abuse, capabilities, kernel exploits, cron jobs, NFS root squashing, Docker escape, LinPEAS |
| [`02-windows-privesc.md`](./privilege-escalation/02-windows-privesc.md) | Service misconfigs, unquoted paths, DLL hijacking, token impersonation, UAC bypass, Potato attacks, kernel exploits, WinPEAS |

#### 2. Persistencia

| Archivo | Contenido |
|---|---|
| [`01-linux-persistence.md`](./persistence/01-linux-persistence.md) | SSH keys, cron jobs, systemd services, init scripts, SUID binaries, LD_PRELOAD, bashrc injection, PAM backdoors |
| [`02-windows-persistence.md`](./persistence/02-windows-persistence.md) | Registry Run keys, scheduled tasks, Windows services, DLL hijacking, startup folder, WMI, COM hijacking, BITS |

#### 3. Movimiento Lateral

| Archivo | Contenido |
|---|---|
| [`01-lateral-movement.md`](./lateral-movement/01-lateral-movement.md) | PsExec, WinRM, Pass-the-Hash, Pass-the-Ticket, Kerberoasting, Mimikatz, SSH tunneling, RDP hijacking |

---

## 🛠️ Herramientas principales

| Herramienta | Plataforma | Uso principal |
|---|---|---|
| **LinPEAS** | Linux | Enumeración automática de vectores de escalada |
| **WinPEAS** | Windows | Enumeración automática de vectores de escalada |
| **Mimikatz** | Windows | Extracción de credenciales y tokens |
| **Impacket** | Linux | PsExec, WMIExec, SecretsDump, Kerberoasting |
| **CrackMapExec** | Linux | Autenticación masiva, pass-the-hash, enumeración |
| **BloodHound** | Linux/Windows | Mapeo de rutas de ataque en Active Directory |
| **Evil-WinRM** | Linux | Shell remota con WinRM |

---

## ⚖️ Aviso ético

Todas las técnicas se practican solo en laboratorios aislados o plataformas autorizadas (HTB, THM, VMs propias). El uso no autorizado de estas técnicas es **ilegal** y puede resultar en consecuencias penales graves.

---

## 🔗 Encaje del módulo en la ruta

Dentro de la **Ruta 2 (Red Team)**, este módulo es la **Fase C**:

1. `01-reconocimiento-osint/` ← Reconocimiento
2. `02-pentesting-red-team/` ← Ciclo de pentest
3. `03-analisis-vulnerabilidades/` ← Análisis
4. `04-explotacion-web/` ← Explotación (pré-requisito)
5. **`05-post-explotacion/`** ← **Este módulo** (Fase C)

---

## ✅ Checkpoint

¿Puedes hacer lo siguiente sin guía?

- [ ] Escalar de usuario a root/SYSTEM en un sistema vulnerable
- [ ] Establecer persistencia que sobreviva un reinicio
- [ ] Moverte lateralmente a otro host en la red
- [ ] Explicar cómo cada técnica se detecta desde Blue Team

Si todo es ✅, estás listo para el siguiente paso: **[Módulo 06 — Forense Digital](../06-forense-digital/)**.

---

**[⬅ Volver a Ciberseguridad](../README.md)** · **[🗺️ Ver Rutas](../../RUTAS.md)**
