document.addEventListener('DOMContentLoaded', function() {
    const modal = document.getElementById('loginModal');
    const signInBtn = document.getElementById('signInBtn');
    const closeBtn = document.getElementById('closeModal');

    function toggleModal() {
        modal.classList.toggle('hidden');
    }

    signInBtn.addEventListener('click', toggleModal);
    closeBtn.addEventListener('click', toggleModal);

    // Close modal when clicking outside
    modal.addEventListener('click', function(e) {
        if (e.target === modal) {
            toggleModal();
        }
    });

    // Handle form submission
    const form = document.querySelector('form');
    form.addEventListener('submit', async function(e) {
        e.preventDefault();
        
        const formData = new FormData(form);
        try {
            const response = await fetch('/api/login/', {
                method: 'POST',
                body: formData,
                headers: {
                    'X-CSRFToken': document.querySelector('[name=csrfmiddlewaretoken]').value
                }
            });
            
            if (response.ok) {
                window.location.href = '/dashboard/';
            } else {
                alert('Invalid credentials. Please try again.');
            }
        } catch (error) {
            console.error('Error:', error);
            alert('An error occurred. Please try again.');
        }
    });
});