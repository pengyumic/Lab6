from django.forms import Select
from django import forms
from .models import User

class UserForm(forms.ModelForm):

    class Meta:
        model = User
        fields = '__all__'
        widgets = {
          'sel_schd': Select(attrs={'size':'3'}),
        }
