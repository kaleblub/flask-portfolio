from flask import Flask
from flask_cors import CORS
from sqlalchemy.orm import scoped_session

import postModel
from database import SessionLocal, engine

# Import Blueprints
from blueprints.main.routes import main_bp
from blueprints.about.routes import about_bp
from blueprints.blog.routes import blog_bp
from blueprints.contact.routes import contact_bp
from blueprints.projects.routes import projects_bp

def create_app():
	postModel.Base.metadata.create_all(bind=engine)

	app = Flask(__name__)
	CORS(app)

	app.session = scoped_session(SessionLocal)#, scopefunc=_app_ctx_stack.__ident_func__)

	#setup all our dependencies


	# Register Blueprints
	app.register_blueprint(main_bp)
	app.register_blueprint(about_bp, url_prefix='/about')
	app.register_blueprint(blog_bp, url_prefix='/blog')
	app.register_blueprint(contact_bp, url_prefix='/contact')
	app.register_blueprint(projects_bp, url_prefix='/projects')

	return app


if __name__ == "__main__":
	create_app().run(debug=True)