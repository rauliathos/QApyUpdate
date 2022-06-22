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

@app.route('/read')
def read():
    all_tasks = ToDos.query.all()
    tasks_string = ""
    for task in all_tasks:
        tasks_string += "<br>"+ task.task
    return tasks_string

@app.route('/complete')
def complete():
    first_task = ToDos.query.first()
    first_task.completed= True
    db.session.commit()
    return str(first_task.completed)

@app.route('/incomplete')
def incomplete():
    first_task = ToDos.query.first()
    first_task.completed= False
    db.session.commit()
    return str(first_task.completed)


@app.route('/delete')
def delete():
    del_task = ToDos.query.first()
    db.session.delete(del_task)
    db.session.commit()
    return "Task DELETED"