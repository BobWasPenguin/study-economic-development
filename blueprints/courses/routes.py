from flask import render_template, abort
from flask_login import login_required

from models import Module, Chapter
from blueprints.courses import courses_bp

@courses_bp.route("/")
@login_required
def list_modules():
    modules = Module.query.all()
    return render_template("courses/modules.html", modules=modules)

@courses_bp.route("/<int:module_id>")
@login_required
def module_detail(module_id):
    module = Module.query.get_or_404(module_id)
    return render_template("courses/module_detail.html", module=module)

@courses_bp.route("/<int:module_id>/chapter/<int:chapter_id>")
@login_required
def chapter_detail(module_id, chapter_id):
    chapter = Chapter.query.filter_by(id=chapter_id, module_id=module_id).first_or_404()
    return render_template("courses/chapter_detail.html", chapter=chapter)
