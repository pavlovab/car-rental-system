from datetime import datetime
from flask import Blueprint, jsonify, request
from sqlalchemy.exc import IntegrityError

from models.models import Rental, db

rental_bp = Blueprint('rental_bp', __name__, url_prefix='/api')


@rental_bp.route('/rentals', methods=['GET'])
def get_rentals():
    rentals = Rental.query.all()
    all_rentals = [rental.to_dict() for rental in rentals]

    return jsonify(all_rentals)


@rental_bp.route('/rentals/<int:rental_id>', methods=['GET'])
def get_rental(rental_id):
    retrieved_rental = Rental.query.get_or_404(rental_id)

    return jsonify(retrieved_rental.to_dict())


@rental_bp.route('/rentals', methods=['POST'])
def create_rental():
    data = request.get_json()
    try:
        new_rental = Rental(car_id=data['car_id'], customer_id=data['customer_id'],
                            start_date=datetime.strptime(data['start_date'], '%Y-%m-%d'),
                            end_date=datetime.strptime(data['end_date'], '%Y-%m-%d'))
    except KeyError:
        return jsonify({'error': 'Missing required field.'}), 400

    db.session.add(new_rental)
    try:
        db.session.commit()
    except IntegrityError:
        # In case an IntegrityError occurs (a foreign key constraint violation for example)
        db.session.rollback()  # Rollback the transaction to prevent corrupted state
        return jsonify({'error': 'Rental creation failed. Check if IDs for Car and Customer are valid.'}), 400

    return jsonify(new_rental.to_dict()), 201


@rental_bp.route('/rentals/<int:rental_id>', methods=['PUT'])
def update_rental(rental_id):
    retrieved_rental = Rental.query.get_or_404(rental_id)
    data = request.get_json()
    retrieved_rental.start_date = datetime.strptime(data.get('start_date',
                                                             retrieved_rental.start_date.strftime('%Y-%m-%d')),
                                                    '%Y-%m-%d')
    retrieved_rental.end_date = datetime.strptime(data.get('end_date',
                                                           retrieved_rental.end_date.strftime('%Y-%m-%d')), '%Y-%m-%d')
    db.session.commit()

    return jsonify(retrieved_rental.to_dict())


@rental_bp.route('/rentals/<int:rental_id>', methods=['DELETE'])
def delete_rental(rental_id):
    retrieved_rental = Rental.query.get_or_404(rental_id)
    db.session.delete(retrieved_rental)
    db.session.commit()

    return '', 204
