from flask import Blueprint, render_template

about_bp = Blueprint("about_bp", __name__, template_folder="templates/about")

@about_bp.route("/")
def about():
	return render_template("/about.html")