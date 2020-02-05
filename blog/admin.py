from django.contrib import admin
from .models import BlogPost


# Register your models here.
class BlogPostAdmin(admin.ModelAdmin):
    list_display = ['title', 'added', 'updated']
    # fields = ['title']
    list_filter = ['added', 'updated'
    ]

admin.site.register(BlogPost, BlogPostAdmin)
