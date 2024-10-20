from flask import Blueprint, jsonify, request
from sqlalchemy.exc import IntegrityError

from models.models import Car, db

car_bp = Blueprint('car_bp', __name__, url_prefix='/api')


@car_bp.route('/cars', methods=['GET'])
def get_cars():
    cars = Car.query.all()
    all_cars = [car.to_dict() for car in cars]

    return jsonify(all_cars)


@car_bp.route('/cars/<int:car_id>', methods=['GET'])
def get_car(car_id):
    retrieved_car = Car.query.get_or_404(car_id)

    return jsonify(retrieved_car.to_dict())


@car_bp.route('/cars', methods=['POST'])
def create_car():
    data = request.get_json()
    try:
        new_car = Car(make=data['make'], model=data['model'], year=data['year'], rental_rate=data['rental_rate'],
                      availability=True, branch_id=data['branch_id'])
    except KeyError:
        return jsonify({'error': 'Missing required field.'}), 400

    db.session.add(new_car)
    try:
        db.session.commit()
        return jsonify(new_car.to_dict()), 201
    except IntegrityError:
        # In case an IntegrityError occurs (a foreign key constraint violation for example)
        db.session.rollback()  # Rollback the transaction to prevent corrupted state
        return jsonify({'error': 'Invalid branch_id field, specified branch does not exist.'}), 400


@car_bp.route('/cars/<int:car_id>', methods=['PUT'])
def update_car(car_id):
    retrieved_car = Car.query.get_or_404(car_id)
    data = request.get_json()
    retrieved_car.make = data.get('make', retrieved_car.make)
    retrieved_car.model = data.get('model', retrieved_car.model)
    retrieved_car.year = data.get('year', retrieved_car.year)
    retrieved_car.rental_rate = data.get('rental_rate', retrieved_car.rental_rate)
    retrieved_car.availability = data.get('availability', retrieved_car.availability)
    retrieved_car.branch_id = data.get('branch_id', retrieved_car.branch_id)
    try:
        db.session.commit()
        return jsonify(retrieved_car.to_dict())
    except IntegrityError:
        # In case an IntegrityError occurs (a foreign key constraint violation for example)
        db.session.rollback()  # Rollback the transaction to prevent corrupted state
        return jsonify({'error': 'Invalid branch_id field, specified branch does not exist.'}), 400


@car_bp.route('/cars/<int:car_id>', methods=['DELETE'])
def delete_car(car_id):
    retrieved_car = Car.query.get_or_404(car_id)
    db.session.delete(retrieved_car)
    try:
        db.session.commit()
        return '', 204
    except IntegrityError:
        # In case an IntegrityError occurs (a foreign key constraint violation for example)
        db.session.rollback()  # Rollback the transaction to prevent corrupted state
        return jsonify({'error': 'Car removal failed. Car is probably still associated with a rental.'}), 400
