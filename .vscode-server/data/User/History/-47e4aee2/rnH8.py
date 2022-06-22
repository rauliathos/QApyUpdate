from application import db

#db.drop_all()
db.create_all()


sample_todo= ToDos(
    task = "Sample todo",
    completed = False
    )

db.session.add(sample_todo)
db.session.commit()