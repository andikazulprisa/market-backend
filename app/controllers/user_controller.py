from flask import jsonify, request, current_app
from app.models.user_model import User
from app import db
import jwt
import datetime
from app.utils.token_required import token_required

def register_user(request):
    data = request.get_json()
    name = data.get('name')
    email = data.get('email')
    password = data.get('password')

    if not all([name, email, password]):
        return jsonify({"error": "Data tidak lengkap"}), 400

    user = User(name=name, email=email, password=password)
    db.session.add(user)
    db.session.commit()

    return jsonify({"message": "User berhasil didaftarkan"}), 201

@token_required
def get_all_users(current_user):
    users = User.query.all()
    result = []
    for user in users:
        result.append({
            "id": user.id,
            "name": user.name,
            "email": user.email
        })
    return jsonify(result)

def login_user(request):
    data = request.get_json()
    email = data.get('email')
    password = data.get('password')

    if not email or not password:
        return jsonify({"error": "Email dan password harus diisi"}), 400
    
    user = User.query.filter_by(email=email).first()
    if not user or user.password != password:
        return jsonify({"error": "Email atau password salah"}), 401
    
    payload = {
        'user_id': user.id,
        'exp': datetime.datetime.utcnow() + datetime.timedelta(hours=2)
    }
    token = jwt.encode(payload, current_app.config['SECRET_KEY'], algorithm='HS256')

    return jsonify({"token": token}), 200

def get_user_by_id(user_id):
    user = User.query.get(user_id)
    if not user:
        return jsonify({"error": "User tidak ditemukan"}), 404

    return jsonify({
        "id": user.id,
        "name": user.name,
        "email": user.email
    })

def update_user(user_id, request):
    user = User.query.get(user_id)
    if not user:
        return jsonify({"error": "User tidak ditemukan"}), 404
    
    data = request.get_json()
    user.name = data.get('name', user.name)
    user.email = data.get('email', user.email)
    user.password = data.get('password', user.password)

    db.session.commit()

    return jsonify({"message": "User berhasil diperbarui"}), 200

def delete_user(user_id):
    user = User.query.get(user_id)
    if not user:
        return jsonify({"error": "User tidak ditemukan"}), 404

    db.session.delete(user)
    db.session.commit()

    return jsonify({"message": "User berhasil dihapus"}), 200