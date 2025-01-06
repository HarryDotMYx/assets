from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from ...forms import AssetAssignmentForm

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