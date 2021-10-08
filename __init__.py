"""Initialize Flask App"""
from flask import Flask
from flask_cors import CORS
from sqlalchemy.orm import scoped_session
import sass

# Import 
import config
from database import startLocalSession, startEngine
from forms import ContactForm 

# Map scss source files to css destination files
sassMap = {"./static/scss/app.scss": "./static/css/main.css"}

def compile_sass_to_css(sass_map):
    for source, dest in sass_map.items():
        with open(dest, "w") as outfile:
            outfile.write(sass.compile(filename=source))
        print(f"{source} compiled to {dest}")

def create_app():
	"""Create Flask App"""

	# Get App Configuration Settings
	configSettings = config.DevelopmentConfig

	# Initiate the App
	app = Flask(__name__)
	CORS(app)

	# Set The Configuration Settings
	app.config.from_object(configSettings)

	# Initiate The Database Engine and Start The Local Session
	app.session = scoped_session(startLocalSession(startEngine(configSettings.SQLALCHEMY_DATABASE_URL)))#, scopefunc=_app_ctx_stack.__ident_func__)
	# postModel.Base.metadata.create_all(bind=engine)

	# Compile SCSS Files Into main.css
	compile_sass_to_css(sassMap)

	# Setup Dependencies
	with app.app_context():
		# Import Blueprints From The Routes
		from blueprints.home.routes import home_bp
		from blueprints.about.routes import about_bp
		from blueprints.blog.routes import blog_bp
		from blueprints.contact.routes import contact_bp
		from blueprints.projects.routes import projects_bp


		# Register Blueprints
		app.register_blueprint(home_bp)
		app.register_blueprint(about_bp, url_prefix='/about')
		app.register_blueprint(blog_bp, url_prefix='/blog')
		app.register_blueprint(contact_bp, url_prefix='/contact')
		app.register_blueprint(projects_bp, url_prefix='/projects')

	return app