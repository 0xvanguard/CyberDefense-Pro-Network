# 🧪 Labs Reproducibles — Post-Explotación

> Entornos Docker preparados para practicar técnicas de post-explotación de forma segura y legal.

## ⚠️ Aviso Legal

Estos labs son **exclusivamente para fines educativos**. Úsalos únicamente en entornos controlados y con autorización explícita. El autor no se hace responsable del uso indebido de estas herramientas.

## 📋 Requisitos Previos

```bash
# Docker y Docker Compose instalados
docker --version
docker compose version

# git (para clonar el repo)
git --version
```

## 🎯 Labs Disponibles

| Lab | Tema | Dificultad | Tiempo estimado |
|-----|------|------------|-----------------|
| [lab-01-privesc-linux](lab-01-privesc-linux/) | Escalada de privilegios Linux | ⭐⭐ | 45 min |
| [lab-02-privesc-windows](lab-02-privesc-windows/) | Escalada de privilegios Windows | ⭐⭐⭐ | 60 min |
| [lab-03-persistence-linux](lab-03-persistence-linux/) | Persistencia Linux | ⭐⭐ | 30 min |
| [lab-04-lateral-movement](lab-04-lateral-movement/) | Movimiento lateral | ⭐⭐⭐ | 45 min |

## 🚀 Inicio Rápido

```bash
# Navegar al lab deseado
cd 01-CIBERSEGURIDAD/05-post-explotacion/labs/lab-01-privesc-linux

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
- `Dockerfile` — Configuración del contenedor
- `scripts/` — Scripts de configuración y solución
- `solutions/` — Soluciones paso a paso (sin spoilers)

## 🔧 Solucionar Problemas

```bash
# Si un contenedor no inicia
docker compose up -d --build

# Limpiar todos los contenedores
docker compose down -v --rmi all

# Verificar puertos en uso
sudo lsof -i :PORT
```

---

*Última actualización: Agosto 2024*
