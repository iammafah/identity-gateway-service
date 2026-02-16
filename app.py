from flask import Flask
from extensions import db, migrate
from auth.routes.auth_routes import auth_bp
from database.models.user_model import User
from dotenv import load_dotenv
from flask_cors import CORS
import os

load_dotenv()

def create_app():
    app = Flask(__name__)

    app.config["SQLALCHEMY_DATABASE_URI"] = os.getenv("DATABASE_URL")
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

    # allowed frontend origins
    allowed_origins = [
        "http://127.0.0.1:5000",
        "http://localhost:5000",
        "https://iammafah.site",
        "https://iammafah.github.io"
    ]

    CORS(
        app,
        resources={r"/auth/*": {"origins": allowed_origins}},
        supports_credentials=True
    )

    db.init_app(app)
    migrate.init_app(app, db)

    app.register_blueprint(auth_bp, url_prefix="/auth")

    return app

app = create_app()
