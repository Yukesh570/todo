from django import forms
from django.forms import ModelForm
from django.forms import inlineformset_factory

from .models import *

class detailform (forms.ModelForm):
    class Meta:
        model = Persondetail
        fields='__all__'
        # exclude = ['phoneno', 'email']

# class emailform (forms.ModelForm):
#     class Meta:
#         model = Email
#         fields='__all__'

# class phoneform (forms.ModelForm):
#     class Meta:
#         model = PhoneNO
#         fields='__all__'


class searchform(forms.ModelForm):
    class Meta:
        model = searchform  # Specify your model class here
        fields = ['query']  # Specify the fields you want to include in the form

    query = forms.CharField(label='Search')

# PersonDetailFormSet = inlineformset_factory(
# Persondetail, 
# PhoneNO, 
# form=phoneform, 
# fields=('Number', 'Phonetype'),
# extra=1
# )

# EmailFormSet = inlineformset_factory(
# Persondetail, 
# Email, 
# form=emailform, 
# fields=('email', 'emailtype'),
# extra=1
# )