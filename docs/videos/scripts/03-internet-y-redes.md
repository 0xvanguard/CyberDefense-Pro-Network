# 🎬 Video 03: Internet y Redes

**Duración:** 20 minutos
**Módulo:** Fundamentos 03
**Objetivo:** Entender TCP/IP, DNS, HTTP y cómo viajan los datos

---

## 📝 Guión

### [00:00] Intro (30 seg)

```
"Bienvenido a CDPN. En este video vamos a entender cómo funciona internet.
No desde el lado de usuario, sino desde el lado de la seguridad.
¿Sabes qué pasa cuando escribes google.com en tu navegador? 
Vamos a verlo."
```

---

### [00:30] Modelo TCP/IP (3 min)

**Visual:** Diagrama de 4 capas

```
"Internet se basa en el modelo TCP/IP, que tiene 4 capas:

1️⃣ CAPA DE APLICACIÓN — Donde interactúas
   HTTP, HTTPS, DNS, FTP, SSH, SMTP
   
2️⃣ CAPA DE TRANSPORTE — Confiable o rápida
   TCP: confiable, ordenado (web, email)
   UDP: rápido, sin garantía (video, gaming)
   
3️⃣ CAPA DE INTERNET — Direcciones
   IP addresses, routing, subnets
   
4️⃣ CAPA DE ACCESO A RED — Física
   Ethernet, WiFi, cables

¿Por qué importa? Porque los atacantes explotan en CADA capa."
```

**Animación:** Paquete de datos bajando por las capas

---

### [03:30] DNS (3 min)

**Visual:** Diagrama de resolución DNS

```
"DNS es el sistema de nombres de dominio. Traduce nombres a IPs.

Cuando escribes google.com:

1. Tu PC consulta su caché DNS
2. Si no está, consulta tu DNS local (router)
3. Si no está, consulta DNS root (13 servidores raíz)
4. Los root servers te dicen quién maneja .com
5. Los servers .com te dicen quién maneja google.com
6. Google te da la IP: 142.250.80.46

Todo esto pasa en MILISEGUNDOS.

¿Y por qué importa en seguridad?
Porque los atacantes pueden:
- Envenenar caché DNS (redirect a sitio falso)
- Crear dominios falsos (phishing)
- Usar DNS para C2 (Command and Control)"
```

**Animación:** Flujo de DNS paso a paso

---

### [06:30] HTTP/HTTPS (4 min)

**Visual:** Request/Response HTTP

```
"HTTP es el protocolo de la web. Funciona con requests y responses.

REQUEST (lo que tú envías):
GET /index.html HTTP/1.1
Host: google.com
User-Agent: Mozilla/5.0
Accept: text/html

RESPONSE (lo que el servidor responde):
HTTP/1.1 200 OK
Content-Type: text/html
Content-Length: 1234

Y HTTPS es HTTP con cifrado TLS.
Los datos van encriptados entre tu navegador y el servidor.

¿Por qué importa?
- Sin HTTPS: cualquiera puede ver tu tráfico
- Con HTTPS: solo tú y el servidor pueden leerlo

Y los atacantes pueden:
- Interceptarlo (Man-in-the-Middle)
- Forzar HTTP (Downgrade attack)
- Robar cookies de sesión"
```

**Animación:** Request/Response visual

---

### [10:30] Puertos (3 min)

**Visual:** Tabla de puertos comunes

```
"Los puertos son como las puertas de un edificio.
Cada servicio tiene su propio puerto.

PUERTOS COMUNES:
20/21 — FTP (transferencia de archivos)
22 — SSH (acceso remoto seguro)
23 — Telnet (acceso remoto inseguro)
25 — SMTP (email saliente)
53 — DNS (resolución de nombres)
80 — HTTP (web sin cifrar)
110 — POP3 (email entrante)
143 — IMAP (email entrante)
443 — HTTPS (web con cifrar)
445 — SMB (archivos compartidos)
3389 — RDP (escritorio remoto)

¿Por qué importa?
Porque Nmap escanea puertos para ver qué servicios corren.
Y un puerto abierto es una puerta que un atacante puede intentar abrir."
```

---

### [13:30] Firewalls (2 min)

**Visual:** Diagrama de firewall

```
"Un firewall es un filtro de tráfico.

Puede ser:
- HARDWARE: dispositivo físico
- SOFTWARE: programa en el servidor
- CLOUD: servicio externo

Reglas típicas:
✅ Permitir: HTTP (80), HTTPS (443), SSH (22)
❌ Bloquear: Telnet (23), FTP (21) innecesario
⚠️ Monitorear: Todo lo demás

Y los atacantes pueden:
- Eviar firewall (tunneling)
- Usar puertos permitidos (C2 over HTTPS)
- Atacar desde dentro (insider threat)"
```

---

### [15:30] Ejercicio Práctico (3 min)

**Visual:** Terminal con comandos

```
"Ahora veamos一些 comandos prácticos:

# Ver tu IP
ip addr show

# Ver rutas
ip route show

# Hacer ping
ping google.com

# Tracear ruta
traceroute google.com

# Ver puertos abiertos
netstat -tlnp

# DNS lookup
nslookup google.com
dig google.com

Prueba estos comandos en tu terminal y observa los resultados."
```

---

### [18:30] Resumen (1.5 min)

**Visual:** Key points

```
"Resumimos lo que aprendimos:

✅ TCP/IP tiene 4 capas: Aplicación, Transporte, Internet, Acceso
✅ DNS traduce nombres a IPs en milisegundos
✅ HTTP/HTTPS son los protocolos de la web
✅ Cada servicio tiene un puerto específico
✅ Los firewalls filtran tráfico

Y todo esto es atacable. Por eso la seguridad es tan importante.

En el próximo video veremos Sistemas Operativos y Terminal.
Nos vemos."
```

---

## 🎯 Checklist de Grabación

- [ ] Diagramas de TCP/IP creados
- [ ] Animación de DNS preparada
- [ ] Request/Response HTTP documentado
- [ ] Tabla de puertos lista
- [ ] Terminal grabado para ejercicio
- [ ] Resumen visual creado

---

*Script creado para CDPN — Video 03 de Fundamentos*
