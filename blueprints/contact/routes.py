from flask import Blueprint, render_template

contact_bp = Blueprint('contact_bp', __name__, template_folder="templates/contact")

@contact_bp.route("/")
def showContact():
	return render_template("/contact.html")