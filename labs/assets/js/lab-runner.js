/* ========================================
   CDPN Lab Runner — Interactive Lab Engine
   ======================================== */

const CDPN_LabRunner = {
    config: null,
    startTime: null,
    exerciseStates: {},

    // Initialize a lab from its config
    init(config) {
        this.config = config;
        this.startTime = Date.now();
        this.exerciseStates = this.loadProgress();

        this.render();
        this.bindEvents();
        this.updateProgress();

        console.log(`🧪 Lab Runner initialized: ${config.id}`);
        return this;
    },

    // Load saved progress
    loadProgress() {
        try {
            const key = `cdpn_lab_${this.config.id}`;
            const saved = localStorage.getItem(key);
            if (saved) return JSON.parse(saved);
        } catch (e) {}
        return {};
    },

    // Save progress
    saveProgress() {
        try {
            const key = `cdpn_lab_${this.config.id}`;
            localStorage.setItem(key, JSON.stringify({
                exercises: this.exerciseStates,
                startedAt: this.startTime,
                lastUpdated: Date.now()
            }));
        } catch (e) {}
    },

    // ===== RENDERING =====
    render() {
        const page = document.getElementById('lab-page');
        if (!page) return;

        const diffConfig = this.getDifficultyConfig();

        page.innerHTML = `
            <!-- HEADER -->
            <header class="lab-header">
                <div class="lab-title-section">
                    <span class="lab-icon">${this.config.icon}</span>
                    <div>
                        <div class="lab-title">${this.config.name}</div>
                        <div class="lab-subtitle">${this.config.subtitle}</div>
                    </div>
                </div>
                <div class="lab-meta-tags">
                    <span class="meta-tag difficulty">${diffConfig.icon} ${diffConfig.label}</span>
                    <span class="meta-tag xp">⚡ ${this.config.totalXP} XP</span>
                    <span class="meta-tag time">⏱️ ${this.config.time}</span>
                    <span class="meta-tag flags">🚩 ${this.config.exercises.length} ejercicios</span>
                </div>
            </header>

            <!-- PROGRESS STRIP -->
            <div class="lab-progress-strip">
                <div class="xp-live">
                    <span class="xp-icon">⚡</span>
                    <span id="live-xp">0</span> / ${this.config.totalXP} XP
                </div>
                <div class="bar-wrapper">
                    <span class="bar-label">Progreso</span>
                    <div class="bar-track">
                        <div class="bar-fill" id="progress-fill"></div>
                    </div>
                    <span class="bar-percent" id="progress-percent">0%</span>
                </div>
                <span class="exercises-count" id="exercises-count">0 / ${this.config.exercises.length} completados</span>
            </div>

            <!-- EXERCISES -->
            <div id="exercises-container">
                ${this.config.exercises.map((ex, i) => this.renderExercise(ex, i)).join('')}
            </div>

            <!-- COMPLETION BANNER -->
            <div class="lab-complete-banner" id="complete-banner">
                <div class="trophy">🏆</div>
                <h2>¡Lab Completado!</h2>
                <div class="xp-earned">+${this.config.totalXP} XP ganados</div>
                <div class="time-spent" id="time-spent"></div>
                <div class="actions">
                    <button class="primary-action" onclick="CDPN_LabRunner.shareResults()">📤 Compartir Resultado</button>
                    <button class="secondary-action" onclick="window.location.href='../index.html'">⬅️ Volver al Catálogo</button>
                </div>
            </div>
        `;
    },

    renderExercise(exercise, index) {
        const state = this.exerciseStates[index] || {};
        const isCompleted = !!state.completed;
        const num = index + 1;

        return `
            <div class="exercise-card ${isCompleted ? 'completed' : ''}" id="exercise-${index}" data-index="${index}">
                <div class="exercise-header" onclick="CDPN_LabRunner.toggleExercise(${index})">
                    <div class="exercise-checkbox" onclick="event.stopPropagation(); CDPN_LabRunner.toggleComplete(${index})">
                        ${isCompleted ? '✓' : ''}
                    </div>
                    <span class="exercise-number">EJ ${num}</span>
                    <span class="exercise-title">${exercise.title}</span>
                    <span class="exercise-xp">${isCompleted ? '✅' : '+' + exercise.xp + ' XP'}</span>
                    <span class="exercise-expand-icon">▼</span>
                </div>
                <div class="exercise-body">
                    <div class="exercise-objective">
                        <strong>🎯 Objetivo:</strong> ${exercise.objective}
                    </div>

                    <div class="exercise-steps">
                        <h4>Pasos a seguir</h4>
                        ${exercise.steps.map((step, si) => `
                            <div class="step-item">
                                <span class="step-num">${si + 1}</span>
                                <span class="step-text">${step}</span>
                            </div>
                        `).join('')}
                    </div>

                    ${exercise.code ? `
                        <div class="code-block">
                            <div class="code-block-header">
                                <span class="lang">${exercise.codeLang || 'bash'}</span>
                                <button class="copy-btn" onclick="CDPN_LabRunner.copyCode(this)">📋 Copiar</button>
                            </div>
                            <pre>${exercise.code}</pre>
                        </div>
                    ` : ''}

                    ${exercise.flag ? `
                        <div class="flag-input-group">
                            <input type="text" class="flag-input"
                                placeholder="🚩 Ingresa la flag aquí..."
                                id="flag-input-${index}"
                                ${isCompleted ? 'disabled' : ''}
                                onkeydown="if(event.key==='Enter') CDPN_LabRunner.submitFlag(${index})">
                            <button class="flag-submit-btn"
                                onclick="CDPN_LabRunner.submitFlag(${index})"
                                ${isCompleted ? 'disabled' : ''}>
                                ${isCompleted ? '✅ Resuelto' : '🚩 Verificar'}
                            </button>
                        </div>
                        <div class="flag-result" id="flag-result-${index}"></div>
                    ` : ''}

                    ${exercise.hint ? `
                        <button class="hint-btn" onclick="CDPN_LabRunner.showHint(${index})">
                            💡 Necesito una pista
                        </button>
                        <div class="hint-text" id="hint-${index}">${exercise.hint}</div>
                    ` : ''}

                    ${exercise.solution ? `
                        <details class="solution-toggle">
                            <summary>🔓 Ver solución (solo si es necesario)</summary>
                            <div class="solution-content">${exercise.solution}</div>
                        </details>
                    ` : ''}

                    <button class="complete-exercise-btn"
                        onclick="CDPN_LabRunner.toggleComplete(${index})"
                        ${isCompleted ? 'disabled' : ''}>
                        ${isCompleted ? '✅ Ejercicio Completado' : '✅ Marcar como Completado'}
                    </button>
                </div>
            </div>
        `;
    },

    // ===== INTERACTIONS =====
    toggleExercise(index) {
        const card = document.getElementById(`exercise-${index}`);
        card.classList.toggle('open');
    },

    toggleComplete(index) {
        const ex = this.config.exercises[index];
        const wasCompleted = !!this.exerciseStates[index]?.completed;

        if (wasCompleted) return; // Don't un-complete

        this.exerciseStates[index] = {
            completed: true,
            completedAt: Date.now()
        };

        this.saveProgress();

        // Award XP
        this.showXPPopup(`+${ex.xp} XP`, ex.title);

        // Update gamification
        if (typeof CDPN_Gamification !== 'undefined') {
            CDPN_Gamification.addXP(ex.xp, `Ejercicio: ${ex.title}`);
        }

        this.updateProgress();
        this.updateExerciseCard(index);
        this.checkLabCompletion();
    },

    submitFlag(index) {
        const ex = this.config.exercises[index];
        const input = document.getElementById(`flag-input-${index}`);
        const result = document.getElementById(`flag-result-${index}`);
        const userFlag = input.value.trim();

        if (!userFlag) return;

        // Check flag (case-insensitive, flexible format)
        const validFlags = Array.isArray(ex.flag) ? ex.flag : [ex.flag];
        const isCorrect = validFlags.some(f =>
            userFlag.toLowerCase() === f.toLowerCase() ||
            userFlag.toLowerCase().replace(/^flag\{/, '').replace(/\}$/, '') ===
            f.toLowerCase().replace(/^flag\{/, '').replace(/\}$/, '')
        );

        if (isCorrect) {
            result.className = 'flag-result correct';
            result.textContent = `✅ ¡Correcto! Flag verificada.`;
            input.disabled = true;
            input.style.borderColor = 'var(--lab-green)';

            // Auto-complete exercise if not already
            if (!this.exerciseStates[index]?.completed) {
                this.toggleComplete(index);
            }
        } else {
            result.className = 'flag-result incorrect';
            result.textContent = `❌ Flag incorrecta. Intenta de nuevo.`;
            input.style.borderColor = 'var(--lab-red)';
            setTimeout(() => {
                input.style.borderColor = '';
                result.className = 'flag-result';
            }, 2000);
        }
    },

    showHint(index) {
        const hint = document.getElementById(`hint-${index}`);
        hint.classList.toggle('visible');

        // Small XP penalty for using hint
        if (typeof CDPN_Gamification !== 'undefined') {
            // Just track it, no penalty
        }
    },

    copyCode(btn) {
        const pre = btn.closest('.code-block').querySelector('pre');
        const text = pre.textContent;
        navigator.clipboard.writeText(text).then(() => {
            btn.textContent = '✅ Copiado';
            setTimeout(() => btn.textContent = '📋 Copiar', 2000);
        });
    },

    // ===== PROGRESS =====
    updateProgress() {
        const total = this.config.exercises.length;
        const completed = Object.values(this.exerciseStates).filter(s => s.completed).length;
        const percent = Math.round((completed / total) * 100);

        // Calculate earned XP
        let earnedXP = 0;
        this.config.exercises.forEach((ex, i) => {
            if (this.exerciseStates[i]?.completed) earnedXP += ex.xp;
        });

        // Update UI
        document.getElementById('live-xp').textContent = earnedXP;
        document.getElementById('progress-fill').style.width = `${percent}%`;
        document.getElementById('progress-percent').textContent = `${percent}%`;
        document.getElementById('exercises-count').textContent = `${completed} / ${total} completados`;
    },

    updateExerciseCard(index) {
        const card = document.getElementById(`exercise-${index}`);
        const state = this.exerciseStates[index];

        if (state?.completed) {
            card.classList.add('completed');
            card.querySelector('.exercise-checkbox').innerHTML = '✓';
            card.querySelector('.exercise-xp').textContent = '✅';

            const btn = card.querySelector('.complete-exercise-btn');
            btn.textContent = '✅ Ejercicio Completado';
            btn.disabled = true;
        }
    },

    checkLabCompletion() {
        const total = this.config.exercises.length;
        const completed = Object.values(this.exerciseStates).filter(s => s.completed).length;

        if (completed === total) {
            const elapsed = Math.round((Date.now() - this.startTime) / 1000);
            const minutes = Math.floor(elapsed / 60);
            const seconds = elapsed % 60;

            document.getElementById('time-spent').textContent =
                `⏱️ Tiempo: ${minutes}m ${seconds}s`;
            document.getElementById('complete-banner').classList.add('visible');

            // Register completion in gamification
            if (typeof CDPN_Gamification !== 'undefined') {
                CDPN_Gamification.completeLab(
                    this.config.id,
                    elapsed,
                    100
                );
            }

            // Scroll to banner
            document.getElementById('complete-banner').scrollIntoView({
                behavior: 'smooth',
                block: 'center'
            });
        }
    },

    shareResults() {
        const total = this.config.exercises.length;
        const completed = Object.values(this.exerciseStates).filter(s => s.completed).length;
        const elapsed = Math.round((Date.now() - this.startTime) / 1000);
        const minutes = Math.floor(elapsed / 60);

        const text = `🧪 ¡Completé el lab "${this.config.name}"!\n` +
            `✅ ${completed}/${total} ejercicios\n` +
            `⚡ ${this.config.totalXP} XP ganados\n` +
            `⏱️ ${minutes} minutos\n` +
            `🔗 CyberDefense Labs`;

        if (navigator.share) {
            navigator.share({ title: 'Lab Completado', text });
        } else {
            navigator.clipboard.writeText(text).then(() => {
                this.showXPPopup('📋', 'Resultados copiados al portapapeles');
            });
        }
    },

    // ===== XP POPUP =====
    showXPPopup(amount, reason) {
        const popup = document.createElement('div');
        popup.className = 'xp-popup';
        popup.innerHTML = `
            <span class="xp-amount">${amount}</span>
            <span class="xp-reason">${reason}</span>
        `;
        document.body.appendChild(popup);

        requestAnimationFrame(() => {
            popup.classList.add('show');
        });

        setTimeout(() => {
            popup.classList.remove('show');
            setTimeout(() => popup.remove(), 400);
        }, 2500);
    },

    // ===== HELPERS =====
    getDifficultyConfig() {
        const map = {
            fundamentos: { label: 'Fundamentos', icon: '📘' },
            intermedio: { label: 'Intermedio', icon: '🟡' },
            avanzado: { label: 'Avanzado', icon: '🟠' },
            expert: { label: 'Expert', icon: '🔴' }
        };
        return map[this.config.difficulty] || map.intermedio;
    },

    // Reset lab progress
    reset() {
        if (confirm('¿Estás seguro? Se borrará todo el progreso de este lab.')) {
            this.exerciseStates = {};
            this.startTime = Date.now();
            this.saveProgress();
            this.render();
            this.bindEvents();
            this.updateProgress();
        }
    },

    // Bind events after render
    bindEvents() {
        // Auto-open first incomplete exercise
        const firstIncomplete = this.config.exercises.findIndex(
            (_, i) => !this.exerciseStates[i]?.completed
        );
        if (firstIncomplete >= 0) {
            setTimeout(() => this.toggleExercise(firstIncomplete), 500);
        }
    }
};

// Export
if (typeof module !== 'undefined' && module.exports) {
    module.exports = CDPN_LabRunner;
}
