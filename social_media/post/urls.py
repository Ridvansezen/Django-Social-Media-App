from django.urls import path, include
from post import views
import social_media.settings 
from django.conf.urls.static import static

from rest_framework.routers import DefaultRouter
from .views import ModelViewSet

app_name = "post"

router = DefaultRouter()
router.register(r'posts', ModelViewSet)

urlpatterns = [
    path('', views.posts, name="posts"),
    path('dashboard/', views.dashboard, name="dashboard"),
    path('addpost/', views.addPost, name="addPost"),
    path('update/<int:id>', views.updatePost, name="updatePost"),
    path('delete/<int:id>', views.deletePost, name="deletePost"),

]
urlpatterns += static(social_media.settings.MEDIA_URL, document_root=social_media.settings.MEDIA_ROOT)