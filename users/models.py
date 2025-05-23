from django.db import models
from django.contrib.auth.models import User
from PIL import Image
from urllib.request import urlopen


class Profile(models.Model):
    """
    Model for the users profile
    """
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.ImageField(
        upload_to='profile_images/',  # This stores the images in the 'profile_images/' folder inside MEDIA_ROOT
        default='profile_images/logo.png'
    )
    location = models.CharField(max_length=100, default='Ennis')
    phone = models.CharField(max_length=20, default='None')

    def __str__(self):
        return f'{self.user.username} Profile'
