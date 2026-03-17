
import json

with open('data.json', 'r') as file:
    data = json.load(file)

for item in data:
    if item["Energy"] == "Happy":
        print(item["Song"])
