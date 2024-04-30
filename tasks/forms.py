from django import forms
from django.forms import ModelForm

from .models import *

class detailform (forms.ModelForm):
    class Meta:
        model = Persondetail
        fields='__all__'


class searchform(forms.ModelForm):
    class Meta:
        model = searchform  # Specify your model class here
        fields = ['query']  # Specify the fields you want to include in the form

    query = forms.CharField(label='Search')