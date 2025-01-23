from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.core.serializers.json import DjangoJSONEncoder
from django.utils import timezone
from ..models import AssetAssignment, Asset
from ..forms import AssetAssignmentForm
import json

@login_required
def assignment_list(request):
    assignments = AssetAssignment.objects.select_related('asset', 'assigned_to', 'assigned_by').all().order_by('-assigned_date')
    assignments_data = [{
        'id': assignment.id,
        'asset': {
            'id': assignment.asset.id,
            'name': assignment.asset.name,
            'tag': assignment.asset.asset_tag
        },
        'assigned_to': assignment.assigned_to.email,
        'assigned_by': assignment.assigned_by.email,
        'assigned_date': assignment.assigned_date.strftime('%b %d, %Y'),
        'return_date': assignment.return_date.strftime('%b %d, %Y') if assignment.return_date else None,
        'expected_return_date': assignment.expected_return_date.strftime('%b %d, %Y') if assignment.expected_return_date else None,
        'notes': assignment.notes or ''
    } for assignment in assignments]
    
    return render(request, 'assets/assignment_list.html', {
        'assignments': assignments,
        'assignments_json': json.dumps(assignments_data, cls=DjangoJSONEncoder),
        'page_title': 'Asset Assignments'
    })

@login_required
def assignment_edit(request, pk):
    assignment = get_object_or_404(AssetAssignment, pk=pk)
    if request.method == 'POST':
        form = AssetAssignmentForm(request.POST, instance=assignment)
        if form.is_valid():
            form.save()
            messages.success(request, 'Assignment updated successfully.')
            return redirect('assignment_list')
    else:
        form = AssetAssignmentForm(instance=assignment)
    
    return render(request, 'assets/forms/assignment_form.html', {
        'form': form,
        'page_title': 'Edit Assignment'
    })

@login_required
def assignment_return(request, pk):
    if request.method == 'POST':
        assignment = get_object_or_404(AssetAssignment, pk=pk)
        if not assignment.return_date:
            assignment.return_date = timezone.now()
            assignment.save()
            
            # Update asset status to available
            asset = assignment.asset
            asset.status = 'available'
            asset.save()
            
            messages.success(request, 'Asset returned successfully.')
        return redirect('assignment_list')
    return redirect('assignment_list')

@login_required
def assignment_delete(request, pk):
    if request.method == 'POST':
        assignment = get_object_or_404(AssetAssignment, pk=pk)
        try:
            # If the asset is currently assigned (no return date), update its status
            if not assignment.return_date:
                asset = assignment.asset
                asset.status = 'available'
                asset.save()
            
            assignment.delete()
            messages.success(request, 'Assignment deleted successfully.')
        except Exception as e:
            messages.error(request, 'Unable to delete assignment.')
        return redirect('assignment_list')
    return redirect('assignment_list')