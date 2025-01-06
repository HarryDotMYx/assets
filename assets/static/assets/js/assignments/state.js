export const assignmentState = () => ({
    showModal: false,
    selectedAssignment: null,
    assignments: [],
    
    init() {
        const assignmentsData = this.$el.getAttribute('data-assignments');
        this.assignments = JSON.parse(assignmentsData || '[]');
    },
    
    viewDetails(assignment) {
        this.selectedAssignment = assignment;
        this.showModal = true;
    }
});