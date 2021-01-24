from django.db.models import fields
from rest_framework import serializers
from myapp.models import Category, Comment, Post

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ('id', 'name')
        
class CommentSerializer(serializers.ModelSerializer):
    author = serializers.CharField( source="author.username", read_only=True)# user = serializers.CharField( source="author.username", read_only=True)   
    class Meta:
        model= Comment
        fields = ('content','author')
     
class PostSerializer(serializers.ModelSerializer):
    comments = CommentSerializer(many= True, read_only = True)
    author = serializers.CharField( source="author.username", read_only=True)
    category = serializers.SerializerMethodField
    class Meta:
        model = Post
        fields = (  'id', 'title', 'comments', 'image','category','publish_date', 'last_updated', 'author', 'slug','comment_count', 'view_count', 'like_count')
        read_only_fields = ['author', "publish_date", "last_updated","slug"]
        
