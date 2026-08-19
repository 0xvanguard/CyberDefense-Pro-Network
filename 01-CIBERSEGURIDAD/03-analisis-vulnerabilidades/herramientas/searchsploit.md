# 🔎 searchsploit — Contexto ofensivo controlado

> `searchsploit` conecta versiones detectadas con exploits públicos disponibles en Exploit-DB.

---

## Uso básico

```bash
searchsploit apache 2.4
searchsploit nginx
searchsploit openssh 7.2
searchsploit phpmyadmin
```

---

## Flujo recomendado

```bash
# 1. Identificar versión con Nmap
nmap -sV 172.31.0.10

# 2. Buscar exploits relacionados
searchsploit <servicio> <version>

# 3. Evaluar relevancia
# ¿Es misma rama? ¿Mismo sistema operativo? ¿Exploit remoto o local?
```

---

## Regla importante

La existencia de un exploit público **no significa** que el riesgo sea automáticamente crítico. Debes cruzarlo con:
- exposición,
- autenticación requerida,
- complejidad,
- impacto CIA,
- controles compensatorios.

---

**[← OpenVAS/GVM](./openvas-gvm.md)** · **[→ Lab](../laboratorio/README-lab.md)**
