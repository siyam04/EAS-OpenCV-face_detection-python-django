from django.urls import path

# Same app
from .views import input, single_user, all_users, update_attendance


urlpatterns = [

    path('input/', input, name='input'),
    path('all-users/', all_users, name='all-users'),
    path('single-user/<int:id>/', single_user, name='single-user'),
    path('update-attendance', update_attendance, name='update-attendance')

]

