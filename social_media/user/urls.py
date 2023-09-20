from django.urls import path
from user import views

app_name = "user"

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