from django.contrib import admin
from .models import*

@admin.register(EtudiantsInscrit)
class EtudiantsInscritAdmin(admin.ModelAdmin):

    list_display = ('nom', 'prenom','promotion','option','photo')

    readonly_fields = ('profil','utilisateur','nom','prenom', 'promotion','option','pays_residence','tel','email', 'societe', 'secteur', 'date_inscrit')

    can_delete = False

    list_filter=('option',)
    search_fields=('nom','prenom', 'utilisateur__username')


@admin.register(MessageEtudiant)
class MessageEtudiantAdmin(admin.ModelAdmin):

    list_display = ('etudiant', 'objet','date_message')

    readonly_fields = ('etudiant','objet','fichier','message','date_message')

    can_delete = False

    list_filter=('date_message',)
    search_fields=('etudiant','objet', 'message')