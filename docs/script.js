/* ========================================
   CyberDefense Pro Network - Interactive Scripts
   ======================================== */

document.addEventListener('DOMContentLoaded', () => {

    // ===== Theme Toggle =====
    const themeToggle = document.getElementById('themeToggle');
    if (themeToggle) {
        themeToggle.addEventListener('click', () => {
            document.body.classList.toggle('light-theme');
            const icon = themeToggle.querySelector('i');
            icon.classList.toggle('fa-moon');
            icon.classList.toggle('fa-sun');
        });
    }

    // ===== Typewriter Effect =====
    const commands = [
        'nmap -sV -sC target.com',
        'python3 recon_automatizado.py -d ejemplo.com',
        'docker compose up -d',
        'yara -r rules/ malware.exe',
        'sqlmap -u "http://target.com/?id=1" --dbs',
        'gobuster dir -u http://target.com -w wordlist.txt',
        'volatility -f memory.dump imageinfo',
        'msfconsole -x "use exploit/multi/handler"'
    ];
    let cmdIndex = 0;
    let charIndex = 0;
    let isDeleting = false;
    const typewriter = document.getElementById('typewriter');

    if (typewriter) {
        function typeEffect() {
            const current = commands[cmdIndex];
            if (isDeleting) {
                typewriter.textContent = current.substring(0, charIndex - 1);
                charIndex--;
            } else {
                typewriter.textContent = current.substring(0, charIndex + 1);
                charIndex++;
            }

            let delay = isDeleting ? 30 : 80;

            if (!isDeleting && charIndex === current.length) {
                delay = 2000;
                isDeleting = true;
            } else if (isDeleting && charIndex === 0) {
                isDeleting = false;
                cmdIndex = (cmdIndex + 1) % commands.length;
                delay = 500;
            }

            setTimeout(typeEffect, delay);
        }
        typeEffect();
    }

    // ===== Stats Counter Animation =====
    function animateStats() {
        document.querySelectorAll('.stat-number[data-target]').forEach(stat => {
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

    // ===== Intersection Observer - Show Sections =====
    const sectionObserver = new IntersectionObserver((entries) => {
        entries.forEach(entry => {
            if (entry.isIntersecting) {
                entry.target.classList.add('visible');
                sectionObserver.unobserve(entry.target);
            }
        });
    }, { threshold: 0.05, rootMargin: '0px 0px -20px 0px' });

    document.querySelectorAll('.module-section').forEach(el => {
        sectionObserver.observe(el);
    });

    // Animate hero stats immediately
    const heroObserver = new IntersectionObserver((entries) => {
        entries.forEach(entry => {
            if (entry.isIntersecting) {
                animateStats();
                heroObserver.unobserve(entry.target);
            }
        });
    }, { threshold: 0.3 });

    const heroStats = document.querySelector('.hero-stats');
    if (heroStats) {
        heroObserver.observe(heroStats);
        // Also animate on load
        setTimeout(animateStats, 500);
    }

    // ===== Submodule Toggle =====
    window.toggleSubmodule = function(card) {
        card.classList.toggle('expanded');
    };

    // ===== Smooth Scroll =====
    document.querySelectorAll('a[href^="#"]').forEach(anchor => {
        anchor.addEventListener('click', function(e) {
            e.preventDefault();
            const target = document.querySelector(this.getAttribute('href'));
            if (target) {
                target.scrollIntoView({ behavior: 'smooth', block: 'start' });
            }
        });
    });

    // ===== Navbar Scroll Effect =====
    const navbar = document.querySelector('.navbar');
    if (navbar) {
        window.addEventListener('scroll', () => {
            if (window.scrollY > 50) {
                navbar.style.background = 'rgba(10, 10, 15, 0.98)';
                navbar.style.boxShadow = '0 2px 20px rgba(0, 0, 0, 0.3)';
            } else {
                navbar.style.background = 'rgba(10, 10, 15, 0.92)';
                navbar.style.boxShadow = 'none';
            }
        });
    }

    console.log('🛡️ CyberDefense Pro Network loaded successfully!');
});
