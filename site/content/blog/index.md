---
title: Blog CDPN
description: Artículos sobre ciberseguridad, hacking ético y seguridad de la información
layout: page
---

<script setup>
const articles = [
  { emoji: '🚀', title: '¿Por qué la ciberseguridad es la carrera del futuro?', path: '01-porque-ciberseguridad', week: 1, desc: 'Estadísticas de demanda laboral, salarios y rutas de aprendizaje.', tags: ['Carrera', 'Mercado'], readTime: '5 min' },
  { emoji: '🌐', title: 'TCP/IP explicado como si tuvieras 5 años', path: '02-tcp-ip-simplificado', week: 2, desc: 'Los fundamentos de redes que toda carrera en ciberseguridad requiere.', tags: ['Redes', 'Fundamentos'], readTime: '4 min' },
  { emoji: '🔍', title: 'Nmap: la guía definitiva para principiantes', path: '03-nmap-guia-definitiva', week: 3, desc: '20 comandos esenciales con casos de uso reales.', tags: ['Herramientas', 'Red Team'], readTime: '6 min' },
  { emoji: '💉', title: 'SQL Injection: el ataque más común explicado', path: '04-sql-injection', week: 4, desc: 'Qué es, cómo funciona y cómo prevenirlo.', tags: ['Web', 'OWASP'], readTime: '5 min' },
  { emoji: '🏆', title: 'Mi primer CTF: lo que aprendí', path: '05-mi-primer-ctf', week: 5, desc: 'Experiencia personal, tips para empezar y recursos.', tags: ['CTF', 'Práctica'], readTime: '4 min' },
  { emoji: '💼', title: 'Cómo conseguí mi primer empleo en ciberseguridad', path: '06-primer-empleo', week: 6, desc: 'Camino personal, certificaciones y tips de entrevista.', tags: ['Carrera', 'Certificaciones'], readTime: '5 min' },
  { emoji: '🧪', title: 'Cómo crear tu laboratorio de ciberseguridad', path: '07-laboratorio-casero', week: 7, desc: 'Hardware, software, Docker y presupuesto.', tags: ['Labs', 'Docker'], readTime: '4 min' },
  { emoji: '🤝', title: 'Las 10 mejores comunidades de ciberseguridad', path: '08-comunidades', week: 8, desc: 'Discords, foros, redes sociales y eventos.', tags: ['Comunidad', 'Networking'], readTime: '3 min' },
  { emoji: '🔬', title: 'Reverse Engineering: desensamblar binarios sin morir', path: '09-reverse-engineering', week: 9, desc: 'Introducción práctica a RE con Ghidra, radare2 y ejemplos reales.', tags: ['RE', 'Ghidra'], readTime: '6 min' },
  { emoji: '🎣', title: 'Phishing: cómo detectar y prevenir el ataque más efectivo', path: '10-phishing-ingenieria-social', week: 10, desc: 'Tipos de phishing, técnicas de detección y herramientas.', tags: ['Phishing', 'Social'], readTime: '5 min' },
  { emoji: '🐳', title: 'Docker para ciberseguridad: monta tu lab en minutos', path: '11-docker-ciberseguridad', week: 11, desc: 'Containers, DVWA, vulnerable apps y laboratorio completo.', tags: ['Docker', 'Labs'], readTime: '5 min' },
  { emoji: '🛡️', title: 'OWASP Top 10: las 10 vulnerabilidades web más peligrosas', path: '12-owasp-top10', week: 12, desc: 'Explicación práctica de cada vulnerabilidad con ejemplos.', tags: ['OWASP', 'Web'], readTime: '7 min' },
]
</script>

<style>
.blog-hero {
  text-align: center;
  padding: 2rem 0 1.5rem;
}
.blog-hero h1 {
  font-size: 2rem;
  margin-bottom: 0.5rem;
}
.blog-hero p {
  color: var(--vp-c-text-2);
  font-size: 1.05rem;
  max-width: 600px;
  margin: 0 auto;
}
.blog-grid {
  display: grid;
  grid-template-columns: repeat(auto-fill, minmax(320px, 1fr));
  gap: 1.2rem;
  padding: 1rem 0 2rem;
}
.blog-card {
  border: 1px solid var(--vp-c-divider);
  border-radius: 12px;
  padding: 1.5rem;
  transition: all 0.25s ease;
  background: var(--vp-c-bg-soft);
  text-decoration: none;
  color: inherit;
  display: flex;
  flex-direction: column;
}
.blog-card:hover {
  border-color: var(--vp-c-brand-1);
  box-shadow: 0 4px 20px rgba(0,0,0,0.08);
  transform: translateY(-2px);
}
.blog-card-emoji {
  font-size: 2rem;
  margin-bottom: 0.6rem;
}
.blog-card-title {
  font-size: 1.05rem;
  font-weight: 600;
  margin-bottom: 0.4rem;
  line-height: 1.4;
}
.blog-card-desc {
  color: var(--vp-c-text-2);
  font-size: 0.9rem;
  flex: 1;
  margin-bottom: 0.8rem;
}
.blog-card-meta {
  display: flex;
  align-items: center;
  gap: 0.6rem;
  flex-wrap: wrap;
  font-size: 0.8rem;
  color: var(--vp-c-text-3);
}
.blog-tag {
  background: var(--vp-c-default-soft);
  padding: 2px 8px;
  border-radius: 6px;
  font-size: 0.75rem;
  color: var(--vp-c-text-2);
}
.blog-tag-accent {
  background: var(--vp-c-brand-soft);
  color: var(--vp-c-brand-1);
}
</style>

<div class="blog-hero">

# 📝 Blog CDPN

Artículos semanales sobre ciberseguridad, hacking ético y seguridad de la información.

</div>

<div class="blog-grid">
  <a v-for="a in articles" :key="a.path" class="blog-card" :href="a.path + '/'">
    <div class="blog-card-emoji">{{ a.emoji }}</div>
    <div class="blog-card-title">{{ a.title }}</div>
    <div class="blog-card-desc">{{ a.desc }}</div>
    <div class="blog-card-meta">
      <span class="blog-tag blog-tag-accent">Semana {{ a.week }}</span>
      <span v-for="tag in a.tags" :key="tag" class="blog-tag">{{ tag }}</span>
      <span style="margin-left:auto">📖 {{ a.readTime }}</span>
    </div>
  </a>
</div>

---

*Artículos publicados semanalmente por el equipo CDPN. Última actualización: Agosto 2026.*
