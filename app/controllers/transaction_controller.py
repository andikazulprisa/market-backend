from flask import request, jsonify
from app.models.transaction_model import Transaction
from app.models.product_model import Product
from app import db

def create_transaction(request):
    data = request.get_json()
    product_id = data.get('product_id')
    quantity = data.get('quantity')

    if not product_id or not quantity:
        return jsonify({"error": "Data tidak lengkap"}), 400

    product = Product.query.get(product_id)
    if not product or product.stock < quantity:
        return jsonify({"error": "Stok tidak mencukupi atau produk tidak ditemukan"}), 400

    total_price = product.price * quantity
    transaction = Transaction(product_id=product_id, quantity=quantity, total_price=total_price)

    product.stock -= quantity

    db.session.add(transaction)
    db.session.commit()

    return jsonify({"message": "Transaksi berhasil", "total_price": total_price}), 201

def get_all_transactions():
    transactions = Transaction.query.all()
    result = []
    for trx in transactions:
        result.append({
            "id": trx.id,
            "product_id": trx.product_id,
            "quantity": trx.quantity,
            "total_price": trx.total_price,
            "timestamp": trx.timestamp.isoformat()
        })
    return jsonify(result)
