from django.contrib import admin
from .models import Baiviet, CategoryBlog


class BlogAdmin(admin.ModelAdmin):
    list_display = ['title', 'date']
    list_filter = ['title']
    search_fields = ['title', 'date']


admin.site.register(Baiviet, BlogAdmin)
admin.site.register(CategoryBlog)
