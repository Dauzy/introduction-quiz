import requests
import json
url = "http://locahost:80"
headers = {'Content-type': 'application/json', 'Accept': 'text/plain'}
quiz_json = 'introduction_quiz.json'
respuestas = open(quiz_json)
data = json.load(respuestas)

r = requests.post(url, data=json.dumps(data), headers=headers)
r.status_code
r.json()
print(data)
