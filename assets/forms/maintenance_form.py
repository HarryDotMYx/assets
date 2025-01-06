from django import forms
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Submit, Row, Column
from ..models import Maintenance

class MaintenanceForm(forms.ModelForm):
    class Meta:
        model = Maintenance
        fields = ['asset', 'maintenance_type', 'description', 'maintenance_date',
                 'cost', 'performed_by', 'next_maintenance_date', 'notes']
        widgets = {
            'maintenance_date': forms.DateInput(attrs={'type': 'date'}),
            'next_maintenance_date': forms.DateInput(attrs={'type': 'date'}),
            'description': forms.Textarea(attrs={'rows': 3}),
            'notes': forms.Textarea(attrs={'rows': 3}),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_method = 'post'
        self.helper.layout = Layout(
            Row(
                Column('asset', css_class='md:col-span-1'),
                Column('maintenance_type', css_class='md:col-span-1'),
                css_class='grid grid-cols-1 md:grid-cols-2 gap-4'
            ),
            'description',
            Row(
                Column('maintenance_date', css_class='md:col-span-1'),
                Column('cost', css_class='md:col-span-1'),
                Column('performed_by', css_class='md:col-span-1'),
                css_class='grid grid-cols-1 md:grid-cols-3 gap-4'
            ),
            'next_maintenance_date',
            'notes',
            Submit('submit', 'Save Maintenance Record', css_class='bg-blue-500 hover:bg-blue-600 text-white px-4 py-2 rounded-lg')
        )