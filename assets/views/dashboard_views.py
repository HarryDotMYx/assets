from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.db.models import Count
from ..models import Asset, AssetAssignment, Maintenance

@login_required
def dashboard(request):
    # Get asset statistics
    total_assets = Asset.objects.count()
    assigned_assets = Asset.objects.filter(status='assigned').count()
    maintenance_assets = Asset.objects.filter(status='maintenance').count()
    available_assets = Asset.objects.filter(status='available').count()

    # Get recent activities (last 10)
    recent_assignments = AssetAssignment.objects.select_related('asset', 'assigned_to')[:5]
    recent_maintenance = Maintenance.objects.select_related('asset')[:5]

    # Combine and sort activities
    recent_activities = []
    
    for assignment in recent_assignments:
        recent_activities.append({
            'timestamp': assignment.assigned_date,
            'description': f"{assignment.asset.name} assigned to {assignment.assigned_to.email}",
            'icon': '<svg class="w-6 h-6" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M12 4.354a4 4 0 110 5.292M15 21H3v-1a6 6 0 0112 0v1zm0 0h6v-1a6 6 0 00-9-5.197M13 7a4 4 0 11-8 0 4 4 0 018 0z"></path></svg>'
        })
    
    for maintenance in recent_maintenance:
        recent_activities.append({
            'timestamp': maintenance.created_at,
            'description': f"Maintenance scheduled for {maintenance.asset.name}",
            'icon': '<svg class="w-6 h-6" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M10.325 4.317c.426-1.756 2.924-1.756 3.35 0a1.724 1.724 0 002.573 1.066c1.543-.94 3.31.826 2.37 2.37a1.724 1.724 0 001.065 2.572c1.756.426 1.756 2.924 0 3.35a1.724 1.724 0 00-1.066 2.573c.94 1.543-.826 3.31-2.37 2.37a1.724 1.724 0 00-2.572 1.065c-.426 1.756-2.924 1.756-3.35 0a1.724 1.724 0 00-2.573-1.066c-1.543.94-3.31-.826-2.37-2.37a1.724 1.724 0 00-1.065-2.572c-1.756-.426-1.756-2.924 0-3.35a1.724 1.724 0 001.066-2.573c-.94-1.543.826-3.31 2.37-2.37.996.608 2.296.07 2.572-1.065z"></path><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M15 12a3 3 0 11-6 0 3 3 0 016 0z"></path></svg>'
        })

    # Sort activities by timestamp
    recent_activities.sort(key=lambda x: x['timestamp'], reverse=True)
    recent_activities = recent_activities[:10]

    context = {
        'total_assets': total_assets,
        'assigned_assets': assigned_assets,
        'maintenance_assets': maintenance_assets,
        'available_assets': available_assets,
        'recent_activities': recent_activities,
        'page_title': 'Dashboard'
    }

    return render(request, 'assets/dashboard.html', context)