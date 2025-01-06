export const renderAssignmentRow = (assignment) => `
    <tr>
        <td class="px-6 py-4 whitespace-nowrap">${assignment.asset.name}</td>
        <td class="px-6 py-4 whitespace-nowrap">${assignment.assigned_to}</td>
        <td class="px-6 py-4 whitespace-nowrap">${assignment.assigned_date}</td>
        <td class="px-6 py-4 whitespace-nowrap">${assignment.return_date || 'Not returned'}</td>
        <td class="px-6 py-4 whitespace-nowrap">
            <button class="view-details-btn text-blue-600 hover:text-blue-900" data-id="${assignment.id}">
                View Details
            </button>
        </td>
    </tr>
`;