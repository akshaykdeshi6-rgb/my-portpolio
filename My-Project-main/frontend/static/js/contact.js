/**
 * frontend/static/js/contact.js
 * Asynchronously handle the contact form submission using REST API.
 */

document.addEventListener('DOMContentLoaded', () => {
    const contactForm = document.getElementById('contact-form');
    if (!contactForm) return;

    const alertSuccess = document.getElementById('alert-success');
    const alertError = document.getElementById('alert-error');
    const submitBtn = contactForm.querySelector('button[type="submit"]');
    const originalBtnText = submitBtn ? submitBtn.innerHTML : 'Send Message';

    // Clear error classes and messages
    const clearErrors = () => {
        const formGroups = contactForm.querySelectorAll('.form-group');
        formGroups.forEach(group => {
            group.classList.remove('error');
            const errMsg = group.querySelector('.error-message');
            if (errMsg) errMsg.remove();
        });
    };

    // Render error message for a specific input field
    const showError = (fieldId, message) => {
        const field = document.getElementById(fieldId);
        if (!field) return;

        const formGroup = field.closest('.form-group');
        formGroup.classList.add('error');

        // Create error message element if not already present
        let errMsg = formGroup.querySelector('.error-message');
        if (!errMsg) {
            errMsg = document.createElement('span');
            errMsg.className = 'error-message';
            formGroup.appendChild(errMsg);
        }
        errMsg.textContent = message;
    };

    // Handle Form Submit Event
    contactForm.addEventListener('submit', async (e) => {
        e.preventDefault();
        clearErrors();
        
        // Hide existing alerts
        if (alertSuccess) alertSuccess.style.display = 'none';
        if (alertError) alertError.style.display = 'none';

        // Gather input values
        const name = document.getElementById('name').value.trim();
        const email = document.getElementById('email').value.trim();
        const subject = document.getElementById('subject').value.trim();
        const message = document.getElementById('message').value.trim();

        // Basic client-side validation
        let hasErrors = false;
        if (!name) {
            showError('name', 'Name is required.');
            hasErrors = true;
        }
        if (!email) {
            showError('email', 'Email is required.');
            hasErrors = true;
        } else if (!/@/.test(email)) {
            showError('email', 'Please enter a valid email address.');
            hasErrors = true;
        }
        if (!subject) {
            showError('subject', 'Subject is required.');
            hasErrors = true;
        }
        if (!message) {
            showError('message', 'Message is required.');
            hasErrors = true;
        }

        if (hasErrors) return;

        // Visual loading state
        if (submitBtn) {
            submitBtn.disabled = true;
            submitBtn.innerHTML = 'Sending...';
        }

        try {
            const response = await fetch('/api/contact', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json'
                },
                body: JSON.stringify({ name, email, subject, message })
            });

            const result = await response.json();

            if (response.status === 201) {
                // Success: reset form and display success alert
                contactForm.reset();
                if (alertSuccess) {
                    alertSuccess.style.display = 'flex';
                    alertSuccess.querySelector('.alert-text').textContent = result.message || 'Message sent successfully!';
                }
            } else if (response.status === 400 && result.errors) {
                // Validation error from backend
                Object.keys(result.errors).forEach(key => {
                    showError(key, result.errors[key]);
                });
                if (alertError) {
                    alertError.style.display = 'flex';
                    alertError.querySelector('.alert-text').textContent = 'Please fix the errors below.';
                }
            } else {
                // Other API/Server error
                if (alertError) {
                    alertError.style.display = 'flex';
                    alertError.querySelector('.alert-text').textContent = result.message || 'Failed to submit the form. Try again later.';
                }
            }
        } catch (error) {
            console.error('Submission Error:', error);
            if (alertError) {
                alertError.style.display = 'flex';
                alertError.querySelector('.alert-text').textContent = 'Network error. Please verify your connection.';
            }
        } finally {
            // Restore button visual state
            if (submitBtn) {
                submitBtn.disabled = false;
                submitBtn.innerHTML = originalBtnText;
            }
        }
    });
});
