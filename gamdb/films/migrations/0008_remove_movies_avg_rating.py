# Generated by Django 4.1.7 on 2023-04-25 07:41

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('films', '0007_actor_comment_director_slug_movies_avg_rating_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='movies',
            name='avg_rating',
        ),
    ]
