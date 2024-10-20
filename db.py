from flask import Blueprint, jsonify
from flask_sqlalchemy import SQLAlchemy

# Initialize SQLAlchemy Database object
db = SQLAlchemy()

db_bp = Blueprint('db_bp', __name__, url_prefix='/api')


@db_bp.route('/reset-db')
def reset_db():
    db.drop_all()
    db.create_all()

    return jsonify('Database reset successfully!'), 200

