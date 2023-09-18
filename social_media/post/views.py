from django.shortcuts import render
from post.models import Post

def index(request):
    return render(request, "index.html")

def posts(request):
    posts = Post.objects.all()


    return render(request, "posts/posts.html", {"posts":posts})
