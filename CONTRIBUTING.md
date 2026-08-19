# 🤝 Guía de Contribuciones

¡Bienvenido a **CyberDefense Pro Network**! Tu experiencia puede ayudar a formar profesionales de ciberseguridad en todo el mundo hispanohablante.

---

## 📋 Tipos de Contribución

### 📚 Contenido Educativo
- Tutoriales paso a paso
- Guías de herramientas
- Ejercicios prácticos
- Case studies de incidentes reales

### 🧪 Laboratorios
- Entornos Docker reproducibles
- Máquinas virtuales
- Scripts de automatización
- Configuraciones de seguridad

### 📖 Documentación
- Mejoras a READMEs
- Traducciones
- Correcciones de errores
- Ejemplos de uso

### 🔧 Herramientas
- Scripts de automatización
- Utilidades de análisis
- Configuraciones de SIEM
- Plantillas de reportes

---

## 🔄 Flujo de Trabajo

### 1. Busca un Issue

```
https://github.com/tu-usuario/CyberDefense-Pro-Network/issues
```

Busca issues con etiquetas:
- `good first issue` - Para nuevos contribuidores
- `help needed` - Necesitan ayuda
- `documentation` - Mejoras de docs
- `new-content` - Nuevo contenido

### 2. Fork y Clone

```bash
# 1. Fork en GitHub

# 2. Clona tu fork
git clone https://github.com/TU-USUARIO/CyberDefense-Pro-Network.git
cd CyberDefense-Pro-Network

# 3. Agrega upstream
git remote add upstream https://github.com/TU-USUARIO/CyberDefense-Pro-Network.git
```

### 3. Crea una Rama

```bash
# Actualiza
git fetch upstream
git checkout main
git merge upstream/main

# Crea rama
git checkout -b feature/tu-contribucion

# Nomenclatura:
# feature/     → Nuevas funcionalidades
# fix/         → Corrección de bugs
# docs/        → Documentación
# lab/         → Laboratorios
# content/     → Contenido educativo
```

### 4. Haz tus Cambios

```bash
# Edita archivos
# Sigue los estándares de calidad (ver abajo)

# Verifica
python3 -m py_compile tu_script.py
markdownlint tu_archivo.md
```

### 5. Documenta

```bash
# Actualiza README si es necesario
# Agrega changelog
# Incluye ejemplos de uso
```

### 6. Commit

```bash
git add .
git commit -m "feat: add new SQL injection lab

- Add vulnerable web application
- Include step-by-step guide
- Add Docker configuration
- Fixes #123"
```

**Formato:** `<tipo>: <descripción corta>`

| Tipo | Uso |
|------|-----|
| `feat:` | Nueva funcionalidad |
| `fix:` | Corrección |
| `docs:` | Documentación |
| `lab:` | Laboratorio |
| `content:` | Contenido |

### 7. Push y PR

```bash
git push origin feature/tu-contribucion
```

Ve a GitHub y crea el Pull Request.

---

## ✅ Estándares de Calidad

### 📝 Para Documentación

```markdown
- [ ] Título claro y descriptivo
- [ ] Objetivos de aprendizaje definidos
- [ ] Prerrequisitos listados
- [ ] Pasos numerados y detallados
- [ ] Ejemplos con salida esperada
- [ ] Screenshots donde aplique
- [ ] Referencias y links
```

### 💻 Para Código

```python
"""
Descripción del script.

Uso: python3 script.py [opciones]
Autor: Tu Nombre
Fecha: 2026-08-19
"""

import module

def funcion_ejemplo(parametro: str) -> bool:
    """
    Descripción de la función.
    
    Args:
        parametro: Descripción
        
    Returns:
        bool: Descripción del retorno
    """
    pass
```

### 🧪 Para Laboratorios

```markdown
## Estructura Requerida

lab-nombre/
├── README.md           # Obligatorio
├── docker-compose.yml  # Si aplica
├── Dockerfile          # Si aplica
├── scripts/           # Scripts de setup
├── docs/              # Documentación
└── screenshots/       # Capturas
```

---

## 📊 Niveles de Contribuidor

| Nivel | Requisito | Beneficios |
|-------|-----------|------------|
| 🌱 **Contributor** | 1-3 PRs | Mención en README |
| 🌿 **Active Contributor** | 4-10 PRs | Badge + mención |
| 🌳 **Maintainer** | 11+ PRs | Acceso directo |
| 🏆 **Core Team** | Invitación | Decisiones del proyecto |

---

## 📞 Soporte

- **Issues:** Para bugs específicos
- **Discussions:** Para preguntas
- **LinkedIn:** Networking profesional

---

## 📜 Código de Conducta

- Sé respetuoso y profesional
- Enfócate en el aprendizaje
- Promueve el uso ético
- Ayuda a otros contribuidores

---

## 📄 Licencia

Al contribuir, aceptas que tu contribución sea licenciada bajo MIT License.

---

*Gracias por hacer posible esta plataforma educativa! 🛡️*
