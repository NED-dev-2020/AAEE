from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.core.mail import send_mail
from django.conf import settings
from emails.mailsend.mailsend import mailsend
from django.http import HttpResponseRedirect
from django.contrib import messages

from django.contrib.auth.models import User, auth
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic.edit import CreateView
from django.urls import reverse

from .models import*
from Service.models import*
from News_membres.models import*

def home(request):
    post_cat = Categorie.objects.all().order_by('-id')[:8]
    post_actu = Actualite.objects.all().order_by('-id')[:3]

    urlvideo = urlVideoAccueil.objects.filter().order_by('-id')[:1]
    return render(request, 'index.html',{'recen':post_actu,'cle_cat':post_cat, 'urlvideo':urlvideo})

@login_required(login_url='/connexion/login/')
def profil_etudiant(request):
    try:
        if request.user.useradmin.droit != 'super-user':
            pass
        else:
            return HttpResponseRedirect('/')
    except:
        return HttpResponseRedirect('/')

    pub = Pub.objects.filter().order_by('-id')
    ann = Annonce.objects.filter().order_by('-id')[:9]
    return render(request, 'dash/profil.html', {'ann':ann, 'pub':pub})


@login_required(login_url='/connexion/login/')
def annonce(request):

    pub = Pub.objects.filter().order_by('-id')
    ann = Annonce.objects.filter().order_by('-id')
    return render(request, 'dash/annonce.html', {'ann':ann, 'pub':pub})


@login_required(login_url='/connexion/login/')
def detail_annonce(request, id):

    pub = Pub.objects.filter().order_by('-id')
    ann = Annonce.objects.get(pk=id)
    return render(request, 'dash/detail_news.html', {'ann':ann, 'pub':pub})


class message_scolarite(LoginRequiredMixin, CreateView):

    model = MessageEtudiant
    fields = ['objet', 'message', 'fichier']

        
    def form_valid(self, form):

        form.instance.etudiant = self.request.user

        return super(message_scolarite, self).form_valid(form)

    def get_success_url(self): 

        return reverse('profil_etudiant')


class edite_profil(LoginRequiredMixin, CreateView):

    model = EtudiantsInscrit
    fields = ['profil','nom','prenom', 'promotion','option','pays_residence','tel','email', 'societe', 'secteur']
    
    def form_valid(self, form):

        form.instance.utilisateur = self.request.user

        return super(edite_profil, self).form_valid(form)

    def get_success_url(self): 

        return reverse('profil_etudiant')

def register(request):

    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']
        password1 = request.POST['password1']
        password2 = request.POST['password2']

        if len(username) >0 and len(email) >0 and len(password1) >0 and len(password2) >0:
            if password1==password2:

                if len(password1) >= 5:
                    if password1 != '01234' and password1 != '12345' and password1 != '54321' and password1 != username:

                        if User.objects.filter(email=email).exists():
                            messages.success(request, "Il existe déjà un compte avec cette adresse email.")
                            return HttpResponseRedirect('register')

                        elif User.objects.filter(username=username).exists():
                            messages.success(request, "Il existe déjà un compte avec ce nom d'utilisateur. Merci d'en choisir un autre.")
                            return HttpResponseRedirect('register')

                        else:
                            user = User.objects.create_user(username=username, email=email, password=password1)
                            user.save()

                            send_mail(
                                "Inscription d'un membre | AAEE ",
                                "Membre inscrit sur le nom d'utilisateur de "+username+', son addresse mail est '+email,
                                email,
                                mailsend,
                                )


                            send_mail(
                                "Bienvenue dans l'AAEE (l'Association des anciens etudiants de l'ECES)",
                                'Connectez-vous et completez votre profil afin de profiter de votre compte AAEE!',
                                email,
                                [email],
                                )

                            messages.success(request, "Compte crée avec succes! connectez-vous pour completer votre profil")
                            return HttpResponseRedirect('/')
                    else:
                        messages.success(request, "Mot de passe trop faible")
                        return HttpResponseRedirect('register')
                else:
                    messages.success(request, "Mot de passe trop court")
                    return HttpResponseRedirect('register')
            else:
                messages.success(request, 'Les deux champs de mot de passe ne correspondent pas.')
                return HttpResponseRedirect('register')
        else:
            messages.success(request, 'Veillez remplir tous les champs.')
            return HttpResponseRedirect('register')
    else:
        return render(request, 'registration/register.html')



