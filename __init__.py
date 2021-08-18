from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS

import click
from flask.cli import with_appcontext
from flask_jwt_extended import JWTManager
from werkzeug.security import generate_password_hash

db = SQLAlchemy()

def create_app():
	app = Flask(__name__)
	app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
	app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
	CORS(app)
	db.init_app(app)




	@click.command(name='create_admin')   
	    @with_appcontext
	    def create_admin():
	        admin=User(email="kaleblub@gmail.com",password="Ironassassin1")
	        admin.password = generate_password_hash(admin.password,'sha256',salt_length=12)
	        db.session.add(admin)
	        db.session.commit()
	 
	    app.cli.add_command(create_admin)


	return app