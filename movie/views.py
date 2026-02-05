from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def home(request):
    # Render the home.html template
    return render(request, 'home.html', {'name': 'User'})

def about(request):
    return HttpResponse("This is the About Page of Movie Reviews.")