import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy

# create the extension
db = SQLAlchemy()
# create the app
app = Flask(__name__)
# configure the SQLite database, relative to the app instance folder
app.config['SECRET_KEY'] = 'mijngeheimesleutel'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///showcar.sqlite'
# initialize the app with the extension
db.init_app(app)

# Registreren van de blueprints
from showcar.cars.views import car_blueprint
from showcar.brands.views import car_brand_blueprint

app.register_blueprint(car_blueprint,url_prefix="/cars")
app.register_blueprint(car_brand_blueprint, url_prefix="/brands")