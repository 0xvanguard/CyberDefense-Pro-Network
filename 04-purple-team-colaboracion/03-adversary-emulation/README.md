# ⚔️ Módulo 03 — Adversary Emulation (Atomic Red Team + CALDERA)

> **Nivel:** Avanzado · **Área:** Purple Team
>
> Objetivo: **emular técnicas de adversarios reales** para validar que tus detecciones funcionan. Aquí el Red Team se convierte en instrumento de medición del Blue Team.

---

## Índice

1. [Pentest vs Red Team vs Emulation](#1-pentest-vs-red-team-vs-emulation)
2. [Atomic Red Team (técnica a técnica)](#2-atomic-red-team-técnica-a-técnica)
3. [CALDERA (operaciones automatizadas)](#3-caldera-operaciones-automatizadas)
4. [El bucle Purple: emular → detectar → mejorar](#4-el-bucle-purple-emular--detectar--mejorar)
5. [Referencias](#5-referencias)

---

## 1. Pentest vs Red Team vs Emulation

| | Pentest | Red Team | **Adversary Emulation** |
|---|---|---|---|
| **Objetivo** | Encontrar vulnerabilidades | Probar detección+respuesta | **Validar detecciones específicas** |
| **Alcance** | Amplio | Campaña completa | Técnica(s) puntual(es) |
| **Sigilo** | No prioritario | Máximo | No prioritario |
| **Repetible** | No | No | **Sí (automatizable)** |

> La emulación es la herramienta del Purple Team: ejecutas **exactamente** la técnica (ej. T1059.001) y miras si tu SIEM dispara. Si no dispara, tienes un **hueco de detección** medible.

---

## 2. Atomic Red Team (técnica a técnica)

**Atomic Red Team** (Red Canary) es una librería de **tests atómicos** mapeados a ATT&CK: pequeños scripts que ejecutan una técnica de forma controlada.

### 2.1 Instalación (PowerShell, en el host de pruebas)

```powershell
# Descargar e instalar el framework
IEX (IWR 'https://raw.githubusercontent.com/redcanaryco/invoke-atomicredteam/master/install-atomicredteam.ps1' -UseBasicParsing)

# Instalar las "atomics" (los tests) en C:\AtomicRedTeam\
Install-AtomicRedTeam -getAtomics

# Cargar el módulo
Import-Module "C:\AtomicRedTeam\invoke-atomicredteam\Invoke-AtomicRedTeam.psd1" -Force
```

> ⚠️ Ejecuta SIEMPRE en un **host de laboratorio aislado**, nunca en producción.

### 2.2 Ver una técnica (antes de ejecutar)

```powershell
# Ver los tests disponibles para una técnica ATT&CK
Invoke-AtomicTest T1059.001 -ShowDetails
```

Esto lista cada test con su **nombre, descripción, comando y dependencias**.

### 2.3 Ejecutar una técnica

```powershell
# Comprobar prerequisitos (dependencias del test)
Invoke-AtomicTest T1059.001 -CheckPrereqs

# Instalar prerequisitos
Invoke-AtomicTest T1059.001 -GetPrereqs

# Ejecutar el test
Invoke-AtomicTest T1059.001

# Limpiar (borrar lo que el test dejó)
Invoke-AtomicTest T1059.001 -Cleanup
```

### 2.4 Técnicas clave para validar un SOC

| Técnica | Qué emula | Qué debe detectar tu SIEM |
|---|---|---|
| `T1059.001` | PowerShell (posiblemente codificado) | Sysmon EID 1 + `-enc` |
| `T1003.001` | Acceso/dump de LSASS | Sysmon EID 10 |
| `T1053.005` | Scheduled task (persistencia) | Sysmon EID 1 + `schtasks /create` |
| `T1083` | Enumeración de archivos/directorios | Comandos de discovery |
| `T1078` | Login con cuentas válidas | Logs de auth + geo anómalo |
| `T1110` | Fuerza bruta | Auth fail + frequency |

### 2.5 Automatizar la validación

```powershell
# Ejecutar varias técnicas en secuencia y dejar que el SIEM las registre
Invoke-AtomicTest T1059.001, T1053.005, T1003.001 -GetPrereqs
Invoke-AtomicTest T1059.001, T1053.005, T1003.001
```

Después, ve al SIEM (Wazuh/Splunk) y verifica **qué alertas dispararon y cuáles no**.

---

## 3. CALDERA (operaciones automatizadas)

**CALDERA** (MITRE) es una plataforma que **automatiza** la emulación de adversarios: define un "adversario" (perfil de TTPs), despliega agentes y ejecuta una **operación** completa.

### 3.1 Arquitectura

```
CALDERA Server (UI + API)
        │
        ├── Agents (implant "Sandcat" en los hosts)
        ├── Abilities (cada técnica ejecutable)
        ├── Adversaries (perfiles: ej. APT29, Discovery)
        └── Operations (campaña contra un grupo de agentes)
```

### 3.2 Instalación (Docker)

```bash
git clone https://github.com/mitre/caldera.git --recursive
cd caldera
docker build . -t caldera:latest
docker run -p 8888:8888 caldera:latest
```

Accede a `http://localhost:8888`. Credenciales por defecto: `admin` / `admin` (o `red` / `admin` para el rol Red en versiones recientes).

### 3.3 Ejecutar una operación

1. **Desplegar un agente** en el host de pruebas (copiar el comando `Sandcat` que CALDERA genera).
2. **Elegir un adversario** (p.ej. `Discovery` para empezar, luego `APT29`-style).
3. **Crear una operación** contra ese agente.
4. **Correr** la operación y observar las *abilities* ejecutándose.

Mientras CALDERA opera, **tu SIEM debe estar capturando**. Al terminar:

```text
1. Extrae las técnicas ejecutadas (CALDERA te dice cuáles fueron).
2. Cruza con las alertas de tu SIEM.
3. Lista las técnicas ejecutadas PERO no detectadas → huecos.
```

### 3.4 Plugins útiles

| Plugin | Uso |
|---|---|
| `atomic` | Importa Atomic Red Team como abilities |
| `stockpile` | Librería de abilities lista |
| `manx` | Comunicación C2 (TCP/UDP) |
| `sandcat` | Agente por defecto |
| `training` | Certificaciones/retos internos |

---

## 4. El bucle Purple: emular → detectar → mejorar

```
        ┌──────────────────────────────────────┐
        │                                       │
        ▼                                       │
1. Elegir técnica ATT&CK                        │
2. Emular (Atomic Red Team / CALDERA)          │
3. Observar SIEM: ¿disparó alerta?             │
        │                                       │
        ├── SÍ → medir precision/FP (ver módulo 02) ──┐
        │                                            │
        └── NO → HUECO: escribir regla nueva          │
                    (Sigma/YARA/Wazuh)               │
                    volver a emular ─────────────────┘
```

### 4.1 Formato de resultado (por técnica)

```text
TÉCNICA: T1059.001 (PowerShell)
EMULADO CON: Atomic Red Team
RESULTADO SIEM: alerta disparada ✅ / no disparada ❌
REGLA: powershell_encoded (Sigma) → estado: ACTIVA
MÉTRICAS: precision 85%, FP 2/día
ACCIÓN: (nada / subir umbral / nueva regla / añadir telemetría)
```

**Entregable de portafolio:** una tabla con 10 técnicas emuladas, su resultado de detección (✅/❌) y las reglas creadas para cerrar los huecos.

---

## 5. Referencias

- [Atomic Red Team (oficial)](https://github.com/redcanaryco/atomic-red-team)
- [CALDERA (MITRE, oficial)](https://github.com/mitre/caldera)
- [MITRE ATT&CK](https://attack.mitre.org/)
- [Detection Engineering (módulo anterior)](../02-detection-engineering/)

---

**[⬅ Detection Engineering](../02-detection-engineering/)** · **[⬅ Volver al README de Purple Team](../README.md)**
