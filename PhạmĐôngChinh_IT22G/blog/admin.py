from django.contrib import admin
from .models import Blog, CategoryBlog


class BlogAdmin(admin.ModelAdmin):
    list_display = ['title', 'date']
    list_filter = ['title']
    search_fields = ['title', 'date']

admin.site.register(Blog, BlogAdmin)
admin.site.register(CategoryBlog)
