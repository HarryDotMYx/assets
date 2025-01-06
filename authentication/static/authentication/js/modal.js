document.addEventListener('DOMContentLoaded', function() {
    const modal = document.getElementById('loginModal');
    const modalContent = modal.querySelector('.modal-content');
    const signInBtn = document.getElementById('signInBtn');
    const closeBtn = document.getElementById('closeModal');
    
    function showModal() {
        modal.style.display = 'flex';
        // Force a reflow
        modal.offsetHeight;
        modal.classList.add('modal-backdrop-visible');
        modalContent.classList.add('modal-content-visible');
    }
    
    function hideModal() {
        modal.classList.remove('modal-backdrop-visible');
        modalContent.classList.remove('modal-content-visible');
        
        setTimeout(() => {
            modal.style.display = 'none';
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
    
    // Rest of the code remains the same
});