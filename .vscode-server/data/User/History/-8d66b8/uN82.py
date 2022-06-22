from app import db

db.drop_all()
db.create_all()
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False