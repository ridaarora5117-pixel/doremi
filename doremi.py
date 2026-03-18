from flask import Flask, jsonify, request
import json

app = Flask (__name__)

@app.route('/api/data', methods =['GET'])
def get_data():
    return jsonify({"message": "Hello!"})

with open('data.json', 'r') as file:
    data = json.load(file)

user_input = input("Select your mood: Happy / Sad : ")

for item in data:
    if item["Energy"] == user_input:
        print(item["Song"])
        
