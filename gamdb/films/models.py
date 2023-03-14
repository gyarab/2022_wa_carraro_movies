from django.db import models

class Movies(models.Model):
    name = models.CharField(max_length=200)
    year = models.IntegerField()
    description = models.TextField()

    def __str__(self):#def metoda __str__ jmeno metody (self) jako prvni metoda v pythonu dostava jako parametr sama sebe
        return f"{self.name}({self.year})"

# Create your models here.
