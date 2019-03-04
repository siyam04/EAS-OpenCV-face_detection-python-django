from django.contrib import admin

# same app
from user_authentication.models import Profile


class ProfileAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'profile_image']
    list_display_links = ['name']
    list_filter = ['name']


admin.site.register(Profile, ProfileAdmin)

