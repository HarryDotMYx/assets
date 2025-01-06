// Chart configuration and setup
export function setupCharts(statusData, categoryData, maintenanceCosts) {
    setupStatusChart(statusData);
    setupCategoryChart(categoryData);
    setupMaintenanceChart(maintenanceCosts);
}

function setupStatusChart(data) {
    const ctx = document.getElementById('statusChart').getContext('2d');
    new Chart(ctx, {
        type: 'bar',
        data: {
            labels: data.map(item => item.status),
            datasets: [{
                label: 'Number of Assets',
                data: data.map(item => item.count),
                backgroundColor: [
                    'rgba(34, 197, 94, 0.6)',  // Available
                    'rgba(59, 130, 246, 0.6)', // Assigned
                    'rgba(234, 179, 8, 0.6)',  // Maintenance
                    'rgba(239, 68, 68, 0.6)'   // Retired
                ]
            }]
        },
        options: {
            responsive: true,
            plugins: {
                legend: {
                    position: 'bottom'
                },
                title: {
                    display: true,
                    text: 'Asset Status Distribution'
                }
            },
            scales: {
                y: {
                    beginAtZero: true,
                    ticks: {
                        stepSize: 1
                    }
                }
            }
        }
    });
}

function setupCategoryChart(data) {
    const ctx = document.getElementById('categoryChart').getContext('2d');
    new Chart(ctx, {
        type: 'doughnut',
        data: {
            labels: data.map(item => item.category__name),
            datasets: [{
                data: data.map(item => item.count),
                backgroundColor: [
                    'rgba(59, 130, 246, 0.6)',
                    'rgba(34, 197, 94, 0.6)',
                    'rgba(234, 179, 8, 0.6)',
                    'rgba(239, 68, 68, 0.6)',
                    'rgba(168, 85, 247, 0.6)'
                ]
            }]
        },
        options: {
            responsive: true,
            plugins: {
                legend: {
                    position: 'bottom'
                },
                title: {
                    display: true,
                    text: 'Assets by Category'
                }
            }
        }
    });
}

function setupMaintenanceChart(data) {
    const ctx = document.getElementById('maintenanceChart').getContext('2d');
    const months = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'];
    
    new Chart(ctx, {
        type: 'line',
        data: {
            labels: data.map(item => months[item.maintenance_date__month - 1]),
            datasets: [{
                label: 'Maintenance Costs ($)',
                data: data.map(item => item.total_cost),
                borderColor: 'rgba(59, 130, 246, 1)',
                backgroundColor: 'rgba(59, 130, 246, 0.1)',
                fill: true
            }]
        },
        options: {
            responsive: true,
            plugins: {
                legend: {
                    position: 'bottom'
                },
                title: {
                    display: true,
                    text: 'Monthly Maintenance Costs'
                }
            },
            scales: {
                y: {
                    beginAtZero: true,
                    ticks: {
                        callback: value => '$' + value
                    }
                }
            }
        }
    });
}