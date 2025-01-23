from .asset_views import (
    asset_list,
    asset_delete
)
from .form_views import (
    asset_create,
    asset_edit,
    assignment_create,
    maintenance_create
)
from .assignment_views import (
    assignment_list,
    assignment_edit,
    assignment_return,
    assignment_delete
)
from .maintenance_views import (
    maintenance_list,
    maintenance_edit,
    maintenance_delete,
    maintenance_details
)
from .dashboard_views import dashboard
from .report_views import reports_dashboard, generate_pdf_report

__all__ = [
    'asset_list',
    'asset_create',
    'asset_edit',
    'asset_delete',
    'assignment_list',
    'assignment_create',
    'assignment_edit',
    'assignment_return',
    'assignment_delete',
    'maintenance_list',
    'maintenance_create',
    'maintenance_edit',
    'maintenance_delete',
    'maintenance_details',
    'dashboard',
    'reports_dashboard',
    'generate_pdf_report'
]