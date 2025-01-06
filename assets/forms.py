from django import forms
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Submit, Row, Column
from .models import Asset, AssetAssignment, Maintenance
from .choices import ASSET_TYPES, STATUS_CHOICES, MANUFACTURERS

class AssetForm(forms.ModelForm):
    asset_type = forms.ChoiceField(
        choices=ASSET_TYPES,
        widget=forms.Select(attrs={'class': 'w-full px-3 py-2 border rounded-lg'}),
        initial='laptop'
    )
    
    manufacturer = forms.ChoiceField(
        choices=MANUFACTURERS['laptop'],
        widget=forms.Select(attrs={'class': 'w-full px-3 py-2 border rounded-lg'})
    )
    
    class Meta:
        model = Asset
        fields = ['asset_type', 'asset_tag', 'name', 'category', 'manufacturer', 'model', 
                 'serial_number', 'purchase_date', 'purchase_cost', 
                 'warranty_expiry', 'status', 'location', 'notes']
        widgets = {
            'purchase_date': forms.DateInput(attrs={'type': 'date'}),
            'warranty_expiry': forms.DateInput(attrs={'type': 'date'}),
            'notes': forms.Textarea(attrs={'rows': 3}),
            'status': forms.Select(choices=STATUS_CHOICES)
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_method = 'post'
        self.helper.layout = Layout(
            Row(
                Column('asset_type', css_class='md:col-span-1'),
                Column('asset_tag', css_class='md:col-span-1'),
                Column('name', css_class='md:col-span-1'),
                css_class='grid grid-cols-1 md:grid-cols-3 gap-4'
            ),
            Row(
                Column('category', css_class='md:col-span-1'),
                Column('status', css_class='md:col-span-1'),
                Column('location', css_class='md:col-span-1'),
                css_class='grid grid-cols-1 md:grid-cols-3 gap-4'
            ),
            Row(
                Column('manufacturer', css_class='md:col-span-1'),
                Column('model', css_class='md:col-span-1'),
                Column('serial_number', css_class='md:col-span-1'),
                css_class='grid grid-cols-1 md:grid-cols-3 gap-4'
            ),
            Row(
                Column('purchase_date', css_class='md:col-span-1'),
                Column('purchase_cost', css_class='md:col-span-1'),
                Column('warranty_expiry', css_class='md:col-span-1'),
                css_class='grid grid-cols-1 md:grid-cols-3 gap-4'
            ),
            'notes',
            Submit('submit', 'Save Asset', css_class='bg-blue-500 hover:bg-blue-600 text-white px-4 py-2 rounded-lg')
        )

    class Media:
        js = ('assets/js/asset_form.js',)