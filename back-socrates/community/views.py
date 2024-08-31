from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status
from django.shortcuts import get_object_or_404, get_list_or_404
from .serializers import PostListSerializer, CategorySerializer, PostSerializer, CommentSerializer
from .models import Post, Category, Comment

# permission Decorators
from rest_framework.decorators import permission_classes
from rest_framework.permissions import IsAuthenticated


@api_view(['GET', 'POST'])
# @permission_classes([IsAuthenticated])
def category_list_create(request):
    if request.method == 'GET':
        categories = get_list_or_404(Category)
        serializer = CategorySerializer(categories, many=True)
        return Response(serializer.data)
    
    elif request.method == 'POST':
        serializer = CategorySerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data)


@api_view(['GET', 'POST'])
@permission_classes([IsAuthenticated])
def post_list_create(request):
    if request.method == 'GET':
        posts = get_list_or_404(Post)
        serializers = PostListSerializer(posts, many=True)
        return Response(serializers.data)
 
    elif request.method == 'POST':
        category = get_object_or_404(Category, pk=request.data.get('category'))
        
        serializer = PostSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save(category=category, user=request.user)
            return Response(serializer.data)


@api_view(['GET', 'DELETE', 'PUT'])
@permission_classes([IsAuthenticated])
def post_detail(request, post_pk):
    post = get_object_or_404(Post, pk=post_pk)
    
    # post detail 확인
    if request.method == 'GET':
        serializer = PostSerializer(post)
        return Response(serializer.data)

    # post detail 삭제
    elif request.method == 'DELETE':
        post.delete()
        # 삭제 후 204 status code 반환
        return Response(status=status.HTTP_204_NO_CONTENT)
    elif request.method == 'PUT':
        serializer = PostSerializer(post, data=request.data, partial=True)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data)
    
    
@permission_classes([IsAuthenticated])
def post_update(request, post_pk):
    post = get_object_or_404(Post, pk=post_pk)
    # post detail 수정
    if request.method == 'PUT':
        serializer = PostSerializer(post, data=request.data, partial=True)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data)



@api_view(['POST'])
@permission_classes([IsAuthenticated])
def comment_create(request, post_pk):
    post = get_object_or_404(Post, pk=post_pk)
    serializer = CommentSerializer(data=request.data)
    if serializer.is_valid(raise_exception=True):
        serializer.save(post=post, user=request.user)
        return Response(serializer.data)


# comment detail에 접근
@api_view(['GET', 'DELETE'])
@permission_classes([IsAuthenticated])
def comment_detail(request, comment_pk):
    comment = get_object_or_404(Comment, pk=comment_pk)

    # comment 조회
    if request.method == 'GET':
        serializer = CommentSerializer(comment)
        return Response(serializer.data)
    
    # comment 삭제
    elif request.method == 'DELETE':
        comment.delete()
        # 삭제 후 204 status code 반환
        return Response(status=status.HTTP_204_NO_CONTENT)