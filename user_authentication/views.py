import json
from datetime import datetime
from django.urls import reverse
from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework.decorators import api_view
from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from rest_framework.views import APIView

# Same app
from .models import Profile, Authentication


############################## Attendance Creating API views from OpenCV #############################

class Users(APIView):
    """Receives data from OpenCV file using API"""
    def get(self, request, username):
        """Matching Process through API Data"""

        # Receive id from OpenCV Data List
        # username = id

        # Matching OpenCV id with Permanent Object id from Database
        if Profile.objects.filter(username=username).exists():

            verified_id = Profile.objects.get(username=username)

            # If matched, then save the id with Authentication table
            attend_obj, attendance_created = Authentication.objects.get_or_create(profile=verified_id, is_active=True, date_time__date=datetime.today())

            # TODO: Save only 1 time. Need to check a condition if this instance is already saved or NOT
            if attendance_created:
                # Returns Status 201 for Success!
                return Response("Attendance Created! of {}".format(username), status=status.HTTP_201_CREATED)
            else:
                return Response("Already counted", status=status.HTTP_200_OK)
        else:
            # Returns Status 404 for Not Matching!
            return Response("Profile not found!", status=status.HTTP_404_NOT_FOUND)


################################# Manual matching views for Django ###################################

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

        template = 'user_authentication/manual_single_user.html'
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

