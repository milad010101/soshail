from atexit import register
from pdb import post_mortem
from django.contrib import admin
from .models import Post
from home import models


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('user', 'slug', 'updted')
    list_filter = ('createf',)
    search_fields = ('slug',)
    prepopulated_fields = {'slug': ('body',)}
