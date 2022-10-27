from django import forms
from django.contrib.auth.forms import UserCreationForm

from .models import *
class InterventionForm(forms.ModelForm):
    CHOICES = (
        ('Fait', 'Fait'),
        ('en attendant', 'en attendant'),
        ('annulée', 'annulée'),

    )
    Status = forms.CharField(widget=forms.Select(choices=CHOICES))
    class Meta :
        model = Intervention
        fields = ['Nom_Client', 'Numéro', 'Ville', 'Date','Address','Code_postal','Commentaire','Prix','Par',]

class ClientForm(forms.ModelForm):
    class Meta :
        model = Client
        fields = '__all__'



class SignUpForm(UserCreationForm):
    Nom = forms.CharField(max_length=30, required=False, help_text='Optional.')
    Prénom = forms.CharField(max_length=30, required=False, help_text='Optional.')
    email = forms.EmailField(max_length=254, help_text='Required. Inform a valid email address.')

    class Meta:
        model = User
        fields = ('username', 'Nom', 'Prénom', 'email', 'password1', 'password2', )