"""
Add detailed asset tracking fields

This migration adds new models and fields for detailed asset tracking including
brand, model, SKU, tag number, type, placement, and person in charge information.
"""

from django.db import migrations, models
import django.db.models.deletion

class Migration(migrations.Migration):
    dependencies = [
        ('assets', '0002_initial_categories'),
    ]

    operations = [
        migrations.CreateModel(
            name='AssetType',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('code', models.CharField(max_length=10, unique=True)),
                ('description', models.TextField(blank=True)),
            ],
            options={
                'verbose_name': 'Asset Type',
                'verbose_name_plural': 'Asset Types',
            },
        ),
        migrations.CreateModel(
            name='Placement',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('code', models.CharField(max_length=10, unique=True)),
                ('description', models.TextField(blank=True)),
            ],
        ),
        migrations.AddField(
            model_name='asset',
            name='brand',
            field=models.CharField(max_length=100, default=''),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='asset',
            name='sku',
            field=models.CharField(max_length=100, blank=True),
        ),
        migrations.AddField(
            model_name='asset',
            name='tag_number',
            field=models.CharField(max_length=50, unique=True, default=''),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='asset',
            name='person_in_charge',
            field=models.CharField(max_length=200, blank=True),
        ),
        migrations.AddField(
            model_name='asset',
            name='asset_type',
            field=models.ForeignKey(to='assets.assettype', on_delete=models.PROTECT, null=True),
        ),
        migrations.AddField(
            model_name='asset',
            name='placement',
            field=models.ForeignKey(to='assets.placement', on_delete=models.PROTECT, null=True),
        ),
    ]