from django.urls import path
from .views import listInscrit

urlpatterns = [
	path('liste-etudiants/', listInscrit, name = 'listInscrit'),
]