import json
import random
from django.contrib.auth import get_user_model
from django.shortcuts import get_object_or_404
from django.contrib.auth.decorators import login_required
from django.views.decorators.http import require_http_methods, require_POST
from django.http import JsonResponse
from rest_framework.permissions import *
from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from .models import User
from movies.models import Genre
from .serializers import *
# from movies.serializers import *

User = get_user_model()
        
# 회원탈퇴
@api_view(['POST'])
@permission_classes([IsAuthenticated]) # 인증된 사용자만 권한 허용
def user_delete(request):
    request.user.delete()
    data = {
            'content': f'{request.user}님의 탈퇴처리가 완료되었습니다.',
        }
    return Response(data, status=status.HTTP_204_NO_CONTENT)

# 회원가입
# 인증 필요 없이 접근 가능한 영역 : 추후 인증 필요
@api_view(['POST'])
def signup(request):
    serializer = SignUpSerializer(data=request.data)
    if serializer.is_valid():
        user = serializer.save()

        # 프로필 이미지를 업로드하고 URL 반환
        profile_image_url = ''
        if 'profile_image' in request.FILES:
            profile_image = request.FILES['profile_image']
            user.profile_image.save(profile_image.name, profile_image)
            profile_image_url = request.build_absolute_uri(user.profile_image.url)

        return Response({'profile_image_url': profile_image_url}, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# 프로필 정보 조회
@api_view(['GET'])
@permission_classes([IsAuthenticated])
def my_profile(request):
    user = request.user  # 현재 요청을 보낸 사용자의 정보를 가져옴
    # user = get_user_model(User)
    # print('########################')
    # print(user)
    serializer = ProfileSerializer(user, many=False)
    return Response(serializer.data)


# 프로필 수정
@api_view(['POST', 'PUT'])
def update_profile(request, username):
    user_profile = get_object_or_404(get_user_model(), username=username)
    me = request.user

    if request.method == 'PUT':
        profile = user_profile.profile
        if me == user_profile:
            serializer = ProfileSerializer(instance=profile, data=request.data)
            if serializer.is_valid(raise_exception=True):
                serializer.save()
                return Response(serializer.data)

    if request.method == 'POST':
        if me == user_profile:
            my_profile = me.profile
            serializer = ProfileSerializer(instance=my_profile, data=request.data)
            if serializer.is_valid(raise_exception=True):
                serializer.save(user=request.user)
                return Response(serializer.data, status=status.HTTP_201_CREATED)


# 싫어하는 장르 조회
@api_view(['GET'])
@permission_classes([IsAuthenticated]) # 인증된 사용자만 권한 허용
def hate_genres_list(request, user_pk):
    user = get_object_or_404(User, pk=user_pk)
    print('###################')
    print(user)
    hate_genres = HateGenreSerializer(user.hate_genres.all(), many=True)

    user_hate_list = {
        'id': user.id,
        'username': user.username,
        'hate_genres': hate_genres,
    }
    return Response(data=user_hate_list)


# 싫어하는 장르 등록 및 해제
@api_view(['PUT'])
@permission_classes([IsAuthenticated])
def hate_genres_detail(request, user_pk, genre_pk):
    user = get_object_or_404(User, pk=user_pk)
    genre = get_object_or_404(Genre, pk=genre_pk)

    if user.hate_genres.filter(pk=genre_pk).exists():
        user.hate_genres.remove(genre)
    else:
        user.hate_genres.add(genre)

    hate_genres = HateGenreSerializer(user.hate_genres.all(), many=True).data

    user_hate_response = {
        'id': user.id,
        'username': user.username,
        'hate_genres': hate_genres,
    }

    return Response(user_hate_response)



# # 사용자가 선택한 영화와 비슷한 장르의 영화를 출력
#     # 사용하려는 알고리즘
#     # 1. 우선적으로 사용자가 싫어하는 장르가 포함된 장르를 모두 제외시킴
#     # 2. vue에서 영화 리스트를 랜덤하게 띄우고, 사용자가 해당 영화를 선택
#     # 3. 선택된 영화의 장르를 저장하고 저장된 장르가 포함되어 있는 영화만이 표시되도록 변경
# @api_view(['GET'])
# @permission_classes([IsAuthenticated])
# def recommand(request, user_pk):
    
#     movies_json = open('./movies/fixtures/movies.json', encoding='utf-8')
#     movies_list = json.load(movies_json)
    
#     genre_json = open('./movies/fixtures/genres.json', encoding='utf-8')
#     genre_list = json.load(genre_json)


#     # 사용자가 싫어하는 장르 id 고르기
#     user = get_object_or_404(User, pk=user_pk)
#     serializer = HateGenreSerializer(user)
#     hate_genres = [genre['id'] for genre in serializer.data.get('hate_genres')]

#     # 싫어하는 장르가 없는 경우 모든 장르를 포함시키고,
#     # 있는 경우 해당하는 장르를 포함하지 않도록 필터링
#     filtered_movies = []
#     for movie in movies_list:
#         if movie['model'] == 'movies.movie':
#             data = movie['fields']
#             data['genre_check'] = [
#                 genre_list[k]['name'] for j in data['genre_check']
#                 if j not in hate_genres
#                 for k in range(len(genre_list)) if j == genre_list[k]['id']
#                 ]
#             filtered_movies.append(data)

#     return JsonResponse({'filtered_movies': filtered_movies})

# # @login_required
# # @require_http_methods(['GET', 'POST'])
# # def change_password(request):
# #     if request.method == 'POST':
# #         form = PasswordChangeForm(request.user, request.POST)
# #         if form.is_valid():
# #             form.save()
# #             update_session_auth_hash(request, form.user)
# #             return redirect('movies:index')
# #     else:
# #         form = PasswordChangeForm(request.user)
# #     context = {
# #         'form': form,
# #     }
# #     return render(request, 'accounts/change_password.html', context)


# # def profile(request, username):
# #     person = get_object_or_404(get_user_model(), username=username)
# #     context = {
# #         'person': person,
# #     }
# #     return render(request, 'accounts/profile.html', context)


# # @login_required
# # @require_http_methods(['GET', 'POST'])
# # def update(request):
# #     if request.method == 'POST':
# #         form = CustomUserChangeForm(request.POST, instance=request.user)
# #         if form.is_valid():
# #             form.save()
# #             return redirect('movies:index')
# #     else:
# #         form = CustomUserChangeForm(instance=request.user)
# #     context = {
# #         'form': form,
# #     }
# #     return render(request, 'accounts/update.html', context)
#     # return redirect('accounts:profile', you.username)