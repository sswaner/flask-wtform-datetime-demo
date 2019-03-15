import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SECRET_KEY'] = os.urandom(192)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://test:test@localhost:5432/test'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

from wtform_datetime.datetime.views import datetime_blueprint

app.register_blueprint(datetime_blueprint)
