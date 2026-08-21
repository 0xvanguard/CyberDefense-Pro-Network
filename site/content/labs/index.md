---
title: Laboratorios Prácticos
description: 25 labs interactivos de ciberseguridad con gamificación, XP y badges
---

<script setup>
import { ref, computed, onMounted } from 'vue'

const labs = ref([
  // Fundamentos
  { id: 'net-01', name: 'Fundamentos de Redes', category: 'fundamentos', difficulty: 'beginner', xp: 100, exercises: 3, time: '30 min', status: 'available' },
  { id: 'linux-01', name: 'Linux y Terminal', category: 'fundamentos', difficulty: 'beginner', xp: 125, exercises: 5, time: '40 min', status: 'available', isNew: true },
  { id: 'crypto-01', name: 'Criptografía Práctica', category: 'fundamentos', difficulty: 'beginner', xp: 150, exercises: 4, time: '45 min', status: 'available', isNew: true },
  { id: 'vuln-01', name: 'Escaneo de Vulnerabilidades', category: 'fundamentos', difficulty: 'beginner', xp: 125, exercises: 4, time: '35 min', status: 'available', isNew: true },
  { id: 'tools-01', name: 'Herramientas Esenciales', category: 'fundamentos', difficulty: 'beginner', xp: 150, exercises: 4, time: '45 min', status: 'available', isNew: true },
  { id: 'linux-sec-01', name: 'Seguridad en Linux', category: 'fundamentos', difficulty: 'beginner', xp: 175, exercises: 5, time: '50 min', status: 'available', isNew: true },
  // Intermedio
  { id: 'recon-01', name: 'Reconocimiento OSINT', category: 'intermedio', difficulty: 'intermediate', xp: 250, exercises: 6, time: '60 min', status: 'available' },
  { id: 'pentest-01', name: 'Pentesting', category: 'intermedio', difficulty: 'intermediate', xp: 300, exercises: 8, time: '90 min', status: 'available' },
  { id: 'webapp-01', name: 'Web Apps Security', category: 'intermedio', difficulty: 'intermediate', xp: 250, exercises: 6, time: '60 min', status: 'available' },
  { id: 'privesc-01', name: 'Privilege Escalation', category: 'intermedio', difficulty: 'intermediate', xp: 300, exercises: 8, time: '90 min', status: 'available' },
  { id: 'vulnscan-01', name: 'Vulnerability Scanning', category: 'intermedio', difficulty: 'intermediate', xp: 200, exercises: 6, time: '45 min', status: 'available' },
  { id: 'web-01', name: 'Web Security', category: 'intermedio', difficulty: 'intermediate', xp: 250, exercises: 6, time: '60 min', status: 'available' },
  { id: 'crypto-02', name: 'Criptografía Avanzada', category: 'intermedio', difficulty: 'intermediate', xp: 200, exercises: 5, time: '45 min', status: 'available' },
  { id: 'disk-forensics-01', name: 'Disk Forensics', category: 'intermedio', difficulty: 'intermediate', xp: 300, exercises: 6, time: '75 min', status: 'available' },
  { id: 'persist-01', name: 'Persistencia', category: 'intermedio', difficulty: 'intermediate', xp: 300, exercises: 8, time: '90 min', status: 'available' },
  { id: 'social-01', name: 'Ingeniería Social', category: 'intermedio', difficulty: 'intermediate', xp: 200, exercises: 5, time: '45 min', status: 'available' },
  { id: 'lateral-01', name: 'Lateral Movement', category: 'intermedio', difficulty: 'intermediate', xp: 350, exercises: 8, time: '100 min', status: 'available' },
  // Avanzado
  { id: 'ad-01', name: 'Active Directory', category: 'avanzado', difficulty: 'advanced', xp: 500, exercises: 12, time: '180 min', status: 'available' },
  { id: 'malware-01', name: 'Análisis de Malware', category: 'avanzado', difficulty: 'advanced', xp: 450, exercises: 10, time: '150 min', status: 'available' },
  { id: 'cloud-01', name: 'Cloud Security', category: 'avanzado', difficulty: 'advanced', xp: 400, exercises: 8, time: '120 min', status: 'available' },
  { id: 'forensics-01', name: 'Forensics Avanzado', category: 'avanzado', difficulty: 'advanced', xp: 500, exercises: 14, time: '200 min', status: 'available' },
  { id: 'reverse-eng-01', name: 'Reverse Engineering', category: 'avanzado', difficulty: 'advanced', xp: 400, exercises: 8, time: '120 min', status: 'available' },
  { id: 'net-forensics-01', name: 'Network Forensics', category: 'avanzado', difficulty: 'advanced', xp: 350, exercises: 6, time: '90 min', status: 'available' },
  // Expert
  { id: 'incident-01', name: 'Incident Response', category: 'expert', difficulty: 'expert', xp: 600, exercises: 6, time: '180 min', status: 'available' },
  { id: 'malware-expert-01', name: 'Malware Expert', category: 'expert', difficulty: 'expert', xp: 700, exercises: 6, time: '210 min', status: 'available' },
  // Blue Team
  { id: 'soc-01', name: 'SOC Operations', category: 'blue-team', difficulty: 'intermediate', xp: 400, exercises: 8, time: '90 min', status: 'available', isNew: true },
  { id: 'incident-02', name: 'Incident Response Blue', category: 'blue-team', difficulty: 'intermediate', xp: 500, exercises: 10, time: '120 min', status: 'available', isNew: true },
  { id: 'siem-01', name: 'SIEM & Monitoreo', category: 'blue-team', difficulty: 'intermediate', xp: 350, exercises: 6, time: '75 min', status: 'available', isNew: true },
  { id: 'hardening-01', name: 'Hardening & Seguridad', category: 'blue-team', difficulty: 'intermediate', xp: 300, exercises: 6, time: '60 min', status: 'available', isNew: true },
  { id: 'forensics-02', name: 'Forensics Blue Team', category: 'blue-team', difficulty: 'intermediate', xp: 400, exercises: 8, time: '90 min', status: 'available', isNew: true },
])

const badges = ref([
  { id: 'first-blood', name: 'First Blood', icon: '🩸', description: 'Completar tu primer lab', requirement: 1, type: 'labs' },
  { id: 'lab-explorer', name: 'Lab Explorer', icon: '🧭', description: 'Completar 5 labs', requirement: 5, type: 'labs' },
  { id: 'lab-master', name: 'Lab Master', icon: '🏅', description: 'Completar 10 labs', requirement: 10, type: 'labs' },
  { id: 'lab-legend', name: 'Lab Legend', icon: '💎', description: 'Completar los 25 labs', requirement: 25, type: 'labs' },
  { id: 'velocista', name: 'Velocista', icon: '⚡', description: 'Completar un lab en <10 min', requirement: 10, type: 'time' },
  { id: 'streak-master', name: 'Streak Master', icon: '🔥', description: '7 días consecutivos', requirement: 7, type: 'streak' },
  { id: 'sharpshooter', name: 'Sharpshooter', icon: '🎯', description: '100% accuracy en ejercicios', requirement: 100, type: 'accuracy' },
  { id: 'crypto-master', name: 'Crypto Master', icon: '🔐', description: 'Completar todos los labs de criptografía', requirement: 2, type: 'category' },
  { id: 'web-hunter', name: 'Web Hunter', icon: '🕸️', description: 'Completar todos los labs de web security', requirement: 3, type: 'category' },
  { id: 'forensic-pro', name: 'Forensic Pro', icon: '🔬', description: 'Completar todos los labs de forensics', requirement: 2, type: 'category' },
])

const totalXP = computed(() => labs.value.reduce((sum, lab) => sum + lab.xp, 0))
const totalExercises = computed(() => labs.value.reduce((sum, lab) => sum + lab.exercises, 0))

const difficultyColors = {
  beginner: { bg: '#d4edda', text: '#155724', label: 'Principiante' },
  intermediate: { bg: '#fff3cd', text: '#856404', label: 'Intermedio' },
  advanced: { bg: '#f8d7da', text: '#721c24', label: 'Avanzado' },
  expert: { bg: '#e2d5f1', text: '#4a1a7a', label: 'Expert' },
}

const categoryIcons = {
  fundamentos: '📘',
  intermedio: '🟡',
  avanzado: '🟠',
  expert: '🔴',
}
</script>

# 🧪 Laboratorios Prácticos

<div style="text-align: center; margin: 2rem 0;">

Aprende ciberseguridad haciendo. Cada lab incluye ejercicios reales, flags por capturar, sistema de XP y badges.

</div>

## 📊 Estadísticas Generales

<div style="display: grid; grid-template-columns: repeat(4, 1fr); gap: 1rem; margin: 2rem 0;">

<div style="background: linear-gradient(135deg, #667eea 0%, #764ba2 100%); color: white; padding: 1.5rem; border-radius: 12px; text-align: center;">
  <div style="font-size: 2.5rem; font-weight: bold;">30</div>
  <div style="opacity: 0.9;">Labs Disponibles</div>
</div>

<div style="background: linear-gradient(135deg, #f093fb 0%, #f5576c 100%); color: white; padding: 1.5rem; border-radius: 12px; text-align: center;">
  <div style="font-size: 2.5rem; font-weight: bold;">177</div>
  <div style="opacity: 0.9;">Ejercicios</div>
</div>

<div style="background: linear-gradient(135deg, #4facfe 0%, #00f2fe 100%); color: white; padding: 1.5rem; border-radius: 12px; text-align: center;">
  <div style="font-size: 2.5rem; font-weight: bold;">10,850</div>
  <div style="opacity: 0.9;">XP Total</div>
</div>

<div style="background: linear-gradient(135deg, #43e97b 0%, #38f9d7 100%); color: white; padding: 1.5rem; border-radius: 12px; text-align: center;">
  <div style="font-size: 2.5rem; font-weight: bold;">4</div>
  <div style="opacity: 0.9;">Niveles</div>
</div>

</div>

---

## 🏆 Leaderboard Global

<div style="background: linear-gradient(135deg, #ffecd2 0%, #fcb69f 100%); padding: 2rem; border-radius: 12px; margin: 2rem 0;">

### 🥇 Top Jugadores

| # | Jugador | XP | Labs | Badges | Nivel |
|---|---------|-----|------|--------|-------|
| 🥇 | CyberNinja | 8,850 | 25 | 10 | 💎 Legend |
| 🥈 | SecWizard | 7,200 | 20 | 8 | 🏅 Master |
| 🥉 | HackerPro | 5,500 | 15 | 6 | 🧭 Explorer |
| 4 | RedTeamer | 4,200 | 12 | 5 | 🧭 Explorer |
| 5 | BlueDefender | 3,000 | 8 | 4 | 🩸 First Blood |

</div>

---

## 🎮 Badges y Logros

<div style="display: grid; grid-template-columns: repeat(2, 1fr); gap: 1rem; margin: 2rem 0;">

<div v-for="badge in badges" :key="badge.id" style="background: white; border: 2px solid #e0e0e0; border-radius: 12px; padding: 1rem; display: flex; align-items: center; gap: 1rem;">
  <div style="font-size: 2rem;">{{ badge.icon }}</div>
  <div>
    <div style="font-weight: bold; color: #333;">{{ badge.name }}</div>
    <div style="font-size: 0.9rem; color: #666;">{{ badge.description }}</div>
  </div>
</div>

</div>

---

## 📘 Fundamento

<div style="display: grid; grid-template-columns: repeat(2, 1fr); gap: 1rem; margin: 1rem 0;">

<div v-for="lab in labs.filter(l => l.category === 'fundamentos')" :key="lab.id" style="background: white; border: 2px solid #28a745; border-radius: 12px; padding: 1.5rem; transition: transform 0.2s, box-shadow 0.2s; cursor: pointer;" onmouseover="this.style.transform='translateY(-5px)'; this.style.boxShadow='0 10px 30px rgba(0,0,0,0.1)'" onmouseout="this.style.transform='translateY(0)'; this.style.boxShadow='none'">
  <div style="display: flex; justify-content: space-between; align-items: start; margin-bottom: 0.5rem;">
    <div style="font-weight: bold; font-size: 1.1rem; color: #333;">
      <span style="margin-right: 0.5rem;">📘</span>
      {{ lab.name }}
      <span v-if="lab.isNew" style="background: #28a745; color: white; padding: 2px 8px; border-radius: 12px; font-size: 0.7rem; margin-left: 0.5rem;">NUEVO</span>
    </div>
    <div style="background: #d4edda; color: #155724; padding: 4px 12px; border-radius: 20px; font-size: 0.8rem; font-weight: bold;">{{ lab.xp }} XP</div>
  </div>
  <div style="display: flex; gap: 1rem; margin-top: 0.5rem;">
    <span style="color: #666; font-size: 0.9rem;">📝 {{ lab.exercises }} ejercicios</span>
    <span style="color: #666; font-size: 0.9rem;">⏱️ {{ lab.time }}</span>
  </div>
  <div style="margin-top: 1rem;">
    <a :href="'/campus/labs/fundamentos/' + lab.id + '/'" style="display: block; background: linear-gradient(135deg, #28a745 0%, #20c997 100%); color: white; text-decoration: none; padding: 10px; border-radius: 8px; text-align: center; font-weight: bold;">🚀 Iniciar Lab</a>
  </div>
</div>

</div>

---

## 🟡 Intermedio

<div style="display: grid; grid-template-columns: repeat(2, 1fr); gap: 1rem; margin: 1rem 0;">

<div v-for="lab in labs.filter(l => l.category === 'intermedio')" :key="lab.id" style="background: white; border: 2px solid #ffc107; border-radius: 12px; padding: 1.5rem; transition: transform 0.2s, box-shadow 0.2s; cursor: pointer;" onmouseover="this.style.transform='translateY(-5px)'; this.style.boxShadow='0 10px 30px rgba(0,0,0,0.1)'" onmouseout="this.style.transform='translateY(0)'; this.style.boxShadow='none'">
  <div style="display: flex; justify-content: space-between; align-items: start; margin-bottom: 0.5rem;">
    <div style="font-weight: bold; font-size: 1.1rem; color: #333;">
      <span style="margin-right: 0.5rem;">🟡</span>
      {{ lab.name }}
    </div>
    <div style="background: #fff3cd; color: #856404; padding: 4px 12px; border-radius: 20px; font-size: 0.8rem; font-weight: bold;">{{ lab.xp }} XP</div>
  </div>
  <div style="display: flex; gap: 1rem; margin-top: 0.5rem;">
    <span style="color: #666; font-size: 0.9rem;">📝 {{ lab.exercises }} ejercicios</span>
    <span style="color: #666; font-size: 0.9rem;">⏱️ {{ lab.time }}</span>
  </div>
  <div style="margin-top: 1rem;">
    <a :href="'/campus/labs/intermedio/' + lab.id + '/'" style="display: block; background: linear-gradient(135deg, #ffc107 0%, #ff9800 100%); color: white; text-decoration: none; padding: 10px; border-radius: 8px; text-align: center; font-weight: bold;">🚀 Iniciar Lab</a>
  </div>
</div>

</div>

---

## 🟠 Avanzado

<div style="display: grid; grid-template-columns: repeat(2, 1fr); gap: 1rem; margin: 1rem 0;">

<div v-for="lab in labs.filter(l => l.category === 'avanzado')" :key="lab.id" style="background: white; border: 2px solid #dc3545; border-radius: 12px; padding: 1.5rem; transition: transform 0.2s, box-shadow 0.2s; cursor: pointer;" onmouseover="this.style.transform='translateY(-5px)'; this.style.boxShadow='0 10px 30px rgba(0,0,0,0.1)'" onmouseout="this.style.transform='translateY(0)'; this.style.boxShadow='none'">
  <div style="display: flex; justify-content: space-between; align-items: start; margin-bottom: 0.5rem;">
    <div style="font-weight: bold; font-size: 1.1rem; color: #333;">
      <span style="margin-right: 0.5rem;">🟠</span>
      {{ lab.name }}
    </div>
    <div style="background: #f8d7da; color: #721c24; padding: 4px 12px; border-radius: 20px; font-size: 0.8rem; font-weight: bold;">{{ lab.xp }} XP</div>
  </div>
  <div style="display: flex; gap: 1rem; margin-top: 0.5rem;">
    <span style="color: #666; font-size: 0.9rem;">📝 {{ lab.exercises }} ejercicios</span>
    <span style="color: #666; font-size: 0.9rem;">⏱️ {{ lab.time }}</span>
  </div>
  <div style="margin-top: 1rem;">
    <a :href="'/campus/labs/avanzado/' + lab.id + '/'" style="display: block; background: linear-gradient(135deg, #dc3545 0%, #e83e8c 100%); color: white; text-decoration: none; padding: 10px; border-radius: 8px; text-align: center; font-weight: bold;">🚀 Iniciar Lab</a>
  </div>
</div>

</div>

---

## 🔴 Expert

<div style="display: grid; grid-template-columns: repeat(2, 1fr); gap: 1rem; margin: 1rem 0;">

<div v-for="lab in labs.filter(l => l.category === 'expert')" :key="lab.id" style="background: white; border: 2px solid #6f42c1; border-radius: 12px; padding: 1.5rem; transition: transform 0.2s, box-shadow 0.2s; cursor: pointer;" onmouseover="this.style.transform='translateY(-5px)'; this.style.boxShadow='0 10px 30px rgba(0,0,0,0.1)'" onmouseout="this.style.transform='translateY(0)'; this.style.boxShadow='none'">
  <div style="display: flex; justify-content: space-between; align-items: start; margin-bottom: 0.5rem;">
    <div style="font-weight: bold; font-size: 1.1rem; color: #333;">
      <span style="margin-right: 0.5rem;">🔴</span>
      {{ lab.name }}
    </div>
    <div style="background: #e2d5f1; color: #4a1a7a; padding: 4px 12px; border-radius: 20px; font-size: 0.8rem; font-weight: bold;">{{ lab.xp }} XP</div>
  </div>
  <div style="display: flex; gap: 1rem; margin-top: 0.5rem;">
    <span style="color: #666; font-size: 0.9rem;">📝 {{ lab.exercises }} ejercicios</span>
    <span style="color: #666; font-size: 0.9rem;">⏱️ {{ lab.time }}</span>
  </div>
  <div style="margin-top: 1rem;">
    <a :href="'/campus/labs/expert/' + lab.id + '/'" style="display: block; background: linear-gradient(135deg, #6f42c1 0%, #9b59b6 100%); color: white; text-decoration: none; padding: 10px; border-radius: 8px; text-align: center; font-weight: bold;">🚀 Iniciar Lab</a>
  </div>
</div>

</div>

---

## 🔵 Blue Team

<div style="display: grid; grid-template-columns: repeat(2, 1fr); gap: 1rem; margin: 1rem 0;">

<div v-for="lab in labs.filter(l => l.category === 'blue-team')" :key="lab.id" style="background: white; border: 2px solid #007bff; border-radius: 12px; padding: 1.5rem; transition: transform 0.2s, box-shadow 0.2s; cursor: pointer;" onmouseover="this.style.transform='translateY(-5px)'; this.style.boxShadow='0 10px 30px rgba(0,0,0,0.1)'" onmouseout="this.style.transform='translateY(0)'; this.style.boxShadow='none'">
  <div style="display: flex; justify-content: space-between; align-items: start; margin-bottom: 0.5rem;">
    <div style="font-weight: bold; font-size: 1.1rem; color: #333;">
      <span style="margin-right: 0.5rem;">🔵</span>
      {{ lab.name }}
      <span v-if="lab.isNew" style="background: #007bff; color: white; padding: 2px 8px; border-radius: 12px; font-size: 0.7rem; margin-left: 0.5rem;">NUEVO</span>
    </div>
    <div style="background: #cce5ff; color: #004085; padding: 4px 12px; border-radius: 20px; font-size: 0.8rem; font-weight: bold;">{{ lab.xp }} XP</div>
  </div>
  <div style="display: flex; gap: 1rem; margin-top: 0.5rem;">
    <span style="color: #666; font-size: 0.9rem;">📝 {{ lab.exercises }} ejercicios</span>
    <span style="color: #666; font-size: 0.9rem;">⏱️ {{ lab.time }}</span>
  </div>
  <div style="margin-top: 1rem;">
    <a :href="'/campus/labs/blue-team/' + lab.id + '/'" style="display: block; background: linear-gradient(135deg, #007bff 0%, #0056b3 100%); color: white; text-decoration: none; padding: 10px; border-radius: 8px; text-align: center; font-weight: bold;">🚀 Iniciar Lab</a>
  </div>
</div>

</div>

---

## 🚀 Cómo Empezar

<div style="background: linear-gradient(135deg, #667eea 0%, #764ba2 100%); color: white; padding: 2rem; border-radius: 12px; margin: 2rem 0;">

### Paso a Paso

1. **Elige un lab** de tu nivel (Fundamento → Intermedio → Avanzado → Expert)
2. **Abre la terminal** del lab interactivo
3. **Sigue las instrucciones** y resuelve cada ejercicio
4. **Captura las flags** para ganar XP
5. **Desbloquea badges** con logros especiales
6. **Sube en el leaderboard** y compite con la comunidad

::: tip 💡 Consejo
Empieza por los labs de Fundamento si eres nuevo. Cada lab tiene hints y soluciones para ayudarte.
:::

</div>

---

## 📈 Progreso por Categoría

<div style="display: grid; grid-template-columns: repeat(4, 1fr); gap: 1rem; margin: 2rem 0;">

<div style="background: #d4edda; padding: 1.5rem; border-radius: 12px; text-align: center;">
  <div style="font-size: 2rem; margin-bottom: 0.5rem;">📘</div>
  <div style="font-weight: bold; color: #155724;">Fundamento</div>
  <div style="font-size: 0.9rem; color: #155724;">6 labs</div>
  <div style="background: #28a745; height: 8px; border-radius: 4px; margin-top: 0.5rem; width: 100%;"></div>
</div>

<div style="background: #fff3cd; padding: 1.5rem; border-radius: 12px; text-align: center;">
  <div style="font-size: 2rem; margin-bottom: 0.5rem;">🟡</div>
  <div style="font-weight: bold; color: #856404;">Intermedio</div>
  <div style="font-size: 0.9rem; color: #856404;">11 labs</div>
  <div style="background: #ffc107; height: 8px; border-radius: 4px; margin-top: 0.5rem; width: 100%;"></div>
</div>

<div style="background: #f8d7da; padding: 1.5rem; border-radius: 12px; text-align: center;">
  <div style="font-size: 2rem; margin-bottom: 0.5rem;">🟠</div>
  <div style="font-weight: bold; color: #721c24;">Avanzado</div>
  <div style="font-size: 0.9rem; color: #721c24;">6 labs</div>
  <div style="background: #dc3545; height: 8px; border-radius: 4px; margin-top: 0.5rem; width: 100%;"></div>
</div>

<div style="background: #e2d5f1; padding: 1.5rem; border-radius: 12px; text-align: center;">
  <div style="font-size: 2rem; margin-bottom: 0.5rem;">🔴</div>
  <div style="font-weight: bold; color: #4a1a7a;">Expert</div>
  <div style="font-size: 0.9rem; color: #4a1a7a;">2 labs</div>
  <div style="background: #6f42c1; height: 8px; border-radius: 4px; margin-top: 0.5rem; width: 100%;"></div>
</div>

</div>

---

## 🎯 Retos Semanales

<div style="background: linear-gradient(135deg, #f093fb 0%, #f5576c 100%); color: white; padding: 2rem; border-radius: 12px; margin: 2rem 0;">

### 🏆 Reto de la Semana

**Completa 3 labs de Fundamento en una semana**

| Requisito | Recompensa |
|-----------|------------|
| Completar 3 labs | 500 XP bonus |
| Completar 5 labs | Badge "Speed Runner" |
| Completar todos los de Fundamento | Badge "Fundamentals Master" |

**Tiempo restante:** 3 días 14 horas

</div>

---

<div style="text-align: center; margin: 3rem 0; color: #666;">

*CyberDefense Labs — Aprende ciberseguridad haciendo*

</div>
