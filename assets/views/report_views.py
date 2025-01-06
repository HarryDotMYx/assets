from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.template.loader import get_template
from django.db.models import Count, Sum
from xhtml2pdf import pisa
from ..models import Asset, AssetAssignment, Maintenance
from decimal import Decimal

@login_required
def reports_dashboard(request):
    # Asset statistics
    total_assets = Asset.objects.count()
    active_assets = Asset.objects.exclude(status='retired').count()
    total_cost = Asset.objects.aggregate(total=Sum('purchase_cost'))['total'] or Decimal('0')
    maintenance_cost = Maintenance.objects.aggregate(total=Sum('cost'))['total'] or Decimal('0')
    
    # Asset status distribution
    status_data = list(Asset.objects.values('status')
                      .annotate(count=Count('id'))
                      .order_by('status'))
    
    # Category distribution
    category_data = list(Asset.objects.values('category__name')
                        .annotate(count=Count('id'))
                        .order_by('-count'))
    
    # Monthly maintenance costs for current year
    maintenance_costs = list(Maintenance.objects
                           .values('maintenance_date__month')
                           .annotate(total_cost=Sum('cost'))
                           .order_by('maintenance_date__month'))
    
    context = {
        'page_title': 'Reports',
        'total_assets': total_assets,
        'active_assets': active_assets,
        'total_cost': total_cost,
        'maintenance_cost': maintenance_cost,
        'status_data': status_data,
        'category_data': category_data,
        'maintenance_costs': maintenance_costs
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