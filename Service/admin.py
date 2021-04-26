from django.contrib import admin
from .models import *

# Register your models here.


#_____________________Register Album_______________________
class AlbumAdmin(admin.ModelAdmin):
	list_display = ('titre','categorie','date_post')
	
admin.site.register(Album,AlbumAdmin)
#___________________________________________________________


#___________________Register Categorie______________________
class CategorieAdmin(admin.ModelAdmin):
	list_display = ('nom',)
admin.site.register(Categorie,CategorieAdmin)
#___________________________________________________________


#_____________________Register Contactez____________________
class ContactAdmin(admin.ModelAdmin):
	list_display = ('nom','prenom','email','objet','date_env')

	readonly_fields = ('nom','prenom','email','objet','message','date_env')
admin.site.register(Contact,ContactAdmin)
#___________________________________________________________


#______________________Register Actualite___________________

class ActualiteAdmin(admin.ModelAdmin):
	list_display = ('titre','date_pub')
admin.site.register(Actualite,ActualiteAdmin)
#____________________________________________________________

admin.site.register(urlVideoAccueil)