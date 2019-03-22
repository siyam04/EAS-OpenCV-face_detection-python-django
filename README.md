# Employee Attendance System by Real-Time Face Detection
* Powered by Python, Django, and OpenCV.

## OS support: Windows10 or Linux.
* Some commands may differ depending on OS. Just google it.

## Instructions: 
* Install latest version of Python
* Install and active virtual environment directory
  1. Open cmd
  2. pip install virtualenv 
  3. Choose destination: cd Desktop> virtualenv YourEnvironmentName 
  4. cd YourEnvironmentName\Scripts>activate
  5. cd.. (exit from Scripts)
* Clone this GitHub repository into your local virtual environment directory (YourEnvironmentName)
* Go to project directory (GitHub repository) where 'manage.py' file exist
* Install all the requirements using previously opened cmd where the virtual environment was activated: 
  1. pip install -r requirements.txt
* Run local server:
  1. python manage.py runserver

#### Type those URLs to the browser:
* API: http://127.0.0.1:8000/matched-user/galib/ (API takes any username for: /galib/)
* EAS Admin dashboard: http://127.0.0.1:8000/admin/
* Manual input: http://127.0.0.1:8000/user/input/
* Single object: http://127.0.0.1:8000/user/single-user/galib/ (takes any username for: /galib/)
* All objects: http://127.0.0.1:8000/user/all-users/

#### Run OpenCV Face Detection:
* Go to project directory (GitHub repository) where 'manage.py' file exist
* Go to openCV_face_recognition directory
* Open cmd here
* Type and Hit Enter:
  1. python facerecognition.py

#### Open both CMD (local server and face recognition) and API dashboard to monitoring the outputs
* status code 201 = Attendance created
* status code 200 = Attendance already exists
* status code 404 = ERROR

#### Server cmd output
![BackEnd server output](https://user-images.githubusercontent.com/23103980/54853075-f36be880-4d18-11e9-8c19-27ecb7d8e12a.PNG)

#### OpenCV cmd output
![OpenCV server output](https://user-images.githubusercontent.com/23103980/54853120-17c7c500-4d19-11e9-8d0e-d97e295b4204.PNG)

#### EAS Admin dashboard
![EAS Dashboard](https://user-images.githubusercontent.com/23103980/54848947-de895800-4d0c-11e9-9fbb-0a9f85531d07.png)

#### API dashboard
![API dashboard](https://user-images.githubusercontent.com/23103980/54848970-f3fe8200-4d0c-11e9-9a94-93ece9717422.PNG)

#### API JSON
![API JSON](https://user-images.githubusercontent.com/23103980/54848989-037dcb00-4d0d-11e9-8bf4-434cb38a797e.png)

#### Manual Input from browser (http://127.0.0.1:8000/user/input/)
![Manual input](https://user-images.githubusercontent.com/23103980/54852796-1e097180-4d18-11e9-9d9a-fc9144491996.png)

#### Verification matched for single object
![Single object matching](https://user-images.githubusercontent.com/23103980/54849105-7d15b900-4d0d-11e9-8967-18e5c86aca60.png)

#### Single object by URL (http://127.0.0.1:8000/user/single-user/galib/)
![Single object matching](https://user-images.githubusercontent.com/23103980/54849253-e3024080-4d0d-11e9-9512-a3b2a808ca7e.png)

#### All objects by URL (http://127.0.0.1:8000/user/all-users/)
![All objects from the Database](https://user-images.githubusercontent.com/23103980/54849293-01683c00-4d0e-11e9-9176-fd04610cfe1a.png)

