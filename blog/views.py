from django.shortcuts import render
from .models import Post, Category

# Create your views here.

def home(request):
    posts = Post.objects.filter(state=True)
    #print(post)
    return render(request, 'index.html', {'posts': posts})

def general(request):
    posts = Post.objects.filter(
        state = True,
        category = Category.objects.get(name='General')
    )
    return render(request, 'general.html', {'posts': posts})

def anime_manga(request):
    posts = Post.objects.filter(
        state = True,
        category = Category.objects.get(name='Anime y Manga')
    )
    return render(request, 'anime_manga.html', {'posts': posts})

def technology(request):
    posts = Post.objects.filter(
        state = True,
        category = Category.objects.get(name='Technology')
    )
    return render(request, 'technology.html', {'posts': posts})

def video_games(request):
    posts = Post.objects.filter(
        state = True,
        category = Category.objects.get(name='Gaming')
    )
    return render(request, 'video_games.html', {'posts': posts})