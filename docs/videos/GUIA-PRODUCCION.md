# 🎬 Guía de Producción de Videos — CDPN

> Guía completa para crear videos profesionales para la plataforma.

---

## 📋 Estructura de Video Estándar

### Duración por Tipo
| Tipo | Duración | Ejemplo |
|------|----------|---------|
| **Introductorio** | 5-10 min | "¿Qué es la ciberseguridad?" |
| **Tutorial** | 15-25 min | "Nmap desde cero" |
| **Lab Walkthrough** | 20-40 min | "Resolución de Lame HTB" |
| **Deep Dive** | 30-60 min | "SQL Injection completa" |

### Estructura de 15 minutos
```
00:00 - 01:00  → Intro + hooks (¿por qué ver este video?)
01:00 - 03:00  → Conceptos teóricos rápidos
03:00 - 12:00  → Demo práctica / Ejercicio
12:00 - 14:00  → Resumen + tips
14:00 - 15:00  → CTA (¿qué sigue?)
```

---

## 🎨 Branding del Video

### Elementos Visuales
- **Intro:** Logo CDPN + animación (3 segundos)
- **Lower thirds:** Nombre del tema + módulo
- **Transiciones:** Fade suave entre secciones
- **Outro:** Logo + "Siguiente video" + Subscribe

### Colores
```
Primario:   #2ecc71 (verde)
Secundario: #3498db (azul)
Acento:     #e74c3c (rojo para alerts)
Fondo:      #0a0e1a (oscuro)
```

### Fuentes
- **Títulos:** Inter Bold
- **Código:** JetBrains Mono
- **Subtítulos:** Inter Regular

---

## 🎙️ Guía de Locución

### Tips de Narración
1. **Habla claro y pausado** — No corras
2. **Usa ejemplos concretos** — "Imagina que eres el admin..."
3. **Muestra el código** — Nunca solo hables
4. **Pausa después de conceptos** — Da tiempo para procesar
5. **Termina con acción** — "Ahora ve al lab y pruébalo"

### Script Template
```markdown
## [00:00] Intro
"Hola, bienvenido a CDPN. Soy [nombre] y en este video vamos a aprender sobre [tema]."

## [01:00] Concepto
"Primero, ¿qué es [tema]? Básicamente es [definición simple]."

## [03:00] Demo
"Ahora vamos a ver cómo funciona en la práctica. Abramos [herramienta]..."

## [12:00] Resumen
"Recapitulando: aprendimos [punto 1], [punto 2] y [punto 3]."

## [14:00] CTA
"Si te gustó, dale like y suscríbete. El siguiente video es sobre [tema]."
```

---

## 🛠️ Herramientas Recomendadas

### Grabación
| Herramienta | Uso | Costo |
|-------------|-----|-------|
| **OBS Studio** | Grabación de pantalla | Gratis |
| **ShareX** | Screenshots/GIFs | Gratis |
| **Kdenlive** | Edición de video | Gratis |
| **DaVinci Resolve** | Edición profesional | Gratis |

### Audio
| Herramienta | Uso | Costo |
|-------------|-----|-------|
| **Audacity** | Edición de audio | Gratis |
| **VoiceMeeter** | Mezcla de audio | Gratis |

### Assets
| Herramienta | Uso | Costo |
|-------------|-----|-------|
| **Canva** | Thumbnails | Gratis |
| **Figma** | Diagramas | Gratis |
| **Mermaid** | Diagramas de código | Gratis |

---

## 📁 Estructura de Archivos

```
docs/videos/
├── GUIA-PRODUCCION.md          # Esta guía
├── scripts/                    # Guiones de cada video
│   ├── 01-que-es-ciberseguridad.md
│   ├── 02-glosario.md
│   ├── 03-internet-y-redes.md
│   ├── 04-sistema-operativo.md
│   ├── 05-criptografia.md
│   ├── 06-vulnerabilidades.md
│   ├── 07-etica-y-leyes.md
│   ├── 08-herramientas.md
│   └── 09-como-seguir-repo.md
├── assets/                     # Recursos gráficos
│   ├── intros/
│   ├── lower-thirds/
│   └── outros/
└── output/                     # Videos finales (no subir a git)
```

---

## 📅 Calendario de Producción

### Semana 1: Pre-producción
- [ ] Escribir guiones para 3 videos
- [ ] Crear plantilla de intro/outro
- [ ] Configurar OBS con branding
- [ ] Grabar audio de prueba

### Semana 2: Producción (Videos 1-3)
- [ ] Grabar video 01 (15 min)
- [ ] Grabar video 02 (15 min)
- [ ] Grabar video 03 (20 min)
- [ ] Editar y exportar

### Semana 3: Producción (Videos 4-6)
- [ ] Grabar video 04 (20 min)
- [ ] Grabar video 05 (15 min)
- [ ] Grabar video 06 (20 min)
- [ ] Editar y exportar

### Semana 4: Producción (Videos 7-9)
- [ ] Grabar video 07 (10 min)
- [ ] Grabar video 08 (25 min)
- [ ] Grabar video 09 (10 min)
- [ ] Subir a plataforma

---

## 📊 Métricas de Éxito

### Por Video
- **Views:** 100+ en primer mes
- **Watch time:** 60%+ promedio
- **Engagement:** 5%+ likes
- **Retention:** 50%+ ve hasta el final

### Por Canal
- **Subscribers:** 1,000+ en 6 meses
- **Views totales:** 10,000+ en 6 meses
- **CTR:** 5%+ (click-through rate)

---

*Guía creada para CDPN — Agosto 2026*
