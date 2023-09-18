from django.urls import path, include
from post import views

app_name = "post"

urlpatterns = [
    path('', views.posts, name="posts")

]