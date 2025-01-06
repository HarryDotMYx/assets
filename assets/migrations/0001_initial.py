"""
Initial migration for assets app

Creates the initial database schema including Category, Asset, AssetAssignment, and Maintenance models.
"""

from django.db import migrations, models
import django.db.models.deletion

class Migration(migrations.Migration):
    initial = True

    dependencies = [
        ('authentication', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('code', models.CharField(max_length=20, unique=True)),
                ('description', models.TextField(blank=True)),
            ],
            options={
                'verbose_name_plural': 'Categories',
            },
        ),
        migrations.CreateModel(
            name='Asset',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('asset_tag', models.CharField(max_length=50, unique=True)),
                ('name', models.CharField(max_length=200)),
                ('manufacturer', models.CharField(max_length=100)),
                ('model', models.CharField(max_length=100)),
                ('serial_number', models.CharField(max_length=100, unique=True)),
                ('purchase_date', models.DateField()),
                ('purchase_cost', models.DecimalField(decimal_places=2, max_digits=10)),
                ('warranty_expiry', models.DateField(blank=True, null=True)),
                ('status', models.CharField(choices=[('available', 'Available'), ('assigned', 'Assigned'), ('maintenance', 'Under Maintenance'), ('retired', 'Retired')], default='available', max_length=20)),
                ('location', models.CharField(max_length=200)),
                ('notes', models.TextField(blank=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='assets.category')),
            ],
        ),
        migrations.CreateModel(
            name='Maintenance',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('maintenance_type', models.CharField(max_length=100)),
                ('description', models.TextField()),
                ('maintenance_date', models.DateField()),
                ('cost', models.DecimalField(decimal_places=2, max_digits=10)),
                ('performed_by', models.CharField(max_length=200)),
                ('next_maintenance_date', models.DateField(blank=True, null=True)),
                ('notes', models.TextField(blank=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('asset', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='assets.asset')),
            ],
        ),
        migrations.CreateModel(
            name='AssetAssignment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('assigned_date', models.DateTimeField(auto_now_add=True)),
                ('return_date', models.DateTimeField(blank=True, null=True)),
                ('expected_return_date', models.DateField(blank=True, null=True)),
                ('notes', models.TextField(blank=True)),
                ('asset', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='assets.asset')),
                ('assigned_by', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='assignments_made', to='authentication.customuser')),
                ('assigned_to', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='authentication.customuser')),
            ],
        ),
    ]