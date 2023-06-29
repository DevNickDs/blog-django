from django.shortcuts import render
from .models import Post, Category
from django.shortcuts import get_object_or_404
from django.db.models import Q
from django.core.paginator import Paginator

# Create your views here.

def home(request):
    posts = search_posts(request, None)
    posts = pages(request, posts)
    return render(request, 'index.html', {'posts': posts})

def general(request):
    posts = search_posts(request, 'General')
    pages = (posts)
    return render(request, 'general.html', {'posts': posts})

def anime_manga(request):
    posts = search_posts(request, 'Anime y Manga')
    pages = (posts)
    return render(request, 'anime_manga.html', {'posts': posts})

def technology(request):
    posts = search_posts(request, 'Technology')
    pages = (posts)
    return render(request, 'technology.html', {'posts': posts})

def video_games(request):
    posts = search_posts(request, 'Gaming')
    pages = (posts)
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

def pages(request, posts):
    paginator = Paginator(posts, 2)
    page_number = request.GET.get("page")
    posts = paginator.get_page(page_number)
    return posts

def details_post(request, slug):
    post = get_object_or_404(Post, slug = slug)
    #print(post)
    return render(request, 'post.html', {'post': post})
