// Animation utility functions
export const fadeIn = (element, duration = 300) => {
    if (!element) return;
    
    element.style.display = 'flex';
    element.style.opacity = '0';
    element.style.transform = 'scale(0.95)';
    
    // Force reflow
    element.offsetHeight;
    
    element.style.transition = `all ${duration}ms cubic-bezier(0.34, 1.56, 0.64, 1)`;
    element.style.opacity = '1';
    element.style.transform = 'scale(1)';
};

export const fadeOut = (element, duration = 200) => {
    if (!element) return;
    
    element.style.transition = `all ${duration}ms cubic-bezier(0.4, 0, 0.2, 1)`;
    element.style.opacity = '0';
    element.style.transform = 'scale(0.95)';
    
    setTimeout(() => {
        element.style.display = 'none';
    }, duration);
};