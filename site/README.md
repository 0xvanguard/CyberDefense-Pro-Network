# 🔄 CDPN Sync System

**Sistema de sincronización bidireccional entre GitHub READMEs y la web interactiva.**

## 📊 Cómo Funciona

```
┌─────────────────────────────────────────────────┐
│          FUENTES DE CONTENIDO (Markdown)         │
├─────────────────────────────────────────────────┤
│ site/content/    ← Editas aquí (o en GitHub)     │
│ ├── index.md           ← Landing page            │
│ ├── modules/           ← Módulos de aprendizaje  │
│ ├── labs/              ← Laboratorios            │
│ └── assets/            ← Imágenes, CSS, JS       │
└─────────────────────────────────────────────────┘
                      │
                      ▼
┌─────────────────────────────────────────────────┐
│        VitePress Build (generador estático)      │
│ site/content/ → docs/ (para GitHub Pages)        │
└─────────────────────────────────────────────────┘
                      │
                      ▼
┌─────────────────────────────────────────────────┐
│                DESPLIEGUE                        │
├─────────────────────────────────────────────────┤
│ GitHub Pages → 0xvanguard.github.io/CDPN/       │
│ GitHub       → READMEs (lectura nativa)          │
│ Web          → HTML generado (desde markdown)    │
└─────────────────────────────────────────────────┘
```

## 🚀 Uso Rápido

### Primera vez
```bash
cd site
npm install
node sync.cjs pull      # Sincronizar READMEs → content/
npm run build           # Generar sitio web
```

### Desarrollo local
```bash
cd site
npm run dev             # Servidor de desarrollo en http://localhost:5173
```

### Sincronizar contenido
```bash
node sync.cjs pull      # GitHub READMEs → site/content/
node sync.cjs status    # Ver estado de sincronización
```

### Build para producción
```bash
node sync.cjs build     # Pull + VitePress build → docs/
```

## 📁 Estructura

```
site/
├── .vitepress/
│   └── config.mjs          # Configuración de VitePress
├── content/
│   ├── index.md            # Landing page
│   ├── modules/            # Módulos de aprendizaje
│   │   ├── fundamentos/
│   │   ├── red-team/
│   │   ├── blue-team/
│   │   ├── purple-team/
│   │   ├── ai-agents/
│   │   └── seguridad-informacion/
│   ├── labs/               # Laboratorios
│   │   ├── intermedio/
│   │   └── avanzado/
│   └── assets/             # Recursos estáticos
├── sync.cjs                # Script de sincronización
├── package.json
└── README.md               # Este archivo
```

## 🔄 Sincronización

### Pull: GitHub → Web
```bash
node sync.cjs pull
```
Copia los README.md del repositorio a `site/content/`, agregando frontmatter YAML y transformando links.

### Push: Web → GitHub
**Método 1: Edit on GitHub**
Cada página de la web tiene un botón "✏️ Editar en GitHub" que abre el archivo correspondiente en el editor de GitHub.

**Método 2: Editar en site/content/**
1. Editar el archivo `.md` en `site/content/`
2. Hacer commit y push
3. GitHub Actions reconstruye automáticamente el sitio

### Status: Ver sincronización
```bash
node sync.cjs status
```
Muestra qué archivos están sincronizados, cuáles están desincronizados, y cuáles solo existen en una plataforma.

## 🧪 Labs Interactivos

Los labs mantienen su interactividad con `lab-runner.js`. Cada lab tiene:
- **README.md** en `labs/` (GitHub) → contenido educativo
- **index.html** en `labs/` (web interactiva) → experiencia con gamificación

Para agregar un nuevo lab:
1. Crear `labs/intermedio/mi-lab/README.md`
2. Crear `labs/intermedio/mi-lab/index.html` (usando lab-runner.js)
3. Agregar al SYNC_MAP en `sync.cjs`
4. Ejecutar `node sync.cjs pull`

## 🚀 Deploy

El deploy es automático via GitHub Actions:
1. Push a `main`
2. Workflow instala dependencias
3. Ejecuta `sync.cjs pull`
4. Build con VitePress
5. Despliega a GitHub Pages

## 📝 Agregar Contenido Nuevo

### Nuevo módulo
1. Crear `site/content/modules/mi-modulo/index.md`
2. Agregar al sidebar en `.vitepress/config.mjs`
3. Agregar al SYNC_MAP si viene de un README

### Nuevo lab
1. Crear `site/content/labs/intermedio/mi-lab.md`
2. Agregar al sidebar en `.vitepress/config.mjs`
3. Mantener el `index.html` interactivo en `labs/`

## 🔧 Comandos

| Comando | Descripción |
|---------|-------------|
| `npm run dev` | Servidor de desarrollo |
| `npm run build` | Build completo (sync + vitepress) |
| `npm run pull` | Solo sincronizar READMEs |
| `npm run status` | Ver estado de sincronización |
| `npm run preview` | Vista previa del build |

---

*Sistema de sincronización creado por Buffy — 21 de Agosto, 2026*
