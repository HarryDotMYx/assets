from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from ...forms import AssetAssignmentForm

@login_required
def assignment_create(request):
    if request.method == 'POST':
        form = AssetAssignmentForm(request.POST)
        if form.is_valid():
            try:
                assignment = form.save(commit=False)
                assignment.assigned_by = request.user
                assignment.save()
                
                # Update asset status
                asset = assignment.asset
                asset.status = 'assigned'
                asset.save()
                
                messages.success(request, f'Asset "{asset.name}" has been successfully assigned to {assignment.assigned_to.email}.')
                return redirect('assignment_list')
            except Exception as e:
                messages.error(request, f'Error creating assignment: {str(e)}')
        else:
            messages.error(request, 'Please correct the errors below.')
    else:
        form = AssetAssignmentForm()
    
    return render(request, 'assets/forms/assignment_form.html', {
        'form': form,
        'page_title': 'New Asset Assignment'
    })