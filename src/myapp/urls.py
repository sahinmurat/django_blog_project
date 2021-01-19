from django.urls import path
from .views import Create, post_list, student_get_update_delete

app_name = "blog"

urlpatterns = [
    path("", post_list , name="list"),
    path("<int:id>", student_get_update_delete , name="detail"),
    path("create/",Create.as_view(), name="create"),
]