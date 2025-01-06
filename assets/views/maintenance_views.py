from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from ..models import Maintenance

@login_required
def maintenance_list(request):
    maintenance_records = Maintenance.objects.all().order_by('-maintenance_date')
    return render(request, 'assets/maintenance_list.html', {
        'maintenance_records': maintenance_records,
        'page_title': 'Maintenance Records'
    })