# 🛠️ Herramientas de Análisis de Memoria

> *"Cada herramienta de análisis de memoria es una lupa diferente para ver lo que el atacante intentó ocultar."*

---

## 📋 Tabla de contenido

1. [Volatility 3: plugins avanzados](#1-volatility-3-plugins-avanzados)
2. [Volatility 2: diferencias con v3](#2-volatility-2-diferencias-con-v3)
3. [Rekall](#3-rekall)
4. [Comparativa de herramientas](#4-comparativa-de-herramientas)
5. [Scripts de automatización](#5-scripts-de-automatización)
6. [Análisis con LiME en Linux](#6-análisis-con-lime-en-linux)
7. [Referencias](#7-referencias)

---

## 1. Volatility 3: plugins avanzados

### Plugins de Windows

| Plugin | Descripción | Ejemplo de uso |
|---|---|---|
| `windows.info` | Info del sistema y perfil | `vol -f mem.raw windows.info` |
| `windows.pslist` | Lista de procesos | `vol -f mem.raw windows.pslist` |
| `windows.pstree` | Árbol de procesos | `vol -f mem.raw windows.pstree` |
| `windows.cmdline` | Comandos de cada proceso | `vol -f mem.raw windows.cmdline` |
| `windows.netscan` | Conexiones de red | `vol -f mem.raw windows.netscan` |
| `windows.malfind` | Código inyectado | `vol -f mem.raw windows.malfind` |
| `windows.hashdump` | Credenciales NTLM | `vol -f mem.raw windows.hashdump` |
| `windows.lsadump` | Credenciales LSA | `vol -f mem.raw windows.lsadump` |
| `windows.cachedump` | Caché de credenciales | `vol -f mem.raw windows.cachedump` |
| `windows.dlllist` | DLLs de un proceso | `vol -f mem.raw windows.dlllist --pid 1234` |
| `windows.handles` | Handles de un proceso | `vol -f mem.raw windows.handles --pid 1234` |
| `windows.filescan` | Archivos en memoria | `vol -f mem.raw windows.filescan` |
| `windows.svcscan` | Servicios | `vol -f mem.raw windows.svcscan` |
| `windows.driverscan` | Drivers | `vol -f mem.raw windows.driverscan` |
| `windows.modules` | Módulos del kernel | `vol -f mem.raw windows.modules` |
| `windows.registry.hivelist` | Hives de registro | `vol -f mem.raw windows.registry.hivelist` |
| `windows.registry.printkey` | Keys del registro | `vol -f mem.raw windows.registry.printkey --key "..."` |
| `windows.getservicesids` | SIDs de servicios | `vol -f mem.raw windows.getservicesids` |
| `windows.envars` | Variables de entorno | `vol -f mem.raw windows.envars` |
| `windows.registry.userassist` | UserAssist (ejecuciones) | `vol -f mem.raw windows.registry.userassist` |

### Plugins de Linux

| Plugin | Descripción | Ejemplo de uso |
|---|---|---|
| `linux.pslist` | Lista de procesos | `vol -f mem.raw linux.pslist` |
| `linux.pstree` | Árbol de procesos | `vol -f mem.raw linux.pstree` |
| `linux.cmdline` | Comandos ejecutados | `vol -f mem.raw linux.cmdline` |
| `linux.bash` | Historial de bash | `vol -f mem.raw linux.bash` |
| `linux.check_syscall` | Syscalls hookadas | `vol -f mem.raw linux.check_syscall` |
| `linux.check_idt` | IDT hookada | `vol -f mem.raw linux.check_idt` |
| `linux.lsmod` | Módulos del kernel | `vol -f mem.raw linux.lsmod` |
| `linux.proc_maps` | Mapas de memoria | `vol -f mem.raw linux.proc_maps --pid 1234` |
| `linux.tty_check` | TTY hash table | `vol -f mem.raw linux.tty_check` |

### Ejemplos avanzados

#### Buscar processes por nombre

```bash
# Filtrar procesos por nombre
vol -f memory.raw windows.pslist | grep -i "chrome\|firefox\|edge"

# Buscar todos los svchost.exe
vol -f memory.raw windows.pslist | grep svchost

# Contar procesos
vol -f memory.raw windows.pslist | wc -l
```

#### Analizar un proceso específico

```bash
# Ver todo de un proceso específico
PID=5567

# Comando ejecutado
vol -f memory.raw windows.cmdline --pid $PID

# DLLs cargadas
vol -f memory.raw windows.dlllist --pid $PID

# Handles abiertos
vol -f memory.raw windows.handles --pid $PID

# Código inyectado
vol -f memory.raw windows.malfind --pid $PID

# Volcar memoria del proceso
vol -f memory.raw windows.malfind --pid $PID --dump
```

#### Buscar credenciales

```bash
# Hashes NTLM
vol -f memory.raw windows.hashdump > hashes.txt

# Credenciales LSA
vol -f memory.raw windows.lsadump > lsadump.txt

# Caché de credenciales
vol -f memory.raw windows.cachedump > cachedump.txt

# UserAssist (ejecuciones de usuario)
vol -f memory.raw windows.registry.userassist > userassist.txt
```

#### Análisis de red

```bash
# Todas las conexiones
vol -f memory.raw windows.netscan > netscan.txt

# Solo conexiones establecidas
vol -f memory.raw windows.netscan | grep ESTABLISHED

# Conexiones a IPs externas
vol -f memory.raw windows.netscan | grep -v "127.0.0.1\|10.\|192.168."

# Conexiones desde procesos sospechosos
vol -f memory.raw windows.netscan | grep "5567\|4012"
```

---

## 2. Volatility 2: diferencias con v3

### Comandos Volatility 2 vs 3

| Función | Volatility 2 | Volatility 3 |
|---|---|---|
| Info del sistema | `imageinfo` | `windows.info` |
| Procesos | `pslist` | `windows.pslist` |
| Árbol de procesos | `pstree` | `windows.pstree` |
| Comandos | `cmdline` | `windows.cmdline` |
| Red | `netscan` | `windows.netscan` |
| Código inyectado | `malfind` | `windows.malfind` |
| Hashes | `hashdump` | `windows.hashdump` |
| DLLs | `dlllist` | `windows.dlllist` |
| Handles | `handles` | `windows.handles` |
| Archivos | `filescan` | `windows.filescan` |
| Servicios | `svcscan` | `windows.svcscan` |
| Drivers | `driverscan` | `windows.driverscan` |
| Registro | `hivelist` | `windows.registry.hivelist` |

### Sintaxis

```bash
# Volatility 2
volatility -f memory.raw --profile=Win10x64_19041 pslist
volatility -f memory.raw --profile=Win10x64_19041 netscan

# Volatility 3
vol -f memory.raw windows.pslist
vol -f memory.raw windows.netscan
```

### ¿Cuándo usar Volatility 2?

- Cuando Volatility 3 no reconoce el perfil del volcado
- Para plugins no disponibles en v3 (ej: `procdump`, `memdump`)
- Para compatibilidad con scripts heredados

---

## 3. Rekall

### Instalación

```bash
# Rekall es una fork de Volatility con mejoras
pip install rekall

# O desde source
git clone https://github.com/google/rekall.git
cd rekall
python setup.py install
```

### Comandos

```bash
# Info del sistema
rekall -f memory.raw imageinfo

# Procesos
rekall -f memory.raw pslist
rekall -f memory.raw pstree

# Red
rekall -f memory.raw netscan

# Código inyectado
rekall -f memory.raw malfind

# Credenciales
rekall -f memory.raw hashdump
```

### Ventajas de Rekall

| Característica | Volatility | Rekall |
|---|---|---|
| **Velocidad** | Media | Rápida |
| **Perfiles auto** | Semi-automático | Automático |
| **Soporte Linux** | Bueno | Excelente |
| **Desarrollo** | Activo | Poco activo |
| **Comunidad** | Grande | Pequeña |

---

## 4. Comparativa de herramientas

| Herramienta | Plataforma | Velocidad | Comunidad | Uso ideal |
|---|---|---|---|---|
| **Volatility 3** | Multi | Media | ⭐⭐⭐⭐⭐ | Análisis estándar |
| **Volatility 2** | Multi | Media | ⭐⭐⭐⭐ | Compatibilidad |
| **Rekall** | Multi | Rápida | ⭐⭐ | Análisis rápido |
| **Volatility Workbench** | Windows | Media | ⭐⭐⭐ | GUI para Volatility |

### ¿Cuándo usar cada una?

| Necesidad | Herramienta |
|---|---|
| **Análisis estándar** | Volatility 3 |
| **Volcado antiguo (Windows XP/7)** | Volatility 2 |
| **Análisis rápido** | Rekall |
| **GUI sin comandos** | Volatility Workbench |
| **Linux forense** | Volatility 3 o Rekall |

---

## 5. Scripts de automatización

### Script de análisis completo (Linux)

```bash
#!/bin/bash
# Script de análisis de memoria con Volatility 3
# Uso: ./analyze_memory.sh <volcado.raw> <salida/>

VOLCADO=$1
SALIDA=$2

if [ -z "$VOLCADO" ] || [ -z "$SALIDA" ]; then
    echo "Uso: $0 <volcado.raw> <directorio_salida>"
    exit 1
fi

mkdir -p $SALIDA

echo "=== Análisis de memoria: $(date) ===" | tee $SALIDA/resumen.txt
echo "Volcado: $VOLCADO" | tee -a $SALIDA/resumen.txt

echo "[1/12] Info del sistema..."
vol -f $VOLCADO windows.info > $SALIDA/01_info.txt 2>&1

echo "[2/12] Lista de procesos..."
vol -f $VOLCADO windows.pslist > $SALIDA/02_pslist.txt 2>&1

echo "[3/12] Árbol de procesos..."
vol -f $VOLCADO windows.pstree > $SALIDA/03_pstree.txt 2>&1

echo "[4/12] Comandos ejecutados..."
vol -f $VOLCADO windows.cmdline > $SALIDA/04_cmdline.txt 2>&1

echo "[5/12] Conexiones de red..."
vol -f $VOLCADO windows.netscan > $SALIDA/05_netscan.txt 2>&1

echo "[6/12] Código inyectado..."
vol -f $VOLCADO windows.malfind > $SALIDA/06_malfind.txt 2>&1

echo "[7/12] Hashes de credenciales..."
vol -f $VOLCADO windows.hashdump > $SALIDA/07_hashdump.txt 2>&1

echo "[8/12] DLLs..."
vol -f $VOLCADO windows.dlllist > $SALIDA/08_dlllist.txt 2>&1

echo "[9/12] Archivos..."
vol -f $VOLCADO windows.filescan > $SALIDA/09_filescan.txt 2>&1

echo "[10/12] Servicios..."
vol -f $VOLCADO windows.svcscan > $SALIDA/10_svcscan.txt 2>&1

echo "[11/12] Registro..."
vol -f $VOLCADO windows.registry.hivelist > $SALIDA/11_hivelist.txt 2>&1

echo "[12/12] Variables de entorno..."
vol -f $VOLCADO windows.envars > $SALIDA/12_envars.txt 2>&1

echo "" | tee -a $SALIDA/resumen.txt
echo "=== Análisis completado ===" | tee -a $SALIDA/resumen.txt
echo "Resultados en: $SALIDA/" | tee -a $SALIDA/resumen.txt
echo "Resumen: $SALIDA/resumen.txt" | tee -a $SALIDA/resumen.txt
```

### Script de IOC rápido

```bash
#!/bin/bash
# Búsqueda rápida de IOC en volcado de memoria
# Uso: ./ioc_check.sh <volcado.raw>

VOLCADO=$1

if [ -z "$VOLCADO" ]; then
    echo "Uso: $0 <volcado.raw>"
    exit 1
fi

echo "=== IOC Check: $(date) ==="
echo "Volcado: $VOLCADO"
echo ""

echo "[*] Procesos con nombres sospechosos..."
vol -f $VOLCADO windows.pslist | grep -iE "mimikatz|lazagne|procdump|psexec|nc|netcat|meterpreter|cobalt"

echo ""
echo "[*] Comandos con base64..."
vol -f $VOLCADO windows.cmdline | grep -iE "\-enc|-e |FromBase64|Invoke-Expression|iex "

echo ""
echo "[*] Conexiones a IPs externas..."
vol -f $VOLCADO windows.netscan | grep ESTABLISHED | grep -vE "127.0.0.1|10\.|192\.168\.|172\.(1[6-9]|2[0-9]|3[01])\."

echo ""
echo "[*] Código inyectado (RWX)..."
vol -f $VOLCADO windows.malfind | grep "VadS\|VadI\|PAGE_EXECUTE"

echo ""
echo "[*] Ejecutables en carpetas temporales..."
vol -f $VOLCADO windows.filescan | grep -iE "Temp\\\\|AppData\\\\Local\\\\Temp"

echo ""
echo "=== IOC Check completado ==="
```

---

## 6. Análisis con LiME en Linux

### Crear volcado con LiME

```bash
# Compilar LiME
git clone https://github.com/504ensicsLabs/LiME.git
cd LiME/src

# Compilar para el kernel actual
make

# Crear volcado
sudo insmod lime-*.ko "path=/tmp/memory.lime format=lime"

# Verificar
ls -lh /tmp/memory.lime
```

### Analizar volcado LiME con Volatility

```bash
# Volatility 3 detecta automáticamente LiME
vol -f memory.lime linux.pslist
vol -f memory.lime linux.pstree
vol -f memory.lime linux.bash
vol -f memory.lime linux.check_syscall
```

### Artefactos Linux en memoria

| Plugin | Qué busca | Ejemplo |
|---|---|---|
| `linux.pslist` | Procesos en ejecución | Procesos ocultos con rootkit |
| `linux.bash` | Historial de bash | Comandos ejecutados por atacante |
| `linux.check_syscall` | Syscalls hookadas | Rootkits que hookan syscalls |
| `linux.check_idt` | IDT hookada | Rootkits a nivel de kernel |
| `linux.lsmod` | Módulos del kernel | Módulos maliciosos |
| `linux.proc_maps` | Mapas de memoria | Shellcode en procesos |

---

## 7. Referencias

| Recurso | URL |
|---|---|
| **Volatility 3** | [https://github.com/volatilityfoundation/volatility3](https://github.com/volatilityfoundation/volatility3) |
| **Volatility 2** | [https://github.com/volatilityfoundation/volatility](https://github.com/volatilityfoundation/volatility) |
| **Rekall** | [https://github.com/google/rekall](https://github.com/google/rekall) |
| **LiME** | [https://github.com/504ensicsLabs/LiME](https://github.com/504ensicsLabs/LiME) |
| **Volatility Documentation** | [https://volatility3.readthedocs.io/](https://volatility3.readthedocs.io/) |
| **SANS FOR508** | [https://www.sans.org/cyber-security-courses/advanced-incident-response/](https://www.sans.org/cyber-security-courses/advanced-incident-response/) |

---

**[⬅ Volatilidad y Análisis](./01-volatilidad-ram.md)** · **[Volver al módulo](../README.md)**
