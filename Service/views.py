from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib import messages
from django.core.mail import send_mail
from emails.mailsend.mailsend import mailsend
from django.conf import settings
from .models  import *
from .forms import *


def detail_album(request,nom):
	detail = Album.objects.filter(categorie__nom=nom)
	return render(request,'service/detail_galerie.html',{'cledetail':detail, 'nom':nom})

def contact(request):

	if request.method == "POST":
		nom = request.POST['nom']
		prenom = request.POST['prenom']
		email = request.POST['email']
		objet = request.POST['objet']
		message = request.POST['message']

		send_mail(
			'contact AAEE | objet : '+objet,
			'Message venant de '+nom+' '+prenom+' : '+message,
			email,
			mailsend,
			fail_silently=False,
			)

		forme = ContactForm(request.POST).save()
		messages.success(request, "Message envoyé avec succès")
		return redirect('contact')
	forme = ContactForm()

	return render(request,'service/contact.html',{'forms':forme})

def actualite(request):
	actual = Actualite.objects.all()
	return render(request,'service/actualite.html',{'cle_actu':actual})

def detail_actualite(request,id):
	detail_actu = Actualite.objects.get(pk=id)

	post_actu = Actualite.objects.all().order_by('-id')[:6]
	return render(request,'service/detail_actualite.html',{'cledetail_actu':detail_actu, 'post_actu':post_actu})

def about(request):
	return render(request, 'service/about.html')

def lien(request):
	return render(request, 'service/liens.html')

def vae(request):
	return render(request,'service/vae.html')

