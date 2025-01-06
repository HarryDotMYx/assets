import { fadeIn, fadeOut } from '../utils/animations.js';

export class Toast {
    constructor() {
        this.createToastContainer();
    }

    createToastContainer() {
        const container = document.createElement('div');
        container.id = 'toast-container';
        container.className = 'fixed top-4 right-4 z-50 flex flex-col gap-2';
        document.body.appendChild(container);
    }

    show(message, type = 'error') {
        const toast = document.createElement('div');
        const bgColor = type === 'error' ? 'bg-red-500' : 'bg-green-500';
        
        toast.className = `${bgColor} text-white px-4 py-2 rounded-lg shadow-lg flex items-center gap-2 transform translate-x-full`;
        toast.innerHTML = `
            <svg class="w-5 h-5" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                ${type === 'error' ? `
                    <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" 
                        d="M12 8v4m0 4h.01M21 12a9 9 0 11-18 0 9 9 0 0118 0z" />
                ` : `
                    <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" 
                        d="M9 12l2 2 4-4m6 2a9 9 0 11-18 0 9 9 0 0118 0z" />
                `}
            </svg>
            <span>${message}</span>
        `;

        document.getElementById('toast-container').appendChild(toast);
        
        // Animate in
        requestAnimationFrame(() => {
            toast.style.transition = 'all 300ms cubic-bezier(0.4, 0, 0.2, 1)';
            toast.style.transform = 'translateX(0)';
        });

        // Remove after 3 seconds
        setTimeout(() => {
            toast.style.transform = 'translateX(full)';
            toast.style.opacity = '0';
            setTimeout(() => toast.remove(), 300);
        }, 3000);
    }
}