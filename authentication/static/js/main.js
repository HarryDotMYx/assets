import { Modal } from './components/modal.js';
import { LoginForm } from './components/loginForm.js';
import { onDOMReady, getElement } from './utils/dom.js';

onDOMReady(() => {
    const loginModal = new Modal('loginModal');
    const signInBtn = getElement('#signInBtn');
    const closeBtn = getElement('#closeModal');
    const loginForm = new LoginForm(getElement('form'));

    if (signInBtn) {
        signInBtn.addEventListener('click', () => loginModal.show());
    }

    if (closeBtn) {
        closeBtn.addEventListener('click', () => loginModal.hide());
    }
});