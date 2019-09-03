# Employee Attendance System by Real-Time Face Detection.
* Developed By Python, Django REST Framework, and OpenCV.

## Instructions (Windows 10x64):
* Some commands may differ depending on OS. Just google it.

* Install latest version of Python3 (64 bit).

* Install and active virtual environment directory
  1. Open cmd
  2. :~$ pip install virtualenv 
  3. Choose destination: :~$ cd Desktop> virtualenv YourEnvironmentName 
  
* Clone this GitHub repository into local machine.

* Go to project directory (GitHub repository) where 'manage.py' file exist.

* Copy 'YourEnvironmentName' folder to the 'GitHub repository'.

* Active virtual environment:
  1. :~$ cd YourEnvironmentName\Scripts>
  2. :~$ activate
  3. (YourEnvironmentName):~$ This '(YourEnvironmentName)' sign will be shown up if virtual environment activated successfully.
  4. :~$ cd../.. (exit from Scripts)

* Install all the requirements using previously opened CMD where the virtual environment was activated:
  >> (YourEnvironmentName):~$ pip install -r requirements.txt
  
* Run Local Server:
  >> (YourEnvironmentName):~$ python manage.py runserver

* PATHs:
  1. API: http://127.0.0.1:8000/matched-user/galib/ (API takes any username for: /galib/)
  2. EAS Admin dashboard: http://127.0.0.1:8000/admin/
  3. Manual input: http://127.0.0.1:8000/user/input/
  4. Single object: http://127.0.0.1:8000/user/single-user/galib/ (takes any username for: /galib/)
  5. All objects: http://127.0.0.1:8000/user/all-users/

* Run OpenCV Face Detection:
  1. Go to project directory (GitHub repository) where 'manage.py' file exist
  2. Go to openCV_face_recognition directory
  3. Open cmd here
  4. Type and Hit Enter:
     >> (YourEnvironmentName):~$ python facerecognition.py

* Open both CMD (local server and face recognition) and API dashboard to monitoring the outputs
  1. status code 201 = Attendance created
  2. status code 200 = Attendance already exists
  3. status code 404 = ERROR

#### Server cmd output
![BackEnd server output](https://user-images.githubusercontent.com/23103980/54853075-f36be880-4d18-11e9-8c19-27ecb7d8e12a.PNG)

#### OpenCV cmd output
![OpenCV server output](https://user-images.githubusercontent.com/23103980/54853120-17c7c500-4d19-11e9-8d0e-d97e295b4204.PNG)

#### EAS Database
![EAS Dashboard](https://user-images.githubusercontent.com/23103980/55824739-508fd880-5b26-11e9-94a9-b9a700646a3e.png)

#### Real-Time Attendance Creating
![Real-Time Attendance Counting](https://user-images.githubusercontent.com/23103980/55796650-4d77f680-5aec-11e9-975e-3f267d5c9371.png)

#### API dashboard
![API dashboard](https://user-images.githubusercontent.com/23103980/54848970-f3fe8200-4d0c-11e9-9a94-93ece9717422.PNG)

#### API JSON
![API JSON](https://user-images.githubusercontent.com/23103980/54848989-037dcb00-4d0d-11e9-8bf4-434cb38a797e.png)

#### Manual Input from browser (http://127.0.0.1:8000/user/input/)
![Manual input](https://user-images.githubusercontent.com/23103980/55796671-5cf73f80-5aec-11e9-8531-4a6ca2f3b895.png)

#### Verification matched for single object
![Single object matching](https://user-images.githubusercontent.com/23103980/55796689-67b1d480-5aec-11e9-87c9-7f6d6c07ffa9.png)

#### All objects by URL (http://127.0.0.1:8000/user/all-users/)
![All objects from the Database](https://user-images.githubusercontent.com/23103980/55796824-afd0f700-5aec-11e9-9136-af7afc536301.png)

#### Single object by URL (http://127.0.0.1:8000/user/single-user/galib/)
![Single object matching](https://user-images.githubusercontent.com/23103980/55796689-67b1d480-5aec-11e9-87c9-7f6d6c07ffa9.png)



