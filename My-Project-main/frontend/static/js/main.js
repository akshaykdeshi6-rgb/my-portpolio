/**
 * frontend/static/js/main.js
 * Handle navbar scroll effects, mobile hamburger menu toggling, 
 * page reveal scroll animations, and progress bar animation.
 */

document.addEventListener('DOMContentLoaded', () => {
    // ── Navbar Scroll Behavior ──
    const navbar = document.querySelector('.navbar');
    
    const handleScroll = () => {
        if (window.scrollY > 30) {
            navbar.classList.add('scrolled');
        } else {
            navbar.classList.remove('scrolled');
        }
    };
    
    window.addEventListener('scroll', handleScroll);
    handleScroll(); // Run initially in case of reload page halfway

    // ── Mobile Navigation Toggle ──
    const navToggle = document.querySelector('.mobile-nav-toggle');
    const navLinks = document.querySelector('.nav-links');

    if (navToggle && navLinks) {
        navToggle.addEventListener('click', () => {
            navToggle.classList.toggle('active');
            navLinks.classList.toggle('active');
        });

        // Close menu when clicking a link
        navLinks.querySelectorAll('a').forEach(link => {
            link.addEventListener('click', () => {
                navToggle.classList.remove('active');
                navLinks.classList.remove('active');
            });
        });
    }

    // ── Scroll Reveal Animations ──
    const revealElements = document.querySelectorAll('.reveal');
    
    const revealOnScroll = () => {
        const triggerBottom = window.innerHeight * 0.85;
        
        revealElements.forEach(element => {
            const elementTop = element.getBoundingClientRect().top;
            
            if (elementTop < triggerBottom) {
                element.classList.add('active');
                
                // If it's a skills page block, animate progress bars
                if (element.classList.contains('skills-group-card')) {
                    animateProgressBars(element);
                }
            }
        });
    };

    // Helper to animate progress bars inside card
    const animateProgressBars = (card) => {
        const progressFills = card.querySelectorAll('.progress-fill');
        progressFills.forEach(fill => {
            const width = fill.getAttribute('data-width');
            fill.style.width = `${width}%`;
        });
    };

    window.addEventListener('scroll', revealOnScroll);
    
    // Trigger initial reveal checks (on page load)
    setTimeout(revealOnScroll, 100);
});
