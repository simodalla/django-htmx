# Generated by Django 4.0.6 on 2022-08-12 16:54

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("films", "0003_alter_film_options_userfilms"),
    ]

    operations = [
        migrations.AddField(
            model_name="film",
            name="users",
            field=models.ManyToManyField(
                related_name="films", through="films.UserFilms", to=settings.AUTH_USER_MODEL
            ),
        ),
    ]
