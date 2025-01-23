from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from ...forms import MaintenanceForm

@login_required
def maintenance_create(request):
    if request.method == 'POST':
        form = MaintenanceForm(request.POST)
        if form.is_valid():
            try:
                maintenance = form.save()
                
                # Update asset status
                asset = maintenance.asset
                asset.status = 'maintenance'
                asset.save()
                
                messages.success(request, f'Maintenance record for "{asset.name}" has been successfully created.')
                return redirect('maintenance_list')
            except Exception as e:
                messages.error(request, f'Error creating maintenance record: {str(e)}')
        else:
            messages.error(request, 'Please correct the errors below.')
    else:
        form = MaintenanceForm()
    
    return render(request, 'assets/forms/maintenance_form.html', {
        'form': form,
        'page_title': 'New Maintenance Record'
    })