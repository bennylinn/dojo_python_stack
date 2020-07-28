from django.shortcuts import render, redirect
from .models import Movie

# Create your views here.
def index(request):
    context = {
        "all_the_movies": Movie.objects.all()
    }
    return render(request, 'index.html', context)

def add(request):
    name = request.POST['name']
    duration = request.POST['duration']
    rating = request.POST['rating']
    
    Movie.objects.create(title=name, duration=int(duration), rating=int(rating))

    return redirect('/')