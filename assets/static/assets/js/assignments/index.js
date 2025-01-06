import { assignmentState } from './state.js';

document.addEventListener('alpine:init', () => {
    Alpine.data('assignmentList', assignmentState);
});