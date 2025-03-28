from django.urls import path
from .views import (
    UserTestimonialsListView,
    UserTestimonialsDetailView,
    testimonialUpdate,
    testimonialDelete
)
from . import views

urlpatterns = [
    path('', UserTestimonialsListView.as_view(), name='home-page'),
    path(
        'UserTestimonials/<int:pk>/',
        UserTestimonialsDetailView.as_view(),
        name='testimonials-detail'
        ),
    path('about/', views.about, name='about-page'),
    path('team/', views.team, name='team-page'),
    path('service/', views.service, name='service-page'),
    path('add_testimonial/', views.add_testimonial, name='testimonial-page'),
    path(
        'edit_testimonial/<int:pk>',
        views.testimonialUpdate.as_view(),
        name='edit-testimonial-page'
        ),
    path(
        'delete_testimonial/<int:pk>',
        views.testimonialDelete.as_view(),
        name='delete-testimonial-page'
        ),
]
