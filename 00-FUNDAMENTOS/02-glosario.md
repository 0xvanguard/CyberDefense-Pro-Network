# 02 — Glosario de términos esenciales

> **Cómo usar este archivo:** No hace falta leerlo entero. Vuelve a él cada vez que un archivo nuevo use un término que no conoces. Está organizado por tema y, dentro de cada tema, alfabéticamente.

> 📖 Convenciones: términos en **negrita** son los más importantes; ↗ señala a otro término del glosario; 📘 a un archivo de la base; 📂 a una carpeta del repo.

---

## 🔤 A–E

**Ataque** — Cualquier intento de comprometer la ↗ **C**onfidencialidad, ↗ **I**ntegridad o ↗ disponibilidad de un sistema.

**APT (Advanced Persistent Threat)** — Atacante sofisticado (a menudo estatal) que entra, se queda y observa durante meses.

**Attack Surface** — La "superficie atacable": todos los puntos por donde un atacante podría entrar.

**Authentication** — Probar quién eres (sabes algo, tienes algo, eres algo). Ver ↗ **MFA**.

**Authorization** — Qué se te permite hacer una vez autenticado.

**Backdoor** — Puerta trasera: acceso oculto que evita la autenticación normal.

**Blue Team** — Equipo de defensa. Ver 📘 [`01-que-es-ciberseguridad.md`](./01-que-es-ciberseguridad.md).

**Bug Bounty** — Programa donde una empresa paga a hackers éticos por reportar vulnerabilidades.

**CIA Triad** — Confidencialidad, Integridad, Disponibilidad (Availability). Los 3 pilares.

**CVE (Common Vulnerabilities and Exposures)** — ID único para una vulnerabilidad pública. Ej: `CVE-2024-12345`.

**CVSS** — Sistema de 0 a 10 para puntuar la gravedad de un ↗ **CVE**.

**CWE (Common Weakness Enumeration)** — Categoría de debilidad de software (la "familia" del problema).

**DDoS (Distributed Denial of Service)** — Tumbar un servicio enviándole tráfico desde miles de máquinas.

**DNS (Domain Name System)** — La "agenda" de internet: traduce `google.com` a `142.250.190.78`.

**Endpoint** — Cualquier dispositivo conectado: laptop, móvil, servidor, IoT.

**Enumeration** — Fase del pentest donde recopilas usuarios, recursos, servicios de un objetivo.

**Exploit** — Código que aprovecha una vulnerabilidad.

---

## 🔤 F–M

**Firewall** — Filtra el tráfico de red según reglas. Hay de hardware y de software.

**Forensics** — Investigación post-incidente para entender qué pasó, cómo y cuándo.

**Hash** — Función que convierte cualquier dato en una cadena fija de tamaño. Ej: SHA-256. Ver 📘 [`05-criptografia-basica.md`](./05-criptografia-basica.md).

**Honeypot** — Sistema señuelo: parece real pero sirve para detectar y estudiar atacantes.

**HTTP / HTTPS** — Protocolo de la web. La S significa "con TLS" (cifrado).

**IDS / IPS** — *Intrusion Detection / Prevention System*. Detecta o bloquea ataques.

**Incident** — Un evento de seguridad confirmado que requiere respuesta.

**Ing Social (Ingeniería Social)** — Engañar a personas para que revelen info o hagan algo. ↗ **Phishing**.

**IOC (Indicator of Compromise)** — Huella que deja un ataque: IP, hash, dominio, patrón.

**IP (Internet Protocol)** — La dirección numérica de cada dispositivo en una red. `192.168.1.1`.

**JWT** — Token firmado para autenticación web sin estado.

**Kill Chain** — Pasos típicos de un ataque: reconocimiento → arma → entrega → exploitation → instalación → command & control → acciones.

**Lateral Movement** — Una vez dentro, el atacante se mueve a otros sistemas de la misma red.

**Linux** — Familia de sistemas operativos (Ubuntu, Debian, Kali, etc.) muy usada en servidores y seguridad.

**Malware** — Software malicioso. Incluye virus, troyanos, ransomware, spyware.

**MFA (Multi-Factor Authentication)** — Pedir 2+ pruebas de identidad. La MFA bloquea el 99% de los ataques de cuentas.

**MITM (Man in the Middle)** — Atacante que intercepta comunicación entre dos partes.

---

## 🔤 N–S

**Nmap** — Escáner de puertos. La navaja suiza del reconocimiento. Ver 📘 [`08-herramientas-esenciales.md`](./08-herramientas-esenciales.md).

**OSINT (Open Source Intelligence)** — Recopilar info de fuentes públicas: redes sociales, leaks, DNS, etc.

**OWASP** — Organización que mantiene el famoso *Top 10* de vulnerabilidades web. Ver 📘 [`06-vulnerabilidades.md`](./06-vulnerabilidades.md).

**P0 / P1 / P2** — Prioridades: P0 = crítico (cae producción), P1 = urgente, P2 = importante.

**Password Hashing** — Guardar contraseñas como ↗ **hash** (no en texto plano).

**Patch** — Actualización que corrige una vulnerabilidad.

**Pentest** — Test de penetración autorizado. Buscar vulnerabilidades con permiso.

**Phishing** — Email/mensaje fraudulento que imita a alguien legítimo. ↗ **Ing Social**.

**Port (puerto)** — "Puerta" de un servicio en una máquina. HTTP=80, HTTPS=443, SSH=22.

**Privilege Escalation** — Conseguir más permisos de los que deberías tener.

**Purple Team** — Equipo mixto red + blue. Ver 📘 [`01-que-es-ciberseguridad.md`](./01-que-es-ciberseguridad.md).

**Ransomware** — ↗ **Malware** que cifra tus datos y pide rescate.

**Red Team** — Equipo ofensivo. Ver 📘 [`01-que-es-ciberseguridad.md`](./01-que-es-ciberseguridad.md).

**Reverse Shell** — Conexión que la víctima abre hacia el atacante. Muy común post-exploit.

**Risk** — Probabilidad × Impacto. Lo que tu jefe quiere ver cuando le pides presupuesto.

**SIEM** — Sistema central que recoge logs y dispara alertas (Splunk, Elastic, Wazuh).

**SOC (Security Operations Center)** — El equipo que vigila 24/7 con ayuda del SIEM.

**SQL Injection** — Inyectar SQL en un input para manipular la base de datos. Ver 📘 [`06-vulnerabilidades.md`](./06-vulnerabilidades.md).

**SSL/TLS** — Protocolo que cifra las comunicaciones en internet. La S de HTTPS.

---

## 🔤 T–Z

**Threat** — Amenaza: algo que podría causar daño (un atacante, una tormenta, un bug).

**Threat Intelligence** — Estudiar amenazas: quién ataca, cómo, por qué, qué busca.

**Threat Hunting** — Buscar activamente atacantes que ya están dentro pero aún no se detectaron.

**Token** — Cadena que prueba que estás autenticado, sin guardar sesión en servidor. Ver ↗ **JWT**.

**TTP (Tactics, Techniques, Procedures)** — Patrones de un atacante. Lo modela MITRE ATT&CK.

**Vulnerability** — Debilidad que un atacante puede explotar.

**WAF (Web Application Firewall)** — Firewall especializado en tráfico HTTP/HTTPS.

**Wireshark** — Analizador de tráfico de red. Captura paquetes para analizarlos. Ver 📘 [`08-herramientas-esenciales.md`](./08-herramientas-esenciales.md).

**XSS (Cross-Site Scripting)** — Inyectar JS malicioso en una página web. Ver 📘 [`06-vulnerabilidades.md`](./06-vulnerabilidades.md).

**Zero-Day** — Vulnerabilidad recién descubierta para la que aún no hay parche.

---

## 📚 Siglas que verás mucho

- **CTF** — *Capture The Flag*: retos de hacking competitivo
- **CSIRT / CERT** — Equipos de respuesta a incidentes
- **EDR / XDR** — Endpoint / Extended Detection & Response
- **GRC** — Governance, Risk, Compliance
- **IAM** — Identity & Access Management
- **IR** — Incident Response
- **MDM** — Mobile Device Management
- **NDR** — Network Detection & Response
- **SOAR** — Security Orchestration, Automation, Response
- **VPN** — Red privada virtual

> 📂 Las definiciones completas de cada rol están en [`01-CIBERSEGURIDAD/`](../01-CIBERSEGURIDAD/) (37 subcarpetas).

---

> ⏭️ **Siguiente:** [`03-internet-y-redes.md`](./03-internet-y-redes.md) — los conceptos mínimos de redes que necesitas.
