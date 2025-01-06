import { getElement, setTextContent } from '../utils/dom.js';

export class Modal {
    constructor(modalId) {
        this.modal = getElement(`#${modalId}`);
        if (!this.modal) return;
        
        this.setupEventListeners();
    }
    
    setupEventListeners() {
        this.modal.addEventListener('click', (e) => {
            if (e.target === this.modal || e.target.matches('.modal-close')) {
                this.hide();
            }
        });
        
        document.addEventListener('keydown', (e) => {
            if (e.key === 'Escape' && !this.modal.classList.contains('hidden')) {
                this.hide();
            }
        });
    }
    
    setContent({ title, assetTag, assignedTo, assignedBy, assignedDate, expectedReturn, returnDate, notes }) {
        setTextContent(getElement('#modalTitle'), title);
        setTextContent(getElement('#modalAssetTag'), assetTag);
        setTextContent(getElement('#modalAssignedTo'), assignedTo);
        setTextContent(getElement('#modalAssignedBy'), assignedBy);
        setTextContent(getElement('#modalAssignedDate'), assignedDate);
        setTextContent(getElement('#modalExpectedReturn'), expectedReturn);
        setTextContent(getElement('#modalReturnDate'), returnDate);
        setTextContent(getElement('#modalNotes'), notes);
    }
    
    show() {
        this.modal?.classList.remove('hidden');
    }
    
    hide() {
        this.modal?.classList.add('hidden');
    }
}