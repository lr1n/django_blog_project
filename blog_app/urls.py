from django.urls import path

from blog_app.views import Home, get_category, get_post


urlpatterns = [
<<<<<<< HEAD
    path('', Home.as_view(), name='home'),
    path('category/<str:slug>', get_category, name='category'),
    path('post/<str:slug>', get_post, name='post'),
=======
    path('', index, name='home'),
    path('category/<str:slug>', get_category, name='category'),
>>>>>>> 859a0113fef3090768f4b2870296a812dc199f76
]
