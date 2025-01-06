document.addEventListener('DOMContentLoaded', () => {
    window.Alpine.data('assignmentList', () => ({
        showModal: false,
        selectedAssignment: null,
        assignments: [],
        
        init() {
            // Get assignments data from the data attribute
            const assignmentsData = this.$el.dataset.assignments;
            this.assignments = JSON.parse(assignmentsData || '[]');
        }
    }));
});