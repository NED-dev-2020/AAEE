# Generated by Django 3.1.1 on 2021-04-08 08:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Service', '0002_actualite_contact'),
    ]

    operations = [
        migrations.AlterField(
            model_name='actualite',
            name='images',
            field=models.FileField(max_length=300, upload_to=''),
        ),
    ]
