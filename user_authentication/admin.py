from django.contrib import admin

# same app
from user_authentication.models import Profile, Authentication


class ProfileAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'username', 'profile_image']
    list_display_links = ['name']
    list_filter = ['name', 'id']
    search_fields = ['id', 'name']


class AuthenticationAdmin(admin.ModelAdmin):
    list_display = ['id', 'profile', 'date_time', 'is_active']
    list_display_links = ['profile']
    list_filter = ['is_active', 'profile']
    search_fields = ['id', 'is_active']


admin.site.register(Profile, ProfileAdmin)
admin.site.register(Authentication, AuthenticationAdmin)

