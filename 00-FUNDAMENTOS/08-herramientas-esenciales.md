# 08 — Herramientas esenciales para empezar

> 🎯 **Objetivo:** conocer las 10-15 herramientas que verás 1000 veces. Todas son gratuitas o tienen versión community. Practica en labs, **nunca en sistemas sin autorización**.

## 1. Antes de instalar nada

- Practica SIEMPRE en máquinas propias o en plataformas tipo **[HackTheBox](https://www.hackthebox.com/)** o **[TryHackMe](https://tryhackme.com/)**.
- Si vas a usar Kali, recuerda que viene preinstalado: solo arranca y aprende.
- Casi todas estas herramientas existen en Docker. Si no quieres instalar nada en tu máquina: `docker run -it kalilinux/kali-rolling /bin/bash`.
- **No mezcles herramientas de ataque con tu vida personal.** Usa una máquina o VM dedicada.

## 2. Reconocimiento / OSINT

### 🔍 Nmap — el rey del escaneo de puertos

```bash
# Scan básico
nmap 192.168.1.1

# Rápido y sigiloso (SYN)
nmap -sS -T4 192.168.1.0/24

# Detección de versiones y OS
nmap -sV -O 192.168.1.1

# Scripts NSE (vulnerabilidades, brute fuerza, etc.)
nmap --script=vuln 192.168.1.1
```

**Para qué:** descubrir qué servicios están expuestos en una IP/rango.

### 🌐 Recon-ng / SpiderFoot / theHarvester — OSINT automatizado

```bash
# theHarvester: emails, subdominios, hosts
theHarvester -d ejemplo.com -b all
```

### 🛰️ Amass — subdominios

```bash
amass enum -d ejemplo.com
```

### 🔎 Shodan / Censys — internet-wide scan data

- [shodan.io](https://shodan.io) — buscar dispositivos conectados en internet.
- Útil para entender tu propia exposición.

## 3. Análisis de tráfico

### 🦈 Wireshark — el analizador por excelencia

- **GUI**: instalas y capturas paquetes.
- **CLI** (`tshark`) para servers:

```bash
sudo tshark -i eth0 -c 100     # captura 100 paquetes
sudo tshark -i eth0 -Y 'http'  # solo HTTP
sudo tshark -i eth0 -Y 'ip.addr == 1.2.3.4'  # filtra IP
```

**Truco:** filtros útiles — `http.request`, `dns.qry.name`, `tcp.flags.syn == 1 && tcp.flags.ack == 0`.

### 🐚 tcpdump — el clásico de CLI

```bash
sudo tcpdump -i eth0 -w captura.pcap   # guarda a archivo
sudo tcpdump -i eth0 'port 80'         # filtra puerto
```

## 4. Web — pentest y defensa

### 🦊 Burp Suite — el inspector web

- **Free** la versión Community (suficiente para empezar).
- **Pro** la versión de pago (mejor flujo de trabajo).
- Funciones: proxy para interceptar, scanner, repeater, intruder.

```
1. Configura tu navegador para usar Burp como proxy (127.0.0.1:8080)
2. Instala el certificado CA de Burp para HTTPS
3. Navega como siempre — Burp captura y permite modificar
4. Replay con Repeater
```

### 🕷️ OWASP ZAP — alternativa gratuita a Burp

- Similar a Burp pero open source.
- Más lento pero sin coste.
- Buen scanner automático para empezar.

### 🌐 Gobuster / dirsearch — fuerza bruta de directorios web

```bash
gobuster dir -u https://ejemplo.com -w /usr/share/wordlists/dirb/common.txt
```

### 🚪 Nikto — escáner web de vulnerabilidades comunes

```bash
nikto -h https://ejemplo.com
```

## 5. Explotación

### 💣 Metasploit Framework — la suite por excelencia

```bash
# Inicia
msfconsole

# Busca un exploit
search type:exploit name:smb

# Usa un módulo
use exploit/windows/smb/ms17_010_eternalblue

# Configura y lanza
set RHOSTS 192.168.1.10
exploit
```

**Solo en labs autorizados.**

### 🧪 searchsploit — busca exploits localmente

```bash
searchsploit nginx 1.14
```

### 📦 John the Ripper / hashcat — romper hashes

```bash
john --wordlist=/usr/share/wordlists/rockyou.txt hash.txt
hashcat -m 0 hash.txt rockyou.txt    # MD5
```

## 6. Frameworks de pentest

### 🐍 Python — el lenguaje universal

- Aprende Python si vas en serio. Casi todas las herramientas tienen API o puedes escribir la tuya.
- Librerías útiles: `requests`, `scapy`, `paramiko`, `pwntools`.

### 🦊 Go / Rust — cada vez más herramientas están escritas en estos

## 7. Blue team / defensa

### 🛡️ Wazuh / OSSEC — HIDS (Host IDS)

- Open source.
- Detecta cambios en archivos, logins raros, etc.

### 📊 Splunk (free) / Elastic Stack — SIEM casero

- Splunk tiene 500 MB/día gratis.
- Elastic Stack (ELK) es open source completo.

### 🔍 Velociraptor — DFIR endpoint

- Para respuesta a incidentes en endpoints.

### 🥃 MISP — threat intelligence platform

- Compartir IoCs entre equipos.

## 8. Ofensivas adicionales

### 🌐 gowitness / aquatone — screenshots de páginas web

```bash
gowitness single https://ejemplo.com
```

### 📡 masscan — internet-scale port scanner

```bash
masscan -p1-65535 --rate 1000 192.168.1.0/24
```

### 🪪 Responder / impacket — Active Directory attacks

- Solo en entornos autorizados. Familiarízate primero con un lab AD.

## 9. Documentación y reporte

### 📝 CherryTree / Obsidian / Joplin

- Para tus notas de pentest. **Nunca** en archivos compartidos sin cifrar.

### 📋 templates de reporte

- Mira los que hay en [`02-pentesting-red-team/portafolio/`](../02-pentesting-red-team/portafolio/).

## 10. Tabla resumen — la mochila mínima

| Categoría | Herramienta principal | Alternativa |
|---|---|---|
| Escaneo de red | nmap | masscan, rustscan |
| Tráfico de red | Wireshark | tcpdump, tshark |
| Proxy web | Burp Suite CE | OWASP ZAP |
| OSINT | theHarvester | recon-ng, spiderfoot |
| Subdominios | amass | subfinder |
| Directorios web | gobuster | dirsearch, feroxbuster |
| Vulnerabilidades web | Nikto | Nuclei |
| Explotación | Metasploit | Busca exploits manualmente |
| Hashes | hashcat | john |
| SIEM casero | ELK | Wazuh |
| Notas | Obsidian | CherryTree |
| Lenguaje | Python | Bash |

## 11. Cómo aprenderlas

1. Lee el `--help` o la doc oficial.
2. Lánzala en tu propio equipo o en un lab tipo TryHackMe.
3. Lee los writeups de otros sobre la misma herramienta.
4. Repite hasta que la uses sin pensar.

## 📌 Dónde practicar con estas herramientas

| Recurso | Dónde |
|---|---|
| HackTheBox / TryHackMe | [`04-LABORATORIOS/htb-thm/`](../04-LABORATORIOS/htb-thm/) |
| Docker labs propios | [`04-LABORATORIOS/docker-labs/`](../04-LABORATORIOS/docker-labs/) |
| Writeups | [`04-LABORATORIOS/ctf-writeups/`](../04-LABORATORIOS/ctf-writeups/) |
| Cheatsheets | [`05-RECURSOS/cheatsheets/`](../05-RECURSOS/cheatsheets/) |

## ✏️ Ejercicios

1. **nmap basico:** escanea `scanme.nmap.org` (es legal, lo permiten para practicar). Mira los puertos abiertos y los servicios.
2. **Wireshark en tu propia red:** captura 30 segundos de tráfico. Filtra solo los DNS y mira qué dominios resuelve tu equipo.
3. **OWASP ZAP:** correlo contra un DVWA local o WebGoat. Mira las alertas que encuentra.
4. **Python + requests:** escribe un script que haga una petición GET a una API pública, parse el JSON, y cuente algo.

> ⏭️ **Siguiente:** [`09-como-seguir-este-repo.md`](./09-como-seguir-este-repo.md) — cómo moverte por el repo desde aquí según tu interés.
