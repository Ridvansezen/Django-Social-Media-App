from django.shortcuts import render,redirect, get_object_or_404
from post.models import Post
from post.forms import PostForm
from django.contrib import messages

from rest_framework import viewsets
from .models import Post
from .serializers import ModelSerializer

def index(request):
    return render(request, "index.html")

def posts(request):
    posts = Post.objects.all()
    return render(request, "posts/posts.html", {"posts":posts})

def dashboard(request):
    if not request.user.is_authenticated:
        messages.info(request, "Bu sayfaya erişmek için giriş yapmalısınız.")
        return redirect("user:login")
    
    posts = Post.objects.filter(author = request.user)
    context = {
        "posts":posts,
    }

    return render(request, "posts/dashboard.html", context)

def addPost(request):
    if not request.user.is_authenticated:
        messages.info(request, "Gönderi ekleyebilmek için giriş yapmalısınız.")
        return redirect("user:login")
    
    form = PostForm(request.POST or None, request.FILES or None)
    
    if form.is_valid():
        post = form.save(commit=False)
        post.author = request.user
        post.save()
        messages.success(request, "Gönderi başarıyla oluşturuldu")
        return redirect("user:profileUser")


    return render(request, "posts/addPost.html", {"form":form})

def updatePost(request, id):
    if not request.user.is_authenticated:
        messages.info(request, "Gönderi düzenleyebilmek için giriş yapmalısınız.")
        return redirect("user:login")
    post = get_object_or_404(Post, id = id)
    form = PostForm(request.POST or None, instance=post)
    if form.is_valid():
        post = form.save(commit=False)
        post.author = request.user
        post.save()
        messages.success(request, "Gönderi başarıyla güncellendi")
        return redirect("user:profileUser")

    return render(request, "posts/updatePost.html", {"form":form})

def deletePost(request, id):
    if not request.user.is_authenticated:
        messages.info(request, "Gönderi silebilmek için giriş yapmalısınız.")
        return redirect("user:login")
    post = get_object_or_404(Post, id = id)
    post.delete()
    messages.success(request, "Gönderi başarıyla silindi")
    return redirect("user:profileUser")


# Rest Framework ------------------------------------


class ModelViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = ModelSerializer

