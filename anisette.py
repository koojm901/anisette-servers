from flask import Flask, jsonify
import os

app = Flask(__name__)

@app.route('/', methods=['GET'])
def home():
    return jsonify({
        "status": "online",
        "message": "AniServer is running!"
    })

# Gunicorn이 'app' 변수를 찾고 Flask가 모듈을 인식하도록 강제합니다.
os.environ['FLASK_APP'] = 'anisette'
