/* ========================================
   CDPN Gamification System
   XP, Badges, Progress, Leaderboard
   ======================================== */

const CDPN_Gamification = {
    // Storage key
    STORAGE_KEY: 'cdpn_gamification',
    
    // XP values for different actions
    XP_VALUES: {
        // Labs
        LAB_COMPLETED: 200,
        LAB_STARTED: 25,
        EXERCISE_COMPLETED: 50,
        
        // Learning
        MODULE_COMPLETED: 150,
        VIDEO_WATCHED: 30,
        ARTICLE_READ: 20,
        
        // Community
        WRITEUP_SHARED: 100,
        ANSWER_GIVEN: 50,
        EVENT_ATTENDED: 150,
        
        // Daily
        DAILY_LOGIN: 10,
        STREAK_BONUS: 5, // per day streak
        
        // Achievements
        FIRST_LAB: 50,
        FIRST_WRITEUP: 75,
        STREAK_7_DAYS: 200,
        STREAK_30_DAYS: 1000
    },
    
    // Badge definitions
    BADGES: {
        // Labs
        'first-lab': {
            name: 'Primer Lab',
            icon: '🎯',
            description: 'Completaste tu primer lab',
            xp: 50,
            condition: (stats) => stats.labsCompleted >= 1
        },
        'lab-master-5': {
            name: 'Lab Enthusiast',
            icon: '🔬',
            description: 'Completaste 5 labs',
            xp: 150,
            condition: (stats) => stats.labsCompleted >= 5
        },
        'lab-master-10': {
            name: 'Lab Expert',
            icon: '🏆',
            description: 'Completaste 10 labs',
            xp: 300,
            condition: (stats) => stats.labsCompleted >= 10
        },
        'lab-master-16': {
            name: 'Lab Legend',
            icon: '👑',
            description: 'Completaste todos los labs',
            xp: 500,
            condition: (stats) => stats.labsCompleted >= 16
        },
        
        // Streaks
        'streak-3': {
            name: 'En Racha',
            icon: '🔥',
            description: '3 días consecutivos',
            xp: 50,
            condition: (stats) => stats.streak >= 3
        },
        'streak-7': {
            name: 'Semana Perfecta',
            icon: '⚡',
            description: '7 días consecutivos',
            xp: 200,
            condition: (stats) => stats.streak >= 7
        },
        'streak-30': {
            name: 'Mes Imparable',
            icon: '💎',
            description: '30 días consecutivos',
            xp: 1000,
            condition: (stats) => stats.streak >= 30
        },
        
        // Writeups
        'first-writeup': {
            name: 'Primer Writeup',
            icon: '📝',
            description: 'Compartiste tu primer writeup',
            xp: 75,
            condition: (stats) => stats.writeupsShared >= 1
        },
        'writeup-master': {
            name: 'Writeup Master',
            icon: '📚',
            description: 'Compartiste 10 writeups',
            xp: 300,
            condition: (stats) => stats.writeupsShared >= 10
        },
        
        // Community
        'helper': {
            name: 'Ayudante',
            icon: '🤝',
            description: 'Respondiste 10 preguntas',
            xp: 100,
            condition: (stats) => stats.answersGiven >= 10
        },
        'mentor': {
            name: 'Mentor',
            icon: '🎓',
            description: 'Respondiste 50 preguntas',
            xp: 500,
            condition: (stats) => stats.answersGiven >= 50
        },
        
        // Levels
        'level-5': {
            name: 'Bronze',
            icon: '🥉',
            description: 'Alcanzaste nivel 5',
            xp: 100,
            condition: (stats) => stats.level >= 5
        },
        'level-10': {
            name: 'Silver',
            icon: '🥈',
            description: 'Alcanzaste nivel 10',
            xp: 200,
            condition: (stats) => stats.level >= 10
        },
        'level-20': {
            name: 'Gold',
            icon: '🥇',
            description: 'Alcanzaste nivel 20',
            xp: 400,
            condition: (stats) => stats.level >= 20
        },
        'level-30': {
            name: 'Diamond',
            icon: '💎',
            description: 'Alcanzaste nivel 30',
            xp: 800,
            condition: (stats) => stats.level >= 30
        },
        'level-50': {
            name: 'Legend',
            icon: '🌟',
            description: 'Alcanzaste nivel 50',
            xp: 2000,
            condition: (stats) => stats.level >= 50
        },
        
        // Special
        'night-owl': {
            name: 'Búho Nocturno',
            icon: '🦉',
            description: 'Completaste un lab después de medianoche',
            xp: 50,
            condition: (stats) => stats.nightOwl
        },
        'speed-demon': {
            name: 'Velocista',
            icon: '⚡',
            description: 'Completaste un lab en menos de 30 min',
            xp: 100,
            condition: (stats) => stats.speedRun
        },
        'perfectionist': {
            name: 'Perfeccionista',
            icon: '✨',
            description: 'Obtuviste 100% en un lab',
            xp: 150,
            condition: (stats) => stats.perfectScore
        }
    },
    
    // Level thresholds
    LEVELS: [
        0, 100, 250, 500, 1000, 1500, 2000, 3000, 4000, 5000,
        6500, 8000, 10000, 12500, 15000, 18000, 21000, 25000, 30000, 35000,
        40000, 46000, 52000, 60000, 70000, 80000, 95000, 110000, 130000, 150000
    ],
    
    // Initialize
    init() {
        this.data = this.loadData();
        this.updateStreak();
        this.checkBadges();
        console.log('🎮 CDPN Gamification initialized');
    },
    
    // Load data from localStorage
    loadData() {
        try {
            const saved = localStorage.getItem(this.STORAGE_KEY);
            if (saved) {
                return JSON.parse(saved);
            }
        } catch (e) {
            console.warn('Failed to load gamification data:', e);
        }
        
        // Default data
        return {
            xp: 0,
            level: 1,
            streak: 0,
            lastLogin: null,
            labsCompleted: [],
            modulesCompleted: [],
            writeupsShared: 0,
            answersGiven: 0,
            badges: [],
            stats: {
                labsCompleted: 0,
                writeupsShared: 0,
                answersGiven: 0,
                nightOwl: false,
                speedRun: false,
                perfectScore: false
            },
            history: []
        };
    },
    
    // Save data to localStorage
    saveData() {
        try {
            localStorage.setItem(this.STORAGE_KEY, JSON.stringify(this.data));
        } catch (e) {
            console.warn('Failed to save gamification data:', e);
        }
    },
    
    // Add XP
    addXP(amount, reason) {
        const oldLevel = this.getLevel();
        this.data.xp += amount;
        const newLevel = this.getLevel();
        this.data.level = newLevel;
        
        // Add to history
        this.data.history.push({
            type: 'xp',
            amount: amount,
            reason: reason,
            timestamp: Date.now()
        });
        
        this.saveData();
        this.checkBadges();
        
        // Show notification
        this.showNotification(`+${amount} XP`, reason);
        
        // Level up notification
        if (newLevel > oldLevel) {
            setTimeout(() => {
                this.showNotification(`🎉 ¡NIVEL ${newLevel}!`, 'Has subido de nivel');
            }, 1000);
        }
        
        return { xp: this.data.xp, level: newLevel, leveledUp: newLevel > oldLevel };
    },
    
    // Get current level
    getLevel() {
        let level = 1;
        for (let i = 1; i < this.LEVELS.length; i++) {
            if (this.data.xp >= this.LEVELS[i]) {
                level = i + 1;
            } else {
                break;
            }
        }
        return level;
    },
    
    // Get XP for next level
    getXPForNextLevel() {
        const currentLevel = this.getLevel();
        if (currentLevel >= this.LEVELS.length) {
            return this.data.xp;
        }
        return this.LEVELS[currentLevel] - this.data.xp;
    },
    
    // Get progress to next level (0-100)
    getLevelProgress() {
        const currentLevel = this.getLevel();
        if (currentLevel >= this.LEVELS.length) {
            return 100;
        }
        const currentThreshold = this.LEVELS[currentLevel - 1];
        const nextThreshold = this.LEVELS[currentLevel];
        const progress = ((this.data.xp - currentThreshold) / (nextThreshold - currentThreshold)) * 100;
        return Math.min(100, Math.max(0, progress));
    },
    
    // Update streak
    updateStreak() {
        const today = new Date().toDateString();
        const lastLogin = this.data.lastLogin;
        
        if (!lastLogin) {
            // First login
            this.data.streak = 1;
        } else if (lastLogin === today) {
            // Already logged in today
            return;
        } else {
            const lastDate = new Date(lastLogin);
            const todayDate = new Date(today);
            const diffDays = Math.floor((todayDate - lastDate) / (1000 * 60 * 60 * 24));
            
            if (diffDays === 1) {
                // Consecutive day
                this.data.streak++;
            } else if (diffDays > 1) {
                // Streak broken
                this.data.streak = 1;
            }
        }
        
        this.data.lastLogin = today;
        this.saveData();
        
        // Check streak badges
        if (this.data.streak >= 7 && !this.data.badges.includes('streak-7')) {
            this.addXP(this.XP_VALUES.STREAK_7_DAYS, 'Racha de 7 días');
        }
        if (this.data.streak >= 30 && !this.data.badges.includes('streak-30')) {
            this.addXP(this.XP_VALUES.STREAK_30_DAYS, 'Racha de 30 días');
        }
    },
    
    // Complete a lab
    completeLab(labId, timeSpent, score) {
        if (!this.data.labsCompleted.includes(labId)) {
            this.data.labsCompleted.push(labId);
            this.data.stats.labsCompleted = this.data.labsCompleted.length;
            
            // Add XP
            this.addXP(this.XP_VALUES.LAB_COMPLETED, `Lab completado: ${labId}`);
            
            // Check achievements
            if (this.data.labsCompleted.length === 1) {
                this.addXP(this.XP_VALUES.FIRST_LAB, 'Primer lab completado');
            }
            
            // Night owl check
            const hour = new Date().getHours();
            if (hour >= 0 && hour < 6) {
                this.data.stats.nightOwl = true;
            }
            
            // Speed run check
            if (timeSpent < 30 * 60) { // less than 30 minutes in seconds
                this.data.stats.speedRun = true;
            }
            
            // Perfect score check
            if (score === 100) {
                this.data.stats.perfectScore = true;
            }
            
            this.saveData();
            this.checkBadges();
        }
    },
    
    // Complete a module
    completeModule(moduleId) {
        if (!this.data.modulesCompleted.includes(moduleId)) {
            this.data.modulesCompleted.push(moduleId);
            this.addXP(this.XP_VALUES.MODULE_COMPLETED, `Módulo completado: ${moduleId}`);
            this.saveData();
        }
    },
    
    // Share a writeup
    shareWriteup() {
        this.data.writeupsShared++;
        this.data.stats.writeupsShared = this.data.writeupsShared;
        this.addXP(this.XP_VALUES.WRITEUP_SHARED, 'Writeup compartido');
        this.saveData();
        this.checkBadges();
    },
    
    // Give an answer
    giveAnswer() {
        this.data.answersGiven++;
        this.data.stats.answersGiven = this.data.answersGiven;
        this.addXP(this.XP_VALUES.ANSWER_GIVEN, 'Pregunta respondida');
        this.saveData();
        this.checkBadges();
    },
    
    // Watch a video
    watchVideo(videoId) {
        this.addXP(this.XP_VALUES.VIDEO_WATCHED, `Video visto: ${videoId}`);
    },
    
    // Read an article
    readArticle(articleId) {
        this.addXP(this.XP_VALUES.ARTICLE_READ, `Artículo leído: ${articleId}`);
    },
    
    // Check and award badges
    checkBadges() {
        let newBadges = [];
        
        for (const [badgeId, badge] of Object.entries(this.BADGES)) {
            if (!this.data.badges.includes(badgeId) && badge.condition(this.data.stats)) {
                this.data.badges.push(badgeId);
                newBadges.push(badge);
                
                // Add badge XP
                if (badge.xp > 0) {
                    this.addXP(badge.xp, `Badge desbloqueado: ${badge.name}`);
                }
                
                // Show notification
                this.showBadgeNotification(badge);
            }
        }
        
        this.saveData();
        return newBadges;
    },
    
    // Get rank based on XP
    getRank() {
        const xp = this.data.xp;
        if (xp >= 100000) return { name: 'Legend', icon: '🌟', color: '#ffd700' };
        if (xp >= 50000) return { name: 'Diamond', icon: '💎', color: '#b9f2ff' };
        if (xp >= 20000) return { name: 'Gold', icon: '🥇', color: '#ffd700' };
        if (xp >= 10000) return { name: 'Silver', icon: '🥈', color: '#c0c0c0' };
        if (xp >= 5000) return { name: 'Bronze', icon: '🥉', color: '#cd7f32' };
        return { name: 'Newcomer', icon: '🌱', color: '#2ecc71' };
    },
    
    // Get stats summary
    getStats() {
        return {
            xp: this.data.xp,
            level: this.getLevel(),
            rank: this.getRank(),
            streak: this.data.streak,
            labsCompleted: this.data.stats.labsCompleted,
            writeupsShared: this.data.stats.writeupsShared,
            answersGiven: this.data.stats.answersGiven,
            badges: this.data.badges.length,
            totalBadges: Object.keys(this.BADGES).length,
            levelProgress: this.getLevelProgress(),
            xpForNextLevel: this.getXPForNextLevel()
        };
    },
    
    // Show notification
    showNotification(title, message) {
        const notification = document.createElement('div');
        notification.className = 'gamification-notification';
        notification.innerHTML = `
            <div class="notification-title">${title}</div>
            <div class="notification-message">${message}</div>
        `;
        document.body.appendChild(notification);
        
        // Animate in
        setTimeout(() => notification.classList.add('show'), 10);
        
        // Remove after 3 seconds
        setTimeout(() => {
            notification.classList.remove('show');
            setTimeout(() => notification.remove(), 300);
        }, 3000);
    },
    
    // Show badge notification
    showBadgeNotification(badge) {
        const notification = document.createElement('div');
        notification.className = 'badge-notification';
        notification.innerHTML = `
            <div class="badge-icon">${badge.icon}</div>
            <div class="badge-info">
                <div class="badge-title">¡Badge Desbloqueado!</div>
                <div class="badge-name">${badge.name}</div>
                <div class="badge-description">${badge.description}</div>
            </div>
        `;
        document.body.appendChild(notification);
        
        // Animate in
        setTimeout(() => notification.classList.add('show'), 10);
        
        // Remove after 4 seconds
        setTimeout(() => {
            notification.classList.remove('show');
            setTimeout(() => notification.remove(), 300);
        }, 4000);
    },
    
    // Reset progress (for testing)
    resetProgress() {
        if (confirm('¿Estás seguro de que quieres resetear todo tu progreso?')) {
            localStorage.removeItem(this.STORAGE_KEY);
            this.data = this.loadData();
            this.showNotification('Progreso reseteado', 'Todos los datos han sido eliminados');
        }
    },
    
    // Export data
    exportData() {
        const dataStr = JSON.stringify(this.data, null, 2);
        const blob = new Blob([dataStr], { type: 'application/json' });
        const url = URL.createObjectURL(blob);
        const a = document.createElement('a');
        a.href = url;
        a.download = `cdpn-progress-${new Date().toISOString().split('T')[0]}.json`;
        a.click();
        URL.revokeObjectURL(url);
    },
    
    // Import data
    importData(file) {
        const reader = new FileReader();
        reader.onload = (e) => {
            try {
                const imported = JSON.parse(e.target.result);
                this.data = imported;
                this.saveData();
                this.showNotification('Progreso importado', 'Tus datos han sido restaurados');
            } catch (err) {
                this.showNotification('Error', 'No se pudo importar el archivo');
            }
        };
        reader.readAsText(file);
    }
};

// Initialize on DOM ready
document.addEventListener('DOMContentLoaded', () => {
    CDPN_Gamification.init();
});

// Export for use in other scripts
if (typeof module !== 'undefined' && module.exports) {
    module.exports = CDPN_Gamification;
}
