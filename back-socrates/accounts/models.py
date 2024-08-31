from django.contrib.auth.models import AbstractUser
from django.db import models
from django.conf import settings
from movies.models import *

# urls에 static url 추가해줘야함~(추가할 때 공식문서 보고 추가해주기) 
# def user_profile_image_path(instance, filename):
#         return f'profile_image_{instance.pk}/{filename}'

class User(AbstractUser):
    nickname = models.CharField(max_length=20, blank=True, null=True)
    birth_date = models.DateField(null=True, blank=True)
    email = models.EmailField(max_length=254, blank=True, null=True)

    #  팔로워(from_user_id가 팔로우 당한사람 : user_pk)(followings가 팔로우를 한 사람) 목록
    # to_user_id가 팔로우를 신청하면 from_user_id가 팔로우를 당함
    
    # 즉, to_user_id가 팔로우 신청을 하면
    # to_user_id의 followers(=팔로잉 목록) 목록에 from_user_id가 추가 됨
    
    # from_user_id의 followings(=팔로워 목록)에 to_user_id가 추가 됨

    # followings = models.ManyToManyField('self', symmetrical=False, related_name='followers', blank=True)
    
    # 프로필 사진 저장소 설정
    # profile_path = models.ImageField(upload_to='profile_images/', null=True, blank=True)
    hate_genres = models.ManyToManyField(Genre, related_name='hate_genre')
    fullname = models.CharField(max_length=255, blank=True)
