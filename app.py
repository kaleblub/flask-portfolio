from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS

# from extensions import database, commands

# Import Blueprints
from blueprints.main.routes import main_bp
from blueprints.about.routes import about_bp
from blueprints.blog.routes import blog_bp
from blueprints.contact.routes import contact_bp
from blueprints.projects.routes import projects_bp

def create_app():

	app = Flask(__name__)
	db = SQLAlchemy()
	app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
	app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
	CORS(app)
	db.init_app(app)

	#setup all our dependencies
	# database.init_app(app)
	# commands.init_app(app)

	# Register Blueprints
	app.register_blueprint(main_bp)
	app.register_blueprint(about_bp, url_prefix='/about')
	app.register_blueprint(blog_bp, url_prefix='/blog')
	app.register_blueprint(contact_bp, url_prefix='/contact')
	app.register_blueprint(projects_bp, url_prefix='/projects')

	return app


if __name__ == "__main__":
	create_app().run(debug=True)