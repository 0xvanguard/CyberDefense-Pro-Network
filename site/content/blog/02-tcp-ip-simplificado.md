---
title: "TCP/IP explicado como si tuvieras 5 años"
description: "Los fundamentos de redes que toda carrera en ciberseguridad requiere"
author: Equipo CDPN
date: 2026-06-08
tags: [redes, tcp-ip, fundamentos, networking]
readingTime: 4 min
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

# TCP/IP explicado como si tuvieras 5 años

<div class="article-meta">
  <span class="accent">📝 Equipo CDPN</span>
  <span>📅 8 Junio 2026</span>
  <span>📖 4 min de lectura</span>
  <span>🏷️ Redes</span>
  <span>🏷️ Fundamentos</span>
</div>

## La analogía del correo postal

Imagina que quieres enviar una carta a tu amigo:

```
1. ESCRIBES la carta → TCP divide en "paquetes"
2. PONES la dirección → IP identifica destino
3. EL CAMIONERO la lleva → Router la dirige
4. TU AMIGO la recibe → TCP reensambla
5. TE CONFIRMA llegada → ACK
```

## Las 4 capas (simplificado)

```
┌─────────────────────────────────┐
│  4. APLICACIÓN                  │
│  HTTP, FTP, SSH, DNS            │
│  "Qué hago con los datos"       │
├─────────────────────────────────┤
│  3. TRANSPORTE                  │
│  TCP (confiable) / UDP (rápido) │
│  "Cómo se envían"               │
├─────────────────────────────────┤
│  2. INTERNET                    │
│  IP, ICMP                       │
│  "A dónde van"                  │
├─────────────────────────────────┤
│  1. ACCESO                      │
│  Ethernet, WiFi                 │
│  "Por dónde viajan"             │
└─────────────────────────────────┘
```

## TCP vs UDP

| Característica | TCP | UDP |
|----------------|-----|-----|
| Confiabilidad | ✅ Garantiza entrega | ❌ No garantiza |
| Velocidad | 🐢 Más lento | 🚀 Más rápido |
| Ejemplos | Web, email, SSH | Streaming, gaming, DNS |
| Handshake | 3 pasos (SYN, SYN-ACK, ACK) | Sin handshake |

## Puerto comunes

| Puerto | Servicio | Para qué sirve |
|--------|----------|----------------|
| 22 | SSH | Acceso remoto seguro |
| 80 | HTTP | Páginas web |
| 443 | HTTPS | Páginas web seguras |
| 53 | DNS | Resolver nombres |
| 21 | FTP | Transferir archivos |
| 3306 | MySQL | Base de datos |

## Prueba tú mismo

```bash
# Ver tu IP
ip addr show

# Probar conexión
ping 8.8.8.8

# Ver puertos abiertos
netstat -tlnp
```

---

*Artículo publicado en el Blog CDPN — Semana 2*
