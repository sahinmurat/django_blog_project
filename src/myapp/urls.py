from django.urls import path
from .views import  post_list, post_get_update_delete, like

app_name = "blog"

urlpatterns = [
    path("", post_list , name="list"),
    path("<str:slug>", post_get_update_delete , name="detail"),
    path("<str:slug>/like",like , name="like"),
    # path("create/",Create.as_view(), name="create"),
]