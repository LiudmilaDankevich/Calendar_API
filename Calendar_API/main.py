import requests
import json


payload = {'name' : 'Milla', 'job' : 'QATesting'}
r = requests.post('https://reqres.in/api/users', json=payload)
print(r.text)