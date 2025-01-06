from django import forms
from crispy_forms.helper import FormHelper
from ..models import AssetAssignment, Asset
from authentication.models import CustomUser

class AssetAssignmentForm(forms.ModelForm):
    asset = forms.ModelChoiceField(
        queryset=Asset.objects.filter(status='available'),
        empty_label="Select an asset",
        widget=forms.Select(attrs={
            'class': 'w-full px-3 py-2 border rounded-lg focus:ring-2 focus:ring-blue-500 focus:border-blue-500'
        })
    )
    
    assigned_to = forms.ModelChoiceField(
        queryset=CustomUser.objects.filter(is_active=True),
        empty_label="Select a user",
        widget=forms.Select(attrs={
            'class': 'w-full px-3 py-2 border rounded-lg focus:ring-2 focus:ring-blue-500 focus:border-blue-500'
        })
    )

    class Meta:
        model = AssetAssignment
        fields = ['asset', 'assigned_to', 'expected_return_date', 'notes']
        widgets = {
            'expected_return_date': forms.DateInput(
                attrs={
                    'type': 'date',
                    'class': 'w-full px-3 py-2 border rounded-lg focus:ring-2 focus:ring-blue-500 focus:border-blue-500'
                }
            ),
            'notes': forms.Textarea(
                attrs={
                    'rows': 3,
                    'class': 'w-full px-3 py-2 border rounded-lg focus:ring-2 focus:ring-blue-500 focus:border-blue-500'
                }
            )
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_method = 'post'
        
        # Only show available assets
        self.fields['asset'].queryset = Asset.objects.filter(status='available')
        
        # Show asset tag and name in dropdown
        self.fields['asset'].label_from_instance = lambda obj: f"{obj.asset_tag} - {obj.name}"