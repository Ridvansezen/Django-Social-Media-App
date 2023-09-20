from django.urls import path, include
from post import views

app_name = "post"

urlpatterns = [
    path('', views.posts, name="posts"),
    path('addpost/', views.addPost, name="addPost"),
    path('update/<int:id>', views.updatePost, name="updatePost"),
    path('delete/<int:id>', views.deletePost, name="deletePost"),

]