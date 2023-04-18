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
    context = {
        "movies": Movies.objects.all()
    }
    return render(request, 'movies.html', context)

def movie(request,id):
    context = {
        "movies": Movies.objects.all()
    }
    return render(request, 'movies.html', context)

def homepage(request):
    #return HttpResponse("HELLOOO")
    context ={
        'movies':Movies.objects.all(),
    }
    return render(request,'main.html',context)

