import { fadeIn, fadeOut } from '../utils/animations.js';
import { getElement } from '../utils/dom.js';

export class Modal {
    constructor(modalId) {
        this.modal = getElement(`#${modalId}`);
        this.content = this.modal?.querySelector('.modal-content');
        this.setupEventListeners();
    }

    setupEventListeners() {
        if (!this.modal) return;
        
        // Close on backdrop click
        this.modal.addEventListener('click', (e) => {
            if (e.target === this.modal) {
                this.hide();
            }
        });

        // Close on escape key
        document.addEventListener('keydown', (e) => {
            if (e.key === 'Escape' && this.modal.style.display === 'flex') {
                this.hide();
            }
        });
    }

    show() {
        fadeIn(this.modal);
        fadeIn(this.content);
        document.body.style.overflow = 'hidden'; // Prevent background scrolling
    }

    hide() {
        fadeOut(this.modal);
        fadeOut(this.content);
        setTimeout(() => {
            document.body.style.overflow = ''; // Restore scrolling
        }, 300);
    }
}