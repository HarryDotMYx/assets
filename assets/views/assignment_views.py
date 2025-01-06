from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.core.serializers.json import DjangoJSONEncoder
from ..models import AssetAssignment
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