from rest_framework import serializers
from community.models import *
from movies.models import *
from django.conf import settings

User = settings.AUTH_USER_MODEL

# 전체/단일/장르별 영화 조회
class MovieListSerializer(serializers.ModelSerializer):   

    class GenreSerializer(serializers.ModelSerializer):
 
        class Meta:
            model = Genre
            # 단일 컬럼 출력 시 ,(콤마) 필수(없으면 인식 못함) 
            fields = '__all__'
    
    genre_check = GenreSerializer(many=True)

    class Meta:
        model = Movie
        fields = '__all__'


# 전체 장르 조회
class GenreSerializer(serializers.ModelSerializer):
        class Meta:
            model = Genre
            fields = ('id', 'name',)


# 싫어하는 장르
class HateGenreSerializer(serializers.ModelSerializer):

    class GenreSerializer(serializers.ModelSerializer):
        class Meta:
            model = Genre
            fields = ('id', 'name',)

    hate_genres = GenreSerializer(many=True, read_only=True)

    class Meta:
        model = User
        # 사용자 id, 이름, 싫어하는 장르
        fields = ('id', 'username', 'hate_genres',)
