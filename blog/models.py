from django.db import models
from django.utils import timezone
from tinymce.models import HTMLField
from django.contrib.auth.models import User
from django.utils.text import slugify
from django.urls import reverse




class Post(models.Model):
    title = models.CharField(max_length=200)
    content = HTMLField()
    excerpt = models.CharField(max_length=300, blank=True, null=True)
    cover_image = models.ImageField(upload_to='blog_images/', blank=True, null=True)
    date_posted = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(default=timezone.now)
    slug = models.SlugField(unique=True, blank=True, null=True)
    published = models.BooleanField(default=False)

    def save(self, *args, **kwargs):
        if not self.slug:  # Generate slug if it's missing
            self.slug = slugify(self.title)
        super().save(*args, **kwargs)
    
    def get_absolute_url(self):
        return reverse('blog_detail', kwargs={'slug': self.slug})

    def __str__(self):
        return self.title

    
