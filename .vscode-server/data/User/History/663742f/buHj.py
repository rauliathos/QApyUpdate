from application import db

class ToDo(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    task = db.Column(db.String(30))
    completed = db.Column(db.Boolean, default_value=False)

sample_todo= Todos(task = "Sample todo",completed = False)