from django import forms
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Submit, Row, Column
from ..models import Asset, Category, AssetType

class AssetForm(forms.ModelForm):
    vendor = forms.CharField(
        max_length=200,
        required=False,
        widget=forms.TextInput(attrs={
            'class': 'w-full px-3 py-2 border rounded-lg focus:ring-2 focus:ring-blue-500 focus:border-blue-500',
            'placeholder': 'Enter vendor name'
        })
    )
    
    class Meta:
        model = Asset
        fields = ['asset_tag', 'category', 'manufacturer', 'model', 
                 'vendor', 'serial_number', 'purchase_date', 'purchase_cost', 
                 'warranty_expiry', 'status', 'location', 'notes']
        widgets = {
            'purchase_date': forms.DateInput(attrs={
                'type': 'date',
                'class': 'w-full px-3 py-2 border rounded-lg'
            }),
            'warranty_expiry': forms.DateInput(attrs={
                'type': 'date',
                'class': 'w-full px-3 py-2 border rounded-lg'
            }),
            'notes': forms.Textarea(attrs={
                'rows': 3,
                'class': 'w-full px-3 py-2 border rounded-lg'
            }),
            'asset_tag': forms.TextInput(attrs={'class': 'w-full px-3 py-2 border rounded-lg'}),
            'model': forms.TextInput(attrs={'class': 'w-full px-3 py-2 border rounded-lg'}),
            'serial_number': forms.TextInput(attrs={'class': 'w-full px-3 py-2 border rounded-lg'}),
            'location': forms.TextInput(attrs={'class': 'w-full px-3 py-2 border rounded-lg'}),
            'purchase_cost': forms.NumberInput(attrs={'class': 'w-full px-3 py-2 border rounded-lg'}),
            'category': forms.Select(attrs={'class': 'w-full px-3 py-2 border rounded-lg'}),
            'manufacturer': forms.Select(attrs={'class': 'w-full px-3 py-2 border rounded-lg'}),
            'status': forms.Select(attrs={'class': 'w-full px-3 py-2 border rounded-lg'})
        }