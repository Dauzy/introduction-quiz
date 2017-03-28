import requests
import json

url = "http://locahost:9200/beeva/quiz?pretty"
quiz_json = 'introduction_quiz.json'
with open('introduction_quiz.json') as data_file:
	data = json.load(data_file)

response = requests.post(url, json=data)
results = json.loads(response.text)
print(response.text)
