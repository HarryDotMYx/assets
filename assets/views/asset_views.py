from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.http import JsonResponse
from ..models import Asset

@login_required
def asset_list(request):
    assets = Asset.objects.all().order_by('-created_at')
    assets_data = [asset.to_dict() for asset in assets]
    return render(request, 'assets/asset_list.html', {
        'assets': assets,
        'assets_json': assets_data,
        'page_title': 'Assets'
    })

@login_required
def asset_delete(request, pk):
    if request.method == 'POST':
        asset = get_object_or_404(Asset, pk=pk)
        try:
            asset.delete()
            messages.success(request, 'Asset deleted successfully.')
        except Exception as e:
            messages.error(request, 'Unable to delete asset. It may be referenced by other records.')
        return redirect('asset_list')
    return JsonResponse({'status': 'error', 'message': 'Invalid request method'})