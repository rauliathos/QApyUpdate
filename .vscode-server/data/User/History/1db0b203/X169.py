from application import db

db.create_all()


testuser = Human(name="Raul")
db.session.add(testuser)
db.session.commit()