document.addEventListener('DOMContentLoaded', () => {
    // 1. Set current year in footer
    const currentYearSpan = document.getElementById('current-year');
    if (currentYearSpan) {
        currentYearSpan.textContent = new Date().getFullYear();
    }

    // 2. Sticky Header Scroll Effect
    const header = document.getElementById('header');
    window.addEventListener('scroll', () => {
        if (window.scrollY > 50) {
            header.classList.add('scrolled');
        } else {
            header.classList.remove('scrolled');
        }
    });

    // 3. Mobile Menu Toggle
    const mobileMenuToggle = document.querySelector('.mobile-menu-toggle');
    const primaryNav = document.getElementById('primary-nav');

    if (mobileMenuToggle && primaryNav) {
        mobileMenuToggle.addEventListener('click', () => {
            const isExpanded = mobileMenuToggle.getAttribute('aria-expanded') === 'true';
            mobileMenuToggle.setAttribute('aria-expanded', !isExpanded);
            primaryNav.classList.toggle('is-open');
        });

        // Close menu when clicking a link
        const navLinks = primaryNav.querySelectorAll('a');
        navLinks.forEach(link => {
            link.addEventListener('click', () => {
                mobileMenuToggle.setAttribute('aria-expanded', 'false');
                primaryNav.classList.remove('is-open');
            });
        });
    }

    // 4. Form Validation with Accessibility
    const setupFormValidation = (formId) => {
        const form = document.getElementById(formId);
        if (!form) return;

        form.addEventListener('submit', (e) => {
            e.preventDefault();
            let isValid = true;
            const inputs = form.querySelectorAll('input[required], textarea[required]');

            inputs.forEach(input => {
                const formGroup = input.closest('.form-group');
                const errorId = `${input.id}-error`;
                const errorElement = document.getElementById(errorId);

                // Basic validation logic
                let isInputValid = true;
                if (input.type === 'checkbox') {
                    isInputValid = input.checked;
                } else if (input.type === 'email') {
                    const emailRegex = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
                    isInputValid = emailRegex.test(input.value);
                } else {
                    isInputValid = input.value.trim() !== '';
                }

                if (!isInputValid) {
                    isValid = false;
                    formGroup.classList.add('has-error');
                    input.setAttribute('aria-invalid', 'true');
                    input.setAttribute('aria-describedby', errorId);
                } else {
                    formGroup.classList.remove('has-error');
                    input.removeAttribute('aria-invalid');
                    input.removeAttribute('aria-describedby');
                }
            });

            if (isValid) {
                // Simulate form submission
                const submitBtn = form.querySelector('button[type="submit"]');
                const originalText = submitBtn.textContent;
                submitBtn.textContent = 'Enviando...';
                submitBtn.disabled = true;

                setTimeout(() => {
                    alert('Formulario enviado con éxito. Gracias por contactarnos.');
                    form.reset();
                    submitBtn.textContent = originalText;
                    submitBtn.disabled = false;
                }, 1500);
            } else {
                // Focus the first invalid field for accessibility
                const firstInvalid = form.querySelector('[aria-invalid="true"]');
                if (firstInvalid) firstInvalid.focus();
            }
        });

        // Remove error state on input
        form.addEventListener('input', (e) => {
            if (e.target.required) {
                const formGroup = e.target.closest('.form-group');
                formGroup.classList.remove('has-error');
                e.target.removeAttribute('aria-invalid');
                e.target.removeAttribute('aria-describedby');
            }
        });
    };

    setupFormValidation('contact-form');
    setupFormValidation('volunteer-form');


});
