// Modal utility functions
export function showModal(modalId) {
    const modal = document.getElementById(modalId);
    if (modal) {
        modal.classList.remove('hidden');
    }
}

export function hideModal(modalId) {
    const modal = document.getElementById(modalId);
    if (modal) {
        modal.classList.add('hidden');
    }
}

export function setupModalCloseHandlers(modalId) {
    const modal = document.getElementById(modalId);
    if (!modal) return;

    // Close on backdrop click
    modal.addEventListener('click', (e) => {
        if (e.target === modal) {
            hideModal(modalId);
        }
    });

    // Close on close button click
    const closeButtons = modal.querySelectorAll('.modal-close, .close-btn');
    closeButtons.forEach(button => {
        button.addEventListener('click', () => hideModal(modalId));
    });
}