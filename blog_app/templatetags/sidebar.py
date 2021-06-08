from django import template
from blog_app.models import Post, Tag

register = template.Library()


@register.inclusion_tag('blog_app/popular_posts.html')
def get_popular(cnt=3):
    posts = Post.objects.order_by('-views')[:cnt]
    return {'posts': posts}
