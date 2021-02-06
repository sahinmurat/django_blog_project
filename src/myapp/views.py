from django.core import serializers
from django.shortcuts import get_object_or_404, render
from django.http import JsonResponse, request
from django.core.serializers import serialize
import json
from django.views.decorators.csrf import csrf_exempt
from rest_framework.views import APIView
from .models import Category, Comment,Post, Like, PostView
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from .serializers import PostSerializer, CommentSerializer
from rest_framework import status
from rest_framework import generics
from django.contrib.auth.decorators import login_required
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.pagination import PageNumberPagination
from .permissions import IsOwner

 
@api_view(['GET'])
@permission_classes([AllowAny])
def list(request):
    paginator = PageNumberPagination()
    paginator.page_size = 200
    if request.method == 'GET':
        posts = Post.objects.filter(status = 'Published')
        result_page = paginator.paginate_queryset(posts, request)
        serializer = PostSerializer(result_page, many = True, context = {'request': request})
        return paginator.get_paginated_response(serializer.data)
    
    
@api_view(['POST'])
@permission_classes([IsAuthenticated])
def create(request):
    paginator = PageNumberPagination()
    paginator.page_size = 200
    if request.method == 'POST':
        print(request.data)
        serializer = PostSerializer(data = request.data)
        if serializer.is_valid():
            serializer.save(author=request.user)
            data = {
                'message': 'it is created'
            }
            return Response(data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)
    
    

 
@permission_classes([IsAuthenticated])
@api_view(["GET","POST"])
def detail_comment(request, slug):
    post = get_object_or_404(Post, slug=slug)
    PostView.objects.create(author=request.user, post=post)
    if request.method == "POST":
        serializer = CommentSerializer(data = request.data)
        if serializer.is_valid():
            serializer.save(author=request.user, post=post)
            data = {
                'message': 'Your comment is added'
            }
            return Response(data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    if request.method == "GET":
        serializer = PostSerializer(post,  context = {'request': request})
        return Response(serializer.data)
    
 

@api_view(["PUT", "DELETE"])
@permission_classes([IsOwner, IsAuthenticated ])
def update_delete(request, slug):
    post = get_object_or_404(Post, slug=slug)
    
    if request.method == "PUT":
        if request.user != post.author:
            return Response(
                {'message': 'You are not the owner of this post!'},  status=status.HTTP_403_FORBIDDEN
            )
        serializer = PostSerializer(post, data=request.data)
        if serializer.is_valid():
            serializer.save()
            data = {
                "message": "Post updated succesfully!"
            }
            return Response(data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    if request.method == "DELETE":
        if request.user != post.author:
            return Response(
                {'message': 'You are not the owner of this post!'},  status=status.HTTP_403_FORBIDDEN
            )
        post.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
 
 
@api_view(["POST"])   
def like(request, slug):
    if request.method == "POST":
        obj = get_object_or_404(Post, slug=slug)
        like_qs = Like.objects.filter(author=request.user, post=obj)
        if like_qs:
            like_qs.delete()
            return Response( {'message': 'Your like  is deleted!'},status=status.HTTP_204_NO_CONTENT)
        else:
            Like.objects.create(author=request.user, post=obj)
            return Response( {'message': 'Your like is succesfully taken!'},status=status.HTTP_204_NO_CONTENT)
    return Response(status=status.HTTP_400_BAD_REQUEST)

# @permission_classes([IsAuthenticated])
# @api_view(["POST"])
# def add_comment(request, slug):
#     post = get_object_or_404(Post, slug=slug)
#     print(post)
#     print(post.content)
#     if request.method == "POST":
#         serializer = CommentSerializer(data = request.data)
#         if serializer.is_valid():
#             serializer.save(author =request.user, post= post)
#             data = {
#                 'message': 'Comment is added'
#             }
#             return Response(data, status=status.HTTP_201_CREATED)
#         return Response(status=status.HTTP_400_BAD_REQUEST)
        
    


# def model_delete_view(request, pk, *args, **kwargs):
#     obj = MyModel.objects.filter(pk=pk)
#     if not obj.exists():
#         return Response(
#             {'message': 'MyModel not found'},
#             status=status.HTTP_404_NOT_FOUND
#         )
#     obj = obj.filter(user=request.user)
#     if not obj.exists():
#         return Response(
#             {'message': 'You are not authorizated'},
#             status=status.HTTP_403_FORBIDDEN
#         )
#     obj.delete()
#     return Response({'message': 'MyModel deleted'}, status=status.HTTP_200_OK)



# @permission_classes([IsAuthenticated])
# @api_view(["GET","PUT", "DELETE","POST"])
# def post_get_update_delete(request, slug):
#     post = get_objjhect_or_404(Post, slug=slug)
    
#     if request.method == "POST":
#         serializer = CommentSerializer(post.comment)
#         if serializer.is_valid():
#             serializer.save(author=request.user)
#             data = {
#                 'message': 'Comment is added'
#             }
#             return Response(data, status=status.HTTP_201_CREATED)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
#     if request.method == "GET":
#         serializer = PostSerializer(post)
#         return Response(serializer.data)
#     if request.method == "PUT":
#         serializer = PostSerializer(post, data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             data = {
#                 "message": "Post updated succesfully!"
#             }
#             return Response(data)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
#     if request.method == "DELETE":
#         post.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)