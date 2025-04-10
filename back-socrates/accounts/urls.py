from django.urls import path
from . import views

app_name = 'accounts'
# 회원가입(POST) : account/signup/
# 프로필 정보 조회 및 수정(GET/PUT) : account/user
# 비밀번호 번형(POST) : account/password/change/
# 비밀번호 찾기(POST) : account/password/reset/

urlpatterns = [
    path('delete/', views.user_delete, name='delete'), # 회원탈퇴
    path('profile/', views.my_profile, name='my_profile'),
    path('profile/update/', views.update_profile, name='update_profile'),
    path('<int:user_pk>/hate_genres/', views.hate_genres_list), # 싫어하는 장르 조회
    # path('<int:user_pk>/hate_genres/<int:genre_pk>/', views.hate_genres_detail), # 싫어하는 장르 등록 및 해제
    # path('<int:user_pk>/recommand/', views.recommand), # 사용자가 좋아요를 한 영화리스트에서 해당 영화와 유사한 영화를 출력
]
