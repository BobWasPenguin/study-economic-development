from flask import Blueprint

auth_bp = Blueprint("auth", __name__, url_prefix="/auth")
courses_bp = Blueprint("courses", __name__, url_prefix="/courses")
library_bp = Blueprint("library", __name__, url_prefix="/library")
