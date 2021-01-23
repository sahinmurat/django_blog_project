from django.core import serializers
from django.shortcuts import get_object_or_404, render
from django.http import JsonResponse, request
from django.core.serializers import serialize
import json
from django.views.decorators.csrf import csrf_exempt
from rest_framework.views import APIView
from .models import Category,Post, Like
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from .serializers import PostSerializer
from rest_framework import status
from rest_framework import generics
from django.contrib.auth.decorators import login_required
from rest_framework.permissions import IsAuthenticated
from rest_framework.pagination import PageNumberPagination


@api_view(['GET','POST'])
@permission_classes([IsAuthenticated])
def post_list(request):
    paginator = PageNumberPagination()
    paginator.page_size = 1
    if request.method == 'GET':
        posts = Post.objects.all()
        result_page = paginator.paginate_queryset(posts, request)
        serializer = PostSerializer(result_page, many = True)
        return paginator.get_paginated_response(serializer.data)
    elif request.method == 'POST':
        serializer = PostSerializer(data = request.data)
        if serializer.is_valid():
            serializer.save(author=request.user)
            data = {
                'message': 'it is created'
            }
            return Response(data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)
    
# class Create(generics.CreateAPIView):
#     serializer_class = PostSerializer
#     queryset = Post.objects.all()
    
@permission_classes([IsAuthenticated])
@api_view(["GET","PUT", "DELETE"])
def post_get_update_delete(request, slug):
    post = get_object_or_404(Post, slug=slug)
    if request.method == "GET":
        serializer = PostSerializer(post)
        return Response(serializer.data)
    if request.method == "PUT":
        serializer = PostSerializer(post, data=request.data)
        if serializer.is_valid():
            serializer.save()
            data = {
                "message": "Post updated succesfully!"
            }
            return Response(data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    if request.method == "DELETE":
        post.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
 
 
@api_view(["GET","PUT", "DELETE"])   
def like(request, slug):
    if request.method == "POST":
        obj = get_object_or_404(Post, slug=slug)
        like_qs = Like.objects.filter(user=request.user, post=obj)
        if like_qs:
            like_qs.delete()
        else:
            Like.objects.create(user=request.user, post=obj)
        return Response(status=status.HTTP_204_NO_CONTENT)
    return Response(status=status.HTTP_400_BAD_REQUEST)


    
