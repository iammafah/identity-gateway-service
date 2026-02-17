from flask import Flask  # Flask app create karne ke liye
from extensions import db, migrate  # database aur migration instances
from auth.routes.auth_routes import auth_bp  # auth blueprint
from database.models.user_model import User  # user model import
from dotenv import load_dotenv  # env load karne ke liye
from flask_cors import CORS  # CORS support
import os  # environment variables read karne ke liye

load_dotenv()  # .env file load

def create_app():
    app = Flask(__name__)  # Flask app instance

    app.config["SQLALCHEMY_DATABASE_URI"] = os.getenv("DATABASE_URL")  # DB connection
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False  # warning avoid

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
    )  # CORS config

    db.init_app(app)  # DB initialize
    migrate.init_app(app, db)  # migrations initialize

    app.register_blueprint(auth_bp, url_prefix="/auth")  # auth routes register

    @app.route("/health")  # uptime monitoring endpoint
    def health():
        return {"status": "ok"}, 200  # simple response

    return app  # app return

app = create_app()  # app instance create
