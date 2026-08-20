# 🔧 Herramientas de Reconocimiento OSINT

Directorio de herramientas para la fase de reconocimiento y enumeración en pentesting.

---

## 📋 Tabla de Contenidos

- [Herramientas Disponibles](#herramientas-disponibles)
- [Instalación](#instalación)
- [Uso Rápido](#uso-rápido)
- [Tutoriales](#tutoriales)
- [Ejercicios Prácticos](#ejercicios-prácticos)

---

## 🛠️ Herramientas Disponibles

### 1. 🔍 recon_automatizado.py

**Descripción:** Herramienta de reconocimiento OSINT automatizado para fase pasiva.

| Característica | Detalle |
|----------------|---------|
| **Lenguaje** | Python 3 |
| **Dependencias** | Ninguna (stdlib) |
| **Dificultad** | Principiante-Intermedio |
| **Funcionalidad** | DNS, subdominios, HTTP titles |
| **Velocidad** | ~50 subdominios/segundo |

```bash
# Uso básico
python3 recon_automatizado.py -d ejemplo.com

# Con wordlist
python3 recon_automatizado.py -d ejemplo.com -w subdominios.txt

# Con salida JSON
python3 recon_automatizado.py -d ejemplo.com -w subdominios.txt -o resultados.json
```

📖 [Código fuente](./recon_automatizado.py)

---

### 2. 📧 theharvester.md (Guía)

**Descripción:** Guía de uso de TheHarvester para recopilación de emails y subdominios.

| Característica | Detalle |
|----------------|---------|
| **Tipo** | Documentación/Guía |
| **Herramienta externa** | theHarvester |
| **Dificultad** | Principiante |
| **Funcionalidad** | Emails, subdominios, IPs |

```bash
# Instalación (Kali Linux)
sudo apt install theharvester

# Uso básico
theharvester -d ejemplo.com -b google,bing,linkedin
```

📖 [Guía completa](theharvester.md)

---

## 📦 Instalación

### Requisitos

```bash
# Python 3.8 o superior
python3 --version

# No requiere dependencias externas para recon_automatizado.py
```

### Instalación Rápida

```bash
# Clonar repositorio
git clone https://github.com/0xvanguard/CyberDefense-Pro-Network.git
cd CyberDefense-Pro-Network/01-CIBERSEGURIDAD/01-reconocimiento-osint/herramientas/

# Dar permisos de ejecución
chmod +x *.py
```

---

## 🚀 Uso Rápido

### Ejemplo 1: Escaneo Básico

```bash
# Solo resolver DNS del dominio
python3 recon_automatizado.py -d ejemplo.com
```

**Salida esperada:**
```
[+] ejemplo.com -> 93.184.216.34
```

### Ejemplo 2: Enumeración Completa

```bash
# Crear wordlist básica
cat > subdominios.txt << 'EOF'
www
mail
ftp
api
admin
test
dev
staging
portal
webmail
blog
shop
EOF

# Ejecutar reconocimiento
python3 recon_automatizado.py -d ejemplo.com -w subdominios.txt
```

**Salida esperada:**
```
[*] Enumerando subdominios con subdominios.txt ...
[+] 8 subdominios resueltos
    mail.ejemplo.com                           -> 93.184.216.35
    www.ejemplo.com                            -> 93.184.216.34
    api.ejemplo.com                            -> 93.184.216.36
```

### Ejemplo 3: Guardar Resultados

```bash
# Guardar informe completo en JSON
python3 recon_automatizado.py -d ejemplo.com -w subdominios.txt -o informe.json

# Ver resultado
cat informe.json | python3 -m json.tool
```

---

## 📚 Tutoriales

### Tutorial 1: Reconocimiento para Bug Bounty

**Objetivo:** Aprender a realizar reconocimiento inicial para un programa de bug bounty.

**Duración:** 30 minutos

**Pasos:**

1. **Identificar el objetivo:**
```bash
# Verificar que tienes permiso
# Ejemplo: buscar en https://bugcrowd.com o https://hackerone.com
```

2. **Crear wordlist personalizada:**
```bash
cat > wordlist_custom.txt << 'EOF'
www
mail
ftp
api
admin
test
dev
staging
portal
webmail
blog
shop
store
app
mobile
EOF
```

3. **Ejecutar reconocimiento:**
```bash
python3 recon_automatizado.py -d target.com -w wordlist_custom.txt -o recon.json
```

4. **Analizar resultados:**
```bash
# Buscar subdominios interesantes
cat recon.json | grep -E '"(admin|api|dev|staging)"'

# Ver títulos de páginas
cat recon.json | python3 -c "import sys,json; d=json.load(sys.stdin); [print(f'{k}: {v}') for k,v in d.get('titles',{}).items()]"
```

5. **Documentar hallazgos:**
```markdown
## Reconocimiento OSINT - target.com

### Subdominios Encontrados
- [ ] admin.target.com (verificar acceso)
- [ ] api.target.com (probar endpoints)
- [ ] dev.target.com (posible entorno de desarrollo)

### Siguientes Pasos
1. Escaneo de puertos
2. Análisis de servicios
3. Pruebas de seguridad
```

📖 [Tutorial completo](../../../docs/TUTORIAL-RECON-OSINT.md)

---

### Tutorial 2: Crear Wordlists Efectivas

**Objetivo:** Aprender a crear wordlists personalizadas para diferentes objetivos.

**Duración:** 20 minutos

**Pasos:**

1. **Wordlist básica:**
```bash
# Crear wordlist con subdominios comunes
cat > wordlist_basica.txt << 'EOF'
# Subdominios comunes
www
mail
ftp
api
admin
test
dev
staging
portal
webmail
blog
shop
store
app
mobile
cloud
vpn
remote
login
sso
auth
oauth
# Servicios
ns1
ns2
ns3
mx1
mx2
smtp
pop
imap
# Cloud
aws
azure
gcp
s3
cdn
static
media
# Redes sociales
facebook
twitter
instagram
linkedin
youtube
EOF
```

2. **Wordlist para empresas:**
```bash
# Basada en el nombre de la empresa
EMPRESA="mitre"
cat > wordlist_empresa.txt << EOF
www.${EMPRESA}.com
mail.${EMPRESA}.com
api.${EMPRESA}.com
dev.${EMPRESA}.com
test.${EMPRESA}.com
admin.${EMPRESA}.com
portal.${EMPRESA}.com
blog.${EMPRESA}.com
shop.${EMPRESA}.com
app.${EMPRESA}.com
EOF
```


---

## 🧪 Ejercicios Prácticos

### Ejercicio 1: Reconocimiento de Dominio Propio

**Objetivo:** Practicar reconocimiento en un dominio que controlas.

**Instrucciones:**

1. **Preparar entorno:**
```bash
# Crear directorio de trabajo
mkdir -p ~/labs/recon
cd ~/labs/recon
```

2. **Ejecutar reconocimiento:**
```bash
# Usar tu propio dominio o uno de práctica
python3 recon_automatizado.py -d tu-dominio.com -w wordlist.txt -o ejercicio1.json
```

3. **Analizar resultados:**
```bash
# Responder preguntas:
# 1. ¿Cuántos subdominios se encontraron?
# 2. ¿Cuáles tienen títulos interesantes?
# 3. ¿Hay algún subdominio que merezca más atención?
```

4. **Documentar hallazgos:**
```markdown
## Ejercicio 1: Reconocimiento de Dominio Propio

### Resultados
- Dominio: tu-dominio.com
- Subdominios encontrados: X
- Subdominios con títulos: X

### Análisis
[Tu análisis aquí]

### Siguientes Pasos
1. Escaneo de puertos en IPs encontradas
2. Análisis de servicios HTTP/HTTPS
3. Pruebas de seguridad en endpoints
```

---

### Ejercicio 2: Comparar Resultados con Otras Herramientas

**Objetivo:** Comparar resultados de recon_automatizado.py con TheHarvester.

**Instrucciones:**

1. **Ejecutar recon_automatizado.py:**
```bash
python3 recon_automatizado.py -d ejemplo.com -w wordlist.txt -o recon1.json
```

2. **Ejecutar TheHarvester:**
```bash
theharvester -d ejemplo.com -b google,bing,linkedin -f recon2.html
```

3. **Comparar resultados:**
```bash
# ¿Qué subdominios encontró cada herramienta?
# ¿Cuáles son exclusivos de cada una?
# ¿Cuáles son comunes?
```

4. **Crear informe comparativo:**
```markdown
## Comparativa de Herramientas

| Herramienta | Subdominios | Emails | IPs |
|-------------|-------------|--------|-----|
| recon_automatizado | X | - | X |
| TheHarvester | X | X | X |
| **Comunes** | X | - | X |

### Conclusiones
[Tu conclusión aquí]
```

---

## 📊 Parámetros de recon_automatizado.py

| Parámetro | Descripción | Requerido | Predeterminado | Ejemplo |
|-----------|-------------|-----------|----------------|---------|
| `-d, --domain` | Dominio objetivo | **Sí** | - | `-d ejemplo.com` |
| `-w, --wordlist` | Archivo wordlist | No | Ninguna | `-w subdominios.txt` |
| `-o, --output` | Archivo JSON salida | No | Ninguno | `-o resultados.json` |
| `-t, --timeout` | Timeout HTTP (seg) | No | 5 | `-t 10` |

---

## 📊 Salida Esperada

### Formato JSON

```json
{
  "dominio": "ejemplo.com",
  "timestamp": "2026-08-19T10:30:00.000000",
  "ip_principal": ["93.184.216.34"],
  "subdominios": {
    "mail.ejemplo.com": ["93.184.216.35"],
    "www.ejemplo.com": ["93.184.216.34"],
    "api.ejemplo.com": ["93.184.216.36"]
  },
  "titles": {
    "ejemplo.com": "Bienvenido a Ejemplo",
    "mail.ejemplo.com": "Webmail - Ejemplo"
  }
}
```

### Interpretación

| Campo | Descripción |
|-------|-------------|
| `dominio` | Dominio analizado |
| `timestamp` | Fecha/hora del escaneo |
| `ip_principal` | IPs del dominio principal |
| `subdominios` | Subdominios encontrados |
| `titles` | Títulos de páginas web |

---

## ⚠️ Consideraciones Éticas

> **🚨 IMPORTANTE:** Estas herramientas son solo para uso educativo.

### ✅ Usos Permitidos
- Sistemas propios de prueba
- Laboratorios Docker aislados
- Plataformas autorizadas (HTB, THM)
- Con autorización explícita por escrito

### ❌ Usos Prohibidos
- Sistemas ajenos sin permiso
- Actividades ilegales
- Causar daño o interrupciones

---

## 🔧 Solución de Problemas

### "Permission denied"
```bash
chmod +x *.py
# O ejecutar con python3
python3 recon_automatizado.py -d ejemplo.com
```

### "Wordlist not found"
```bash
# Verificar ruta
ls -la /ruta/a/tu/wordlist.txt

# Crear wordlist básica
echo -e "www\nmail\napi\nadmin" > subdominios.txt
```

### Timeout en conexiones
```bash
# Aumentar timeout
python3 recon_automatizado.py -d ejemplo.com -t 15
```

---

## 📚 Recursos Relacionados

### Documentación del Repositorio
- [Fundamentos OSINT](../teoria/01-fundamentos-osint.md)
- [Definir Scope](../tecnicas/01-definir-scope.md)
- [Templates de Reportes](../portafolio/)

### Herramientas Complementarias
- [Nmap](../../03-analisis-vulnerabilidades/herramientas/) - Escaneo de puertos
- [Shodan](https://shodan.io) - Búsqueda de dispositivos
- [Censys](https://censys.io) - Búsqueda de certificados

### Recursos Externos
- [MITRE ATT&CK - Reconnaissance](https://attack.mitre.org/techniques/T1596/)
- [OWASP Testing Guide](https://owasp.org/www-project-web-security-testing-guide/)
- [PTES - Intelligence Gathering](http://www.pentest-standard.org/index.php/Intelligence_Gathering)

---

## 📝 Changelog

### [1.0.0] - 2026-08-19
- ✅ recon_automatizado.py v1.0
- ✅ Documentación completa
- ✅ Tutoriales paso a paso
- ✅ Ejercicios prácticos

---

*Directorio mantenido por la comunidad • [Contribuir](../../../CONTRIBUTING.md)*
