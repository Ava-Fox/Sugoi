import json

with open("sample.json", "r") as file:
    data = json.loads(file.read())
    print(data)