/* ========================================
   CDPN Shared JavaScript — Theme, Navbar, Typewriter
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

    // ===== Typewriter Effect =====
    const typewriter = document.getElementById('typewriter');
    if (typewriter) {
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
        let cmdIndex = 0, charIndex = 0, isDeleting = false;

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
                delay = 2000; isDeleting = true;
            } else if (isDeleting && charIndex === 0) {
                isDeleting = false;
                cmdIndex = (cmdIndex + 1) % commands.length;
                delay = 500;
            }
            setTimeout(typeEffect, delay);
        }
        typeEffect();
    }

    // ===== Submodule Toggle =====
    window.toggleSubmodule = function(card) {
        card.classList.toggle('expanded');
    };

    // ===== Smooth Scroll =====
    document.querySelectorAll('a[href^="#"]').forEach(anchor => {
        anchor.addEventListener('click', function(e) {
            const target = document.querySelector(this.getAttribute('href'));
            if (target) {
                e.preventDefault();
                target.scrollIntoView({ behavior: 'smooth', block: 'start' });
            }
        });
    });

    // ===== Language Switcher (a11y-enhanced) =====
    const langSwitcher = document.getElementById('langSwitcher');
    const langToggle = document.getElementById('langToggle');
    const langDropdown = document.getElementById('langDropdown');
    if (langSwitcher && langToggle && langDropdown) {
        const setLangOpen = (open) => {
            langSwitcher.classList.toggle('open', open);
            langToggle.setAttribute('aria-expanded', String(open));
            langDropdown.hidden = !open;
            // Update aria-label to reflect current state
            const currentLang = (typeof CDPN_i18n !== 'undefined' && CDPN_i18n.current) || 'es';
            const langName = langToggle.querySelector('.lang-name');
            const label = `Cambiar idioma. Idioma actual: ${langName ? langName.textContent.trim() : currentLang}`;
            langToggle.setAttribute('aria-label', label);
            if (open) {
                // Focus the currently-active language option
                const activeBtn = langDropdown.querySelector(`button[data-lang="${currentLang}"]`)
                    || langDropdown.querySelector('button[data-lang]');
                if (activeBtn) activeBtn.focus();
            }
        };

        // Toggle dropdown
        langToggle.addEventListener('click', (e) => {
            e.stopPropagation();
            setLangOpen(!langSwitcher.classList.contains('open'));
        });

        // Close on outside click
        document.addEventListener('click', (e) => {
            if (!langSwitcher.contains(e.target)) setLangOpen(false);
        });

        // Close on Escape
        document.addEventListener('keydown', (e) => {
            if (e.key === 'Escape' && langSwitcher.classList.contains('open')) {
                setLangOpen(false);
                langToggle.focus();
            }
        });

        // Handle language selection
        langDropdown.querySelectorAll('button[data-lang]').forEach(btn => {
            btn.addEventListener('click', () => {
                const lang = btn.dataset.lang;
                if (typeof CDPN_i18n !== 'undefined') {
                    CDPN_i18n.set(lang);
                    announce(lang);
                }
                setLangOpen(false);
                langToggle.focus();
            });
        });

        // Highlight current language
        function updateActiveLang() {
            const currentLang = typeof CDPN_i18n !== 'undefined' ? CDPN_i18n.current : 'es';
            langDropdown.querySelectorAll('button[data-lang]').forEach(btn => {
                const isActive = btn.dataset.lang === currentLang;
                btn.classList.toggle('active-lang', isActive);
                btn.setAttribute('aria-selected', String(isActive));
            });
        }
        setInterval(updateActiveLang, 500);
    }

    // ===== Live region for SR announcements =====
    function announce(msg) {
        let live = document.getElementById('cdpn-live');
        if (!live) {
            live = document.createElement('div');
            live.id = 'cdpn-live';
            live.setAttribute('aria-live', 'polite');
            live.setAttribute('aria-atomic', 'true');
            live.className = 'sr-only';
            document.body.appendChild(live);
        }
        live.textContent = msg;
    }


});
