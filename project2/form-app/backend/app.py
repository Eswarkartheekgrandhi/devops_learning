from flask import Flask, request, jsonify

from flask_cors import CORS

from pymongo import MongoClient

app = Flask(__name__)

CORS(app)

client = MongoClient("mongodb://mongodb:27017/")

db = client["formdb"]

users_collection = db["users"]

@app.route('/submit', methods=['POST'])

def submit():

    data = request.json

    user = {

    "name": data.get("name"),

    "email": data.get("email")

    }

    users_collection.insert_one(user)

    return jsonify({

    "message": "User saved successfully"

    })

@app.route('/users', methods=['GET'])

def get_users():

    users = []

    for user in users_collection.find():

        users.append({

        "id": str(user["_id"]),

        "name": user["name"],

        "email": user["email"]

        })

    return jsonify(users)

if __name__ == '__main__':

    app.run(debug=True, host='0.0.0.0', port=5000)