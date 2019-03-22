from datetime import datetime
from rest_framework.views import APIView
from rest_framework import status
from rest_framework.response import Response

# Same app importing
from user_authentication.models import Profile, Authentication


# 'Attendance Creating' API views from OpenCV data

# API Logic function

class Users(APIView):
    """Receives data from OpenCV file using API and creates real time attendance"""

    def get(self, request, username):
        """Matching process through API data"""

        # Checking existence of OpenCV 'username' with saved 'username' from Profile table into database
        if Profile.objects.filter(username=username).exists():

            # If 'username' exists, then matched and get
            verified_username = Profile.objects.get(username=username)

            # Then save the 'username' into Authentication table into database
            attend_obj, attendance_created = Authentication.objects.get_or_create(
                profile=verified_username,
                is_active=True,
                date_time__date=datetime.today()
            )

            print('\n---------------------------------------------------------------------')

            # Shows the 'received data' status to the server output
            print('- RECEIVED-DATA STATUS: ', attend_obj)

            # If attendance created successfully
            if attendance_created:

                # Shows the 'attendance status' to the server output
                print('- ATTENDANCE STATUS:', attendance_created)

                # API context in JSON format
                context = {"status": "Attendance Created for {}".format(username)}

                # Returns status 201 for successfully created!
                return Response(context, status=status.HTTP_201_CREATED)

            # If Not
            else:
                # Shows the 'attendance status' to the server output
                print('- ATTENDANCE STATUS:', attendance_created)

                # API context in JSON format
                context = {"status": "Attendance Already Exists for {}".format(username)}

                # Returns status 200 for existence!
                return Response(context, status=status.HTTP_200_OK)

        else:
            # Returns status 404 for not matching!
            return Response("ERROR 404!", status=status.HTTP_404_NOT_FOUND)



