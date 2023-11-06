"""
URL configuration for social_media project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from post import views
import social_media.settings
from django.conf.urls.static import static

from rest_framework.routers import DefaultRouter
from post.views import ModelViewSet
from user.views import UserModelViewSet

router = DefaultRouter()
router.register(r'posts', ModelViewSet)
router.register(r'user_profiles', UserModelViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name="index"),
    path('user/', include("user.urls")),
    path('posts/', include("post.urls")),
    path('api/', include(router.urls), name='api'),
    
]
urlpatterns += static(social_media.settings.MEDIA_URL, document_root=social_media.settings.MEDIA_ROOT)