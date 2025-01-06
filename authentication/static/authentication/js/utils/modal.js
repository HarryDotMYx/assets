export function showModal(modal, modalContent) {
    modal.style.display = 'flex';
    modal.offsetHeight; // Force reflow
    modal.classList.add('modal-backdrop-visible');
    modalContent.classList.add('modal-content-visible');
}

export function hideModal(modal, modalContent) {
    modal.classList.remove('modal-backdrop-visible');
    modalContent.classList.remove('modal-content-visible');
    
    setTimeout(() => {
        modal.style.display = 'none';
    }, 300);
}