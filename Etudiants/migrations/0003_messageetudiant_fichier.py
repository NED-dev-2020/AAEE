# Generated by Django 3.2 on 2021-04-07 17:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Etudiants', '0002_messageetudiant'),
    ]

    operations = [
        migrations.AddField(
            model_name='messageetudiant',
            name='fichier',
            field=models.FileField(blank=True, null=True, upload_to=''),
        ),
    ]
