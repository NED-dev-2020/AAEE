from django.contrib import admin
from django.urls import path, include


admin.site.site_title= ' '
admin.site.site_header= "AAEE"
admin.site.index_title= "Association des Anciens Etudiants de l'ECES."

urlpatterns = [

    path('connexion/', include('django.contrib.auth.urls')),
    path('AAEE2021@ECES/dmin/', admin.site.urls),

    path('', include('Etudiants.urls')),
    path('service/', include('Service.urls')),
]

from django.conf.urls.static import*
from django.conf import settings

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)+ static(settings.STATIC_URL,document_root=settings.STATIC_ROOT)

