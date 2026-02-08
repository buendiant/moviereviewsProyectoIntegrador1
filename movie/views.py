from django.shortcuts import render
from django.http import HttpResponse
from .models import Movie

# Create your views here.

def home(request):
    # Render the home.html template
    return render(request, 'home.html', {'name': 'Juan Antonio'})
    #return render (request, 'home.html')
    #return render(request, 'home.html', {name: 'Juan Antonio'})
    searchTerm = request.GET.get('searchMovie') # Captura lo que escribes en el input
    if searchTerm:
        movies = Movie.objects.filter(title__icontains=searchTerm)
    else:
        movies = Movie.objects.all()   
    return render(request, 'home.html', {'searchTerm': searchTerm, 'movies': movies})

def about(request):
    return render(request, 'about.html')