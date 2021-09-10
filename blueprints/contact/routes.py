from flask import Blueprint, render_template

# Get the Contact Form Modal to be accessed from every page
def getContactModal():
	contactModalHTML=[]
	with open('blueprints/contact/templates/contact/contactModal.html', 'r') as f:
	    content = f.read()
	    contactModalHTML.append(content)
	return content

contact_bp = Blueprint('contact_bp', __name__, template_folder="templates/contact")

@contact_bp.route("/")
def showContact():
	return render_template("/contact.html")