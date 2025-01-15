from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from ...forms import AssetForm
from ...models import Asset

@login_required
def asset_create(request):
    if request.method == 'POST':
        form = AssetForm(request.POST)
        if form.is_valid():
            asset = form.save(commit=False)
            asset.person_in_charge = request.user.email  # Set the logged-in user's email
            asset.save()
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
            asset = form.save(commit=False)
            asset.person_in_charge = request.user.email  # Update with current user's email
            asset.save()
            messages.success(request, 'Asset updated successfully.')
            return redirect('asset_list')
    else:
        form = AssetForm(instance=asset)
    
    return render(request, 'assets/forms/asset_form.html', {
        'form': form,
        'page_title': 'Edit Asset'
    })