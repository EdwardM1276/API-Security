from flask import Flask, jsonify, request 
import os
import hashlib

app = Flask(__name__)



def hash_password(password):
    return hashlib.sha256(password.encode()).hexdigest()
#Our sensitive data

data = {"users": [
    {"Administrator":"admin","password":hash_password("admin2020"),"ssn":"123-45-6789","email":"admin@edu.com"},
    {"Thabo":"user1","password":hash_password("Thabo2020"),"ssn":"987-65-4321","email":"thabo@edu.com"},
        ]}

API_KEY = os.getenv("API_KEY","mySecretKey")

def is_authorized():
    auth_key =request.headers.get("X-API-Key")
    return auth_key == API_KEY

@app.route("/data")

def get_data():
    if not is_authorized():
        return jsonify({"error": "Unauthorized"}), 401
    return jsonify(data) 

if __name__ == "__main__":
    app.run(host = "127.0.0.1", port=3000)

