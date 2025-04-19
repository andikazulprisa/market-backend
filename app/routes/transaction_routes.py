from flask import Blueprint, request
from app.controllers import transaction_controller

bp = Blueprint('transaction_routes', __name__)

@bp.route('/transactions', methods=['POST'])
def create_transaction():
    return transaction_controller.create_transaction(request)

@bp.route('/transactions', methods=['GET'])
def get_all_transactions():
    return transaction_controller.get_all_transactions()
