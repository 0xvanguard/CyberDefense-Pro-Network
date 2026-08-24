/* ========================================
   CDPN AI Security Lab Tracker
   Bridges AI Security labs with gamification
   ======================================== */

const CDPN_AISecurityTracker = {
    STORAGE_KEY: 'cdpn_lab_progress',
    
    // Lab configurations
    LABS: {
        'prompt-injection-01': { name: 'Prompt-Injection-01', icon: '💉', xp: 350, totalQuestions: 8 },
        'jailbreak-01': { name: 'Jailbreak-01', icon: '🔓', xp: 400, totalQuestions: 10 },
        'red-teaming-01': { name: 'Red-Teaming-01', icon: '🎯', xp: 400, totalQuestions: 10 }
    },

    /**
     * Record an exercise answer for an AI Security lab
     * @param {string} labId - e.g. 'prompt-injection-01'
     * @param {string} questionId - e.g. 'q1'
     * @param {number} points - XP for this question
     * @param {boolean} isCorrect - Whether the answer was correct
     */
    recordAnswer(labId, questionId, points, isCorrect) {
        if (!isCorrect) return;

        const allProgress = this.getAllProgress();
        if (!allProgress[labId]) {
            allProgress[labId] = {
                exercises: {},
                startedAt: Date.now(),
                completedAt: null,
                totalTime: 0,
                score: 0,
                hintsUsed: 0
            };
        }

        const lab = allProgress[labId];
        lab.exercises[questionId] = {
            completed: true,
            completedAt: Date.now(),
            points: points
        };

        // Recalculate score
        lab.score = Object.values(lab.exercises)
            .filter(e => e.completed)
            .reduce((sum, e) => sum + (e.points || 0), 0);

        this.saveAllProgress(allProgress);

        // Award XP through gamification system
        if (typeof CDPN_Gamification !== 'undefined') {
            CDPN_Gamification.addXP(points, `${labId} — ${questionId}`);
        }

        // Check if lab is fully completed
        this.checkLabCompletion(labId, allProgress);

        return lab;
    },

    /**
     * Check if all questions in a lab are answered and trigger completion
     */
    checkLabCompletion(labId, allProgress) {
        const labConfig = this.LABS[labId];
        if (!labConfig) return;

        const lab = allProgress[labId];
        if (!lab || lab.completedAt) return;

        const completedCount = Object.values(lab.exercises).filter(e => e.completed).length;
        if (completedCount >= labConfig.totalQuestions) {
            lab.completedAt = Date.now();
            if (lab.startedAt) {
                lab.totalTime = Math.round((lab.completedAt - lab.startedAt) / 1000);
            }
            this.saveAllProgress(allProgress);

            // Register completion in gamification
            if (typeof CDPN_Gamification !== 'undefined') {
                CDPN_Gamification.completeLab(labId, lab.totalTime, 100);
            }
        }
    },

    /**
     * Get all AI Security lab progress
     */
    getAllProgress() {
        try {
            return JSON.parse(localStorage.getItem(this.STORAGE_KEY) || '{}');
        } catch (e) {
            return {};
        }
    },

    /**
     * Save all progress
     */
    saveAllProgress(data) {
        try {
            localStorage.setItem(this.STORAGE_KEY, JSON.stringify(data));
        } catch (e) {
            console.warn('Failed to save lab progress:', e);
        }
    },

    /**
     * Get progress percentage for a specific lab
     */
    getLabProgress(labId) {
        const all = this.getAllProgress();
        const lab = all[labId];
        const config = this.LABS[labId];
        if (!lab || !config) return 0;
        
        const completed = Object.values(lab.exercises).filter(e => e.completed).length;
        return Math.round((completed / config.totalQuestions) * 100);
    },

    /**
     * Get summary stats for all AI Security labs
     */
    getSummary() {
        const all = this.getAllProgress();
        let totalCompleted = 0;
        let totalXP = 0;
        let labsCompleted = 0;
        const labStats = {};

        for (const [labId, config] of Object.entries(this.LABS)) {
            const lab = all[labId];
            const completed = lab ? Object.values(lab.exercises).filter(e => e.completed).length : 0;
            const score = lab ? lab.score : 0;
            const isComplete = lab && lab.completedAt;

            labStats[labId] = {
                name: config.name,
                icon: config.icon,
                totalXP: config.xp,
                questionsAnswered: completed,
                totalQuestions: config.totalQuestions,
                score: score,
                progress: Math.round((completed / config.totalQuestions) * 100),
                completed: !!isComplete
            };

            totalCompleted += completed;
            totalXP += score;
            if (isComplete) labsCompleted++;
        }

        return {
            labs: labStats,
            totalLabs: Object.keys(this.LABS).length,
            labsCompleted: labsCompleted,
            totalQuestions: Object.values(this.LABS).reduce((s, c) => s + c.totalQuestions, 0),
            questionsAnswered: totalCompleted,
            totalXPEarned: totalXP
        };
    },

    /**
     * Update gamification stats with AI Security data
     */
    syncToGamification() {
        if (typeof CDPN_Gamification === 'undefined') return;

        const summary = this.getSummary();
        CDPN_Gamification.data.stats.aiLabsCompleted = summary.labsCompleted;
        CDPN_Gamification.data.stats.aiLabs = {
            completed: {}
        };
        
        for (const [labId, stats] of Object.entries(summary.labs)) {
            CDPN_Gamification.data.stats.aiLabs.completed[labId] = stats.progress;
        }
        
        CDPN_Gamification.data.stats.badges = CDPN_Gamification.data.badges;
        CDPN_Gamification.saveData();
        CDPN_Gamification.checkBadges();
    }
};

// Initialize on DOM ready
document.addEventListener('DOMContentLoaded', () => {
    if (typeof CDPN_Gamification !== 'undefined') {
        CDPN_Gamification.init();
        CDPN_AISecurityTracker.syncToGamification();
    }
});
