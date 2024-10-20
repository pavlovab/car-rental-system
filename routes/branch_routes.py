from flask import Blueprint, jsonify, request
from sqlalchemy.exc import IntegrityError

from models.models import Branch, db

branch_bp = Blueprint('branch_bp', __name__, url_prefix='/api')


@branch_bp.route('/branches', methods=['GET'])
def get_branches():
    branches = Branch.query.all()

    return jsonify([branch.to_dict() for branch in branches])


@branch_bp.route('/branches/<int:branch_id>', methods=['GET'])
def get_branch(branch_id):
    retrieved_branch = Branch.query.get_or_404(branch_id)

    return jsonify(retrieved_branch.to_dict())


@branch_bp.route('/branches', methods=['POST'])
def create_branch():
    data = request.get_json()
    try:
        new_branch = Branch(name=data['name'], location=data['location'])
    except KeyError:
        return jsonify({'error': 'Missing required field.'}), 400

    db.session.add(new_branch)
    db.session.commit()

    return jsonify(new_branch.to_dict()), 201


@branch_bp.route('/branches/<int:branch_id>', methods=['PUT'])
def update_branch(branch_id):
    retrieved_branch = Branch.query.get_or_404(branch_id)
    data = request.get_json()
    retrieved_branch.name = data.get('name', retrieved_branch.name)
    retrieved_branch.location = data.get('location', retrieved_branch.location)
    db.session.commit()

    return jsonify(retrieved_branch.to_dict())


@branch_bp.route('/branches/<int:branch_id>', methods=['DELETE'])
def delete_branch(branch_id):
    retrieved_branch = Branch.query.get_or_404(branch_id)
    db.session.delete(retrieved_branch)
    try:
        db.session.commit()
        return '', 204
    except IntegrityError:
        # In case an IntegrityError occurs (a foreign key constraint violation for example)
        db.session.rollback()  # Rollback the transaction to prevent corrupted state
        return jsonify({'error': 'Can not delete branch, associated cars still exist.'}), 400
