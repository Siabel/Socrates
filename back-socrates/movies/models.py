from django.core.files.base import ContentFile
from django.db import models
from django.conf import settings
import requests

class Genre(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=50)

class Movie(models.Model):
    movie_id = models.IntegerField(primary_key=True)
    title = models.CharField(max_length=50)
    genres = models.ManyToManyField(Genre)
    overview = models.TextField()
    poster_path = models.ImageField(upload_to='movie_posters/', null=True, blank=True)
    vote_avg = models.FloatField()
    popularity = models.FloatField(null=True)
    released_date = models.DateField()

# class Review(models.Model):
#     user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
#     movie = models.ForeignKey(Movie, on_delete=models.CASCADE, related_name='reviews')

#     content = models.TextField()
#     review_date = models.DateTimeField(auto_now_add=True)
#     rating = models.FloatField()


class Like(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE, related_name='likes')


class Recommendation(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    genre = models.ForeignKey(Genre, on_delete=models.CASCADE)