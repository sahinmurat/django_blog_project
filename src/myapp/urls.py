from django.urls import path
from .views import  post_list,post_get_post, post_put_delete, like

app_name = "blog"

urlpatterns = [
    path("", post_list , name=""),
    # path("<str:slug>", post_get_update_delete , name="detail"),
    path("<str:slug>/get", post_get_post , name="get-comment"),
    path("<str:slug>/upd", post_put_delete , name="del-upd"),
    path("<str:slug>/like",like , name="like"),
 
]

 