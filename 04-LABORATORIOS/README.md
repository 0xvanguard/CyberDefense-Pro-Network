<div align="center">

# 🧪 04 — LABORATORIOS

**Práctica controlada · CTFs · HTB · TryHackMe · Labs propios**

*"If you didn't break it and fix it, you didn't learn it."*

</div>

---

## 🎯 Propósito

Esta sección concentra **toda la práctica hands-on**: writeups, máquinas resueltas y entornos vulnerables propios. Es el lugar donde la teoría documentada en `01-CIBERSEGURIDAD/` y `02-SEGURIDAD-INFORMACION/` se valida en escenarios reales.

---

## 📂 Estructura

| Carpeta | Contenido |
|---|---|
| [`ctf-writeups/`](./ctf-writeups/) | Writeups detallados de CTFs (picoCTF, HTB CTF, BSides, etc.) |
| [`htb-thm/`](./htb-thm/) | Máquinas HackTheBox + rooms TryHackMe |
| [`labs-propios/`](./labs-propios/) | Entornos vulnerables creados por mí |
| [`docker-labs/`](./docker-labs/) | `docker-compose.yml` para reproducir cada lab localmente |

---

## 📝 Plantilla estándar de writeup

> Todo writeup debe seguir esta estructura para mantener consistencia:

```markdown
# [Nombre de la máquina/CTF]

| Metadato | Valor |
|---|---|
| Plataforma | HTB / THM / picoCTF / ... |
| Dificultad | Easy / Medium / Hard / Insane |
| Categoría | Web / AD / Linux / Windows / Crypto / ... |
| Fecha | YYYY-MM-DD |
| Tiempo invertido | Xh Ym |

## 🎯 Resumen ejecutivo
Una línea con el TL;DR.

## 🔍 Reconocimiento
- Nmap scan
- Web enumeration (gobuster/ffuf)
- Servicios identificados

## 💥 Explotación
- Vector de entrada
- CVE/técnica usada (referenciar MITRE ATT&CK)
- Foothold obtenido

## 🚀 Escalada de privilegios
- Vector de privesc
- Técnica MITRE ATT&CK aplicable

## 🛡️ Lecciones defensivas
- ¿Cómo se detectaría con Wazuh/Sigma?
- ¿Qué control hubiera prevenido?

## 📚 Referencias
- Links a CVEs, blogs, docs oficiales
```

---

## 🐳 Estándar de docker-labs

Cada lab propio debe incluir:

```
docker-labs/<nombre-lab>/
├── docker-compose.yml      ← Orquestación
├── README.md               ← Objetivo + setup + walkthrough
├── Dockerfile              ← Si requiere build custom
└── solucion/               ← Walkthrough completo (oculto en .gitignore opcional)
```

**Reglas de oro:**
1. ✅ Siempre red bridge aislada (`networks:` definido, no `host`)
2. ✅ Usuario no-root en containers
3. ✅ Variables sensibles en `.env` (con `.env.example` versionado)
4. ✅ `docker compose down -v` debe limpiar todo el estado

---

## 🏁 Plataformas tracked

| Plataforma | Username | Progreso |
|---|---|---|
| HackTheBox | _por completar_ | _N máquinas_ |
| TryHackMe | _por completar_ | _N rooms_ |
| picoCTF | _por completar_ | _N retos_ |
| RootMe | _por completar_ | _N retos_ |

> Actualizar mensualmente.

---

<div align="center">

**[⬅ Volver al README principal](../README.md)**

</div>
