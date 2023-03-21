# Generated by Django 4.1.7 on 2023-03-21 09:16

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('films', '0002_director'),
    ]

    operations = [
        migrations.AddField(
            model_name='movies',
            name='director',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='films.director'),
        ),
        migrations.AlterField(
            model_name='director',
            name='birth_year',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='movies',
            name='description',
            field=models.TextField(blank=True),
        ),
        migrations.AlterField(
            model_name='movies',
            name='year',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]