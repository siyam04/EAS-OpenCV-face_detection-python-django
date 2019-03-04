from django.db import models
from django.contrib.auth.models import User


class Profile(models.Model):
    """Authenticated User Profile"""

    name = models.CharField(max_length=50, null=False)
    profile_image = models.ImageField(upload_to='profile_img', blank=False)

    def __str__(self):
        return self.name


