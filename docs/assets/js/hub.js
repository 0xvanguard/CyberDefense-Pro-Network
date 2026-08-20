/* ========================================
   CDPN Hub JavaScript — Stats Animation, IntersectionObserver
   ======================================== */
document.addEventListener('DOMContentLoaded', () => {

    // ===== Stats Counter Animation =====
    function animateStats() {
        document.querySelectorAll('.hub-stat-num[data-target]').forEach(stat => {
            if (stat.dataset.animated) return;
            stat.dataset.animated = 'true';
            const target = parseInt(stat.getAttribute('data-target'));
            const duration = 2000;
            const step = target / (duration / 16);
            let current = 0;
            const timer = setInterval(() => {
                current += step;
                if (current >= target) {
                    stat.textContent = target + '+';
                    clearInterval(timer);
                } else {
                    stat.textContent = Math.floor(current);
                }
            }, 16);
        });
    }

    // ===== Intersection Observer for Cards =====
    const cardObserver = new IntersectionObserver((entries) => {
        entries.forEach(entry => {
            if (entry.isIntersecting) {
                entry.target.style.opacity = '1';
                entry.target.style.transform = 'translateY(0)';
                cardObserver.unobserve(entry.target);
            }
        });
    }, { threshold: 0.1 });

    document.querySelectorAll('.module-card').forEach((card, i) => {
        card.style.opacity = '0';
        card.style.transform = 'translateY(20px)';
        card.style.transition = `opacity 0.5s ease ${i * 0.08}s, transform 0.5s ease ${i * 0.08}s`;
        cardObserver.observe(card);
    });

    // Animate stats when visible
    const statsSection = document.querySelector('.hub-stats');
    if (statsSection) {
        const statsObserver = new IntersectionObserver((entries) => {
            entries.forEach(entry => {
                if (entry.isIntersecting) {
                    animateStats();
                    statsObserver.unobserve(entry.target);
                }
            });
        }, { threshold: 0.3 });
        statsObserver.observe(statsSection);
        setTimeout(animateStats, 800);
    }

    console.log('🛡️ CDPN hub.js loaded');
});
