from application import app, db
from application.models import ToDos
from application.forms import TaskForm
from flask import redirect, url_for, render_template, request

@app.route('/')
def index():
    todo = ToDos.query.all()
    # empstr = ""
    # for t in todo:
    #     empstr += f'{t.id} {t.task}  {t.completed} <br>' 
    # return empstr
    return render_template("task.html", todos=todo)

@app.route('/about')
def about():
    return render_template("about.html")


@app.route('/add', methods =[ 'GET','POST'])
def add():
    form = TaskForm()
    if request.method == 'POST':
        if form.validate_on_submit():
            taskData = ToDos(
                task = form.task.data,
                completed = form.completed.data
            )
            db.session.add(taskData)
            db.session.commit()
            return redirect(url_for('index'))
    return render_template('addtask.html', form=form)

@app.route('/complete/<int:id>')
def complete(id):
    todo = ToDos.query.get(id)
    todo.completed = True
    db.session.commit()
    return redirect(url_for('index'))

@app.route('/incomplete/<int:id>')
def incomplete(id):
    todo = ToDos.query.get(id)
    todo.completed = False
    db.session.commit()
    return redirect(url_for('index'))

@app.route('/update/<int:task>/<newtask>')
def update(task, newtask):
    todo = ToDos.query.get(task)
    todo.task = newtask
    db.session.commit()
    return render_template(url_for('index'))

@app.route('/delete/<int:id>')
def delete(id):
    todo = ToDos.query.get(id)
    db.session.delete(todo)
    db.session.commit()
    return redirect(url_for('index'))
