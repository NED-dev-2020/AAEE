from django.db import models

from django_countries.fields import CountryField
from django.utils.safestring import mark_safe
from django.contrib.auth.models import User

from datetime import*

class EtudiantsInscrit(models.Model):
    
    utilisateur = models.OneToOneField(User, null=True, on_delete=models.CASCADE, related_name="etudiant")

    profil = models.FileField(upload_to='Profil_etudiant')

    nom = models.CharField(max_length=50)
    prenom = models.CharField(max_length=60)
    promotion = models.IntegerField()

    LISTE_OPTION = (
        ('Langues et Affaires', 'Langues et Affaires'),
        ('Management QSE', 'Management QSE'),
        ('Banque, Finances et Assurances', 'Banque, Finances et Assurances'),
        ("Comptabilité et Gestion d'Entreprise", "Comptabilité et Gestion d'Entreprise"),
        ('Transport et Logistique', 'Transport et Logistique'),
        ('Maintenance Industrielle', 'Maintenance Industrielle'),
        ('Electricité Industrielle', 'Electricité Industrielle'),
        ('Génie Informatique', 'Génie Informatique'),
        ('Ressources Humaines', 'Ressources Humaines'),
        ('Secretariat de Direction', 'Secretariat de Direction'),
        ('Communication et Multi-média', 'Communication et Multi-média'),
        ('Traduction et Interpretariat', 'Traduction et Interpretariat'),
        ('Administration des Affaires', 'Administration des Affaires'),
        ('Informatique et Technologies Numériques', 'Informatique et Technologies Numériques'),
        ('Electromécanique', 'Electromécanique'),
        ('Chaine de la logistique', 'Chaine de la logistique'),
        ('Commerce international et Marketing', 'Commerce international et Marketing'),
    )

    option = models.CharField(max_length=100, choices=LISTE_OPTION)
    pays_residence = CountryField()
    tel = models.CharField('Téléphone', max_length=25)
    email = models.EmailField()

    societe = models.CharField(null=True, blank=True, max_length=150)

    secteur = models.CharField("secteur d'expertise", max_length=150)

    date_inscrit = models.DateField(auto_now_add=True)

    def __str__(self):
        return f"{self.nom} {self.prenom} (Promotion {self.promotion}, {self.option})"
    
    def photo(self):
        if self.profil.url is not None:
            return mark_safe('<img src="{}" height="50" width="60"/>'.format(self.profil.url))
        else:
            return ""

class MessageEtudiant(models.Model):
    etudiant = models.ForeignKey(User(), on_delete=models.CASCADE)
    objet = models.CharField(max_length=100)
    message = models.TextField()
    fichier = models.FileField(null=True, blank=True)

    date_message = models.DateField(auto_now_add=True)