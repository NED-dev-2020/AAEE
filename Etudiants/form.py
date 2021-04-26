from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import*


class Register(UserCreationForm):
    class Meta:
        model = EtudiantsInscrit
        fields = (
            'utilisateur__username',
            'utilisateur__password1',
            'utilisateur__password2',
            
            'profil','utilisateur','nom','prenom',
            'promotion','option','pays_residence','tel',
            'email', 'societe', 'secteur', 'date_inscrit'
        )