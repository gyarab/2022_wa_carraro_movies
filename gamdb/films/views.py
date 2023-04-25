from django.shortcuts import render
from .models import Movies, Director, Genre, Actor

def directors(request):
    context = {
        'logic': True,
        'title': "Nejoblíbenější režiséři",
        'directors': Director.objects.all()
    }
    print(context)
    return render(request, 'directors.html', context)
def director(request):
    context = {
        'logic': True,
        'title': "Nejoblíbenější režiséři",
        'directors': Director.objects.all()
    }
    print(context)
    return render(request, 'directors.html', context)

    
def movies(request):
    movies_querystring = Movies.objects.all()
    genre = request.GET.get('genre')
    search = request.GET.get('search')
    if search:
        movies_querystring = movies_querystring.filter(name__icontains=search)
    if genre:
        movies_querystring = movies_querystring.filter(genres__name=genre)
    context = {
        "movies": movies_querystring,
        "genres": Genre.objects.all().order_by('name'),
        "genre": genre,
        "search":search,
    }
    return render(request, 'movies.html', context)

def movie(request,id):
    context = {
        "movies": Movies.objects.all()
    }
    return render(request, 'movies.html', context)

def actor(request):
    context = {
        "movies": Actor.objects.all()
    }
    return render(request, 'actors.html', context)

def homepage(request):
    #return HttpResponse("HELLOOO")
    context ={
        'movies':Movies.objects.all(),
    }
    return render(request,'main.html',context)

