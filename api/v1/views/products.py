#!/usr/bin/env python3
""" Routes for Product functionalities """
from models.product import Product
from models.user import User
from models import storage
from flask import request, abort, jsonify
from api.v1.views import app_views


@app_views.route('/products', methods=['POST'], strict_slashes=False)
def register_product():
    """ Creates new product """
    data = request.get_json()

    required_fields = ["name", "description", "price"]

    missing = [field for field in required_fields if field not in data]

    if missing:
        return jsonify({"error": f"Missing fields: {', '.join(missing)}"}), 400

    new_product = Product(**data)
    new_product.save()

    return jsonify(new_product.to_dict()), 201


@app_views.route('/products', methods=['GET'], strict_slashes=False)
def get_all_products():
    """ Retrieves all orders of a customer """
    
    all_products = storage.all(Product)
    products = [product.to_dict() for product in all_products.values()]

    return jsonify(products), 200


@app_views.route('/products/<product_id>', methods=['GET'], strict_slashes=False)
def get_product(product_id):
    """ Retrieves a specific product """
    
    product = storage.get(Product, product_id)
    if not product:
        abort(404)

    return jsonify(product.to_dict()), 200


@app_views.route('/products/<product_id>', methods=['PUT'], strict_slashes=False)
def update_product(product_id):
    """ Update product """
    data = request.get_json()
    if not data:
        abort(400, description="Not a valid JSON")

    product = storage.get(Product, product_id)
    if not product:
        abort(404)


    ignore = ['created_at', 'updated_at', 'id']

    for key, value in data.items():
        if key not in ignore:
            setattr(product, key, value)
    product.save()

    return jsonify({
        "message": "Product updated successfully",
        "product": product.to_dict()
    }), 200


@app_views.route('/products/<product_id>', methods=['DELETE'], strict_slashes=False)
def delete_product(product_id):
    """ Deletes a product from the database """

    product = storage.get(Product, product_id)
    if not product:
        abort(404)

    storage.delete(product)
    storage.save()

    return jsonify({"message": "Product deleted successfully"}), 200
