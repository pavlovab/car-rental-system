from flask import Blueprint, jsonify, request
from sqlalchemy.exc import IntegrityError

from models.models import Customer, db

customer_bp = Blueprint('customer_bp', __name__, url_prefix='/api')


@customer_bp.route('/customers', methods=['GET'])
def get_customers():
    customers = Customer.query.all()

    return jsonify([customer.to_dict() for customer in customers])


@customer_bp.route('/customers/<int:customer_id>', methods=['GET'])
def get_customer(customer_id):
    retrieved_customer = Customer.query.get_or_404(customer_id)

    return jsonify(retrieved_customer.to_dict())


@customer_bp.route('/customers', methods=['POST'])
def create_customer():
    data = request.get_json()
    try:
        new_customer = Customer(name=data['name'], email=data['email'], phone=data['phone'])
    except KeyError:
        return jsonify({'error': 'Missing required field.'}), 400

    db.session.add(new_customer)
    db.session.commit()

    return jsonify(new_customer.to_dict()), 201


@customer_bp.route('/customers/<int:customer_id>', methods=['PUT'])
def update_customer(customer_id):
    retrieved_customer = Customer.query.get_or_404(customer_id)
    data = request.get_json()
    retrieved_customer.name = data.get('name', retrieved_customer.name)
    retrieved_customer.email = data.get('email', retrieved_customer.email)
    retrieved_customer.phone = data.get('phone', retrieved_customer.phone)
    db.session.commit()

    return jsonify(retrieved_customer.to_dict())


@customer_bp.route('/customers/<int:customer_id>', methods=['DELETE'])
def delete_customer(customer_id):
    retrieved_customer = Customer.query.get_or_404(customer_id)
    db.session.delete(retrieved_customer)
    try:
        db.session.commit()
        return '', 204
    except IntegrityError:
        # In case an IntegrityError occurs (a foreign key constraint violation for example)
        db.session.rollback()  # Rollback the transaction to prevent corrupted state
        return jsonify({'error': 'Customer removal failed. Customer is still probably associated with a rental.'}), 400
