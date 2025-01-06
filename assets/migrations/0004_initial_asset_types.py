"""
Create initial asset types and placements

This migration creates the initial set of asset types and placement locations.
"""

from django.db import migrations

def create_initial_data(apps, schema_editor):
    AssetType = apps.get_model('assets', 'AssetType')
    Placement = apps.get_model('assets', 'Placement')
    
    # Create asset types
    asset_types = [
        {'name': 'Printer', 'code': 'PRT', 'description': 'Printing devices'},
        {'name': 'Laptop', 'code': 'LPT', 'description': 'Portable computers'},
        {'name': 'Desktop', 'code': 'DSK', 'description': 'Desktop computers'},
        {'name': 'Server', 'code': 'SRV', 'description': 'Server hardware'},
        {'name': 'Network', 'code': 'NET', 'description': 'Network equipment'}
    ]
    
    for data in asset_types:
        AssetType.objects.create(**data)
    
    # Create placements
    placements = [
        {'name': 'MIS Department', 'code': 'MIS', 'description': 'Management Information Systems'},
        {'name': 'Admin', 'code': 'ADM', 'description': 'Administration Department'},
        {'name': 'SMD', 'code': 'SMD', 'description': 'Strategic Management Department'}
    ]
    
    for data in placements:
        Placement.objects.create(**data)

def remove_initial_data(apps, schema_editor):
    AssetType = apps.get_model('assets', 'AssetType')
    Placement = apps.get_model('assets', 'Placement')
    AssetType.objects.all().delete()
    Placement.objects.all().delete()

class Migration(migrations.Migration):
    dependencies = [
        ('assets', '0003_asset_details'),
    ]

    operations = [
        migrations.RunPython(create_initial_data, remove_initial_data)
    ]