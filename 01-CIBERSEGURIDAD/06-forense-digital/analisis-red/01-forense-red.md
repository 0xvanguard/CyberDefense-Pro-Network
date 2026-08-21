# 🌐 Forense de Red

> *"La red es el sistema nervioso del atacante. Cada conexión, cada paquete, cada log deja rastros que cuentan la historia del compromiso."*

---

## 📋 Tabla de contenido

1. [¿Qué es la forense de red?](#1-qué-es-la-forense-de-red)
2. [Captura de tráfico](#2-captura-de-tráfico)
3. [Análisis de paquetes con Wireshark](#3-análisis-de-paquetes-con-wireshark)
4. [Análisis de logs de firewall](#4-análisis-de-logs-de-firewall)
5. [Forense DNS](#5-forense-dns)
6. [Detección de C2 (Command & Control)](#6-detección-de-c2-command--control)
7. [Análisis de logs de proxy](#7-análisis-de-logs-de-proxy)
8. [Flujos de trabajo](#8-flujos-de-trabajo)
9. [Defensa y detección](#9-defensa-y-detección)
10. [Referencias](#10-referencias)

---

## 1. ¿Qué es la forense de red?

### Definición

La **forense de red** es el análisis de tráfico de red y logs de dispositivos de red para reconstruir actividades de un atacante, identificar compromisos y recopilar evidencia.

### Fuentes de evidencia de red

| Fuente | Qué revela | Retención típica |
|---|---|---|
| **PCAP (capturas)** | Paquetes completos | Días-semanas |
| **Logs de firewall** | Conexiones permitidas/bloqueadas | Meses |
| **Logs de DNS** | Dominios consultados | Semanas-meses |
| **Logs de proxy** | Navegación web | Meses |
| **Logs de VPN** | Conexiones remotas | Meses |
| **Logs de IDS/IPS** | Intentos de ataque | Meses |
| **NetFlow** | Metadatos de tráfico | Semanas-meses |
| **Logs de servidor** | Accesos a servicios | Meses |
| **Logs de email** | Correos enviados/recibidos | Meses |

### Flujo de evidencia de red

```
┌─────────────┐    ┌─────────────┐    ┌─────────────┐    ┌─────────────┐
│  Captura    │───▶│  Análisis   │───▶│  Correlación│───▶│  Reporte    │
│  (PCAP/Log) │    │  (Wireshark)│    │  (SIEM)     │    │  (Hallazgos)│
└─────────────┘    └─────────────┘    └─────────────┘    └─────────────┘
```

---

## 2. Captura de tráfico

### tcpdump

```bash
# Capturar todo el tráfico
sudo tcpdump -i eth0 -w captura.pcap

# Capturar tráfico de un host específico
sudo tcpdump -i eth0 host 10.10.10.100 -w host.pcap

# Capturar tráfico de un puerto
sudo tcpdump -i eth0 port 443 -w https.pcap

# Capturar tráfico DNS
sudo tcpdump -i eth0 port 53 -w dns.pcap

# Capturar tráfico HTTP
sudo tcpdump -i eth0 port 80 -w http.pcap

# Capturar con filtro de expresión
sudo tcpdump -i eth0 'host 10.10.10.100 and (port 80 or port 443)' -w filtro.pcap

# Limitar tamaño de archivo
sudo tcpdump -i eth0 -w captura.pcap -C 100 -W 10
# -C 100: archivos de 100MB
# -W 10: máximo 10 archivos (rotación)
```

### tshark (Wireshark CLI)

```bash
# Capturar tráfico
tshark -i eth0 -w captura.pcap

# Capturar con filtro
tshark -i eth0 -f "host 10.10.10.100" -w host.pcap

# Capturar con límite de paquetes
tshark -i eth0 -c 10000 -w captura.pcap

# Capturar solo DNS
tshark -i eth0 -f "port 53" -w dns.pcap

# Capturar solo HTTP
tshark -i eth0 -f "port 80" -w http.pcap
```

### Captura en Windows

```powershell
# Netsh (Windows built-in)
netsh trace start capture=yes tracefile=C:\evidencia\trace.etl
# ... ejecutar actividad sospechosa ...
netsh trace stop

# Convertir a pcap
# Usar tshark para convertir ETL a pcap
```

---

## 3. Análisis de paquetes con Wireshark

### Filtros esenciales

```bash
# Filtrar por IP
ip.addr == 10.10.10.100
ip.src == 10.10.10.100
ip.dst == 185.234.72.15

# Filtrar por puerto
tcp.port == 80
tcp.port == 443
udp.port == 53

# Filtrar por protocolo
http
dns
tls
tcp.flags.syn == 1

# Combinar filtros
ip.addr == 10.10.10.100 and tcp.port == 443
http and ip.addr == 185.234.72.15
dns and ip.addr == 10.10.10.100
```

### Análisis de tráfico sospechoso

```bash
# 1. Buscar conexiones TCP inusuales
# Wireshark filter: tcp.flags.syn == 1 and tcp.flags.ack == 0
# (solo SYN = inicio de conexión)

# 2. Buscar DNS queries sospechosas
dns.qry.name contains "pastebin"
dns.qry.name contains "ngrok"
dns.qry.name contains "serveo"

# 3. Buscar HTTP requests con User-Agent sospechoso
http.user_agent contains "python-requests"
http.user_agent contains "curl"
http.user_agent contains "Wget"

# 4. Buscar tráfico cifrado inusual
tls.handshake.type == 1 and tls.handshake.extensions_server_name != ""

# 5. Buscar exfiltración por DNS
dns.qry.name.len > 50  # DNS queries muy largas (posible exfiltración)
```

### Extracción de archivos

```bash
# Wireshark: File > Export Objects > HTTP
# Seleccionar archivos a exportar

# tshark CLI: exportar objetos HTTP
tshark -r captura.pcap --export-objects http,evidencia_http/
tshark -r captura.pcap --export-objects smb,evidencia_smb/
tshark -r captura.pcap --export-objects dicom,evidencia_dicom/

# Exportar streams TCP
tshark -r captura.pcap -q -z "follow,tcp,ascii,stream" > streams.txt
```

### Análisis con tshark

```bash
# Resumen de tráfico
tshark -r captura.pcap -q -z io,phs

# Top conversaciones
tshark -r captura.pcap -q -z conv,ip

# Top protocols
tshark -r captura.pcap -q -z io,phs

# DNS queries
tshark -r captura.pcap -Y "dns" -T fields -e dns.qry.name | sort | uniq -c | sort -rn

# HTTP requests
tshark -r captura.pcap -Y "http.request" -T fields -e http.host -e http.request.uri | head -20

# IPs más activas
tshark -r captura.pcap -T fields -e ip.src | sort | uniq -c | sort -rn | head -10
```

---

## 4. Análisis de logs de firewall

### iptables (Linux)

```bash
# Ver logs de iptables
journalctl -k | grep -i "iptables\|DROP\|REJECT"

# Configurar logging de iptables
iptables -A INPUT -j LOG --log-prefix "IPT-DROP: "
iptables -A FORWARD -j LOG --log-prefix "IPT-FORWARD: "

# Analizar logs
cat /var/log/messages | grep "IPT-DROP" | awk '{print $NF}' | sort | uniq -c | sort -rn
```

### Windows Firewall

```powershell
# Ver logs del firewall
Get-WinEvent -FilterHashtable @{LogName='Microsoft-Windows-Windows Firewall With Advanced Security/Firewall'} | Select-Object TimeCreated, Message | Select-Object -First 20

# Filtrar por eventos de bloqueo
Get-WinEvent -FilterHashtable @{LogName='Microsoft-Windows-Windows Firewall With Advanced Security/Firewall'; Id=2004} | Select-Object -First 10
```

### Palo Alto / Fortinet / Cisco

```bash
# Palo Alto: logs de tráfico
grep "traffic" /var/log/pan/traffic.log | grep "deny" | head -20

# Fortinet: logs de firewall
grep "date=2026-08-20" /var/log/fortigate.log | grep "action=deny" | head -20

# Cisco ASA: logs
show logging | grep "%ASA-4-106023"
# (106023 = denied connection)
```

---

## 5. Forense DNS

### ¿Por qué es importante?

El DNS es el **libro de visitas** de la red. Cada dominio consultado revela:
- Qué servicios usó el atacante
- Qué dominios de C2 contactó
- Qué datos exfiltró (si usa DNS tunneling)

### Análisis de logs DNS

```bash
# Linux (dnsmasq)
cat /var/log/dnsmasq.log | awk '{print $NF}' | sort | uniq -c | sort -rn | head -20

# Windows DNS Server
Get-DnsServerLog | Where-Object {$_.Message -like "*query*"} | Select-Object -First 20

# Bind9
grep "queries:" /var/log/named/queries.log | awk '{print $NF}' | sort | uniq -c | sort -rn
```

### DNS Tunneling Detection

```bash
# Indicadores de DNS tunneling:
# 1. Queries DNS muy largas (>50 caracteres)
# 2. Muchas queries a subdominios de un mismo dominio
# 3. Queries TXT inusuales
# 4. Tráfico DNS constante

# Buscar queries largas
cat dns.log | awk '{if(length($NF)>50) print}' | head -20

# Buscar dominios con muchos subdominios
cat dns.log | awk '{print $NF}' | cut -d. -f1-2 | sort | uniq -c | sort -rn | head -20

# Buscar queries TXT inusuales
cat dns.log | grep "TXT" | head -20
```

### Herramientas de análisis DNS

| Herramienta | Uso |
|---|---|
| **dnscap** | Captura de tráfico DNS |
| **DNScat2** | Detección de DNS tunneling |
| **passivedns** | Análisis de DNS pasivo |
| **Security Onion** | SIEM con análisis DNS integrado |

---

## 6. Detección de C2 (Command & Control)

### Indicadores de C2

| Indicador | Qué buscar | Herramienta |
|---|---|---|
| **Beaconing** | Conexiones periódicas regulares | Wireshark, Zeek |
| **DGA** | Dominios generados algorítmicamente | Análisis DNS |
| **Domain fronting** | HTTPS a dominio legítimo, contenido malicioso | Proxy logs |
| **DNS over HTTPS** | DNS cifrado para evadir monitoreo | Proxy logs |
| **IP hardcodeadas** | Conexiones directas a IPs | Firewall logs |
| **User-Agent genérico** | python-requests, curl, wget | HTTP logs |

### Análisis de beaconing

```bash
# Beaconing: conexiones periódicas a un servidor C2
# Patrón típico: cada 30s, 60s, 5min, etc.

# Con Wireshark:
# 1. Filtrar por IP del C2
# 2. Ver time delta entre packets
# 3. Si el delta es constante → beaconing

# Con tshark:
tshark -r captura.pcap -Y "ip.addr == 185.234.72.15" \
    -T fields -e frame.time_relative -e ip.src -e ip.dst | \
    awk '{print $1}' | awk 'NR>1{print $1-prev}{prev=$1}' | sort | uniq -c | sort -rn | head -10

# Si hay un delta constante (ej: 30 segundos), es beaconing
```

### Detección de DGA (Domain Generation Algorithm)

```bash
# Los DGA generan dominios pseudo-aleatorios
# Indicadores:
# - Subdominios largos y aleatorios
# - Alta entropía en el nombre del dominio
# - Muchos NXDOMAIN responses

# Analizar entropía de dominios
cat dns.log | awk '{print $NF}' | while read domain; do
    entropy=$(echo -n "$domain" | fold -w1 | sort | uniq -c | sort -rn | \
        awk '{p=$1/length; printf "-%s*log2(%s)", p, p}' | bc -l | tr -d '\n')
    echo "$entropy $domain"
done | sort -rn | head -20
```

---

## 7. Análisis de logs de proxy

### Squid (Linux)

```bash
# Ver logs de proxy
tail -f /var/log/squid/access.log

# Analizar dominios más consultados
cat /var/log/squid/access.log | awk '{print $7}' | cut -d/ -f3 | sort | uniq -c | sort -rn | head -20

# Buscar descargas sospechosas
grep -iE "\.exe|\.ps1|\.bat|\.vbs|\.dll" /var/log/squid/access.log

# Buscar conexiones a IPs (no dominios)
grep -E "^[0-9]+\.[0-9]+\.[0-9]+\.[0-9]+" /var/log/squid/access.log
```

### Windows Proxy (TMG/Forefront)

```powershell
# Ver logs de proxy
Get-Content "C:\Program Files\Microsoft Forefront TMG\Logs\W3SVC1\*.log" | Select-Object -Last 100

# Buscar User-Agent sospechoso
Select-String -Path "C:\Program Files\Microsoft Forefront TMG\Logs\W3SVC1\*.log" -Pattern "python-requests|curl|wget"
```

### Cloudflare / Zscaler

```bash
# Cloudflare logs (via API)
curl -H "X-Auth-Email: email@company.com" \
     -H "X-Auth-Key: API_KEY" \
     "https://api.cloudflare.com/client/v4/zones/ZONE_ID/logs/received?start=2026-08-20T00:00:00Z&end=2026-08-20T23:59:59Z"

# Zscaler logs (via API)
curl -H "Authorization: API_KEY" \
     "https://admin.zscaler.net/api/v1/logs?start=2026-08-20"
```

---

## 8. Flujos de trabajo

### Flujo 1: Análisis de PCAP

```bash
# 1. Importar PCAP en Wireshark
# 2. Aplicar filtro: ip.addr == <IP sospechosa>
# 3. Analizar conversations (Statistics > Conversations)
# 4. Exportar objetos HTTP
# 5. Seguir streams TCP (Follow > TCP Stream)
# 6. Documentar hallazgos
```

### Flujo 2: Análisis de logs

```bash
# 1. Recopilar logs de firewall, DNS, proxy
# 2. Unificar en un formato común
# 3. Correlacionar por timestamp
# 4. Buscar IPs y dominios sospechosos
# 5. Identificar patrones de actividad
# 6. Documentar hallazgos
```

### Flujo 3: Detección de C2

```bash
# 1. Buscar beaconing (conexiones periódicas)
# 2. Analizar DNS queries (DGA, tunneling)
# 3. Revisar proxy logs (descargas, User-Agents)
# 4. Correlacionar con Intel de amenazas (MISP, OTX)
# 5. Identificar dominios/IPs de C2
# 6. Bloquear y documentar
```

---

## 9. Defensa y detección

### Para Blue Team

| Técnica atacante | Detección | Implementación |
|---|---|---|
| **C2 beaconing** | Conexiones periódicas | Monitoreo de intervalos |
| **DNS tunneling** | Queries largas, muchos subdominios | Análisis de DNS |
| **Exfiltración HTTPS** | Tráfico saliente inusual | Proxy con SSL inspection |
| **Domain fronting** | Conexiones a CDNs inusuales | Análisis de SNI vs Host header |
| **Protocolos evasivos** | DNS over HTTPS, ICMP tunneling | Monitoreo de protocolos |

### Implementación de monitoreo

```bash
# 1. SIEM con alertas de red
# (Splunk, ELK, QRadar)

# 2. Zeek (análisis de red)
zeek -i eth0
# Genera logs: conn.log, dns.log, http.log, ssl.log

# 3. Suricata (IDS/IPS)
suricata -c /etc/suricata/suricata.yaml -i eth0

# 4. Network Miner (análisis forense)
networkminer -f captura.pcap
```

---

## 10. Referencias

| Recurso | URL |
|---|---|
| **Wireshark** | [https://www.wireshark.org/](https://www.wireshark.org/) |
| **Zeek (formerly Bro)** | [https://zeek.org/](https://zeek.org/) |
| **Suricata** | [https://suricata.io/](https://suricata.io/) |
| **NetworkMiner** | [https://www.netresec.com/?page=NetworkMiner](https://www.netresec.com/?page=NetworkMiner) |
| **SANS FOR558** | [https://www.sans.org/cyber-security-courses/network-forensic-analysis-response/](https://www.sans.org/cyber-security-courses/network-forensic-analysis-response/) |
| **MITRE ATT&CK** | [https://attack.mitre.org/](https://attack.mitre.org/) |

---

## 📝 Entregable de portafolio

```markdown
# Forense de Red — Caso INC-2026-0847

## Contexto
- Fuente: Captura PCAP (10GB) + logs de firewall (1GB)
- Sospecha: exfiltración de datos
- Periodo: 2026-08-20 00:00 - 23:59 UTC

## Hallazgos
1. **Beaconing detectado:**
   - IP: 185.234.72.15
   - Intervalo: 30 segundos exactos
   - Protocolo: HTTPS (443)
   - Duración: 14 horas

2. **DNS Tunneling:**
   - Dominio: x.company.com
   - Queries: 12,000+ (promedio 833/hora)
   - Subdominios: 45 caracteres promedio

3. **Exfiltración:**
   - Datos enviados via DNS queries (base64 encoded)
   - Volumen estimado: ~5MB
   - Destino: x.company.com

## Conclusión
- Reverse shell con beaconing de 30 segundos
- Datos exfiltrados via DNS tunneling
- C2 server: 185.234.72.15

## Evidencia
- PCAP: /evidencia/caso001/captura.pcap (SHA-256: 8f7e6d5c...)
- Logs: /evidencia/caso001/logs/
- Reporte: /evidencia/caso001/forense_red.pdf
```

---

**[⬅ Volver al módulo](../README.md)** · **[→ Metadatos Forenses](../analisis-metadatos/01-metadatos-forenses.md)**
