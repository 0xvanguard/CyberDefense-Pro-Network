# 🛠️ theHarvester — Guía de uso

> **theHarvester** es la herramienta OSINT más usada para recopilar emails, subdominios, IPs y empleados de fuentes públicas. Es el punto de partida estándar en cualquier pentest profesional.

[![GitHub](https://img.shields.io/badge/GitHub-theHarvester-black?style=flat-square&logo=github)](https://github.com/laramies/theHarvester)
[![Kali](https://img.shields.io/badge/Incluida%20en-Kali%20Linux-blue?style=flat-square)]()

---

## Instalación

```bash
# En Kali Linux (ya viene instalada)
theharvester --version

# En cualquier sistema con Python 3.9+
git clone https://github.com/laramies/theHarvester.git
cd theHarvester
pip3 install -r requirements/base.txt
python3 theHarvester.py --help

# Con pipx (recomendado para aislar dependencias)
pipx install theHarvester
```

---

## Sintaxis básica

```bash
theharvester -d <dominio> -b <fuentes> [opciones]
```

| Parámetro | Descripción | Ejemplo |
|---|---|---|
| `-d` | Dominio objetivo | `-d empresa.com` |
| `-b` | Fuentes de búsqueda | `-b google,bing,crtsh` |
| `-l` | Límite de resultados | `-l 500` |
| `-f` | Guardar resultados (HTML + XML) | `-f reporte-empresa` |
| `-s` | Usar Shodan para IPs encontradas | `-s` |
| `-v` | Verificar hostname via DNS | `-v` |
| `-n` | Búsqueda DNS reversa | `-n` |

---

## Fuentes disponibles (las más útiles)

```bash
# Ver todas las fuentes disponibles
theharvester -b all --help
```

| Fuente | Qué recopila | ¿Requiere API key? |
|---|---|---|
| `google` | Emails, subdominios, URLs | No |
| `bing` | Emails, subdominios | No |
| `crtsh` | Subdominios via certificados TLS | No |
| `linkedin` | Empleados y nombres | No |
| `github-code` | Emails en código público | No |
| `shodan` | Hosts, IPs, puertos | Sí (gratuita) |
| `hunter` | Emails corporativos | Sí (gratuita) |
| `securitytrails` | DNS histórico, subdominios | Sí (gratuita) |
| `virustotal` | Subdominios, URLs | Sí (gratuita) |

---

## Comandos de práctica por escenario

### Reconocimiento inicial básico (sin API keys)
```bash
theharvester -d empresa.com -b google,bing,crtsh,linkedin -l 300 -f recon-inicial
```

### Máxima cobertura pasiva
```bash
theharvester -d empresa.com -b google,bing,crtsh,linkedin,github-code,yahoo -l 500 -f recon-completo -v
```

### Solo subdominios (rápido)
```bash
theharvester -d empresa.com -b crtsh,bing -l 200
```

### Con validación DNS y Shodan (requiere API key de Shodan)
```bash
theharvester -d empresa.com -b google,crtsh,shodan -l 400 -s -v -f recon-shodan
```

### Guardar en múltiples formatos y revisar
```bash
theharvester -d empresa.com -b google,bing,crtsh -l 300 -f resultado
# Genera: resultado.html y resultado.xml
open resultado.html   # macOS
xdg-open resultado.html  # Linux
```

---

## Interpretación de resultados

### Emails encontrados
```
[*] Emails found: 12
--------------------------------------------------
john.smith@empresa.com
hsmith@empresa.com
info@empresa.com
support@empresa.com
```
**Qué observar:**
- El patrón de emails (`nombre.apellido@` vs `iniciales@`) → útil para adivinar emails no publicados
- Emails de empleados con acceso publicado en distintas fuentes
- Emails de dominio alternativo (empresa-corp.com, empresa-dev.com)

### Hosts/subdominios
```
[*] Hosts found: 34
--------------------------------------------------
mail.empresa.com:203.0.113.1
dev.empresa.com:203.0.113.5
staging.empresa.com:203.0.113.8
vpn.empresa.com:203.0.113.12
```
**Qué observar:**
- `dev.`, `staging.`, `test.` → entornos de desarrollo potencialmente menos protegidos
- `vpn.`, `remote.`, `citrix.` → vectores de acceso externo
- `mail.`, `webmail.` → potencial para password spray o phishing dirigido
- IPs distintas → pueden indicar terceros o infraestructura separada

---

## Automatización básica con Python

```python
import subprocess
import json
from datetime import datetime

def run_harvester(domain: str, sources: str = "google,bing,crtsh", limit: int = 300):
    """
    Ejecuta theHarvester y guarda resultados estructurados.
    Solo usar contra dominios propios o con autorización.
    """
    timestamp = datetime.now().strftime("%Y%m%d-%H%M%S")
    output_file = f"recon-{domain}-{timestamp}"
    
    cmd = [
        "theharvester",
        "-d", domain,
        "-b", sources,
        "-l", str(limit),
        "-f", output_file
    ]
    
    print(f"[*] Iniciando recon contra: {domain}")
    print(f"[*] Fuentes: {sources}")
    print(f"[*] Output: {output_file}.html")
    
    result = subprocess.run(cmd, capture_output=True, text=True)
    
    print(result.stdout)
    if result.returncode == 0:
        print(f"[+] Recon completado. Revisa {output_file}.html")
    else:
        print(f"[-] Error: {result.stderr}")
    
    return output_file

# Uso: solo contra dominios propios o con autorización escrita
if __name__ == "__main__":
    # Cambiar por tu propio dominio de prueba
    run_harvester("tudominio.com")
```

---

## API Keys recomendadas (todas gratuitas)

Configura las API keys en `~/.theHarvester/api-keys.yaml`:

```yaml
apikeys:
  shodan:
    key: TU_API_KEY_SHODAN  # shodan.io → cuenta gratuita
  hunter:
    key: TU_API_KEY_HUNTER  # hunter.io → 25 búsquedas/mes gratis
  securitytrails:
    key: TU_API_KEY_ST      # securitytrails.com → 50 queries/mes gratis
  virustotal:
    key: TU_API_KEY_VT      # virustotal.com → gratuita
```

---

## Errores comunes

| Error | Causa | Solución |
|---|---|---|
| `ModuleNotFoundError` | Dependencias faltantes | `pip3 install -r requirements/base.txt` |
| `No results for google` | Rate limit de Google | Usa `-b bing,crtsh` o espera 1h |
| `Shodan API error` | API key inválida o sin quota | Verifica key en shodan.io |
| `TimeoutError` | Red lenta o fuente caída | Reduce fuentes o usa `-l 100` |

---

**[← Teoría OSINT](../teoria/01-fundamentos-osint.md)** · **[→ Lab práctico](../laboratorio/README-lab.md)**
