---
title: "Docker para ciberseguridad: monta tu lab en minutos"
description: "Containers, DVWA, vulnerable apps y laboratorio completo con Docker Compose"
author: Equipo CDPN
date: 2026-08-10
tags: [docker, labs, containers, practica]
readingTime: 5 min
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

# Docker para ciberseguridad: monta tu lab en minutos

<div class="article-meta">
  <span class="accent">📝 Equipo CDPN</span>
  <span>📅 10 Agosto 2026</span>
  <span>📖 5 min de lectura</span>
  <span>🏷️ Docker</span>
  <span>🏷️ Labs</span>
</div>

## ¿Por qué Docker?

Docker te permite crear **entornos aislados** (containers) con aplicaciones vulnerables sin afectar tu sistema. Es la forma más rápida de montar un laboratorio de ciberseguridad.

### Ventajas

- ⚡ **Rápido** — Un container se levanta en segundos
- 🔄 **Reproducible** — "Funciona en mi máquina" ya no es excusa
- 🧹 **Limpio** — Destruyes y creas containers infinitas veces
- 📦 **Portable** — Funciona en Linux, Mac, Windows, cloud

## Instalación

```bash
# Linux (Ubuntu/Debian)
sudo apt update
sudo apt install docker.io docker-compose-plugin
sudo usermod -aG docker $USER
# Cerrar y abrir terminal de nuevo

# Verificar instalación
docker --version
docker compose version
```

## Lab 1: DVWA (Damn Vulnerable Web App)

DVWA es una aplicación web vulnerable perfecta para practicar.

```bash
# Crear directorio del lab
mkdir -p ~/labs/dvwa && cd ~/labs/dvwa

# Crear docker-compose.yml
cat > docker-compose.yml << 'EOF'
services:
  dvwa:
    image: vulnerables/web-dvwa
    ports:
      - "80:80"
    environment:
      - MYSQL_PASS=dvwa
    restart: unless-stopped
EOF

# Levantar
docker compose up -d

# Acceder a http://localhost/dvwa
# Login: admin / password
```

## Lab 2: vulnerable-apps completo

```bash
# Crear lab completo con múltiples apps vulnerables
mkdir -p ~/labs/vulnlab && cd ~/labs/vulnlab

cat > docker-compose.yml << 'EOF'
services:
  # Web vulnerable
  dvwa:
    image: vulnerables/web-dvwa
    ports:
      - "8080:80"
    restart: unless-stopped

  # SQL injection
  webgoat:
    image: webgoat/webgoat
    ports:
      - "8081:8080"
    restart: unless-stopped

  # Juice Shop (OWASP)
  juiceshop:
    image: bkimminich/juice-shop
    ports:
      - "8082:3000"
    restart: unless-stopped

  # Metasploitable (máquina vulnerable completa)
  metasploitable:
    image: tianon/metasploitable
    ports:
      - "8083:80"
      - "2121:21"
      - "4444:4444"
    restart: unless-stopped
EOF

docker compose up -d
```

## Lab 3: vulnerable Linux CLI

```bash
# Container Kali para atacar
docker run -it --name kali \
  --network host \
  kalilinux/kali-rolling /bin/bash

# Dentro de Kali:
apt update && apt install -y nmap nikto sqlmap
```

## Comandos esenciales de Docker

```bash
# Container lifecycle
docker ps                    # Containers corriendo
docker ps -a                 # Todos los containers
docker stop <id>             # Parar container
docker rm <id>               # Eliminar container
docker logs <id>             # Ver logs

# Networking
docker network ls            # Redes disponibles
docker network inspect bridge

# Utility
docker exec -it <id> bash    # Shell dentro del container
docker-compose up -d         # Levantar todo
docker-compose down          # Parar todo
docker-compose logs -f       # Ver logs en tiempo real
```

## Topología de lab sugerida

```
┌──────────────────────────────────────────────────┐
│              TU LABORATORIO DOCKER               │
├──────────────────────────────────────────────────┤
│                                                  │
│  ┌──────────────┐  ┌──────────────┐             │
│  │   Kali       │  │  Metasploit  │             │
│  │  (atacante)  │──│  (framework) │             │
│  └──────┬───────┘  └──────────────┘             │
│         │                                        │
│  ┌──────┴───────────────────────────────┐       │
│  │          RED VULNERABLE              │       │
│  ├─────────┬──────────┬────────┬────────┤       │
│  │  DVWA   │ WebGoat  │ Juice  │ Meta-  │       │
│  │  :8080  │  :8081   │ Shop   │ splash │       │
│  │         │          │ :8082  │ :8083  │       │
│  └─────────┴──────────┴────────┴────────┘       │
│                                                  │
└──────────────────────────────────────────────────┘
```

## Tips de seguridad

```bash
# SIEMPRE usa redes aisladas
docker network create vulnlab
docker run --network vulnlab ...

# NO expongas puertos sensibles a 0.0.0.0
# MAL:   ports: "4444:4444"
# BIEN:  ports: "127.0.0.1:4444:4444"

# Usa --rm para containers temporales
docker run --rm -it kalilinux/kali-rolling

# Limpia después de usar
docker system prune -a  # Eliminar todo lo no usado
```

## Conclusión

Docker te da un **laboratorio completo en minutos**, sin arruinar tu sistema operativo. Con €0 y 5 comandos puedes tener DVWA, WebGoat, Juice Shop y Metasploitable corriendo.

---

*Artículo publicado en el Blog CDPN — Semana 11*
