// Animation utility functions
const fadeIn = (element, duration = 300) => {
    element.style.display = 'flex';
    element.style.opacity = '0';
    element.style.transform = 'scale(0.95)';
    
    requestAnimationFrame(() => {
        element.style.transition = `opacity ${duration}ms ease-out, transform ${duration}ms ease-out`;
        element.style.opacity = '1';
        element.style.transform = 'scale(1)';
    });
};

const fadeOut = (element, duration = 200) => {
    element.style.transition = `opacity ${duration}ms ease-in, transform ${duration}ms ease-in`;
    element.style.opacity = '0';
    element.style.transform = 'scale(0.95)';
    
    setTimeout(() => {
        element.style.display = 'none';
    }, duration);
};

export { fadeIn, fadeOut };