from application import app, db
from application.models import ToDos



@app.route('/home')
def home():
    return 'This is the home page'




@app.route('/')
def index():
    todo = ToDos.query.first()
    return f'Task: {todo.task} Completed: {todo.completed} '

@app.route('/add')
def add():
    return "Added a new todo"    