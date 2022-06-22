from application import app, db
from application.models import Games


@app.route('/')
@app.route('/home')
def home():
    return 'This is the home page'


@app.route('/add')
def add():
    new_game = Games(name="New Game")
    db.session.add(new_game)
    db.session.commit()
    return "Added new game to database"

@app.route('/read')
def read():
    all_games = Games.query.all()
    games_string = ""
    for game in all_games:
        games_string += "<br>"+ game.name
    return games_string

@app.route('/update/<name>')
def update(name):
    first_game = Games.query.first()
    first_game.name = name
    db.session.commit()
    return first_game.name



'''
@app.route('/delete')
def delete():
    game_to_be_deleted = Games.query.first()
    
    game_to_be_deleted.name = name.delete()
    db.session.delete(game_to_be_deleted)
    db.session.commit()
    return f"{name} was deleted!"
'''


@app.route('/delete/<name>')
def delete(name):
    game_to_be_deleted = Games.query.first()
 
    game_to_be_deleted.name = name.replace(game_to_be_deleted.name, "")()
    db.session.delete(game_to_be_deleted)
    db.session.commit()
    return f"{name} was deleted!"


@app.route('/count')
def count():
    total = Games.query.count()
    return str(total)
