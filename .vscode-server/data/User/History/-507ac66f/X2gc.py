from application import app, db
from application.models import ToDos


@app.route('/')
@app.route('/home')
def home():
    return 'This is the home page'


sample_todo= ToDos(
    task = "Sample todo",
    completed = False
    )

db.session.add(sample_todo)
db.session.commit()

@app.route('/')
def index():
    todo = ToDos.query.first()
    return f'Task: {todo.task} Completed: {todo.completed} '

@app.route('/add')
def add():
    return "Added a new todo"    