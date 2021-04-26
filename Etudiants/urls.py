from django.urls import path
from django.contrib.auth import views as auth_views
from .views import*


urlpatterns = [
    path('', home, name='home'),
    path('membres/profil/', profil_etudiant, name="profil_etudiant"),
    path('aaee/message/', message_scolarite.as_view(), name="message_scolarite"),
    path('membres/modifier/profil/', edite_profil.as_view(), name="edite_profil"),

    path('news/all/', annonce, name="annonce"),
	path('news/<int:id>/', detail_annonce, name="detail_annonce"),

    path('register', register, name="register"),

    path('reset/', auth_views.PasswordResetView.as_view(), name='reset_password'),
    path('reset-done/', auth_views.PasswordResetDoneView.as_view(), name='password_reset_done'),
    path('reset-confirm/<uidb54>/<token>/', auth_views.PasswordResetConfirmView.as_view(), name='password_reset_confirm'),
    path('reset-complet/', auth_views.PasswordResetCompleteView.as_view(), name='password_reset_complete'),
]