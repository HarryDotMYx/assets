import { showModal, hideModal } from './utils/modal.js';
import { fadeIn, fadeOut } from './utils/animations.js';

document.addEventListener('DOMContentLoaded', function() {
    const modal = document.getElementById('loginModal');
    const modalContent = modal.querySelector('.modal-content');
    const signInBtn = document.getElementById('signInBtn');
    const closeBtn = document.getElementById('closeModal');
    
    signInBtn.addEventListener('click', () => showModal(modal, modalContent));
    closeBtn.addEventListener('click', () => hideModal(modal, modalContent));
    
    modal.addEventListener('click', (e) => {
        if (e.target === modal) {
            hideModal(modal, modalContent);
        }
    });
});