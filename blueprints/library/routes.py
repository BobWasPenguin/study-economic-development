from flask import render_template
from flask_login import login_required

from models import Resource
from blueprints import library_bp

@library_bp.route("/")
@login_required
def list_resources():
    resources = Resource.query.all()
    return render_template("library/resources.html", resources=resources)
