from django.db import models
from .category import Category
from .asset_type import AssetType
from .placement import Placement

class Asset(models.Model):
    STATUS_CHOICES = [
        ('available', 'Available'),
        ('assigned', 'Assigned'),
        ('maintenance', 'Under Maintenance'),
        ('retired', 'Retired')
    ]

    asset_tag = models.CharField(max_length=50, unique=True)
    name = models.CharField(max_length=200)
    category = models.ForeignKey(Category, on_delete=models.PROTECT)
    asset_type = models.ForeignKey(AssetType, on_delete=models.PROTECT, null=True)
    placement = models.ForeignKey(Placement, on_delete=models.PROTECT, null=True)
    manufacturer = models.CharField(max_length=100)
    model = models.CharField(max_length=100)
    sku = models.CharField(max_length=100, null=True, blank=True)
    serial_number = models.CharField(max_length=100, unique=True)
    purchase_date = models.DateField()
    purchase_cost = models.DecimalField(max_digits=10, decimal_places=2)
    warranty_expiry = models.DateField(null=True, blank=True)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='available')
    location = models.CharField(max_length=200)
    notes = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    person_in_charge = models.CharField(max_length=200, blank=True)

    def __str__(self):
        return f"{self.asset_tag} - {self.name}"

    def to_dict(self):
        """Convert asset instance to dictionary for JSON serialization"""
        return {
            'id': self.id,
            'asset_tag': self.asset_tag,
            'name': self.name,
            'category': str(self.category),
            'manufacturer': self.manufacturer,
            'model': self.model,
            'serial_number': self.serial_number,
            'status': self.get_status_display(),
            'location': self.location,
            'notes': self.notes,
            'person_in_charge': self.person_in_charge,
            'purchase_date': self.purchase_date.isoformat() if self.purchase_date else None,
            'warranty_expiry': self.warranty_expiry.isoformat() if self.warranty_expiry else None,
        }