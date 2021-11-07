"""Initialize Flask app as Application Factory."""
from flask import Flask
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()  # Initialize Database

def init_app():
   """Construct the core application."""
   app = Flask(__name__, instance_relative_config=False)
   app.config.from_object("config.Config")  # Import configuration

   # Initialize Plugins
   db.init_app(app)

   with app.app_context():

      # Import routes
      from . import routes  

      # Create database tables for our data models
      db.create_all()  

      return app