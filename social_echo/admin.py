from django.contrib import admin
from .models import Posts


@admin.register(Posts)
class PostsAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'message', 'author')
    list_display_links = ('id', 'title', 'message', 'author')
    list_per_page = 10
    ordering = ['-id']
    search_fields = ['title', 'id', 'author__username']
