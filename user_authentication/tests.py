from django.test import TestCase

# Create your tests here.
from django.test import TestCase
from user_authentication.models import Profile
from django.core.files.images import ImageFile
from django.urls import reverse
# Create your tests here.
class AttendanceTest(TestCase):
    def setUp(self):
        print("Running setup")
        p = Profile.objects.create()
        p.name = "Some name"
        p.profile_image =  ImageFile(open("ccccc.jpg", "rb"))
        p.save(())    
    
    def test_attendance_update(self):
        data = {'id':1}
        r = self.client.post(reverse('update-attendance'), data = data)
        self.assertEqual(201, r.status_code)
