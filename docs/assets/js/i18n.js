/* ========================================
   CDPN Internationalization (i18n)
   Auto-detect language by browser + IP geolocation
   ======================================== */

const CDPN_i18n = {
    // Supported languages
    supported: ['es', 'en', 'zh', 'pt', 'fr', 'ar', 'ja', 'ko', 'ru', 'de'],

    // Language names for the switcher
    langNames: {
        es: 'Español',
        en: 'English',
        zh: '中文',
        pt: 'Português',
        fr: 'Français',
        ar: 'العربية',
        ja: '日本語',
        ko: '한국어',
        ru: 'Русский',
        de: 'Deutsch'
    },

    // Country → Language mapping (fallback)
    countryLang: {
        CN: 'zh', TW: 'zh', HK: 'zh', MO: 'zh',
        US: 'en', GB: 'en', AU: 'en', CA: 'en', NZ: 'en', IE: 'en',
        BR: 'pt', AO: 'pt', MZ: 'pt', CV: 'pt',
        FR: 'fr', BE: 'fr', CH: 'fr', LU: 'fr', MC: 'fr',
        SA: 'ar', AE: 'ar', EG: 'ar', MA: 'ar', IQ: 'ar',
        JP: 'ja',
        KR: 'ko',
        RU: 'ru', BY: 'ru', KZ: 'ru',
        DE: 'at', AT: 'de', LI: 'de',
        MX: 'es', ES: 'es', AR: 'es', CO: 'es', CL: 'es',
        PE: 'es', VE: 'es', EC: 'es', GT: 'es', CU: 'es',
        BO: 'es', DO: 'es', HN: 'es', PY: 'es', SV: 'es',
        NI: 'es', CR: 'es', PA: 'es', UY: 'es', PR: 'es'
    },

    // Current language
    current: 'es',

    // Translation keys → translations
    translations: null,

    /**
     * Initialize the i18n system
     */
    async init() {
        // 1. Check localStorage for saved preference
        const saved = localStorage.getItem('cdpn-lang');
        if (saved && this.supported.includes(saved)) {
            this.current = saved;
            await this.loadTranslations();
            this.applyAll();
            return;
        }

        // 2. Detect from browser language
        const browserLang = this.detectBrowserLang();

        // 3. Detect from IP geolocation (async)
        const countryLang = await this.detectCountryLang();

        // Priority: browser lang if supported, else country lang, else 'es'
        if (browserLang && this.supported.includes(browserLang)) {
            this.current = browserLang;
        } else if (countryLang && this.supported.includes(countryLang)) {
            this.current = countryLang;
        } else {
            this.current = 'es';
        }

        // Load and apply
        await this.loadTranslations();
        this.applyAll();
        this.updateSwitcherUI();

        console.log(`🌍 CDPN i18n: Detected language → ${this.current}`);
    },

    /**
     * Detect language from browser settings
     */
    detectBrowserLang() {
        const lang = navigator.language || navigator.userLanguage || '';
        // Extract base language (e.g., "zh-CN" → "zh", "en-US" → "en")
        return lang.split('-')[0].toLowerCase();
    },

    /**
     * Detect country from IP using free API
     */
    async detectCountryLang() {
        try {
            // Use ip-api.com (free, no key needed, 45 req/min)
            const res = await fetch('https://ipapi.co/json/', { signal: AbortSignal.timeout(3000) });
            if (!res.ok) return null;
            const data = await res.json();
            const country = data.country_code;
            if (country) {
                localStorage.setItem('cdpn-country', country);
                return this.countryLang[country] || null;
            }
        } catch (e) {
            // Silently fail — network might be blocked
            console.log('🌍 i18n: Geolocation API unavailable, using browser language');
        }
        return null;
    },

    /**
     * Load translations file
     */
    async loadTranslations() {
        if (this.translations) return;
        try {
            const base = this.getBasePath();
            const res = await fetch(`${base}assets/i18n/translations.json`);
            if (res.ok) {
                this.translations = await res.json();
            }
        } catch (e) {
            console.warn('🌍 i18n: translations.json not found, using data attributes only');
            this.translations = {};
        }
    },

    /**
     * Get base path for GitHub Pages
     */
    getBasePath() {
        const path = window.location.pathname;
        // If inside /modules/*, go up two levels
        if (path.includes('/modules/')) return '../../';
        // If in docs root
        return '';
    },

    /**
     * Apply translations to all elements with data-i18n
     */
    applyAll() {
        if (!this.translations) return;
        const dict = this.translations[this.current] || this.translations['es'] || {};

        // Text content
        document.querySelectorAll('[data-i18n]').forEach(el => {
            const key = el.getAttribute('data-i18n');
            if (dict[key]) {
                el.textContent = dict[key];
            }
        });

        // HTML content (for elements with links inside)
        document.querySelectorAll('[data-i18n-html]').forEach(el => {
            const key = el.getAttribute('data-i18n-html');
            if (dict[key]) {
                el.innerHTML = dict[key];
            }
        });

        // Placeholders
        document.querySelectorAll('[data-i18n-placeholder]').forEach(el => {
            const key = el.getAttribute('data-i18n-placeholder');
            if (dict[key]) {
                el.placeholder = dict[key];
            }
        });

        // Page title
        if (dict._pageTitle) {
            document.title = dict._pageTitle;
        }

        // Update lang attribute
        document.documentElement.lang = this.current;

        // Update switcher UI
        this.updateSwitcherUI();
    },

    /**
     * Switch language manually
     */
    async set(lang) {
        if (!this.supported.includes(lang)) return;
        this.current = lang;
        localStorage.setItem('cdpn-lang', lang);
        await this.loadTranslations();
        this.applyAll();
    },

    /**
     * Update the language switcher UI
     */
    updateSwitcherUI() {
        const btn = document.getElementById('langToggle');
        if (btn) {
            const flag = this.getFlag(this.current);
            const name = this.langNames[this.current] || this.current;
            btn.innerHTML = `<span class="lang-flag">${flag}</span> <span class="lang-name">${name}</span>`;
        }
        // Update active state in dropdown
        const dropdown = document.getElementById('langDropdown');
        if (dropdown) {
            dropdown.querySelectorAll('button[data-lang]').forEach(b => {
                b.classList.toggle('active-lang', b.dataset.lang === this.current);
            });
        }
    },

    /**
     * Get emoji flag for language
     */
    getFlag(lang) {
        const flags = {
            es: '🇪🇸', en: '🇺🇸', zh: '🇨🇳', pt: '🇧🇷',
            fr: '🇫🇷', ar: '🇸🇦', ja: '🇯🇵', ko: '🇰🇷',
            ru: '🇷🇺', de: '🇩🇪'
        };
        return flags[lang] || '🌐';
    }
};

// Auto-initialize on DOM ready
document.addEventListener('DOMContentLoaded', () => {
    CDPN_i18n.init();
});
