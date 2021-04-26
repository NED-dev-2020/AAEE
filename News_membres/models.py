from django.db import models
from ckeditor.fields import RichTextField
from datetime import*

class Annonce(models.Model):
	images = models.FileField(upload_to='annonce')
	
	titre = models.CharField(max_length=100)
	text = RichTextField()

	date_pub = models.DateField(auto_now_add=True)

	def __str__(self):
		return f'{self.titre}'

class Pub(models.Model):
	text = RichTextField()
	activer = models.BooleanField(default=True)

	date_pub = models.DateField(auto_now_add=True)