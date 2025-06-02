from flask import Flask, render_template, request
from dotenv import load_dotenv
import datetime as dt

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
        # Simply render the dashboard template without any query parameters.
        # Users will be able to submit the form to /dashboard to fetch data.
        return render_template("home.html",
                               title="Dashboard",
                               chapters_count=20,
                               cases_count=6,
                               indicators=[],
                               news_items=[],
                               countries=[("ID", "Indonesia"), ("US", "United States"), ("VN", "Vietnam")],
                               current_country=None,
                               now=dt.datetime.utcnow)

    @app.route("/dashboard")
    def dashboard():
        # Get the selected country code (default to "ID" if none provided)
        country = request.args.get("country", "ID")

        # TODO: Replace these placeholders with real API calls.
        indicators = [
            {"label": "GDP (USD Bn)",       "value": "1 188"},
            {"label": "Inflation Rate (%)", "value": "2.8"},
            {"label": "Unemployment (%)",   "value": "4.3"},
            {"label": "Gini Index",         "value": "38.7"},
            {"label": "FDI Inflow (Bn)",    "value": "15.2"},
            {"label": "HDI",                "value": "0.72"},
        ]

        news_items = [
            {
                "title":   "Central Bank Holds Rates Steady",
                "url":     "https://example.com/article1",
                "image":   "https://source.unsplash.com/800x600?economics",
                "summary": "Officials signalled a wait-and-see approach as core inflation stabilises.",
                "source":  "Reuters"
            },
            {
                "title":   "Export Growth Surges in Q1",
                "url":     "https://example.com/article2",
                "image":   "https://source.unsplash.com/800x600?trade",
                "summary": "Merchandise exports jumped 15% year-on-year, driven by electronics and agriculture.",
                "source":  "Bloomberg"
            },
            {
                "title":   "Foreign Direct Investment Rises",
                "url":     "https://example.com/article3",
                "image":   "https://source.unsplash.com/800x600?investment",
                "summary": "FDI inflows for the first half of the year reached $20 billion, up 10% from last year.",
                "source":  "Financial Times"
            },
        ]

        countries = [
            ("ID", "Indonesia"),
            ("US", "United States"),
            ("VN", "Vietnam"),
            # Add more (code, name) tuples as needed
        ]

        return render_template("home.html",
                               title="Dashboard",
                               chapters_count=20,
                               cases_count=6,
                               indicators=indicators,
                               news_items=news_items,
                               countries=countries,
                               current_country=country,
                               now=dt.datetime.utcnow)

    return app

if __name__ == "__main__":
    app = create_app()
    app.run()
