from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from ..forms import AssetForm, AssetAssignmentForm, MaintenanceForm
from ..models import Asset

@login_required
def asset_create(request):
    if request.method == 'POST':
        form = AssetForm(request.POST)
        if form.is_valid():
            asset = form.save()
            messages.success(request, 'Asset created successfully.')
            return redirect('asset_list')
    else:
        form = AssetForm()
    
    return render(request, 'assets/forms/asset_form.html', {
        'form': form,
        'page_title': 'Add New Asset'
    })

@login_required
def asset_edit(request, pk):
    asset = get_object_or_404(Asset, pk=pk)
    if request.method == 'POST':
        form = AssetForm(request.POST, instance=asset)
        if form.is_valid():
            form.save()
            messages.success(request, 'Asset updated successfully.')
            return redirect('asset_list')
    else:
        form = AssetForm(instance=asset)
    
    return render(request, 'assets/forms/asset_form.html', {
        'form': form,
        'page_title': 'Edit Asset'
    })

@login_required
def assignment_create(request):
    if request.method == 'POST':
        form = AssetAssignmentForm(request.POST)
        if form.is_valid():
            assignment = form.save(commit=False)
            assignment.assigned_by = request.user
            assignment.save()
            
            # Update asset status
            asset = assignment.asset
            asset.status = 'assigned'
            asset.save()
            
            messages.success(request, 'Asset assignment created successfully.')
            return redirect('assignment_list')
    else:
        form = AssetAssignmentForm()
    
    return render(request, 'assets/forms/assignment_form.html', {
        'form': form,
        'page_title': 'New Asset Assignment'
    })

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