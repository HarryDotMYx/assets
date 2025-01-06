from django.contrib import admin
from .models import Category, Asset, AssetAssignment, Maintenance

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'description')
    search_fields = ('name',)

@admin.register(Asset)
class AssetAdmin(admin.ModelAdmin):
    list_display = ('asset_tag', 'name', 'category', 'status', 'location')
    list_filter = ('status', 'category', 'location')
    search_fields = ('asset_tag', 'name', 'serial_number')
    date_hierarchy = 'purchase_date'

@admin.register(AssetAssignment)
class AssetAssignmentAdmin(admin.ModelAdmin):
    list_display = ('asset', 'assigned_to', 'assigned_by', 'assigned_date', 'return_date')
    list_filter = ('assigned_date', 'return_date')
    search_fields = ('asset__name', 'assigned_to__email')
    date_hierarchy = 'assigned_date'

@admin.register(Maintenance)
class MaintenanceAdmin(admin.ModelAdmin):
    list_display = ('asset', 'maintenance_type', 'maintenance_date', 'cost')
    list_filter = ('maintenance_date', 'maintenance_type')
    search_fields = ('asset__name', 'maintenance_type')
    date_hierarchy = 'maintenance_date'