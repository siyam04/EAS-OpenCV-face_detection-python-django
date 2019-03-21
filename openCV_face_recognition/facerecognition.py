import os
import requests
import face_recognition
import numpy as np
import cv2


# make a list of all the available images
images = os.listdir('images')
known_face_encodings=[]
known_face_names=[]

for i in os.listdir('images'):
    pic = face_recognition.load_image_file('images/'+i)
    known_face_encodings.append(face_recognition.face_encodings(pic)[0])
    known_face_names.append(i[:i.rfind('_')])

video_capture = cv2.VideoCapture(0)

while True:

    # load your image
    _, frame = video_capture.read()
    frameRGB = cv2.cvtColor(frame,cv2.COLOR_BGR2RGB)
    # image_to_be_matched = face_recognition.load_image_file('testImage/enhanced.png')

    # encoded the loaded image into a feature vector
    image_to_be_matched_encoded = face_recognition.face_encodings(frameRGB)

    if len(image_to_be_matched_encoded)>0:

    # iterate over each image
        for (i, image) in enumerate(known_face_encodings):

            # load the image
            #current_image = face_recognition.load_image_file("images/" + image)

            # encode the loaded image into a feature vector
            current_image_encoded = image_to_be_matched_encoded[0]

            # match your image with the image and check if it matches
            result = face_recognition.compare_faces([image], current_image_encoded)
            #print(result)

            if result[0] == True:
                distance = np.linalg.norm(image-current_image_encoded)
                #print(distance)
                #distance1 = face_recognition.face_distance(image_to_be_matched_encoded,[current_image_encoded])
                #print(distance1)
                #print(distance)
                #print(result)

                #check if it was a match
                if distance <= 0.40:

                    user_name = known_face_names[i]
                    id = i
                    print("----OpenCV List Data----\n" + "name: " + known_face_names[i] + "\nid: " + str(id))

                    # Django API receives the Matched user ID from OpenCV
                    URL = "http://127.0.0.1:8000/matched-user/{}".append(user_name)

                    # defining a params dict for the parameters to be sent to the API
                    # PARAMS = {'id': 2}

                    # TODO: Check this condition before data send. Make sure only 201 will be sent
                    # sending get request and saving the response as response object
                    data_send = requests.get(url=URL)

                    print(data_send, '\n')

    # Display the resulting image
    cv2.imshow('Video', frame)

    # Hit 'q' on the keyboard to quit!
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release handle to the WebCam
video_capture.release()
cv2.destroyAllWindows()
