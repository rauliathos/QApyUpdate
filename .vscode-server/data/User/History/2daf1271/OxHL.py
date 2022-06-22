from application import db


class ToDos(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    task = db.Column(db.String(30))
    completed = db.Column(db.Boolean, default=False)


sample_todo= ToDos(
    task = "Sample todo",
    completed = False
    )

db.session.add(sample_todo)
db.session.commit()