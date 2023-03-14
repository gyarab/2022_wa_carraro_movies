from django.contrib import admin
from.models import Movies

# Register your models here
class MoviesAdmin(admin.ModelAdmin):#trida 
    list_display=['id','name','year']#ktere atributy budou zobrazene
    list_display_links=['name']# ktere atributy budou klikaci
    search_fields=['id','name','description']#podle ceho budu moct vyhledavat
admin.site.register(Movies,MoviesAdmin)