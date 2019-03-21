from django.db import models
from django.contrib.auth.models import User


class Profile(models.Model):
    """Authenticated User Profile"""

    name = models.CharField(max_length=50, null=False)
    profile_image = models.ImageField(upload_to='profile_img', blank=False)

    def __str__(self):
        return self.name

# class AttendanceManager(models.Manager):
#     def 

class Authentication(models.Model):
    """Changing Status of a User based on real OpenCV Data"""

    profile = models.ForeignKey(Profile, on_delete=models.CASCADE)
    date_time = models.DateTimeField(auto_now_add=True)
    is_active = models.BooleanField(default=False)

    def __str__(self):
        return str(self.is_active)
