import { AssignmentList } from './components/AssignmentList.js';
import { parseJSONSafely } from './utils/data.js';
import { getElement } from './utils/dom.js';

document.addEventListener('DOMContentLoaded', () => {
    const container = getElement('[data-assignments]');
    if (!container) return;

    const assignmentsData = parseJSONSafely(container.dataset.assignments, []);
    new AssignmentList(assignmentsData);
});