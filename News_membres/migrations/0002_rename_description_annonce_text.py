# Generated by Django 3.2 on 2021-04-23 21:28

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('News_membres', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='annonce',
            old_name='description',
            new_name='text',
        ),
    ]
