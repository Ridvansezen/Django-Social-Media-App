from django.shortcuts import render

def followers(request):
    followers_count = 12
    context = {
        "followers_count": followers_count
    }
    return followers_count