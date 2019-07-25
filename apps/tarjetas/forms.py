from django import forms
from django.contrib.auth.forms import UserCreationForm
from apps.tarjetas.models import Personaje, Tarjeta


class PersonajeForm(UserCreationForm):
    class Meta:
        model = Personaje
        fields = (
        	'name'
            'info') 
        labels=  {
        'name': 'Nombre de Personaje',
        'info': 'Información de Personaje',
        }
        widgets = {
            'name': forms.TextInput(attrs={'class':'form-control'}),
            'info': forms.TextInput(attrs={'class':'form-control'})

        }