from memoryapp import app
from memoryapp.repository import *
from flask import jsonify


@app.route('/categories/<int:category_id>/cards', methods=['GET'])
def cards(category_id):
    return jsonify(get_cards(category_id))

