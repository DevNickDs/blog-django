from django.shortcuts import render
from .models import Post, Category
from django.shortcuts import get_object_or_404
from django.db.models import Q

# Create your views here.

def home(request):
    posts = search_posts(request, None)
    #print(post)
    return render(request, 'index.html', {'posts': posts})

def general(request):
    posts = search_posts(request, 'General')
    return render(request, 'general.html', {'posts': posts})

def anime_manga(request):
    posts = search_posts(request, 'Anime y Manga')
    return render(request, 'anime_manga.html', {'posts': posts})

def technology(request):
    posts = search_posts(request, 'Technology')
    return render(request, 'technology.html', {'posts': posts})

def video_games(request):
    posts = search_posts(request, 'Gaming')
    return render(request, 'video_games.html', {'posts': posts})

def search_posts(request, category_name):
    queryset = request.GET.get('search')
    posts = Post.objects.filter(state=True)
    if queryset:
        posts = posts.filter(
            Q(title__icontains=queryset) |
            Q(description__icontains=queryset)
        ).distinct()

    if category_name:
        category = Category.objects.get(name=category_name)
        posts = posts.filter(category=category)

    return posts

def details_post(request, slug):
    post = get_object_or_404(Post, slug = slug)
    #print(post)
    return render(request, 'post.html', {'post': post})
