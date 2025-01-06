export function fadeIn(element, duration = 300) {
    element.style.opacity = '0';
    element.style.display = 'flex';
    element.style.transform = 'scale(0.95)';
    
    requestAnimationFrame(() => {
        element.style.transition = `opacity ${duration}ms ease-out, transform ${duration}ms ease-out`;
        element.style.opacity = '1';
        element.style.transform = 'scale(1)';
    });
}

export function fadeOut(element, duration = 200) {
    element.style.transition = `opacity ${duration}ms ease-in, transform ${duration}ms ease-in`;
    element.style.opacity = '0';
    element.style.transform = 'scale(0.95)';
    
    setTimeout(() => {
        element.style.display = 'none';
    }, duration);
}