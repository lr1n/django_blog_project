from django.urls import path

from blog_app.views import Home, PostsByCategory, get_post


urlpatterns = [
    path('', Home.as_view(), name='home'),
    path('category/<str:slug>', PostsByCategory.as_view(), name='category'),
    path('post/<str:slug>', get_post, name='post'),
]
