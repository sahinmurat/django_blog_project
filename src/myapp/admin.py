from django.contrib import admin
from .models import Category,PostView,Post, Comment,Like

admin.site.register(Category)
admin.site.register(Post)
admin.site.register(Comment)
admin.site.register(Like)
admin.site.register(PostView)

# Register your models here.
