from django.contrib import admin
from .models import Post


class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'slug', 'author', 'published_time', 'status')
    list_filter = ('status', 'created_time', 'published_time', 'author')
    search_fields = ('title', 'body')
    prepopulated_fields = { 'slug': ('title',) }
    raw_id_fields = ('author',)
    date_hierarchy = 'published_time'
    ordering = ['status', 'published_time']

admin.site.register(Post, PostAdmin)
