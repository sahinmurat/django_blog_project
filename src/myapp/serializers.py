from django.db.models import fields
from rest_framework import serializers
from myapp.models import Category, Post

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ('id', 'name')
        
class PostSerializer(serializers.ModelSerializer):
    # url = serializers.HyperlinkedIdentityField(
    #     view_name = 'detail', #viewda belirttigimiz adres
    #     lookup_field = 'id'
    # )
    author = serializers.CharField( source="author.username", read_only=True)
    class Meta:
        model = Post
        fields = (  'id', 'title','content', 'category','publish_date', 'last_updated', 'author', 'slug')
        read_only_fields = ['author', "publish_date", "last_updated","slug"]
        
        
    #     class BlogPostSerializer(serializers.ModelSerializer):
    # url = serializers.HyperlinkedIdentityField(
    #     view_name ='detail',
    #     lookup_field = 'slug',
    # )
    # author = serializers.CharField( source="author.username", read_only=True)
    # class Meta:
    #     model = BlogPost
    #     fields = ("url",  "title", "content", "image", "status", 'author', 'comment_count', 'view_count', 'like_count')
    #     read_only_fields = ['author', "create_date", "update_date","slug"]
        
        
    #         {
    #     "title": "upppqaa",
    #     "content": "qaa",
    #     "category": 1,
    #     "author": "murat"
    # }