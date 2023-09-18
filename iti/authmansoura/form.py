from django import forms
from .models import Myaccount


class updateprofile(forms.ModelForm):
    class Meta:
        model = Myaccount
        fields = '__all__'
