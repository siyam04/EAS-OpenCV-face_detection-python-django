import requests


r = requests.post('http://localhost:8000/user/update-attendance', data={'id': 1})

print(r)
