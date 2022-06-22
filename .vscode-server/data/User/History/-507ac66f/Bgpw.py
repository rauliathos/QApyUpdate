from application import app, db
from application.models import Games


@app.route('/')
@app.route('/home')
def home():
    return 'This is the home page'