import requests
import json

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

print('http://localhost:4200/dashboard?token='+access_token())
