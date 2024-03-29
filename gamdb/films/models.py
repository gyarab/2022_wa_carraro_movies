from django.db import models# models = reprezentace databaze
from datetime import datetime

class Movie(models.Model):
    name = models.CharField(max_length=200)
    slug = models.SlugField()
    image_url = models.CharField(max_length=200,blank=True)
    year = models.IntegerField(blank=True,null=True)
    description = models.TextField(blank=True,null= True)#blank=true je ze neni povinne
    director = models.ForeignKey('Director',blank=True,null=True,on_delete=models.SET_NULL)
    genres = models.ManyToManyField('Genre')#manytomanyfield propoji ty tabulky n:m

    def __str__(self):#def metoda __str__ jmeno metody (self) jako prvni metoda v pythonu dostava jako parametr sama sebe
        return f"{self.name}({self.year})"
    def genre_display(self):
        return ", ".join([i.name for i in self.genres.all()])
class Actor(models.Model):
    name = models.CharField(max_length=100)
    slug = models.SlugField()
    birth_year = models.IntegerField(blank=True,null=True)
    photo_url = models.CharField(max_length=400, blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    def __str__(self):
        return f"{self.name}({self.birth_year})"
class Comment(models.Model):
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)
    author = models.CharField(max_length=255, blank=True)
    text = models.TextField(blank=True)
    rating = models.IntegerField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)


class Director(models.Model):
    name = models.CharField(max_length=100)
    slug = models.SlugField()
    birth_year = models.IntegerField(blank=True,null=True)

    def __str__(self):
        return f"{self.name}({self.birth_year})"
class Genre(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return f"{self.name}"
# Create your models here.
