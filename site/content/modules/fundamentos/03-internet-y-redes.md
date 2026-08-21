---
title: "03 — Internet y redes: lo mínimo que necesitas saber"
---

# 03 — Internet y redes: lo mínimo que necesitas saber

> 🎯 **Objetivo:** entender qué pasa cuando abres una página web, envías un email o haces un ping. Sin entrar en profundidad académica — solo lo justo para defender o atacar.

## 1. La idea más simple: paquetes, direcciones y routers

Internet es una red de redes. Para que dos máquinas hablen:
1. Tu mensaje se parte en **paquetes**.
2. Cada paquete lleva **direcciones** de origen y destino.
3. **Routers** (enrutadores) van pasando los paquetes hasta el destino.
4. El receptor reensambla los paquetes y ve tu mensaje completo.

## 2. Direcciones

| Tipo | Ejemplo | Para qué |
|---|---|---|
| **IPv4** | `192.168.1.42` | La forma clásica. ~4.000 millones de direcciones. |
| **IPv6** | `2001:db8::1` | La nueva. Direcciones casi infinitas. |
| **MAC** | `aa:bb:cc:dd:ee:ff` | La "dirección física" del hardware de red. |
| **Dominio** | `google.com` | Lo que escribes en el navegador. |

> 💡 Un atacante puede falsificar paquetes (spoofing), interceptarlos (MITM), o inundar un destino con miles de paquetes (DDoS).

## 3. El modelo TCP/IP en 4 capas (simplificado)

```
┌──────────────────────────────────┐
│ 4. Aplicación                    │ ← HTTP, HTTPS, DNS, SSH, SMTP
├──────────────────────────────────┤
│ 3. Transporte                    │ ← TCP (fiable) / UDP (rápido)
├──────────────────────────────────┤
│ 2. Internet                      │ ← IP, ICMP (ping)
├──────────────────────────────────┤
│ 1. Acceso a red / enlace         │ ← Ethernet, WiFi, ARP
└──────────────────────────────────┘
```

**Para defensive:**
- Capa 4 (app): firewalls como WAF, IDS de aplicación
- Capa 3 (transporte): reglas de firewall por puerto
- Capa 2 (internet): filtrado por IP, GeoIP
- Capa 1 (enlace): segurizar switches, segmentar VLANs

## 4. Los protocolos que verás en tu día a día

| Protocolo | Puerto | Uso | ¿Seguro? |
|---|---|---|---|
| **HTTP** | 80 | Web sin cifrar | ❌ |
| **HTTPS** | 443 | Web cifrada (TLS) | ✅ |
| **SSH** | 22 | Consola remota cifrada | ✅ |
| **DNS** | 53 | Resuelve nombres a IPs | ⚠️ a veces |
| **FTP** | 21 | Transferencia de archivos | ❌ (credenciales en claro) |
| **SFTP** | 22 | FTP sobre SSH | ✅ |
| **SMTP** | 25/587 | Envío de email | ⚠️ sin TLS puede ser inseguro |
| **RDP** | 3389 | Escritorio remoto Windows | ⚠️ objetivo de ransomware |
| **SMB** | 445 | Compartición archivos Windows | ⚠️ muy atacado |

> 💡 Aprende los puertos comunes de memoria. Cuando veas el 22 abierto, sabes que hay SSH; el 445 en Windows es para SMB y suele ser mala pinta expuesto a internet.

## 5. DNS — la agenda de internet

Cuando escribes `github.com` en el navegador:

1. Tu equipo pregunta al **resolv DNS** (suele ser el de tu ISP o `8.8.8.8`).
2. El resolv busca en servidores raíz, luego `.com`, luego `github.com`.
3. Te devuelve una IP: `140.82.121.4`.
4. Tu navegador conecta con esa IP.

**Ataques relacionados:**
- **DNS spoofing / poisoning** — resolver devuelve IP falsa
- **DNS tunneling** — sacar datos covertly vía consultas DNS
- **Subdomain takeover** — reclamar un subdominio que apunta a un servicio dado de baja

## 6. HTTP — la web en vivo

Una petición HTTP/1.1 básica:

```http
GET / HTTP/1.1
Host: ejemplo.com
User-Agent: Mozilla/5.0
Cookie: session=abc123
```

Y una respuesta:

```http
HTTP/1.1 200 OK
Content-Type: text/html
Content-Length: 1234

<html>...</html>
```

**Puntos importantes para pentest:**
- **Métodos**: `GET`, `POST`, `PUT`, `DELETE`, `OPTIONS`, `PATCH`
- **Headers sensibles**: `Cookie`, `Authorization`, `X-Forwarded-For`
- **Status codes**: `200` OK, `301` redirige, `401` no auth, `403` prohibido, `404` no existe, `500` error servidor

## 7. TLS / HTTPS — el candado

HTTPS no es un protocolo aparte: es **HTTP sobre TLS**.

Lo que hace TLS:
1. **Handshake** — acuerdan algoritmos, intercambian claves.
2. **Certificado** — el servidor prueba su identidad (cadena de confianza).
3. **Cifrado** — todo el tráfico va cifrado de ahí en adelante.

**Riesgos típicos:**
- Certificados vencidos o auto-firmados
- TLS viejo (TLS 1.0 / 1.1 ya casi prohibidos)
- Certificados para dominios equivocados

## 8. Comandos básicos que vas a usar mil veces

```bash
# Ver tu IP y tu config de red
ip a            # Linux
ipconfig /all   # Windows

# Probar conectividad
ping 8.8.8.8

# Trazar la ruta hasta un destino
traceroute google.com     # Linux/Mac
tracert google.com        # Windows

# Resolución DNS
nslookup google.com
dig google.com            # más detallado (Linux)

# Ver puertos abiertos en tu máquina
ss -tuln         # Linux moderno
netstat -an      # clásico (Windows y Linux viejo)

# Capturar tráfico (necesitas permisos)
sudo tcpdump -i eth0 -c 10
```

## 9. Modelo Zero Trust en una frase

> **"Nunca confíes, siempre verifica."** En lugar de confiar en que "estás dentro de la oficina" o "estás en la VPN", cada petición se valida: quién eres, qué dispositivo tienes, qué intentas hacer, desde dónde.

## 📌 Dónde practicar y profundizar

| Recurso | Dónde |
|---|---|
| Práctica aislada | [`04-LABORATORIOS/labs-propios/`](../04-LABORATORIOS/labs-propios/) |
| Redes y herramientas | [`08-herramientas-esenciales.md`](./08-herramientas-esenciales.md) |
| Pentest web | [`02-pentesting-red-team/`](../02-pentesting-red-team/) |
| Blue team / detección | [`02-SEGURIDAD-INFORMACION/02-blue-team-defensa/`](../02-SEGURIDAD-INFORMACION/02-blue-team-defensa/) |
| Cheatsheets de redes | [`05-RECURSOS/cheatsheets/`](../05-RECURSOS/cheatsheets/) |

## ✏️ Ejercicios prácticos

### Ejercicio 1: Análisis de tu red local (15 min)

```bash
# 1. Descubre tu rango de red
ip a | grep inet | grep -v 127.0.0.1
# Ejemplo: 192.168.1.105/24 → tu rango es 192.168.1.0/24

# 2. Escanea todos los dispositivos
nmap -sn 192.168.1.0/24
# Nota cuántos dispositivos hay: router, celular, smart TV, etc.

# 3. Identifica qué corre en tu router
nmap -sV 192.168.1.1
# ¿Qué puertos están abiertos? ¿HTTP? ¿HTTPS?
```

**Preguntas:**
- ¿Cuántos dispositivos encontraste?
- ¿Algún dispositivo tiene puertos inesperados abiertos?
- ¿Tu router usa la IP por defecto del fabricante?

### Ejercicio 2: DNS en acción (10 min)

```bash
# 1. Resolución básica
dig google.com
# Mira la sección ANSWER: ¿qué IP devuelve?

# 2. Trazar la ruta completa
dig +trace github.com
# Verás: raíz → .com → github.com → IP final

# 3. Consultar tipos de registro
dig MX google.com    # ¿qué servidores de email usa?
dig NS google.com    # ¿qué servidores DNS usa?
dig TXT google.com   # ¿qué registros TXT tiene? (SPF, DKIM)

# 4. Ver tu propio DNS
cat /etc/resolv.conf   # Linux
ipconfig /displaydns    # Windows
```

**Preguntas:**
- ¿Qué IP tiene google.com en tu país?
- ¿Cuántos saltos hay desde tu DNS hasta google.com?

### Ejercicio 3: Captura y análisis de tráfico (20 min)

```bash
# 1. Captura 30 segundos de tráfico DNS
sudo tcpdump -i eth0 port 53 -w dns_capture.pcap -c 100

# 2. Abre con tshark y analiza
tshark -r dns_capture.pcap -T fields -e dns.qry.name | sort | uniq -c | sort -rn
# Verás qué dominios resuelve tu equipo más frecuentemente

# 3. Captura solo HTTP
sudo tcpdump -i eth0 port 80 -A | head -50
# Verás headers HTTP en texto plano (¡sin cifrar!)
```

**Preguntas:**
- ¿Qué dominios aparecen más? ¿Son legítimos?
- ¿Viste contraseñas o datos sensibles en el tráfico HTTP?

### Ejercicio 4: Test de puertos remotos (10 min)

```bash
# 1. Escanea scanme.nmap.org (legal para practicar)
nmap -sV scanme.nmap.org

# 2. Mira los servicios y versiones
# ¿Qué software corren? ¿Está actualizado?

# 3. Escanea solo puertos comunes
nmap -p 21,22,25,53,80,443,3306,3389,8080 scanme.nmap.org
```

### Ejercicio 5: Construye tu propia cheatsheet de red (10 min)

Crea un archivo `red-cheatsheet.md` con:

```markdown
# Mi Cheatsheet de Redes

## IPs y subredes
- Mi IP: ___
- Mi gateway: ___
- Mi DNS: ___
- Rango de red: ___/24

## Puertos comunes que memorizo
| Puerto | Servicio | Riesgo si abierto |
|--------|----------|-------------------|
| 22 | SSH | Bajo si autorizado |
| 80 | HTTP | Medio |
| 443 | HTTPS | Bajo |
| 3389 | RDP | ALTO - ransomware |
| 445 | SMB | ALTO - EternalBlue |

## Comandos que uso siempre
- `nmap -sV IP` → escaneo con versiones
- `dig dominio` → resolución DNS
- `traceroute IP` → ruta de paquetes
- `tcpdump -i eth0 port 80` → capturar HTTP
```

> ⏭️ **Siguiente:** [`04-sistema-operativo-y-terminal.md`](./04-sistema-operativo-y-terminal.md) — Linux y Windows desde la perspectiva defensiva.
