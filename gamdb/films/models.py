from django.db import models# models = reprezentace databaze

class Movies(models.Model):
    name = models.CharField(max_length=200)
    year = models.IntegerField(blank=True,null=True)
    description = models.TextField(blank=True)#blank=true je ze neni povinne
    director = models.ForeignKey('Director',blank=True,null=True,on_delete=models.SET_NULL)
    genres = models.ManyToManyField('Genre')#manytomanyfield propoji ty tabulky n:m

    def __str__(self):#def metoda __str__ jmeno metody (self) jako prvni metoda v pythonu dostava jako parametr sama sebe
        return f"{self.name}({self.year})"
    def genre_display(self):
        return ", ".join([i.name for i in self.genres.all()])
class Director(models.Model):
    name = models.CharField(max_length=100)
    birth_year = models.IntegerField(blank=True,null=True)

    def __str__(self):
        return f"{self.name}({self.birth_year})"
class Genre(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return f"{self.name}"
# Create your models here.
