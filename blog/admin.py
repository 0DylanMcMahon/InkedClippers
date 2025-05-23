from django.contrib import admin
from .models import Post
from tinymce.widgets import TinyMCE
from django.db import models

class BlogPostAdmin(admin.ModelAdmin):
    formfield_overrides = {
        models.TextField: {'widget': TinyMCE()},
    }

admin.site.register(Post, BlogPostAdmin)