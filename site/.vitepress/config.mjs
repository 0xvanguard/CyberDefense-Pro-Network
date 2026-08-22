import { defineConfig } from 'vitepress'

export default defineConfig({
  title: 'CDPN - CyberDefense Pro Network',
  description: 'Plataforma #1 en español para aprender ciberseguridad',
  lang: 'es',
  
  // Base URL for GitHub Pages
  base: '/CyberDefense-Pro-Network/campus/',
  
  // Clean URLs — remove .html from links (postbuild handles file conversion)
  cleanUrls: true,
  
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
    // Security headers (meta tags - limited, prefer Cloudflare Worker)
    ['meta', { 'http-equiv': 'X-Content-Type-Options', content: 'nosniff' }],
    ['meta', { 'http-equiv': 'X-Frame-Options', content: 'DENY' }],
    ['meta', { name: 'referrer', content: 'strict-origin-when-cross-origin' }],
    ['meta', { 'http-equiv': 'Content-Security-Policy', content: "default-src 'self'; script-src 'self' 'unsafe-inline' https://cdnjs.cloudflare.com https://www.googletagmanager.com; style-src 'self' 'unsafe-inline' https://fonts.googleapis.com https://cdnjs.cloudflare.com; font-src 'self' https://fonts.gstatic.com https://cdnjs.cloudflare.com; img-src 'self' data: https: blob:; connect-src 'self' https://api.github.com; frame-ancestors 'none'; upgrade-insecure-requests" }],
  ],

  markdown: {
    lineNumbers: false,
    math: false,
    // Optimize markdown rendering
    anchor: {
      permalink: false
    }
  },

  // Sitemap for SEO
  sitemap: {
    hostname: 'https://0xvanguard.github.io/CyberDefense-Pro-Network/'
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
      {
        text: '💼 Roles',
        items: [
          { text: '🔴 Red Team', link: '/roles/red-team/' },
          { text: '🔵 Blue Team', link: '/roles/blue-team/' },
          { text: '🔧 Engineering', link: '/roles/engineering/' },
          { text: '📋 GRC', link: '/roles/grc/' },
          { text: '🤖 AI Security', link: '/roles/ai-security/' },
        ]
      },
      { text: '📝 Blog', link: '/blog/' },
      { text: '🏆 Leaderboard', link: '/leaderboard' },
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
            { text: '10 — Linux para Ciberseguridad', link: '/modules/fundamentos/10-linux-ciberseguridad' },
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
            { text: '11 — Introducción a Red Team', link: '/modules/red-team/11-introduccion-red-team' },
            { text: '12 — Post-Exploación Avanzada', link: '/modules/red-team/12-post-exploacion-avanzada' },
            { text: '14 — Active Directory Hacking', link: '/modules/red-team/14-active-directory-hacking' },
          ]
        }
      ],
      '/modules/blue-team/': [
        {
          text: '🔵 Blue Team / Defensa',
          items: [
            { text: 'Visión General', link: '/modules/blue-team/' },
            { text: '01 — Fundamentos Blue Team y SOC', link: '/modules/blue-team/01-fundamentos-blue-team-y-soc' },
            { text: '02 — Análisis de Incidentes', link: '/modules/blue-team/02-analisis-incidentes' },
            { text: '03 — Threat Hunting', link: '/modules/blue-team/03-threat-hunting' },
            { text: '04 — SIEM y Monitoreo', link: '/modules/blue-team/04-siem-monitoreo' },
            { text: '05 — Hardening y Seguridad', link: '/modules/blue-team/05-hardening' },
            { text: '06 — Forense de Endpoint', link: '/modules/blue-team/06-forense-endpoint' },
          ]
        }
      ],
      '/modules/purple-team/': [
        {
          text: '🟣 Purple Team',
          items: [
            { text: 'Visión General', link: '/modules/purple-team/' },
            { text: '01 — Endpoint Procesos y Telemetría', link: '/modules/purple-team/01-purple-endpoint-procesos-telemetria' },
            { text: '02 — Detection Engineering', link: '/modules/purple-team/02-detection-engineering' },
            { text: '03 — Adversary Emulation', link: '/modules/purple-team/03-adversary-emulation' },
            { text: '04 — Tabletop Exercises', link: '/modules/purple-team/04-tabletop-exercises' },
            { text: '05 — Breach & Attack Simulation', link: '/modules/purple-team/05-breach-attack-simulation' },
            { text: '06 — Automated Compliance', link: '/modules/purple-team/06-automated-compliance' },
            { text: '07 — Threat Intelligence Purple Team', link: '/modules/purple-team/07-threat-intelligence' },
            { text: '15 — Purple Team Operations', link: '/modules/purple-team/15-purple-team-operations' },
          ]
        }
      ],
      '/modules/ai-agents/': [
        {
          text: '🤖 AI Agents & Tools',
          items: [
            { text: 'Visión General', link: '/modules/ai-agents/' },
            { text: '01 — Agentes OSINT', link: '/modules/ai-agents/01-agentes-osint' },
            { text: '02 — Agentes Pentest', link: '/modules/ai-agents/02-agentes-pentest' },
            { text: '03 — LLM Security', link: '/modules/ai-agents/03-llm-security' },
            { text: '04 — MLSecOps', link: '/modules/ai-agents/04-mlsecops' },
            { text: '05 — Automatización Python', link: '/modules/ai-agents/05-automatizacion-python' },
            { text: '17 — AI Security', link: '/modules/ai-agents/17-ai-security' },
          ]
        }
      ],
      '/modules/seguridad-informacion/': [
        {
          text: '🛡️ Seguridad de la Información',
          items: [
            { text: 'Visión General', link: '/modules/seguridad-informacion/' },
            { text: '01 — Gestión de Riesgos', link: '/modules/seguridad-informacion/01-gestion-riesgos' },
            { text: '02 — Blue Team / Defensa', link: '/modules/seguridad-informacion/02-blue-team-defensa' },
            { text: '03 — SOC Operations', link: '/modules/seguridad-informacion/03-soc-operations' },
            { text: '04 — DevSecOps', link: '/modules/seguridad-informacion/04-devsecops' },
            { text: '05 — Hardening', link: '/modules/seguridad-informacion/05-hardening-seg-info' },
            { text: '06 — Compliance y Normativas', link: '/modules/seguridad-informacion/06-compliance-normativas' },
            { text: '07 — Threat Intelligence', link: '/modules/seguridad-informacion/07-threat-intelligence-seg-info' },
            { text: '16 — Cloud Security', link: '/modules/seguridad-informacion/16-cloud-security' },
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
      '/roles/red-team/': [
        {
          text: '🔴 Red Team Roles',
          items: [
            { text: '⚔️ Pentester / Red Team', link: '/roles/red-team/pentester-red-team' },
            { text: '🎯 Penetration Tester', link: '/roles/red-team/penetration-tester-specialized' },
            { text: '🎯 Threat Hunter', link: '/roles/red-team/threat-hunter' },
            { text: '🕵️ Threat Intelligence', link: '/roles/red-team/threat-intelligence' },
            { text: '🏹 Bug Bounty', link: '/roles/red-team/bug-bounty-hunting' },
            { text: '🦠 Malware Analyst', link: '/roles/red-team/malware-analyst' },
            { text: '🔢 Cryptographer', link: '/roles/red-team/cryptographer' },
            { text: '🔎 Vulnerability Manager', link: '/roles/red-team/vulnerability-manager' },
            { text: '🔬 Forense Digital', link: '/roles/red-team/forense-digital' },
          ]
        }
      ],
      '/roles/blue-team/': [
        {
          text: '🔵 Blue Team Roles',
          items: [
            { text: '🚨 Analista SOC', link: '/roles/blue-team/analista-soc' },
            { text: '🧑‍💻 Security Analyst', link: '/roles/blue-team/security-analyst' },
            { text: '🚒 Incident Responder', link: '/roles/blue-team/incident-responder' },
            { text: '🛡️ Seguridad Defensiva', link: '/roles/blue-team/seguridad-defensiva-blue-team' },
            { text: '💻 Endpoint Security', link: '/roles/blue-team/seguridad-endpoint' },
            { text: '🌐 Network Security', link: '/roles/blue-team/seguridad-redes' },
            { text: '🛡️ Operational Security', link: '/roles/blue-team/seguridad-operacional' },
          ]
        }
      ],
      '/roles/engineering/': [
        {
          text: '🔧 Engineering Roles',
          items: [
            { text: '🔧 Security Engineer', link: '/roles/engineering/security-engineer' },
            { text: '💼 Security Consultant', link: '/roles/engineering/security-consultant' },
            { text: '🏛️ Arquitecto de Seguridad', link: '/roles/engineering/arquitecto-seguridad' },
            { text: '☁️ Cloud Security', link: '/roles/engineering/seguridad-nube' },
            { text: '🧱 AppSec', link: '/roles/engineering/seguridad-aplicaciones' },
            { text: '🏭 IoT/OT Security', link: '/roles/engineering/seguridad-iot-ot' },
            { text: '🔐 Data Security', link: '/roles/engineering/seguridad-informacion-datos' },
            { text: '📦 Supply Chain', link: '/roles/engineering/seguridad-cadena-suministro' },
            { text: '🤖 AI Security', link: '/roles/engineering/ia-security' },
            { text: '📋 GRC/Compliance', link: '/roles/engineering/grc-compliance' },
          ]
        }
      ],
      '/roles/grc/': [
        {
          text: '📋 GRC Roles',
          items: [
            { text: '👔 CISO', link: '/roles/grc/ciso' },
            { text: '🛡️ DPO', link: '/roles/grc/dpo' },
            { text: '📊 Risk Manager', link: '/roles/grc/risk-manager' },
            { text: '📋 Auditor de Seguridad', link: '/roles/grc/auditor-seguridad' },
            { text: '📐 ISO 27001', link: '/roles/grc/iso-27001' },
            { text: '🔏 Privacy Engineer', link: '/roles/grc/privacy-engineer' },
            { text: '🔄 Business Continuity', link: '/roles/grc/business-continuity' },
          ]
        }
      ],
      '/roles/ai-security/': [
        {
          text: '🤖 AI Security Roles',
          items: [
            { text: '💬 Prompt Engineer', link: '/roles/ai-security/prompt-engineer-security' },
            { text: '🎯 AI Red Teamer', link: '/roles/ai-security/ai-red-teamer' },
            { text: '🧠 ML Security Engineer', link: '/roles/ai-security/ml-security-engineer' },
            { text: '🏛️ AI Governance', link: '/roles/ai-security/ai-governance-officer' },
            { text: '🚨 AI Incident Responder', link: '/roles/ai-security/ai-incident-responder' },
            { text: '📦 AI Supply Chain', link: '/roles/ai-security/ai-supply-chain-security' },
            { text: '🤖 Agentic Security Dev', link: '/roles/ai-security/agentic-security-developer' },
          ]
        }
      ],
      '/blog/': [
        {
          text: '📝 Blog CDPN',
          items: [
            { text: '📋 Todos los artículos', link: '/blog/' },
            { text: '─────────', link: 'noop' },
            { text: '🚀 ¿Por qué ciberseguridad?', link: '/blog/01-porque-ciberseguridad' },
            { text: '🌐 TCP/IP explicado', link: '/blog/02-tcp-ip-simplificado' },
            { text: '🔍 Nmap guía definitiva', link: '/blog/03-nmap-guia-definitiva' },
            { text: '💉 SQL Injection', link: '/blog/04-sql-injection' },
            { text: '🏆 Mi primer CTF', link: '/blog/05-mi-primer-ctf' },
            { text: '💼 Primer empleo', link: '/blog/06-primer-empleo' },
            { text: '🧪 Lab casero', link: '/blog/07-laboratorio-casero' },
            { text: '🤝 Mejores comunidades', link: '/blog/08-comunidades' },
            { text: '🔬 Reverse Engineering', link: '/blog/09-reverse-engineering' },
            { text: '🎣 Phishing y Social Engineering', link: '/blog/10-phishing-ingenieria-social' },
            { text: '🐳 Docker para ciberseguridad', link: '/blog/11-docker-ciberseguridad' },
            { text: '🛡️ OWASP Top 10', link: '/blog/12-owasp-top10' },
            { text: '🔑 Hashing y Cracking', link: '/blog/13-hashing-cracking' },
            { text: '📡 Wi-Fi Hacking', link: '/blog/14-wifi-hacking' },
            { text: '💰 Bug Bounty', link: '/blog/15-bug-bounty' },
            { text: '☁️ Cloud Security', link: '/blog/16-cloud-security' },
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
    // Optimize build
    build: {
      cssMinify: true
    },
    // Custom CSS
    css: {
      preprocessorOptions: {}
    },
    // Resolve aliases
    resolve: {
      alias: {}
    },
    // Optimize dev server
    server: {
      fs: {
        allow: ['..']
      }
    }
  }
})
