from django.shortcuts import render


def index(request):
    return render(request, 'blog_app/index.html')


def get_category(request):
    return render(request, 'blog_app/category.html')
