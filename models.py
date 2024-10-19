from db import db

MAX_NAME_LEN = 70
MAX_LOCATION_LEN = 300
MAX_MAKE_LEN = 50
MAX_MODEL_LEN = 50
MAX_USER_INFO_LEN = 100
MAX_TELEPHONE_NUM_LEN = 20


class Branch(db.Model):
    __tablename__ = 'branches'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(MAX_NAME_LEN), nullable=False)
    location = db.Column(db.String(MAX_LOCATION_LEN), nullable=False)
    # Create a bidirectional relationship with the Car model, a.k.a. add a 'branch' attribute to the Car model, which
    # allows access to the branch that a specific car is associated with.
    # Fetch the cars for a particular branch only when you access 'branch.cars' via 'lazy=True' instead of loading
    # the cars when the Branch object is first queried
    cars = db.relationship('Car', backref='branch', lazy=True)


class Car(db.Model):
    __tablename__ = 'cars'

    id = db.Column(db.Integer, primary_key=True)
    make = db.Column(db.String(MAX_MAKE_LEN), nullable=False)
    model = db.Column(db.String(MAX_MODEL_LEN), nullable=False)
    year = db.Column(db.Integer, nullable=False)
    rental_rate = db.Column(db.Float, nullable=False)
    availability = db.Column(db.Boolean, default=True)
    branch_id = db.Column(db.Integer, db.ForeignKey('branches.id'), nullable=False)
    # Create a 'car' attribute in the Rental model that refers back to the Car instance associated with that rental
    rentals = db.relationship('Rental', backref='car', lazy=True)


class Customer(db.Model):
    __tablename__ = 'customers'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(MAX_USER_INFO_LEN), nullable=False)
    email = db.Column(db.String(MAX_USER_INFO_LEN), unique=True, nullable=False)
    phone = db.Column(db.String(MAX_TELEPHONE_NUM_LEN), nullable=False)
    rentals = db.relationship('Rental', backref='customer', lazy=True)


class Rental(db.Model):
    __tablename__ = 'rentals'

    id = db.Column(db.Integer, primary_key=True)
    car_id = db.Column(db.Integer, db.ForeignKey('cars.id'), nullable=False)
    customer_id = db.Column(db.Integer, db.ForeignKey('customers.id'), nullable=False)
    start_date = db.Column(db.DateTime, nullable=False)
    end_date = db.Column(db.DateTime, nullable=False)
