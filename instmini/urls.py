from django.urls import path
from .views import *
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('image/<id>', ImageAPIView.as_view()),
    path('posts/new', PostCreateAPIView.as_view()),
    path('tags', TagListCreateAPIView.as_view()),
    path('posts', PostListAPIView.as_view()),
    # path('users/<int:pk>', UsersPostListAPIView.as_view())
    path('users/<str:username>', UsersPostListAPIView.as_view())
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
