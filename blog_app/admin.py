from django.contrib import admin

from .models import Category, Tag, Post


class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('title',)}


class TagAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('title',)}


class PostAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('title',)}


admin.site.register(Category)
admin.site.register(Tag)
admin.site.register(Post)
