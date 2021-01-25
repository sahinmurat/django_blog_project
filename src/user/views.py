from django.shortcuts import render
from rest_framework import generics
from django.contrib.auth.models import User
from .serializers import RegistrationSerializer, ProfileSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
# Create your views here.

class RegisterView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = RegistrationSerializer

@api_view(["GET", "PUT"])
def Profile_get_update(request):
    # profile = get_object_or_404(Profile, user__id=id)
    if request.method == "GET":
        serializer = ProfileSerializer(request.user.profile)
        return Response(serializer.data)

    if request.method == "PUT":
        serializer = ProfileSerializer(request.user.profile, data=request.data)
        if serializer.is_valid():
            serializer.save()
            data = {
                "message": "Profile updated succesfully!"
            }
            return Response(data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
