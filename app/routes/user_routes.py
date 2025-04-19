from flask import Blueprint, request, jsonify
from app.controllers import user_controller
from app.models.user_model import User


bp = Blueprint('user_routes', __name__)

@bp.route('/register', methods=['POST'])
def register():
    return user_controller.register_user(request)

@bp.route('/users', methods=['GET'])
def get_users():
    return user_controller.get_all_users()

@bp.route('/users/<int:user_id>', methods=['GET'])
def get_user_by_id(user_id):
    return user_controller.get_user_by_id(user_id)

@bp.route('/users/<int:user_id>', methods=['PUT'])
def update_user(user_id):
    return user_controller.update_user(user_id, request)

@bp.route('/users/<int:user_id>', methods=['DELETE'])
def delete_user(user_id):
    return user_controller.delete_user(user_id)

@bp.route('/login', methods=['POST'])
def login():
    return user_controller.login_user(request)