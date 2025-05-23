from django.urls import path, include
from .views import blog_home, blog_detail
from . import views

urlpatterns = [
    path('', views.blog_home, name='blog-home'),
    path('<slug:slug>/', blog_detail, name='blog_detail'),
    path('tinymce/', include('tinymce.urls')),
]