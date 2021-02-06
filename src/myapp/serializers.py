from django.db.models import fields
from rest_framework import serializers
from myapp.models import Category, Comment, Post
from django.db.models import Q

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
    category_name = serializers.SerializerMethodField()
    status_name = serializers.SerializerMethodField()
    owner = serializers.SerializerMethodField(read_only = True)
    has_liked = serializers.SerializerMethodField()
    class Meta:
        model = Post
        fields = (  'id', 'owner', 'title', 'content','comments', 'has_liked', 'image','category','category_name','status','status_name','publish_date', 'last_updated', 'author', 'slug','comment_count', 'view_count', 'like_count')
        read_only_fields = ['author', "publish_date", "last_updated","slug"]
        
    def get_category_name(self, obj):
        return obj.get_category_display()
    
    def get_status_name(self, obj):
        return obj.get_status_display()
    
    def get_owner(self, obj):
        request = self.context['request']
        if request.user.is_authenticated:
            if obj.author == request.user:
                return True
            return False
    def get_has_liked(self, obj):
        request = self.context['request']
        if request.user.is_authenticated:
            if Post.objects.filter(Q(like__author=request.user) & Q(like__post=obj)).exists():
                return True
            return False
        
