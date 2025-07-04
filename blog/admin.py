# board/admin.py

from django.contrib import admin
# add
from .models import Post, Tag
from .forms import PostForm

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    form = PostForm

    def save_model(self, request, obj, form, change):
        super().save_model(request, obj, form, change)
        tags = form.cleaned_data.get('tag_input', [])
        obj.tags.clear()
        for tag_name in tags:
            tag_obj, created = Tag.objects.get_or_create(name=tag_name)
            obj.tags.add(tag_obj)

@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    list_display = ['name']
