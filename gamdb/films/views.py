from django.shortcuts import render
from django.http import HttpResponse
from .models import Movies, Director

def directors(request):
    context = {
        'logic': True,
        'title': "Nejoblíbenější režiséři",
        'directors': Director.objects.all()
    }
    print(context)
    return render(request, 'directors.html', context)

def homepage(request):
    #return HttpResponse("HELLOOO")
    context ={
        'movies':Movies.objects.all(),
    }
    return render(request,'main.html',context)

