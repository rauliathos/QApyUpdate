from application import db

db.create_all()


testuser = Users(name="Raul")
db.session.add(testuser)
db.session.commit()