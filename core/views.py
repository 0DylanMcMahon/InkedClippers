from django.shortcuts import render, redirect, get_object_or_404
from .models import (
    BarberMembers,
    TeamMembers,
    BarberServices,
    UserTestimonial,
    TattooMembers,
    TattooServices,
    TattooQuestions,
    AftercareQuestions
)
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import UserPassesTestMixin
from django.contrib import messages
from .forms import TestimonialForm
from django.urls import reverse, reverse_lazy
from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView,
)


class UserTestimonialsListView(ListView):
    """
    List view to display a list of UserTestimonials.
    """
    model = UserTestimonial
    template_name = 'core/home.html'
    context_object_name = 'new_testimonial'
    paginate_by = 3


class UserTestimonialsDetailView(DetailView):
    """
    Detail view to display a single UserTestimonial.
    """
    model = UserTestimonial


@login_required
def add_testimonial(request):
    """
    View for adding/creating a Testimonial.
    """
    if request.method == 'POST':
        form = TestimonialForm(request.POST)
        if form.is_valid():
            testimonial = form.save(commit=False)
            testimonial.user = request.user
            testimonial.save()
            messages.success(request, 'Thank you for leaving a review')
            return redirect('/')
    else:
        form = TestimonialForm()
    context = {
        'form': form
    }
    return render(request, 'core/add_testimonial.html', context)


class testimonialUpdate(UserPassesTestMixin, UpdateView):
    """
    View for updating a Testimonial.
    """
    model = UserTestimonial
    fields = ['review', 'rating', 'member', 'service']

    def test_func(self):
        testimonial = self.get_object()
        return self.request.user == testimonial.user

    def form_valid(self, form):
        response = super().form_valid(form)
        messages.success(
            self.request,
            'You have successfully updated your review'
            )
        return response

    def get_success_url(self):
        return reverse('testimonials-detail', args=[self.object.pk])


class testimonialDelete(UserPassesTestMixin, DeleteView):
    """
    View for deleting a Testimonial.
    """
    model = UserTestimonial
    success_url = reverse_lazy('home-page')

    def test_func(self):
        testimonial = self.get_object()
        return self.request.user == testimonial.user

    def delete(self, request, *args, **kwargs):
        messages.success(request, 'You have successfully deleted your review')
        return super().delete(request, *args, **kwargs)


def about(request):
    """
    View for the about page
    """
    return render(request, 'core/about.html')


def team(request):
    """
    View for barbers page which has services and barbershop employees
    """
    services = BarberServices.objects.all()
    membersB = BarberMembers.objects.all()
    membersT = TattooMembers.objects.all()
    context = {
        'services': services,
        'membersB': membersB,
        'membersT': membersT,
    }
    return render(request, 'core/team.html', context)


def service(request):
    """
    View for tattoo page which has services, tattoo studio employees
    and a FAQ's for questions about getting a tattoo and aftercare
    """
    members = TattooMembers.objects.all()
    services = BarberServices.objects.all()
    questions = TattooQuestions.objects.all()
    aftercare_questions = AftercareQuestions.objects.all()
    ear_piercings = TattooServices.objects.filter(name__in=[
        'Lobe',
        'Helix',
        'Tragus',
        'Anti-Tragus',
        'Conch',
        'Rook',
        'Daith',
        'Forward Helix',
        'Industrial']
        )

    facial_piercings = TattooServices.objects.filter(name__in=[
        'Eyebrow',
        'Anti-Eyebrow',
        'Nose',
        'Septum',
        'Bridge',
        'Rhino',
        'Cheek',
        'Dahlia']
        )

    oral_piercings = TattooServices.objects.filter(name__in=[
        'Tongue',
        'Web',
        'Smiley',
        'Labret',
        'Vertical Labret',
        'Ashley',
        'Medusa',
        'Monroe']
        )

    body_piercings = TattooServices.objects.filter(name__in=[
        'Navel',
        'Nipple',
        'Nape',
        'Surface',
        'Custom',
        'Microdermal',
        'Genital']
        )
    context = {
        'members': members,
        'services': services,
        'ear_piercings': ear_piercings,
        'facial_piercings': facial_piercings,
        'oral_piercings': oral_piercings,
        'body_piercings': body_piercings,
        'questions': questions,
        'aftercare_questions': aftercare_questions,
    }
    return render(request, 'core/service.html', context)
