import os
import cv2
import requests
import numpy as np
import face_recognition
from os.path import splitext


# make a list of all the available images
images = os.listdir('images')
known_face_encodings = []
known_face_names = []

for i in os.listdir('images'):
    pic = face_recognition.load_image_file('images/'+i)
    known_face_encodings.append(face_recognition.face_encodings(pic)[0])
    known_face_names.append(i[:i.rfind('_')])

video_capture = cv2.VideoCapture(0)

while True:

    # load your image
    _, frame = video_capture.read()
    frameRGB = cv2.cvtColor(frame,cv2.COLOR_BGR2RGB)

    # encoded the loaded image into a feature vector
    image_to_be_matched_encoded = face_recognition.face_encodings(frameRGB)

    if len(image_to_be_matched_encoded) > 0:

        # iterate over each image
        for (i, image) in enumerate(known_face_encodings):

            # encode the loaded image into a feature vector
            current_image_encoded = image_to_be_matched_encoded[0]

            # match your image with the image and check if it matches
            result = face_recognition.compare_faces([image], current_image_encoded)

            if result[0] == True:
                distance = np.linalg.norm(image-current_image_encoded)

                # check if it was a match
                if distance <= 0.40:

                    # Takes same username without .jpg/.png Extension
                    user_name = splitext(known_face_names[i])[0]

                    # Shows the username to the terminal
                    print("\n----OpenCV List Data----\n- Name: {}".format(user_name))

                    # Django API receives the Matched username from OpenCV
                    URL = "http://127.0.0.1:8000/matched-user/{}/".format(user_name)

                    # Sending API get request and saving the response as response object
                    data_send = requests.get(url=URL)

                    # Shows the RESPONSE ro the terminal based on Status
                    if data_send.status_code == 200:
                        print('- Already Exist! ', data_send)
                    elif data_send.status_code == 201:
                        print('- Created :) ', data_send)
                    else:
                        print('- Not Found :o', data_send)

    # Display the resulting image
    cv2.imshow('Video', frame)

    # Hit 'q' on the keyboard to quit!
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release handle to the WebCam
video_capture.release()
cv2.destroyAllWindows()
