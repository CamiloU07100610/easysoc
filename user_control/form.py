from .models import User_test
from django import forms
class UserForm(forms.ModelForm):
    class Meta:
        model = User_test
        fields = ['username', 'mail', 'password']