# 🔒 Cadena de Custodia y Adquisición Forense

> *"La evidencia más poderosa del mundo es inútil si no puedes demostrar que no fue alterada."*

---

## 📋 Tabla de contenido

1. [Principios fundamentales](#1-principios-fundamentales)
2. [Cadena de custodia](#2-cadena-de-custodia)
3. [Integridad y hashing](#3-integridad-y-hashing)
4. [Orden de volatilidad](#4-orden-de-volatilidad)
5. [Adquisición de disco](#5-adquisición-de-disco)
6. [Adquisición de memoria RAM](#6-adquisición-de-memoria-ram)
7. [Adquisición en la nube](#7-adquisición-en-la-nube)
8. [Protocolos legales](#8-protocolos-legales)
9. [Errores comunes y cómo evitarlos](#9-errores-comunes-y-cómo-evitarlos)
10. [Defensa: evasión forense](#10-defensa-evasión-forense)
11. [Herramientas](#11-herramientas)
12. [Referencias](#12-referencias)

---

## 1. Principios fundamentales

### El estándar: NIST SP 800-86

El marco de referencia para todo análisis forense sigue cuatro fases:

```
┌─────────────┐    ┌─────────────┐    ┌─────────────┐    ┌─────────────┐
│  Collection  │───▶│ Examination  │───▶│   Analysis   │───▶│  Reporting   │
│ (Adquisición)│    │ (Extracción) │    │ (Respuesta)  │    │ (Documentar) │
└─────────────┘    └─────────────┘    └─────────────┘    └─────────────┘
```

> **Este documento cubre la Fase 1 (Collection): cómo obtener evidencia sin alterarla.**

### Los 3 principios sagrados

| Principio | Significado | Ejemplo |
|---|---|---|
| **No alterar evidencia** | Nunca trabajes sobre el original | Siempre crear copia bit a bit primero |
| **Cadena de custodia** | Documentar quién, qué, cuándo y dónde | Registro escrito de cada movimiento |
| **Reproducibilidad** | Otro forense debe poder repetir tu proceso | Herramientas documentadas, versiones registradas |

### ¿Qué es evidencia digital?

Todo dato almacenado en formato electrónico que puede ser usado como prueba:

- **Voluminosa:** discos duros, SSDs, memorias USB, tarjetas SD
- **Volátil:** RAM, registros de red, procesos en ejecución
- **Dados:** logs de servidores, correos, bases de datos
- **Genérica:** metadatos, timestamps, registros de auditoría

---

## 2. Cadena de custodia

### ¿Qué es?

Un registro continuo que documenta cada interacción con la evidencia desde su recolección hasta su presentación en tribunal.

### Plantilla de cadena de custodia

```text
╔══════════════════════════════════════════════════════════════════════╗
║                    CADENA DE CUSTODIA                                ║
╠══════════════════════════════════════════════════════════════════════╣
║ Caso:           INC-2026-0847                                       ║
║ Evidencia ID:   EVD-001 (Disco duro WD Blue 1TB)                    ║
║ Fecha:          2026-08-20                                          ║
╠══════════════════════════════════════════════════════════════════════╣
║ # │ Fecha/Hora    │ Quién        │ Acción         │ Hash SHA-256   ║
╠══════════════════════════════════════════════════════════════════════╣
║ 1 │ 2026-08-20    │ J. García     │ Adquisición    │ 4b3a9f...e2c1  ║
║   │ 10:00:00      │ #CI-4521      │ (imagen dd)    │                ║
╠══════════════════════════════════════════════════════════════════════╣
║ 2 │ 2026-08-20    │ J. García     │ Traslado a     │ 4b3a9f...e2c1  ║
║   │ 11:30:00      │               │ Lab Forense    │                ║
╠══════════════════════════════════════════════════════════════════════╣
║ 3 │ 2026-08-20    │ M. López      │ Análisis       │ 4b3a9f...e2c1  ║
║   │ 14:00:00      │ #CI-3892      │ (copia trabajo)│                ║
╚══════════════════════════════════════════════════════════════════════╝
```

### Campos obligatorios

| Campo | Descripción | Ejemplo |
|---|---|---|
| **ID del caso** | Identificador único del investigación | INC-2026-0847 |
| **ID de evidencia** | Identificador único del artículo | EVD-001 |
| **Fecha/hora** | Timestamp preciso (con zona horaria) | 2026-08-20 10:00:00 UTC-3 |
| **Responsable** | Nombre y cargo de quien manipula | J. García, Forense Senior |
| **Acción** | Qué se hizo con la evidencia | Adquisición, análisis, traslado |
| **Hash** | Hash SHA-256 que verifica integridad | 4b3a9f...e2c1 |
| **Ubicación** | Dónde se encuentra la evidencia | Lab Forense, Caja #5 |

### Reglas de la cadena de custodia

1. **Registrar TODO:** cada acceso, cada movimiento, cada copia
2. **Hash al inicio y al final:** debe ser idéntico
3. ** sellado físico:** usar bolsas de evidencia numeradas
4. **Acceso restringido:** solo personal autorizado
5. **Almacenamiento seguro:** temperatura controlada, candado, acceso loggeado

---

## 3. Integridad y hashing

### ¿Por qué es crítico?

Si el hash de la evidencia cambia en algún momento, **toda la cadena de custodia se invalida** y la evidencia pierde valor legal.

### Algoritmos de hash recomendados

| Algoritmo | Velocidad | Seguridad | Uso forense |
|---|---|---|---|
| **SHA-256** | Media | ⭐⭐⭐⭐⭐ | ✅ Estándar actual |
| **SHA-512** | Media | ⭐⭐⭐⭐⭐ | ✅ Para evidencia crítica |
| **MD5** | Rápida | ⭐⭐ | ⚠️ Solo para referencia (colisiones conocidas) |
| **SHA-1** | Media | ⭐⭐⭐ | ⚠️ Evitar en nuevos casos |

> **Regla:** siempre calcula **al menos dos hashes** (SHA-256 + otro) por redundancia.

### Calcular hashes

```bash
# SHA-256 (recomendado)
sha256sum evidencia.dd
# Output: 4b3a9f2c8e1d...  evidencia.dd

# Múltiples hashes de una vez
sha256sum evidencia.dd > hashes.txt
md5sum evidencia.dd >> hashes.txt
sha1sum evidencia.dd >> hashes.txt

# Verificar integridad posteriormente
sha256sum -c hashes.txt
# evidencia.dd: OK
```

### Verificación en diferentes herramientas

```bash
# Con dc3dd (hash integrado durante adquisición)
dc3dd if=/dev/sdb of=/evidencia/img.dd hash=sha256 log=hash.log

# Con FTK Imager (GUI)
# Tools > Verify Drive > Seleccionar imagen > Verify

# Con Autopsy (GUI)
# Al agregar caso: ingresa hash conocido para verificación automática
```

### Firma digital de evidencia

Para evidencia crítica, usar firma digital (GPG):

```bash
# Firmar la imagen
gpg --detach-sign evidencia.dd

# Verificar firma
gpg --verify evidencia.dd.sig evidencia.dd
```

---

## 4. Orden de volatilidad

### RFC 3227: Guidelines for Evidence Collection

La evidencia más volátil se captura **primero** porque desaparece primero:

```
MÁS VOLÁTIL                                    MENOS VOLÁTIL
    │                                               │
    ▼                                               ▼
┌─────────┐  ┌─────────┐  ┌─────────┐  ┌─────────┐  ┌─────────┐
│  CPU /  │  │  RAM /  │  │  Red /  │  │  Disco  │  │  Logs   │
│ Caché   │  │ Estado  │  │ARP/DNS  │  │  duro   │  │remotos  │
└─────────┘  └─────────┘  └─────────┘  └─────────┘  └─────────┘
  Orden 1      Orden 2      Orden 3      Orden 4      Orden 5
```

### Tabla de volatilidad

| Orden | Tipo | Qué capturar | Herramienta | Tiempo disponible |
|---|---|---|---|---|
| 1 | **CPU** | Registros, caché L1/L2/L3 | (poco práctico en IR) | Nanosegundos |
| 2 | **RAM** | Volcado completo de memoria | avml, winpmem, DumpIt | Segundos (se pierde al apagar) |
| 3 | **Red** | Conexiones activas, ARP, DNS cache | netstat, Volatility netscan | Minutos |
| 4 | **Procesos** | Árbol de procesos, archivos abiertos | Volatility pslist, /proc | Minutos |
| 5 | **Disco** | Imagen bit a bit completa | dc3dd, dd, FTK Imager | Horas |
| 6 | **Logs** | Syslog, SIEM, backups | rsync, WMI | Días/meses |

### Decisión: ¿Apagar o no apagar?

| Escenario | Recomendación | Razón |
|---|---|---|
| **Servidor encendido** | **NO apagar** — capturar RAM primero | Se pierde evidencia volátil |
| **Laptop con bitlocker** | **NO apagar** — bypass de encryption requiere RAM | Claves en memoria |
| **Estación de trabajo** | Capturar RAM → luego apagar → adquirir disco | Equilibrio |
| **Dispositivo apagado** | **NO encender** — adquirir disco directamente | Encender altera evidencia |

---

## 5. Adquisición de disco

### Métodos de adquisición

#### 5.1 Adquisición física (dispositivo completo)

```bash
# CREAR IMAGEN CON dc3dd (RECOMENDADO)
# Incluye hashing integrado y puede verificar bad sectors
dc3dd if=/dev/sda of=/evidencia/caso001.dd \
    hash=sha256 log=/evidencia/caso001_hash.log \
    hlog=/evidencia/caso001_hashdetail.log

# Parámetros importantes:
# if=         → input file (dispositivo fuente)
# of=         → output file (imagen de salida)
# hash=       → algoritmo de hash (sha256, md5)
# log=        → archivo de log con hash resultante
# hlog=       → log detallado del proceso de hashing

# Verificar bad sectors
dc3dd if=/dev/sda of=/evidencia/caso001.dd \
    hash=sha256 log=hash.log \
    -bn2  # Reporta bad blocks pero continúa
```

```bash
# ALTERNATIVA: dd (más universal pero sin hashing integrado)
dd if=/dev/sda of=/evidencia/caso001.dd bs=4M conv=sync,noerror status=progress

# Calcular hash por separado
sha256sum /dev/sda > /evidencia/original_hash.txt
sha256sum /evidencia/caso001.dd >> /evidencia/original_hash.txt
# Los dos hashes deben coincidir
```

#### 5.2 Adquisición lógica (particiones)

```bash
# Adquirir solo la partición Windows (NTFS)
dc3dd if=/dev/sda2 of=/evidencia/partition_ntfs.dd hash=sha256 log=hash.log

# Adquirir partición EFI
dc3dd if=/dev/sda1 of=/evidencia/partition_efi.dd hash=sha256 log=hash.log
```

#### 5.3 Formatos de imagen

| Formato | Extensión | Compresión | Hash integrado | Uso |
|---|---|---|---|---|
| **RAW (dd)** | `.dd`, `.raw` | No | No | Estándar, compatible |
| **E01 (Expert Witness)** | `.E01` | Sí | Sí (MD5+SHA1) | Autopsy, FTK |
| **AFF4** | `.aff4` | Sí | Sí | Formato abierto, forense |
| **VHD** | `.vhd` | No | No | Virtualización |

### Windows: FTK Imager (GUI)

```
1. Abrir FTK Imager
2. File > Create Disk Image
3. Seleccionar: Physical Drive → disco destino
4. Tipo: Raw (dd)
5. Destino: ruta de almacenamiento
6. Iniciar adquisición
7. Verificar hash al finalizar
```

### Verificación post-adquisición

```bash
# SIEMPRE verificar que la imagen coincide con el original
# Método 1: comparar hashes
sha256sum /dev/sda
sha256sum /evidencia/caso001.dd
# Deben coincidir

# Método 2: con dc3dd (ya calculó el hash durante adquisición)
cat /evidencia/caso001_hash.log

# Método 3: con FTK Imager (GUI)
# Tools > Verify Image > Seleccionar .E01
```

---

## 6. Adquisición de memoria RAM

### ¿Por qué la memoria es crítica?

La RAM contiene datos que **no están en el disco**:

- Claves de cifrado (BitLocker, LUKS, VeraCrypt)
- Contraseñas en texto plano
- Conexiones de red activas
- Procesos maliciosos en ejecución
- Comandos ejecutados (bash history en memoria)
- DLLs inyectadas
- Artefactos de navegadores

### Herramientas de adquisición de RAM

#### Linux: avml (recomendado)

```bash
# Instalar avml
# Opción 1: desde releases de GitHub
wget https://github.com/microsoft/avml/releases/latest/download/avml
chmod +x avml

# Opción 2: compilar desde source
git clone https://github.com/microsoft/avml.git
cd avml && cargo build --release

# Capturar RAM
sudo ./avml memory.lime

# Verificar tamaño (debe ser ≈ cantidad de RAM instalada)
ls -lh memory.lime
# -rw-r--r-- 1 user user 16G memory.lime  (para 16GB de RAM)
```

#### Windows: winpmem

```bash
# Descargar winpmem (Physical Memory Acquisition)
# https://github.com/Velocidex/winpmem/releases

# Ejecutar como Administrador
winpmem_4.0.exe memory.raw

# Verificar
dir memory.raw
# Tamaño debe ser ≈ RAM instalada
```

#### Windows: DumpIt

```
1. Descargar DumpIt desde Comae Technologies
2. Ejecutar como Administrador
3. DumpIt crea automáticamente memory.raw en la misma carpeta
4. Verificar tamaño del archivo
```

### Precauciones antes de capturar RAM

| Precaución | Razón |
|---|---|
| **Ejecutar desde USB** | No montar disco local que modifique RAM |
| **No instalar software** | La instalación altera la memoria |
| **Ejecutar lo más rápido posible** | La RAM se modifica constantemente |
| **Documentar el proceso** | Cadena de custodia incluye hora exacta |

### Qué se puede extraer de la RAM

| Artefacto | Plugin Volatility | Ejemplo |
|---|---|---|
| Procesos | `pslist`, `pstree` | `cmd.exe` con base64 en arguments |
| Conexiones | `netscan` | Conexión a IP de C2 |
| DLLs cargadas | `dlllist` | Mimikatz en memoria de lsass |
| Credenciales | `hashdump`, `lsadump` | NTLM hashes |
| Código inyectado | `malfind` | Shellcode en explorer.exe |
| Archivos abiertos | `filescan` | Documentos abiertos por el atacante |
| Comandos ejecutados | `cmdline` | PowerShell con -enc (base64) |

---

## 7. Adquisición en la nube

### AWS

```bash
# Crear snapshot de un EBS volume
aws ec2 create-snapshot \
    --volume-id vol-0123456789abcdef0 \
    --description "Forensic snapshot - Case INC-2026-0847"

# Listar snapshots
aws ec2 describe-snapshots \
    --filters "Name=status,Values=completed"

# Descargar snapshot como imagen
# (requiere convertir a EBS → EC2 instance → export)
```

### Azure

```bash
# Crear snapshot de un Managed Disk
az snapshot create \
    --resource-group forensic-rg \
    --name forensic-snapshot-001 \
    --source /subscriptions/.../disks/target-disk \
    --sku Standard_LRS
```

### Google Cloud

```bash
# Crear snapshot de un Persistent Disk
gcloud compute disks snapshot target-disk \
    --snapshot-names=forensic-snapshot-001 \
    --zone=us-central1-a
```

---

## 8. Protocolos legales

### ¿Qué necesitas antes de iniciar?

| Requisito | Descripción |
|---|---|
| **Autorización escrita** | Orden judicial, contrato de investigación, permiso del titular |
| **Alcance definido** | Qué se va a analizar y qué no |
| **Personal autorizado** | Lista de personas con acceso a la evidencia |
| **Almacenamiento seguro** | Lugar controlado para evidencia física |
| **Plan de respaldo** | Qué hacer si la evidencia se daña |

### Cadena de custodia legal

```
1. RECOLECCIÓN
   └─ Registrar: fecha, hora, ubicación, quién, qué
   └─ Fotografiar el estado original
   └─ Calcular hash inicial

2. ALMACENAMIENTO
   └─ Sellado con bolsa de evidencia numerada
   └─ Registro de ingreso a almacén
   └─ Control de temperatura/humedad

3. ANÁLISIS
   └─ Trabajar SOLO sobre copia
   └─ Documentar cada paso
   └─ Calcular hash de copia de trabajo

4. PRESENTACIÓN
   └─ Hash final = hash inicial (integridad probada)
   └─ Cadena de custodia completa
   └─ Metodología documentada y reproducible
```

### Errores legales comunes

| Error | Consecuencia | Cómo evitar |
|---|---|---|
| No documentar acceso | Evidencia declarada inadmisible | Cadena de custodia estricta |
| Trabajar sobre original | Alteración de evidencia | Siempre usar copias |
| No verificar hash | No se puede probar integridad | Hash antes y después de cada fase |
| Cadena rota | La defensa impugna la evidencia | Registrar cada movimiento |

---

## 9. Errores comunes y cómo evitarlos

### ❌ Error 1: Apagar el sistema antes de capturar RAM

```bash
# MAL: apagar inmediatamente
shutdown -h now

# BIEN: capturar RAM primero
sudo ./avml memory.lime
# Luego apagar
shutdown -h now
```

### ❌ Error 2: No verificar el hash

```bash
# MAL: asumir que la imagen es correcta
dd if=/dev/sda of=img.dd

# BIEN: verificar siempre
sha256sum /dev/sda > original.txt
dd if=/dev/sda of=img.dd
sha256sum img.dd >> original.txt
# Comparar hashes
```

### ❌ Error 3: Montar el disco sin write-blocker

```bash
# MAL: montar directamente (modifica metadatos)
mount /dev/sda2 /mnt/evidence

# BIEN: usar write-blocker o montar como solo lectura
mount -o ro,loop /dev/sda2 /mnt/evidence
# O mejor: NO montar, trabajar con The Sleuth Kit directamente
fls -r -o 2048 img.dd
```

### ❌ Error 4: No documentar el proceso

```bash
# MAL: solo ejecutar comandos sin registro
dc3dd if=/dev/sda of=img.dd hash=sha256

# BIEN: documentar todo
echo "=== Forense: J. García ===" > log.txt
echo "Fecha: $(date -u '+%Y-%m-%d %H:%M:%S UTC')" >> log.txt
echo "Dispositivo: /dev/sda (WD Blue 1TB, S/N: WD-XXX)" >> log.txt
echo "Comando: dc3dd if=/dev/sda of=/evidencia/img.dd hash=sha256" >> log.txt
dc3dd if=/dev/sda of=/evidencia/img.dd hash=sha256 log=hash.log 2>&1 | tee -a log.txt
echo "Hash resultado: $(cat hash.log | grep sha256)" >> log.txt
```

---

## 10. Defensa: evasión forense

### Técnicas que los atacantes usan para evadir análisis

| Técnica | Cómo funciona | Detección |
|---|---|---|
| **Anti-forensics: borrado seguro** | Sobrescribir datos múltiples veces | Metadatos de archivos, logs de borrado |
| **Timestomping** | Modificar timestamps de archivos | Comparar $MFT con UsnJrnl, logs del sistema |
| **Encryption** | Cifrar evidencia antes de apagar | Forzar apagado para capturar RAM con claves |
| **Log manipulation** | Borrar o modificar logs | Logs de auditoría, logs en SIEM remoto |
| **Live forensics evasion** | Ejecutar solo en memoria | Volatility, monitoreo de procesos |
| **Steganography** | Ocultar datos en archivos multimedia | Análisis de entropía, herramientas estego |

### Defensas contra evasión

| Defensa | Implementación |
|---|---|
| **Logs centralizados** | SIEM que recibe logs antes de que el atacante pueda borrarlos |
| **Monitoreo de integridad** | Tripwire, AIDE para detectar cambios en archivos del sistema |
| **Copia de seguridad de RAM** | Snapshot de memoria en intervalos regulares |
| **Write-blockers físicos** | Dispositivos hardware que impiden escritura a discos |
| **Timestamping con blockchain** | Timestamps verificables en cadena de bloques |

---

## 11. Herramientas

### Comparativa de herramientas de adquisición

| Herramienta | Plataforma | Formato | Hash | Uso principal |
|---|---|---|---|---|
| **dc3dd** | Linux | dd/raw | ✅ SHA-256, MD5 | Adquisición de disco |
| **dd** | Linux/macOS | dd/raw | ❌ (manual) | Adquisición universal |
| **FTK Imager** | Windows | E01, dd | ✅ MD5, SHA1 | Adquisición GUI |
| **avml** | Linux | lime | ❌ (manual) | Adquisición de RAM |
| **winpmem** | Windows | raw | ❌ (manual) | Adquisición de RAM |
| **DumpIt** | Windows | raw | ❌ (manual) | Adquisición de RAM |
| **Guymager** | Linux | E01, AFF | ✅ | Adquisición GUI Linux |

### Flujo de trabajo completo

```
1. PREPARACIÓN
   └─ Autorización legal ✅
   └─ Herramientas listas (USB booteable) ✅
   └─ Cadena de custodia en blanco ✅

2. DOCUMENTACIÓN INICIAL
   └─ Fotografiar sistema ✅
   └─ Registrar hora, lugar, responsable ✅
   └─ Documentar estado del sistema ✅

3. ADQUISICIÓN VOLÁTIL
   └─ Capturar RAM (avml/winpmem) ✅
   └─ Capturar red (netstat) ✅
   └─ Capturar procesos ✅

4. ADQUISICIÓN ESTÁTICA
   └─ Write-blocker conectado ✅
   └─ Imagen de disco (dc3dd) ✅
   └─ Hash verificado ✅

5. VERIFICACIÓN
   └─ Hash de imagen = hash de original ✅
   └─ Cadena de custodia actualizada ✅
   └─ Evidencia sellada y almacenada ✅
```

---

## 12. Referencias

### Estándares y marcos

| Recurso | URL |
|---|---|
| **NIST SP 800-86** — Guide to Integrating Forensic Techniques | [https://csrc.nist.gov/pubs/sp/800/86/final](https://csrc.nist.gov/pubs/sp/800/86/final) |
| **RFC 3227** — Evidence Collection and Archiving | [https://www.rfc-editor.org/rfc/rfc3227](https://www.rfc-editor.org/rfc/rfc3227) |
| **NIST SP 800-101** — Guidelines on Mobile Device Forensics | [https://csrc.nist.gov/pubs/sp/800/101/r1/final](https://csrc.nist.gov/pubs/sp/800/101/r1/final) |

### Herramientas

| Herramienta | URL |
|---|---|
| **dc3dd** — dd con hashing | [https://sourceforge.net/projects/dc3dd/](https://sourceforge.net/projects/dc3dd/) |
| **avml** — Memory acquisition (Linux) | [https://github.com/microsoft/avml](https://github.com/microsoft/avml) |
| **winpmem** — Memory acquisition (Windows) | [https://github.com/Velocidex/winpmem](https://github.com/Velocidex/winpmem) |
| **FTK Imager** — Disk imaging | [https://www.exterro.com/ftk-imager](https://www.exterro.com/ftk-imager) |
| **The Sleuth Kit** — Forensic analysis | [https://www.sleuthkit.org/](https://www.sleuthkit.org/) |

### Formación

| Recurso | URL |
|---|---|
| **SANS FOR508** — Advanced Incident Response | [https://www.sans.org/cyber-security-courses/advanced-incident-response/](https://www.sans.org/cyber-security-courses/advanced-incident-response/) |
| **CyberDefenders** — CTF forenses | [https://cyberdefenders.org/](https://cyberdefenders.org/) |
| **Blue Team Labs Online** | [https://blueteamlabs.online/](https://blueteamlabs.online/) |

---

## 📝 Entregable de portafolio

```markdown
# Adquisición Forense — Caso INC-2026-0847

## Contexto
- Fecha: 2026-08-20
- Dispositivo: Estación de trabajo Dell OptiPlex 7090
- Disco: WD Blue 1TB (S/N: WD-XXX)
- RAM: 16GB DDR4
- Responsable: J. García (#CI-4521)

## Proceso
1. Sistema encendido, capturar RAM primero
   - Herramienta: avml
   - Resultado: memory.lime (16GB)
   - Hash SHA-256: 4b3a9f2c...e2c1

2. Apagar sistema, conectar write-blocker

3. Adquirir imagen de disco
   - Herramienta: dc3dd
   - Resultado: imagen.dd (1TB)
   - Hash SHA-256: 8f7e6d5c...a1b2

4. Verificación
   - Hash de imagen = hash calculado durante adquisición ✅
   - Cadena de custodia documentada ✅

## Evidencia generada
- /evidencia/caso001/memory.lime
- /evidencia/caso001/imagen.dd
- /evidencia/caso001/hash.log
- /evidencia/caso001/cadena_custodia.pdf
```

---

**[⬅ Volver al módulo](../README.md)** · **[→ Análisis de Disco](../analisis-disco/01-sistemas-archivos-img.md)**
