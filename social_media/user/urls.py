from django.urls import path, include
from user import views

from rest_framework.routers import DefaultRouter
from .views import UserModelViewSet

app_name = "user"

router = DefaultRouter()
router.register(r'user_profiles', UserModelViewSet)

urlpatterns = [
    path('login/', views.loginUser, name="login"),
    path('register/', views.register, name="register"),
    path('logout/', views.logoutUser, name="logout"),
    path('profile/', views.profileUser, name="profileUser"),
    path('profile_author/<int:author_id>/', views.profileAuthor, name="profileAuthor"),
    path('settings/', views.userSettings, name="settings"),
    path('change_username/', views.change_username, name="change_username"),
    path('change_password/', views.change_password, name="change_password"),
    path('delete_profile/', views.delete_profile, name="delete_profile"),
]