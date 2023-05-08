from django.shortcuts import render
from .models import Movies, Director, Genre, Actor, Comment
from django.db.models import Q
from .forms import CommentForm

def directors(request):
    c context = {
        'directors': Director.objects.all()
    }
    print(context)
    return render(request, 'directors.html', context)

def director(request):
    context = {
        "director": Director.objects.get(id=id)
    }
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
    m = Movie.objects.get(id=id)
    f = CommentForm()

    if request.POST:
        f = CommentForm(request.POST)
        if f.is_valid():
            # ulozit do DB
            c = Comment(
                movie=m,
                author=f.cleaned_data.get('author'),
                text=f.cleaned_data.get('text'),
                rating=f.cleaned_data.get('rating'),
            )
            if not c.author:
                c.author = 'Anonym'
            c.save()
            # nastavit prazdny form
            f = CommentForm()

    context = {
        "movie": m,
        "comments": Comment.objects.filter(movie=m).order_by('-created_at'),
        "form": f
    }
    return render(request, 'movies.html', context)

def actor(request):
    context = {
      "actor": Actor.objects.get(id=id)
    }
    return render(request, 'actors.html', context)

def actors(request):
    context = {
        "actors": Actor.objects.all()
    }
    return render(request, 'actors.html', context)

def homepage(request):
     context = {
        # TODO use first 10 top rated
        "movies": Movie.objects.all(),
        "actors": Actor.objects.all(),
        "directors": Director.objects.all(),
        "genres": Genre.objects.all(),
    }

  return render(request, 'homepage.html', context)      

