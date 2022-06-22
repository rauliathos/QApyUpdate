from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__) # Declare Flask object
app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///data.db"

db = SQLAlchemy(app) # Declare SQLAlchemy object

class ToDo(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    task = db.Column(db.String(30))
    completed = db.Column(db.Boolean, default=False)

db.create_all()

sample_todo= ToDos(
    task = "Sample todo",
    completed = False
    )

db.session.add(sample_todo)
db.session.commit()

@app.route('/')
def index():
    todo = Todos.query.first()
    return todo.task

@app.route('/add')
def add():
    return "added a new todo"

if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=5000)