import json
import requests
from datetime import datetime
from django.http import JsonResponse
from rest_framework.response import Response
from .models import *
from .serializers import *
from rest_framework.decorators import api_view, permission_classes

TMDB_API_KEY = '7129c2707bdcc88780b426387d0a1c89'

# 모든 장르들 받아오기
@api_view(['GET'])
def genres(request):
    genres = Genre.objects.all()

    serializer = GenreSerializer(genres, many=True)
    return Response(serializer.data)


def sync_tmdb(request):
    TMDB_API_KEY = '7129c2707bdcc88780b426387d0a1c89'

    genre_url = f"https://api.themoviedb.org/3/genre/movie/list?api_key={TMDB_API_KEY}&language=ko-KR"
    genres = requests.get(genre_url).json()
    genre_mapping = {genre['id']: genre['name'] for genre in genres.get('genres', [])}

    total_data = []

    for i in range(1, 26):
        url = f"https://api.themoviedb.org/3/movie/popular?api_key={TMDB_API_KEY}&language=ko-KR&page={i}&sort_by=popularity.desc"
        movies = requests.get(url).json()

        if 'results' in movies:
            for movie in movies['results']:
                if movie.get('release_date', ''):
                    data = {
                        'title': movie['title'],
                        'genre': ', '.join([genre_mapping.get(genre_id, '') for genre_id in movie.get('genre_ids', [])]),
                        'overview': movie['overview'],
                        'poster_path': movie['poster_path'],
                        'rating': movie['vote_average'],
                        'duration': None,
                        'released_date': datetime.strptime(movie['release_date'], "%Y-%m-%d").date(),
                    }

                    total_data.append(data)
        else:
            print(movies)

    for data in total_data:
        movie_instance, created = Movie.objects.get_or_create(
            title=data['title'],
            defaults={
                'genre': data['genre'],
                'overview': data['overview'],
                'poster_path': data['poster_path'],
                'rating': data['rating'],
                'duration': data['duration'],
                'released_date': data['released_date'],
            }
        )

    response_data = {
        'success': True,
        'message': 'Data synchronized successfully.'
    }
    return JsonResponse(response_data)


# movie data json파일로 저장
def get_movie_datas():
    total_data = []

    for i in range(1, 26):
        url = f"https://api.themoviedb.org/3/movie/popular?api_key={TMDB_API_KEY}&language=ko-KR&page={i}&sort_by=popularity.desc"
        movies = requests.get(url).json()

        for movie in movies['results']:
            if movie.get('release_date', ''):
                fields = {
                    'movie_id': movie['id'],
                    'title': movie['title'],
                    'released_date': movie['release_date'],
                    'popularity': movie['popularity'],
                    'vote_avg': movie['vote_average'],
                    'overview': movie['overview'],
                    'poster_path': movie['poster_path'],
                    'genres': movie['genre_ids']
                }

                data = {
                    "pk": movie['id'],
                    "model": "movies.movie",
                    "fields": fields
                }

                total_data.append(data)

    with open("movies/fixtures/movies.json", "w", encoding="utf-8") as w:
        json.dump(total_data, w, indent=4, ensure_ascii=False)

get_movie_datas()