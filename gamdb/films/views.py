from django.shortcuts import render
from django.http import HttpResponse
from .models import Movies

def homepage(request):
    #return HttpResponse("HELLOOO")
    context ={
        'movies':Movies.objects.all(),
    }
    return render(request,'main.html',context)

