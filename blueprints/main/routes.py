from flask import Blueprint, render_template

main_bp = Blueprint('main_bp', __name__, template_folder="templates/main")

@main_bp.route("/")
def index():
	return render_template("/home.html")

