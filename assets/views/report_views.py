from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.template.loader import get_template
from django.db.models import Count, Sum
from xhtml2pdf import pisa
from ..models import Asset, AssetAssignment, Maintenance

@login_required
def reports_dashboard(request):
    # Asset status distribution
    status_data = Asset.objects.values('status').annotate(count=Count('id'))
    
    # Category distribution
    category_data = Asset.objects.values('category__name').annotate(count=Count('id'))
    
    # Monthly maintenance costs
    maintenance_costs = Maintenance.objects.values('maintenance_date__month').annotate(
        total_cost=Sum('cost')
    ).order_by('maintenance_date__month')
    
    context = {
        'page_title': 'Reports',
        'status_data': list(status_data),
        'category_data': list(category_data),
        'maintenance_costs': list(maintenance_costs)
    }
    
    return render(request, 'assets/reports/dashboard.html', context)

@login_required
def generate_pdf_report(request):
    # Get the data
    assets = Asset.objects.all().select_related('category')
    assignments = AssetAssignment.objects.all().select_related('asset', 'assigned_to')
    maintenance_records = Maintenance.objects.all().select_related('asset')
    
    template = get_template('assets/reports/pdf_template.html')
    context = {
        'assets': assets,
        'assignments': assignments,
        'maintenance_records': maintenance_records,
    }
    
    html = template.render(context)
    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = 'attachment; filename="asset_report.pdf"'
    
    # Create PDF
    pisa_status = pisa.CreatePDF(html, dest=response)
    if pisa_status.err:
        return HttpResponse('PDF generation error')
    
    return response