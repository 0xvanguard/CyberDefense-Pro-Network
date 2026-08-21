---
title: "TCP/IP explicado como si tuvieras 5 años"
description: "Los fundamentos de redes que toda carrera en ciberseguridad requiere"
---

# TCP/IP explicado como si tuvieras 5 años

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
