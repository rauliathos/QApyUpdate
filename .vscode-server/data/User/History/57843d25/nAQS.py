from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import os

app = Flask(__name__) # Declare Flask object

app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv("DATABASE_URI") # Set the connection string to connect to a database
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False 
db = SQLAlchemy(app) # Declare SQLAlchemy object

