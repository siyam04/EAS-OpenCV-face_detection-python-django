from django.urls import path
# Same app
from .views import input, single_user, all_users


# Custom user_authentication app's paths
urlpatterns = [

    # http://127.0.0.1:8000/user/input/
    path('input/', input, name='input'),

    # http://127.0.0.1:8000/user/single-user/galib/
    path('single-user/<username>/', single_user, name='single-user'),

    # http://127.0.0.1:8000/user/all-users/
    path('all-users/', all_users, name='all-users'),

]

