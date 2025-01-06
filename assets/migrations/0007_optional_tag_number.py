"""
Make tag_number field optional

This migration makes the tag_number field optional by setting null and blank to True.
"""

from django.db import migrations, models

class Migration(migrations.Migration):
    dependencies = [
        ('assets', '0006_optional_sku'),
    ]

    operations = [
        migrations.AlterField(
            model_name='asset',
            name='tag_number',
            field=models.CharField(max_length=50, unique=True, null=True, blank=True),
        ),
    ]