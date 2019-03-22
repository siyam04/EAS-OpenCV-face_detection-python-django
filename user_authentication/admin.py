from django.contrib import admin
# same app
from user_authentication.models import Profile, Authentication


# Dashboard customization

# For 'Profile Table'
class ProfileAdmin(admin.ModelAdmin):

    # Editable 'username'
    list_editable = ['username']

    # Filtering by 'name' and 'id'
    list_filter = ['name', 'id']

    # Direct click ability to the 'name'
    list_display_links = ['name']

    # Search by 'id' and 'name'
    search_fields = ['id', 'name']

    # Display fields according to this order from 'Profile Table'
    list_display = ['id', 'name', 'username', 'profile_image']


# For 'Authentication Table'
class AuthenticationAdmin(admin.ModelAdmin):

    # Editable 'is_active'
    list_editable = ['is_active']

    # Direct click ability to the 'profile'
    list_display_links = ['profile']

    # Search by 'id' and 'is_active'
    search_fields = ['id', 'is_active']

    # Filtering by 'is_active' and 'profile'
    list_filter = ['is_active', 'profile']

    # Display fields according to this order from 'Authentication Table'
    list_display = ['id', 'profile', 'date_time', 'is_active']


# Registration with system
admin.site.register(Profile, ProfileAdmin)
admin.site.register(Authentication, AuthenticationAdmin)

