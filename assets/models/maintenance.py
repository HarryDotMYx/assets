from django.db import models
from .asset import Asset

class Maintenance(models.Model):
    asset = models.ForeignKey(Asset, on_delete=models.PROTECT)
    maintenance_type = models.CharField(max_length=100)
    description = models.TextField()
    maintenance_date = models.DateField()
    cost = models.DecimalField(max_digits=10, decimal_places=2)
    performed_by = models.CharField(max_length=200)
    next_maintenance_date = models.DateField(null=True, blank=True)
    notes = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.asset} - {self.maintenance_type}"