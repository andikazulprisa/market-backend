from flask import Blueprint, request
from app.controllers import product_controller

bp = Blueprint('product_routes', __name__)

@bp.route('/products', methods=['POST'])
def create_product():
    return product_controller.create_product()

@bp.route('/products', methods=['GET'])
def get_all_products():
    return product_controller.get_all_products()

@bp.route('/products/<int:product_id>', methods=['GET'])
def get_product_by_id(product_id):
    return product_controller.get_product_by_id(product_id)

@bp.route('/products/<int:product_id>', methods=['PUT'])
def update_product(product_id):
    return product_controller.update_product(product_id, request)

@bp.route('/products/<int:product_id>', methods=['DELETE'])
def delete_product(product_id):
    return product_controller.delete_product(product_id)
