---
title: "Nmap: la guía definitiva para principiantes"
description: "20 comandos esenciales de Nmap con casos de uso reales"
author: Equipo CDPN
date: 2026-06-15
tags: [herramientas, nmap, red-team, enumeracion]
readingTime: 6 min
---

<script setup>
import { useData } from 'vitepress'
const { frontmatter } = useData()
</script>

<style>
.article-meta { display:flex; gap:0.8rem; flex-wrap:wrap; margin:0.8rem 0 1.5rem; font-size:0.85rem; color:var(--vp-c-text-3); }
.article-meta span { background:var(--vp-c-default-soft); padding:2px 10px; border-radius:6px; }
.article-meta .accent { background:var(--vp-c-brand-soft); color:var(--vp-c-brand-1); }
</style>

# Nmap: la guía definitiva para principiantes

<div class="article-meta">
  <span class="accent">📝 Equipo CDPN</span>
  <span>📅 15 Junio 2026</span>
  <span>📖 6 min de lectura</span>
  <span>🏷️ Herramientas</span>
  <span>🏷️ Red Team</span>
</div>

## ¿Qué es Nmap?

**Nmap** (Network Mapper) es la herramienta estándar para descubrir hosts, puertos y servicios en una red. Es gratis, open source y la usan tanto pentesters como sysadmins.

## 20 comandos que debes conocer

### Descubrimiento básico
```bash
nmap 192.168.1.1          # Escaneo básico
nmap -sn 192.168.1.0/24   # Descubrir hosts (sin escanear puertos)
nmap -Pn 192.168.1.1      # Escanear sin ping
```

### Escaneo de puertos
```bash
nmap -sV 192.168.1.1      # Detectar versiones de servicios
nmap -sC 192.168.1.1      # Scripts por defecto
nmap -p 22,80,443 target  # Escanear puertos específicos
nmap -p- target           # Todos los 65,535 puertos
```

### Escaneos avanzados
```bash
nmap -A target            # Agresivo (OS, versiones, scripts)
nmap -O target            # Detectar sistema operativo
nmap -sU target           # Escaneo UDP
nmap -T4 target           # Velocidad agresiva
```

### Output
```bash
nmap -oN scan.txt target  # Guardar en formato normal
nmap -oX scan.xml target  # Guardar en XML
nmap -oG scan.txt target  # Guardar en formato greppable
```

### Scripts NSE
```bash
nmap --script vuln target         # Escaneo de vulnerabilidades
nmap --script http-enum target    # Enumeración HTTP
nmap --script smb-enum* target    # Enumeración SMB
nmap --script ftp-anon target     # Verificar FTP anónimo
```

## Casos de uso reales

| Caso | Comando |
|------|---------|
| Descubrir hosts en tu red | `nmap -sn 192.168.1.0/24` |
| Ver qué corre en un server | `nmap -sV -sC 10.0.0.1` |
| Buscar vulnerabilidades | `nmap --script vuln 10.0.0.1` |
| Auditar FTP anónimo | `nmap --script ftp-anon -p 21 10.0.0.1` |

## Tips de profesionales

1. **Empieza lento** — No uses -T5 en producción
2. **Documenta todo** — Usa -oN para guardar resultados
3. **Sé ético** — Solo escanea sistemas que tengas permiso
4. **Combina con otras herramientas** — Nmap + Nikto + Burp

---

*Artículo publicado en el Blog CDPN — Semana 3*
