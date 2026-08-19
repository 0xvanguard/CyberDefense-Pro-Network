# Plantilla de Informe de Reconocimiento Inicial

> **Uso:** copia este archivo, renómbralo (por ejemplo `informe-recon-novapay-labs.md`) y complétalo con tus hallazgos para cada lab.

---

## 1. Datos generales

- **Nombre del lab:** `Lab 01 — Mapeo de superficie básico`  
- **Estudiante:** `Tu nombre o alias`  
- **Fecha:** `AAAA-MM-DD`  
- **Entorno:** `Máquina local / VM / Docker / VPN HTB/THM (según aplique)`  

---

## 2. Scope y limitaciones

### 2.1 Alcance autorizado

- **Dominios incluidos:**  
  - `ejemplo: novapay-labs.local`  
- **Rangos de red incluidos:**  
  - `ejemplo: 10.20.30.0/24`  
- **Otros elementos incluidos (si aplica):**  
  - `ejemplo: subdominios internos simulados, etc.`  

### 2.2 Fuera de alcance

- `ejemplo: cualquier IP fuera de 10.20.30.0/24`  
- `ejemplo: fuerza bruta de credenciales`  
- `ejemplo: ejecución de exploits o DoS`  

> **Nota:** trabajar fuera del scope es un fallo crítico en un pentest profesional.

---

## 3. Metodología de reconocimiento

Describe brevemente **cómo** abordaste el reconocimiento, siguiendo las fases del módulo.

### 3.1 Resumen de fases

- **Fase 1 – Definición de scope y contexto:**  
  `¿Qué entendiste del negocio simulado y del alcance?`  

- **Fase 2 – Reconocimiento pasivo:**  
  `¿Qué consultas OSINT pasivas hiciste? (WHOIS, DNS, etc.)`  

- **Fase 3 – Descubrimiento de hosts:**  
  `¿Cómo identificaste qué IPs estaban activas?`  

- **Fase 4 – Enumeración de puertos y servicios:**  
  `¿Qué tipo de escaneos hiciste y con qué criterios?`  

- **Fase 5 – Organización de hallazgos:**  
  `¿Cómo estructuraste la información que encontraste?`  

### 3.2 Herramientas utilizadas

Lista las herramientas principales que usaste y para qué:

- `whois` → `consulta de registro de dominio`  
- `dig` → `consultas DNS (A, MX, NS, TXT...)`  
- `nmap` → `host discovery y escaneo de puertos`  
- `otras...` → `describe brevemente el uso`  

---

## 4. Hallazgos técnicos

### 4.1 Tabla de hosts y servicios

Rellena esta tabla con los resultados de tu reconocimiento técnico.

| Host/IP | Nombre/Hostname | Puertos abiertos | Servicios aparentes | Notas |
|--------|------------------|------------------|---------------------|-------|
| `10.20.30.10` | `web-frontend` (si lo sabes) | `80, 443` | `HTTP, HTTPS` | `Sitio público, posible portal de marketing` |
| `10.20.30.20` | `merchant-panel` | `443, 8443` | `HTTPS, posible panel admin` | `Portal para merchants, login expuesto` |
| ... | ... | ... | ... | ... |

Puedes añadir tablas adicionales si lo necesitas (por ejemplo, una por host).

### 4.2 Detalles por host (opcional pero recomendado)

#### Host: `10.20.30.10`

- **Puertos/servicios relevantes:**  
  - `80/tcp – HTTP (Apache 2.4.x)`  
  - `443/tcp – HTTPS (nginx 1.18.x)`  
- **Observaciones:**  
  - `Página de marketing de NovaPay Labs.`  
  - `Links a documentación pública.`  

#### Host: `10.20.30.20`

- **Puertos/servicios relevantes:**  
  - `443/tcp – HTTPS`  
  - `8443/tcp – HTTPS alternativo`  
- **Observaciones:**  
  - `Panel de merchants con formulario de login.`  
  - `Banner indica versión del framework.`  

*(Añade tantas subsecciones como hosts relevantes hayas identificado.)*

---

## 5. Observaciones y primeras hipótesis

Aquí no explotas nada; solo **piensas como atacante** y dejas anotadas ideas para futuras fases.

### 5.1 Observaciones generales

- `ejemplo: El rango parece tener pocos hosts expuestos, lo que sugiere segmentación decente.`  
- `ejemplo: Hay varios servicios HTTPS, pero no se revisó aún la configuración de TLS.`  

### 5.2 Posibles vectores a investigar en siguientes módulos

- `ejemplo: Panel de merchants en 8443 con banner de versión específico → candidato a revisión de vulnerabilidades web.`  
- `ejemplo: Servicios no estándar expuestos en puertos altos → revisar qué aplicaciones son.`  

> Estas hipótesis se retomarán en módulos como Pentesting / Red Team y Análisis de Vulnerabilidades.

---

## 6. Resumen ejecutivo

Redacta aquí un resumen de 3–6 líneas dirigido a alguien no técnico (por ejemplo, un gerente de seguridad o CTO):

- ¿Qué encontraste a nivel de superficie de ataque?  
- ¿Qué te llamó más la atención?  
- ¿Qué recomendarías como siguiente paso de alto nivel?  

**Ejemplo de estructura (no lo copies literal, adáptalo a tu caso):**

> Durante el reconocimiento inicial de `NovaPay Labs` se identificaron X hosts activos dentro del rango autorizado, con servicios web y de administración expuestos. La superficie de ataque observada es coherente con una startup fintech en fase de pruebas, aunque destaca la presencia de [servicio/puerto inusual] que podría requerir revisión más detallada. Como siguientes pasos, se recomienda priorizar un análisis de vulnerabilidades de los paneles web y una revisión específica de la exposición de servicios internos.

---

## 7. Notas y comandos utilizados (para tu propio uso)

Puedes usar esta sección como bitácora técnica personal:

```bash
# Ejemplos (sustituye por los tuyos)
whois novapay-labs.local

dig novapay-labs.local ANY

nmap -sn 10.20.30.0/24

nmap -sV -p 80,443,8443 10.20.30.10
```

No es obligatorio entregar esta parte, pero te ayudará a repetir y mejorar tu metodología en futuros labs.
