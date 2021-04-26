from django.db import models
from datetime import datetime, date
from ckeditor.fields import RichTextField

# Create your models here.
class Categorie(models.Model):
	nom = models.CharField(max_length=30)
	images = models.FileField()

	def __str__(self):
		return self.nom

class Album(models.Model):
	titre = models.CharField(max_length=30, null=True, blank=True)
	categorie = models.ForeignKey(Categorie, default=None, null=True, on_delete=models.CASCADE)
	images = models.FileField()
	description = models.TextField(null=True, blank=True)
	date_post = models.DateField(auto_now_add=True)

	def __str__(self):
		return f" {self.titre} {self.categorie} {self.date_post}"

class Actualite(models.Model):
	titre = models.CharField(max_length=30)
	images = models.FileField()
	description = RichTextField()
	date_pub = models.DateField(auto_now_add=True)

	def __str__(self):
		return f" {self.titre} | {self.date_pub}"

class Contact(models.Model):
	nom = models.CharField(max_length=25)
	prenom = models.CharField(max_length=25)
	email = models.EmailField(null=True,blank=True)
	objet = models.CharField(max_length=35)
	message = models.TextField()
	date_env = models.DateField(auto_now_add=True)



	def __str__(self):
		return f" {self.nom} | {self.message} {self.date_env}"

class urlVideoAccueil(models.Model):
	url = models.TextField()

	def __str__(self):
			return f"{self.url}"


