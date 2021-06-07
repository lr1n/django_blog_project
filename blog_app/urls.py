from django.urls import path

from blog_app.views import Home, get_category, get_post


urlpatterns = [
    path('', Home.as_view(), name='home'),
    path('category/<str:slug>', get_category, name='category'),
    path('post/<str:slug>', get_post, name='post'),
]
