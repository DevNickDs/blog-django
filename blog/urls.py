from django.urls import path
from . import views

app_name = 'blog'

urlpatterns = [
    path('', views.home, name='home'),
    path('general/', views.general, name='general'),
    path('anime_manga/', views.anime_manga, name='anime_manga'),
    path('technology/', views.technology, name='technology'),
    path('video_games/', views.video_games, name='video_games'),
    path('<slug:slug>', views.details_post, name='details_post'),
]
