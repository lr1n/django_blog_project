from django.urls import path

from blog_app.views import Home, PostsByCategory, GetPost, PostsByTag


urlpatterns = [
    path('', Home.as_view(), name='home'),
    path('category/<str:slug>', PostsByCategory.as_view(), name='category'),
    path('tag/<str:slug>', PostsByTag.as_view(), name='tag'),
    path('post/<str:slug>', GetPost.as_view(), name='post'),
]
