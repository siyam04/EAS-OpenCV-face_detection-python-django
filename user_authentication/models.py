from django.db import models
from django.contrib.auth.models import User


# Main Database

# Permanent Profile Table
class Profile(models.Model):
    """Authenticated User Profile"""

    # Profile name
    name = models.CharField(max_length=50, null=False)

    # This 'username' is same to the OpenCV image username.
    username = models.CharField(max_length=50, blank=True, null=True)

    # Profile image
    profile_image = models.ImageField(upload_to='profile_img', blank=False)

    # Returns objects by 'name' to the server output
    def __str__(self):
        return self.name


# Real-Time Attendance Authentication Table
class Authentication(models.Model):
    """Changing Status of a User based on real OpenCV Data"""

    # Relational field with the 'Profile Table'. Generates according to the 'Profile Table'
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE)

    # Auto date and time
    date_time = models.DateTimeField(auto_now_add=True)

    # Status
    is_active = models.BooleanField(default=False)

    # Returns objects by 'is_active' to the server output. TypeCasted o String (str()).
    def __str__(self):
        return str(self.is_active)


