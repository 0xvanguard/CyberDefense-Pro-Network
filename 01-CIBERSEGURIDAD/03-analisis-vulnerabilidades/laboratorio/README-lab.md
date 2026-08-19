# 🧪 Lab 03 — Vulnerability Assessment con enfoque Red / Blue / Purple

> **Objetivo:** Descubrir, priorizar, validar y reportar hallazgos reales dentro de un entorno controlado, separando claramente la óptica de Red Team, Blue Team y Purple Team.

---

## Arquitectura del lab

```text
Red 172.31.0.0/24

172.31.0.10  → app-web-vuln      (DVWA)
172.31.0.20  → webgoat           (training OWASP)
172.31.0.30  → juice-shop        (app moderna vulnerable)
```

---

## Prerrequisitos

- [ ] Docker + Docker Compose
- [ ] Nmap
- [ ] Nuclei
- [ ] searchsploit
- [ ] Navegador web

---

## Levantar el entorno

```bash
cd laboratorio/
docker compose up -d
docker compose ps
```

Accesos:
- DVWA → `http://localhost:8082`
- WebGoat → `http://localhost:8083/WebGoat`
- Juice Shop → `http://localhost:3000`

---

## Parte A — Descubrimiento (Red Team)

```bash
# Descubrir servicios
nmap -sV -sC 172.31.0.0/24 -oA discovery-module3

# Escanear apps con nuclei
nuclei -u http://localhost:8082 -tags exposure,tech,cves -severity low,medium,high,critical -o dvwa-nuclei.txt
nuclei -u http://localhost:8083 -tags exposure,tech,cves -severity low,medium,high,critical -o webgoat-nuclei.txt
nuclei -u http://localhost:3000 -tags exposure,tech,cves -severity low,medium,high,critical -o juice-nuclei.txt
```

**Entregable Red Team:** lista de hallazgos preliminares con evidencia.

---

## Parte B — Priorización (Blue Team)

Construye una tabla con estas columnas:

| Activo | Hallazgo | Severidad | C | I | A | Exposición | Prioridad |
|---|---|---|---|---|---|---|---|

Criterio sugerido:
- Expuesto públicamente + afecta C/I/A en alto = prioridad inmediata.
- Informativo + sin exploitabilidad clara = backlog.

---

## Parte C — Validación (Red + Purple)

Toma 2 hallazgos y valídalos manualmente.

Ejemplos:
- versión expuesta en headers,
- directory listing,
- credenciales por defecto,
- panel o endpoint expuesto,
- ausencia de headers de seguridad.

```bash
# Ejemplo: headers manuales
curl -I http://localhost:8082
curl -I http://localhost:3000

# Buscar exploit público relacionado si aplica
searchsploit nginx
searchsploit apache
```

**Entregable Purple Team:** indicar si el hallazgo era real, falso positivo o riesgo inflado; luego proponer cómo re-testear tras corregir.

---

## Parte D — Reporte final

Usa el template del módulo y documenta al menos:
- 5 hallazgos totales,
- 2 validados manualmente,
- impacto CIA por hallazgo,
- observaciones separadas por Red / Blue / Purple,
- plan de remediación por severidad.

---

## Reto elite

1. Elige el activo con mayor riesgo.
2. Justifica por qué es el más peligroso sin depender solo del CVSS.
3. Explica cómo lo vería Red, cómo lo priorizaría Blue y cómo lo cerraría Purple.
4. Define un criterio de re-test para confirmar que la remediación funcionó.

---

## Limpiar el entorno

```bash
docker compose down
docker compose down -v  # Elimina también los volúmenes
```

---

**[← searchsploit](../herramientas/searchsploit.md)** · **[→ Template de reporte](../portafolio/TEMPLATE-reporte-vulnerabilidades.md)**
