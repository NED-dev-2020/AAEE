# Generated by Django 3.2 on 2021-04-07 16:57

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django_countries.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='EtudiantsInscrit',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('profil', models.FileField(upload_to='Profil_etudiant')),
                ('nom', models.CharField(max_length=50)),
                ('prenom', models.CharField(max_length=60)),
                ('promotion', models.IntegerField()),
                ('option', models.CharField(choices=[('Langues et Affaires', 'Langues et Affaires'), ('Management QSE', 'Management QSE'), ('Banque, Finances et Assurances', 'Banque, Finances et Assurances'), ("Comptabilité et Gestion d'Entreprise", "Comptabilité et Gestion d'Entreprise"), ('Transport et Logistique', 'Transport et Logistique'), ('Maintenance Industrielle', 'Maintenance Industrielle'), ('Electricité Industrielle', 'Electricité Industrielle'), ('Génie Informatique', 'Génie Informatique'), ('Ressources Humaines', 'Ressources Humaines'), ('Secretariat de Direction', 'Secretariat de Direction'), ('Communication et Multi-média', 'Communication et Multi-média'), ('Traduction et Interpretariat', 'Traduction et Interpretariat'), ('Administration des Affaires', 'Administration des Affaires'), ('Informatique et Technologies Numériques', 'Informatique et Technologies Numériques'), ('Electromécanique', 'Electromécanique'), ('Chaine de la logistique', 'Chaine de la logistique'), ('Commerce international et Marketing', 'Commerce international et Marketing')], max_length=100)),
                ('pays_residence', django_countries.fields.CountryField(max_length=2)),
                ('tel', models.CharField(max_length=25, verbose_name='Téléphone')),
                ('email', models.EmailField(max_length=254)),
                ('societe', models.CharField(blank=True, max_length=150, null=True)),
                ('secteur', models.CharField(choices=[('Langues et Affaires', 'Langues et Affaires'), ('Management QSE', 'Management QSE'), ('Banque, Finances et Assurances', 'Banque, Finances et Assurances'), ("Comptabilité et Gestion d'Entreprise", "Comptabilité et Gestion d'Entreprise"), ('Transport et Logistique', 'Transport et Logistique'), ('Maintenance Industrielle', 'Maintenance Industrielle'), ('Electricité Industrielle', 'Electricité Industrielle'), ('Génie Informatique', 'Génie Informatique'), ('Ressources Humaines', 'Ressources Humaines'), ('Secretariat de Direction', 'Secretariat de Direction'), ('Communication et Multi-média', 'Communication et Multi-média'), ('Traduction et Interpretariat', 'Traduction et Interpretariat'), ('Administration des Affaires', 'Administration des Affaires'), ('Informatique et Technologies Numériques', 'Informatique et Technologies Numériques'), ('Electromécanique', 'Electromécanique'), ('Chaine de la logistique', 'Chaine de la logistique'), ('Commerce international et Marketing', 'Commerce international et Marketing'), ('Autre ...', 'Autre ...')], max_length=100, verbose_name="secteur d'expertise")),
                ('date_inscrit', models.DateField(auto_now_add=True)),
                ('utilisateur', models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='etudiant', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
