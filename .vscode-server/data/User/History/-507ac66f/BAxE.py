from application import app, db
from application.models import ToDos



@app.route('/home')
def home():
    return 'This is the home page'




@app.route('/')
def index():
    todo = ToDos.query.first()
    return f'Task: {todo.task} Completed: {todo.completed} '

@app.route('/add/<taskName>')
def add(taskName):
    new_task = ToDos(task="Brand New Task", completed=False)
    new_task.task = taskName
    db.session.add(new_task)
    db.session.commit()
    return "Added a new todo"    

