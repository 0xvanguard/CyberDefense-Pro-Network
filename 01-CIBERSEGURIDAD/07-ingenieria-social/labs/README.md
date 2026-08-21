# 🎯 Labs Reproducibles — Ingeniería Social

> Entornos preparados para practicar técnicas de ingeniería social de forma segura y legal.

## ⚠️ Aviso Legal

Estos labs son **exclusivamente para fines educativos**. Úsalos únicamente en entornos controlados y con autorización explícita. El uso indebido de estas técnicas es ilegal y éticamente inaceptable.

## 📋 Requisitos Previos

```bash
# Docker y Docker Compose instalados
docker --version
docker compose version

# Herramientas adicionales (según lab)
pip install gophish  # Para lab de phishing
```

## 🎯 Labs Disponibles

| Lab | Tema | Dificultad | Tiempo estimado |
|-----|------|------------|-----------------|
| [lab-01-gophish-setup](lab-01-gophish-setup/) | Configuración de GoPhish | ⭐ | 30 min |
| [lab-02-phishing-campaign](lab-02-phishing-campaign/) | Campañas de phishing | ⭐⭐ | 45 min |
| [lab-03-pretexting](lab-03-pretexting/) | Escenarios de pretexting | ⭐⭐ | 30 min |

## 🚀 Inicio Rápido

```bash
# Navegar al lab deseado
cd 01-CIBERSEGURIDAD/07-ingenieria-social/labs/lab-01-gophish-setup

# Levantar el entorno
docker compose up -d

# Ver logs
docker compose logs -f

# Detener el entorno
docker compose down
```

## 📖 Estructura de Cada Lab

Cada lab contiene:
- `README.md` — Instrucciones detalladas
- `docker-compose.yml` — Definición del entorno
- `templates/` — Plantillas y scripts de ejemplo
- `solutions/` — Soluciones paso a paso

## Ética y Responsabilidad

Al practicar ingeniería social:

1. **Nunca** ataques a sistemas o personas reales sin autorización
2. **Siempre** documenta tu autorización antes de practicar
3. **Reporta** cualquier vulnerabilidad encontrada al equipo de seguridad
4. **Respeta** la privacidad y dignidad de las personas

---

*Última actualización: Agosto 2024*
