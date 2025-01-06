"""
Make SKU field optional

This migration makes the SKU field optional by setting null and blank to True.
"""

from django.db import migrations, models

class Migration(migrations.Migration):
    dependencies = [
        ('assets', '0005_remove_brand_field'),
    ]

    operations = [
        migrations.AlterField(
            model_name='asset',
            name='sku',
            field=models.CharField(max_length=100, null=True, blank=True),
        ),
    ]