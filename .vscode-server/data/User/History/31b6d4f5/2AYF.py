from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import os

app = Flask(__name__) # Declare Flask object



app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///data.db"
db = SQLAlchemy(app) # Declare SQLAlchemy object

class ToDo(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    task = db.Column(db.String(30))
    completed = db.Column(db.Boolean, default_value=False)

sample_todo= Todos(task = "Sample todo",completed = False)

if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=5000)