# from django.contrib.auth import get_user_model
from rest_framework import serializers
from allauth.account import app_settings as allauth_settings
from allauth.utils import get_username_max_length
from allauth.account.adapter import get_adapter
from dj_rest_auth.serializers import UserDetailsSerializer
from .models import User
from movies.models import *
from movies.serializers import *
from dj_rest_auth.registration.serializers import RegisterSerializer

class SignUpSerializer(RegisterSerializer):
    nickname = serializers.CharField(required=False,allow_blank=True, max_length=255)
    birth_date = serializers.DateField(allow_null=True, required=False)
    profile_path = serializers.ImageField(required=False, allow_null=True, allow_empty_file=True)
    hate_genres = serializers.ListField(child=serializers.IntegerField(), required=False, default=[])
    fullname = serializers.CharField(required=False, allow_blank=True, max_length=255)

    def get_cleaned_data(self):
        cleaned_data = super().get_cleaned_data()
        cleaned_data['nickname'] = self.validated_data.get('nickname', '')
        cleaned_data['fullname'] = self.validated_data.get('fullname', '')
        cleaned_data['birth_date'] = self.validated_data.get('birth_date', None)
        # cleaned_data['profile_path'] = self.validated_data.get('profile_path', '')
        cleaned_data['hate_genres'] = self.validated_data.get('hate_genres', [])
        return cleaned_data


    def save(self, request):
        adapter = get_adapter()
        user = adapter.new_user(request)
        self.cleaned_data = self.get_cleaned_data()
        adapter.save_user(request, user, self)
        self.custom_signup(request, user)

        user.nickname = self.cleaned_data.get('nickname', '')
        user.fullname = self.cleaned_data.get('fullname', '')
        user.birth_date = self.cleaned_data.get('birth_date', None)
        # user.profile_path = self.cleaned_data.get('profile_path', '')

        hate_genres_ids = self.cleaned_data.get('hate_genres', [])
        user.hate_genres.set(hate_genres_ids)

        user.save()

        return user

class ProfileSerializer(serializers.ModelSerializer):
    class GenreSerializer(serializers.ModelSerializer):
        class Meta:
            model = Genre
            fields = ('id', 'name',)

    hate_genres = GenreSerializer(many=True)

    class Meta:
        model = User
        fields = ('id', 'username', 'birth_date', 'fullname', 'email', 'hate_genres',)


# 싫어하는 장르
class HateGenreSerializer(serializers.ModelSerializer):

    class GenreSerializer(serializers.ModelSerializer):
        class Meta:
            model = Genre
            fields = ('id', 'name',)

    hate_genres = GenreSerializer(many=True, read_only=True)

    class Meta:
        model = User
        fields = '__all__'

    # profile_path 필드를 직렬화할 때 URL로 변환해주는 코드 추가
    # def to_representation(self, instance):
    #     representation = super().to_representation(instance)
    #     representation['profile_path'] = instance.profile_path.url if instance.profile_path else None
    #     return representation
