from flask import render_template, request, redirect
from werkzeug.utils import redirect
from taskmaster import app, db
from taskmaster.models import Todo

@app.route('/', methods=["GET", "POST"])
def index():
    if request.method == "POST":
        try:
            task = Todo(name=request.form['name'])
            db.session.add(task)
            db.session.commit()
        except:
            return "Could not add task"
    tasks = Todo.query.order_by(Todo.created).all()
    return render_template('index.html', tasks=tasks)

@app.route('/delete/<int:id>')
def delete(id):
    task = Todo.query.filter_by(id=id).first()
    try:
        db.session.delete(task)
        db.session.commit()
        return redirect('/')
    except:
        return "Cannot Delete Record"
    