from django.shortcuts import render
from django.http import HttpResponse
from .models import Post


def blog_home(request):
    context = {
        'posts': Post.objects.all(),
        'title': 'About'
    }
    return render(request, 'blog/blog.html', context,)

def about(request):
    return HttpResponse('<h1>Blog About</h1>')
    