"""
Add vendor field to Asset model

This migration adds a vendor field to store vendor information for assets.
"""

from django.db import migrations, models

class Migration(migrations.Migration):
    dependencies = [
        ('assets', '0010_remove_asset_tag_number_alter_asset_id_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='asset',
            name='vendor',
            field=models.CharField(blank=True, max_length=200),
        ),
    ]