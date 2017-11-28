from django.contrib import admin
from .models import BlogPost


class BlogAdmin(admin.ModelAdmin):
    exclude = ['is_starred']


admin.site.register(BlogPost, BlogAdmin)
