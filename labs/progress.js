/* ========================================
   CDPN Lab Progress Tracker
   Tracks per-exercise progress within labs
   ======================================== */

const CDPN_LabProgress = {
    STORAGE_KEY: 'cdpn_lab_progress',

    // Initialize progress tracking for a specific lab
    init(labId) {
        this.labId = labId;
        this.data = this.loadLabProgress(labId);
        console.log(`📊 Lab progress initialized for: ${labId}`);
        return this;
    },

    // Load progress for a specific lab
    loadLabProgress(labId) {
        try {
            const allProgress = JSON.parse(localStorage.getItem(this.STORAGE_KEY) || '{}');
            return allProgress[labId] || {
                exercises: {},
                startedAt: null,
                completedAt: null,
                totalTime: 0,
                score: 0,
                hintsUsed: 0
            };
        } catch (e) {
            return {
                exercises: {},
                startedAt: null,
                completedAt: null,
                totalTime: 0,
                score: 0,
                hintsUsed: 0
            };
        }
    },

    // Save progress for this lab
    save() {
        try {
            const allProgress = JSON.parse(localStorage.getItem(this.STORAGE_KEY) || '{}');
            allProgress[this.labId] = this.data;
            localStorage.setItem(this.STORAGE_KEY, JSON.stringify(allProgress));
        } catch (e) {
            console.warn('Failed to save lab progress:', e);
        }
    },

    // Mark exercise as started
    startExercise(exerciseNum) {
        if (!this.data.startedAt) {
            this.data.startedAt = Date.now();
        }
        this.data.exercises[exerciseNum] = {
            ...this.data.exercises[exerciseNum],
            started: true,
            startedAt: Date.now()
        };
        this.save();
    },

    // Mark exercise as completed
    completeExercise(exerciseNum, points) {
        this.data.exercises[exerciseNum] = {
            ...this.data.exercises[exerciseNum],
            completed: true,
            completedAt: Date.now(),
            points: points || 0
        };

        // Recalculate score
        this.data.score = Object.values(this.data.exercises)
            .filter(e => e.completed)
            .reduce((sum, e) => sum + (e.points || 0), 0);

        this.save();

        // Check if lab is fully completed
        this.checkLabCompletion();

        // Award XP through main gamification system
        if (typeof CDPN_Gamification !== 'undefined') {
            CDPN_Gamification.addXP(points || 0, `Ejercicio ${exerciseNum} completado`);
        }

        return this.data;
    },

    // Check if all exercises are completed
    checkLabCompletion() {
        const exercises = Object.values(this.data.exercises);
        const allCompleted = exercises.length > 0 && exercises.every(e => e.completed);

        if (allCompleted && !this.data.completedAt) {
            this.data.completedAt = Date.now();
            if (this.data.startedAt) {
                this.data.totalTime = Math.round((this.data.completedAt - this.data.startedAt) / 1000);
            }
            this.save();

            // Award lab completion XP
            if (typeof CDPN_Gamification !== 'undefined') {
                CDPN_Gamification.completeLab(
                    this.labId,
                    this.data.totalTime,
                    this.data.score
                );
            }

            return true;
        }
        return false;
    },

    // Use a hint
    useHint() {
        this.data.hintsUsed++;
        this.save();
        // Small XP penalty or just tracking
        return this.data.hintsUsed;
    },

    // Get progress percentage
    getProgress() {
        const exercises = Object.values(this.data.exercises);
        if (exercises.length === 0) return 0;
        const completed = exercises.filter(e => e.completed).length;
        return Math.round((completed / exercises.length) * 100);
    },

    // Get status object
    getStatus() {
        return {
            labId: this.labId,
            started: !!this.data.startedAt,
            completed: !!this.data.completedAt,
            progress: this.getProgress(),
            score: this.data.score,
            exercises: this.data.exercises,
            hintsUsed: this.data.hintsUsed,
            totalTime: this.data.totalTime
        };
    },

    // Reset this lab's progress
    reset() {
        this.data = {
            exercises: {},
            startedAt: null,
            completedAt: null,
            totalTime: 0,
            score: 0,
            hintsUsed: 0
        };
        this.save();
    },

    // ===== STATIC HELPERS =====

    // Get all lab progress (for the catalog page)
    static getAllProgress() {
        try {
            return JSON.parse(localStorage.getItem('cdpn_lab_progress') || '{}');
        } catch (e) {
            return {};
        }
    },

    // Get summary stats for dashboard
    static getSummary() {
        const all = this.getAllProgress();
        const labs = Object.keys(all);
        const completed = labs.filter(id => all[id].completed);
        const inProgress = labs.filter(id => all[id].started && !all[id].completed);

        return {
            total: labs.length,
            completed: completed.length,
            inProgress: inProgress.length,
            notStarted: 0, // calculated elsewhere
            totalScore: completed.reduce((sum, id) => sum + (all[id].score || 0), 0),
            avgTime: completed.length > 0
                ? Math.round(completed.reduce((sum, id) => sum + (all[id].totalTime || 0), 0) / completed.length)
                : 0
        };
    },

    // Export all progress
    static exportAll() {
        const data = localStorage.getItem('cdpn_lab_progress') || '{}';
        const blob = new Blob([data], { type: 'application/json' });
        const url = URL.createObjectURL(blob);
        const a = document.createElement('a');
        a.href = url;
        a.download = `cdpn-lab-progress-${new Date().toISOString().split('T')[0]}.json`;
        a.click();
        URL.revokeObjectURL(url);
    }
};

// Export
if (typeof module !== 'undefined' && module.exports) {
    module.exports = CDPN_LabProgress;
}
