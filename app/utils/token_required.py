import jwt
from functools import wraps
from flask import request, jsonify, current_app
from app.models.user_model import User


def token_required(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        token = None

        if 'Authorization' in request.headers:
            bearer = request.headers['Authorization']
            token = bearer.split(" ")[1] if "" in bearer else bearer

        if not token:
            return jsonify({'message': 'Token tidak ditemukan'}), 401

        try:
            data = jwt.decode(token, current_app.config['SECRET_KEY'], algorithms=['HS256'])
            current_user = User.query.get(data['user_id'])
            if not current_user:
                return jsonify({'message': 'User tidak ditemukan'}), 401
        except jwt.ExpiredSignatureError:
            return jsonify({'message': 'Token telah kadaluarsa'}), 401
        except jwt.InvalidTokenError:
            return jsonify({'message': 'Token tidak valid'}), 401
        
        return f(current_user, *args, **kwargs)

    return decorated