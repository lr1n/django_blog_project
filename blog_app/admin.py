from django.contrib import admin
from django import forms
from ckeditor_uploader.widgets import CKEditorUploadingWidget
from django.utils.safestring import mark_safe

from .models import Category, Tag, Post


class CategoryAdmin(admin.ModelAdmin):
    list_display = ('pk', 'title', 'slug')
    list_display_links = ('pk', 'title')
    search_fields = ('title',)
    prepopulated_fields = {'slug': ('title',)}


class TagAdmin(admin.ModelAdmin):
    list_display = ('pk', 'title', 'slug')
    list_display_links = ('pk', 'title')
    search_fields = ('title',)
    prepopulated_fields = {'slug': ('title',)}


class PostAdminForm(forms.ModelForm):
    content = forms.CharField(widget=CKEditorUploadingWidget())

    class Meta:
        model = Post
        fields = '__all__'


class PostAdmin(admin.ModelAdmin):
    save_on_top = True
    list_display = (
        'id', 'title', 'slug', 'category', 'created_at', 'get_photo'
    )
    list_display_links = ('id', 'title')
    search_fields = ('title',)
    list_filter = ('category',)
    readonly_fields = ('views', 'created_at', 'get_photo')
    # in this order fields will be shown us when we are in editing mode
    fields = (
        'title',
        'slug',
        'category',
        'tags',
        'content',
        'photo',
        'get_photo',
        'views',
        'created_at',
    )
    prepopulated_fields = {'slug': ('title',)}
    form = PostAdminForm

    def get_photo(self, obj):
        """This method allows us to see the picture itself in 'list_display',
        not a link to it, because if we use the name of field 'photo', we will
        see a link to it, not a photo.
        """
        if obj.photo:
            return mark_safe(f'<img src="{obj.photo.url}" width="50">')
        else:
            return '-'

    # it's for representation in admin
    get_photo.short_description = 'photo'

    # # 'save_us' allow us change some content in post and save it
    # # as new object in db
    # save_as = True


admin.site.register(Category, CategoryAdmin)
admin.site.register(Tag, TagAdmin)
admin.site.register(Post, PostAdmin)
