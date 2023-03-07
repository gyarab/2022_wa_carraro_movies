from django.db import models

class Movies(models.Model):
    name = models.CharField(max_length=200)
    year = models.IntegerField()
    description = models.TextField()

# Create your models here.
