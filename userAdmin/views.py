from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.contrib.auth.decorators import login_required

from Etudiants.models import EtudiantsInscrit

def verif():
	try:
		if request.user.useradmin.droit == 'super-user':
			pass
		else:
			return HttpResponseRedirect('/')
	except:
		return HttpResponseRedirect('/')


@login_required(login_url='/connexion/login/')
def listInscrit(request):

	verif()

	etudiant = EtudiantsInscrit.objects.filter().order_by('-id')

	template = 'userAdmin/list_inscrit.html'
	context = {
		'etudiant':etudiant
	}
	return render(request, template, context)