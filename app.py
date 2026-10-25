from flask import Flask, jsonify

app = Flask(__name__)

@app.get("/")
def home():
    return jsonify(message="Hello from Jenkins CI/CD!")

@app.get("/health")
def health():
    return jsonify(status="ok")

