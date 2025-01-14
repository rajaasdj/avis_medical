from django import forms
from .models import *

class AvisForm(forms.ModelForm):


    class Meta:
        model = Avis
        fields = ['emoji']
        widgets = {
            'emoji': forms.HiddenInput(),
            
        }
