from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

app_name = 'movies'

urlpatterns = [
    path('sync-tmdb/', views.sync_tmdb, name='sync_tmdb'),
    path('genres/', views.genres, name='genres'),
]