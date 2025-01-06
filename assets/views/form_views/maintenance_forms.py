from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from ...forms import MaintenanceForm

@login_required
def maintenance_create(request):
    if request.method == 'POST':
        form = MaintenanceForm(request.POST)
        if form.is_valid():
            maintenance = form.save()
            
            # Update asset status
            asset = maintenance.asset
            asset.status = 'maintenance'
            asset.save()
            
            messages.success(request, 'Maintenance record created successfully.')
            return redirect('maintenance_list')
    else:
        form = MaintenanceForm()
    
    return render(request, 'assets/forms/maintenance_form.html', {
        'form': form,
        'page_title': 'New Maintenance Record'
    })