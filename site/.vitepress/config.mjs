import { defineConfig } from 'vitepress'

export default defineConfig({
  title: 'CDPN - CyberDefense Pro Network',
  description: 'Plataforma #1 en español para aprender ciberseguridad',
  lang: 'es',
  
  // Base URL for GitHub Pages
  base: '/CyberDefense-Pro-Network/campus/',
  
  // Build output to docs/campus/ — keeps existing docs/ files intact
  // When running from site/content/, this resolves to ../../docs/campus
  outDir: '../../docs/campus',
  
  // Clean only the campus/ output directory
  cleanOutDir: true,
  
  // READMEs have links to repo files that don't exist in VitePress yet
  // These will be fixed incrementally as content is migrated
  ignoreDeadLinks: true,

  head: [
    ['link', { rel: 'icon', type: 'image/svg+xml', href: '/CyberDefense-Pro-Network/favicon.svg' }],
    ['meta', { name: 'theme-color', content: '#0a0e1a' }],
    ['meta', { property: 'og:type', content: 'website' }],
    ['meta', { property: 'og:title', content: 'CDPN - CyberDefense Pro Network' }],
    ['meta', { property: 'og:description', content: 'Plataforma #1 en español para aprender ciberseguridad' }],
    ['meta', { property: 'og:image', content: '/CyberDefense-Pro-Network/assets/og-image.png' }],
  ],

  markdown: {
    lineNumbers: true,
    math: false,
  },

  themeConfig: {
    logo: '/favicon.svg',
    siteTitle: 'CDPN',
    
    // Edit link - points to GitHub for bidirectional sync
    editLink: {
      pattern: 'https://github.com/0xvanguard/CyberDefense-Pro-Network/edit/main/site/content/:path',
      text: '✏️ Editar en GitHub'
    },

    // Campus link from main site
    campusLink: {
      text: '🎓 Campus Virtual',
      link: '/CyberDefense-Pro-Network/campus/'
    },

    // Last updated
    lastUpdated: {
      text: 'Última actualización'
    },

    // Search
    search: {
      provider: 'local',
      options: {
        translations: {
          button: { buttonText: 'Buscar', buttonAriaLabel: 'Buscar' },
          modal: {
            noResultsText: 'Sin resultados',
            resetButtonTitle: 'Limpiar',
            footer: { selectText: 'Seleccionar', navigateText: 'Navegar', closeText: 'Cerrar' }
          }
        }
      }
    },

    // Social links
    socialLinks: [
      { icon: 'github', link: 'https://github.com/0xvanguard/CyberDefense-Pro-Network' }
    ],

    // Navigation
    nav: [
      { text: 'Inicio', link: '/' },
      {
        text: 'Módulos',
        items: [
          { text: '🚀 Fundamentos', link: '/modules/fundamentos/' },
          { text: '🔴 Red Team', link: '/modules/red-team/' },
          { text: '🔵 Blue Team', link: '/modules/blue-team/' },
          { text: '🟣 Purple Team', link: '/modules/purple-team/' },
          { text: '🤖 AI Agents', link: '/modules/ai-agents/' },
          { text: '🛡️ Seguridad Info.', link: '/modules/seguridad-informacion/' },
        ]
      },
      { text: 'Labs', link: '/labs/' },
      { text: '✏️ Editar', link: '/admin.html' },
    ],

    // Sidebar
    sidebar: {
      '/modules/fundamentos/': [
        {
          text: '🚀 Fundamentos',
          items: [
            { text: 'Visión General', link: '/modules/fundamentos/' },
            { text: '01 — ¿Qué es Ciberseguridad?', link: '/modules/fundamentos/01-que-es-ciberseguridad' },
            { text: '02 — Glosario', link: '/modules/fundamentos/02-glosario' },
            { text: '03 — Internet y Redes', link: '/modules/fundamentos/03-internet-y-redes' },
            { text: '04 — SO y Terminal', link: '/modules/fundamentos/04-sistema-operativo-y-terminal' },
            { text: '05 — Criptografía Básica', link: '/modules/fundamentos/05-criptografia-basica' },
            { text: '06 — Vulnerabilidades', link: '/modules/fundamentos/06-vulnerabilidades' },
            { text: '07 — Ética y Leyes', link: '/modules/fundamentos/07-etica-y-leyes' },
            { text: '08 — Herramientas Esenciales', link: '/modules/fundamentos/08-herramientas-esenciales' },
            { text: '09 — Cómo Seguir', link: '/modules/fundamentos/09-como-seguir-este-repo' },
          ]
        },
        {
          text: '🗺️ Rutas',
          items: [
            { text: 'Ruta Defensor', link: '/modules/fundamentos/rutas/ruta-defensor' },
            { text: 'Ruta Atacante', link: '/modules/fundamentos/rutas/ruta-atacante' },
            { text: 'Ruta AI Security', link: '/modules/fundamentos/rutas/ruta-ai-security' },
          ]
        }
      ],
      '/modules/red-team/': [
        {
          text: '🔴 Red Team / Ofensiva',
          items: [
            { text: 'Visión General', link: '/modules/red-team/' },
            { text: '01 — Reconocimiento OSINT', link: '/modules/red-team/01-reconocimiento-osint' },
            { text: '02 — Pentesting', link: '/modules/red-team/02-pentesting-red-team' },
            { text: '03 — Análisis Vulnerabilidades', link: '/modules/red-team/03-analisis-vulnerabilidades' },
            { text: '04 — Explotación Web', link: '/modules/red-team/04-explotacion-web' },
            { text: '05 — Post-Explotación', link: '/modules/red-team/05-post-explotacion' },
            { text: '06 — Forense Digital', link: '/modules/red-team/06-forense-digital' },
            { text: '07 — Ingeniería Social', link: '/modules/red-team/07-ingenieria-social' },
            { text: '08 — Criptografía', link: '/modules/red-team/08-criptografia' },
          ]
        }
      ],
      '/modules/blue-team/': [
        {
          text: '🔵 Blue Team / Defensa',
          items: [
            { text: 'Visión General', link: '/modules/blue-team/' },
          ]
        }
      ],
      '/modules/purple-team/': [
        {
          text: '🟣 Purple Team',
          items: [
            { text: 'Visión General', link: '/modules/purple-team/' },
          ]
        }
      ],
      '/modules/ai-agents/': [
        {
          text: '🤖 AI Agents & Tools',
          items: [
            { text: 'Visión General', link: '/modules/ai-agents/' },
          ]
        }
      ],
      '/modules/seguridad-informacion/': [
        {
          text: '🛡️ Seguridad de la Información',
          items: [
            { text: 'Visión General', link: '/modules/seguridad-informacion/' },
          ]
        }
      ],
      '/labs/': [
        {
          text: '🧪 Laboratorios',
          items: [
            { text: 'Catálogo de Labs', link: '/labs/' },
            { text: 'Intermedio', items: [
              { text: 'recon-01: Reconocimiento', link: '/labs/intermedio/recon-01' },
              { text: 'pentest-01: Pentesting', link: '/labs/intermedio/pentest-01' },
              { text: 'webapp-01: Web Apps', link: '/labs/intermedio/webapp-01' },
              { text: 'privesc-01: Privilege Escalation', link: '/labs/intermedio/privesc-01' },
              { text: 'vulnscan-01: Vulnerability Scan', link: '/labs/intermedio/vulnscan-01' },
              { text: 'web-01: Web Security', link: '/labs/intermedio/web-01' },
              { text: 'crypto-01: Criptografía', link: '/labs/intermedio/crypto-01' },
              { text: 'disk-forensics-01: Disk Forensics', link: '/labs/intermedio/disk-forensics-01' },
            ]},
            { text: 'Avanzado', items: [
              { text: 'ad-01: Active Directory', link: '/labs/avanzado/ad-01' },
              { text: 'malware-01: Malware Analysis', link: '/labs/avanzado/malware-01' },
              { text: 'cloud-01: Cloud Security', link: '/labs/avanzado/cloud-01' },
              { text: 'forensics-01: Advanced Forensics', link: '/labs/avanzado/forensics-01' },
              { text: 'reverse-eng-01: Reverse Engineering', link: '/labs/avanzado/reverse-eng-01' },
              { text: 'net-forensics-01: Network Forensics', link: '/labs/avanzado/net-forensics-01' },
            ]},
          ]
        }
      ],
    },

    // Footer
    footer: {
      message: 'CyberDefense Pro Network — Formando profesionales de ciberdefensa',
      copyright: '© 2026 CDPN. Todos los derechos reservados.'
    },

    // Outline (table of contents)
    outline: {
      level: [2, 3],
      label: 'En esta página'
    },

    // Carbon ads (disabled)
    carbonAds: undefined,
  },

  // Build configuration
  vite: {
    // Custom CSS
    css: {
      preprocessorOptions: {}
    },
    // Resolve aliases
    resolve: {
      alias: {}
    }
  }
})
