from django.urls import path
from . import views

app_name = 'community'
urlpatterns = [
    path('category/', views.category_list_create),
    path('posts/', views.post_list_create),
    path('posts/<int:post_pk>/', views.post_detail),
    path('posts/<int:post_pk>/update/', views.post_update),
    path('posts/<int:post_pk>/comments/', views.comment_create),
    path('posts/comments/<int:comment_pk>/', views.comment_detail),
]
