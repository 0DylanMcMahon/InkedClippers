from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from .models import Post


def blog_home(request):
    context = {
        'posts': Post.objects.all(),
        'title': 'About',
        'recent_posts': Post.objects.all().order_by('-created_at')[:3],
    }
    return render(request, 'blog/blog.html', context,)

def blog_detail(request, slug):
    context = {
        'post': get_object_or_404(Post, slug=slug),
    }
    return render(request, 'blog/blog_detail.html', context)
    