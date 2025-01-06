export const getElement = (selector) => document.querySelector(selector);
export const getElements = (selector) => document.querySelectorAll(selector);

export const setTextContent = (element, content) => {
    if (element) {
        element.textContent = content;
    }
};