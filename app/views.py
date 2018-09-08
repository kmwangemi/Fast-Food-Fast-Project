from flask import request, jsonify, make_response
from app import app
import os

import uuid

from app.models import User, Orders

user_info = User()
order_model = Orders()


def create_order(current_user):
    """endpoint to create a new order"""
    try:
        data = request.get_json()
        if not data or not data['title'].strip():
            return jsonify({"message": "Name cannot be empty!"}), 401
        for req in order_model.orders.values():
            if data['title'].strip() == req['title']:
                return jsonify({"message": "Sorry!! data exists!"}), 401
        # update request
        user_id = current_user['username']
        create = order_model.add_orders(data['title'].strip(), data['description'], user_id)
                                                
        return jsonify({
            "message": "Order created", 'order': create }), 201
    except Exception as e:
        return jsonify({
            "Error": "Error!, check you are sending correct information"
        }), 400

@app.route('/api/v1/orders', methods=['GET'])
#@login_required
def get_all_orders(current_user):
    """Gets all orders"""
    all_orders = []
    for order in order_model.orders.values():
        all_orders.append(order)
    return jsonify(all_orders)