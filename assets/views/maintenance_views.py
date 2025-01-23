from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from django.contrib import messages
from ..models import Maintenance, Asset
from ..forms import MaintenanceForm

@login_required
def maintenance_list(request):
    maintenance_records = Maintenance.objects.select_related('asset').all().order_by('-maintenance_date')
    return render(request, 'assets/maintenance_list.html', {
        'maintenance_records': maintenance_records,
        'page_title': 'Maintenance Records'
    })

@login_required
def maintenance_details(request, pk):
    record = get_object_or_404(Maintenance, pk=pk)
    return JsonResponse({
        'id': record.id,
        'asset_name': record.asset.name,
        'maintenance_type': record.maintenance_type,
        'maintenance_date': record.maintenance_date.strftime('%b %d, %Y'),
        'cost': str(record.cost),
        'performed_by': record.performed_by,
        'next_maintenance_date': record.next_maintenance_date.strftime('%b %d, %Y') if record.next_maintenance_date else None,
        'notes': record.notes
    })

@login_required
def maintenance_edit(request, pk):
    maintenance = get_object_or_404(Maintenance, pk=pk)
    if request.method == 'POST':
        form = MaintenanceForm(request.POST, instance=maintenance)
        if form.is_valid():
            maintenance = form.save()
            
            # Update asset status
            asset = maintenance.asset
            asset.status = 'maintenance'
            asset.save()
            
            messages.success(request, 'Maintenance record updated successfully.')
            return redirect('maintenance_list')
    else:
        form = MaintenanceForm(instance=maintenance)
    
    return render(request, 'assets/forms/maintenance_form.html', {
        'form': form,
        'page_title': 'Edit Maintenance Record'
    })

@login_required
def maintenance_delete(request, pk):
    if request.method == 'POST':
        maintenance = get_object_or_404(Maintenance, pk=pk)
        try:
            # Update asset status back to available
            asset = maintenance.asset
            asset.status = 'available'
            asset.save()
            
            maintenance.delete()
            messages.success(request, 'Maintenance record deleted successfully.')
        except Exception as e:
            messages.error(request, 'Unable to delete maintenance record.')
        return redirect('maintenance_list')
    return JsonResponse({'status': 'error', 'message': 'Invalid request method'})