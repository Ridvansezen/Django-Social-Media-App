from django.shortcuts import render,redirect
from user.forms import RegisterForm,LoginForm
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import login,logout,authenticate
from django.db import IntegrityError

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
            return redirect("myapp:index")
        
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
