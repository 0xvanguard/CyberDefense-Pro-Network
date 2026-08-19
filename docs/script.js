/* ========================================
   CyberDefense Pro Network - Scripts
   ======================================== */

// DOM Elements
const themeToggle = document.getElementById('themeToggle');
const mobileMenuBtn = document.getElementById('mobileMenuBtn');
const typingCommand = document.getElementById('typingCommand');
const terminalOutput = document.getElementById('terminalOutput');

// ========================================
// Theme Toggle (Dark/Light Mode)
// ========================================
function initTheme() {
    const savedTheme = localStorage.getItem('theme') || 'dark';
    document.documentElement.setAttribute('data-theme', savedTheme);
    updateThemeIcon(savedTheme);
}

function toggleTheme() {
    const currentTheme = document.documentElement.getAttribute('data-theme');
    const newTheme = currentTheme === 'dark' ? 'light' : 'dark';
    
    document.documentElement.setAttribute('data-theme', newTheme);
    localStorage.setItem('theme', newTheme);
    updateThemeIcon(newTheme);
}

function updateThemeIcon(theme) {
    const icon = themeToggle.querySelector('i');
    icon.className = theme === 'dark' ? 'fas fa-moon' : 'fas fa-sun';
}

// ========================================
// Mobile Menu
// ========================================
function toggleMobileMenu() {
    const navMenu = document.querySelector('.nav-menu');
    navMenu.classList.toggle('active');
}

// ========================================
// Terminal Animation
// ========================================
const commands = [
    { cmd: 'cdpn --version', output: 'CyberDefense Pro Network v1.0.0' },
    { cmd: 'nmap -sV target.com', output: 'Starting Nmap scan...\nPORT    STATE SERVICE\n80/tcp  open  http\n443/tcp open  https\n22/tcp  open  ssh' },
    { cmd: 'python3 recon_automatizado.py -d ejemplo.com', output: '[+] Resolving domain...\n[+] 5 subdomains found\n[+] Scan complete!' },
    { cmd: 'docker compose up -d', output: 'Creating network...\nCreating container...\n✓ All services started' },
    { cmd: 'yara -r rules/ malware样本.exe', output: 'malware样本.exe Malware_Rule_1 [author="CDPN"]' },
];

let currentCommand = 0;
let isTyping = false;

async function typeCommand(command) {
    if (isTyping) return;
    isTyping = true;
    
    typingCommand.textContent = '';
    
    for (let char of command) {
        await delay(50 + Math.random() * 50);
        typingCommand.textContent += char;
    }
    
    await delay(500);
    isTyping = false;
}

function showOutput(output) {
    terminalOutput.innerHTML = `<pre>${output}</pre>`;
}

function cycleCommands() {
    const cmd = commands[currentCommand];
    
    typeCommand(cmd.cmd).then(() => {
        setTimeout(() => {
            showOutput(cmd.output);
            currentCommand = (currentCommand + 1) % commands.length;
            
            setTimeout(() => {
                terminalOutput.innerHTML = '';
                cycleCommands();
            }, 3000);
        }, 500);
    });
}

function delay(ms) {
    return new Promise(resolve => setTimeout(resolve, ms));
}

// ========================================
// Counter Animation
// ========================================
function animateCounters() {
    const counters = document.querySelectorAll('.stat-number[data-count]');
    
    counters.forEach(counter => {
        const target = parseInt(counter.getAttribute('data-count'));
        const duration = 2000;
        const increment = target / (duration / 16);
        let current = 0;
        
        const updateCounter = () => {
            current += increment;
            if (current < target) {
                counter.textContent = Math.floor(current);
                requestAnimationFrame(updateCounter);
            } else {
                counter.textContent = target;
            }
        };
        
        updateCounter();
    });
}

// ========================================
// Tool Filter
// ========================================
function initToolFilter() {
    const filterBtns = document.querySelectorAll('.filter-btn');
    const toolCards = document.querySelectorAll('.tool-card');
    
    filterBtns.forEach(btn => {
        btn.addEventListener('click', () => {
            // Remove active class from all buttons
            filterBtns.forEach(b => b.classList.remove('active'));
            // Add active class to clicked button
            btn.classList.add('active');
            
            const filter = btn.getAttribute('data-filter');
            
            toolCards.forEach(card => {
                const category = card.getAttribute('data-category');
                
                if (filter === 'all' || category === filter) {
                    card.style.display = 'block';
                    card.style.animation = 'fadeIn 0.3s ease';
                } else {
                    card.style.display = 'none';
                }
            });
        });
    });
}

// ========================================
// Smooth Scroll
// ========================================
function initSmoothScroll() {
    document.querySelectorAll('a[href^="#"]').forEach(anchor => {
        anchor.addEventListener('click', function(e) {
            e.preventDefault();
            const target = document.querySelector(this.getAttribute('href'));
            
            if (target) {
                target.scrollIntoView({
                    behavior: 'smooth',
                    block: 'start'
                });
            }
        });
    });
}

// ========================================
// Scroll Effects
// ========================================
function initScrollEffects() {
    const navbar = document.querySelector('.navbar');
    
    window.addEventListener('scroll', () => {
        if (window.scrollY > 50) {
            navbar.style.background = 'rgba(10, 10, 15, 0.98)';
            navbar.style.boxShadow = '0 2px 20px rgba(0, 0, 0, 0.3)';
        } else {
            navbar.style.background = 'rgba(10, 10, 15, 0.95)';
            navbar.style.boxShadow = 'none';
        }
    });
}

// ========================================
// Intersection Observer for Animations
// ========================================
function initAnimations() {
    const observerOptions = {
        threshold: 0.1,
        rootMargin: '0px 0px -50px 0px'
    };
    
    const observer = new IntersectionObserver((entries) => {
        entries.forEach(entry => {
            if (entry.isIntersecting) {
                entry.target.classList.add('animate-in');
                observer.unobserve(entry.target);
            }
        });
    }, observerOptions);
    
    // Observe elements
    document.querySelectorAll('.module-card, .tool-card, .lab-card, .case-card').forEach(el => {
        el.style.opacity = '0';
        el.style.transform = 'translateY(30px)';
        el.style.transition = 'opacity 0.5s ease, transform 0.5s ease';
        observer.observe(el);
    });
}

// Add CSS for animations
const style = document.createElement('style');
style.textContent = `
    .animate-in {
        opacity: 1 !important;
        transform: translateY(0) !important;
    }
    
    @keyframes fadeIn {
        from { opacity: 0; transform: translateY(10px); }
        to { opacity: 1; transform: translateY(0); }
    }
    
    .nav-menu.active {
        display: flex;
        flex-direction: column;
        position: absolute;
        top: 100%;
        left: 0;
        right: 0;
        background: var(--bg-secondary);
        padding: var(--spacing-lg);
        border-bottom: 1px solid var(--border-color);
    }
`;
document.head.appendChild(style);

// ========================================
// Initialize
// ========================================
document.addEventListener('DOMContentLoaded', () => {
    // Theme
    initTheme();
    themeToggle.addEventListener('click', toggleTheme);
    
    // Mobile menu
    mobileMenuBtn.addEventListener('click', toggleMobileMenu);
    
    // Terminal animation
    cycleCommands();
    
    // Counter animation
    animateCounters();
    
    // Tool filter
    initToolFilter();
    
    // Smooth scroll
    initSmoothScroll();
    
    // Scroll effects
    initScrollEffects();
    
    // Animations
    initAnimations();
    
    console.log('🛡️ CyberDefense Pro Network loaded successfully!');
});

// ========================================
// Module Card Interactions
// ========================================
document.querySelectorAll('.module-card').forEach(card => {
    card.addEventListener('click', function() {
        const module = this.getAttribute('data-module');
        // Could open modal or navigate to module page
        console.log(`Module selected: ${module}`);
    });
});

// ========================================
// Lab Button Interactions
// ========================================
document.querySelectorAll('.btn-lab:not(.disabled)').forEach(btn => {
    btn.addEventListener('click', function() {
        const labName = this.closest('.lab-card').querySelector('.lab-name').textContent;
        
        // Show instructions
        alert(`Starting lab: ${labName}\n\nThis would open the lab environment in a real implementation.`);
    });
});
