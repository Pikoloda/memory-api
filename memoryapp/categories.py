from flask import jsonify
from memoryapp import app

categories_list = [
    {'category_id': 1, 'name': 'Dom'},
    {'category_id': 2, 'name': 'Rodzina'}
]


@app.route('/categories', methods=['GET'])
def categories():
    return jsonify(categories_list)