# Generated by Django 4.1.7 on 2023-03-21 10:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('films', '0004_genre_movies_genres'),
    ]

    operations = [
        migrations.AlterField(
            model_name='movies',
            name='genres',
            field=models.ManyToManyField(blank=True, null=True, to='films.genre'),
        ),
    ]
