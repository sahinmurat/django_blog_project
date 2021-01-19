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
    
    class Meta:
        model = Post
        fields = (  'id', 'title','content', 'category','publish_date', 'last_updated', 'author', 'slug')