# 🧪 Lab 04 — SQLi, XSS e IDOR + hardening

> **Objetivo:** Explotar tres vulnerabilidades en DVWA/WebGoat/Juice Shop, aplicar mitigaciones básicas en un reverse proxy y re-testear.

---

## Arquitectura del lab

```text
Red 172.32.0.0/24 (se separa de la del Módulo 03 para claridad)

172.32.0.10  → dvwa-web
172.32.0.20  → webgoat
172.32.0.30  → juice-shop
172.32.0.40  → reverse-proxy-nginx
```

---

## Prerrequisitos

- [ ] Docker + Docker Compose
- [ ] Navegador
- [ ] Herramientas del módulo 03 (opcional para apoyo)

---

## Levantar el entorno

```bash
cd laboratorio/
docker compose up -d
docker compose ps
```

Accesos esperados (ejemplo):
- DVWA → `http://localhost:8084`
- WebGoat → `http://localhost:8085/WebGoat`
- Juice Shop → `http://localhost:8086`

Todo el tráfico pasará por el `reverse-proxy` que aplicarás.

---

## Fase 1 — Explotación

Sigue las guías en `../explotacion/` para:
- [ ] SQLi en DVWA.
- [ ] XSS en DVWA y Juice Shop.
- [ ] IDOR en WebGoat y/o Juice Shop.

Documenta cada caso con el template de writeup.

---

## Fase 2 — Hardening

- Configura el `reverse-proxy` usando el archivo de ejemplo.
- Añade headers de seguridad.
- Revisa la checklist de hardening.

---

## Fase 3 — Re-test (Purple Team)

- Repite las pruebas de explotación.
- Documenta qué cambió y qué ya no es explotable.
- Actualiza el change-log.

---

## Limpiar el entorno

```bash
docker compose down
docker compose down -v
```

---

**[← Checklist hardening](../defensa/checklist-hardening-web.md)** · **[→ Templates de portafolio](../portafolio/TEMPLATE-writeup-exploit.md)**
