from flask import Flask
from sqlalchemy import event
from sqlalchemy.engine import Engine

from config import Config
from db import db_bp
from models.models import db
from routes.car_routes import car_bp
from routes.customer_routes import customer_bp
from routes.rental_routes import rental_bp
from routes.branch_routes import branch_bp

app = Flask(__name__)

app.config.from_object(Config)

# Initialize SQLAlchemy Database
db.init_app(app)


# Add enforcement for foreign keys, so that the creation of a car, for example, with a non-existent branch_id is not
# possible
@event.listens_for(Engine, "connect")
def enable_sqlite_fks(dbapi_connection, connection_record):
    cursor = dbapi_connection.cursor()
    cursor.execute("PRAGMA foreign_keys=ON")
    cursor.close()


# Register Blueprints for routes
app.register_blueprint(db_bp)
app.register_blueprint(car_bp)
app.register_blueprint(customer_bp)
app.register_blueprint(rental_bp)
app.register_blueprint(branch_bp)

with app.app_context():
    db.create_all()

if __name__ == '__main__':
    app.run(debug=True)
