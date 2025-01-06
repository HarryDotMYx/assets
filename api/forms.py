from django import forms
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Submit

class LoginForm(forms.Form):
    email = forms.EmailField(
        widget=forms.EmailInput(attrs={'class': 'w-full px-3 py-2 border rounded-lg'})
    )
    password = forms.CharField(
        widget=forms.PasswordInput(attrs={'class': 'w-full px-3 py-2 border rounded-lg'})
    )

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_method = 'post'
        self.helper.layout = Layout(
            'email',
            'password',
            Submit('submit', 'Sign In', css_class='w-full py-2 text-white rounded-lg bg-gradient-to-r from-blue-500 to-purple-600 hover:opacity-90')
        )