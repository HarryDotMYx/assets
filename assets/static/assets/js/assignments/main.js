import { showModal, hideModal, setupModalCloseHandlers } from '../modules/modal.js';

document.addEventListener('DOMContentLoaded', () => {
    // Setup modal close handlers
    setupModalCloseHandlers('assignmentModal');

    // Setup view details handlers
    const tableBody = document.getElementById('assignmentsTableBody');
    if (tableBody) {
        tableBody.addEventListener('click', (e) => {
            if (e.target.matches('.view-details-btn')) {
                const assignmentId = e.target.dataset.id;
                const assignment = findAssignment(assignmentId);
                if (assignment) {
                    showAssignmentDetails(assignment);
                }
            }
        });
    }
});

function findAssignment(id) {
    const assignmentsData = document.querySelector('[data-assignments]');
    if (!assignmentsData) return null;
    
    const assignments = JSON.parse(assignmentsData.dataset.assignments || '[]');
    return assignments.find(a => a.id === parseInt(id));
}

function showAssignmentDetails(assignment) {
    updateModalContent(assignment);
    showModal('assignmentModal');
}

function updateModalContent(assignment) {
    const elements = {
        'modalTitle': `Assignment Details - ${assignment.asset.name}`,
        'modalAssetTag': assignment.asset.tag,
        'modalAssignedTo': assignment.assigned_to,
        'modalAssignedBy': assignment.assigned_by,
        'modalAssignedDate': assignment.assigned_date,
        'modalExpectedReturn': assignment.expected_return_date || 'Not specified',
        'modalReturnDate': assignment.return_date || 'Not returned',
        'modalNotes': assignment.notes || 'No notes'
    };

    for (const [id, value] of Object.entries(elements)) {
        const element = document.getElementById(id);
        if (element) {
            element.textContent = value;
        }
    }
}