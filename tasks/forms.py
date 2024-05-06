from django import forms
from django.forms import ModelForm
from django.forms.models import inlineformset_factory
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

from .models import *

class emailform (forms.ModelForm):
    class Meta:
        model = Email
        fields='__all__'

class phoneform (forms.ModelForm):
    class Meta:
        model = PhoneNO
        fields='__all__'


class CreateUserForm(UserCreationForm):
    class Meta:
        model=User
        fields=['username','email','password1','password2','first_name','last_name']


# Phoneformset = inlineformset_factory(
#     Persondetail ,PhoneNO , form=phoneform,extra=1,can_delete=True, fk_name='Persondetail'
# )
# Emailformset= inlineformset_factory(
#     Persondetail ,Email , form=emailform,extra=1,can_delete=True
# )

class detailform (forms.ModelForm):
    class Meta:
        model = Persondetail
        fields='__all__'
        # exclude = ['phoneno', 'email']
    # def __init__(self, *args, **kwargs):
    #     super(detailForm, self).__init__(*args, **kwargs)
    #     self.fields['phoneno'] = Phoneformset(instance=self.instance)
    #     self.fields['email'] = Emailformset(instance=self.instance)




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