import requests
import json


payload = {'PhoneNumber': '+375297521744'}
r = requests.post('https://dev.dsync.app:6443/api/Identity/getOTP', json=payload)
print(r.text)