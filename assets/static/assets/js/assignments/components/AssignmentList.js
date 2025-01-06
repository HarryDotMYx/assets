import { Modal } from './Modal.js';
import { renderAssignmentRow } from '../templates/assignmentRow.js';

export class AssignmentList {
    constructor(assignments) {
        this.assignments = assignments;
        this.tableBody = document.getElementById('assignmentsTableBody');
        this.modal = new Modal('assignmentModal');
        
        this.init();
    }
    
    init() {
        this.renderAssignments();
        this.setupEventListeners();
    }
    
    renderAssignments() {
        this.tableBody.innerHTML = this.assignments
            .map(assignment => renderAssignmentRow(assignment))
            .join('');
    }
    
    setupEventListeners() {
        this.tableBody.addEventListener('click', (e) => {
            if (e.target.matches('.view-details-btn')) {
                const assignmentId = parseInt(e.target.dataset.id);
                const assignment = this.assignments.find(a => a.id === assignmentId);
                if (assignment) {
                    this.showDetails(assignment);
                }
            }
        });
    }
    
    showDetails(assignment) {
        this.modal.setContent({
            title: `Assignment Details - ${assignment.asset.name}`,
            assetTag: assignment.asset.tag,
            assignedTo: assignment.assigned_to,
            assignedBy: assignment.assigned_by,
            assignedDate: assignment.assigned_date,
            expectedReturn: assignment.expected_return_date || 'Not specified',
            returnDate: assignment.return_date || 'Not returned',
            notes: assignment.notes || 'No notes'
        });
        
        this.modal.show();
    }
}