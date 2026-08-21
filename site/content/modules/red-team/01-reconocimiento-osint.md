---
title: 01 — Reconocimiento OSINT (Clásico, sin IA)
description: 01 — Reconocimiento OSINT (Clásico, sin IA)
---

# 01 — Reconocimiento OSINT (Clásico, sin IA)

> **Objetivo del módulo:** Dominar las técnicas clásicas de reconocimiento y OSINT técnico para mapear la superficie de ataque de un objetivo, sin usar IA, de forma sistemática, legal y reproducible.

Este módulo es la **puerta de entrada práctica** a el Área 1. Aquí aprendes a descubrir **qué existe**, **dónde está** y **cómo se ve** un objetivo antes de pensar en explotar nada.

---

## 🎯 Objetivos de aprendizaje

Al completar este módulo deberías ser capaz de:

- Explicar la diferencia entre **OSINT general** y **reconocimiento técnico aplicado a pentesting**.
- Identificar el **scope autorizado** (dominios, rangos IP, assets en nube, subdominios).
- Usar herramientas clásicas (whois, dig, Nmap, etc.) para:
  - Resolver dominios, registrar DNS y obtener información de registros.
  - Descubrir hosts activos en un rango de red.
  - Enumerar puertos y servicios expuestos.
- Organizar tus hallazgos en un formato estructurado (tablas, notas, diagramas simples).
- Generar un **informe de reconocimiento** claro y reutilizable para siguientes fases del pentest.

---

## 📚 Teoría mínima

Este módulo asume que te concentras en **OSINT técnico y recon activo básico** sobre objetivos autorizados.

### OSINT vs Reconocimiento técnico

- **OSINT (Open Source Intelligence):**
  - Información obtenida de fuentes públicas: buscadores, redes sociales, registros públicos, leaks, etc.
  - Puede incluir datos humanos (personas, roles), de negocio y técnicos.

- **Reconocimiento técnico aplicado a pentesting:**
  - Se centra en la **superficie técnica**: dominios, subdominios, IPs, puertos, servicios, tecnologías visibles.
  - Incluye recon pasivo (sin tocar directamente al objetivo) y recon activo controlado (como Nmap) dentro del scope autorizado.

### Fases típicas de recon

1. **Definición de scope**
   - Qué dominios, subdominios, rangos de IP y aplicaciones están autorizados.
   - Qué está explícitamente fuera de alcance.

2. **Reconocimiento pasivo**
   - WHOIS, registros DNS, certificados (CRT), datos de OSINT general.
   - Sin enviar tráfico directo al objetivo (o lo mínimo posible).

3. **Descubrimiento de hosts**
   - Identificar qué IPs están activas dentro del rango autorizado.

4. **Enumeración de puertos y servicios**
   - Identificar qué puertos están abiertos y qué servicios parecen correr allí.

5. **Organización de hallazgos**
   - Tablas por host, servicio, versión y posibles vectores de ataque a investigar.

---

## 🗂 Estructura del módulo

```text
01-reconocimiento-osint/
├── teoria/
│   └── 01-fundamentos-osint.md   ← Conceptos base, metodología, fases
│
├── herramientas/
│   ├── whois/                    ← Uso básico + ejemplos
│   ├── dig-dns/                  ← Consultas DNS típicas
│   ├── nmap/                     ← Escaneos host discovery + puertos
│   └── otros/                    ← Otras herramientas de apoyo
│
├── tecnicas/
│   ├── 01-definir-scope.md          ← Cómo delimitar scope de forma profesional
│   ├── 02-recon-pasivo-dns-whois.md ← Procedimiento paso a paso
│   ├── 03-host-discovery-nmap.md    ← Descubrimiento de hosts
│   └── 04-enumeracion-puertos.md    ← Puertos/servicios básicos
│
├── laboratorios/
│   ├── lab-01-mapeo-superficie-basico/
│   │   ├── enunciado.md           ← Planteamiento del lab
│   │   ├── guia-paso-a-paso.md    ← Opcional, solo si se necesita apoyo
│   │   └── entregables.md         ← Qué debe producir el estudiante
│   └── (futuros labs...)
│
└── portafolio/
    └── TEMPLATE-informe-recon.md  ← Plantilla de informe de reconocimiento
```

> Todos los labs utilizarán una **empresa ficticia** y entornos controlados (rango de IPs de laboratorio, dominios simulados, etc.). Nunca se practicarán técnicas sobre objetivos reales sin autorización.

---

## 📂 Tipos de entregables del módulo

En este módulo se esperan entregables clásicos de recon, por ejemplo:

- **`informe-recon-inicial.md`**
  - Resumen del objetivo, scope, metodología y hallazgos clave.

- **Tablas de hosts y servicios**
  - Host/IP, puertos abiertos, servicios detectados, notas.

- **Notas técnicas de comandos**
  - Colección de comandos usados (whois, dig, Nmap) con comentarios.

- **Diagrama simple de superficie de ataque** (opcional)
  - Puede ser un esquema en texto o una imagen sencilla mostrando hosts y servicios principales.

Estos entregables se podrán luego enlazar desde `PORTAFOLIO.md` como evidencia de habilidades de reconocimiento.

---

## 🔗 Encaje del módulo en el área y la ruta

Dentro de el Área 1, este módulo es el **primer paso** de la ruta ofensiva:

1. `01-reconocimiento-osint/`  ← Este módulo (recon clásico)
2. `02-pentesting-red-team/`   ← Ciclo completo de pentest sobre labs
3. `03-analisis-vulnerabilidades/`
4. `04-explotacion-web/` y `05-post-explotacion/`
5. Otros módulos ofensivos (forense, ingeniería social, criptografía)

También alimenta directamente:

- Rutas de **Pentester / Red Team**.
- Rutas de **Analista SOC / Blue Team**, que necesitan entender qué se expone.
- Área 3, donde más adelante podrás automatizar parte de este recon con IA, pero sobre una base clásica sólida.

---

---

## 🛠️ Herramientas esenciales de OSINT

### WHOIS — Información de dominios

```bash
# WHOIS básico
cyberwhois example.com
cyberwhois 8.8.8.8

# Datos que obtienes:
# - Registrante (nombre, email, dirección)
# - Fechas de registro/expiración
# - Nameservers
# - Rango IP asociado
# - ASN (Autonomous System Number)

# WHOIS conwhois CLI
whois example.com | grep -i "registrar\|creation\|expir"
```

### DNS — Mapa del dominio

```bash
# Registros DNS esenciales
nslookup example.com                    # IP principal
dig example.com A                       # Registro A (IPv4)
 dig example.com AAAA                    # Registro A (IPv6)
 dig example.com MX                      # Mail servers
 dig example.com NS                      # Nameservers
 dig example.com TXT                     # Textos (SPF, DKIM, etc.)
dig example.com SOA                     # Start of Authority

# Subdominios con brute force
for sub in mail ftp vpn webmail admin portal api dev staging; do
  dig +short $sub.example.com
  done

# Usando subfinder (herramienta OSINT)
subfinder -d example.com -silent

# Usando amass
amass enum -passive -d example.com
```

### Nmap — Reconocimiento activo

```bash
# Descubrimiento de hosts (solo ping)
 nmap -sn 192.168.1.0/24                 # Descubrir hosts activos
 nmap -sn -PE 192.168.1.0/24              # Solo ping ICMP

# Escaneo completo de puertos
nmap -sS -sV -sC -O -p- 192.168.1.10    # TCP SYN + version + scripts + OS
nmap -sU -p- 192.168.1.10               # UDP scan (lento)

# Output para analizar después
nmap -sV -oN scan.txt 192.168.1.0/24     # Output normal
nmap -sV -oX scan.xml 192.168.1.0/24     # Output XML (para tools)

# Scripts de Nmap
nmap --script=http-enum 192.168.1.10     # Enumerar directorios web
nmap --script=smb-enum-shares 192.168.1.10  # Enumerar shares SMB
 nmap --script=ssl-cert 192.168.1.10     # Ver certificado SSL
```

### OSINT web y redes sociales

```bash
# Buscar emails asociados a un dominio
theHarvester -d example.com -b google,linkedin

# Buscar subdominios en Certificate Transparency
crt.sh/?q=%.example.com

# Buscar en Google (dorks)
# site:example.com filetype:pdf
# site:example.com inurl:admin
# site:example.com intitle:"index of"

# Buscar información de empleados
# linkedin.com/company/example +People
# hunter.io (buscar emails corporativos)

# Verificar si un dominio está en listas negras
# virustotal.com/gui/domain/example.com
# urlscan.io
```

---

## 🧪 Ejercicios prácticos

### Ejercicio 1: Mapeo completo de un dominio

```bash
# Objetivo: mapear example.com completamente
# Paso 1: WHOIS
whois example.com | tee evidencias/whois.txt

# Paso 2: DNS
 dig example.com A MX NS TXT SOA | tee evidencias/dns.txt

# Paso 3: Subdominios
subfinder -d example.com -silent | tee evidencias/subdominios.txt

# Paso 4: Descubrir IPs
while read sub; do
  dig +short $sub.example.com
done < evidencias/subdominios.txt | sort -u | tee evidencias/ips.txt

# Paso 5: Nmap sobre las IPs encontradas
 nmap -sV -sC -oN evidencias/nmap.txt -iL evidencias/ips.txt

# Paso 6: Generar reporte
echo "# Reporte OSINT: example.com" > reporte.md
echo "- Dominio: example.com" >> reporte.md
echo "- IPs encontradas: $(wc -l < evidencias/ips.txt)" >> reporte.md
echo "- Subdominios: $(wc -l < evidencias/subdominios.txt)" >> reporte.md
echo "- Puertos abiertos: $(grep -c 'open' evidencias/nmap.txt)" >> reporte.md
```

### Ejercicio 2: Análisis de un rango de IPs

```bash
# Objetivo: analizar 192.168.1.0/24
# Paso 1: Descubrir hosts
nmap -sn 192.168.1.0/24 -oG - | grep "Up" | awk '{print $2}' | tee hosts.txt

# Paso 2: Escaneo rápido de puertos comunes
 nmap -sV --top-ports 100 -iL hosts.txt -oN scan-rapido.txt

# Paso 3: Escaneo profundo de hosts interesantes
nmap -sV -sC -O -p- $(head -1 hosts.txt) -oN scan-profundo.txt

# Paso 4: Documentar hallazgos
echo "Hosts activos: $(wc -l < hosts.txt)"
echo "Puertos abiertos: $(grep -c 'open' scan-rapido.txt)"
```

### Ejercicio 3: OSINT de redes sociales

```bash
# Objetivo: obtener información de empleados de una empresa ficticia
# Paso 1: Buscar emails
theHarvester -d empresa-ficticia.com -b google -f reporte-emails.html

# Paso 2: Buscar en LinkedIn
# - Buscar "empresa-ficticia" en LinkedIn
# - Filtrar por empleados
# - Documentar roles y nombres

# Paso 3: Buscar en Google
# site:linkedin.com/in "empresa-ficticia"
# site:github.com "empresa-ficticia"

# Paso 4: Crear tabla de hallazgos
cat > tabla-empleados.md << 'EOF'
| Nombre | Rol | Email | Perfil |
|--------|-----|-------|--------|
| Juan Pérez | Admin | juan@empresa.com | linkedin.com/in/juan |
EOF
```

### Ejercicio 4: CTF de Reconocimiento

```bash
# Reto: encontrar 5 vulnerabilidades en un dominio de práctica
# 1. Subdominios ocultos (usando subfinder + amass)
# 2. Directorios sensibles (usando gobuster)
gobuster dir -u http://target.com -w /usr/share/wordlists/dirb/common.txt

# 3. Versiones de software obsoletas
nmap -sV target.com | grep -i "version"

# 4. Información filtrada en headers
curl -I http://target.com | grep -i "server\|x-powered"

# 5. Archivos expuestos
gobuster dir -u http://target.com -w /usr/share/wordlists/dirb/common.txt -x php,txt,bak,old
```

---

## 📋 Checklist de reconocimiento

Antes de pasar a la fase de explotación, verifica que tienes:

- [ ] Dominio y subdominios principales
- [ ] Rango de IPs asociado
- [ ] Puertos abiertos y servicios
- [ ] Versiones de software
- [ ] Tecnologías web detectadas
- [ ] Empleados / emails (si aplica)
- [ ] Información de WHOIS
- [ ] Registros DNS relevantes
- [ ] Certificados SSL/TLS
- [ ] Directorios y archivos expuestos

---

## ✅ Próximos pasos dentro de este módulo

Los siguientes pasos naturales serán:

- Crear `teoria/01-fundamentos-osint.md` con la teoría resumida que soporte estas prácticas.
- Definir el **Lab 01 — Mapeo de superficie básico** en `laboratorios/lab-01-mapeo-superficie-basico/`.
- Crear `portafolio/TEMPLATE-informe-recon.md` para unificar cómo presentas tus hallazgos.

Con eso, el módulo quedará listo para empezar a añadir ejercicios concretos y ejemplos de alta calidad para tu portafolio.
