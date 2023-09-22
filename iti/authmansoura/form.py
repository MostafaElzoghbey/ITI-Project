from django import forms
from .models import Myaccount
from students.models import *


class updateprofile(forms.ModelForm):
    class Meta:
        model = Myaccount
        fields = '__all__'


class Newbookform(forms.ModelForm):
    class Meta:
        model=books
        fields='__all__'
