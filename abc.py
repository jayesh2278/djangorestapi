import requests
import json

data = {
    "username": "jayesh",
    "password": "jayesh"
}
url = "http://localhost:8000/api/authtoken/"
response = requests.post(url, data=data)
token = json.loads(response.text).get('token')
print(token)

if token:
     token = f"Token {token}"
     headers = {"Authorization": token}
     response = requests.get("http://localhost:8000/api/ArticleListView", headers=headers)
     print(response.text)
else:
     print('No Key')