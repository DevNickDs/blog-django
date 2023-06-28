from django.shortcuts import render

# Create your views here.

def home(request):
    return render(request, 'index.html')

def general(request):
    return render(request, 'general.html')

def anime_manga(request):
    return render(request, 'anime_manga.html')

def technology(request):
    return render(request, 'technology.html')

def video_games(request):
    return render(request, 'video_games.html')