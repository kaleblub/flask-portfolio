from flask import Blueprint, render_template

projects_bp = Blueprint('projects_bp', __name__, template_folder="templates/projects")

@projects_bp.route("/")
def projects():
	return render_template("/portfolio.html") #, projects=allProjects)