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
    category = serializers.SerializerMethodField()
    status = serializers.SerializerMethodField()
    owner = serializers.SerializerMethodField(read_only = True)
    class Meta:
        model = Post
        fields = (  'id', 'owner', 'title', 'comments', 'image','category','status','publish_date', 'last_updated', 'author', 'slug','comment_count', 'view_count', 'like_count')
        read_only_fields = ['author', "publish_date", "last_updated","slug"]
        
    def get_category(self, obj):
        return obj.get_category_display()
    
    def get_status(self, obj):
        return obj.get_status_display()
    
    def get_owner(self, obj):
        request = self.context['request']
        if request.user.is_authenticated:
            if obj.author == request.user:
                return True
            return False
        
