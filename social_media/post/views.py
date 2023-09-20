from django.shortcuts import render,redirect, get_object_or_404
from post.models import Post
from post.forms import PostForm
from django.contrib import messages

def index(request):
    return render(request, "index.html")

def posts(request):
    posts = Post.objects.all()
    return render(request, "posts/posts.html", {"posts":posts})

def addPost(request):
    form = PostForm(request.POST or None)
    if form.is_valid():
        post = form.save(commit=False)
        post.author = request.user
        post.save()
        messages.success(request, "Gönderi başarıyla oluşturuldu")
        return redirect("user:profileUser")

    return render(request, "posts/addPost.html", {"form":form})

def updatePost(request, id):
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
    post = get_object_or_404(Post, id = id)
    post.delete()
    messages.success(request, "Gönderi başarıyla silindi")
    return redirect("user:profileUser")
