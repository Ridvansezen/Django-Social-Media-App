from django.shortcuts import render,redirect, get_object_or_404
from user.forms import RegisterForm,LoginForm
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import login,logout,authenticate
from django.db import IntegrityError
from post.models import Post
from user.forms import ChangeUsernameForm
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib.auth import update_session_auth_hash
from django.contrib.auth.decorators import login_required
from .models import UserProfile
from django.http import HttpResponse

from rest_framework import viewsets
from .models import User
from .serializers import UserModelSerializer


def loginUser (request):
    form = LoginForm(request.POST or None)
    context = {
        "form":form
    }
    if form.is_valid():
        username = form.cleaned_data.get("username")
        password = form.cleaned_data.get("password")

        user = authenticate(username = username, password = password)

        if user is None:
            messages.info(request, "Kullanıcı adı veya parola hatalı")
            return render(request, "user/login.html", context)
        
        messages.success(request, "Başarıyla giriş yaptınız")
        login(request, user)

        return redirect("index")
    return render(request, "user/login.html", context)

    return render(request, "user/login.html")

def register (request):
    form = RegisterForm(request.POST or None)
    if form.is_valid():
        username = form.cleaned_data.get("username")
        password = form.cleaned_data.get("password")

        try:
            newUser = User(username = username)
            newUser.set_password(password)
            newUser.save()
            login(request, newUser)
            messages.success(request, "Başarıyla kayıt oldunuz")
            return redirect("index")
        
        except IntegrityError:
            messages.info(request, "Bu kullanıcı adı alınmış")

    context = {
        "form": form
    }
   
   
    return render(request, "user/register.html",context)

def logoutUser (request):
    logout(request)
    messages.success(request, "Başarıyla çıkış yaptınız")
    return redirect("index")


def profileUser(request):
    if not request.user.is_authenticated:
        messages.info(request, "Profilinizi görüntüleyebilmek için giriş yapmalısınız.")
        return redirect("user:login")
    user = request.user
    registiration_date = user.date_joined
    posts = Post.objects.filter(author = request.user)

    context = {
        'user':user,
        'registiration_date' :registiration_date,
        'posts':posts
    }

    return render(request, "user/Userprofile.html", context)

def profileAuthor(request, author_id):
    author = get_object_or_404(User, id=author_id)
    registiration_date = author.date_joined
    posts = Post.objects.filter(author= author_id)

    context = {
        'author':author,
        'registiration_date' :registiration_date,
        'posts':posts
    }

    return render(request, "user/profileAuthor.html", context)

def userSettings(request):
    if not request.user.is_authenticated:
        messages.info(request, "Ayarlar sayfasını görüntüleyebilmek için giriş yapmalısınız.")
        return redirect("user:login")
    return render(request, "user/settings.html")

def change_username(request):
    if not request.user.is_authenticated:
        return redirect("user:login")
    if request.method == "POST":
        form = ChangeUsernameForm(request.POST)
        if form.is_valid():
            new_username = form.cleaned_data["new_username"]
            request.user.username = new_username
            request.user.save()
            messages.success(request, "Kullanıcı adı başarıyla değiştirildi")
            return redirect("user:settings")
        
    else:
        form = ChangeUsernameForm()

    return render(request, "user/change_username.html", {"form":form})

def change_password(request):
    if not request.user.is_authenticated:
        return redirect("user:login")
    if request.method == "POST":
        form = PasswordChangeForm(request.user, request.POST)
        if form.is_valid():
            user = form.save()
            update_session_auth_hash(request, user)
            messages.success(request, "Parola başarıyla değiştirildi")
            return redirect("user:settings")
    else:
        form = PasswordChangeForm(request.user)

    return render(request, "user/change_password.html", {"form": form})


def delete_profile(request):
    if not request.user.is_authenticated:
        return redirect("user:login")
    if request.method == "POST":
        request.user.delete()
        messages.success(request, "Hesabınız başarıyla silindi")
        return redirect("index")
    else:
        return render(request, "user/delete_profile_confirmation.html")
    

def follower(request):
    followers_count = UserProfile.objects.get(user_id = 1)
    followers_count = {
        "followers_count":followers_count,
    }
    return render(request, "user/profileAuthor.html", followers_count)


# Rest Framework ------------------------------------


class UserModelViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserModelSerializer


