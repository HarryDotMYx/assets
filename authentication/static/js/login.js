import { showModal, hideModal } from './modal.js';

document.addEventListener('DOMContentLoaded', function() {
    const modal = document.getElementById('loginModal');
    const modalContent = modal.querySelector('.modal-content');
    const signInBtn = document.getElementById('signInBtn');
    const closeBtn = document.getElementById('closeModal');
    const form = document.querySelector('form');
    
    function toggleModal() {
        if (modal.classList.contains('hidden')) {
            showModal(modal, modalContent);
        } else {
            hideModal(modal, modalContent);
        }
    }
    
    signInBtn.addEventListener('click', toggleModal);
    closeBtn.addEventListener('click', toggleModal);
    
    // Close modal when clicking outside
    modal.addEventListener('click', function(e) {
        if (e.target === modal) {
            hideModal(modal, modalContent);
        }
    });
    
    // Handle form submission
    form.addEventListener('submit', async function(e) {
        e.preventDefault();
        const submitBtn = form.querySelector('button[type="submit"]');
        submitBtn.disabled = true;
        submitBtn.innerHTML = `
            <svg class="animate-spin h-5 w-5 mr-2" xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24">
                <circle class="opacity-25" cx="12" cy="12" r="10" stroke="currentColor" stroke-width="4"></circle>
                <path class="opacity-75" fill="currentColor" d="M4 12a8 8 0 018-8V0C5.373 0 0 5.373 0 12h4zm2 5.291A7.962 7.962 0 014 12H0c0 3.042 1.135 5.824 3 7.938l3-2.647z"></path>
            </svg>
            Signing in...
        `;
        
        const formData = new FormData(form);
        try {
            const response = await fetch('/login/', {
                method: 'POST',
                body: formData,
                headers: {
                    'X-CSRFToken': document.querySelector('[name=csrfmiddlewaretoken]').value
                }
            });
            
            if (response.ok) {
                window.location.href = '/dashboard/';
            } else {
                throw new Error('Invalid credentials');
            }
        } catch (error) {
            submitBtn.disabled = false;
            submitBtn.innerHTML = 'Sign In';
            alert('Invalid credentials. Please try again.');
        }
    });
});