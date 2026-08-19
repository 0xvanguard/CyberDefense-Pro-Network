# Reporte de Reconocimiento OSINT

> **⚠️ Plantilla para uso educativo.**  
> Anonimiza o reemplaza todos los datos reales antes de publicar.
> Solo documenta objetivos propios o con autorización escrita.

---

## Portada

| Campo | Valor |
|---|---|
| **Objetivo** | [Dominio o nombre de empresa — anonimizar si es real] |
| **Analista** | Tu nombre / alias |
| **Fecha** | YYYY-MM-DD |
| **Alcance autorizado** | [Descripción del alcance — ej: "Dominio propio de práctica"] |
| **Clasificación** | Público / Confidencial / Solo para portafolio |
| **Herramientas usadas** | theHarvester · crt.sh · Shodan · Google Dorks · dig |

---

## Resumen Ejecutivo

> *(Máximo 150 palabras — para que lo entienda alguien no técnico)*

Se realizó un proceso de reconocimiento OSINT pasivo sobre [OBJETIVO] durante [FECHAS]. Se identificaron **[N] subdominios**, **[N] direcciones de correo electrónico** y **[N] servicios expuestos** usando únicamente fuentes públicas, sin interactuar directamente con los sistemas del objetivo.

Los hallazgos más relevantes son: [Ej: "Dos subdominios de staging accesibles públicamente" / "Patrón de emails corporativos identificado" / "Versión de servidor web expuesta en headers"].

Nivel de riesgo estimado: **[Bajo / Medio / Alto]**

---

## Metodología

Este análisis siguió las 5 fases de reconocimiento OSINT:

1. **Planificación** — Definición de alcance y herramientas
2. **Recolección pasiva** — Sin interactuar con el objetivo
3. **Procesamiento** — Normalización y deduplicación de datos
4. **Análisis y correlación** — Identificación de patrones y vectores
5. **Documentación** — Este reporte

---

## Hallazgos

### 1. Información de dominio (DNS / WHOIS)

```
Dominio:      [dominio.com]
Registrador:  [Ej: GoDaddy, Namecheap]
Creado:       [Fecha]
Expira:       [Fecha]
NS primario:  [ns1.ejemplo.com]
MX registros: [mail.dominio.com → IP]
SPF:          [Sí / No configurado]
DMARC:        [Sí / No configurado]
```

**Observaciones:**  
[Ej: "Sin registro DMARC — susceptible a email spoofing" / "Dominio expira en 30 días"]

---

### 2. Subdominios descubiertos

| Subdominio | IP | Servicio detectado | Riesgo |
|---|---|---|---|
| `www.dominio.com` | x.x.x.x | HTTP/HTTPS (Nginx 1.18) | Bajo |
| `dev.dominio.com` | x.x.x.x | HTTP sin TLS | Medio |
| `staging.dominio.com` | x.x.x.x | Aplicación web accesible | Alto |
| `vpn.dominio.com` | x.x.x.x | OpenVPN | Medio |

**Total subdominios:** [N]  
**Fuentes:** crt.sh · theHarvester · Shodan

---

### 3. Emails identificados

| Email | Fuente | Observación |
|---|---|---|
| `nombre@dominio.com` | LinkedIn + Google | Empleado activo — cargo: [X] |
| `info@dominio.com` | Sitio web | Email genérico de contacto |

**Patrón detectado:** `[nombre].[apellido]@dominio.com`  
**Uso potencial:** Generación de lista de usuarios para validación (solo en pentest autorizado)

---

### 4. Infraestructura expuesta (Shodan)

| IP | Puerto | Servicio | Versión | Riesgo |
|---|---|---|---|---|
| x.x.x.x | 22 | SSH | OpenSSH 7.4 (desactualizado) | Medio |
| x.x.x.x | 443 | HTTPS | Apache 2.4.49 (vulnerable) | Alto |
| x.x.x.x | 3389 | RDP | Expuesto a internet | Alto |

---

### 5. Información filtrada

> *(Credenciales, configs, código fuente encontrado accidentalmente)*

| Fuente | Descripción | Riesgo |
|---|---|---|
| GitHub | Archivo `.env` con variable DB_PASSWORD en repo público | Crítico |
| Pastebin | Ningún hallazgo | — |

---

## Análisis de superficie de ataque

```
Vectores identificados (ordenados por criticidad):

🔴 CRÍTICO
  └── [Ej: Credenciales expuestas en GitHub]

🟠 ALTO  
  ├── [Ej: Entorno staging accesible públicamente sin autenticación]
  └── [Ej: RDP expuesto a internet]

🟡 MEDIO
  ├── [Ej: Versiones de software desactualizadas visibles en headers]
  └── [Ej: Sin DMARC — posible vector de phishing]

🟢 BAJO
  └── [Ej: Empleados identificables en LinkedIn]
```

---

## Recomendaciones

| # | Hallazgo | Recomendación | Prioridad |
|---|---|---|---|
| 1 | Credenciales en GitHub | Revocar inmediatamente + rotar secretos + configurar GitLeaks en CI | Inmediata |
| 2 | Staging público | Proteger con autenticación básica o restricción por IP | Alta |
| 3 | Sin DMARC | Configurar registro DMARC con política `reject` | Media |
| 4 | Versiones expuestas | Configurar headers para ocultar versiones de servidor | Baja |

---

## Herramientas y comandos utilizados

```bash
# Recopilar los comandos exactos que usaste aquí
whois dominio.com
dig dominio.com ANY
curl -s "https://crt.sh/?q=%.dominio.com&output=json" | ...
theharvester -d dominio.com -b google,bing,crtsh -l 300 -f reporte
```

---

## Notas para tu portafolio

Antes de publicar este reporte:
- [ ] Reemplaza todas las IPs reales con `x.x.x.x` o rangos ficticios
- [ ] Usa un dominio genérico (`empresa-ejemplo.com`) si no es tu propio dominio
- [ ] Elimina cualquier dato personal real de terceros
- [ ] Añade una nota de "uso educativo y autorizado" al inicio
- [ ] El reporte en sí ya demuestra metodología profesional — es lo que importa para el portafolio

**Formato para publicar en LinkedIn:**  
"Completé el Módulo 01 de reconocimiento OSINT — aquí está mi reporte de práctica documentando metodología, herramientas y hallazgos en un entorno autorizado. #CyberSecurity #OSINT #OpenToWork"

---

*Reporte generado siguiendo la metodología del [Módulo 01 — Reconocimiento OSINT](../README.md) de la Plataforma de Estudio de Ciberseguridad y Seguridad de la Información.*
