from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from dotenv import load_dotenv
import os


db = SQLAlchemy()
migrate = Migrate()

def create_app():
    load_dotenv()  # baca .env

    app = Flask(__name__)
    app.config.from_object('app.config.Config')

    db.init_app(app)
    migrate.init_app(app, db)

    from app.models.user_model import User  # Import model di sini agar migrasi dapat mengenali model

    from app.routes.user_routes import bp as user_bp  # Import blueprint di sini agar dapat digunakan
    app.register_blueprint(user_bp)
    
    from app.models import product_model, transaction_model  # Import model di sini agar migrasi dapat mengenali model

    from app.routes.product_routes import bp as product_bp  # Import blueprint di sini agar dapat digunakan
    app.register_blueprint(product_bp)

    from app.routes.transaction_routes import bp as transaction_bp  # Import blueprint di sini agar dapat digunakan
    app.register_blueprint(transaction_bp)

    return app

