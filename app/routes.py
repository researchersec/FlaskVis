from flask import Blueprint, jsonify
import json

main = Blueprint('main', __name__)

@main.route('/data')
def data():
    with open('latest.json', 'r') as f:
        data = json.load(f)
    return jsonify(data)
