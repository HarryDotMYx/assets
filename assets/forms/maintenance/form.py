from django import forms
from crispy_forms.helper import FormHelper
from ...models import Maintenance
from .fields import MaintenanceFields
from .layout import get_maintenance_layout

class MaintenanceForm(forms.ModelForm, MaintenanceFields):
    class Meta:
        model = Maintenance
        fields = [
            'asset', 'maintenance_type', 'description', 
            'maintenance_date', 'cost', 'performed_by',
            'next_maintenance_date', 'notes'
        ]

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_method = 'post'
        self.helper.layout = get_maintenance_layout()