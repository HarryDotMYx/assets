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
from .assignment_views import assignment_list
from .maintenance_views import maintenance_list
from .dashboard_views import dashboard
from .report_views import reports_dashboard, generate_pdf_report

__all__ = [
    'asset_list',
    'asset_create',
    'asset_edit',
    'asset_delete',
    'assignment_list',
    'assignment_create',
    'maintenance_list',
    'maintenance_create',
    'dashboard',
    'reports_dashboard',
    'generate_pdf_report'
]