import pip
import requests
import json
import os
try:
  import pyperclip
except ImportError:
  os.system('pip3 install pyperclip')


def access_token():
  url = ''
  header = {'Content-Type': 'application/json'}
  params = {
    "userId": "",
    "userPassword": "",
    "grantType": "password",
    "clientId": "",
    "clientPassword": ""
  }
  r = requests.post(url,data = json.dumps(params), headers = header)
  # a = r.content.decode()
  response_body = r.json()['data']
  # response_count = r.json()['body']['count']
  return response_body[0]['access_token']

try:
  pyperclip.copy('grp-portal/dashboard?token='+access_token())
except pyperclip.PyperclipException:
  os.system('sudo apt-get install xclip')
# print('http://localhost:4200/grp-portal/dashboard?token='+access_token())
