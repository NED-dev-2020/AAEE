# Generated by Django 3.2 on 2021-04-23 22:45

import ckeditor.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('News_membres', '0002_rename_description_annonce_text'),
    ]

    operations = [
        migrations.CreateModel(
            name='Pub',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', ckeditor.fields.RichTextField()),
                ('activer', models.BooleanField(default=True)),
                ('date_pub', models.DateField(auto_now_add=True)),
            ],
        ),
    ]
