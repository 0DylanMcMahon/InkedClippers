from django.db import models
from django.contrib.auth.models import User


"""
I changed the Team members model name to Barbermembers and created a new
TeamMembers model. the name never changed in the admin panel
and its a bit confusing.
"""


class BarberMembers(models.Model):
    """
    Model for the barbers info
    """
    name = models.CharField(max_length=100)
    image = models.ImageField(upload_to='staff/')
    role = models.CharField(max_length=100)
    bio = models.TextField()

    def __str__(self):
        return self.name


class TeamMembers(models.Model):
    """
    Model for all the team members info
    """
    name = models.CharField(max_length=100)
    image = models.ImageField(upload_to='staff/')
    role = models.CharField(max_length=100)
    bio = models.TextField()

    def __str__(self):
        return self.name


class TattooMembers(models.Model):
    """
    Model for the Tattoo and piercer info
    """
    name = models.CharField(max_length=100)
    image = models.ImageField(upload_to='staff/')
    role = models.CharField(max_length=100)
    bio = models.TextField()

    def __str__(self):
        return self.name


class UserTestimonial(models.Model):
    """
    Model for Users to leave testimonials
    """
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    review = models.TextField()
    member = models.ForeignKey(TeamMembers, on_delete=models.CASCADE)
    date_created = models.DateTimeField(auto_now_add=True)

    RATING_CHOICES = (
        (1, '⭐'),
        (2, '⭐⭐'),
        (3, '⭐⭐⭐'),
        (4, '⭐⭐⭐⭐'),
        (5, '⭐⭐⭐⭐⭐'),
    )

    BARBER = 'Barber'
    TATTOO_ARTIST = 'Tattoo Artist'
    PIERCER = 'Piercer'
    SERVICE_CHOICES = [
        (BARBER, 'Barber'),
        (TATTOO_ARTIST, 'Tattoo Artist'),
        (PIERCER, 'Piercer')
    ]

    service = models.CharField(choices=SERVICE_CHOICES, max_length=20)
    rating = models.IntegerField(choices=RATING_CHOICES)

    def __str__(self):
        return f"Testimonial by {self.user.username}"


class BarberServices(models.Model):
    """
    Model for the Barbers services
    """
    name = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=5, decimal_places=2)
    discount_price = models.DecimalField(max_digits=5, decimal_places=2)


class TattooServices(models.Model):
    """
    Model for the Tattoo & piercer info
    """
    name = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=5, decimal_places=2)
    discount_price = models.DecimalField(max_digits=5, decimal_places=2)


class TattooQuestions(models.Model):
    """
    Model for asking questions about getting a tattoo
    """
    question = models.CharField(max_length=200)
    answer = models.TextField()


class AftercareQuestions(models.Model):
    """
    Model for asking questions about tattoo aftercare
    """
    question = models.CharField(max_length=200)
    answer = models.TextField()
