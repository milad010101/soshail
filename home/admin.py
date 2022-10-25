from atexit import register
from pdb import post_mortem
from django.contrib import admin
from .models import Post, Coments, Like
from home import models


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('user', 'slug', 'updted')
    search_fields = ('slug',)
    prepopulated_fields = {'slug': ('body',)}


@admin.register(Coments)
class ComentsAdmin(admin.ModelAdmin):
    pass


admin.site.register(Like)
