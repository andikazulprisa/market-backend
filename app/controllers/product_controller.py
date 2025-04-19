from flask import request, jsonify
from app.models.product_model import Product
from app import db


def create_product():
    data = request.get_json()
    print("DATA DITERIMA:", data)

    name = data.get('name')
    description = data.get('description')
    price = data.get('price')
    stock = data.get('stock', 0)
    print(name, description, price, stock)
    if not name or price is None:
        return jsonify({'error': 'Data tidak lengkap'}), 400
    
    try:
        product = Product(name=name, description=description, price=price, stock=stock)
        db.session.add(product)
        db.session.commit()
        return jsonify({'message': 'Produk berhasil ditambahkan'}), 201
    except Exception as e:
        print("Error saat menambahkan produk:", e)
        return jsonify({'error': 'Gagal menambahkan produk'}), 500


def get_all_products():
    products = Product.query.all()
    result = []
    for product in products:
        result.append({
            'id': product.id,
            'name': product.name,
            'description': product.description,
            'price': product.price,
            'stock': product.stock
        })
    return jsonify(result), 200

def get_product_by_id(product_id):
    product = Product.query.get(product_id)
    if not product:
        return jsonify({'error': 'Produk tidak ditemukan'}), 404
    
    return jsonify({
        'id': product.id,
        'name': product.name,
        'description': product.description,
        'price': product.price,
        'stock': product.stock
    })

def update_product(product_id, request):
    product = Product.query.get(product_id)
    if not product:
        return jsonify({'error': 'Produk tidak ditemukan'}), 404
    
    data = request.get_json()
    product.name = data.get('name', product.name)
    product.description = data.get('description', product.description)
    product.price = data.get('price', product.price)
    product.stock = data.get('stock', product.stock)

    db.session.commit()

    return jsonify({'message': 'Produk berhasil diperbarui'}), 200

def delete_product(product_id):
    product = Product.query.get(product_id)
    if not product:
        return jsonify({'error': 'Produk tidak ditemukan'}), 404
    
    db.session.delete(product)
    db.session.commit()

    return jsonify({'message': 'Produk berhasil dihapus'}), 200