from django.shortcuts import render
from django.views.generic import ListView, DetailView
from django.db.models import F

from blog_app.models import Category, Tag, Post


class Home(ListView):
    model = Post
    template_name = 'blog_app/index.html'
    context_object_name = 'posts'
    paginate_by = 4

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Classic Blog Design'
        return context


class PostsByCategory(ListView):
    template_name = 'blog_app/index.html'
    context_object_name = 'posts'
    paginate_by = 4
    # when we allow to non-existent object we will get '404' error
    allow_empty = False

    def get_queryset(self, ):
        return Post.objects.filter(category__slug=self.kwargs['slug'])

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = Category.objects.get(slug=self.kwargs['slug'])
        return context


class PostsByTag(ListView):
    pass


class GetPost(DetailView):
    model = Post
    template_name = 'blog_app/single.html'
    context_object_name = 'post'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        self.object.views = F('views') + 1
        self.object.save()
        self.object.refresh_from_db()
        return context


# def index(request):
#     return render(request, 'blog_app/index.html')


# def get_category(request, slug):
#     return render(request, 'blog_app/category.html')


# def get_post(request, slug):
#     return render(request, 'blog_app/category.html')
