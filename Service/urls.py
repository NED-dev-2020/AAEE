from django.urls import path
from . import views

urlpatterns = [
     path('vae/',views.vae,name='vae'),

     path('actual/',views.actualite,name='post_actualite'),
     path('actualite/<int:id>/detail/', views.detail_actualite, name="detail_actualite"),

     path('detail/<str:nom>/',views.detail_album,name='album_by_categorie'),
     
     path('contact',views.contact,name='contact'),

     path('about/',views.about,name='about'),
     path('liens/',views.lien,name='liens'),
]