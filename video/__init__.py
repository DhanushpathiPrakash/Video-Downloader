from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_login import LoginManager
import os

app = Flask(__name__)
app.config['MAX_CONTENT_LENGTH'] = 160 * 1024 * 1024
app.config['SECRET_KEY'] = '5791628bb0b13ce0c676dfde280ba245'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'
db = SQLAlchemy(app)
db.create_all()
from video import routes

try:
	os.mkdir(os.path.join(app.root_path, 'static', 'videos'))
except:
	pass


from video import routes
from video import db
db.create_all()
db.session.commit()
