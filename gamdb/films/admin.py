from django.contrib import admin
from.models import Movies
from.models import Director, Actor,Comment
from.models import Genre

# Register your models here
class MoviesAdmin(admin.ModelAdmin):#trida 
    list_display=['id','name','year','director']#ktere atributy budou zobrazene
    list_display_links=['name']# ktere atributy budou klikaci
    list_filter=['genres']
    search_fields=['id','name','description']#podle ceho budu moct vyhledavat
admin.site.register(Movies,MoviesAdmin)

class DirectorAdmin(admin.ModelAdmin):
    list_display=['id','name','birth_year']
    list_display_links=['name']
admin.site.register(Director,DirectorAdmin)
admin.site.register(Actor)
admin.site.register(Comment)

admin.site.register(Genre)