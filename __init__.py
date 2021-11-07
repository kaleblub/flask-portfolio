''' Initialize Flask App With Imports '''
from flask import Flask
from flask_cors import CORS
from sqlalchemy.orm import scoped_session

''' Custom Imports '''
import config # Used For Configuration Settings
from database import SessionLocal, engine
from forms import ContactForm
from static.scripts import compile_sass_to_css # Used while creating the app

def create_app():
	''' Create Flask App '''

	# Get Configuration Settings From 'config.py'
	configSettings = config.DevelopmentConfig

	# Initiate the Flask App
	app = Flask(__name__)
	CORS(app)

	# Configure The Flask App With The Configuration Settings
	app.config.from_object(configSettings)

	# Start The App Local Session In The App
	app.session = scoped_session(SessionLocal)
	
	# Compile SCSS Files Into 'main.css'
	compile_sass_to_css(configSettings.sassMap)

	''' Setup Dependencies '''
	with app.app_context():
		# Import Blueprints From The Routes
		from blueprints.home.routes import home_bp
		from blueprints.about.routes import about_bp
		from blueprints.blog.routes import blog_bp
		# from blueprints.contact.routes import contact_bp
		from blueprints.projects.routes import projects_bp

		''' Register Blueprints '''
		app.register_blueprint(home_bp)
		app.register_blueprint(about_bp, url_prefix='/about')
		app.register_blueprint(blog_bp, url_prefix='/blog')
		# app.register_blueprint(contact_bp, url_prefix='/contact')
		app.register_blueprint(projects_bp, url_prefix='/projects')

	return app