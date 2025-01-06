from django import forms
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Submit, Row, Column
from ..models import Asset, Category, AssetType
from ..choices import ASSET_TYPES, STATUS_CHOICES, MANUFACTURERS

class AssetForm(forms.ModelForm):
    asset_type_choice = forms.ChoiceField(
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
        fields = ['asset_type_choice', 'asset_tag', 'name', 'category', 'manufacturer', 'model', 
                 'serial_number', 'purchase_date', 'purchase_cost', 
                 'warranty_expiry', 'status', 'location', 'notes']
        widgets = {
            'purchase_date': forms.DateInput(attrs={'type': 'date', 'class': 'w-full px-3 py-2 border rounded-lg'}),
            'warranty_expiry': forms.DateInput(attrs={'type': 'date', 'class': 'w-full px-3 py-2 border rounded-lg'}),
            'notes': forms.Textarea(attrs={'rows': 3, 'class': 'w-full px-3 py-2 border rounded-lg'}),
            'status': forms.Select(choices=STATUS_CHOICES, attrs={'class': 'w-full px-3 py-2 border rounded-lg'}),
            'asset_tag': forms.TextInput(attrs={'class': 'w-full px-3 py-2 border rounded-lg'}),
            'name': forms.TextInput(attrs={'class': 'w-full px-3 py-2 border rounded-lg'}),
            'model': forms.TextInput(attrs={'class': 'w-full px-3 py-2 border rounded-lg'}),
            'serial_number': forms.TextInput(attrs={'class': 'w-full px-3 py-2 border rounded-lg'}),
            'location': forms.TextInput(attrs={'class': 'w-full px-3 py-2 border rounded-lg'}),
            'purchase_cost': forms.NumberInput(attrs={'class': 'w-full px-3 py-2 border rounded-lg'}),
            'category': forms.Select(attrs={'class': 'w-full px-3 py-2 border rounded-lg'})
        }

    def __init__(self, *args, **kwargs):
        instance = kwargs.get('instance')
        if instance:
            # If editing existing asset, set initial asset_type_choice
            initial = kwargs.get('initial', {})
            initial['asset_type_choice'] = instance.asset_type.code if instance.asset_type else 'laptop'
            kwargs['initial'] = initial
            
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_method = 'post'
        
        # Update category choices from database
        self.fields['category'].queryset = Category.objects.all()
        
        self.helper.layout = Layout(
            Row(
                Column('asset_type_choice', css_class='md:col-span-1'),
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

    def save(self, commit=True):
        instance = super().save(commit=False)
        
        # Get or create AssetType based on the choice
        asset_type_code = self.cleaned_data['asset_type_choice']
        asset_type, _ = AssetType.objects.get_or_create(
            code=asset_type_code,
            defaults={'name': dict(ASSET_TYPES)[asset_type_code]}
        )
        instance.asset_type = asset_type
        
        if commit:
            instance.save()
        return instance

    class Media:
        js = ('assets/js/asset_form.js',)