"""
Create initial categories

This migration creates the initial set of asset categories.
"""

from django.db import migrations

def create_initial_categories(apps, schema_editor):
    Category = apps.get_model('assets', 'Category')
    
    categories = [
        {
            'name': 'Computer Equipment',
            'code': 'COMP',
            'description': 'Includes laptops, desktops, servers, and workstations'
        },
        {
            'name': 'Network Equipment',
            'code': 'NET',
            'description': 'Routers, switches, access points, and network infrastructure'
        },
        {
            'name': 'Peripherals',
            'code': 'PERI',
            'description': 'Keyboards, mice, monitors, printers, and scanners'
        },
        {
            'name': 'Storage Devices',
            'code': 'STOR',
            'description': 'External drives, NAS devices, and storage systems'
        },
        {
            'name': 'Power Equipment',
            'code': 'PWR',
            'description': 'UPS systems, power distribution units, and generators'
        }
    ]
    
    for data in categories:
        Category.objects.create(**data)

def remove_categories(apps, schema_editor):
    Category = apps.get_model('assets', 'Category')
    Category.objects.all().delete()

class Migration(migrations.Migration):
    dependencies = [
        ('assets', '0001_initial'),
    ]

    operations = [
        migrations.RunPython(create_initial_categories, remove_categories)
    ]