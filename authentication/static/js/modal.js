document.addEventListener('DOMContentLoaded', function() {
    const modal = document.getElementById('loginModal');
    const modalContent = modal.querySelector('.modal-content');
    const signInBtn = document.getElementById('signInBtn');
    const closeBtn = document.getElementById('closeModal');
    
    function showModal() {
        // First show the modal with opacity 0
        modal.classList.remove('hidden');
        
        // Force a reflow to enable the transition
        modal.offsetHeight;
        
        // Add the visible classes to trigger the transitions
        modal.classList.add('modal-backdrop-visible');
        modalContent.classList.add('modal-content-visible');
    }
    
    function hideModal() {
        modal.classList.remove('modal-backdrop-visible');
        modalContent.classList.remove('modal-content-visible');
        
        // Wait for the animation to finish before hiding the modal
        setTimeout(() => {
            modal.classList.add('hidden');
        }, 300);
    }
    
    signInBtn.addEventListener('click', showModal);
    closeBtn.addEventListener('click', hideModal);
    
    // Close modal when clicking outside
    modal.addEventListener('click', function(e) {
        if (e.target === modal) {
            hideModal();
        }
    });
    
    // Handle form submission
    const form = document.querySelector('form');
    form.addEventListener('submit', async function(e) {
        e.preventDefault();
        const submitBtn = form.querySelector('button[type="submit"]');
        submitBtn.disabled = true;
        submitBtn.innerHTML = `
            <svg class="animate-spin h-5 w-5 mr-2 inline" xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24">
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