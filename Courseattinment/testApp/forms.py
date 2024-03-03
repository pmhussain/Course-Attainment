from django import forms
from . models import *

class COForm(forms.ModelForm):
    class Meta:
        model = CO
        fields = '__all__'
