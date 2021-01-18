from django.urls import path
from .views import Create

app_name = "blog"

urlpatterns = [
    path("",Create.as_view(), name="list"),
   
]