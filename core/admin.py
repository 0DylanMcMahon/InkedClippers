from django.contrib import admin
from .models import (
    TeamMembers,
    UserTestimonial,
    BarberServices,
    TattooServices,
    BarberMembers,
    TattooMembers,
    TattooQuestions,
    AftercareQuestions,
)

# Registered my models here to display them on the admin site
admin.site.register(TeamMembers)

admin.site.register(UserTestimonial)

admin.site.register(BarberServices)

admin.site.register(BarberMembers)

admin.site.register(TattooMembers)

admin.site.register(TattooServices)

admin.site.register(AftercareQuestions)

admin.site.register(TattooQuestions)