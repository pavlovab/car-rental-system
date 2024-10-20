from flask import Flask

from config import Config
from models import db

app = Flask(__name__)

app.config.from_object(Config)

# Initialize SQLAlchemy Database
db.init_app(app)

if __name__ == '__main__':
    app.run(debug=True)
