# 🔒 Guía de Seguridad para Labs Docker
## CyberDefense Pro Network

---

## 📋 Tabla de Contenidos

1. [Checklist de Seguridad](#checklist)
2. [Mejores Prácticas](#mejores-prácticas)
3. [Configuración Segura](#configuración)
4. [Monitoreo y Logging](#monitoreo)
5. [Respuesta a Incidentes](#incidentes)

---

## ✅ Checklist de Seguridad {#checklist}

### Antes de crear un lab:

- [ ] **Credenciales**: Usar variables de entorno, nunca hardcoded
- [ ] **Recursos**: Definir límites de CPU y memoria
- [ ] **Healthchecks**: Agregar para todos los servicios críticos
- [ ] **Capabilities**: Usar `cap_drop: ALL` y agregar solo las necesarias
- [ ] **Filesystem**: Usar `read_only: true` cuando sea posible
- [ ] **Logging**: Configurar rotación de logs
- [ ] **Red**: Usar red aislada para el lab
- [ ] **Git**: Agregar `.env` a `.gitignore`

### Durante el desarrollo:

- [ ] **Testing**: Probar con `docker compose up -d`
- [ ] **Health**: Verificar con `docker compose ps`
- [ ] **Logs**: Revisar con `docker compose logs`
- [ ] **Seguridad**: Escanear imágenes con Docker Scout

### Antes de publicar:

- [ ] **Revisión**: Revisar cada docker-compose.yml
- [ ] **Documentación**: Actualizar README con credenciales seguras
- [ ] **Template**: Usar template seguro como base
- [ ] **Validación**: Ejecutar `docker compose config`

---

## 🛡️ Mejores Prácticas {#mejores-prácticas}

### 1. Credenciales Seguras

**❌ MAL:**
```yaml
environment:
  - MYSQL_ROOT_PASSWORD=root123
  - ADMIN_PASSWORD=admin
```

**✅ BIEN:**
```yaml
environment:
  - MYSQL_ROOT_PASSWORD=${MYSQL_ROOT_PASSWORD}
  - ADMIN_PASSWORD=${ADMIN_PASSWORD}
```

**Archivo .env:**
```bash
MYSQL_ROOT_PASSWORD=CHANGE_ME_$(openssl rand -base64 32)
ADMIN_PASSWORD=CHANGE_ME_$(openssl rand -base64 32)
```

### 2. Límites de Recursos

**❌ MAL:**
```yaml
services:
  web:
    image: nginx
```

**✅ BIEN:**
```yaml
services:
  web:
    image: nginx
    deploy:
      resources:
        limits:
          cpus: '1.0'
          memory: 512M
        reservations:
          cpus: '0.25'
          memory: 128M
```

### 3. Capabilities

**❌ MAL:**
```yaml
services:
  web:
    image: nginx
    privileged: true  # ⚠️ NUNCA usar en producción
```

**✅ BIEN:**
```yaml
services:
  web:
    image: nginx
    cap_drop:
      - ALL
    cap_add:
      - NET_BIND_SERVICE  # Solo si necesita puertos < 1024
    security_opt:
      - no-new-privileges:true
```

### 4. Filesystem Read-Only

**❌ MAL:**
```yaml
services:
  web:
    image: nginx
```

**✅ BIEN:**
```yaml
services:
  web:
    image: nginx
    read_only: true
    tmpfs:
      - /tmp
      - /var/cache/nginx
      - /var/run
```

### 5. Healthchecks

**❌ MAL:**
```yaml
services:
  web:
    image: nginx
```

**✅ BIEN:**
```yaml
services:
  web:
    image: nginx
    healthcheck:
      test: ["CMD", "curl", "-f", "http://localhost/"]
      interval: 30s
      timeout: 10s
      retries: 3
      start_period: 40s
```

### 6. Logging

**❌ MAL:**
```yaml
services:
  web:
    image: nginx
```

**✅ BIEN:**
```yaml
services:
  web:
    image: nginx
    logging:
      driver: json-file
      options:
        max-size: "10m"
        max-file: "3"
```

---

## 🔧 Configuración Segura {#configuración}

### Template Docker Compose Seguro

```yaml
version: '3.8'

services:
  web:
    image: vulnerables/web-dvwa:latest
    container_name: ${LAB_NAME:-lab}-web
    
    # 🔒 Seguridad
    deploy:
      resources:
        limits:
          cpus: '1.0'
          memory: 512M
        reservations:
          cpus: '0.25'
          memory: 128M
    
    cap_drop:
      - ALL
    cap_add:
      - NET_BIND_SERVICE
    
    read_only: true
    tmpfs:
      - /tmp
      - /var/run
    
    security_opt:
      - no-new-privileges:true
    
    healthcheck:
      test: ["CMD", "curl", "-f", "http://localhost/"]
      interval: 30s
      timeout: 10s
      retries: 3
      start_period: 40s
    
    logging:
      driver: json-file
      options:
        max-size: "10m"
        max-file: "3"
    
    environment:
      - MYSQL_PASSWD=${MYSQL_PASSWORD:-changeme}
    
    networks:
      lab-net:
        ipv4_address: 10.0.1.10
    
    ports:
      - "${WEB_PORT:-8080}:80"
    
    restart: unless-stopped

networks:
  lab-net:
    driver: bridge
    ipam:
      config:
        - subnet: 10.0.1.0/24
```

### .env Template

```bash
# Lab Configuration
LAB_NAME=lab

# Database Credentials
MYSQL_ROOT_PASSWORD=CHANGE_ME_$(openssl rand -base64 32)
MYSQL_DATABASE=lab
MYSQL_USER=labuser
MYSQL_PASSWORD=CHANGE_ME_$(openssl rand -base64 32)

# Application Credentials
ADMIN_PASSWORD=CHANGE_ME_$(openssl rand -base64 32)

# Ports
WEB_PORT=8080
DB_PORT=3306
```

---

## 📊 Monitoreo y Logging {#monitoreo}

### Verificar Estado de Contenedores

```bash
# Ver todos los contenedores
docker compose ps

# Ver logs en tiempo real
docker compose logs -f

# Ver logs de un servicio específico
docker compose logs -f web

# Verificar healthchecks
docker inspect --format='{{.State.Health.Status}}' <container>
```

### Escaneo de Seguridad

```bash
# Escanear imagen con Docker Scout
docker scout cves <image>

# Escanear con Trivy
trivy image <image>

# Verificar vulnerabilidades
docker scout quickview <image>
```

### Métricas de Recursos

```bash
# Ver uso de recursos
docker stats

# Ver uso de un contenedor específico
docker stats <container>
```

---

## 🚨 Respuesta a Incidentes {#incidentes}

### Si un contenedor está comprometido:

1. **Detener el contenedor**
   ```bash
   docker compose stop <service>
   ```

2. **Preservar evidencia**
   ```bash
   docker commit <container> evidence:$(date +%Y%m%d)
   docker logs <container> > evidence.log
   ```

3. **Analizar**
   ```bash
   docker history <image>
   docker inspect <container>
   ```

4. **Limpiar**
   ```bash
   docker compose down -v  # Eliminar contenedores y volúmenes
   docker system prune -a  # Limpiar imágenes no utilizadas
   ```

5. **Reconstruir**
   ```bash
   docker compose up -d --build
   ```

---

## 📚 Recursos

- [Docker Security Best Practices](https://docs.docker.com/engine/security/)
- [CIS Docker Benchmark](https://www.cisecurity.org/benchmark/docker)
- [OWASP Docker Security](https://cheatsheetseries.owasp.org/cheatsheets/Docker_Security_Cheat_Sheet.html)
- [Docker Scout](https://docs.docker.com/scout/)
- [Trivy Scanner](https://trivy.dev/)

---

## 🔄 Changelog

### v1.0.0 (2026-08-21)
- Creación inicial de la guía
- Checklist de seguridad
- Mejores prácticas
- Template seguro
- Guía de monitoreo
- Guía de respuesta a incidentes

---

*Guía creada por Buffy — Codebuff Security Team*
*Fecha: 21 de Agosto de 2026*
