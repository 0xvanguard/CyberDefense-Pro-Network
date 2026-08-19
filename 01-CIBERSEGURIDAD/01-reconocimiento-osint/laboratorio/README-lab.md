# 🧪 Lab 01 — Reconocimiento OSINT en entorno local

> **Objetivo del lab:** Practicar reconocimiento OSINT completo contra un objetivo controlado, sin riesgo legal, en un entorno 100% reproducible con Docker.

---

## ¿Qué vas a practicar?

1. Ejecutar theHarvester contra un dominio de práctica público autorizado
2. Realizar reconocimiento DNS manual
3. Buscar subdominios via certificados TLS
4. Aplicar Google Dorks básicos
5. Documentar hallazgos en el template de reporte

---

## Prerrequisitos

- [ ] Docker y Docker Compose instalados (`docker --version`)
- [ ] theHarvester instalado (`theharvester --version`)
- [ ] Conexión a internet activa
- [ ] Cuenta gratuita en Shodan (opcional pero recomendada)

```bash
# Verificar prerrequisitos
docker --version && docker compose version
theharvester --version
dig --version
```

---

## Objetivo de práctica autorizado

Este lab usa **`testphp.vulnweb.com`** — un sitio de práctica oficial de Acunetix diseñado específicamente para ser objetivo de herramientas de seguridad. Es 100% legal practicar contra él.

Otros objetivos de práctica autorizados:
- `hackthissite.org` — plataforma de retos legal
- `scanme.nmap.org` — servidor oficial de Nmap para práctica
- Tus propios dominios/VMs

> ⚠️ **NUNCA** uses estas técnicas contra sitios reales sin autorización escrita.

---

## Entorno Docker (opcional — para práctica offline)

Si prefieres un objetivo 100% local sin depender de internet:

```bash
# Levantar el entorno local de práctica
cd laboratorio/
docker compose up -d

# Verificar que está corriendo
docker compose ps

# El objetivo estará disponible en:
# http://localhost:8080  → aplicación web vulnerable
# localhost:8080         → objetivo para theHarvester local
```

---

## Ejecución del lab paso a paso

### Paso 1 — Reconocimiento DNS básico (5 min)

```bash
# WHOIS del dominio
whois vulnweb.com

# Registros DNS
dig vulnweb.com ANY
dig +short A testphp.vulnweb.com
dig +short MX vulnweb.com
dig +short NS vulnweb.com
dig +short TXT vulnweb.com

# Registro SPF (anti-spoofing de email)
dig +short TXT vulnweb.com | grep spf
```

**Anota:** ¿Qué servidores DNS usa? ¿Tiene registros SPF/DMARC configurados?

---

### Paso 2 — Subdominios via certificados TLS (5 min)

```bash
# Buscar subdominios en crt.sh (sin tocar el servidor objetivo)
curl -s "https://crt.sh/?q=%.vulnweb.com&output=json" \
  | python3 -m json.tool \
  | grep 'name_value' \
  | sort -u

# Versión más limpia
curl -s "https://crt.sh/?q=%.vulnweb.com&output=json" \
  | python3 -c "import sys,json; data=json.load(sys.stdin); [print(x['name_value']) for x in data]" \
  | sort -u
```

**Anota:** ¿Cuántos subdominios encontraste? ¿Alguno parece un entorno de desarrollo?

---

### Paso 3 — theHarvester (10 min)

```bash
# Recon básico
theharvester -d vulnweb.com -b google,bing,crtsh -l 200

# Guardar resultados en HTML
theharvester -d vulnweb.com -b google,bing,crtsh,linkedin -l 300 -f recon-vulnweb

# Abrir reporte
open recon-vulnweb.html     # macOS
xdg-open recon-vulnweb.html  # Linux
```

**Anota:** ¿Emails encontrados? ¿Subdominios nuevos? ¿IPs asociadas?

---

### Paso 4 — Shodan manual (10 min)

Abre [https://www.shodan.io](https://www.shodan.io) y busca:

```
org:"Acunetix"
hostname:"vulnweb.com"
net:45.33.32.156
```

**Anota:** ¿Qué puertos están abiertos? ¿Qué versiones de software aparecen? ¿Hay algo inesperado?

---

### Paso 5 — Google Dorks básicos (10 min)

Ejecuta estas búsquedas en Google (reemplaza con tu dominio de práctica autorizado):

```
site:vulnweb.com
site:vulnweb.com filetype:php
site:vulnweb.com inurl:admin OR inurl:login
cache:testphp.vulnweb.com
```

**Anota:** ¿Cuántas páginas indexadas? ¿Archivos PHP visibles? ¿Panel de admin expuesto?

---

## Reto final (sin guía)

> Aplica todo lo anterior a **scanme.nmap.org** (objetivo oficial de Nmap, práctica autorizada).

Responde estas preguntas documentando tus comandos y capturas:

1. ¿Cuál es el rango de IPs del ASN de scanme.nmap.org?
2. ¿Qué certificados TLS tiene emitidos? ¿Qué subdominios revela `crt.sh`?
3. ¿Qué información aparece en Shodan sobre esta IP?
4. ¿Qué registros DNS tiene configurados?
5. ¿Qué tecnologías web usa el sitio (Wappalyzer/BuiltWith)?

Documenta todo en el **template de reporte** → `../portafolio/TEMPLATE-reporte-osint.md`

---

## Limpiar el entorno Docker

```bash
# Detener y eliminar contenedores
docker compose down

# Eliminar también volúmenes
docker compose down -v
```

---

**[← Herramientas](../herramientas/theharvester.md)** · **[→ Template de reporte](../portafolio/TEMPLATE-reporte-osint.md)**
