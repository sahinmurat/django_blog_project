from rest_framework.permissions import BasePermission

class IsOwner(BasePermission):
    message = 'You are not the owner of this post'
    
    def has_object_permission(self, request, view, obj):
        return obj.author == request.user