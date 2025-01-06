"""
Remove brand field and use manufacturer field instead

This migration removes the redundant brand field since we already have manufacturer field.
"""

from django.db import migrations

class Migration(migrations.Migration):
    dependencies = [
        ('assets', '0004_initial_asset_types'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='asset',
            name='brand',
        ),
    ]