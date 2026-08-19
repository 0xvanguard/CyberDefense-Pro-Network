# 🤝 Cómo Contribuir

> Esta plataforma crece con la comunidad. Cada contribución aprobada se convierte en una entrada de portafolio de código abierto para quien la crea.

---

## Tipos de contribuciones aceptadas

| Tipo | Ejemplo | Carpeta destino |
|---|---|---|
| 📝 Módulo nuevo | Guía de Wireshark para Blue Team | `02-SEGURIDAD-INFORMACION/` |
| 🧪 Lab Docker | Entorno DVWA reproducible | `04-LABORATORIOS/docker-labs/` |
| 📄 Writeup | CTF Hack The Box documentado | `04-LABORATORIOS/ctf-writeups/` |
| 📋 Cheatsheet | Comandos frecuentes de Nmap | `05-RECURSOS/cheatsheets/` |
| 🛠️ Script | Script de hardening para Ubuntu | Módulo relacionado |
| 📚 Recurso | Libro o curso recomendado validado | `05-RECURSOS/` |

---

## Proceso de contribución

```bash
# 1. Fork del repositorio
git clone https://github.com/TU-USUARIO/University-Cybersecurity-Free.git

# 2. Crea una rama descriptiva
git checkout -b feat/nuevo-modulo-wireshark

# 3. Trabaja en tu contribución
# (usa TEMPLATE-MODULO.md como base para nuevos módulos)

# 4. Commit con mensaje claro
git commit -m "feat: módulo Wireshark para análisis de tráfico - Blue Team"

# 5. Push y Pull Request
git push origin feat/nuevo-modulo-wireshark
```

Abre el Pull Request contra `main` con una descripción que incluya:
- Qué aporta el contenido
- A qué ruta/módulo pertenece
- Nivel (básico/intermedio/avanzado)
- Proyecto de portafolio que genera

---

## Estándares de calidad

Todo el contenido debe cumplir:

- ✅ **Ético y legal** — sin exploits para sistemas sin autorización, sin datos reales de víctimas.
- ✅ **En español** — salvo nombres técnicos propios (SIEM, OSINT, payload, etc.).
- ✅ **Reproducible** — los labs Docker deben funcionar con `docker compose up`.
- ✅ **Documentado** — README en la carpeta con objetivo, prerrequisitos y resultado esperado.
- ✅ **Con proyecto de portafolio** — todo módulo debe indicar qué entregable genera.
- ✅ **Respeta la estructura** — usa [`TEMPLATE-MODULO.md`](./TEMPLATE-MODULO.md) para nuevos módulos.

---

## Tu contribución como portafolio

Contribuir a este repositorio genera evidencia de Open Source directamente visible en tu GitHub:

- ⭐ Apareces en el historial de commits del proyecto.
- 📊 Tu contribución suma en tus estadísticas de GitHub.
- 🔗 Puedes referenciarla en LinkedIn como "contribución a proyecto educativo de ciberseguridad open source".

---

## Código de conducta

- Respeto a todos los niveles — no hay preguntas tontas en seguridad.
- Sin contenido ofensivo, discriminatorio o ilegal.
- El objetivo es aprender y enseñar, no competir ni intimidar.
- **Hack the planet, not your neighbor.**

---

*[← Volver al README](./README.md)*
