from django.shortcuts import render, get_object_or_404
from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view
# Same app
from .models import Profile, Authentication


def input(request):
    """Input Authenticated User's info"""

    # Returns all instances with id into terminal
    saved_data = Profile.objects.values_list('id', 'name').distinct()
    print(saved_data)

    # Verify user by unique id
    if request.method == 'POST':
        id = request.POST['id']
        print(id)

        # Mapping with saved data
        profile = get_object_or_404(Profile, id=id)
        template = 'user_authentication/single_user.html'
        context = {'profile': profile}
        # Shows data if matched
        return render(request, template, context)

    # Returns input page if no submission
    template = 'user_authentication/input.html'
    return render(request, template)


def single_user(request, id=None):
    """Returns single user's data"""

    profile = get_object_or_404(Profile, id=id)
    context = {'profile': profile}
    template = 'user_authentication/single_user.html'

    return render(request, template, context)


def all_users(request):
    """Returns All User's info"""

    user_data_all = Profile.objects.all().order_by('-id')
    template = 'user_authentication/all_users.html'
    context = {'user_data_all': user_data_all}

    return render(request, template, context)


@api_view(['POST'])
def update_attendance(request):
    """Custom API for take input from OpenCV file"""

    user_id = request.POST.get('id')
    if Profile.objects.filter(pk=user_id).exists():
        p = Profile.objects.get(pk=user_id)
        a = Authentication(profile=p, is_active=True)
        a.save()
        return Response("Attendance Created", status=status.HTTP_201_CREATED)
    else:
        return Response("Profile not found", status= status.HTTP_404_NOT_FOUND)

