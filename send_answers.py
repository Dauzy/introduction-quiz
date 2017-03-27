import json

quiz_json = 'introduction_quiz.json'

respuestas = open(quiz_json)
data = json.load(respuestas)

print(data)
