from flask import Flask, render_template
from dotenv import load_dotenv

from config import DevConfig
from extensions import db, login_manager, migrate
from models import User

from blueprints.auth.routes import auth_bp
from blueprints.courses.routes import courses_bp
from blueprints.library.routes import library_bp

load_dotenv()

def create_app(config_class=DevConfig):
    app = Flask(__name__)
    app.config.from_object(config_class)

    db.init_app(app)
    login_manager.init_app(app)
    migrate.init_app(app, db)

    app.register_blueprint(auth_bp)
    app.register_blueprint(courses_bp)
    app.register_blueprint(library_bp)

    @app.route("/")
    def home():
        return render_template("home.html")

    return app

if __name__ == "__main__":
    app = create_app()
    app.run()
