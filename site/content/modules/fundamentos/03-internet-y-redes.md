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

## ✏️ Ejercicios

1. **Haz un traceroute** desde tu casa a `github.com`. ¿Cuántos saltos? ¿En qué país pasan?
2. **Mira tu propio router.** Entra a `192.168.1.1` (o `192.168.0.1`) y mira qué dispositivos hay conectados.
3. **Prueba DNS:** `dig +trace google.com`. Verás todos los servidores consultados.
4. **Mira los headers HTTP:** abre las DevTools del navegador, pestaña *Network*, recarga una página, mira los *Request Headers*.

> ⏭️ **Siguiente:** [`04-sistema-operativo-y-terminal.md`](./04-sistema-operativo-y-terminal.md) — Linux y Windows desde la perspectiva defensiva.
