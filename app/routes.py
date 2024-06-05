from flask import jsonify
from app import app, mongo

@app.route('/')
def home():
    return "Welcome to ZooZone Flask App!"

@app.route('/membres')
def get_membres():
    membres = mongo.db.Membres.find({}, {"_id": 0, "name": 1})  # 0 means exclude field, 1 means include field
    result = [membre for membre in membres]
    return jsonify(result)