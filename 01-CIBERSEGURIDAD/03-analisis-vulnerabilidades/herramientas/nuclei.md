# ⚡ Nuclei — Escaneo rápido con plantillas

> `Nuclei` permite detectar exposiciones y vulnerabilidades conocidas usando plantillas reproducibles y fáciles de automatizar.

---

## Instalación

```bash
# Go instalado
go install -v github.com/projectdiscovery/nuclei/v3/cmd/nuclei@latest

# Actualizar templates
nuclei -update-templates
```

---

## Uso básico

```bash
# Escanear una URL
nuclei -u http://localhost:8082

# Filtrar por severidad
nuclei -u http://localhost:8082 -severity low,medium,high,critical

# Filtrar por etiquetas
nuclei -u http://localhost:8082 -tags exposure,tech,cves

# Guardar resultados en JSONL
nuclei -u http://localhost:8082 -jsonl -o nuclei-results.jsonl
```

---

## Casos útiles en este módulo

```bash
# Exposiciones comunes
nuclei -u http://localhost:8082 -tags exposure

# Hallazgos CVE conocidos
nuclei -u http://localhost:8082 -tags cves

# Tecnologías detectadas
nuclei -u http://localhost:8082 -tags tech
```

---

## Cómo leer resultados

No todo resultado de Nuclei es igual. Para cada match revisa:
- URL afectada
- severidad sugerida
- evidencia del match
- si realmente es explotable
- qué parte de CIA puede afectar

---

## Buenas prácticas

- Confirmar hallazgos manualmente.
- No reportar matches sin contexto.
- Agrupar resultados repetidos por activo.
- Usar salida JSONL para análisis posterior.

---

**[← Red/Blue/Purple](../teoria/03-red-blue-purple-operando-juntos.md)** · **[→ OpenVAS/GVM](./openvas-gvm.md)**
